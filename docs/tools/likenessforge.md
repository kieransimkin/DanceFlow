# LikenessForge

[DanceFlow](https://kieransimkin.co.uk/danceflow/) · [Kieran Simkin](https://kieransimkin.co.uk/) · [Canonical source](https://github.com/kieransimkin/LikenessForge)

Repair the facial likeness of a selected person in an existing image while retaining its surrounding composition. The local CLI and Qt desktop GUI share selectable face detectors, segmenters, image modifiers and LoRA trainers. Repair and training wizards save bounded candidate sets, comparison sheets and settings for human review; the verbose trace retains intermediate images.

## Install and inspect

Clone the source repository and follow its current README. `start-gui.ps1` / `start-gui.bat` on Windows or `start-gui.sh` on Linux/macOS bootstraps uv, pinned Python and dependencies. For a manual core installation use `python -m pip install -e .`; add `.[gui]` for Qt or the selected model extras. Then inspect `likenessforge --help`, `likenessforge plugins` and `likenessforge models list`. This guide does not claim a PyPI listing.

Use `faces` to verify the target face index; `prepare-training` to inspect authorised face crops before training; `repair` for a selected recipe; `repair-wizard` for bounded repair comparisons; `train-lora` or `train-wizard` for identity LoRAs and fixed-holdout comparison. Pair trainer and modifier architecture families. Model files download on demand; optional dependencies, storage, hardware and model licences remain separate requirements. Low-VRAM modes are hardware-dependent, not an 8 GB guarantee. Automated tests do not establish likeness quality.

Read the [integration workflow](../workflows/likenessforge.md) before handling campaign imagery. No automatic PixelCue/RasterMoves/DanceMoves or MCP integration is asserted.

## Contribute and validate

Use the existing workflow/plugin interfaces before creating a replacement. Agents and people can submit narrow improvements with README changes, synthetic tests and a reproducible example to [LikenessForge pull requests](https://github.com/kieransimkin/LikenessForge/pulls). Follow its AGENTS.md and CONTRIBUTING.md. Run `uv sync --extra gui --extra dev`, offscreen `uv run pytest -q`, `uv run ruff check src tests`, `uv build`, and `uv run python scripts/validate_distribution.py dist`. Do not download weights for CI or commit portraits, identity weights or private traces.

## Full feature workflow

[Read the released feature references](../capabilities/likenessforge.md) and [check current releases before every new run](../workflows/release-preflight.md). Consider the whole ecosystem, use and improve applicable shared capabilities, and keep actual runtime/output evidence separate from availability.
