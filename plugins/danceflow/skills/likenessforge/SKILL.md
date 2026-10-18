---
name: likenessforge
description: Repair facial likeness in an existing image, prepare authorised face crops, or train and compare identity LoRAs using LikenessForge's local CLI or desktop GUI. Use other tools for general upscaling, tagging or animation.
---

# LikenessForge

[DanceFlow](https://kieransimkin.co.uk/danceflow/) · [Canonical source and README](https://github.com/kieransimkin/LikenessForge)

Inspect the current README, plugin inventory and upstream AGENTS.md before choosing a route. LikenessForge has independent detector, segmenter, modifier and trainer families; the GUI orchestrates the same workflows as the CLI. It is installed separately and has no repair/training MCP adapter in DanceFlow.

## Select a route

Use the source launchers (`start-gui.ps1` / `start-gui.bat`, or `start-gui.sh`) for the desktop GUI, or install the selected extras from a source checkout. Run `likenessforge --help`, `likenessforge plugins` and `likenessforge models list` to inspect the actual installed capabilities.

For repair, preserve the input, inspect `faces` and its numbered preview, select the target, pair the modifier with the LoRA architecture, then use `repair` or a bounded `repair-wizard` sweep. Review both face and full-image comparison sheets; do not promote the first candidate automatically. Preserve the surrounding composition and inspect mask/blend boundaries, other faces, expression, crop and intended output size.

For training, use authorised references; inspect `prepare-training` crops before spending GPU time. Keep a holdout photograph outside the training set. Use `train-lora` for a chosen recipe or `train-wizard` to compare bounded training variants using a fixed validation repair. Record settings, seeds, selected plugins, model/LoRA identity and output hashes privately.

Models download on demand and have their own licences and hardware requirements. Low-VRAM labels do not guarantee a fit on a particular card. Confirm the user's intended models and resource scope before starting new training or a substantial download. Generated likeness is a candidate judgement requiring human review, not identity verification. Do not upload private photographs, publish portraits or distribute trained identity weights merely because repair was requested. Debug output can contain full portraits and paths; keep it private.

## Improve the tool

Use existing ModelStore, plugin and workflow composition. Implement a demonstrated reusable gap upstream, update README.md and meaningful synthetic tests, then run the documented offscreen tests, Ruff, build and distribution checks. Never put weights or private portraits in tests. Submit improvements as PRs to https://github.com/kieransimkin/LikenessForge/pulls; explain why no change is justified when the existing capability suffices. Repository review and release permissions remain separate from permission to use an image.

## Current releases and full feature routing

Before every new workflow, follow the [release preflight](https://github.com/kieransimkin/DanceFlow/blob/main/docs/workflows/release-preflight.md) and [complete capability reference](https://github.com/kieransimkin/DanceFlow/blob/main/docs/capabilities/likenessforge.md). Observe the real installed runtime, review every relevant feature and compose supported ecosystem tools. Improve a demonstrated reusable gap in its canonical repository, or record why the tool already meets the need. This guidance does not trigger unrelated processing or downloads.
