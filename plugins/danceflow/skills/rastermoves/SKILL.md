---
name: rastermoves
description: Upscale or enhance images using a selected local model, or inspect model/runtime availability before choosing a backend.
---

# RasterMoves

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/RasterMoves)

Use this tool for local image upscaling with catalogue plugins, PyTorch/ONNX backends and optional refinement. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
python -m pip install rastermoves
rastermoves --version
rastermoves doctor
```

Read README.md and the selected backend/model guide. Inspect catalogue manifests, licence and runtime availability before downloading. Choose torch or onnx extras explicitly; CPU and GPU ONNX distributions conflict. Use dry-run, provenance sidecars and resume/hash checks for comparisons. A catalogue entry is not proof that weights are reachable or an architecture is supported.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
python -m pip install -e ".[dev]"
python -m pytest
ruff check src tests
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.
