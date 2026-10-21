"""Read the shipped ecosystem references without importing or running an engine."""
from __future__ import annotations

from copy import deepcopy
from importlib import metadata
import json
from pathlib import Path
import re


DISTRIBUTION_NAME = "danceflow-agent-tools"
DATA_DIRECTORY = "share/danceflow-agent-tools"
MAX_DOCUMENT_BYTES = 1024 * 1024
COMPONENT_SECTIONS = ("capabilities", "skill", "guide")
WORKFLOW_NAMES = (
    "framerudiments",
    "framerudiments-complete",
    "framerudiments-media",
    "likenessforge",
    "release-preflight",
    "tool-onboarding",
    "visual-language",
)
OVERVIEW_PATHS = {
    "mcp": "docs/mcp-ecosystem.md",
    "ecosystem": "docs/ecosystem.md",
    "capabilities": "docs/capabilities/index.md",
    "toolkit": "docs/capabilities/toolkit.md",
    "setup": "plugins/danceflow/skills/setup/SKILL.md",
}
_IDENTIFIER = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def document_metadata(content: str, components: list[dict]) -> dict:
    """Describe the actual shipped document without a second workflow inventory.

    Component mentions are related references, never inferred dependencies or
    permission to execute their tools. Markdown remains the source of truth.
    """
    def plain(value: str) -> str:
        value = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", value)
        value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
        return " ".join(value.replace("`", "").replace("**", "").split())

    lines = content.splitlines()
    if lines:
        lines[0] = lines[0].lstrip("\ufeff")
    title = next((plain(line.lstrip("# ")) for line in lines
                  if re.match(r"^#{1,6}\s+\S", line)), "Untitled reference")
    # Agent Skills descriptions provide better routing text than a setup heading.
    summary = ""
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if line.startswith("description:"):
                summary = plain(line.partition(":")[2].strip().strip("\"'"))
                if summary in ("|", ">", "|-", ">-"):
                    summary = ""
                break
    if not summary:
        paragraph = []
        fenced = False
        frontmatter = bool(lines and lines[0].strip() == "---")
        for number, line in enumerate(lines):
            stripped = line.strip()
            if frontmatter:
                if number and stripped == "---":
                    frontmatter = False
                continue
            if stripped.startswith(("```", "~~~")):
                fenced = not fenced
                continue
            if fenced:
                continue
            if not stripped:
                if paragraph:
                    break
                continue
            if stripped.startswith(("#", "![", "|", "<!--")):
                continue
            if not paragraph and (stripped.casefold().startswith("website:") or
                                  re.fullmatch(r"<?https?://\S+>?", stripped)):
                continue
            paragraph.append(stripped)
        summary = plain(" ".join(paragraph))
    related = []
    folded = content.casefold()
    for component in components:
        if any(re.search(r"(?<!\w)" + re.escape(value.casefold()) + r"(?!\w)", folded)
               for value in (component["name"], component["title"])):
            related.append(component["name"])
    return {"title": title, "summary": summary[:600], "related_components": related}


def _data_root() -> Path:
    """Resolve this checkout or this distribution's installed data-file record."""
    module = Path(__file__).resolve()
    source = module.parents[2]
    if (source / "src" / "danceflow_agents").resolve() == module.parent:
        if (source / "catalogue.json").is_file():
            return source

    # pip --target relocates data beside the package without rewriting its
    # original ../../share RECORD entries. Anchor this fallback to this module,
    # never the caller's working directory or a global installation prefix.
    relocated = module.parents[1] / DATA_DIRECTORY
    if (relocated / "catalogue.json").is_file():
        return relocated

    try:
        distribution = metadata.distribution(DISTRIBUTION_NAME)
    except metadata.PackageNotFoundError as exc:
        raise FileNotFoundError(
            "DanceFlow reference data is missing; install danceflow-agent-tools or use its source checkout"
        ) from exc
    for entry in distribution.files or ():
        if tuple(entry.parts[-3:]) == ("share", DISTRIBUTION_NAME, "catalogue.json"):
            catalogue = Path(distribution.locate_file(entry)).resolve()
            if catalogue.is_file():
                return catalogue.parent
    raise FileNotFoundError(
        "The installed DanceFlow distribution is missing its catalogue and reference data; reinstall it"
    )


