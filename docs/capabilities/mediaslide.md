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
