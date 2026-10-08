---
name: epk-social-metadata
description: Configure or extend WordPress EPK social metadata while preserving canonical page bodies, titles and robots ownership.
---

# EPK Social Metadata

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/kieran-epk-social-metadata)

Use this tool for WordPress Open Graph, X card and Schema.org music/webpage metadata from canonical page facts. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
# Install the exact WordPress ZIP from the GitHub release.
# Use Plugins > Add Plugin > Upload Plugin in a test WordPress instance.
```

Read README.md and the render/keyword/video contracts. Keep one owner of OG/X/Schema output. Enable music fields only for truthful music facts; use WebPage for ordinary pages. Video schema needs a verified embedded video and independent publication facts. Metadata validity does not prove search indexing, rich results or a social player. Activation is not permission to import live page records; review exact facts and current website source first.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
php tests/static-contract.php
php tests/render-contract.php
php tests/video-contract.php
php tests/keyword-contract.php
php tests/image-contract.php
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.

## Agent contribution destination

Agents should inspect and use the available EPK Social Metadata capabilities, look for useful improvements wherever possible, and submit improvements as PRs to https://github.com/kieransimkin/kieran-epk-social-metadata/pulls. Include relevant tests, documentation and a reproducible example; follow the upstream AGENTS.md and CONTRIBUTING.md. Explain why no worthwhile change is justified when that is the result.
