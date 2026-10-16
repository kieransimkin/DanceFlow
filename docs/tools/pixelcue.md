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

## Image understanding with PrismMoves

PixelCue 0.9.0+ also provides /v1/analysis and Python APIs for bounded colour, texture, composition and frequency measurements, with explicit CLIP, DINOv2, BLIP and OCR hypotheses. PrismMoves organises those receipts into inspectable visual-language reports; its analysis engine stays in PixelCue. Use the hub's pixelcue_visual_analysis tool for a raw receipt. Cached-model inference requires explicit opt-in; this adapter never downloads weights. Store selected weights/cache in the owning project's ignored models/ directory.

![Synthetic fixture beside actual PixelCue palette and texture measurements](https://raw.githubusercontent.com/kieransimkin/PrismMoves/main/docs/images/visual-profile-example.png)

Generated measurement figure, not a UI screenshot or proof of model accuracy. See [PrismMoves](prismmoves.md) and the [visual-language workflow](../workflows/visual-language.md).
