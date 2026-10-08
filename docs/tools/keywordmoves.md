# KeywordMoves

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/keywordmoves)

Source-specific keyword research, local phrase extraction and reviewed evidence imports.

Read the selected plugin guide under docs before running it. Use google-search, bing-search or the named social module for that source; text-library extract-literal for contiguous local phrases; native-export and observed-evidence for reviewed exports/browser observations. Preserve raw exports and result JSON. Trends indices, impressions, platform counts, local occurrences and LLM proposals are different evidence. Paid providers, hosted inference and authenticated collectors need the user's explicit scope and budget. Do not add unsupported scraping.

## Development checks

```sh
python -m pip install -e ".[dev]"
python -m pytest
ruff check src tests
```

Submit contributions to https://github.com/kieransimkin/keywordmoves/pulls. See the repository's current instructions before editing.
