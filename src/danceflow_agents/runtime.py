"""Configured canonical runtimes and bounded, inspectable component jobs.

This is an adapter boundary, not an operating-system sandbox. Native project
files can contain additional paths; review them under the owning tool's rules.
"""
from __future__ import annotations

import atexit
from datetime import datetime, timezone
from importlib import metadata
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
import threading
import uuid

from jsonschema import Draft202012Validator

DISTRIBUTIONS = {
    "stemlab": "danceflow-stemlab", "dancerudiments": "dancerudiments",
    "framerudiments": "framerudiments", "keywordmoves": "keywordmoves",
    "rastermoves": "rastermoves", "likenessforge": "likenessforge",
    "pixelcue": "pixelcue", "prismmoves": "prismmoves", "thumbmoves": "thumbmoves",
}
MAX_LOG_BYTES = 8 * 1024 * 1024
PERMISSIONS = ("write", "inference", "download", "network", "publication", "training")


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def temporary_preflight(parent: Path) -> None:
    """Test exact create/read/atomic-rename/delete access before a child starts."""
    parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".access-probe-", dir=parent) as directory:
        source = Path(directory) / "probe"
        source.write_bytes(b"danceflow-access-probe")
        if source.read_bytes() != b"danceflow-access-probe":
            raise OSError("Temporary-directory readback failed")
        target = source.with_name("renamed")
        source.replace(target)
        if target.read_bytes() != b"danceflow-access-probe":
            raise OSError("Temporary-directory rename readback failed")
        target.unlink()


class RuntimeConfig:
    """Only the operator's startup configuration can select executable/code roots."""
    def __init__(self, components: set[str], path: Path | None = None):
        self.components = components
        self.data: dict = {}
        if path is not None:
            if path.stat().st_size > 1024 * 1024:
                raise ValueError("Runtime configuration exceeds one MiB")
            self.data = json.loads(path.read_text(encoding="utf-8-sig"))
        schema = {
            "type": "object", "additionalProperties": False,
            "properties": {
                "schema": {"const": "danceflow.runtimes.v1"},
                "node": {"type": "string", "minLength": 1},
                "powershell": {"type": "string", "minLength": 1},
                "max_jobs": {"type": "integer", "minimum": 1, "maximum": 4},
                "components": {
                    "type": "object", "propertyNames": {"enum": sorted(components)},
                    "additionalProperties": {
                        "type": "object", "additionalProperties": False,
                        "properties": {
                            "python": {"type": "string", "minLength": 1},
                            "source_root": {"type": "string", "minLength": 1},
                            "models_dir": {"type": "string", "minLength": 1},
                            "read_only": {"type": "boolean"},
                        },
                    },
                },
                "wordpress": {
                    "type": "object", "additionalProperties": False,
                    "required": ["site_url", "credential_path"],
                    "properties": {
                        "site_url": {"type": "string", "pattern": "^https://"},
                        "credential_path": {"type": "string", "minLength": 1},
                    },
                },
            },
        }
        Draft202012Validator(schema).validate(self.data)
        for entry in self.data.get("components", {}).values():
            for key in ("source_root", "models_dir"):
                if key in entry and not Path(entry[key]).is_absolute():
                    raise ValueError(f"Runtime {key} must be absolute")
        if "wordpress" in self.data:
            from urllib.parse import urlsplit
            wp = self.data["wordpress"]
            url = urlsplit(wp["site_url"])
            if not url.hostname or url.username or url.password or url.query or url.fragment:
                raise ValueError("WordPress site_url must be an HTTPS site without credentials, query or fragment")
            if not Path(wp["credential_path"]).is_absolute():
                raise ValueError("WordPress credential_path must be absolute")

    def component(self, name: str) -> dict:
        if name not in self.components:
            raise ValueError("Unknown DanceFlow component")
        return dict(self.data.get("components", {}).get(name, {}))

    def python(self, name: str) -> str:
        return self.component(name).get("python", sys.executable)

    def availability(self, name: str) -> dict:
        entry = self.component(name)
        if entry.get("python") and Path(entry["python"]).resolve() != Path(sys.executable).resolve():
            return {"status": "configured_unverified", "reason": "Separate Python selected; package/API checked on invocation"}
        if name == "workflowmoves":
            root = entry.get("source_root")
            return {"status": "configured_unverified" if root and Path(root).is_dir() else "unavailable",
                    "reason": "WorkflowMoves requires an operator-selected trusted source_root"}
        distribution = DISTRIBUTIONS.get(name)
        if distribution:
            try:
                return {"status": "installed_unverified", "distribution": distribution,
                        "version": metadata.version(distribution),
                        "reason": "Distribution metadata observed; engine and optional backends not executed"}
            except metadata.PackageNotFoundError:
                pass
        return {"status": "unavailable", "reason": "Optional runtime not observed in this Python environment"}

    def environment(self, name: str, workspace: Path) -> dict[str, str]:
        env = dict(os.environ)
        env.update(PYTHONIOENCODING="utf-8", PYTHONUNBUFFERED="1")
        entry = self.component(name)
        root = Path(entry.get("models_dir") or
                    (Path(entry["source_root"]) / "models" if entry.get("source_root") else workspace / name / "models"))
        # Provisioning is still explicit. These paths only localise caches when
        # the operation's own consent gates permit model use/downloads.
        env.update(HF_HOME=str(root / "huggingface"), TORCH_HOME=str(root / "torch"),
                   XDG_CACHE_HOME=str(root / "cache"))
        return env


