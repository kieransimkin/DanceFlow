"""Synthetic jobs verify consent, confinement, receipts and process lifecycle."""
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import sys
import threading
import time
from types import SimpleNamespace

from jsonschema import ValidationError
import pytest

from danceflow_agents import runtime
from danceflow_agents.runtime import ComponentJobs, RuntimeConfig, temporary_preflight


JOB_SCRIPT = r'''
import argparse
from pathlib import Path
import sys
import time
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("--output")
parser.add_argument("--delay", type=float, default=0)
parser.add_argument("--exit-code", type=int, default=0)
parser.add_argument("--log-bytes", type=int, default=0)
parser.add_argument("--output-kind", choices=["file", "dir"], default="file")
args = parser.parse_args()
print("fixture-started", flush=True)
if args.log_bytes:
    print("x" * args.log_bytes, flush=True)
time.sleep(args.delay)
if args.output:
    output = Path(args.output)
    if args.output_kind == "dir":
        output.mkdir(exist_ok=True)
        output = output / "fixture.txt"
    output.write_text("synthetic output", encoding="utf-8")
print("fixture-finished", flush=True)
raise SystemExit(args.exit_code)
'''


@pytest.fixture
def jobs(tmp_path):
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (workspace / "input.txt").write_text("synthetic input", encoding="utf-8")
    source = tmp_path / "trusted-runtime"
    source.mkdir()
    (source / "fixture.py").write_text(JOB_SCRIPT, encoding="utf-8")
    configuration = tmp_path / "runtimes.json"
    configuration.write_text(json.dumps({
        "schema": "danceflow.runtimes.v1",
        "max_jobs": 2,
        "components": {"workflowmoves": {"source_root": str(source), "python": sys.executable}},
    }), encoding="utf-8")
    config = RuntimeConfig({"workflowmoves"}, configuration)
    manager = ComponentJobs(workspace, config)
    descriptor = {
        "script": "fixture.py", "prefix": [], "effects": ["write"], "timeout_seconds": 20,
        "partial_exit_codes": [2],
        "input_schema": {
            "type": "object", "additionalProperties": False, "required": ["input"],
            "properties": {
                "input": {"type": "string"}, "output": {"type": "string"},
                "delay": {"type": "number", "minimum": 0, "default": 0},
                "exit_code": {"type": "integer", "default": 0},
                "log_bytes": {"type": "integer", "minimum": 0, "default": 0},
                "output_kind": {"type": "string", "enum": ["file", "dir"], "default": "file"},
            },
        },
        "parameters": {
            "input": {"kind": "input_file", "positional": 0},
            "output": {"kind": "output_file", "flag": "--output"},
            "delay": {"kind": "value", "flag": "--delay"},
            "exit_code": {"kind": "value", "flag": "--exit-code"},
            "log_bytes": {"kind": "value", "flag": "--log-bytes"},
            "output_kind": {"kind": "value", "flag": "--output-kind"},
        },
    }
    yield SimpleNamespace(manager=manager, config=config, descriptor=descriptor, workspace=workspace, source=source)
    manager.close()


def start(jobs, arguments=None, *, descriptor=None, permissions=None):
    return jobs.manager.start("workflowmoves", "synthetic", descriptor or jobs.descriptor,
                              arguments or {"input": "input.txt", "output": "result.txt"},
                              {"write": True} if permissions is None else permissions)


def finished(jobs, job_id, timeout=10):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        receipt = jobs.manager.status(job_id)
        if "finished_at" in receipt:
            return receipt
        time.sleep(0.02)
    pytest.fail("Synthetic job did not finish within its test deadline")


def wait_for_live_log(jobs, job_id, text="fixture-started", timeout=5):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        result = jobs.manager.logs(job_id)
        if text in result["text"]:
            return result
        time.sleep(0.02)
    pytest.fail("Flushed live output was not readable before the job completed")


def test_temporary_preflight_is_atomic_and_leaves_no_probe(tmp_path):
    parent = tmp_path / "temporary-parent"
    temporary_preflight(parent)
    assert parent.is_dir() and list(parent.iterdir()) == []


