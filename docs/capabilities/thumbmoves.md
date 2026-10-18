# ThumbMoves: cache-only feature workflow

Baseline: [thumbmoves-v0.1.2](https://github.com/kieransimkin/PixelCue/releases/tag/thumbmoves-v0.1.2). [Check the current release](../workflows/release-preflight.md) before each run; PixelCue's normal `v` releases are a separate stream.

Use the [complete package README](https://github.com/kieransimkin/PixelCue/blob/thumbmoves-v0.1.2/packages/thumbmoves/README.md) for its CLI, Python API, result type, format/size controls, platform backends, batch use, errors and examples. Windows and freedesktop cache hits can provide previews without source decoding. Preserve cache hit/miss/backend evidence and allow bounded failures. macOS has no public equivalent and returns a miss.

A miss never opens an original or renders a new thumbnail. Requesting later source decoding belongs to the actual media tool and task. A cached preview does not prove full-file picture or video quality. Do not scan unrelated directories merely because cache access is inexpensive.

The examples in the tagged README and PixelCue's viewer demonstrate the real API/backend states. A generated thumbnail illustration cannot prove a cache hit; no fabricated preview is added to this contract.
