# RasterMoves

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/RasterMoves)

Local image upscaling with catalogue plugins, pytorch/onnx backends and optional refinement.

Read README.md and the selected backend/model guide. Inspect catalogue manifests, licence and runtime availability before downloading. Choose torch or onnx extras explicitly; CPU and GPU ONNX distributions conflict. Use dry-run, provenance sidecars and resume/hash checks for comparisons. A catalogue entry is not proof that weights are reachable or an architecture is supported.

## Development checks

```sh
python -m pip install -e ".[dev]"
python -m pytest
ruff check src tests
```

Submit contributions to https://github.com/kieransimkin/RasterMoves/pulls. See the repository's current instructions before editing.
