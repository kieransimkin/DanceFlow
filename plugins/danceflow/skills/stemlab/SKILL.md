---
name: stemlab
description: Analyse local music or inspect existing StemLab reports and sample-exact loop boundaries.
---

# StemLab

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/stemlab)

Use this tool for music, stem, rhythm, structure, harmony, lyrics, sonic features and loop evidence. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
python -m pip install "danceflow-stemlab[codex]"
stemlab --help
```

Read docs/README.md and docs/codex-publishing.md. Prefer the existing React timeline for playback and saved reports for exact bounds. Discover model availability before inference. Loops use inclusive start_sample and exclusive end_sample at the native rate; a 48 kHz grid cannot be applied to a 44.1 kHz master. Model downloads, expensive jobs and model-specific licences require explicit choices. Poll jobs until completion and inspect backend errors.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
python -m pip install -e ".[dev]"
python -m pytest
ruff check src tests scripts
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.

## Agent contribution destination

Agents should inspect and use the available StemLab capabilities, look for useful improvements wherever possible, and submit improvements as PRs to https://github.com/kieransimkin/stemlab/pulls. Include relevant tests, documentation and a reproducible example; follow the upstream AGENTS.md and CONTRIBUTING.md. Explain why no worthwhile change is justified when that is the result.

## Current releases and full feature routing

Before every new workflow, follow the [release preflight](https://github.com/kieransimkin/DanceFlow/blob/main/docs/workflows/release-preflight.md) and [complete capability reference](https://github.com/kieransimkin/DanceFlow/blob/main/docs/capabilities/stemlab.md). Observe the real installed runtime, review every relevant feature and compose supported ecosystem tools. Improve a demonstrated reusable gap in its canonical repository, or record why the tool already meets the need. This guidance does not trigger unrelated processing or downloads.

## Source-bound Unity and agent handoffs

For a relevant Unity/rig or Potbot task, read danceflow://workflows/potbot-unity and the matching preview skill. Preserve original master/beat/recording clocks, finite bounds and rig profile hashes; reuse canonical engines. A documented source preview is distinct from a qualified native host or a working MCP consumer.
