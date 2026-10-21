"""Ecosystem references must be complete, bounded and available after installation."""
from importlib import metadata
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from danceflow_agents import catalogue as catalogue_module
from danceflow_agents.catalogue import (
    COMPONENT_SECTIONS,
    EcosystemCatalogue,
    MAX_DOCUMENT_BYTES,
    OVERVIEW_PATHS,
    WORKFLOW_NAMES,
)

try:
    import tomllib
except ImportError:
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1]
SAMPLE_COMPONENT = {
    "name": "pixelcue",
    "title": "PixelCue",
    "repository": "https://github.com/kieransimkin/PixelCue",
    "website": "https://kieransimkin.co.uk/danceflow/",
    "capabilities": "Local visual evidence",
    "experimental": False,
}


def make_data_root(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    (root / "catalogue.json").write_text(json.dumps([SAMPLE_COMPONENT]), encoding="utf-8")
    reference = root / "docs/capabilities/pixelcue.md"
    reference.parent.mkdir(parents=True)
    reference.write_text("# PixelCue\n\nSynthetic public reference.\n", encoding="utf-8")
    return root


def test_full_catalogue_and_every_component_reference_are_available():
    catalogue = EcosystemCatalogue()
    expected = json.loads((ROOT / "catalogue.json").read_text("utf-8"))
    assert [entry["name"] for entry in catalogue.components()] == [entry["name"] for entry in expected]
    for component in expected:
        name = component["name"]
        actual = catalogue.component(name)
        assert {key: actual[key] for key in component} == component
        paths = {
            "capabilities": ROOT / f"docs/capabilities/{name}.md",
            "skill": ROOT / f"plugins/danceflow/skills/{name}/SKILL.md",
            "guide": ROOT / f"docs/tools/{name}.md",
        }
        for section in COMPONENT_SECTIONS:
            assert actual["resources"][section] == f"danceflow://components/{name}/{section}"
            assert catalogue.read_component(name, section) == paths[section].read_text("utf-8")


def test_all_workflows_and_shared_overviews_are_discoverable():
    catalogue = EcosystemCatalogue()
    assert set(WORKFLOW_NAMES) == {path.stem for path in (ROOT / "docs/workflows").glob("*.md")}
    assert catalogue.workflows() == [
        {"name": name, "uri": f"danceflow://workflows/{name}"} for name in WORKFLOW_NAMES
    ]
    for name in WORKFLOW_NAMES:
        assert catalogue.read_workflow(name) == (ROOT / f"docs/workflows/{name}.md").read_text("utf-8")
    assert catalogue.overviews() == [
        {"name": name, "uri": f"danceflow://overview/{name}"} for name in OVERVIEW_PATHS
    ]
    for name, relative in OVERVIEW_PATHS.items():
        assert catalogue.read_overview(name) == (ROOT / relative).read_text("utf-8")


def test_caller_cannot_mutate_catalogue_or_resource_identities():
    catalogue = EcosystemCatalogue()
    original = catalogue.component("pixelcue")
    changed = catalogue.component("pixelcue")
    changed["capabilities"] = "changed"
    changed["resources"]["guide"] = "file:///private"
    assert catalogue.component("pixelcue") == original


def test_source_discovery_does_not_depend_on_working_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert EcosystemCatalogue().root == ROOT


@pytest.mark.parametrize("layout", ["prefix", "target"])
def test_installed_data_discovery_handles_prefix_and_relocated_target(tmp_path, monkeypatch, layout):
    # Wheel data files can be above site-packages or alongside a --target installation.
    if layout == "prefix":
        distribution_base = tmp_path / "environment/lib/python3.12/site-packages"
        entry = metadata.PackagePath("../../../share/danceflow-agent-tools/catalogue.json")
    else:
        distribution_base = tmp_path / "target"
        entry = metadata.PackagePath("../../share/danceflow-agent-tools/catalogue.json")
    distribution_base.mkdir(parents=True)
    installed_root = make_data_root(
        (distribution_base / entry).resolve().parent if layout == "prefix"
        else distribution_base / "share/danceflow-agent-tools"
    )
    monkeypatch.setattr(catalogue_module, "__file__", str(distribution_base / "danceflow_agents/catalogue.py"))
    seen = []

    def distribution(name):
        seen.append(name)
        return SimpleNamespace(files=[entry], locate_file=lambda file: distribution_base / file)

    monkeypatch.setattr(catalogue_module.metadata, "distribution", distribution)
    catalogue = EcosystemCatalogue()
    assert seen == (["danceflow-agent-tools"] if layout == "prefix" else [])
    assert catalogue.root == installed_root
    assert catalogue.read_component("pixelcue").startswith("# PixelCue")


def test_missing_installed_resources_fail_clearly(tmp_path, monkeypatch):
    monkeypatch.setattr(catalogue_module, "__file__", str(tmp_path / "site-packages/danceflow_agents/catalogue.py"))
    monkeypatch.setattr(catalogue_module.metadata, "distribution", lambda name: SimpleNamespace(files=[]))
    with pytest.raises(FileNotFoundError, match="missing its catalogue"):
        EcosystemCatalogue()


@pytest.mark.parametrize("name", ["../pixelcue", r"..\pixelcue", "/etc/passwd", "C:private", "%2e%2e", "PixelCue", "pixelcue/guide", "", "x" * 65, "unlisted"])
def test_component_and_workflow_identifiers_cannot_select_arbitrary_paths(name):
    catalogue = EcosystemCatalogue()
    for reader in (catalogue.read_component, catalogue.read_workflow, catalogue.read_overview):
        with pytest.raises(ValueError):
            reader(name)


def test_component_section_is_allowlisted():
    with pytest.raises(ValueError, match="section"):
        EcosystemCatalogue().read_component("pixelcue", "../../../private")


def test_reference_symlink_cannot_escape_data_root(tmp_path):
    root = make_data_root(tmp_path / "data")
    reference = root / "docs/capabilities/pixelcue.md"
    reference.unlink()
    outside = tmp_path / "private.md"
    outside.write_text("Private", encoding="utf-8")
    try:
        reference.symlink_to(outside)
    except (NotImplementedError, OSError) as exc:
        pytest.skip(f"Symlinks unavailable in this test environment: {exc}")
    with pytest.raises(ValueError, match="inside its installed data directory"):
        EcosystemCatalogue(root).read_component("pixelcue")


def test_reference_reads_are_bounded_in_bytes(tmp_path):
    root = make_data_root(tmp_path / "data")
    (root / "docs/capabilities/pixelcue.md").write_bytes(b"x" * (MAX_DOCUMENT_BYTES + 1))
    with pytest.raises(ValueError, match="1 MiB"):
        EcosystemCatalogue(root).read_component("pixelcue")


@pytest.mark.parametrize("value", [
    [],
    {},
    [None],
    [SAMPLE_COMPONENT, SAMPLE_COMPONENT],
    [dict(SAMPLE_COMPONENT, name="../escape")],
    [dict(SAMPLE_COMPONENT, title="")],
    [dict(SAMPLE_COMPONENT, experimental="false")],
])
def test_invalid_catalogue_fails_before_discovery(tmp_path, value):
    root = make_data_root(tmp_path / "data")
    (root / "catalogue.json").write_text(json.dumps(value), encoding="utf-8")
    with pytest.raises(ValueError):
        EcosystemCatalogue(root)


def test_every_advertised_reference_is_in_wheel_data_files():
    project = tomllib.loads((ROOT / "pyproject.toml").read_text("utf-8"))
    data_files = project["tool"]["setuptools"]["data-files"]
    destinations = set()
    for destination, patterns in data_files.items():
        for pattern in patterns:
            for source in ROOT.glob(pattern):
                destinations.add(f"{destination}/{source.name}")
    required = {"catalogue.json", *OVERVIEW_PATHS.values()}
    for component in EcosystemCatalogue().components():
        name = component["name"]
        required.update({
            f"docs/capabilities/{name}.md",
            f"docs/tools/{name}.md",
            f"plugins/danceflow/skills/{name}/SKILL.md",
        })
    required.update(f"docs/workflows/{name}.md" for name in WORKFLOW_NAMES)
    assert {f"share/danceflow-agent-tools/{relative}" for relative in required} <= destinations
