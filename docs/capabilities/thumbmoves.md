# ThumbMoves: capability and package reference

Audited 23 October 2026: **thumbmoves-v0.1.2**, exact source [`53e9b393a3510d396b7da4bfd5da307cafd86a94`](https://github.com/kieransimkin/PixelCue/tree/53e9b393a3510d396b7da4bfd5da307cafd86a94). This is a dated source/documentation audit, not installed-runtime or end-to-end acceptance. [Check current releases before use](../workflows/release-preflight.md).

## Current README feature routes

- [Agents and contributors](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/README.md#agents-and-contributors)
- [Platform behavior](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/README.md#platform-behavior)
- [Installation](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/README.md#installation)
- [CLI](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/README.md#cli)
- [Design goals](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/README.md#design-goals)
- [License](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/README.md#license)

## Source documentation and examples

- [`README.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/README.md)
- [`docs/RELEASING.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/docs/RELEASING.md)
- [`docs/branding/README.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/docs/branding/README.md)
- [`packages/thumbmoves/AGENTS.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/AGENTS.md)
- [`packages/thumbmoves/CHANGELOG.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/CHANGELOG.md)
- [`packages/thumbmoves/CONTRIBUTING.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/CONTRIBUTING.md)
- [`packages/thumbmoves/README.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/README.md)
- [`packages/thumbmoves/docs/RELEASING.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/docs/RELEASING.md)
- [`packages/thumbmoves/docs/blog/2026-10-03-thumbmoves-release/publication-record.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/docs/blog/2026-10-03-thumbmoves-release/publication-record.md)
- [`packages/thumbmoves/docs/branding/README.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/docs/branding/README.md)

## Package evidence

- [`packages/thumbmoves/README.md`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/README.md) — SHA-256 `02edf30f6d4ad0f453374d6ef2056aeb2ed51ecee7b194c88e1da127dfd80852`.
- [`packages/thumbmoves/pyproject.toml`](https://github.com/kieransimkin/PixelCue/blob/53e9b393a3510d396b7da4bfd5da307cafd86a94/packages/thumbmoves/pyproject.toml) — SHA-256 `c6bd7d335cf2ce18ac6bca28496e67a5d8079b7310d66fee9f98e86657f25fed`.

Package files were read at the pinned source. Published distributions, installed identity, working host examples, rights and reviewed output require their own verification.

## Historical detailed reference

The following older index is retained for detailed routes. Its earlier version is historical; the audited source links above identify current documented availability.

# ThumbMoves: cache-only feature workflow

Baseline: [thumbmoves-v0.1.2](https://github.com/kieransimkin/PixelCue/releases/tag/thumbmoves-v0.1.2). [Check the current release](../workflows/release-preflight.md) before each run; PixelCue's normal `v` releases are a separate stream.

Use the [complete package README](https://github.com/kieransimkin/PixelCue/blob/thumbmoves-v0.1.2/packages/thumbmoves/README.md) for its CLI, Python API, result type, format/size controls, platform backends, batch use, errors and examples. Windows and freedesktop cache hits can provide previews without source decoding. Preserve cache hit/miss/backend evidence and allow bounded failures. macOS has no public equivalent and returns a miss.

A miss never opens an original or renders a new thumbnail. Requesting later source decoding belongs to the actual media tool and task. A cached preview does not prove full-file picture or video quality. Do not scan unrelated directories merely because cache access is inexpensive.

The examples in the tagged README and PixelCue's viewer demonstrate the real API/backend states. A generated thumbnail illustration cannot prove a cache hit; no fabricated preview is added to this contract.

## Default-branch availability

The official default branch was also inspected at [`66c714a07ce71f11c4dbdfeb9a8d91438e5b4738`](https://github.com/kieransimkin/PixelCue/tree/66c714a07ce71f11c4dbdfeb9a8d91438e5b4738). It differs from the audited stable tag. [Read that exact README](https://github.com/kieransimkin/PixelCue/blob/66c714a07ce71f11c4dbdfeb9a8d91438e5b4738/README.md) for later source/documentation work; this does not establish a newer release, registry version or installed runtime.
