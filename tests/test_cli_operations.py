"""Synthetic command-contract checks; no engines, models, services or accounts run."""
from copy import deepcopy
import argparse
import json

import pytest
from jsonschema import Draft202012Validator

from danceflow_agents.cli_operations import OPERATIONS, UNSUPPORTED_OPERATIONS, build_arguments, effects_for_arguments, validated_arguments


def operation(component, name):
    return OPERATIONS[component][name]


def test_registry_is_strict_serializable_and_has_only_known_path_metadata():
    json.dumps(OPERATIONS, allow_nan=False)
    assert set(OPERATIONS) == {"stemlab", "framerudiments", "rastermoves", "prismmoves", "likenessforge", "workflowmoves"}
    for component, entries in OPERATIONS.items():
        for name, descriptor in entries.items():
            schema = descriptor["input_schema"]
            Draft202012Validator.check_schema(schema)
            assert schema["additionalProperties"] is False, (component, name)
            assert set(schema["properties"]) == set(descriptor["parameters"])
            assert bool(descriptor.get("module")) != bool(descriptor.get("script"))
            assert descriptor["source"].startswith("https://github.com/kieransimkin/")
            assert 1 <= descriptor["timeout_seconds"] <= 86400
            assert set(descriptor["effects"]) <= {"write", "inference", "download", "network", "publication", "training"}
            for parameter, metadata in descriptor["parameters"].items():
                assert metadata["kind"] in {"value", "flag", "repeat", "input_file", "input_dir", "output_file", "output_dir"}
                if metadata["kind"].startswith(("input_", "output_")):
                    assert "default" not in schema["properties"][parameter]
            assert "argv" not in schema["properties"]
            assert "extra_args" not in schema["properties"]


def test_native_stemlab_owns_expensive_analysis_and_its_canonical_job_lifecycle():
    assert "analyze" not in OPERATIONS["stemlab"]
    assert "midi" not in OPERATIONS["stemlab"]
    assert "MCP provider" in UNSUPPORTED_OPERATIONS["stemlab"]["analyze_midi_evidence_loops"]
    assert build_arguments(operation("stemlab", "models"), {}) == ["models"]


def test_frame_plan_output_is_a_file_and_profile_suite_is_a_file():
    plan = operation("framerudiments", "plan")
    assert plan["parameters"]["output"]["kind"] == "output_file"
    assert build_arguments(plan, {"project": "/work/project.json", "output": "/work/plan.json"}) == [
        "plan", "/work/project.json", "--output", "/work/plan.json"
    ]
    assert operation("framerudiments", "presets_profile")["parameters"]["suite"]["kind"] == "input_file"


def test_frame_demo_exclusive_views_and_dependency_download_consent():
    demo = operation("framerudiments", "demo")
    with pytest.raises(ValueError, match="at most one demo view"):
        build_arguments(demo, {"directory": "out", "font": "font.ttf", "rangoli": True, "spectrum": True})
    setup = operation("framerudiments", "effects_setup")
    with pytest.raises(ValueError, match="allow_downloads"):
        build_arguments(setup, {"engine": "projectm", "directory": "out"})
    assert build_arguments(setup, {"engine": "projectm", "directory": "out", "allow_downloads": True}) == [
        "effects-setup", "projectm", "out", "--parallel", "4"
    ]
    with pytest.raises(ValueError):
        build_arguments(setup, {"engine": "projectm", "directory": "out", "allow_downloads": "true"})


def test_raster_global_cache_flag_precedes_subcommand_and_compute_is_offline():
    args = build_arguments(operation("rastermoves", "upscale"), {
        "input": "/work/input.png", "output": "/work/output.png", "cache_dir": "/work/models",
        "model": "selected-model", "width": 1024,
    })
    assert args[:4] == ["--cache-dir", "/work/models", "upscale", "/work/input.png"]
    assert args[-2:] == ["--offline", "--report"]
    assert "--overwrite" not in args and "--external-plugins" not in args
    assert "download" not in operation("rastermoves", "upscale")["effects"]


def test_raster_rejects_conflicting_sizes_models_and_unsupported_arg_passthrough():
    base = {"input": "input.png", "output": "output.png"}
    descriptor = operation("rastermoves", "upscale")
    for invalid in ({"width": 512, "scale": 2}, {"model": "one", "model_file": "two.pth"},
                    {"extra_args": ["--overwrite"]}, {"backend": "arbitrary-python-entry-point"}):
        with pytest.raises(ValueError):
            build_arguments(descriptor, {**base, **invalid})
    with pytest.raises(ValueError, match="multiple of 8"):
        build_arguments(operation("rastermoves", "refine"), {**base, "tile": 513})


