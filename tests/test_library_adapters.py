"""Adapter contracts use synthetic library doubles; no production host or inference."""
import base64
import importlib.machinery
import json
from pathlib import Path
import shutil
import sys
from types import SimpleNamespace

import pytest
from jsonschema import Draft202012Validator

from danceflow_agents.library_adapters import LibraryAdapters, MAX_THUMBNAIL_BYTES


def test_discovery_does_not_import_or_execute_optional_libraries(monkeypatch, tmp_path):
    monkeypatch.setattr("danceflow_agents.library_adapters.importlib.util.find_spec",
                        lambda name: importlib.machinery.ModuleSpec(name, None))
    monkeypatch.setattr("danceflow_agents.library_adapters.importlib.import_module",
                        lambda name: pytest.fail("Discovery imported a native module"))
    adapters = LibraryAdapters(tmp_path)
    assert adapters.available("dancerudiments")["status"] == "installed_unverified"
    assert adapters.available("dancerudiments")["runtime"]["api_checked"] is False
    operations = adapters.operations()
    for items in operations.values():
        for item in items:
            Draft202012Validator.check_schema(item["input_schema"])
    operations["dancerudiments"].clear()
    assert adapters.operations()["dancerudiments"]
    for name in ("mediaslide", "dancevault", "epk-social-metadata"):
        assert adapters.operations()[name] == []
        assert adapters.available(name)["status"] == "integration_only"
    assert "Range/resume" in " ".join(adapters.integration_descriptors()["dancevault"]["limits"])


@pytest.fixture
def rudiments(monkeypatch):
    calls = []
    descriptors = [
        {"name": "example", "description": "Synthetic catalogue fixture", "period_pips": 192, "dimensions": 3},
        {"name": "other", "description": "Other fixture", "period_pips": 64, "dimensions": 3},
    ]
    def sample(name, pip):
        calls.append((name, pip))
        if name != "example":
            raise ValueError("native unknown pattern")
        return SimpleNamespace(as_tuple=lambda: (.125, -.5, .75))
    native = SimpleNamespace(PIPS_PER_BEAT=64, catalogue=lambda: descriptors,
                             sample=sample, __file__="synthetic-native-extension")
    monkeypatch.setitem(sys.modules, "dancerudiments", native)
    return native, calls


def test_native_sample_delegates_signed_pips_and_preserves_period(rudiments):
    _, calls = rudiments
    result = LibraryAdapters(None).run("dancerudiments", "sample", {"name": "example", "pips": [-1, 0, 256]})
    assert calls == [("example", -1), ("example", 0), ("example", 256)]
    assert result["result"]["descriptor"]["period_pips"] == 192
    assert result["result"]["samples"][0] == {"pip": -1, "position": [.125, -.5, .75]}
    assert result["runtime"]["api_checked"] is True
    assert result["status"] == "ok"
    rows = LibraryAdapters(None).run("dancerudiments", "catalogue", {"query": "SYNTHETIC", "limit": 1})
    assert rows["result"]["total"] == 1
    assert rows["result"]["items"][0]["name"] == "example"


@pytest.mark.parametrize("pips", [[True], [1.5], [2**31], [-(2**31)-1], [], [0] * 4097])
def test_native_invalid_pips_are_rejected_before_call(rudiments, pips):
    _, calls = rudiments
    with pytest.raises(ValueError, match="Invalid pips"):
        LibraryAdapters(None).run("dancerudiments", "sample", {"name": "example", "pips": pips})
    assert not calls


def test_native_errors_are_not_motion_fallbacks(rudiments):
    native, _ = rudiments
    adapters = LibraryAdapters(None)
    with pytest.raises(ValueError, match="native unknown pattern"):
        adapters.run("dancerudiments", "sample", {"name": "missing", "pips": [0]})
    native.PIPS_PER_BEAT = 16
    with pytest.raises(RuntimeError, match="64-pip"):
        adapters.run("dancerudiments", "catalogue", {})


def test_missing_optional_package_has_explicit_error(monkeypatch):
    def missing(_):
        raise ModuleNotFoundError("synthetic unavailable dependency")
    monkeypatch.setattr("danceflow_agents.library_adapters.importlib.import_module", missing)
    with pytest.raises(RuntimeError, match="Optional package dancerudiments is unavailable"):
        LibraryAdapters(None).run("dancerudiments", "catalogue", {})


@pytest.fixture
def thumbnail(monkeypatch, tmp_path):
    source = tmp_path / "synthetic.jpg"
    source.write_bytes(b"source-must-not-be-decoded")
    calls = []
    state = {"result": None}
    info = SimpleNamespace(name="fixture-cache", platform="fixture", cache_only_supported=True, notes="Synthetic backend")
    def cached(path, **kwargs):
        calls.append((path, kwargs))
        if isinstance(state["result"], Exception):
            raise state["result"]
        return state["result"]
    native = SimpleNamespace(backend_info=lambda: info, get_cached_thumbnail=cached, __file__="synthetic-thumbmoves")
    monkeypatch.setitem(sys.modules, "thumbmoves", native)
    return source, calls, state


