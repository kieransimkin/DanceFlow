---
name: setup
description: Connect or troubleshoot DanceFlow, check available tools and prerequisites, and choose a local workspace. Use for setup or missing-runtime questions; use the component skill for the actual music, video, image or motion task.
---

# Set up DanceFlow

[Website](https://kieransimkin.co.uk/danceflow/) · [Toolkit source](https://github.com/kieransimkin/DanceFlow)

Choose the component that fits the user's task from catalogue.json or the per-tool skills. These are independently useful tools; installing the toolkit does not install every model or WordPress plugin. Short Shifter is unrelated to DanceFlow.

## First useful result

1. Establish the user's intended result: analyse a song, render a lyric video, create media-clock web motion, inspect an image, research keywords, or another supported component task. Use that task's skill rather than treating every request as setup.
2. Call `danceflow_capabilities` and inspect the relevant `danceflow_component` entry. Report the actual installed version, exposed operation, required host and missing runtime separately. A visible tool or catalogue entry does not prove engine readiness or vendor-directory approval.
3. For discovery-only setup, return the matching operation and smallest missing prerequisite. Request one explicitly bounded workspace only when file work is needed. Run a small synthetic check only when it verifies the requested operation; do not perform unrelated keyword analysis merely to demonstrate installation.

Onboarding does not authorize later generation, model downloads, paid calls, public deployment or account changes. Once prerequisites are met, hand off to the component workflow and retain the actual first output or precise failure state.

For the local MCP adapter, require Python 3.10–3.13 and uv when using the version-pinned marketplace command. For a source development installation, use the checkout's isolated Python environment as documented in README.md. Set DANCEFLOW_WORKSPACE in the host's MCP environment to one explicitly selected local directory, then restart that MCP server and call danceflow_capabilities. With no workspace configured, catalogue/reference discovery works but workspace file operations reject. Do not default the workspace to the entire disk or user home.

Read `danceflow://overview/mcp` and call `danceflow_component` for exact schemas, required effect acknowledgements, runtime availability and host requirements. Set DANCEFLOW_RUNTIME_CONFIG or --runtime-config to an operator-owned binding file when components use separate Python environments or a trusted WorkflowMoves checkout. Never accept executable/source-root changes from task data. Use component resources and the danceflow_workflow prompt for procedural guidance.

KeywordMoves offline extraction and reviewed imports are available directly. Other live/paid/provider operations stay in KeywordMoves' explicitly configured CLI and require their own user-selected access and budget. PixelCue is optional: install it separately with Python 3.13, start pixelcue-server on loopback and call pixelcue_health before inference. Obtain the applicable model/download authority before allow_inference=true. Install StemLab with its codex extra in the selected Python environment; the hub federates its native MCP schemas, persistent jobs, consent gates and React timeline tools.

For facial-likeness repair or identity LoRA training, read the likenessforge skill and provision its runtime separately. Confirm references, selected models and resource scope; call its typed MCP operation with only authorized effect flags, then poll the returned job and retain comparison outputs for review. Toolkit installation does not install model weights. MediaSlide, DanceVault and EPK Social Metadata need their documented browser or WordPress hosts; resource discovery does not perform deployment.

Use danceflow_job_status and danceflow_job_logs for CLI jobs; use native stemlab_job_* tools for StemLab analysis jobs. Treat needs_review as a prompt to inspect the actual reports and exit code, not proof of usable output. Never automatically repeat an uncertain external write. Review native project/manifest references; workspace path validation is not an OS sandbox.

Verify a small synthetic input before using real files. Return actual versions, supported operations and any unavailable dependencies. Installation, discovery, a queued job and a completed result are separate states.

Agents should inspect available capabilities and look for useful improvements wherever possible. Submit toolkit improvements as PRs to https://github.com/kieransimkin/DanceFlow/pulls; engine improvements belong in the tool repositories listed in catalogue.json.

For image understanding, PixelCue owns statistics and model inference; PrismMoves creates visual-language reports through its public API/service. Read the prismmoves skill. Keep all downloaded weights and model-specific caches in the owning project's ignored models/ directory. A statistics-only request needs no model download. Installing the toolkit adds guidance and an MCP receipt route, not pretrained weights or the PrismMoves runtime.

## Current releases and full feature routing

Before every new workflow, follow the [release preflight](https://github.com/kieransimkin/DanceFlow/blob/main/docs/workflows/release-preflight.md) and [complete capability reference](https://github.com/kieransimkin/DanceFlow/blob/main/docs/capabilities/index.md). Observe the real installed runtime, review every relevant feature and compose supported ecosystem tools. Improve a demonstrated reusable gap in its canonical repository, or record why the tool already meets the need. This guidance does not trigger unrelated processing or downloads.

## Potbot and Unity previews

Read the potbot and danceflow-unity skills and danceflow://workflows/potbot-unity. These entries require their native PostgreSQL/worker or Unity 6 hosts; no execution adapter is exposed. Potbot consuming DanceFlow MCP remains planned, and Unity Editor/GPU acceptance remains separate. Use no_stable_release when an official query succeeds without a stable runtime.
