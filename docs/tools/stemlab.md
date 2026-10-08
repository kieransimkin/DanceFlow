# StemLab

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/stemlab)

Music, stem, rhythm, structure, harmony, lyrics, sonic features and loop evidence.

Read docs/README.md and docs/codex-publishing.md. Prefer the existing React timeline for playback and saved reports for exact bounds. Discover model availability before inference. Loops use inclusive start_sample and exclusive end_sample at the native rate; a 48 kHz grid cannot be applied to a 44.1 kHz master. Model downloads, expensive jobs and model-specific licences require explicit choices. Poll jobs until completion and inspect backend errors.

## Development checks

```sh
python -m pip install -e ".[dev]"
python -m pytest
ruff check src tests scripts
```

Submit contributions to https://github.com/kieransimkin/stemlab/pulls. See the repository's current instructions before editing.
