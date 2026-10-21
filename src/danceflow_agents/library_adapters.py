"""Bounded calls to installed library APIs; browser and WordPress hosts stay explicit.

Discovery reads module/package metadata only. No npm installation, arbitrary script,
browser mount, media decoding fallback or WordPress mutation is performed here.
"""
from __future__ import annotations

import base64
import contextlib
import copy
import importlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import threading

from jsonschema import Draft202012Validator, ValidationError


MAX_INPUT_BYTES = 1024 * 1024
MAX_RESULT_BYTES = 4 * 1024 * 1024
MAX_THUMBNAIL_BYTES = 2 * 1024 * 1024
MAX_NODE_DIAGNOSTIC_BYTES = 256 * 1024
NODE_TIMEOUT_SECONDS = 30
NODE_PACKAGES = {
    "dancemoves": "@kieransimkin/dancemoves",
    "react-timeline-sequence": "react-timeline-sequence",
}
PYTHON_PACKAGES = {"dancerudiments": "dancerudiments", "thumbmoves": "thumbmoves"}


def _object(properties: dict, required: tuple[str, ...] = ()) -> dict:
    return {"type": "object", "properties": properties, "required": list(required),
            "additionalProperties": False}


def _operation(name: str, description: str, properties: dict,
               required: tuple[str, ...] = ()) -> dict:
    return {"name": name, "description": description,
            "input_schema": _object(properties, required)}


_TIME = {"type": "number", "minimum": -86400, "maximum": 86400}
_DURATION = {"type": "number", "exclusiveMinimum": 0, "maximum": 86400}
_CLOCK = {
    "oneOf": [
        {"type": "object", "required": ["mode", "bpm", "firstBeatSeconds"],
         "properties": {"mode": {"const": "fixed"},
                        "bpm": {"type": "number", "minimum": 20, "maximum": 400},
                        "firstBeatSeconds": {"type": "number", "minimum": 0, "maximum": 86400},
                        "offsetPips": {"type": "number"}}},
        {"type": "object", "required": ["mode", "pips_per_beat", "source_audio", "origin_beat", "beats"],
         "properties": {
             "mode": {"const": "variable"}, "pips_per_beat": {"const": 64},
             "source_audio": {"type": "object", "required": ["sample_rate"],
                              "properties": {"sample_rate": {"type": "integer", "minimum": 1, "maximum": 768000},
                                             "num_frames": {"type": "integer", "minimum": 2},
                                             "sha256": {"type": "string", "maxLength": 128}}},
             "origin_beat": {"type": "integer", "minimum": 0},
             "beats": {"type": "array", "minItems": 2, "maxItems": 25000,
                       "items": {"type": "object", "required": ["beat", "frame"],
                                 "properties": {"beat": {"type": "integer", "minimum": 0},
                                                "frame": {"type": "integer", "minimum": 0}}}},
         }},
    ]
}
_LYRIC_LINE = {"type": "object", "required": ["start"], "properties": {
    "id": {"type": "string", "maxLength": 256},
    "start": {"type": "number", "minimum": 0, "maximum": 86400},
    "end": {"type": "number", "minimum": 0, "maximum": 86400},
    "label": {"type": "string", "maxLength": 10000},
}}
_LYRIC_WORD = {"type": "object", "required": ["start", "end"], "properties": {
    **_LYRIC_LINE["properties"], "lineId": {"type": "string", "maxLength": 256},
}}

