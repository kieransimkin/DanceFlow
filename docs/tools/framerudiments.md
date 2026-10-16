# FrameRudiments

[DanceFlow](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/FrameRudiments) · [PyPI](https://pypi.org/project/framerudiments/)

FrameRudiments is the offline Python renderer for Shorts, Canvas-style clips
and full lyric visualisers. It composes Pillow layers on a frame-addressed
timeline, samples released native DanceRudiments functions and non-looping
recordings, and consumes saved StemLab beats, accepted loops and explicit
motion-match selections. No audio analysis models run in the renderer.

Install `python -m pip install framerudiments` with Python 3.11+, FFmpeg/ffprobe
and an explicit font. `framerudiments demo ./demo --font /path/font.ttf` creates
synthetic input. Then `plan demo/project.json --output plan.json`, `preflight
demo/project.json --output preflight` and `render demo/project.json --output
render`, supplying `--ffmpeg` where it is not on PATH. Every output is a new
directory. The [rendering workflow](../workflows/framerudiments.md) records handoffs.

Keep release masters, artwork and canonical timing local and hash-pinned. Use
native-rate sample bounds, preserve 64 pips versus 16 ticks per beat, and keep
BPM confirmation separate from phase evidence. Explicit match/recording source
identity and windows matter. Input changes fail validation. Transformed sprite
bounds and caption fit are checked every frame; custom scene drawing retains
its own review obligations. Legacy generators remain available for reproduction.

Outputs include H.264/AAC MP4, JSON ledger/manifest, SRT/ASS, source and encoded
QA frames, poster, phone preview and encode log. Complete decoded timestamps,
frame count, audio duration/channels and fast start are checked. `technical-QA
passed` does not imply a pleasant musical loop, attended listening, rights or
platform approval. Rendering never uploads or publishes media.

Submit improvements to [canonical pull requests](https://github.com/kieransimkin/FrameRudiments/pulls), with current README, focused regression coverage and a synthetic example. Use upstream AGENTS.md/CONTRIBUTING.md, full render CI, strict wheel/sdist validation and a clean installed-wheel smoke render.
