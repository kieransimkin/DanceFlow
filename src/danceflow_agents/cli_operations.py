"""Bounded, declarative adapters to the canonical ecosystem command lines.

This module never imports an engine, launches a process, installs a package or
touches a user file. The host owns runtime selection, path confinement, effect
approval and process/job management. All argv tokens come from this registry and
validated values; there is deliberately no arbitrary argv/extra-argument input.

Sources are stable tagged upstream CLIs, linked on every descriptor. Command
completion is process evidence only: inspect the owning tool's receipts before
claiming model, media, editorial or publication success.
"""
from __future__ import annotations

from copy import deepcopy
import math
import re
from typing import Any


_MISSING = object()
# argv is shell-free, but the receiving CLI still interprets option-looking
# tokens. In particular, nargs='*' can consume an injected --out as a new flag.
# Include dash variants conservatively for the PowerShell transport as well.
_OPTION_TOKEN_PATTERN = r"^\s*[-\u2010-\u2015\u2212\ufe63\uff0d]"
_OPTION_TOKEN = re.compile(_OPTION_TOKEN_PATTERN)
_SOURCES = {
    "stemlab": ("stemlab", "v1.11.0", "src/stemlab/cli.py"),
    "framerudiments": ("FrameRudiments", "v0.4.5", "src/framerudiments/cli.py"),
    "rastermoves": ("RasterMoves", "v0.3.4", "src/rastermoves/cli.py"),
    "prismmoves": ("PrismMoves", "v0.2.0", "src/prismmoves/cli.py"),
    "likenessforge": ("LikenessForge", "v0.4.5", "src/likenessforge/cli.py"),
    "workflowmoves": ("WorkflowMoves", "e7997ba577c02c02ee23d0d8a2e0d39572f557e3", ""),
}


def _string(*, choices=None, default=_MISSING, maximum=4096, pattern=None):
    schema = {
        "type": "string", "minLength": 1, "maxLength": maximum,
        "not": {"anyOf": [{"pattern": _OPTION_TOKEN_PATTERN}, {"pattern": "\u0000"}]},
    }
    if choices is not None:
        schema["enum"] = list(choices)
    if default is not _MISSING:
        schema["default"] = default
    if pattern is not None:
        schema["pattern"] = pattern
    return schema


def _number(minimum, maximum, default=_MISSING, *, integer=False):
    schema = {"type": "integer" if integer else "number", "minimum": minimum, "maximum": maximum}
    if default is not _MISSING:
        schema["default"] = default
    return schema


def _integer(minimum, maximum, default=_MISSING):
    return _number(minimum, maximum, default, integer=True)


def _param(schema, *, kind="value", flag=None, positional=None, required=False, **metadata):
    item = {"kind": kind, **metadata}
    if flag is not None:
        item["flag"] = flag
    if positional is not None:
        item["positional"] = positional
    return schema, item, required


def _value(flag, schema=None, *, required=False, **metadata):
    return _param(schema or _string(), flag=flag, required=required, **metadata)


def _flag(flag, *, default=False, false_flag=None):
    metadata = {"false_flag": false_flag} if false_flag else {}
    return _param({"type": "boolean", "default": default}, kind="flag", flag=flag, **metadata)


def _ack(description):
    return _param({"type": "boolean", "const": True, "description": description},
                  kind="flag", required=True, emit=False)


def _path(kind, flag=None, *, positional=None, required=True, multiple=False, **metadata):
    schema = _string(maximum=8192)
    if multiple:
        schema = {"type": "array", "items": schema, "minItems": 1, "maxItems": 64, "uniqueItems": True}
    return _param(schema, kind=kind, flag=flag, positional=positional, required=required,
                  multiple=multiple, **metadata)


def _repeat(flag, schema=None, *, maximum=64, many=False, default=_MISSING, emit_empty=False):
    array = {"type": "array", "items": schema or _string(), "maxItems": maximum, "uniqueItems": True}
    if default is not _MISSING:
        array["default"] = default
    return _param(array, kind="repeat", flag=flag, many=many, emit_empty=emit_empty)


def _operation(component, prefix, description, parameters=None, *, module=None, script=None,
               effects=(), partial=(), timeout=300, fixed=(), constraints=(), source=None, notes=()):
    parameters = parameters or {}
    repo, ref, upstream_path = _SOURCES[component]
    return {
        "description": description,
        **({"script": script} if script else {"module": module or component}),
        "prefix": list(prefix),
        "input_schema": {
            "type": "object", "additionalProperties": False,
            "properties": {name: deepcopy(value[0]) for name, value in parameters.items()},
            "required": [name for name, value in parameters.items() if value[2]],
        },
        "parameters": {name: deepcopy(value[1]) for name, value in parameters.items()},
        "effects": list(effects),
        "partial_exit_codes": list(partial),
        "timeout_seconds": timeout,
        "fixed_arguments": list(fixed),
        "constraints": list(constraints),
        "source": source or f"https://github.com/kieransimkin/{repo}/blob/{ref}/{script or upstream_path}",
        "notes": list(notes),
    }


OPERATIONS: dict[str, dict[str, dict[str, Any]]] = {
    name: {} for name in _SOURCES
}


def _add(component, name, prefix, description, parameters=None, **options):
    OPERATIONS[component][name] = _operation(component, prefix, description, parameters, **options)


# StemLab's native MCP adapter owns analysis/MIDI/evidence/loop jobs. These are
# additional canonical CLI routes not present in that adapter, plus cheap discovery.
for _command in ("doctor", "models", "analysis-actions", "midi-models", "evidence-models"):
    _add("stemlab", _command.replace("-", "_"), [_command],
         "Inspect StemLab runtime or registered analysis capabilities without starting inference.")

_add("stemlab", "export_timeline", ["export-timeline"],
     "Export saved results through the canonical React timeline to a new static directory.", {
         "results": _path("input_dir", positional=0),
         "output": _path("output_dir", "--output"),
         "include_audio": _flag("--include-audio"),
         "artwork": _path("input_file", "--artwork", required=False),
     }, effects=["write"], timeout=3600)

_add("stemlab", "repair_spectrograms", ["repair-spectrograms"],
     "Repair spectrogram PNGs in an existing results directory from retained NPZ evidence.", {
         "results": _path("input_dir", positional=0, writable=True),
         "max_plot_frames": _value("--max-plot-frames", _integer(2, 65536, 8192)),
     }, effects=["write"], timeout=3600,
     notes=["Writes into the supplied results directory; not an immutable export."])

