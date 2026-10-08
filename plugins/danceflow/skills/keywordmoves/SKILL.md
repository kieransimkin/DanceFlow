---
name: keywordmoves
description: Research keywords or import, validate and compare dated search/platform evidence without mixing unlike metrics.
---

# KeywordMoves

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/keywordmoves)

Use this tool for source-specific keyword research, local phrase extraction and reviewed evidence imports. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
python -m pip install keywordmoves
keywordmoves plugins --json
```

Read the selected plugin guide under docs before running it. Use google-search, bing-search or the named social module for that source; text-library extract-literal for contiguous local phrases; native-export and observed-evidence for reviewed exports/browser observations. Preserve raw exports and result JSON. Trends indices, impressions, platform counts, local occurrences and LLM proposals are different evidence. Paid providers, hosted inference and authenticated collectors need the user's explicit scope and budget. Do not add unsupported scraping.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
python -m pip install -e ".[dev]"
python -m pytest
ruff check src tests
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.
