"""Discovery must work without engine execution or prior knowledge of an ID."""
from copy import deepcopy
import hashlib
from pathlib import Path

import pytest

from danceflow_agents.catalogue import EcosystemCatalogue, WORKFLOW_NAMES, document_metadata
from danceflow_agents import discovery
from danceflow_agents.discovery import DiscoveryIndex


def make_index(source=None, tools=None, catalogue=None):
    catalogue = catalogue or EcosystemCatalogue()
    components = catalogue.components()
    for component in components:
        component["runtime"] = {"status": "unavailable", "reason": "Synthetic test inventory"}
    return DiscoveryIndex(catalogue, components, tools or [], source)


def make_source(tmp_path):
    source = tmp_path / "WorkflowMoves"
    (source / "workflows/nested").mkdir(parents=True)
    (source / "skills/colour-review").mkdir(parents=True)
    return source


def test_browse_exposes_every_component_and_shipped_reference_without_ids():
    index = make_index()
    components = index.search(kind="component", limit=100)
    assert components["total"] == 15
    assert {row["id"] for row in components["results"]} == {
        component["name"] for component in index.catalogue.components()}
    assert all(row["next_call"]["tool"] == "danceflow_component" for row in components["results"])
    assert index.search(kind="skill", limit=100)["total"] == 15
    coverage = components["coverage"]
    assert coverage["packaged_references"] == {"status": "complete", "count": 57, "issues": []}
    assert coverage["workflowmoves"]["status"] == "not_configured"
    assert coverage["workflowmoves"]["setup"]["tool"] == "danceflow_read_reference"


def test_every_page_is_reachable_once_and_workflows_do_not_include_tools_or_components():
    index = make_index()
    first = index.search(limit=9)
    found = []
    page = first
    while True:
        found.extend((row["kind"], row["id"]) for row in page["results"])
        if not page["has_more"]:
            assert page["next_offset"] is None and page["next_page"] is None
            break
        assert page["next_page"]["tool"] == "danceflow_search"
        page = index.search(**page["next_page"]["arguments"])
    assert len(found) == first["total"] == len(set(found))
    assert index.search(limit=9) == first
    workflows = index.list_workflows(limit=100)
    assert workflows["total"] == len(WORKFLOW_NAMES)
    assert {row["name"] for row in workflows["results"]} == set(WORKFLOW_NAMES)
    assert all(row["kind"] == "workflow" and row["execution"] == "instructions_only"
               for row in workflows["results"])
    assert index.search(offset=10000)["results"] == []


def test_actual_manual_and_native_tool_definitions_are_searchable_with_exact_schemas():
    tools = [
        {"name": "pixelcue_health", "description": "Read the existing local service health.",
         "inputSchema": {"type": "object", "properties": {}},
         "annotations": {"readOnlyHint": True}},
        {"name": "stemlab_future_feature", "description": "Inspect beat anchors and rubato.",
         "inputSchema": {"type": "object", "properties": {"anchor_sample": {"type": "integer"}},
                         "required": ["anchor_sample"], "additionalProperties": False},
         "outputSchema": {"type": "object", "properties": {"ok": {"type": "boolean"}}}},
    ]
    index = make_index(tools=tools)
    native = index.search(query="stemlab_future_feature", kind="tool")["results"][0]
    assert native["tool"] == "stemlab_future_feature"
    assert native["execution"] == "native_mcp" and native["component"] == "stemlab"
    assert native["input_schema"] == tools[1]["inputSchema"]
    assert native["output_schema"] == tools[1]["outputSchema"]
    assert native["next_call"] == {"tool": "danceflow_component", "arguments": {"component": "stemlab"}}
    assert index.search(query="rubato", kind="tool")["total"] == 1
    assert index.search(query="anchor_sample", kind="tool")["total"] == 1
    assert index.search(kind="tool")["total"] == 2
    native["input_schema"].clear()
    assert index.search(query="stemlab_future_feature", kind="tool")["results"][0]["input_schema"]