def test_thumbnail_hit_and_miss_are_distinct_without_source_reads(thumbnail, monkeypatch, tmp_path):
    source, calls, state = thumbnail
    monkeypatch.setattr(Path, "read_bytes", lambda _: pytest.fail("Adapter opened the source file"))
    adapters = LibraryAdapters(tmp_path)
    miss = adapters.run("thumbmoves", "cached_thumbnail", {"path": source.name})
    assert miss["status"] == "cache_miss"
    assert miss["result"]["cache_hit"] is False
    assert "data_base64" not in miss["result"]
    state["result"] = SimpleNamespace(data=b"synthetic-thumbnail", size=(3, 2), output_format="PNG", cache_only=True)
    hit = adapters.run("thumbmoves", "cached_thumbnail", {"path": source.name, "output_format": "PNG", "max_size": [16, 12]})
    assert hit["status"] == "ok"
    assert hit["result"]["mime_type"] == "image/png"
    assert base64.b64decode(hit["result"]["data_base64"]) == b"synthetic-thumbnail"
    assert calls[1] == (source, {"max_size": (16, 12), "output_format": "PNG", "quality": 82})


def test_thumbnail_errors_and_size_bounds_are_not_cache_misses(thumbnail, tmp_path):
    source, _, state = thumbnail
    adapters = LibraryAdapters(tmp_path)
    state["result"] = OSError("synthetic cache failure")
    with pytest.raises(OSError, match="synthetic cache failure"):
        adapters.run("thumbmoves", "cached_thumbnail", {"path": source.name})
    state["result"] = SimpleNamespace(data=b"x" * (MAX_THUMBNAIL_BYTES + 1), cache_only=True)
    with pytest.raises(ValueError, match="two-MiB"):
        adapters.run("thumbmoves", "cached_thumbnail", {"path": source.name})
    with pytest.raises(ValueError, match="Invalid max_size"):
        adapters.run("thumbmoves", "cached_thumbnail", {"path": source.name, "max_size": [1025, 1]})


def test_thumbnail_workspace_and_symlink_escape_rejected_before_import(tmp_path, monkeypatch):
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    outside = tmp_path / "outside.jpg"
    outside.write_bytes(b"synthetic")
    (workspace / "escape.jpg").symlink_to(outside)
    monkeypatch.setattr("danceflow_agents.library_adapters.importlib.import_module",
                        lambda name: pytest.fail("Path validation must run before import"))
    for name in ("../outside.jpg", "escape.jpg"):
        with pytest.raises(ValueError, match="outside"):
            LibraryAdapters(workspace).run("thumbmoves", "cached_thumbnail", {"path": name})
    with pytest.raises(ValueError, match="individual file"):
        LibraryAdapters(workspace).run("thumbmoves", "cached_thumbnail", {"path": "."})
    with pytest.raises(ValueError, match="DANCEFLOW_WORKSPACE"):
        LibraryAdapters(None).run("thumbmoves", "cached_thumbnail", {"path": "image.jpg"})


def _node_package(workspace, name, source):
    root = workspace / "node_modules" / name
    root.mkdir(parents=True)
    (root / "package.json").write_text(json.dumps({"name": name, "version": "0.0.0-synthetic-test",
                                                "exports": {".": "./index.cjs", "./server": "./index.cjs"}}))
    (root / "index.cjs").write_text(source)
    return root


@pytest.fixture
def node_adapter(tmp_path):
    if not shutil.which("node"):
        pytest.skip("Node is optional; fixed bridge integration requires it")
    return LibraryAdapters(tmp_path)


def test_node_discovery_only_reads_metadata_and_run_uses_exact_public_export(node_adapter, tmp_path):
    _node_package(tmp_path, "@kieransimkin/dancemoves", """
      console.log('synthetic native diagnostic');
      module.exports = {validatePageConfig: input => ({fromNative: true, input}),
        validateTimingFile: (text, options) => ({text, options}),
        validateMotionCapture: capture => {throw new RangeError('native capture rejection');}};
    """)
    status = node_adapter.available("dancemoves")
    assert status["status"] == "installed_unverified"
    assert status["runtime"]["api_checked"] is False
    result = node_adapter.run("dancemoves", "validate_page_config", {"config": {"bpm": 123}})
    assert result["result"] == {"fromNative": True, "input": {"bpm": 123}}
    assert result["runtime"]["version"] == "0.0.0-synthetic-test"
    assert result["runtime"]["api_checked"] is True
    assert Path(result["runtime"]["entry"]).is_relative_to(tmp_path)
    timing = node_adapter.run("dancemoves", "validate_timing_file", {"text": "[00:00.00]Cue"})
    assert timing["result"]["options"] == {"kind": "cue", "maxBytes": 1024 * 1024}
    with pytest.raises(RuntimeError, match="RangeError: native capture rejection"):
        node_adapter.run("dancemoves", "validate_motion_capture", {"capture": {}})


