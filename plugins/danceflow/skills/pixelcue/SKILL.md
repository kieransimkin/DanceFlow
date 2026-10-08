---
name: pixelcue
description: Tag or index local images, videos and archives, or integrate with an already-running PixelCue service.
---

# PixelCue

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/PixelCue)

Use this tool for local visual-media tagging with selectable VLMs, a desktop scanner and REST/Socket.IO service. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
python -m pip install pixelcue
pixelcue-server --help
```

Use Python 3.13 and inspect the repository's uv CUDA index before installing GPU dependencies. Read the REST and Socket.IO section of README.md. GET /health discovers model profiles; POST /v1/keywords takes one server-local path and returns a bare string list. Choose a small SmolVLM profile for initial testing; JoyCaption is heavier. Inference may download weights. Tags, including content/face labels, are model judgements. Paths are local to the service; keep it on loopback unless the user explicitly designs access controls.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
uv sync --group dev
uv run pytest
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.
