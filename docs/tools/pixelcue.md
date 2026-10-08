# PixelCue

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/PixelCue)

Local visual-media tagging with selectable vlms, a desktop scanner and rest/socket.io service.

Use Python 3.13 and inspect the repository's uv CUDA index before installing GPU dependencies. Read the REST and Socket.IO section of README.md. GET /health discovers model profiles; POST /v1/keywords takes one server-local path and returns a bare string list. Choose a small SmolVLM profile for initial testing; JoyCaption is heavier. Inference may download weights. Tags, including content/face labels, are model judgements. Paths are local to the service; keep it on loopback unless the user explicitly designs access controls.

## Development checks

```sh
uv sync --group dev
uv run pytest
```

Submit contributions to https://github.com/kieransimkin/PixelCue/pulls. See the repository's current instructions before editing.