_add("stemlab", "rudiments", ["rudiments"],
     "Match retained audio attack evidence to installed DanceRudiments patterns.", {
         "source": _path("input_file", positional=0, allow_directory=True),
         "output": _path("output_dir", "--output"),
         "bpm": _value("--bpm", _number(1, 1000)),
         "first_beat_seconds": _value("--first-beat-seconds", _number(0, 86400, 0)),
         "top": _value("--top", _integer(1, 500, 20)),
         "collection": _value("--collection", _string(choices=["initial", "expansion", "atlas", "continuum", "club", "dancefloor"])),
         "max_patterns": _value("--max-patterns", _integer(1, 20000, 1000)),
         "stems": _repeat("--stem"),
     }, effects=["write"], timeout=3600)

_add("stemlab", "phrase_loops", ["phrase-loops"],
     "Rank line-complete phrase auditions from saved evidence; no seamless-loop approval is inferred.", {
         "results": _path("input_dir", positional=0, writable=True),
         "feedback": _path("input_file", "--feedback", required=False),
         "min_seconds": _value("--min-seconds", _number(0.001, 3600, 5)),
         "max_seconds": _value("--max-seconds", _number(0.001, 3600, 30)),
         "min_lines": _value("--min-lines", _integer(1, 128, 4)),
         "top": _value("--top", _integer(1, 64, 6)),
         "max_bar_phase_error": _value("--max-bar-phase-error", _number(0, .5)),
         "export_audio": _flag("--export-audio"),
     }, effects=["write"], timeout=3600, constraints=["phrase_duration"],
     notes=["Writes deep/phrase_loops in the supplied results directory."])

_cue_parameters = {
    "results": _path("input_dir", positional=0),
    "output": _path("output_dir", "--output"),
    "tolerance_ms": _value("--tolerance-ms", _number(0, 60000, 150)),
    "beat_model": _value("--beat-model", _string(default="auto", maximum=200)),
    "downbeats": _flag("--downbeats"),
    "precision": _value("--precision", _string(choices=["exact", "milliseconds", "centiseconds"], default="exact")),
    "fail_on_review": _flag("--fail-on-review", default=True),
}
_cue_source = "https://github.com/kieransimkin/stemlab/blob/v1.11.0/src/stemlab/cue_cli.py"
_add("stemlab", "generate_cues", ["generate-cues"], "Generate beat-linked cues from retained song evidence.", {
    **_cue_parameters,
    "title": _value("--title"),
    "artist": _value("--artist", required=True),
}, effects=["write"], partial=[2], source=_cue_source,
     notes=["Exit 2 may mean saved cues require review; parse errors also use 2, so inspect receipts."])
_add("stemlab", "snap_cues", ["snap-cues"], "Snap a supplied LRC to retained detected beat evidence.", {
    **_cue_parameters,
    "results": _path("input_file", positional=0, allow_directory=True),
    "cues": _path("input_file", positional=1),
    "force_snap": _flag("--force-snap"),
    "sample_rate": _value("--sample-rate", _integer(1, 10000000)),
}, effects=["write"], partial=[2], source=_cue_source)

_add("stemlab", "match_clip", ["match-clip"], "Match an audio clip to source audio and retain a new evidence JSON file.", {
    "source": _path("input_file", positional=0), "clip": _path("input_file", positional=1),
    "output": _path("output_file", "--output"),
    "sample_rate": _value("--sample-rate", _integer(2000, 24000, 8000)),
    "clip_start": _value("--clip-start", _number(0, 86400, 0)),
    "clip_end": _value("--clip-end", _number(0, 86400)),
}, effects=["write"], timeout=3600, constraints=["clip_duration"],
     source="https://github.com/kieransimkin/stemlab/blob/v1.11.0/src/stemlab/clip_cli.py")

_add("stemlab", "beat_offset", ["beat-offset"], "Compare detected beats to canonical timing in saved results.", {
    "results": _path("input_dir", positional=0), "output": _path("output_dir", "--output"),
    "canonical_bpm": _value("--canonical-bpm", _number(1, 400)),
    "audio": _path("input_file", "--audio", required=False),
    "alignment_bpm_basis": _value("--alignment-bpm-basis", _string(choices=["canonical", "combined", "combined_family", "combined_fit"])),
    "alignment_analysis": _value("--alignment-analysis", _string(default="consensus", maximum=200)),
}, effects=["write"], source="https://github.com/kieransimkin/stemlab/blob/v1.11.0/src/stemlab/beat_offset_cli.py")

_record_parameters = {
    "source": _path("input_file", positional=0, allow_directory=True),
    "output": _path("output_dir", "--output"),
    "bpm": _value("--bpm", _number(1, 1000)), "bpm_confirmed": _flag("--bpm-confirmed"),
    "beat_zero": _value("--beat-zero", _number(0, 86400)),
    "beat_model": _value("--beat-model", _string(default="auto", maximum=200)),
    "moving_average_beats": _value("--moving-average-beats", _number(.000001, 64, .25)),
    "normalize": _value("--normalize", _string(choices=["none", "global", "per-axis"], default="none")),
    "filter_phase": _value("--filter-phase", _string(choices=["zero", "causal"], default="zero")),
    "length_policy": _value("--length-policy", _string(choices=["strict", "pad", "trim"], default="strict")),
    "start": _value("--start", _number(0, 86400, 0)),
    "end": _value("--end", _number(0, 86400)),
    "include_audio": _flag("--include-audio"),
    "harness": _flag("--harness", default=True, false_flag="--no-harness"),
}
_record_source = "https://github.com/kieransimkin/stemlab/blob/v1.11.0/src/stemlab/recording_cli.py"
_add("stemlab", "record_rudiment", ["record-rudiment"],
     "Record bounded source-derived motion or Fourier bands using the canonical StemLab implementation.", {
         **_record_parameters,
         "mode": _value("--mode", _string(choices=["peak", "average", "moving-average", "waveform"], default="peak")),
         "frequency_bands": _value("--frequency-bands", _integer(1, 1024)),
         "fft_size": _value("--fft-size", _integer(16, 65536, 2048)),
         "frequency_min": _value("--frequency-min", _number(0, 10000000, 0)),
         "frequency_max": _value("--frequency-max", _number(0, 10000000)),
         "frequency_scale": _value("--frequency-scale", _string(choices=["linear", "log"], default="linear")),
         "filter_order": _value("--filter-order", _integer(1, 12, 4)),
         "legacy": _flag("--legacy"),
         "name": _value("--name", _string(default="audio_recording", maximum=200)),
     }, effects=["write"], timeout=3600, source=_record_source, constraints=["source_duration", "fourier"])