def _check_identifier(name: str) -> None:
    if not isinstance(name, str) or len(name) > 64 or not _IDENTIFIER.fullmatch(name):
        raise ValueError("Reference identifiers must be lowercase names separated by single hyphens")


class EcosystemCatalogue:
    """An allowlisted, bounded view of the toolkit's bundled public documentation.

    The root override is for embedding and tests, never a client-supplied workspace.
    Neither selecting a component nor reading its references proves it is installed.
    """

    def __init__(self, root: Path | None = None):
        self.root = (Path(root) if root is not None else _data_root()).resolve(strict=True)
        if not self.root.is_dir():
            raise ValueError("DanceFlow reference data root must be a directory")
        catalogue = json.loads(self._read("catalogue.json"))
        if not isinstance(catalogue, list) or not catalogue:
            raise ValueError("DanceFlow catalogue must be a nonempty list of components")
        self._components: dict[str, dict] = {}
        for component in catalogue:
            if not isinstance(component, dict):
                raise ValueError("Every DanceFlow catalogue component must be an object")
            name = component.get("name")
            _check_identifier(name)
            if name in self._components:
                raise ValueError(f"Duplicate DanceFlow component: {name}")
            for field in ("title", "repository", "website", "capabilities"):
                if not isinstance(component.get(field), str) or not component[field].strip():
                    raise ValueError(f"DanceFlow component {name} is missing its {field}")
            if not isinstance(component.get("experimental"), bool):
                raise ValueError(f"DanceFlow component {name} needs an experimental boolean")
            self._components[name] = component

    def _read(self, relative: str) -> str:
        path = (self.root / relative).resolve(strict=True)
        if not path.is_relative_to(self.root):
            raise ValueError("DanceFlow reference must stay inside its installed data directory")
        if not path.is_file():
            raise ValueError("DanceFlow reference must be a regular file")
        with path.open("rb") as stream:
            content = stream.read(MAX_DOCUMENT_BYTES + 1)
        if len(content) > MAX_DOCUMENT_BYTES:
            raise ValueError("DanceFlow reference exceeds the 1 MiB document limit")
        return content.decode("utf-8")

    def component(self, name: str) -> dict:
        """Return canonical identity, capability summary and discoverable resource URIs."""
        _check_identifier(name)
        if name not in self._components:
            raise ValueError(f"Unknown DanceFlow component: {name}")
        component = deepcopy(self._components[name])
        component["resources"] = {
            section: f"danceflow://components/{name}/{section}"
            for section in COMPONENT_SECTIONS
        }
        return component

    def components(self) -> list[dict]:
        """List the complete canonical ecosystem in catalogue order."""
        return [self.component(name) for name in self._components]

    def read_component(self, name: str, section: str = "capabilities") -> str:
        """Read a component capability reference, portable skill or integration guide."""
        self.component(name)
        if section not in COMPONENT_SECTIONS:
            raise ValueError("Component section must be capabilities, skill or guide")
        paths = {
            "capabilities": f"docs/capabilities/{name}.md",
            "skill": f"plugins/danceflow/skills/{name}/SKILL.md",
            "guide": f"docs/tools/{name}.md",
        }
        return self._read(paths[section])

    def read_workflow(self, name: str) -> str:
        """Read one shipped workflow guide by its advertised identifier."""
        _check_identifier(name)
        if name not in WORKFLOW_NAMES:
            raise ValueError(f"Unknown DanceFlow workflow: {name}")
        return self._read(f"docs/workflows/{name}.md")

    def workflows(self) -> list[dict]:
        """List shipped workflow guides with summaries drawn from their bodies."""
        return [
            {"name": name, "uri": f"danceflow://workflows/{name}",
             **document_metadata(self.read_workflow(name), self.components()),
             "execution": "instructions_only",
             "next_call": {"tool": "danceflow_get_workflow", "arguments": {"name": name}}}
            for name in WORKFLOW_NAMES
        ]

    def read_overview(self, name: str = "ecosystem") -> str:
        """Read a shared ecosystem, capability, toolkit or setup reference."""
        _check_identifier(name)
        if name not in OVERVIEW_PATHS:
            raise ValueError(f"Unknown DanceFlow overview: {name}")
        return self._read(OVERVIEW_PATHS[name])

    def overviews(self) -> list[dict]:
        """List shared reference identifiers and resource URIs."""
        return [
            {"name": name, "uri": f"danceflow://overview/{name}"}
            for name in OVERVIEW_PATHS
        ]