def test_raster_plans_do_not_turn_into_inference_or_downloads():
    plan = operation("rastermoves", "plan_all_models")
    args = build_arguments(plan, {"input": "input.png", "output": "plan"})
    assert args == ["upscale", "input.png", "--output", "plan", "--all-models", "--dry-run", "--offline"]
    assert plan["effects"] == ["write"]  # Canonical Registry initializes its cache directory.
    assert "all_models_inference" in UNSUPPORTED_OPERATIONS["rastermoves"]


def test_prism_image_lists_are_separately_confined_and_models_use_nargs():
    descriptor = operation("prismmoves", "profile")
    assert descriptor["parameters"]["images"]["multiple"] is True
    args = build_arguments(descriptor, {"images": ["a.png", "b.png"], "output": "reports", "models": ["clip", "ocr"]})
    assert args[:2] == ["a.png", "b.png"]
    start = args.index("--models")
    assert args[start:start + 3] == ["--models", "clip", "ocr"]
    assert "--allow-download" not in args
    assert descriptor["partial_exit_codes"] == [2]


def test_prism_zero_model_default_does_not_inherit_upstream_preset_model_default():
    descriptor = operation("prismmoves", "preset_analyse")
    args = build_arguments(descriptor, {"captures": "capture.json", "output": "report"})
    start = args.index("--models")
    assert args[start + 1].startswith("--")
    assert "clip" not in args and "blip" not in args
    assert descriptor["module"] == "prismmoves.preset_pipeline"


def test_prism_keyword_models_require_actual_download_flag_and_loopback_origin():
    descriptor = operation("prismmoves", "profile")
    base = {"images": ["input.png"], "output": "report", "pixelcue_models": ["selected-profile"]}
    with pytest.raises(ValueError, match="allow_download=true"):
        build_arguments(descriptor, base)
    assert "--allow-download" in build_arguments(descriptor, {**base, "allow_download": True})
    for url in ("https://127.0.0.1:8765", "http://example.com", "http://user:secret@localhost:8765"):
        with pytest.raises(ValueError):
            build_arguments(descriptor, {"images": ["a.png"], "output": "out", "pixelcue_url": url})


def test_prism_permissions_follow_measurements_selected_models_and_actual_download_choice():
    descriptor = operation("prismmoves", "profile")
    base = {"images": ["input.png"], "output": "report"}
    assert effects_for_arguments(descriptor, base) == ["write"]
    assert effects_for_arguments(descriptor, {**base, "models": ["clip"]}) == ["inference", "write"]
    assert effects_for_arguments(descriptor, {**base, "pixelcue_url": "http://127.0.0.1:8765"}) == ["network", "write"]
    assert effects_for_arguments(descriptor, {**base, "models": ["clip"], "allow_download": True}) == [
        "download", "inference", "network", "write"
    ]


@pytest.mark.parametrize("name,base,parameter", [
    ("profile", {"images": ["input.png"], "output": "reports"}, "pixelcue_models"),
    ("preset_analyse", {"captures": "capture.json", "output": "reports"}, "keyword_models"),
])
@pytest.mark.parametrize("injected", ["--out", "--out=/tmp/outside-report", "--allow-download", "-h", "--"])
def test_prism_nargs_cannot_override_validated_paths_or_flags(name, base, parameter, injected):
    descriptor = operation("prismmoves", name)
    arguments = {**base, "allow_download": True, parameter: [injected, "/tmp/outside-report"]}
    assert not Draft202012Validator(descriptor["input_schema"]).is_valid(arguments)
    with pytest.raises(ValueError):
        build_arguments(descriptor, arguments)