_add("stemlab", "generate_batch", ["generate-batch"],
     "Create a bounded comparison batch from source audio or retained stems without new separation.", {
         **_record_parameters,
         "modes": _repeat("--mode", _string(choices=["peak", "average", "moving-average", "waveform"]), maximum=4),
         "dimensions": _repeat("--dimensions", _integer(1, 1024), maximum=8),
         "max_candidates": _value("--max-candidates", _integer(1, 1024, 48)),
         "seed": _value("--seed", _integer(0, 2147483647, 0)),
         "low_pass": _repeat("--low-pass", _number(.000001, 10000000), maximum=16),
         "high_pass": _repeat("--high-pass", _number(.000001, 10000000), maximum=16),
     }, effects=["write"], timeout=3600, source=_record_source, constraints=["source_duration"])


# FrameRudiments delegates rendering, plan validation, pinned runtimes and preset
# handling to the released renderer. Executable overrides and CMake args stay host-side.
for _command in ("renderers", "sprites", "visualisers"):
    _add("framerudiments", _command, [_command], "List installed renderer, sprite or pinned visualiser capabilities.")
_project_parameters = {
    "project": _path("input_file", positional=0),
    "output": _path("output_dir", "--output"),
}
_add("framerudiments", "plan", ["plan"], "Validate pinned project inputs and write a new frame ledger JSON file.", {
    **_project_parameters, "output": _path("output_file", "--output"),
}, effects=["write"], timeout=600)
_add("framerudiments", "preflight", ["preflight"], "Run the canonical renderer preflight in a new evidence directory.",
     _project_parameters, effects=["write"], timeout=3600)
_add("framerudiments", "render", ["render"], "Render a source-bound project with media and verification artifacts.", {
    **_project_parameters,
    "preset": _value("--preset", _string(choices=["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"], default="fast")),
    "crf": _value("--crf", _integer(0, 51, 20)),
}, effects=["write"], timeout=14400)
_add("framerudiments", "demo", ["demo"], "Generate an explicit synthetic demo project in a new directory.", {
    "directory": _path("output_dir", positional=0), "font": _path("input_file", "--font"),
    "rangoli": _flag("--rangoli"), "spectrum": _flag("--spectrum"), "rudiments": _flag("--rudiments"),
    "effects": _repeat("--effect", _string(choices=["butterchurn", "projectm"]), maximum=2),
    "effect_preset": _value("--effect-preset", _string(choices=["feedback", "kaleidoscope", "julia"], default="feedback")),
    "width": _value("--width", _integer(64, 4096, 360)), "height": _value("--height", _integer(64, 4096, 640)),
}, effects=["write"], timeout=3600, constraints=["demo_view"])
_add("framerudiments", "effects_setup", ["effects-setup"],
     "Explicitly download/build one pinned canonical visualiser runtime.", {
         "engine": _param(_string(choices=["butterchurn", "projectm"]), positional=0, required=True),
         "directory": _path("output_dir", positional=1),
         "parallel": _value("--parallel", _integer(1, 64, 4)),
         "allow_downloads": _ack("Authorize downloading and building the selected pinned runtime."),
     }, effects=["write", "download", "network"], timeout=14400)
_add("framerudiments", "presets_install", ["presets-install"],
     "Install separately pinned upstream executable preset libraries after explicit authorization.", {
         "directory": _path("output_dir", positional=0),
         "packs": _repeat("--pack", maximum=16),
         "cache": _path("input_dir", "--cache", required=False),
         "allow_downloads": _ack("Authorize installing the selected pinned executable preset libraries."),
     }, effects=["write", "download", "network"], timeout=3600)
_add("framerudiments", "presets_profile", ["presets-profile"],
     "Capture a bounded selection of canonical preset responses; run Prism analysis separately.", {
         "suite": _path("input_file", positional=0),
         "catalogue": _path("input_file", positional=1),
         "output": _path("output_dir", "--output", allow_existing=True),
         "intervals": _repeat("--intervals", _number(0, 3600), maximum=64, many=True, default=[0, 1, 2, 4]),
         "images": _repeat("--image", maximum=32),
         "audio_modes": _repeat("--audio-mode", _string(choices=["programme", "silence"]), maximum=2),
         "ids": _repeat("--id", maximum=128),
         "limit": _value("--limit", _integer(1, 128, 8)),
         "resume": _flag("--resume"), "retry_failed": _flag("--retry-failed"),
         "max_edge": _value("--max-edge", _integer(32, 2048, 256)),
     }, effects=["write"], partial=[2], timeout=14400,
     notes=["Exit 2 can mean partial captures or an ordinary error; inspect per-preset state.",
            "No client-controlled --prism-python executable is accepted; use PrismMoves operations."])


# RasterMoves defaults to cache-only execution. Downloading weights/refiners is a
# separately named operation; external Python plugins and overwrite are excluded.
_raster_cache = {"cache_dir": _path("output_dir", "--cache-dir", required=False,
                                    allow_existing=True, before_prefix=True)}
_add("rastermoves", "doctor", ["doctor"], "Inspect installed runtime versions and available devices.")
_add("rastermoves", "models", ["models"], "Search locally available model manifests and retain licence metadata.", {
    **_raster_cache,
    "query": _param(_string(maximum=500), positional=0),
    "architecture": _value("--architecture", _string(maximum=200)),
    "scale": _value("--scale", _integer(1, 64)), "tag": _value("--tag", _string(maximum=200)),
}, fixed=["--json"], effects=["write"],
     notes=["Upstream Registry initializes the local cache directory, without downloading weights."])
_add("rastermoves", "info", ["info"], "Inspect one locally known model without fetching catalogue or weights.", {
    **_raster_cache, "model": _param(_string(maximum=500), positional=0, required=True),
}, fixed=["--offline"], effects=["write"],
     notes=["Upstream Registry initializes the local cache directory; catalogue fetching is disabled."])
