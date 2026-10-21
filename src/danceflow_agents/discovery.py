"""Bounded, read-only discovery across actual tools and canonical instructions.

The index contains no engine implementation and performs no tool invocation,
network request, package installation or model download. It searches the current
tool definitions and allowlisted public reference documents, not user assets.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import re

from .catalogue import (
    COMPONENT_SECTIONS, MAX_DOCUMENT_BYTES, OVERVIEW_PATHS, WORKFLOW_NAMES,
    EcosystemCatalogue, document_metadata,
)


SEARCH_KINDS = ("all", "component", "tool", "workflow", "skill", "reference")
MAX_QUERY_CHARACTERS = 512
MAX_SOURCE_DOCUMENTS = 512
MAX_SOURCE_ENTRIES = 4096
MAX_SOURCE_BYTES = 16 * 1024 * 1024
MAX_SNIPPET_CHARACTERS = 600
_KIND_ORDER = {name: number for number, name in enumerate(SEARCH_KINDS[1:])}
_STOP_WORDS = frozenset("a an and are as at be can do for from how i in is it my of on or the to use with".split())


def _call(tool_name: str, **arguments) -> dict:
    return {"tool": tool_name, "arguments": arguments}


def _tokens(value: str) -> list[str]:
    return list(dict.fromkeys(token for token in re.findall(r"[^\W_]+", value.casefold())
                              if token not in _STOP_WORDS))


class DiscoveryIndex:
    """An ephemeral index built from the hub's real, currently advertised tools.

    ``components`` are EcosystemBridge.component results; ``tools`` are MCP tool
    dictionaries using their wire aliases. The optional WorkflowMoves root is
    operator-owned configuration. It is never selected by a tool argument.
    """

    def __init__(self, catalogue: EcosystemCatalogue, components: list[dict],
                 tools: list[dict], workflowmoves_root: Path | str | None = None):
        self.catalogue = catalogue
        self.components = {row["name"]: deepcopy(row) for row in components}
        if len(self.components) != len(components):
            raise ValueError("Duplicate component identities in the discovery inventory")
        self._rows: dict[str, dict] = {}
        self._readable_bodies: dict[str, str] = {}
        self.coverage = {
            "components": {"count": len(components), "status": "catalogued"},
            "tools": {"count": len(tools), "status": "advertised_by_current_server",
                      "note": "Advertised schemas do not establish runtime readiness or successful execution."},
            "packaged_references": {"status": "complete", "count": 0, "issues": []},
            "workflowmoves": {"status": "not_configured", "count": 0, "issues": [],
                "note": "Set components.workflowmoves.source_root in the operator-owned runtime configuration to discover its canonical workflows and skills. No source checkout is downloaded by discovery.",
                "setup": _call("danceflow_read_reference", name="mcp", kind="overview")},
        }
        self._index_components()
        self._index_tools(tools)
        self._index_packaged_documents()
        if workflowmoves_root is not None:
            self._index_workflowmoves(Path(workflowmoves_root))

    def _add(self, row: dict, text: str = "") -> None:
        key = row["kind"] + ":" + row["id"]
        if key in self._rows:
            raise ValueError(f"Duplicate discovery identity: {key}")
        row["_body"] = text
        self._rows[key] = row

    def _index_components(self) -> None:
        for name, component in self.components.items():
            self._add({
                "id": name, "name": name, "kind": "component", "component": name,
                "title": component["title"], "summary": component["capabilities"],
                "runtime": deepcopy(component.get("runtime", {})),
                "references": deepcopy(component.get("resources", {})),
                "native_host_routes": deepcopy(component.get("native_host_routes", {})),
                "repository": component["repository"],
                "next_call": _call("danceflow_component", component=name),
            }, json.dumps(component, ensure_ascii=False, sort_keys=True))

    def _index_tools(self, tools: list[dict]) -> None:
        operation_details = {
            operation["tool"]: operation
            for component in self.components.values()
            for operation in component.get("operations", [])
        }
        for tool in tools:
            name = tool["name"]
            metadata = tool.get("_meta", {}) or {}
            component_name = metadata.get("danceflow/component")
            if component_name not in self.components:
                component_name = next((component for component in self.components
                    if name.startswith(component.replace("-", "_") + "_")), None)
            component = self.components.get(component_name, {})
            details = operation_details.get(name, {})
            row = {
                "id": name, "name": name, "tool": name, "kind": "tool",
                "component": component_name, "title": tool.get("title") or name,
                "summary": tool.get("description", ""),
                "input_schema": deepcopy(tool.get("inputSchema", tool.get("input_schema", {}))),
                "annotations": deepcopy(tool.get("annotations", {})),
                "execution": details.get("execution", metadata.get("danceflow/execution",
                    "native_mcp" if name.startswith("stemlab_") and not details else "mcp_tool")),
                "runtime": deepcopy(component.get("runtime", {})),
                "references": deepcopy(component.get("resources", {})),
                "next_call": (_call("danceflow_component", component=component_name) if component_name
                              else _call("danceflow_capabilities")),
                "invocation": {"tool": name, "arguments": "Supply an object matching input_schema; preserve its required permission and consent fields."},
            }
            output = tool.get("outputSchema", tool.get("output_schema"))
            if output is not None:
                row["output_schema"] = deepcopy(output)
            for field in ("effects", "conditional_effects", "notes", "source", "partial_exit_codes"):
                if field in details:
                    row[field] = deepcopy(details[field])
            self._add(row, json.dumps(tool, ensure_ascii=False, sort_keys=True))

    def _document(self, *, identifier: str, kind: str, text: str, source: dict,
                  component: str | None = None, uri: str | None = None,
                  section: str | None = None, workflow: bool = False) -> dict:
        row = {"id": identifier, "name": identifier, "kind": kind,
               "component": component, "source": source,
               **document_metadata(text, list(self.components.values())),
               "execution": "instructions_only", "untrusted_data": True}
        if component is not None and component not in row["related_components"]:
            row["related_components"].insert(0, component)
        if uri is not None:
            row["uri"] = uri
        if section is not None:
            row["section"] = section
        if workflow:
            if identifier in self._readable_bodies:
                raise ValueError(f"Duplicate workflow identity: {identifier}")
            if kind in ("workflow", "skill"):
                row["workflow_type"] = "portable_skill" if kind == "skill" else "guide"
            else:
                row["document_type"] = "reference"
            row["next_call"] = _call("danceflow_get_workflow", name=identifier)
            self._readable_bodies[identifier] = text
        elif component is not None:
            row["next_call"] = _call("danceflow_read_reference", name=component,
                                     kind="component", section=section)
        else:
            row["next_call"] = _call("danceflow_read_reference", name=identifier, kind="overview")
        self._add(row, text)
        return row

    @staticmethod
    def _source(provider: str, relative: str, text: str) -> dict:
        return {"provider": provider, "path": relative,
                "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                "identity": ("bundled_reference" if provider == "danceflow"
                             else "configured_local_source_release_unverified")}

    def _packaged(self, identifier: str, reader, **kwargs) -> None:
        try:
            text = reader()
            relative = kwargs.pop("relative")
            self._document(identifier=identifier, text=text, **kwargs,
                           source=self._source("danceflow", relative, text))
        except (OSError, UnicodeError, ValueError) as exc:
            status = self.coverage["packaged_references"]
            status["status"] = "partial"
            status["issues"].append({"name": identifier, "error": type(exc).__name__,
                                     "reason": "Bundled reference could not be read or indexed."})
        else:
            self.coverage["packaged_references"]["count"] += 1

    def _index_packaged_documents(self) -> None:
        for name in self.components:
            for section in COMPONENT_SECTIONS:
                relative = (f"plugins/danceflow/skills/{name}/SKILL.md" if section == "skill"
                            else f"docs/{'tools' if section == 'guide' else 'capabilities'}/{name}.md")
                self._packaged(f"{name}/{section}",
                    lambda n=name, s=section: self.catalogue.read_component(n, s),
                    kind="skill" if section == "skill" else "reference", component=name,
                    section=section, relative=relative,
                    uri=f"danceflow://components/{name}/{section}")
        for name in WORKFLOW_NAMES:
            self._packaged(name, lambda n=name: self.catalogue.read_workflow(n),
                kind="workflow", workflow=True, relative=f"docs/workflows/{name}.md",
                uri=f"danceflow://workflows/{name}")
        for name, relative in OVERVIEW_PATHS.items():
            self._packaged(name, lambda n=name: self.catalogue.read_overview(n),
                kind="reference", relative=relative, uri=f"danceflow://overview/{name}")

    def _index_workflowmoves(self, configured_root: Path) -> None:
        status = self.coverage["workflowmoves"]
        status.update(status="complete", note="WorkflowMoves instructions are read from the configured source checkout; local source is not proof of a released or approved version.")
        issues = status["issues"]
        try:
            root = configured_root.resolve(strict=True)
            if not root.is_dir():
                raise ValueError("Configured source is not a directory")
        except (OSError, ValueError, RuntimeError):
            status.update(status="unavailable", note="Configured WorkflowMoves source_root is missing, unreadable or cyclic; packaged DanceFlow discovery remains available.")
            return
        entries = documents = byte_count = indexed_bytes = 0
        stopped = False
        visited_directories = {root}

        def issue(path: str, reason: str) -> None:
            status["issue_count"] = status.get("issue_count", 0) + 1
            if len(issues) < 100:
                issues.append({"path": path, "reason": reason})
            else:
                status["issues_not_shown"] = status["issue_count"] - len(issues)
            status["status"] = "partial"

        for folder in ("workflows", "skills"):
            top = root / folder
            try:
                if top.is_symlink():
                    raise ValueError("Symlinked instruction directories are not followed")
                resolved_top = top.resolve(strict=True)
                if not resolved_top.is_relative_to(root) or resolved_top in visited_directories:
                    raise ValueError("Instruction directory escapes the source or repeats an already visited directory")
                if not resolved_top.is_dir():
                    raise ValueError("Instruction directory is not a directory")
            except (OSError, ValueError, RuntimeError) as exc:
                issue(folder, "Instruction directory unavailable: " + type(exc).__name__)
                continue
            visited_directories.add(resolved_top)
            def walk_error(exc):
                issue(folder, "Instruction directory could not be enumerated: " + type(exc).__name__)
            for directory, directories, files in os.walk(top, followlinks=False, onerror=walk_error):
                entries += len(directories) + len(files)
                if entries > MAX_SOURCE_ENTRIES:
                    issue(folder, f"Source entry limit {MAX_SOURCE_ENTRIES} reached; narrow the configured source.")
                    stopped = True
                    break
                directories.sort()
                safe_directories = []
                for child in directories:
                    path = Path(directory) / child
                    try:
                        if path.is_symlink():
                            raise ValueError("Symlinked instruction directories are not followed")
                        resolved_directory = path.resolve(strict=True)
                        if not resolved_directory.is_relative_to(root) or resolved_directory in visited_directories:
                            raise ValueError("Instruction directory escapes the source or repeats an already visited directory")
                    except (OSError, ValueError, RuntimeError) as exc:
                        issue(path.relative_to(root).as_posix(), "Instruction directory omitted: " + type(exc).__name__)
                    else:
                        visited_directories.add(resolved_directory)
                        safe_directories.append(child)
                directories[:] = safe_directories
                for filename in sorted(files):
                    if not filename.casefold().endswith(".md"):
                        continue
                    path = Path(directory) / filename
                    relative = path.relative_to(root).as_posix()
                    documents += 1
                    if documents > MAX_SOURCE_DOCUMENTS:
                        issue(relative, f"Source document limit {MAX_SOURCE_DOCUMENTS} reached; remaining instructions were not indexed.")
                        stopped = True
                        break
                    try:
                        if path.is_symlink():
                            raise ValueError("Symlinked instructions are not accepted")
                        resolved = path.resolve(strict=True)
                        if not resolved.is_relative_to(root):
                            raise ValueError("Instruction escapes the configured source")
                        if not resolved.is_file():
                            raise ValueError("Instruction is not a regular file")
                        with resolved.open("rb") as stream:
                            raw = stream.read(min(MAX_DOCUMENT_BYTES + 1,
                                                  MAX_SOURCE_BYTES - byte_count + 1))
                        byte_count += len(raw)
                        if byte_count > MAX_SOURCE_BYTES:
                            issue(relative, f"Source byte limit {MAX_SOURCE_BYTES} reached; remaining instructions were not indexed.")
                            stopped = True
                            break
                        if len(raw) > MAX_DOCUMENT_BYTES:
                            raise ValueError("Instruction exceeds the 1 MiB document limit")
                        text = raw.decode("utf-8")
                        skill = folder == "skills" and filename == "SKILL.md"
                        reference = ((folder == "skills" and not skill) or
                                     any(part.casefold() in ("capabilities", "references")
                                         for part in Path(relative).parts[:-1]))
                        kind = "reference" if reference else ("skill" if skill else "workflow")
                        suffix = Path(relative).parent.as_posix() if skill else str(Path(relative).with_suffix("")).replace("\\", "/")
                        # Keep the workflows/ or skills/ prefix to avoid aliases
                        # between nested guides and portable skills.
                        identifier = "workflowmoves/" + suffix
                        self._document(identifier=identifier, kind=kind,
                            text=text, source=self._source("workflowmoves", relative, text),
                            component="workflowmoves", workflow=True)
                    except (OSError, UnicodeError, ValueError, RuntimeError) as exc:
                        issue(relative, "Instruction omitted: " + type(exc).__name__)
                    else:
                        status["count"] += 1
                        indexed_bytes += len(raw)
                        status[kind + "_count"] = status.get(kind + "_count", 0) + 1
                if stopped:
                    break
            if stopped:
                break
        status["bytes_indexed"] = indexed_bytes
        status["bytes_read"] = byte_count
        status["limits"] = {"documents": MAX_SOURCE_DOCUMENTS, "entries": MAX_SOURCE_ENTRIES,
                            "total_bytes": MAX_SOURCE_BYTES, "document_bytes": MAX_DOCUMENT_BYTES}

    def _validate(self, query: str, kind: str, component: str | None, limit: int, offset: int) -> None:
        if not isinstance(query, str) or len(query) > MAX_QUERY_CHARACTERS:
            raise ValueError(f"query must be text of at most {MAX_QUERY_CHARACTERS} characters")
        if kind not in SEARCH_KINDS:
            raise ValueError("kind must be one of: " + ", ".join(SEARCH_KINDS))
        if component is not None and component not in self.components:
            raise ValueError("Unknown component; call danceflow_capabilities to list valid identifiers")
        if type(limit) is not int or not 1 <= limit <= 100:
            raise ValueError("limit must be an integer from 1 to 100")
        if type(offset) is not int or offset < 0:
            raise ValueError("offset must be a nonnegative integer")

    def _select(self, query: str, kind: str, component: str | None, limit: int, offset: int,
                *, workflows_only: bool = False) -> dict:
        self._validate(query, kind, component, limit, offset)
        terms = _tokens(query)
        ranked = []
        for row in self._rows.values():
            if workflows_only and (row["kind"] not in ("workflow", "skill") or
                                   row["id"] not in self._readable_bodies):
                continue
            if kind != "all" and row["kind"] != kind:
                continue
            if component is not None and component != row.get("component") and component not in row.get("related_components", []):
                continue
            title = (row["id"] + " " + row["title"]).casefold()
            summary = row["summary"].casefold()
            body = row["_body"].casefold()
            matched = [term for term in terms if term in title or term in summary or term in body]
            if terms and not matched:
                continue
            score = sum(8 * (term in title) + 4 * (term in summary) + (term in body) for term in matched)
            if terms and len(matched) == len(terms):
                score += 10
            if query.strip() and query.strip().casefold() == row["id"].casefold():
                score += 100
            ranked.append((-score, _KIND_ORDER[row["kind"]], row["id"], row, matched))
        ranked.sort(key=lambda value: value[:3])
        result = []
        for negative_score, _, _, row, matched in ranked[offset:offset + limit]:
            public = deepcopy({key: value for key, value in row.items() if not key.startswith("_")})
            text = " ".join(row["_body"].split())
            start = min((text.casefold().find(term) for term in matched if term in text.casefold()), default=0)
            start = max(0, start - 100)
            public.update(score=-negative_score, matched_terms=matched,
                          snippet=text[start:start + MAX_SNIPPET_CHARACTERS])
            result.append(public)
        total = len(ranked)
        next_offset = offset + len(result) if offset + len(result) < total else None
        return {"schema": "danceflow.discovery.v1", "query": query, "kind": kind,
                "component": component, "total": total, "offset": offset, "limit": limit,
                "has_more": next_offset is not None, "next_offset": next_offset,
                "results": result, "coverage": deepcopy(self.coverage),
                "search_method": "Local case-insensitive lexical matching across names, summaries, schemas and reference bodies; no semantic model or network search.",
                "next_page": (_call("danceflow_list_workflows" if workflows_only else "danceflow_search",
                    **{"query": query, "component": component, "limit": limit, "offset": next_offset},
                    **({} if workflows_only else {"kind": kind})) if next_offset is not None else None)}

    def search(self, query: str = "", kind: str = "all", component: str | None = None,
               limit: int = 20, offset: int = 0) -> dict:
        """Search every indexed capability; an empty query browses all records."""
        return self._select(query, kind, component, limit, offset)

    def list_workflows(self, query: str = "", component: str | None = None,
                       limit: int = 20, offset: int = 0) -> dict:
        """List packaged guides and configured WorkflowMoves guides/skill recipes."""
        return self._select(query, "all", component, limit, offset, workflows_only=True)

    def get_workflow(self, name: str) -> dict:
        """Read an advertised workflow/linked reference identity, never a path."""
        if not isinstance(name, str) or name not in self._readable_bodies:
            raise ValueError("Unknown or unavailable workflow; call danceflow_list_workflows and use an advertised name")
        row = next(row for row in self._rows.values()
                   if row["id"] == name and row["kind"] in ("workflow", "skill", "reference"))
        public = deepcopy({key: value for key, value in row.items() if not key.startswith("_")})
        public.update(content=self._readable_bodies[name], coverage=deepcopy(self.coverage),
                      related_component_calls=[_call("danceflow_component", component=component)
                                               for component in row["related_components"]],
                      note="This is an instruction document. Reading it does not execute a workflow, supply missing inputs or grant permission for its effects.")
        return public
