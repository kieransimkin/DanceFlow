# React Timeline Sequence

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/react-timeline-sequence)

React audio transport, sequence lanes, seeking, zoom and sample-frame loop regions.

Read README.md and docs/loops.md. Supply React/React DOM 18+ and a container with useful height. Reuse TimelineSequence for transport, playhead, ruler, seeking, zoom/follow and lane geometry. Loop start/end values belong to a declared sample rate; loops remain disabled until selected and enabled. Dispose buffered audio resources and test seeking/zoom/loop playback through the shared transport.

## Development checks

```sh
npm ci --ignore-scripts
npm run typecheck
npm test
npm run build
```

Submit contributions to https://github.com/kieransimkin/react-timeline-sequence/pulls. See the repository's current instructions before editing.

## Full feature workflow

[Read the released feature references](../capabilities/react-timeline-sequence.md) and [check current releases before every new run](../workflows/release-preflight.md). Consider the whole ecosystem, use and improve applicable shared capabilities, and keep actual runtime/output evidence separate from availability.