_add("rastermoves", "refiners", ["refiners"], "List canonical pinned refinement workflows without downloads.", fixed=["--json"])
_add("rastermoves", "sync", ["sync"], "Explicitly refresh OpenModelDB catalogue metadata; no weights are downloaded.", {
    **_raster_cache, "allow_downloads": _ack("Authorize the canonical catalogue metadata download."),
}, effects=["write", "download", "network"], timeout=600)
_add("rastermoves", "download", ["download"], "Explicitly download one selected model's weights to the configured cache.", {
    **_raster_cache, "model": _param(_string(maximum=500), positional=0, required=True),
    "backend": _value("--backend", _string(choices=["auto", "spandrel", "onnx"], default="auto")),
    "strict_checksums": _flag("--strict-checksums", default=True),
    "allow_downloads": _ack("Authorize this selected model download after reviewing its licence."),
}, effects=["write", "download", "network"], timeout=3600)
_refinement_source = "https://github.com/kieransimkin/RasterMoves/blob/v0.3.4/src/rastermoves/refinement/cli.py"
_add("rastermoves", "download_refiner", ["download-refiner"], "Explicitly prefetch one canonical pinned refiner.", {
    **_raster_cache, "refiner": _param(_string(choices=["sd15-tile", "sdxl-tile"]), positional=0, required=True),
    "strict_checksums": _flag("--strict-checksums", default=True),
    "allow_downloads": _ack("Authorize the selected refiner's pinned model-component downloads."),
}, effects=["write", "download", "network"], timeout=3600, source=_refinement_source)
_raster_image = {
    **_raster_cache, "input": _path("input_file", positional=0, allow_directory=True),
    "output": _path("output_file", "--output", allow_directory=True),
    "recursive": _flag("--recursive"), "continue_on_error": _flag("--continue-on-error"),
    "max_output_mp": _value("--max-output-mp", _number(.001, 64, 64)),
    "strict_checksums": _flag("--strict-checksums", default=True),
}
_upscale_parameters = {
    **_raster_image,
    "model": _value("--model", _string(maximum=500)),
    "model_file": _path("input_file", "--model-file", required=False),
    "native_scale": _value("--native-scale", _integer(1, 64)),
    "backend": _value("--backend", _string(choices=["auto", "spandrel", "onnx"], default="auto")),
    "device": _value("--device", _string(default="auto", maximum=40, pattern=r"^(auto|cpu|mps|cuda(?::[0-9]+)?)$")),
    "precision": _value("--precision", _string(choices=["fp32", "fp16"], default="fp32")),
    "tile": _value("--tile", _integer(0, 8192, 256)), "overlap": _value("--overlap", _integer(0, 4096, 32)),
    "tile_pad": _value("--tile-pad", _integer(0, 4096, 16)), "force_tiling": _flag("--force-tiling"),
    "scale": _value("--scale", _number(.01, 64)), "width": _value("--width", _integer(1, 65536)),
    "height": _value("--height", _integer(1, 65536)), "long_edge": _value("--long-edge", _integer(1, 65536)),
    "alpha": _value("--alpha", _string(choices=["lanczos", "model"], default="lanczos")),
    "format": _value("--format", _string(choices=["png", "webp", "jpg", "tiff"], default="png")),
    "extra_arches": _flag("--extra-arches"),
}
_add("rastermoves", "upscale", ["upscale"], "Upscale local images with installed cached weights and provenance sidecars.",
     _upscale_parameters, effects=["write", "inference"], fixed=["--offline", "--report"],
     timeout=14400, constraints=["raster_size", "raster_model"],
     notes=["No overwrite or external plugin loading. Exit 1 can retain successful batch outputs."])
_add("rastermoves", "plan_all_models", ["upscale"], "Print the canonical all-model output plan without downloading or running models.", {
    **_raster_cache, "input": _path("input_file", positional=0),
    "output": _path("output_dir", "--output"),
}, fixed=["--all-models", "--dry-run", "--offline"], effects=["write"], timeout=600,
     notes=["Upstream Registry may initialize its cache directory; no model inference or image output is performed."])
_refine_parameters = {
    **_raster_image,
    "refiner": _value("--refiner", _string(choices=["sd15-tile", "sdxl-tile"], default="sd15-tile")),
    "format": _value("--format", _string(choices=["png", "webp", "tiff"], default="png")),
    "strength": _value("--refine-strength", _number(0, 1, .22)),
    "steps": _value("--refine-steps", _integer(1, 200, 40)),
    "guidance": _value("--refine-guidance", _number(0, 50, 5)),
    "control_scale": _value("--refine-control-scale", _number(0, 10, 1)),
    "tile": _value("--refine-tile", _integer(64, 4096)),
    "overlap": _value("--refine-overlap", _integer(0, 2048, 64)),
    "blend": _value("--refine-blend", _number(0, 1, 1)),
    "color_match": _flag("--refine-color-match"),
    "mask_feather": _value("--refine-mask-feather", _number(0, 1024, 0)),
    "protect_mask": _path("input_file", "--protect-mask", required=False),
    "seed": _value("--seed", _integer(0, 2147483647, 0)),
    "prompt": _value("--refine-prompt"), "negative_prompt": _value("--refine-negative-prompt"),
    "device": _value("--refine-device", _string(default="auto", maximum=40, pattern=r"^(auto|cpu|mps|cuda(?::[0-9]+)?)$")),
    "precision": _value("--refine-precision", _string(choices=["auto", "fp16", "fp32"], default="auto")),
    "offload": _value("--refine-offload", _string(choices=["none", "model", "sequential"])),
    "scheduler": _value("--refine-scheduler", _string(choices=["ddim", "euler"])),
    "resume": _flag("--resume"),
}
_add("rastermoves", "refine", ["refine"], "Refine images at unchanged dimensions with cached weights and retained baselines.",
     _refine_parameters, effects=["write", "inference"], fixed=["--offline"], timeout=14400,
     constraints=["refine_tile"], source=_refinement_source)
_add("rastermoves", "plan_refinement", ["refine"], "Write no images; print the validated canonical refinement plan.",
     _refine_parameters, fixed=["--offline", "--dry-run"], constraints=["refine_tile"], source=_refinement_source)