def test_node_timeline_uses_upstream_clock_and_lyrics_exports(node_adapter, tmp_path):
    _node_package(tmp_path, "react-timeline-sequence", """
      module.exports = {
        validateBeatClock: clock => {if (clock.bpm === 99) throw new Error('native clock rejection'); return clock;},
        phasePipsAt: (clock, seconds) => 1234,
        tempoAtSeconds: (clock, seconds) => 98,
        secondsAtPips: (clock, pips) => 7,
        matchBeat: (clock, seconds, tolerance) => ({seconds, tolerance, actualAnchor: true}),
        beatGrid: (clock, start, end, limit) => [{fromNative: true, start, end, limit}],
        lyricLineStatesAtTime: (lines, words, time, duration) => [{lines, words, time, duration}],
      };
    """)
    clock = {"mode": "fixed", "bpm": 120, "firstBeatSeconds": 0}
    result = node_adapter.run("react-timeline-sequence", "sample_beat_clock", {"clock": clock, "seconds": [1], "pips": [-1]})
    assert result["result"] == {"at_seconds": [{"seconds": 1, "pips": 1234, "bpm": 98}],
                                "at_pips": [{"pips": -1, "seconds": 7}]}
    matched = node_adapter.run("react-timeline-sequence", "match_beat", {"clock": clock, "seconds": .1})
    assert matched["result"] == {"seconds": .1, "tolerance": .15, "actualAnchor": True}
    grid = node_adapter.run("react-timeline-sequence", "beat_grid", {"clock": clock, "start": 0, "end": 2, "limit": 3})
    assert grid["result"][0]["limit"] == 3
    lyrics = node_adapter.run("react-timeline-sequence", "lyric_state", {"lines": [], "seconds": 0, "duration": 1})
    assert lyrics["result"] == [{"lines": [], "words": [], "time": 0, "duration": 1}]
    with pytest.raises(RuntimeError, match="native clock rejection"):
        node_adapter.run("react-timeline-sequence", "sample_beat_clock", {"clock": {**clock, "bpm": 99}, "seconds": [0]})


def test_node_missing_exports_are_explicit_and_no_parent_node_modules_fallback(node_adapter, tmp_path):
    assert node_adapter.available("dancemoves")["status"] == "unavailable"
    _node_package(tmp_path, "@kieransimkin/dancemoves", "module.exports = {};")
    with pytest.raises(RuntimeError, match="lacks required API validatePageConfig"):
        node_adapter.run("dancemoves", "validate_page_config", {"config": {}})
    child = tmp_path / "child"
    child.mkdir()
    with pytest.raises(RuntimeError, match="Optional workspace package is unavailable"):
        LibraryAdapters(child).run("dancemoves", "validate_page_config", {"config": {}})


def test_node_symlink_escape_is_rejected(node_adapter, tmp_path):
    child = tmp_path / "child"
    (child / "node_modules").mkdir(parents=True)
    outside = _node_package(tmp_path, "react-timeline-sequence", "throw new Error('must not run');")
    (child / "node_modules" / "react-timeline-sequence").symlink_to(outside, target_is_directory=True)
    adapters = LibraryAdapters(child)
    assert adapters.available("react-timeline-sequence")["status"] == "unavailable"
    with pytest.raises(RuntimeError, match="outside"):
        adapters.run("react-timeline-sequence", "validate_beat_clock", {"clock": {"mode": "fixed", "bpm": 120, "firstBeatSeconds": 0}})


@pytest.mark.parametrize("stream,size", [("stdout", 5 * 1024 * 1024), ("stderr", 512 * 1024)])
def test_node_native_output_is_bounded_while_reading(node_adapter, tmp_path, stream, size):
    _node_package(tmp_path, "@kieransimkin/dancemoves",
                  f"process.{stream}.write('x'.repeat({size})); module.exports = {{validatePageConfig: x => x}};")
    with pytest.raises(ValueError, match="bounded"):
        node_adapter.run("dancemoves", "validate_page_config", {"config": {}})


def test_node_call_has_a_real_deadline(node_adapter, tmp_path, monkeypatch):
    _node_package(tmp_path, "@kieransimkin/dancemoves", "while (true) {}")
    monkeypatch.setattr("danceflow_agents.library_adapters.NODE_TIMEOUT_SECONDS", .2)
    with pytest.raises(RuntimeError, match="within 0.2 seconds"):
        node_adapter.run("dancemoves", "validate_page_config", {"config": {}})


def test_operation_and_input_bounds_are_checked_without_execution(monkeypatch):
    adapters = LibraryAdapters(None)
    monkeypatch.setattr(adapters, "_node", lambda *args: pytest.fail("Invalid request executed a library"))
    with pytest.raises(ValueError, match="supported component/operation"):
        adapters.run("dancemoves", "eval", {"code": "1+1"})
    with pytest.raises(ValueError, match="additionalProperties"):
        adapters.run("dancemoves", "validate_page_config", {"config": {}, "package": "arbitrary"})
    with pytest.raises(ValueError, match="one MiB"):
        adapters.run("dancemoves", "validate_page_config", {"config": {"large": "x" * (1024 * 1024)}})
    with pytest.raises(ValueError):
        adapters.run("dancemoves", "validate_page_config", {"config": {"bpm": float("nan")}})