def test_generic_builder_guards_string_tokens_even_without_generated_schema_restrictions():
    descriptor = {
        "prefix": [], "input_schema": {
            "type": "object", "additionalProperties": False,
            "properties": {
                "positional": {"type": "string"}, "scalar": {"type": "string"},
                "many": {"type": "array", "items": {"type": "string"}},
                "repeat": {"type": "array", "items": {"type": "string"}},
            },
        },
        "parameters": {
            "positional": {"kind": "value", "positional": 0},
            "scalar": {"kind": "value", "flag": "--scalar"},
            "many": {"kind": "repeat", "flag": "--many", "many": True},
            "repeat": {"kind": "repeat", "flag": "--repeat"},
        },
    }
    for parameter in descriptor["parameters"]:
        for malicious in ("--out", "-o", " --out", "\t--out", "\u2013Out", "\u2014Out", "value\0suffix"):
            value = [malicious] if parameter in {"many", "repeat"} else malicious
            with pytest.raises(ValueError, match="literal CLI values"):
                build_arguments(descriptor, {parameter: value})
    literal = "normal-hyphenated text --out remains one literal argument"
    assert build_arguments(descriptor, {"scalar": literal, "many": ["profile-one", "profile two"]}) == [
        "--scalar", literal, "--many", "profile-one", "profile two"
    ]


def test_option_guard_preserves_typed_negative_numbers_in_scalars_arrays_and_positionals():
    number = {"type": "number", "minimum": -10, "maximum": 10}
    descriptor = {
        "prefix": [], "input_schema": {
            "type": "object", "additionalProperties": False,
            "properties": {"position": number, "amount": number,
                           "offsets": {"type": "array", "items": number}},
        },
        "parameters": {
            "position": {"kind": "value", "positional": 0},
            "amount": {"kind": "value", "flag": "--amount"},
            "offsets": {"kind": "repeat", "flag": "--offsets", "many": True},
        },
    }
    args = build_arguments(descriptor, {"position": -3, "amount": -1.5, "offsets": [-2, -.25]})
    parser = argparse.ArgumentParser()
    parser.add_argument("position", type=float)
    parser.add_argument("--amount", type=float)
    parser.add_argument("--offsets", type=float, nargs="*")
    result = parser.parse_args(args)
    assert (result.position, result.amount, result.offsets) == (-3, -1.5, [-2, -.25])


def test_powershell_and_repeated_path_arguments_receive_the_same_option_guard():
    wordpress = operation("workflowmoves", "wordpress_read_post")
    with pytest.raises(ValueError):
        build_arguments(wordpress, {"post_id": 42, "receipt_out": "-Execute"})
    with pytest.raises(ValueError):
        build_arguments(operation("likenessforge", "repair"), {
            "image": "input.png", "output": "candidate.png", "allow_downloads": True,
            "references": ["--output", "/tmp/outside.png"],
        })
    args = build_arguments(wordpress, {"post_id": 42, "receipt_out": "/work/-reviewed receipt.json"})
    assert args[args.index("-ReceiptOut") + 1] == "/work/-reviewed receipt.json"


def test_likeness_uses_real_cli_module_requires_download_choice_and_repeats_references():
    descriptor = operation("likenessforge", "repair")
    assert descriptor["module"] == "likenessforge.cli"
    assert set(descriptor["effects"]) == {"write", "inference", "download", "network"}
    base = {"image": "portrait.png", "output": "candidate.png"}
    with pytest.raises(ValueError, match="allow_downloads"):
        build_arguments(descriptor, base)
    args = build_arguments(descriptor, {**base, "allow_downloads": True,
                                      "references": ["reference1.png", "reference2.png"]})
    assert args[:3] == ["repair", "portrait.png", "candidate.png"]
    positions = [index for index, item in enumerate(args) if item == "--reference"]
    assert [args[index + 1] for index in positions] == ["reference1.png", "reference2.png"]
    assert "--allow-downloads" not in args  # Consent is a host contract, not an invented upstream flag.


def test_training_requires_separate_training_choice_and_exact_holdout_position():
    descriptor = operation("likenessforge", "train_wizard")
    base = {"images": "dataset", "validation": "holdout.png", "output": "training",
            "trigger": "subject_token", "allow_downloads": True}
    with pytest.raises(ValueError, match="allow_training"):
        build_arguments(descriptor, base)
    args = build_arguments(descriptor, {**base, "allow_training": True})
    assert args[:4] == ["train-wizard", "dataset", "holdout.png", "training"]
    assert "--background" not in args  # This flag is absent from upstream train-wizard.
    assert "--extra-arg" not in args
    assert "training" in descriptor["effects"]