# PrismMoves supports both measurements and explicitly selected optional models.
_visual_models = _string(choices=["clip", "dinov2", "blip", "ocr"])
_prism_models = {
    "models": _repeat("--models", _visual_models, maximum=4, many=True, default=[], emit_empty=True),
    "models_dir": _path("input_dir", "--models-dir", required=False),
    "allow_download": _flag("--allow-download"),
    "device": _value("--device", _string(choices=["cpu", "cuda", "mps"], default="cpu")),
    "max_edge": _value("--max-edge", _integer(32, 2048, 768)),
}
_add("prismmoves", "profile", [], "Profile bounded local images and write evidence-labelled JSON, HTML, Markdown and SVG reports.", {
    **_prism_models,
    "images": _path("input_file", positional=0, multiple=True), "output": _path("output_dir", "--out"),
    "pixelcue_url": _value("--pixelcue-url", _string(maximum=100, pattern=r"^http://(localhost|127\.0\.0\.1|\[::1\])(?::[0-9]{1,5})?/?$")),
    "pixelcue_models": _repeat("--pixelcue-models", _string(maximum=200), many=True, maximum=8),
    "background": _value("--background", _string(default="#ffffff", pattern=r"^#[0-9A-Fa-f]{6}$")),
    "role": _value("--role", _string(default="unknown", maximum=500)),
    "lineage": _value("--lineage", _string(default="unknown", maximum=500)),
}, effects=["write"], partial=[2], timeout=3600,
     constraints=["prism_download"], notes=["Optional model downloads remain disabled unless allow_download is true.",
                                          "Exit 2 may retain reports with unavailable images/models; inspect analysis.json."])
_preset_source = "https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/src/prismmoves/preset_pipeline.py"
_add("prismmoves", "preset_analyse", ["analyse"], "Describe captured presets using temporal evidence and a bounded semantic budget.", {
    **_prism_models,
    "captures": _path("input_file", "--captures"),
    "output": _path("output_dir", "--out", allow_existing=True),
    "cache_dir": _path("output_dir", "--cache-dir", required=False, allow_existing=True),
    "budget": _value("--budget", _integer(1, 256, 24)),
    "keyword_models": _repeat("--keyword-models", _string(maximum=200), many=True, maximum=8),
    "max_edge": _value("--max-edge", _integer(32, 2048, 256)),
    "semantic_edge": _value("--semantic-edge", _integer(32, 2048, 384)),
}, module="prismmoves.preset_pipeline", effects=["write"],
     partial=[2], timeout=14400, source=_preset_source, constraints=["prism_download"],
     notes=["Retained request signatures govern resumption; changed settings require new output."])
_add("prismmoves", "preset_legacy", ["legacy"], "Replay retained legacy preset reports without new model inference.", {
    "reports": _path("input_dir", "--reports"), "output": _path("output_dir", "--out"),
    "budget": _value("--budget", _integer(1, 256, 24)),
}, module="prismmoves.preset_pipeline", effects=["write"], source=_preset_source, timeout=3600)
_add("prismmoves", "preset_reindex", ["reindex"], "Rebuild the canonical gallery index for an existing report directory.", {
    "output": _path("output_dir", "--out", allow_existing=True),
}, module="prismmoves.preset_pipeline", effects=["write"], source=_preset_source)
for _name, _model_parameter in (("profile", "pixelcue_models"), ("preset_analyse", "keyword_models")):
    OPERATIONS["prismmoves"][_name]["conditional_effects"] = [
        {"parameter": "models", "when": "nonempty", "effects": ["inference"]},
        {"parameter": _model_parameter, "when": "nonempty", "effects": ["inference"]},
        {"parameter": "allow_download", "equals": True, "effects": ["download", "network"]},
    ]
OPERATIONS["prismmoves"]["profile"]["conditional_effects"].append(
    {"parameter": "pixelcue_url", "when": "nonempty", "effects": ["network"]})


# LikenessForge has no package __main__; the actual module entry point is .cli.
# Its inference routes can download on demand and have no universal offline flag.
_likeness_module = "likenessforge.cli"
_add("likenessforge", "plugins", ["plugins"], "List installed detector, segmenter, modifier and trainer plugin metadata.",
     module=_likeness_module, fixed=["--json"], effects=["write"],
     notes=["The upstream CLI initializes empty project-local model directories even during discovery."])
_add("likenessforge", "models", ["models", "list"], "List model-backed plugins without downloading weights.",
     module=_likeness_module, effects=["write"])
_add("likenessforge", "download_model", ["models", "download"], "Explicitly provision a named canonical plugin's model.", {
    "name": _param(_string(maximum=200), positional=0, required=True),
    "allow_downloads": _ack("Authorize downloading the selected model-backed plugin's weights."),
}, module=_likeness_module, effects=["write", "download", "network"], timeout=14400)
_likeness_common = {
    "detector": _value("--detector", _string(maximum=200)),
    "allow_downloads": _ack("This canonical command may download missing selected model weights on demand."),
}
_face = _string(default="largest", maximum=20, pattern=r"^(largest|[0-9]+)$")
_add("likenessforge", "faces", ["faces"], "Detect and index faces using the selected canonical detector.", {
    **_likeness_common, "image": _path("input_file", positional=0),
    "preview": _path("output_file", "--preview", required=False),
}, module=_likeness_module, effects=["write", "inference", "download", "network"], partial=[2], timeout=3600,
     notes=["Exit 2 can mean no faces were found; argparse errors also use 2, so inspect output."])