OPERATIONS = {
    "dancerudiments": [
        _operation("catalogue", "Read native movement descriptors, periods and dimensions; no motion engine fallback.", {
            "query": {"type": "string", "maxLength": 200},
            "offset": {"type": "integer", "minimum": 0, "maximum": 1000000},
            "limit": {"type": "integer", "minimum": 1, "maximum": 500},
        }),
        _operation("sample", "Sample a named native movement at signed integer pips (64 pips per beat).", {
            "name": {"type": "string", "minLength": 1, "maxLength": 256},
            "pips": {"type": "array", "minItems": 1, "maxItems": 4096,
                     "items": {"type": "integer", "minimum": -(2**31), "maximum": 2**31 - 1}},
        }, ("name", "pips")),
    ],
    "thumbmoves": [
        _operation("backend_info", "Inspect the native platform's cache-only thumbnail backend contract.", {}),
        _operation("cached_thumbnail", "Read an existing OS thumbnail for one workspace file; a miss never decodes the source.", {
            "path": {"type": "string", "minLength": 1, "maxLength": 4096},
            "max_size": {"type": "array", "minItems": 2, "maxItems": 2,
                         "items": {"type": "integer", "minimum": 1, "maximum": 1024}},
            "output_format": {"enum": ["JPEG", "PNG", "WEBP"]},
            "quality": {"type": "integer", "minimum": 1, "maximum": 95},
        }, ("path",)),
    ],
    "dancemoves": [
        _operation("validate_page_config", "Validate and normalize page/beat configuration with the installed DanceMoves API; no browser mount.", {
            "config": {"type": "object"},
        }, ("config",)),
        _operation("validate_timing_file", "Validate supplied UTF-8 cue/lyric text using the DanceMoves server API; no URL fetch or file write.", {
            "text": {"type": "string", "maxLength": MAX_INPUT_BYTES},
            "kind": {"enum": ["cue", "lyric"]},
            "filename": {"type": "string", "maxLength": 256},
        }, ("text",)),
        _operation("validate_motion_capture", "Validate an existing bounded motion capture using DanceMoves; no sensor capture or upload.", {
            "capture": {"type": "object"},
        }, ("capture",)),
    ],
    "react-timeline-sequence": [
        _operation("validate_beat_clock", "Validate a supplied fixed or sample-frame variable clock with the released timeline API.", {
            "clock": _CLOCK,
        }, ("clock",)),
        _operation("sample_beat_clock", "Return native phase/tempo at source seconds and optionally source seconds at pips; no audio analysis.", {
            "clock": _CLOCK,
            "seconds": {"type": "array", "minItems": 1, "maxItems": 2048, "items": _TIME},
            "pips": {"type": "array", "maxItems": 2048,
                     "items": {"type": "number", "minimum": -(2**31), "maximum": 2**31 - 1}},
        }, ("clock", "seconds")),
        _operation("match_beat", "Match a source time to the upstream clock; variable clocks use actual beat anchors.", {
            "clock": _CLOCK, "seconds": _TIME,
            "tolerance_seconds": {"type": "number", "minimum": 0, "maximum": 60},
        }, ("clock", "seconds")),
        _operation("beat_grid", "Produce a bounded display grid using the installed timeline API.", {
            "clock": _CLOCK, "start": _TIME, "end": _TIME,
            "limit": {"type": "integer", "minimum": 1, "maximum": 2000},
        }, ("clock", "start", "end")),
        _operation("lyric_state", "Read active lyric/word states at a source time using the timeline's optional lyric-audition API.", {
            "lines": {"type": "array", "maxItems": 5000, "items": _LYRIC_LINE},
            "words": {"type": "array", "maxItems": 10000, "items": _LYRIC_WORD},
            "seconds": _TIME, "duration": _DURATION,
        }, ("lines", "seconds", "duration")),
    ],
    "mediaslide": [],
    "dancevault": [],
    "epk-social-metadata": [],
}

INTEGRATIONS = {
    "mediaslide": {
        "kind": "browser-library", "package": "react-mediaslide",
        "api": ["MediaSlide", "version", "getVersion"],
        "prerequisites": ["React host with client-side mounting and an explicitly sized container",
                          "ResizeObserver and IntersectionObserver; stable item IDs and application pagination",
                          "Expected-frame and trusted-origin checks for active HTML slide messages"],
        "limits": ["No standalone MCP/CLI renderer or browser session is supplied by this adapter",
                   "Package discovery is not proof of a rendered gallery or installed website version"],
        "reference": "https://github.com/kieransimkin/react-mediaslide/blob/v1.1.26/README.md",
    },
    "dancevault": {
        "kind": "wordpress-plugin",
        "api": ["admin-post.php: dancevault_create", "admin-post.php: dancevault_revoke",
                "admin-post.php: dancevault_download"],
        "prerequisites": ["An explicitly selected WordPress/PHP host with sodium and HTTPS",
                          "Destination-host acceptance before private assets; protected upload/temporary storage",
                          "WordPress capability and nonce checks for create/revoke; recipient password for download"],
        "limits": ["No standalone CLI or REST API; no WordPress credentials or mutations through this adapter",
                   "No plaintext fallback, Range/resume, chunk uploader or email sending",
                   "Stable synthetic Apache/nginx acceptance does not approve a production host"],
        "reference": "https://github.com/kieransimkin/DanceVault/blob/v1.0.1/README.md",
    },
    "epk-social-metadata": {
        "kind": "wordpress-plugin",
        "api": ["WordPress page REST metadata: registered _ksem_* fields", "?ksem_player=PAGE_ID"],
        "prerequisites": ["WordPress 6.7+ and PHP 8.0+ with the exact plugin installed",
                          "Authenticated edit_post capability for protected page metadata",
                          "Verified canonical page, audio and independent public-video facts; one metadata owner"],
        "limits": ["No standalone CLI or configured WordPress account through this adapter",
                   "Saving/importing metadata and deploying the plugin require separate host operations",
                   "Valid markup does not prove search indexing, ranking or social-player delivery"],
        "reference": "https://github.com/kieransimkin/kieran-epk-social-metadata/blob/v1.2.5/README.md",
    },
}