def test_workflow_claim_preserves_explicit_identity_packet_approval_and_private_state():
    descriptor = operation("workflowmoves", "outreach_claim")
    values = {"root": "claims", "account": "account", "venue": "venue", "obligation": "obligation",
              "owner": "execution", "approval": "review-reference", "packet": "packet.json"}
    args = build_arguments(descriptor, values)
    assert descriptor["script"] == "tools/outreach_send_gate.py"
    assert descriptor["parameters"]["root"]["allow_existing"] is True
    assert args[0] == "claim"
    for name, value in values.items():
        assert args[args.index("--" + name) + 1] == value
    assert descriptor["effects"] == ["write"]
    assert "publication" not in descriptor["effects"]


@pytest.mark.parametrize("name,mode", [
    ("wordpress_upload_media", "UploadMedia"), ("wordpress_create_draft", "CreateDraft"),
    ("wordpress_publish_post", "PublishPost"), ("wordpress_schedule_post", "SchedulePost"),
])
def test_wordpress_mutations_preserve_exact_native_gates_without_credential_arguments(name, mode):
    descriptor = operation("workflowmoves", name)
    values = {"manifest": "reviewed.json", "expected_manifest_sha256": "a" * 64, "receipt_out": "new-receipt.json"}
    args = build_arguments(descriptor, values)
    assert descriptor["runtime"] == "powershell"
    assert descriptor["script"] == "tools/wordpress_blog_api.ps1"
    assert args[:2] == ["-Mode", mode] and args[-1] == "-Execute"
    assert args[args.index("-ExpectedManifestSha256") + 1] == "a" * 64
    assert set(descriptor["effects"]) == {"write", "network", "publication"}
    assert not descriptor["parameters"]["receipt_out"].get("allow_existing", False)
    for extra in ({"credential_path": "secret"}, {"site_url": "https://elsewhere.invalid"},
                  {"expected_manifest_sha256": "not-a-hash"}):
        with pytest.raises(ValueError):
            build_arguments(descriptor, {**values, **extra})


def test_wordpress_readback_never_injects_execute_or_publication_effect():
    descriptor = operation("workflowmoves", "wordpress_read_post")
    args = build_arguments(descriptor, {"post_id": 42, "receipt_out": "readback.json"})
    assert args == ["-Mode", "ReadPost", "-ReceiptOut", "readback.json", "-PostId", "42"]
    assert "publication" not in descriptor["effects"] and "-Execute" not in args


def test_paths_have_no_implicit_defaults_and_existing_input_mutation_is_explicit():
    for name in ("repair_spectrograms", "phrase_loops"):
        descriptor = operation("stemlab", name)
        assert descriptor["parameters"]["results"]["writable"] is True
        assert "write" in descriptor["effects"]
    descriptor = operation("stemlab", "generate_cues")
    with pytest.raises(ValueError, match="artist"):
        build_arguments(descriptor, {"results": "song", "output": "cues"})


def test_defaults_are_copied_and_source_bounds_and_finite_numbers_are_checked():
    descriptor = operation("framerudiments", "presets_profile")
    original = deepcopy(descriptor)
    supplied = {"suite": "suite.json", "catalogue": "catalogue.json", "output": "out"}
    result = validated_arguments(descriptor, supplied)
    result["intervals"].append(8)
    assert descriptor == original and "intervals" not in supplied
    for arguments in ({"min_seconds": 20, "max_seconds": 10}, {"min_seconds": float("nan")}):
        with pytest.raises(ValueError):
            build_arguments(operation("stemlab", "phrase_loops"), {"results": "song", **arguments})
    with pytest.raises(ValueError, match="power of two"):
        build_arguments(operation("stemlab", "record_rudiment"), {"source": "song.wav", "output": "out", "fft_size": 300})
    args = build_arguments(operation("stemlab", "record_rudiment"), {
        "source": "song.wav", "output": "out", "fft_size": 2048.0,
    })
    assert args[args.index("--fft-size") + 1] == "2048"


def test_permission_annotations_preserve_partial_output_interpretation():
    assert operation("prismmoves", "profile")["partial_exit_codes"] == [2]
    assert operation("framerudiments", "presets_profile")["partial_exit_codes"] == [2]
    assert operation("likenessforge", "faces")["partial_exit_codes"] == [2]
    assert operation("workflowmoves", "check_blogworthiness")["partial_exit_codes"] == [1]
    assert operation("framerudiments", "render")["partial_exit_codes"] == []