def test_job_runs_canonical_argv_and_retains_inspectable_receipt(jobs):
    output = "name with spaces; literal.txt"
    launched = start(jobs, {"input": "input.txt", "output": output})
    receipt = finished(jobs, launched["job_id"])
    assert receipt["status"] == "completed" and receipt["returncode"] == 0
    assert receipt["arguments"]["input"] == str(jobs.workspace / "input.txt")
    assert (jobs.workspace / output).read_text("utf-8") == "synthetic output"
    retained = json.loads((jobs.workspace / receipt["receipt"]).read_text("utf-8"))
    assert retained == receipt
    assert "fixture-finished" in jobs.manager.logs(receipt["job_id"])["text"]
    assert jobs.manager.list_jobs()[0]["job_id"] == receipt["job_id"]
    receipt["arguments"]["input"] = "caller mutation"
    assert jobs.manager.status(receipt["job_id"])["arguments"]["input"] != "caller mutation"


def test_live_logs_and_cancel_are_available_while_process_runs(jobs):
    launched = start(jobs, {"input": "input.txt", "output": "later.txt", "delay": 30})
    job_id = launched["job_id"]
    assert wait_for_live_log(jobs, job_id)["untrusted_data"] is True
    assert jobs.manager.status(job_id)["status"] == "running"
    assert jobs.manager.cancel(job_id)["status"] == "cancelled"
    receipt = finished(jobs, job_id)
    assert receipt["status"] == "cancelled"
    assert not (jobs.workspace / "later.txt").exists()


@pytest.mark.parametrize("code, status", [(0, "completed"), (2, "needs_review"), (7, "failed")])
def test_exit_status_does_not_hide_partial_or_failed_results(jobs, code, status):
    launched = start(jobs, {"input": "input.txt", "exit_code": code})
    receipt = finished(jobs, launched["job_id"])
    assert receipt["returncode"] == code
    assert receipt["status"] == status


def test_failed_publication_records_uncertain_external_outcome_without_retry(jobs):
    descriptor = deepcopy(jobs.descriptor)
    descriptor["effects"] = ["publication"]
    launched = start(jobs, {"input": "input.txt", "exit_code": 7}, descriptor=descriptor,
                     permissions={"publication": True})
    receipt = finished(jobs, launched["job_id"])
    assert receipt["status"] == "failed"
    assert receipt["external_outcome"].startswith("unknown")
    assert jobs.manager.logs(receipt["job_id"])["text"].count("fixture-started") == 1


def test_job_timeout_terminates_owned_process(jobs):
    descriptor = deepcopy(jobs.descriptor)
    descriptor["timeout_seconds"] = 1
    launched = start(jobs, {"input": "input.txt", "delay": 30}, descriptor=descriptor)
    receipt = finished(jobs, launched["job_id"])
    assert receipt["status"] == "timed_out"
    assert receipt["returncode"] != 0


def test_log_storage_and_reads_remain_bounded(jobs, monkeypatch):
    monkeypatch.setattr(runtime, "MAX_LOG_BYTES", 1024)
    launched = start(jobs, {"input": "input.txt", "log_bytes": 4096})
    receipt = finished(jobs, launched["job_id"])
    assert receipt["log_bytes"] == 1024 and receipt["log_truncated"] is True
    first = jobs.manager.logs(receipt["job_id"], offset=0, limit=256)
    second = jobs.manager.logs(receipt["job_id"], offset=first["next_offset"], limit=65536)
    assert first["next_offset"] == 256 and second["next_offset"] == 1024
    for offset, limit in [(-1, 10), (False, 10), (0, 0), (0, 65537), (0, True)]:
        with pytest.raises(ValueError):
            jobs.manager.logs(receipt["job_id"], offset=offset, limit=limit)


@pytest.mark.parametrize("permissions", [{}, {"write": False}, {"write": "yes"}, {"write": 1}, {"shell": True}])
def test_missing_or_malformed_consent_prevents_launch(jobs, permissions):
    with pytest.raises(ValueError):
        start(jobs, permissions=permissions)
    assert jobs.manager.list_jobs() == []
    assert not (jobs.workspace / "result.txt").exists()


@pytest.mark.parametrize("permissions", [[], False, "", 0, "write"])
def test_permissions_must_be_an_object_even_for_read_only_operations(jobs, permissions):
    descriptor = deepcopy(jobs.descriptor)
    descriptor["effects"] = []
    with pytest.raises(ValueError, match="Permissions"):
        start(jobs, {"input": "input.txt"}, descriptor=descriptor, permissions=permissions)
    assert jobs.manager.list_jobs() == []