class ComponentJobs:
    def __init__(self, workspace: Path | None, config: RuntimeConfig):
        self.workspace = workspace.resolve(strict=True) if workspace else None
        self.config = config
        self._jobs: dict[str, dict] = {}
        self._processes: dict[str, subprocess.Popen] = {}
        self._threads: dict[str, threading.Thread] = {}
        self._lock = threading.RLock()
        self._reserved: set[str] = set()
        self._closed = False
        atexit.register(self.close)

    def _inside(self, name: str, *, exists: bool = False) -> Path:
        if self.workspace is None:
            raise ValueError("Set DANCEFLOW_WORKSPACE or --workspace first")
        path = Path(name)
        resolved = (path if path.is_absolute() else self.workspace / path).resolve(strict=exists)
        if not resolved.is_relative_to(self.workspace):
            raise ValueError("Path is outside the selected workspace")
        return resolved

    def _job_directory(self, job_id: str) -> Path:
        if not re.fullmatch(r"[0-9a-f]{32}", job_id):
            raise ValueError("Invalid job ID")
        return self._inside(str(Path(".danceflow/jobs") / job_id))

    def _save(self, job: dict) -> None:
        directory = self._job_directory(job["job_id"])
        handle, name = tempfile.mkstemp(prefix=".receipt-", suffix=".tmp", dir=directory)
        temporary = Path(name)
        try:
            with os.fdopen(handle, "w", encoding="utf-8") as stream:
                stream.write(json.dumps(job, indent=2) + "\n")
                stream.flush()
                os.fsync(stream.fileno())
            temporary.replace(directory / "receipt.json")
        finally:
            temporary.unlink(missing_ok=True)

    def prepare(self, component: str, descriptor: dict, arguments: dict) -> tuple[list[str], dict, list[str]]:
        from .cli_operations import build_arguments, validated_arguments

        normalized, outputs = validated_arguments(descriptor, arguments), []
        for name, parameter in descriptor.get("parameters", {}).items():
            if name not in normalized or normalized[name] is None:
                continue
            kind = parameter.get("kind", "value")
            if kind not in ("input_file", "input_dir", "output_file", "output_dir"):
                continue
            values = normalized[name] if parameter.get("multiple") else [normalized[name]]
            resolved_values = []
            for value in values:
                path = self._inside(value, exists=kind.startswith("input"))
                if kind == "input_file" and not path.is_file() and not (parameter.get("allow_directory") and path.is_dir()):
                    raise ValueError(f"{name} requires an input file")
                if kind == "input_dir" and not path.is_dir():
                    raise ValueError(f"{name} requires an input directory")
                if kind.startswith("output"):
                    if path.exists() and not parameter.get("allow_existing"):
                        raise ValueError(f"{name} must be a new output path; existing evidence is preserved")
                    if path.exists() and ((kind == "output_dir" and not path.is_dir()) or
                                          (kind == "output_file" and not path.is_file())):
                        raise ValueError(f"{name} has the wrong output path type")
                    outputs.append(str(path))
                elif parameter.get("writable"):
                    outputs.append(str(path))
                resolved_values.append(str(path))
            normalized[name] = resolved_values if parameter.get("multiple") else resolved_values[0]
        args = build_arguments(descriptor, normalized)
        if descriptor.get("runtime") == "powershell":
            wp = self.config.data.get("wordpress")
            if not wp:
                raise ValueError("Configure the WordPress site and credential binding at server startup")
            command = [self.config.data.get("powershell", "pwsh"), "-NoLogo", "-NoProfile", "-NonInteractive", "-File"]
        else:
            command = [self.config.python(component)]
        if descriptor.get("script"):
            root_value = self.config.component(component).get("source_root")
            if not root_value:
                raise ValueError("Configure this component's trusted source_root at server startup")
            root = Path(root_value).resolve(strict=True)
            script = (root / descriptor["script"]).resolve(strict=True)
            if not script.is_relative_to(root) or not script.is_file():
                raise ValueError("Script is outside its configured source root")
            command.append(str(script))
        else:
            command.extend(["-I", "-m", descriptor["module"]])
        command.extend(args)
        if descriptor.get("runtime") == "powershell":
            command.extend(["-SiteUrl", wp["site_url"], "-CredentialPath", wp["credential_path"]])
        return command, normalized, outputs

    def start(self, component: str, operation: str, descriptor: dict,
              arguments: dict, permissions: dict | None = None) -> dict:
        from .cli_operations import effects_for_arguments
        if permissions is not None and not isinstance(permissions, dict):
            raise ValueError("Permissions must be an object of known boolean fields")
        supplied = permissions or {}
        if set(supplied) - set(PERMISSIONS) or any(type(value) is not bool for value in supplied.values()):
            raise ValueError("Permissions must be known boolean fields")
        needed = set(effects_for_arguments(descriptor, arguments))
        missing = sorted(name for name in needed if not supplied.get(name, False))
        if missing:
            raise ValueError("This operation requires explicit permission flags: " + ", ".join(missing))
        if self.config.component(component).get("read_only") and needed:
            raise ValueError("Component is configured read_only")
        if self.workspace is None:
            raise ValueError("Configure a workspace before running component jobs")
        with self._lock:
            if self._closed:
                raise ValueError("Job manager is closed")
            if len(self._processes) >= self.config.data.get("max_jobs", 1):
                raise ValueError("Maximum active jobs reached; poll or cancel an owned job first")
            # Validate output existence under the same lock as reservation and
            # launch: an earlier job may finish while this request waits.
            command, normalized, outputs = self.prepare(component, descriptor, arguments)
            if any(Path(path).is_relative_to(Path(owned)) or Path(owned).is_relative_to(Path(path))
                   for path in outputs for owned in self._reserved):
                raise ValueError("An active job already owns an output path")
            parent = self._inside(".danceflow/jobs")
            temporary_preflight(parent)
            for output in outputs:
                temporary_preflight(Path(output).parent)
            job_id = uuid.uuid4().hex
            directory = parent / job_id
            directory.mkdir()
            job = {
                "schema": "danceflow.component-job.v1", "job_id": job_id,
                "component": component, "operation": operation, "status": "starting",
                "created_at": now(), "arguments": normalized, "permissions": supplied,
                "runtime": self.config.availability(component), "output_paths": outputs,
                "receipt": str(directory.relative_to(self.workspace) / "receipt.json"),
                "limits": ["Exit status is not creative review, backend completeness, public verification or host acceptance.",
                           "Native project/manifest contents are trusted configuration; top-level path checks are not an OS sandbox.",
                           "No automatic retries; inspect partial artifacts and reconcile uncertain external actions."],
            }
            self._jobs[job_id] = job
            self._save(job)
            try:
                process = subprocess.Popen(command, cwd=self.workspace,
                                           env=self.config.environment(component, self.workspace),
                                           stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           start_new_session=os.name != "nt",
                                           creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0)
            except OSError as exc:
                job.update(status="unavailable", error=type(exc).__name__, finished_at=now())
                self._save(job)
                return dict(job)
            self._processes[job_id] = process
            self._reserved.update(outputs)
            job.update(status="running", started_at=now(), pid=process.pid)
            self._save(job)
            timeout = min(max(int(descriptor.get("timeout_seconds", 3600)), 1), 86400)
            thread = threading.Thread(target=self._monitor, args=(job_id, descriptor, timeout), daemon=True,
                                      name="danceflow-component-job")
            self._threads[job_id] = thread
            thread.start()
            return dict(job)

    def _monitor(self, job_id: str, descriptor: dict, timeout: int) -> None:
        process = self._processes[job_id]
        job = self._jobs[job_id]
        log = self._job_directory(job_id) / "output.log"
        count = 0
        def consume() -> None:
            nonlocal count
            with log.open("wb") as stream:
                while True:
                    chunk = process.stdout.read1(8192)
                    if not chunk:
                        break
                    remaining = MAX_LOG_BYTES - min(count, MAX_LOG_BYTES)
                    if remaining:
                        stream.write(chunk[:remaining])
                        stream.flush()
                    count += len(chunk)
        reader = threading.Thread(target=consume, daemon=True)
        reader.start()
        try:
            code = process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            with self._lock:
                job["status"] = "timed_out"
            self._terminate(process)
            code = process.wait(timeout=15)
        reader.join(timeout=10)
        with self._lock:
            if job["status"] == "running":
                job["status"] = ("completed" if code == 0 else
                                 "needs_review" if code in descriptor.get("partial_exit_codes", []) else "failed")
            job.update(returncode=code, finished_at=now(), log_bytes=min(count, MAX_LOG_BYTES),
                       log_truncated=count > MAX_LOG_BYTES)
            if "publication" in descriptor.get("effects", []) and job["status"] != "completed":
                job["external_outcome"] = "unknown; re-read the destination and retained receipts before another attempt"
            self._save(job)
            self._reserved.difference_update(job["output_paths"])
            self._processes.pop(job_id, None)
        if process.stdout:
            process.stdout.close()

    @staticmethod
    def _terminate(process: subprocess.Popen) -> None:
        if process.poll() is not None:
            return
        if os.name == "nt":
            subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10, check=False)
        else:
            try:
                os.killpg(process.pid, signal.SIGTERM)
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass

    def status(self, job_id: str) -> dict:
        with self._lock:
            if job_id in self._jobs:
                return json.loads(json.dumps(self._jobs[job_id]))
        receipt = self._inside(str(self._job_directory(job_id) / "receipt.json"), exists=True)
        if receipt.stat().st_size > 1024 * 1024:
            raise ValueError("Job receipt exceeds one MiB")
        job = json.loads(receipt.read_text(encoding="utf-8"))
        if job.get("job_id") != job_id or job.get("schema") != "danceflow.component-job.v1":
            raise ValueError("Invalid retained job receipt")
        if job.get("status") in ("starting", "running"):
            job.update(status="unknown_after_restart", reason="No owned process in this server session; reconcile saved evidence")
        return job

    def logs(self, job_id: str, offset: int = 0, limit: int = 16000) -> dict:
        self.status(job_id)
        if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= 65536:
            raise ValueError("Use a nonnegative byte offset and a limit from 1 to 65536")
        path = self._job_directory(job_id) / "output.log"
        if not path.exists():
            return {"job_id": job_id, "text": "", "next_offset": offset}
        path = self._inside(str(path), exists=True)
        with path.open("rb") as stream:
            stream.seek(offset)
            data = stream.read(limit)
        return {"job_id": job_id, "text": data.decode("utf-8", errors="replace"),
                "next_offset": offset + len(data), "untrusted_data": True}

    def cancel(self, job_id: str) -> dict:
        self._job_directory(job_id)
        with self._lock:
            process = self._processes.get(job_id)
            if process is None:
                return self.status(job_id)
            self._jobs[job_id]["status"] = "cancelled"
            self._save(self._jobs[job_id])
        self._terminate(process)
        return self.status(job_id)

    def list_jobs(self, limit: int = 50) -> list[dict]:
        if type(limit) is not int or not 1 <= limit <= 100:
            raise ValueError("Job limit must be 1..100")
        directory = self._inside(".danceflow/jobs")
        if not directory.exists():
            return []
        receipts = sorted(directory.glob("*/receipt.json"), key=lambda path: path.stat().st_mtime, reverse=True)
        return [self.status(path.parent.name) for path in receipts[:limit]]

    def close(self) -> None:
        with self._lock:
            if self._closed:
                return
            self._closed = True
            active = list(self._processes)
        for job_id in active:
            self.cancel(job_id)
        for thread in list(self._threads.values()):
            thread.join(timeout=20)