class LibraryAdapters:
    def __init__(self, workspace: Path | None, node_executable: str = "node"):
        self.workspace = Path(workspace).resolve(strict=True) if workspace is not None else None
        if self.workspace is not None and not self.workspace.is_dir():
            raise ValueError("Workspace must be a directory")
        self.node_executable = node_executable

    def operations(self) -> dict:
        """Return schemas only; importing a native engine is deferred until run()."""
        return copy.deepcopy(OPERATIONS)

    def integration_descriptors(self) -> dict:
        return copy.deepcopy(INTEGRATIONS)

    @staticmethod
    def _python_runtime(package: str, module=None) -> dict:
        try:
            version = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            version = None
        return {"package": package, "version": version,
                "module_path": getattr(module, "__file__", None),
                "api_checked": module is not None}

    def _node_package(self, package: str) -> dict:
        if self.workspace is None:
            raise ValueError("Set DANCEFLOW_WORKSPACE or --workspace for workspace node_modules")
        package_path = self.workspace / "node_modules" / package
        root = package_path.resolve(strict=True)
        if not root.is_relative_to(self.workspace):
            raise ValueError("Node package resolves outside the selected workspace")
        manifest = (root / "package.json").resolve(strict=True)
        if not manifest.is_relative_to(root) or manifest.stat().st_size > 65536:
            raise ValueError("Unsafe or oversized Node package metadata")
        info = json.loads(manifest.read_text(encoding="utf-8"))
        if info.get("name") != package:
            raise ValueError("Installed Node package name does not match the fixed adapter")
        return {"package": package, "version": info.get("version"),
                "package_path": str(root), "api_checked": False}

    def available(self, component: str) -> dict:
        if component not in OPERATIONS:
            raise ValueError("Unknown library component")
        if component in INTEGRATIONS:
            return {"status": "integration_only",
                    "reason": "Use the documented browser or WordPress host; no server action is advertised.",
                    "integration": copy.deepcopy(INTEGRATIONS[component])}
        if component in PYTHON_PACKAGES:
            package = PYTHON_PACKAGES[component]
            try:
                spec = importlib.util.find_spec(package)
            except (ImportError, ValueError):
                spec = None
            if spec is None:
                return {"status": "unavailable", "reason": f"Optional Python package {package} is not installed."}
            return {"status": "installed_unverified",
                    "reason": "Module metadata found; the native API has not been imported or executed.",
                    "runtime": self._python_runtime(package)}
        if self.workspace is None:
            return {"status": "workspace_required", "reason": "Select a workspace with the installed npm package."}
        if not shutil.which(self.node_executable):
            return {"status": "unavailable", "reason": "Node.js is not available; no install was attempted."}
        try:
            runtime = self._node_package(NODE_PACKAGES[component])
        except (OSError, ValueError) as error:
            return {"status": "unavailable", "reason": str(error)}
        return {"status": "installed_unverified",
                "reason": "Workspace package metadata found; exports and Node compatibility are checked only when invoked.",
                "runtime": runtime}

    def _file(self, name: str) -> Path:
        if self.workspace is None:
            raise ValueError("Set DANCEFLOW_WORKSPACE or --workspace to a user-selected directory")
        requested = Path(name)
        path = (requested if requested.is_absolute() else self.workspace / requested).resolve(strict=True)
        if not path.is_relative_to(self.workspace):
            raise ValueError("File is outside the selected workspace")
        if not path.is_file():
            raise ValueError("Supply one individual file")
        return path

    @staticmethod
    def _module(package: str):
        try:
            # Optional libraries must never write diagnostics into MCP stdout.
            with contextlib.redirect_stdout(sys.stderr):
                return importlib.import_module(package)
        except ImportError as error:
            raise RuntimeError(f"Optional package {package} is unavailable: {error}") from error

    @staticmethod
    def _function(module, name: str):
        function = getattr(module, name, None)
        if not callable(function):
            raise RuntimeError(f"Installed package does not expose required API {name}; install a compatible release")
        return function

    def _rudiments(self, operation: str, arguments: dict) -> tuple[dict, dict, str]:
        native = self._module("dancerudiments")
        catalogue = self._function(native, "catalogue")()
        if getattr(native, "PIPS_PER_BEAT", None) != 64:
            raise RuntimeError("Installed DanceRudiments does not expose the expected 64-pip contract")
        if operation == "catalogue":
            query = arguments.get("query", "").casefold()
            rows = [row for row in catalogue if query in (str(row["name"]) + " " + str(row["description"])).casefold()]
            offset, limit = arguments.get("offset", 0), arguments.get("limit", 100)
            result = {"pips_per_beat": 64, "total": len(rows), "offset": offset,
                      "limit": limit, "items": rows[offset:offset + limit]}
        else:
            sample = self._function(native, "sample")
            descriptor = next((row for row in catalogue if row["name"] == arguments["name"]), None)
            result = {"pips_per_beat": 64, "name": arguments["name"], "descriptor": descriptor,
                      "samples": [{"pip": pip, "position": list(sample(arguments["name"], pip).as_tuple())}
                                  for pip in arguments["pips"]]}
        return result, self._python_runtime("dancerudiments", native), "ok"

    def _thumbnail(self, operation: str, arguments: dict) -> tuple[dict, dict, str]:
        # Reject path escapes before loading any optional backend.
        source = self._file(arguments["path"]) if operation == "cached_thumbnail" else None
        native = self._module("thumbmoves")
        info = self._function(native, "backend_info")()
        backend = {"name": info.name, "platform": info.platform,
                   "cache_only_supported": info.cache_only_supported, "notes": info.notes}
        runtime = self._python_runtime("thumbmoves", native)
        if operation == "backend_info":
            return backend, runtime, "ok"
        thumbnail = self._function(native, "get_cached_thumbnail")(
            source, max_size=tuple(arguments.get("max_size", [320, 240])),
            output_format=arguments.get("output_format", "JPEG"), quality=arguments.get("quality", 82))
        if thumbnail is None:
            return {"cache_hit": False, "cache_only": True, "backend": backend,
                    "path": str(source), "reason": "No existing thumbnail is available; the source was not decoded."}, runtime, "cache_miss"
        if thumbnail.cache_only is not True:
            raise RuntimeError("ThumbMoves returned a result without the required cache-only contract")
        if len(thumbnail.data) > MAX_THUMBNAIL_BYTES:
            raise ValueError("Cached thumbnail exceeds the two-MiB result limit; request a smaller size")
        result = {"cache_hit": True, "cache_only": True, "backend": backend,
                  "path": str(source), "size": list(thumbnail.size),
                  "output_format": thumbnail.output_format,
                  "mime_type": {"JPEG": "image/jpeg", "PNG": "image/png", "WEBP": "image/webp"}[thumbnail.output_format],
                  "bytes": len(thumbnail.data), "data_base64": base64.b64encode(thumbnail.data).decode("ascii")}
        return result, runtime, "ok"

    def _node(self, component: str, operation: str, arguments: dict) -> tuple[object, dict, str]:
        if not shutil.which(self.node_executable):
            raise RuntimeError("Node.js is unavailable; install the compatible runtime and selected workspace package explicitly")
        try:
            self._node_package(NODE_PACKAGES[component])
        except (OSError, ValueError) as error:
            raise RuntimeError(f"Optional workspace package is unavailable: {error}") from error
        environment = os.environ.copy()
        # Do not permit external preload scripts or global module search overrides.
        environment.pop("NODE_OPTIONS", None)
        environment.pop("NODE_PATH", None)
        request = json.dumps({"component": component, "operation": operation, "arguments": arguments}, allow_nan=False)
        returncode, stdout = self._node_process(request, environment)
        try:
            response = json.loads(stdout)
        except (ValueError, TypeError) as error:
            raise RuntimeError("Node library returned no valid bridge result; check the installed package and runtime") from error
        if not isinstance(response, dict):
            raise RuntimeError("Node library returned an invalid bridge result")
        if returncode != 0 or response.get("status") != "ok":
            failure = response.get("error", {})
            code = f" ({failure['code']})" if isinstance(failure.get("code"), str) else ""
            raise RuntimeError(f"{failure.get('name', 'NativeLibraryError')}{code}: {failure.get('message', 'Library call failed')}")
        return response["result"], response["runtime"], "ok"

    def _node_process(self, request: str, environment: dict) -> tuple[int, bytes]:
        """Bound both pipes while reading; a noisy installed package cannot fill memory."""
        process = subprocess.Popen(
            [self.node_executable, str(Path(__file__).with_name("library_bridge.mjs")), str(self.workspace)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            cwd=self.workspace, env=environment, shell=False,
        )
        output = bytearray()
        exceeded: list[str] = []

        def read(stream, limit, label, retained=None):
            size = 0
            with stream:
                while chunk := stream.read(65536):
                    size += len(chunk)
                    if size > limit:
                        exceeded.append(label)
                        if process.poll() is None:
                            process.kill()
                        break
                    if retained is not None:
                        retained.extend(chunk)

        def write():
            try:
                with process.stdin:
                    process.stdin.write(request.encode("utf-8"))
            except (BrokenPipeError, OSError):
                pass

        readers = [
            threading.Thread(target=read, args=(process.stdout, MAX_RESULT_BYTES, "stdout", output), daemon=True),
            threading.Thread(target=read, args=(process.stderr, MAX_NODE_DIAGNOSTIC_BYTES, "diagnostic output"), daemon=True),
            threading.Thread(target=write, daemon=True),
        ]
        for thread in readers:
            thread.start()
        timed_out = False
        try:
            process.wait(timeout=NODE_TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            timed_out = True
            process.kill()
            process.wait(timeout=3)
        finally:
            for thread in readers:
                thread.join(timeout=1)
        if timed_out:
            raise RuntimeError(f"Installed library did not finish the bounded Node call within {NODE_TIMEOUT_SECONDS} seconds")
        if exceeded:
            raise ValueError("Node library exceeded its bounded " + exceeded[0] + " limit")
        if any(thread.is_alive() for thread in readers):
            raise RuntimeError("Node library did not close its result streams")
        return process.returncode, bytes(output)

    def run(self, component: str, operation: str, arguments: dict) -> dict:
        selected = next((item for item in OPERATIONS.get(component, []) if item["name"] == operation), None)
        if selected is None:
            raise ValueError("Select a supported component/operation from library discovery")
        encoded = json.dumps(arguments, allow_nan=False).encode("utf-8")
        if len(encoded) > MAX_INPUT_BYTES:
            raise ValueError("Library arguments exceed one MiB")
        try:
            Draft202012Validator(selected["input_schema"]).validate(arguments)
        except ValidationError as error:
            location = ".".join(str(part) for part in error.absolute_path) or "arguments"
            # Avoid embedding full private inputs in a schema exception.
            raise ValueError(f"Invalid {location}: {error.validator} constraint failed") from None
        with contextlib.redirect_stdout(sys.stderr):
            if component == "dancerudiments":
                result, runtime, status = self._rudiments(operation, arguments)
            elif component == "thumbmoves":
                result, runtime, status = self._thumbnail(operation, arguments)
            else:
                result, runtime, status = self._node(component, operation, arguments)
        envelope = {"component": component, "operation": operation, "status": status,
                    "runtime": runtime, "result": result}
        if len(json.dumps(envelope, allow_nan=False).encode("utf-8")) > MAX_RESULT_BYTES:
            raise ValueError("Native library result exceeds four MiB; narrow the request")
        return envelope
