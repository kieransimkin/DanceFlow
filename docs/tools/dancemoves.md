# DanceMoves

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/DanceMoves)

Bpm-synchronised web motion, shared clocks, effects, input, lifecycle and adaptive quality.

Start with docs/shared-feature-coverage.md, docs/javascript-api.md, docs/api/effects.md and the selected adapter guide. Mount one runtime per non-overlapping root; await readiness, connect render/input/quality owners explicitly, and destroy on disposal. Core clocks use 16 ticks per beat, distinct from native 64-pip patterns. Check reduced motion, forced colours, visibility, pause/seek/rate change, downgrade and recovery in the rendered result. Bound intermittent accents to one declared subject, including blur/shadow extents.

## Development checks

```sh
npm ci --ignore-scripts
npm run build
npm test
npm run test:legacy
```

Submit contributions to https://github.com/kieransimkin/DanceMoves/pulls. See the repository's current instructions before editing.
