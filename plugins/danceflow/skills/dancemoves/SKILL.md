---
name: dancemoves
description: Implement or debug rhythmic web effects in JavaScript, React, Next.js or the WordPress adapter.
---

# DanceMoves

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/DanceMoves)

Use this tool for BPM-synchronised web motion, shared clocks, effects, input, lifecycle and adaptive quality. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
npm install @kieransimkin/dancemoves
```

Start with docs/shared-feature-coverage.md, docs/javascript-api.md, docs/api/effects.md and the selected adapter guide. Mount one runtime per non-overlapping root; await readiness, connect render/input/quality owners explicitly, and destroy on disposal. Core clocks use 16 ticks per beat, distinct from native 64-pip patterns. Check reduced motion, forced colours, visibility, pause/seek/rate change, downgrade and recovery in the rendered result. Bound intermittent accents to one declared subject, including blur/shadow extents.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
npm ci --ignore-scripts
npm run build
npm test
npm run test:legacy
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.

## Agent contribution destination

Agents should inspect and use the available DanceMoves capabilities, look for useful improvements wherever possible, and submit improvements as PRs to https://github.com/kieransimkin/DanceMoves/pulls. Include relevant tests, documentation and a reproducible example; follow the upstream AGENTS.md and CONTRIBUTING.md. Explain why no worthwhile change is justified when that is the result.
