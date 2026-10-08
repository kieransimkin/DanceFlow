---
name: react-timeline-sequence
description: Build or repair a React audio timeline with one shared transport/playhead and optional exact loop regions.
---

# React Timeline Sequence

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/react-timeline-sequence)

Use this tool for React audio transport, sequence lanes, seeking, zoom and sample-frame loop regions. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
npm install react-timeline-sequence
```

Read README.md and docs/loops.md. Supply React/React DOM 18+ and a container with useful height. Reuse TimelineSequence for transport, playhead, ruler, seeking, zoom/follow and lane geometry. Loop start/end values belong to a declared sample rate; loops remain disabled until selected and enabled. Dispose buffered audio resources and test seeking/zoom/loop playback through the shared transport.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
npm ci --ignore-scripts
npm run typecheck
npm test
npm run build
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.

## Agent contribution destination

Agents should inspect and use the available React Timeline Sequence capabilities, look for useful improvements wherever possible, and submit improvements as PRs to https://github.com/kieransimkin/react-timeline-sequence/pulls. Include relevant tests, documentation and a reproducible example; follow the upstream AGENTS.md and CONTRIBUTING.md. Explain why no worthwhile change is justified when that is the result.