def test_operator_read_only_binding_cannot_be_overridden(jobs):
    jobs.config.data["components"]["workflowmoves"]["read_only"] = True
    with pytest.raises(ValueError, match="read_only"):
        start(jobs)


def test_existing_output_is_never_overwritten(jobs):
    existing = jobs.workspace / "result.txt"
    existing.write_text("retain original evidence", encoding="utf-8")
    with pytest.raises(ValueError, match="new output"):
        start(jobs)
    assert existing.read_text("utf-8") == "retain original evidence"


def test_waiting_launch_rechecks_output_after_another_job_finishes(jobs, monkeypatch):
    # Gate B immediately before launch-lock acquisition. Before the fix, its
    # prepare() has already observed an absent output here. A can then create
    # that file and release its reservation before B resumes with stale checks.
    waiting = threading.Event()
    resume = threading.Event()
    original_lock = jobs.manager._lock

    class PausedLaunchLock:
        def __enter__(self):
            if threading.current_thread().name.startswith("waiting-launch"):
                waiting.set()
                if not resume.wait(10):
                    raise TimeoutError("Test did not release the waiting launch")
            return original_lock.__enter__()

        def __exit__(self, *args):
            return original_lock.__exit__(*args)

    monkeypatch.setattr(jobs.manager, "_lock", PausedLaunchLock())
    script = JOB_SCRIPT.replace(
        'output.write_text("synthetic output", encoding="utf-8")',
        'output.write_text(Path(args.input).read_text("utf-8"), encoding="utf-8")',
    )
    (jobs.source / "fixture.py").write_text(script, encoding="utf-8")
    (jobs.workspace / "second.txt").write_text("must not replace first evidence", encoding="utf-8")
    with ThreadPoolExecutor(max_workers=1, thread_name_prefix="waiting-launch") as pool:
        blocked = pool.submit(start, jobs, {"input": "second.txt", "output": "same.txt"})
        try:
            assert waiting.wait(5), "Competing launch did not reach the lock"
            first = start(jobs, {"input": "input.txt", "output": "same.txt"})
            assert finished(jobs, first["job_id"])["status"] == "completed"
            assert (jobs.workspace / "same.txt").read_text("utf-8") == "synthetic input"
        finally:
            resume.set()
        with pytest.raises(ValueError, match="new output"):
            blocked.result(timeout=5)
    assert (jobs.workspace / "same.txt").read_text("utf-8") == "synthetic input"
    assert len(jobs.manager.list_jobs()) == 1


@pytest.mark.parametrize("parameter", ["input", "output"])
def test_top_level_paths_cannot_escape_selected_workspace(jobs, parameter):
    outside = jobs.workspace.parent / "outside.txt"
    outside.write_text("outside evidence", encoding="utf-8")
    arguments = {"input": "input.txt", "output": "result.txt", parameter: str(outside)}
    with pytest.raises(ValueError, match="outside"):
        start(jobs, arguments)
    assert outside.read_text("utf-8") == "outside evidence"


def symlink_or_skip(link: Path, target: Path, *, directory=False):
    try:
        link.symlink_to(target, target_is_directory=directory)
    except (NotImplementedError, OSError) as exc:
        pytest.skip(f"Symlinks unavailable in this test environment: {exc}")


def test_symlinked_output_parent_cannot_escape_workspace(jobs):
    outside = jobs.workspace.parent / "outside"
    outside.mkdir()
    symlink_or_skip(jobs.workspace / "escape", outside, directory=True)
    with pytest.raises(ValueError, match="outside"):
        start(jobs, {"input": "input.txt", "output": "escape/result.txt"})
    assert list(outside.iterdir()) == []


def test_script_must_stay_in_operator_selected_source_root(jobs):
    outside = jobs.source.parent / "outside.py"
    outside.write_text("raise AssertionError('must never execute')", encoding="utf-8")
    descriptor = deepcopy(jobs.descriptor)
    descriptor["script"] = "../outside.py"
    with pytest.raises(ValueError, match="outside its configured source root"):
        start(jobs, descriptor=descriptor)


def test_active_job_limit_prevents_another_launch(jobs):
    jobs.config.data["max_jobs"] = 1
    active = start(jobs, {"input": "input.txt", "output": "first.txt", "delay": 30})
    wait_for_live_log(jobs, active["job_id"])
    with pytest.raises(ValueError, match="Maximum active"):
        start(jobs, {"input": "input.txt", "output": "second.txt"})