_repair_common = {
    **_likeness_common, "image": _path("input_file", positional=0),
    "segmenter": _value("--segmenter", _string(maximum=200)),
    "modifier": _value("--modifier", _string(maximum=200)),
    "face": _value("--face", _face),
    "lora": _path("input_file", "--lora", required=False, allow_directory=True),
    "references": _path("input_file", "--reference", required=False, multiple=True, repeat=True),
    "prompt": _value("--prompt"), "negative_prompt": _value("--negative-prompt"),
    "seed": _value("--seed", _integer(0, 2147483647, 0)),
    "low_vram": _value("--low-vram", _string(choices=["auto", "off", "cpu_offload", "bnb4"])),
}
_add("likenessforge", "repair", ["repair"], "Repair one explicitly selected face with the canonical workflow.", {
    **_repair_common, "output": _path("output_file", positional=1),
    "lora_scale": _value("--lora-scale", _number(0, 5, 1)),
    "crop_margin": _value("--crop-margin", _number(0, 5)), "feather": _value("--feather", _integer(0, 2048)),
    "steps": _value("--steps", _integer(1, 200)), "guidance": _value("--guidance", _number(0, 50)),
    "strength": _value("--strength", _number(0, 1)),
}, module=_likeness_module, effects=["write", "inference", "download", "network"], timeout=14400)
_add("likenessforge", "repair_wizard", ["repair-wizard"], "Create a bounded canonical repair comparison and evidence manifest.", {
    **_repair_common, "output": _path("output_dir", positional=1),
    "preset": _value("--preset", _string(choices=["quick", "balanced", "thorough"], default="quick")),
}, module=_likeness_module, effects=["write", "inference", "download", "network"], timeout=14400)
_training_common = {
    **_likeness_common,
    "images": _path("input_dir", positional=0), "output": _path("output_dir", positional=1),
    "segmenter": _value("--segmenter", _string(maximum=200)),
    "trainer": _value("--trainer", _string(maximum=200)),
    "trigger": _value("--trigger", _string(maximum=200), required=True), "face": _value("--face", _face),
    "background": _value("--background", _string(choices=["blur", "neutral", "black", "original"], default="blur")),
}
_add("likenessforge", "prepare_training", ["prepare-training"], "Prepare authorized segmented face crops without training a LoRA.",
     _training_common, module=_likeness_module, effects=["write", "inference", "download", "network"], timeout=14400)
_add("likenessforge", "train_lora", ["train-lora"], "Train one explicitly authorized identity LoRA with bounded settings.", {
    **_training_common,
    "allow_training": _ack("Authorize training on the supplied identity dataset."),
    "steps": _value("--steps", _integer(1, 10000, 800)), "rank": _value("--rank", _integer(1, 256, 16)),
    "learning_rate": _value("--learning-rate", _number(.00000001, .1, .0001)), "low_vram": _flag("--low-vram"),
}, module=_likeness_module, effects=["write", "inference", "download", "network", "training"], timeout=86400)
_train_wizard_parameters = {name: value for name, value in _training_common.items() if name != "background"}
_add("likenessforge", "train_wizard", ["train-wizard"], "Train bounded candidate LoRAs and compare fixed holdout repairs.", {
    **_train_wizard_parameters,
    "validation": _path("input_file", positional=1), "output": _path("output_dir", positional=2),
    "modifier": _value("--modifier", _string(maximum=200)), "validation_face": _value("--validation-face", _face),
    "preset": _value("--preset", _string(choices=["quick", "balanced", "thorough"], default="quick")),
    "seed": _value("--seed", _integer(0, 2147483647, 0)), "low_vram": _flag("--low-vram"),
    "prompt": _value("--prompt"), "negative_prompt": _value("--negative-prompt"),
    "allow_training": _ack("Authorize the selected bounded training and holdout comparison batch."),
}, module=_likeness_module, effects=["write", "inference", "download", "network", "training"], timeout=86400)


# WorkflowMoves is a configured checkout of scripts, not an invented Python package.
for _name, _script, _parameter, _description in (
    ("check_blogworthiness", "check_blogworthiness.py", "path", "Validate recorded blogworthiness fields; not editorial truth or publication approval."),
    ("audit_epk_evidence", "audit_epk_evidence.py", "records", "Audit recorded EPK evidence without claiming browser, sensor or rights verification."),
    ("audit_epk_layout", "audit_epk_layout.py", "records", "Audit supplied layout observations and width coverage."),
):
    _add("workflowmoves", _name, [], _description, {_parameter: _path("input_file", positional=0)},
         script="tools/" + _script, partial=[1],
         notes=["Exit 1 can indicate validation findings or an error; inspect structured output."])
_add("workflowmoves", "audit_epk_timing", [], "Find hardcoded EPK timing bindings in a supplied HTML file.", {
    "html": _path("input_file", positional=0), "configured_urls": _repeat("--configured-url"),
}, script="tools/audit_epk_timing_bindings.py", partial=[1])
_add("workflowmoves", "audit_campaign_media", [], "Audit a media ledger and catalogue into a new provenance report.", {
    "ledger": _path("input_file", positional=0), "catalogue": _path("input_file", positional=1),
    "output": _path("output_file", "--output"),
}, script="tools/audit_campaign_media.py", effects=["write"])
_add("workflowmoves", "publicity_inventory", [], "Inventory bounded local publicity candidates without granting send authority.", {
    "root": _path("input_dir", positional=0), "output": _path("output_file", "--output"),
}, script="tools/publicity_inventory.py", effects=["write"], timeout=600)
_add("workflowmoves", "compose_epk_playback", [], "Compose reviewed explicit player mappings into new local HTML.", {
    "source": _path("input_file", positional=0), "bindings": _path("input_file", positional=1),
    "output": _path("output_file", "--output"),
}, script="tools/compose_epk_playback.py", effects=["write"])
_add("workflowmoves", "compose_epk_cover", [], "Compose a local artwork-first player from fresh source HTML.", {
    "source": _path("input_file", positional=0), "output": _path("output_file", "--output"),
    "cover_url": _value("--cover-url", required=True), "cover_alt": _value("--cover-alt", required=True),
}, script="tools/compose_epk_cover.py", effects=["write"])
_add("workflowmoves", "integrate_epk_media", [], "Transform local HTML using an explicit media profile and retain an edit receipt.", {
    "source": _path("input_file", positional=0), "profile": _path("input_file", positional=1),
    "output": _path("output_file", positional=2), "record": _path("output_file", "--record"),
}, script="tools/integrate_epk_media.py", effects=["write"])
_add("workflowmoves", "clean_epk_video_links", [], "Remove redundant local video links and retain exact edit evidence.", {
    "source": _path("input_file", positional=0), "output": _path("output_file", "--output"),
    "record": _path("output_file", "--record"),
}, script="tools/clean_epk_video_links.py", effects=["write"])
_claim_root = {"root": _path("output_dir", "--root", allow_existing=True)}
_claim_identity = {
    **_claim_root,
    "key": _value("--key", _string(maximum=64, pattern=r"^[0-9a-f]{64}$"), required=True),
    "token": _value("--token", _string(maximum=48, pattern=r"^[0-9a-f]{48}$"), required=True),
}
_add("workflowmoves", "outreach_list", ["list"], "List retained active send claims; this operation never sends a message.", {
    "root": _path("input_dir", "--root"),
}, script="tools/outreach_send_gate.py")
_add("workflowmoves", "outreach_claim", ["claim"], "Create an atomic claim for an approved packet; no approval is granted and nothing is sent.", {
    **_claim_root,
    **{name: _value("--" + name, _string(maximum=1000), required=True)
       for name in ("account", "venue", "obligation", "owner", "approval")},
    "packet": _path("input_file", "--packet"),
}, script="tools/outreach_send_gate.py", effects=["write"],
     notes=["Permanent duplicate tombstones and exact owner tokens remain managed by the canonical helper."])
