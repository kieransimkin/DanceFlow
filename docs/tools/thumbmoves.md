# ThumbMoves

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/PixelCue/tree/main/packages/thumbmoves)

Cache-only thumbnail access with explicit cache misses.

The canonical source is packages/thumbmoves in PixelCue, not the separate empty ThumbMoves repository. Read that package's README and backend documentation. Preserve cache-only semantics: a missing thumbnail is an explicit miss. Windows, freedesktop and macOS routes have different availability; inspect diagnostics rather than claiming cross-platform success from one backend.

## Development checks

```sh
python -m pip install -e "packages/thumbmoves[dev]"
python -m pytest packages/thumbmoves/tests
```

Submit contributions to https://github.com/kieransimkin/PixelCue/pulls. See the repository's current instructions before editing.

## Full feature workflow

[Read the released feature references](../capabilities/thumbmoves.md) and [check current releases before every new run](../workflows/release-preflight.md). Consider the whole ecosystem, use and improve applicable shared capabilities, and keep actual runtime/output evidence separate from availability.
