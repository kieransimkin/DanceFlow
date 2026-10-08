---
name: thumbmoves
description: Retrieve existing OS thumbnail-cache entries without silently regenerating missing thumbnails.
---

# ThumbMoves

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/PixelCue/tree/main/packages/thumbmoves)

Use this tool for cache-only thumbnail access with explicit cache misses. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
python -m pip install thumbmoves
thumbmoves --help
```

The canonical source is packages/thumbmoves in PixelCue, not the separate empty ThumbMoves repository. Read that package's README and backend documentation. Preserve cache-only semantics: a missing thumbnail is an explicit miss. Windows, freedesktop and macOS routes have different availability; inspect diagnostics rather than claiming cross-platform success from one backend.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
python -m pip install -e "packages/thumbmoves[dev]"
python -m pytest packages/thumbmoves/tests
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.