def test_keyword_search_reaches_reference_bodies_and_host_dependent_components():
    index = make_index()
    result = index.search(query="butterchurn", kind="workflow", limit=100)
    assert "framerudiments-complete" in {row["id"] for row in result["results"]}
    assert all(len(row["snippet"]) <= discovery.MAX_SNIPPET_CHARACTERS for row in result["results"])
    for component in ("mediaslide", "dancevault", "epk-social-metadata"):
        found = index.search(kind="component", component=component)["results"]
        assert len(found) == 1 and found[0]["runtime"]["status"] == "unavailable"
        assert found[0]["references"]["guide"]


def test_shipped_workflow_get_preserves_body_and_reads_are_not_execution():
    index = make_index()
    result = index.get_workflow("visual-language")
    assert result["content"] == index.catalogue.read_workflow("visual-language")
    assert result["title"] == "Image evidence and visual-language profiles"
    assert result["execution"] == "instructions_only"
    assert "pixelcue" in result["related_components"]
    assert result["related_component_calls"]
    with pytest.raises(ValueError, match="advertised name"):
        index.get_workflow("../../private.md")


def test_canonical_workflows_and_skills_keep_unicode_crlf_identity_and_namespaces(tmp_path):
    source = make_source(tmp_path)
    first = "# Crème workflow\r\n\r\nReview café colours with PixelCue.\r\n"
    (source / "workflows/colour.md").write_bytes(first.encode("utf-8"))
    (source / "workflows/nested/colour.md").write_text("# Other colour guide\n\nCompare retained evidence.", encoding="utf-8")
    (source / "skills/colour-review/SKILL.md").write_text(
        "---\nname: colour-review\ndescription: Review café colour families.\n---\n# Colour review\n\nRead approved inputs.", encoding="utf-8")
    index = make_index(source)
    listed = index.list_workflows(limit=100)
    assert listed["total"] == len(WORKFLOW_NAMES) + 3
    assert listed["coverage"]["workflowmoves"]["status"] == "complete"
    assert listed["coverage"]["workflowmoves"]["count"] == 3
    identifier = "workflowmoves/workflows/colour"
    result = index.get_workflow(identifier)
    assert result["content"] == first
    assert result["source"]["path"] == "workflows/colour.md"
    assert result["source"]["sha256"] == hashlib.sha256(first.encode("utf-8")).hexdigest()
    assert result["next_call"] == {"tool": "danceflow_get_workflow", "arguments": {"name": identifier}}
    assert "pixelcue" in result["related_components"]
    search = index.search(query="CAFÉ", component="workflowmoves", limit=100)
    assert {row["name"] for row in search["results"]} == {
        identifier, "workflowmoves/skills/colour-review"}
    skill = index.get_workflow("workflowmoves/skills/colour-review")
    assert skill["kind"] == "skill" and skill["workflow_type"] == "portable_skill"


def test_source_symlink_escape_and_nonadvertised_paths_cannot_be_read(tmp_path):
    source = make_source(tmp_path)
    outside = tmp_path / "private"
    outside.mkdir()
    (outside / "private.md").write_text("externaluniquesecret987654321", encoding="utf-8")
    try:
        (source / "workflows/escape.md").symlink_to(outside / "private.md")
        (source / "workflows/escape-dir").symlink_to(outside, target_is_directory=True)
    except (OSError, NotImplementedError):
        pytest.skip("This platform does not permit creating test symlinks")
    index = make_index(source)
    status = index.list_workflows()["coverage"]["workflowmoves"]
    assert status["status"] == "partial" and status["issue_count"] == 2
    assert index.search("externaluniquesecret987654321", component="workflowmoves")["total"] == 0
    for name in ("workflowmoves/workflows/escape", str(outside / "private.md"),
                 "workflowmoves/../../private/private", "workflowmoves/workflows/escape-dir/private"):
        with pytest.raises(ValueError, match="advertised name"):
            index.get_workflow(name)


