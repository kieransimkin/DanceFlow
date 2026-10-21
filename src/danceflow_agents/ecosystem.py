"""Compose the complete catalogue, canonical libraries, CLI jobs and native MCP."""
from __future__ import annotations

import atexit
from pathlib import Path
import threading

from .catalogue import EcosystemCatalogue
from .library_adapters import LibraryAdapters
from .native_mcp import NativeMCP
from .runtime import ComponentJobs, RuntimeConfig


class EcosystemBridge:
    def __init__(self, workspace: Path | None, runtime_config: Path | None = None):
        self.workspace = workspace
        self.catalogue = EcosystemCatalogue()
        self.config = RuntimeConfig({row["name"] for row in self.catalogue.components()}, runtime_config)
        self.libraries = LibraryAdapters(workspace, self.config.data.get("node", "node"))
        self.jobs = ComponentJobs(workspace, self.config)
        self._native: NativeMCP | None = None
        self._native_error: str | None = None
        self._lock = threading.Lock()
        atexit.register(self.close)

    def cli_operations(self) -> dict:
        from .cli_operations import OPERATIONS
        return OPERATIONS

    def component(self, name: str) -> dict:
        from .cli_operations import UNSUPPORTED_OPERATIONS
        row = self.catalogue.component(name)
        library_operations = self.libraries.operations()
        if name in library_operations:
            row["runtime"] = self.libraries.available(name)
        elif name == "pixelcue":
            row["runtime"] = {"status": "service_configured_unverified", "reason": "Call pixelcue_health to verify the configured loopback service"}
        else:
            row["runtime"] = self.config.availability(name)
        row["operations"] = [
            {"name": operation, "tool": tool_name(name, operation),
             "description": descriptor["description"], "input_schema": descriptor["input_schema"],
             "effects": descriptor.get("effects", []), "execution": "background_job",
             "conditional_effects": descriptor.get("conditional_effects", []),
             "partial_exit_codes": descriptor.get("partial_exit_codes", []),
             "source": descriptor.get("source"), "notes": descriptor.get("notes", [])}
            for operation, descriptor in self.cli_operations().get(name, {}).items()
        ]
        row["operations"].extend({**operation, "tool": tool_name(name, operation["name"]),
                                  "execution": "native_library"}
                                 for operation in library_operations.get(name, []))
        if name == "stemlab":
            row["native_mcp"] = {"status": "unavailable" if self._native_error else row["runtime"]["status"],
                                 "reason": self._native_error,
                                 "description": "Native stemlab_* tools are federated into tools/list when its codex extra is installed. Its job, consent and artifact semantics are preserved.",
                                 "guide": "danceflow://native/stemlab/guide"}
        if name == "keywordmoves":
            row["existing_tools"] = ["keywordmoves_run"]
        if name == "pixelcue":
            row["existing_tools"] = ["pixelcue_health", "pixelcue_keywords", "pixelcue_visual_analysis"]
        row["native_host_routes"] = UNSUPPORTED_OPERATIONS.get(name, {})
        return row

    def capabilities(self) -> dict:
        rows = []
        for component in self.catalogue.components():
            detail = self.component(component["name"])
            rows.append({**component, "runtime": detail["runtime"],
                         "tools": [op["tool"] for op in detail["operations"]] + detail.get("existing_tools", []),
                         **({"native_mcp": detail["native_mcp"]} if "native_mcp" in detail else {})})
        return {"schema": "danceflow.ecosystem.v1", "components": rows,
                "workflows": self.catalogue.workflows(), "overviews": self.catalogue.overviews(),
                "limits": ["Catalogue coverage, runtime availability, invocation and reviewed output are separate states.",
                           "Browser UI and WordPress plugins require their documented hosts; resources do not simulate those hosts.",
                           "Optional packages, services, GPU models and Node peers are installed separately.",
                           "Native project files are trusted configuration. This adapter is not an operating-system sandbox."]}

    def native(self) -> NativeMCP | None:
        with self._lock:
            if self._native_error or self.workspace is None:
                return None
            if self._native is None:
                if self.config.availability("stemlab")["status"] == "unavailable":
                    return None
                args = ["-I", "-m", "stemlab.codex", "serve", "--workspace", str(self.workspace)]
                if self.config.component("stemlab").get("read_only"):
                    args.append("--read-only")
                self._native = NativeMCP(self.config.python("stemlab"), args, self.workspace,
                                         environment=self.config.environment("stemlab", self.workspace))
            return self._native

    def native_tools(self) -> list:
        provider = self.native()
        if provider is None:
            return []
        try:
            return provider.tools()
        except Exception as exc:
            # A missing optional engine must not take down unrelated tools.
            self._native_error = f"{type(exc).__name__}: native StemLab MCP is unavailable; inspect its runtime and restart after repair"
            provider.close()
            return []

    def native_guide(self) -> str:
        self.native_tools()
        provider = self.native()
        if provider is None:
            return "Native StemLab MCP unavailable. Install its codex extra in the selected runtime; no installation or model download is performed by discovery."
        return provider.instructions

    def close(self) -> None:
        self.jobs.close()
        if self._native is not None:
            self._native.close()


def tool_name(component: str, operation: str) -> str:
    return component.replace("-", "_") + "_" + operation.replace("-", "_")
