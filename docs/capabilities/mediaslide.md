# MediaSlide: capability and package reference

Audited 23 October 2026: **v1.1.26**, exact source [`55bab00b5a10c51c43b14fd0128fd400122fe6ff`](https://github.com/kieransimkin/react-mediaslide/tree/55bab00b5a10c51c43b14fd0128fd400122fe6ff). This is a dated source/documentation audit, not installed-runtime or end-to-end acceptance. [Check current releases before use](../workflows/release-preflight.md).

## Current README feature routes

- [What it does](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md#what-it-does)
- [Install](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md#install)
- [Working example](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md#working-example)
- [Props](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md#props)
- [Develop and release](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md#develop-and-release)
- [Potential problems](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md#potential-problems)
- [Licence](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md#licence)

## Source documentation and examples

- [`README.md`](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md)
- [`docs/ECOSYSTEM.md`](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/docs/ECOSYSTEM.md)

## Package evidence

- [`README.md`](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/README.md) — SHA-256 `43dbcba3cae27e542ac971fe12e41ed92826002b7e65351f0bc0ff5b0e5e070d`.
- [`package.json`](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/package.json) — SHA-256 `2f78acefcab6e2c97f69fbe552c35ef26236859ded1695a9c30c7d7b9290b258`.
- [`LICENSE`](https://github.com/kieransimkin/react-mediaslide/blob/55bab00b5a10c51c43b14fd0128fd400122fe6ff/LICENSE) — SHA-256 `bf99626fac05aa9380076169a03fd4d9fe60a2ab0b84f3874199ee4ba41c9f35`.

Package files were read at the pinned source. Published distributions, installed identity, working host examples, rights and reviewed output require their own verification.

## Historical detailed reference

The following older index is retained for detailed routes. Its earlier version is historical; the audited source links above identify current documented availability.

# MediaSlide: complete capability reference

Inspected source: `v1.1.25`, with the DanceFlow integration prepared as `v1.1.26`. This is a dated baseline; [check current releases before every new workflow](../workflows/release-preflight.md), including GitHub and npm because their historical versions diverged.

## Presentation

- List, details, thumbnails and slide modes.
- Adjustable thumbnail size and spacing.
- Large double-buffered image stage and rendered-file buffers.
- Responsive selection-detail sidebar and component-level stage expansion.

## Input and lifecycle

- Pointer, touch, wheel and ArrowLeft/ArrowRight navigation.
- ResizeObserver-driven responsive geometry.
- IntersectionObserver-driven previous and next page requests.
- Initial selection plus selection/open/close callbacks.

## Extensibility

- Custom renderers for every view mode.
- Custom `renderBigInfo` detail panel.
- Asynchronous `renderFile` route for active HTML or application media.
- Stable package version exports through `version` and `getVersion`.

## Composition

Use MediaSlide as collection UI. Compose DanceMoves for rhythmic live effects, React Timeline Sequence for time-based React scenes, ThumbMoves for cache-only previews, PixelCue/PrismMoves for visual evidence, RasterMoves for reviewed upscaling and FrameRudiments for offline video.

## Potential problems

- Verify GitHub release, npm dist-tag and imported runtime independently.
- Browser observers and global event listeners require client-side mounting and teardown tests.
- HTML `slideReady` messages need an expected-frame and trusted-origin policy.
- Stage expansion does not invoke the browser Fullscreen API.
- Default links navigate; use custom renderers for selection-only applications.

## Default-branch availability

The official default branch was also inspected at [`cae7b86605d086ff8a80a26b41e7f21dbe8f44d7`](https://github.com/kieransimkin/react-mediaslide/tree/cae7b86605d086ff8a80a26b41e7f21dbe8f44d7). It differs from the audited stable tag. [Read that exact README](https://github.com/kieransimkin/react-mediaslide/blob/cae7b86605d086ff8a80a26b41e7f21dbe8f44d7/README.md) for later source/documentation work; this does not establish a newer release, registry version or installed runtime.