def test_self_symlink_instruction_is_omitted_without_hiding_valid_discovery(tmp_path):
    source = make_source(tmp_path)
    body = "# Valid workflow\r\n\r\nRetained public instructions.\r\n"
    (source / "workflows/valid.md").write_bytes(body.encode("utf-8"))
    loop = source / "workflows/loop.md"
    try:
        loop.symlink_to(loop.name)
    except (OSError, NotImplementedError):
        pytest.skip("This platform does not permit creating test symlinks")
    index = make_index(source)
    result = index.list_workflows(limit=100)
    status = result["coverage"]["workflowmoves"]
    assert status["status"] == "partial" and status["count"] == 1
    assert status["issues"][0]["path"] == "workflows/loop.md"
    assert result["total"] == len(WORKFLOW_NAMES) + 1
    valid = index.get_workflow("workflowmoves/workflows/valid")
    assert valid["content"] == body
    assert valid["source"]["sha256"] == hashlib.sha256(body.encode("utf-8")).hexdigest()
    assert index.search(kind="component")["total"] == 15


def test_looped_configured_source_is_unavailable_without_breaking_packaged_discovery(tmp_path):
    loop = tmp_path / "looped-source"
    try:
        loop.symlink_to(loop.name, target_is_directory=True)
    except (OSError, NotImplementedError):
        pytest.skip("This platform does not permit creating test symlinks")
    index = make_index(loop)
    result = index.list_workflows(limit=100)
    status = result["coverage"]["workflowmoves"]
    assert status["status"] == "unavailable" and status["count"] == 0
    assert result["total"] == len(WORKFLOW_NAMES)
    assert result["coverage"]["packaged_references"]["status"] == "complete"
    assert index.search(kind="component")["total"] == 15


def test_looped_instruction_folder_does_not_hide_other_source_folders(tmp_path):
    source = tmp_path / "WorkflowMoves"
    (source / "skills/valid").mkdir(parents=True)
    (source / "skills/valid/SKILL.md").write_text("# Valid skill\n\nRetain original assets.", encoding="utf-8")
    loop = source / "workflows"
    try:
        loop.symlink_to(loop.name, target_is_directory=True)
    except (OSError, NotImplementedError):
        pytest.skip("This platform does not permit creating test symlinks")
    index = make_index(source)
    result = index.list_workflows(limit=100)
    status = result["coverage"]["workflowmoves"]
    assert status["status"] == "partial" and status["count"] == 1
    assert status["issues"][0]["path"] == "workflows"
    assert index.get_workflow("workflowmoves/skills/valid")["kind"] == "skill"
    assert result["total"] == len(WORKFLOW_NAMES) + 1


def test_directory_resolution_escape_is_pruned_before_enumeration(tmp_path, monkeypatch):
    source = make_source(tmp_path)
    alias = source / "workflows/junction-like"
    alias.mkdir()
    (alias / "never-read.md").write_text("junctionoutsideuniquesentinel", encoding="utf-8")
    outside = tmp_path / "outside"
    outside.mkdir()
    original_resolve = Path.resolve
    def resolve(path, *args, **kwargs):
        # A Windows junction may resolve elsewhere without is_symlink() being
        # true. Exercise the same boundary on all supported test platforms.
        if path == alias:
            return outside
        return original_resolve(path, *args, **kwargs)
    monkeypatch.setattr(Path, "resolve", resolve)
    index = make_index(source)
    status = index.search()["coverage"]["workflowmoves"]
    assert status["status"] == "partial" and status["count"] == 0
    assert status["issues"][0]["path"] == "workflows/junction-like"
    assert index.search("junctionoutsideuniquesentinel")["total"] == 0


def test_source_document_and_total_byte_limits_report_omissions(tmp_path, monkeypatch):
    source = make_source(tmp_path)
    (source / "workflows/a.md").write_text("# First\n\nTen bytes extra.", encoding="utf-8")
    (source / "workflows/b.md").write_text("# Second\n\nTen bytes extra.", encoding="utf-8")
    monkeypatch.setattr(discovery, "MAX_SOURCE_BYTES", 40)
    index = make_index(source)
    status = index.list_workflows()["coverage"]["workflowmoves"]
    assert status["status"] == "partial" and status["count"] == 1
    assert "byte limit" in status["issues"][0]["reason"]
    monkeypatch.setattr(discovery, "MAX_SOURCE_BYTES", 10000)
    monkeypatch.setattr(discovery, "MAX_SOURCE_DOCUMENTS", 1)
    limited = make_index(source).list_workflows()["coverage"]["workflowmoves"]
    assert limited["status"] == "partial" and limited["count"] == 1
    assert "document limit" in limited["issues"][0]["reason"]


