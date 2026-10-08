# Arcadians playground

[DanceFlow](https://kieransimkin.co.uk/danceflow/) · [Arcadians by Kieran Simkin](https://kieransimkin.co.uk/arcadians/)

The full public MP3 and unchanged artwork are hash-pinned to the published StemLab example. Only public audio and reference timing are downloaded. Private lossless masters and campaign records are excluded.

Run from the repository root with Python 3.13 and Node 22 or newer:

```sh
python -m pip install -e .
# Only the waveform primitive is required here; this is not a full StemLab analysis installation.
python -m pip install --no-deps danceflow-stemlab==1.3.3
python -m pip install numpy soundfile fastapi
npm ci --prefix demos
python scripts/prepare_arcadians.py
npm run build --prefix demos
python -m http.server 8897 --bind 127.0.0.1 --directory docs/playground
```

StemLab generates the real waveform. Artist references supply sections and lyric timing. KeywordMoves produces a saved literal-extraction report, which the static UI filters. DanceRudiments 0.2.3 samples its actual C++/WASM catalogue at integer pips; DanceMoves 3.1.15 owns the media clock, playback lifecycle, accessibility and adaptive quality. React Timeline Sequence 0.2.1 owns the timeline transport and sample-frame audition ranges. This does not establish inferred downbeats or accepted seamless loops, neural analysis accuracy, PixelCue inference, or RasterMoves model performance.

The motion subject is bounded to 96 px plus maximum ±64 px/±24 px travel, inside a stage with at least 320 px width and 230 px height on desktop. On narrow screens the token is reduced to 72 px with the same travel. There are no glows or particles. Preference overrides remain authoritative after a manual quality restoration.

Demo application code that composes DanceMoves is GPL-2.0-or-later. Components retain their original licences; served licence files accompany the bundle. Arcadians music, lyrics and artwork remain Kieran Simkin's materials, supplied for these examples rather than relicensed as software.