@pytest.mark.parametrize("parent_first", [True, False])
def test_active_output_reservations_include_parent_and_child_paths(jobs, parent_first):
    directory = deepcopy(jobs.descriptor)
    directory["parameters"]["output"].update(kind="output_dir", allow_existing=True)
    if parent_first:
        active = start(jobs, {"input": "input.txt", "output": "result", "output_kind": "dir", "delay": 30}, descriptor=directory)
        next_arguments, next_descriptor = {"input": "input.txt", "output": "result/child.txt"}, jobs.descriptor
    else:
        active = start(jobs, {"input": "input.txt", "output": "result/child.txt", "delay": 30})
        next_arguments, next_descriptor = {"input": "input.txt", "output": "result", "output_kind": "dir"}, directory
    wait_for_live_log(jobs, active["job_id"])
    with pytest.raises(ValueError, match="already owns"):
        start(jobs, next_arguments, descriptor=next_descriptor)


def test_writable_input_state_is_reserved_like_an_output(jobs):
    state = jobs.workspace / "state"
    state.mkdir()
    descriptor = deepcopy(jobs.descriptor)
    descriptor["parameters"]["input"].update(kind="input_dir", writable=True)
    active = start(jobs, {"input": "state", "delay": 30}, descriptor=descriptor)
    wait_for_live_log(jobs, active["job_id"])
    with pytest.raises(ValueError, match="already owns"):
        start(jobs, {"input": "input.txt", "output": "state/result.txt"})


def test_restart_does_not_claim_or_cancel_an_unowned_process(jobs):
    job_id = "a" * 32
    directory = jobs.workspace / ".danceflow/jobs" / job_id
    directory.mkdir(parents=True)
    (directory / "receipt.json").write_text(json.dumps({
        "schema": "danceflow.component-job.v1", "job_id": job_id,
        "status": "running", "pid": 1,
    }), encoding="utf-8")
    assert jobs.manager.status(job_id)["status"] == "unknown_after_restart"
    assert jobs.manager.cancel(job_id)["status"] == "unknown_after_restart"


def test_retained_receipt_symlink_cannot_read_outside_workspace(jobs):
    job_id = "b" * 32
    directory = jobs.workspace / ".danceflow/jobs" / job_id
    directory.mkdir(parents=True)
    outside = jobs.workspace.parent / "outside-receipt.json"
    outside.write_text(json.dumps({
        "schema": "danceflow.component-job.v1", "job_id": job_id,
        "status": "completed", "private": "outside evidence",
    }), encoding="utf-8")
    symlink_or_skip(directory / "receipt.json", outside)
    with pytest.raises(ValueError, match="outside"):
        jobs.manager.status(job_id)


def test_shutdown_cancels_owned_jobs_and_joins_monitor_threads(jobs):
    launched = start(jobs, {"input": "input.txt", "delay": 30})
    wait_for_live_log(jobs, launched["job_id"])
    jobs.manager.close()
    assert jobs.manager.status(launched["job_id"])["status"] == "cancelled"
    assert all(not thread.is_alive() for thread in jobs.manager._threads.values())
    assert not jobs.manager._processes
    with pytest.raises(ValueError, match="closed"):
        start(jobs)


@pytest.mark.parametrize("value", [
    {"components": {"unknown": {}}},
    {"components": {"workflowmoves": {"command": "arbitrary"}}},
    {"max_jobs": 0},
    {"max_jobs": 5},
    {"components": {"workflowmoves": {"read_only": "yes"}}},
])
def test_runtime_configuration_rejects_unknown_or_invalid_fields(tmp_path, value):
    configuration = tmp_path / "invalid.json"
    configuration.write_text(json.dumps(value), encoding="utf-8")
    with pytest.raises(ValidationError):
        RuntimeConfig({"workflowmoves"}, configuration)


@pytest.mark.parametrize("key", ["source_root", "models_dir"])
def test_runtime_code_and_model_paths_must_be_absolute(tmp_path, key):
    configuration = tmp_path / "invalid.json"
    configuration.write_text(json.dumps({"components": {"workflowmoves": {key: "relative/path"}}}), encoding="utf-8")
    with pytest.raises(ValueError, match="absolute"):
        RuntimeConfig({"workflowmoves"}, configuration)