_add("workflowmoves", "outreach_inspect", ["inspect"], "Check claim ownership and unchanged approved packet bytes without sending.", {
    **_claim_identity, "root": _path("input_dir", "--root"),
}, script="tools/outreach_send_gate.py")
_add("workflowmoves", "outreach_finish", ["finish"], "Retain verified send evidence and release only the exact owned mutex; uncertain sends remain claimed.", {
    **_claim_identity, "receipt": _path("input_file", "--receipt"),
}, script="tools/outreach_send_gate.py", effects=["write"],
     notes=["The helper verifies receipt state, packet ownership and form evidence hashes; it never sends or retries."])

# This transport retains the owning script's exact manifest hashes and receipts.
# The operator binds site URL and credential location outside tool arguments.
for _name, _mode in (
    ("wordpress_inventory", "Inventory"), ("wordpress_read_post", "ReadPost"),
    ("wordpress_upload_media", "UploadMedia"), ("wordpress_create_draft", "CreateDraft"),
    ("wordpress_publish_post", "PublishPost"), ("wordpress_schedule_post", "SchedulePost"),
):
    _mutates = _mode not in {"Inventory", "ReadPost"}
    _wp_parameters = {"receipt_out": _path("output_file", "-ReceiptOut")}
    if _mode == "ReadPost":
        _wp_parameters["post_id"] = _value("-PostId", _integer(1, 2147483647), required=True)
    if _mutates:
        _wp_parameters.update({
            "manifest": _path("input_file", "-ManifestPath"),
            "expected_manifest_sha256": _value("-ExpectedManifestSha256",
                _string(maximum=64, pattern=r"^[a-fA-F0-9]{64}$"), required=True),
        })
    _add("workflowmoves", _name, ["-Mode", _mode],
         "Invoke the canonical guarded WordPress transport with operator-bound credentials and a new receipt.",
         _wp_parameters, script="tools/wordpress_blog_api.ps1",
         effects=["write", "network"] + (["publication"] if _mutates else []),
         fixed=["-Execute"] if _mutates else [], timeout=600,
         notes=["Requires operator-configured PowerShell 7.5+, HTTPS site and credential binding.",
                "Never retry an uncertain remote mutation automatically; inspect retained receipt and re-read.",
                "Native manifest authority fields, media hashes and fresh-post review hashes remain mandatory."])
    OPERATIONS["workflowmoves"][_name]["runtime"] = "powershell"


UNSUPPORTED_OPERATIONS = {
    "stemlab": {
        "analyze_midi_evidence_loops": "Use the persistent canonical StemLab MCP provider, which owns download opt-ins, jobs and receipts.",
        "bootstrap_serve": "Dependency installation and long-lived service startup are owner runtime configuration, not arbitrary CLI calls.",
        "generate_stem_batch_generate_average_comparison": "Use native analysis first, then bounded retained-source recording routes; raw-input variants can download separation models.",
        "axis_source_overrides": "NAME=path and backend executable overrides need host-side trusted configuration; no opaque nested path passthrough.",
    },
    "framerudiments": {
        "executable_overrides": "FFmpeg, ffprobe, Prism Python and arbitrary CMake arguments remain owner-configured executables.",
        "authoring_ui": "The canonical authoring UI is a browser product; use its capability resources and a host browser.",
    },
    "rastermoves": {
        "gui": "Interactive GUI sessions are not bounded MCP jobs.",
        "external_plugins": "Client-provided Python plugin directories or arbitrary backend names are not loaded.",
        "all_models_inference": "Unbounded catalogue-wide inference is excluded; inspect plan_all_models then invoke selected models explicitly.",
        "overwrite": "Existing media must not be silently replaced; use new output paths.",
    },
    "prismmoves": {
        "model_path_overrides": "Provision selected weights in a configured project models directory; opaque NAME=path values are not accepted.",
    },
    "likenessforge": {
        "gui": "Interactive desktop sessions are not bounded MCP jobs.",
        "config_extra_args": "Arbitrary plugin configuration and trainer extra arguments are not forwarded; use supported typed options.",
        "remote_lora": "The MCP route accepts a confined local LoRA asset; remote LoRA provisioning is a separate owner action.",
        "offline_inference": "The canonical CLI has no universal offline flag; computation requires explicit download/network acknowledgement.",
    },
    "workflowmoves": {
        "wordpress_credentials": "Credentials and site selection are operator configuration; the authenticated transport accepts only typed mode/manifest/hash/receipt inputs.",
        "browser_observers": "Layout collection and player scripts run inside the authorized host browser, not a Python subprocess.",
        "install": "Project integration changes agent instructions and route files; use the reviewed canonical installer separately.",
        "generic_send": "No generic email-send operation exists; a claim is not send authority. WordPress retains its separate native publication gates.",
    },
}

# Lower-case alias keeps the data easy to consume without coupling the host to a
# naming convention. Both refer to the same JSON-serializable descriptor mapping.
operations = OPERATIONS