def test_canonical_capability_and_skill_references_are_searchable_not_workflows(tmp_path):
    source = make_source(tmp_path)
    (source / "workflows/danceflow/capabilities").mkdir(parents=True)
    (source / "workflows/danceflow/capabilities/synthetic.md").write_text(
        "# Synthetic capability\n\nUniquecapabilityreference inspection.", encoding="utf-8")
    (source / "skills/colour-review/references").mkdir()
    (source / "skills/colour-review/references/model.md").write_text(
        "# Assessment\n\nUniqueassessmentreference scoring.", encoding="utf-8")
    index = make_index(source)
    assert index.list_workflows(limit=100)["total"] == len(WORKFLOW_NAMES)
    found = index.search("uniquecapabilityreference", kind="reference")["results"]
    assert len(found) == 1
    assert found[0]["name"] == "workflowmoves/workflows/danceflow/capabilities/synthetic"
    assert found[0]["document_type"] == "reference"
    assert "workflow_type" not in found[0]
    full = index.get_workflow(found[0]["next_call"]["arguments"]["name"])
    assert "Uniquecapabilityreference" in full["content"]
    assert index.search("uniqueassessmentreference", kind="reference")["total"] == 1
    assert full["coverage"]["workflowmoves"]["reference_count"] == 2


def test_source_oversized_document_missing_folders_and_missing_root_are_explicit(tmp_path):
    source = make_source(tmp_path)
    (source / "workflows/large.md").write_bytes(b"x" * (discovery.MAX_DOCUMENT_BYTES + 1))
    index = make_index(source)
    status = index.search()["coverage"]["workflowmoves"]
    assert status["status"] == "partial" and status["count"] == 0
    assert status["issues"][0]["path"] == "workflows/large.md"
    empty = tmp_path / "empty"
    empty.mkdir()
    missing = make_index(empty).search()["coverage"]["workflowmoves"]
    assert missing["status"] == "partial" and missing["issue_count"] == 2
    absent = make_index(tmp_path / "absent").search()["coverage"]["workflowmoves"]
    assert absent["status"] == "unavailable" and absent["count"] == 0


def test_unreadable_packaged_reference_is_reported_without_hiding_other_features(monkeypatch):
    catalogue = EcosystemCatalogue()
    original = catalogue.read_workflow
    def read(name):
        if name == "visual-language":
            raise FileNotFoundError("Synthetic missing bundled reference")
        return original(name)
    monkeypatch.setattr(catalogue, "read_workflow", read)
    index = make_index(catalogue=catalogue)
    result = index.list_workflows(limit=100)
    assert result["total"] == 6
    assert result["coverage"]["packaged_references"]["status"] == "partial"
    assert result["coverage"]["packaged_references"]["count"] == 56
    assert index.search(kind="component")["total"] == 15


@pytest.mark.parametrize("arguments", [
    {"kind": "unknown"}, {"component": "../stemlab"}, {"query": "x" * 513},
    {"limit": 0}, {"limit": 101}, {"limit": True}, {"offset": -1}, {"offset": False},
])
def test_invalid_discovery_filters_are_explicit(arguments):
    with pytest.raises(ValueError):
        make_index().search(**arguments)


def test_duplicate_actual_tool_names_fail_instead_of_silent_shadowing():
    tool = {"name": "synthetic", "inputSchema": {"type": "object"}}
    with pytest.raises(ValueError, match="Duplicate discovery identity"):
        make_index(tools=[tool, deepcopy(tool)])


def test_document_metadata_comes_from_body_and_does_not_infer_dependencies():
    components = [{"name": "pixelcue", "title": "PixelCue"}]
    actual = document_metadata("# Example\n\nUse [PixelCue](https://example.invalid) for café evidence.\n", components)
    assert actual == {"title": "Example", "summary": "Use PixelCue for café evidence.",
                      "related_components": ["pixelcue"]}
    assert "dependencies" not in actual
    assert document_metadata("\ufeff# Heading\n\nWebsite: https://example.invalid\n\nUseful description.", []) == {
        "title": "Heading", "summary": "Useful description.", "related_components": []}