def validated_arguments(descriptor: dict[str, Any], arguments: dict[str, Any]) -> dict[str, Any]:
    """Validate a strict public schema and return an independent defaulted value.

    Filesystem validation belongs to the host. This function only checks values;
    it is safe to use during discovery, planning and unit tests without engines.
    """
    from jsonschema import Draft202012Validator

    if not isinstance(arguments, dict):
        raise ValueError("Operation arguments must be an object")
    schema = descriptor["input_schema"]
    values = deepcopy(arguments)
    for name, spec in schema["properties"].items():
        if name not in values and "default" in spec:
            values[name] = deepcopy(spec["default"])
    errors = sorted(Draft202012Validator(schema).iter_errors(values), key=lambda item: str(item.path))
    if errors:
        first = errors[0]
        location = ".".join(map(str, first.path)) or "arguments"
        raise ValueError(f"{location}: {first.message}")

    def finite(value):
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("Numeric values must be finite")
        if isinstance(value, (list, tuple)):
            for item in value:
                finite(item)
        if isinstance(value, dict):
            for item in value.values():
                finite(item)
    finite(values)
    # Keep this guard independent of registry schema generation: synthetic or
    # future descriptors must not bypass token validation by using a bare string
    # schema. Inspect typed strings only; legitimate negative JSON numbers are
    # numeric arguments, not attempted flags. No argument values are split.
    for name, parameter in descriptor["parameters"].items():
        if name not in values or parameter.get("emit") is False:
            continue
        tokens = values[name] if isinstance(values[name], list) else [values[name]]
        for value in tokens:
            if isinstance(value, str) and (_OPTION_TOKEN.search(value) or "\0" in value):
                raise ValueError(f"{name}: literal CLI values must not begin with an option prefix or contain NUL")
    # JSON Schema accepts 2048.0 as an integer; canonical argparse int options
    # require the integral spelling rather than the string "2048.0".
    for name, spec in schema["properties"].items():
        if name not in values:
            continue
        if spec.get("type") == "integer":
            values[name] = int(values[name])
        elif spec.get("type") == "array" and spec.get("items", {}).get("type") == "integer":
            values[name] = [int(item) for item in values[name]]
    _validate_constraints(descriptor.get("constraints", ()), values)
    return values


def _validate_constraints(constraints, values):
    for constraint in constraints:
        if constraint == "demo_view" and sum(bool(values.get(name)) for name in ("rangoli", "spectrum", "rudiments")) > 1:
            raise ValueError("Choose at most one demo view: rangoli, spectrum or rudiments")
        if constraint == "raster_size" and sum(name in values for name in ("scale", "width", "height", "long_edge")) > 1:
            raise ValueError("Choose one final size: scale, width, height or long_edge")
        if constraint == "raster_model" and "model" in values and "model_file" in values:
            raise ValueError("Choose a registered model or a local model_file")
        if constraint == "refine_tile":
            tile = values.get("tile", 1024 if values.get("refiner") == "sdxl-tile" else 512)
            if tile % 8:
                raise ValueError("Refinement tile size must be a multiple of 8")
            if values.get("overlap", 64) >= tile:
                raise ValueError("Refinement overlap must be smaller than tile size")
            if 0 < values.get("strength", .22) * values.get("steps", 40) < 1:
                raise ValueError("Refinement strength and steps must permit one denoising step")
        if constraint == "prism_download" and (values.get("pixelcue_models") or values.get("keyword_models")) and not values.get("allow_download"):
            raise ValueError("Selected PixelCue keyword models require explicit allow_download=true")
        if constraint == "phrase_duration" and values["min_seconds"] > values["max_seconds"]:
            raise ValueError("min_seconds must not exceed max_seconds")
        if constraint in {"clip_duration", "source_duration"}:
            start_name, end_name = ("clip_start", "clip_end") if constraint == "clip_duration" else ("start", "end")
            if end_name in values and values[end_name] <= values.get(start_name, 0):
                raise ValueError(f"{end_name} must be greater than {start_name}")
        if constraint == "fourier":
            fft = values["fft_size"]
            if fft & (fft - 1):
                raise ValueError("fft_size must be a power of two")
            if values.get("frequency_scale") == "log" and values.get("frequency_min", 0) <= 0:
                raise ValueError("Log frequency scale requires positive frequency_min")
            if "frequency_max" in values and values["frequency_max"] <= values.get("frequency_min", 0):
                raise ValueError("frequency_max must exceed frequency_min")


def build_arguments(descriptor: dict[str, Any], arguments: dict[str, Any]) -> list[str]:
    """Build canonical argv tokens after schema and cross-field validation.

    Path metadata: ``multiple`` means an array of separately confined paths;
    ``repeat`` emits its flag once per path. ``allow_directory`` accepts either
    an input file or directory; ``allow_existing`` supports documented resume or
    state directories. Hosts must not create output paths before tools requiring
    a new path have opened them. ``before_prefix`` is used for real global flags.
    Literal strings beginning with a dash are rejected, including list and
    positional values. Use ordinary prose or an absolute path for such inputs;
    typed negative numeric arguments retain their numeric meaning.
    """
    values = validated_arguments(descriptor, arguments)
    before, options, positionals = [], [], []
    for name, parameter in descriptor["parameters"].items():
        if name not in values or parameter.get("emit") is False:
            continue
        value = values[name]
        flag = parameter.get("flag")
        if "positional" in parameter:
            tokens = [str(item) for item in value] if isinstance(value, list) else [str(value)]
            positionals.append((parameter["positional"], tokens))
            continue
        destination = before if parameter.get("before_prefix") else options
        if parameter["kind"] == "flag":
            chosen = flag if value else parameter.get("false_flag")
            if chosen:
                destination.append(chosen)
        elif isinstance(value, list):
            if not value and not parameter.get("emit_empty"):
                continue
            if parameter.get("many"):
                destination.extend([flag, *map(str, value)])
            else:
                for item in value:
                    destination.extend([flag, str(item)])
        elif flag:
            destination.extend([flag, str(value)])
    return (before + list(descriptor["prefix"]) +
            [item for _, tokens in sorted(positionals) for item in tokens] +
            options + list(descriptor.get("fixed_arguments", ())))


def effects_for_arguments(descriptor: dict[str, Any], arguments: dict[str, Any]) -> list[str]:
    """Resolve real optional model/download effects from the validated invocation."""
    values = validated_arguments(descriptor, arguments)
    effects = set(descriptor.get("effects", ()))
    for condition in descriptor.get("conditional_effects", ()):
        value = values.get(condition["parameter"])
        matches = bool(value) if condition.get("when") == "nonempty" else value == condition.get("equals")
        if matches:
            effects.update(condition["effects"])
    return sorted(effects)
