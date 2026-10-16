---
name: framerudiments
description: Render offline Shorts, Canvas-style videos and lyric visualisers from native DanceRudiments motion and saved StemLab timing or recordings.
---

# FrameRudiments

[DanceFlow](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/FrameRudiments)

Use the shared Python renderer for new or materially revised offline videos.
Read its current README and project-format guide; use the existing historical
generator when reproducing an approved old film. Keep release artwork/layouts
in declarative projects or scene hooks. Improve a reusable missing mechanism
in FrameRudiments instead of copying another clock, caption or encoder loop.

Install `framerudiments` from PyPI in a dedicated Python 3.11+ environment and
provide FFmpeg/ffprobe and an explicitly selected font. Inspect `framerudiments
--help`; `demo` creates synthetic fixtures, `plan` validates pins and exports
the frame ledger, `preflight` checks every composed frame and `render` encodes
and verifies a new output directory. No command publishes or schedules media.

Pin the exact authorised master, canonical LRC/CUE/font/artwork and source
sample bounds. Reuse StemLab beat/loop/matcher/recording files, retaining report
hashes, source offsets, BPM and phase status. Explicitly select a match window;
scores do not approve motion. Native recordings stop at capture bounds and
keep all axes and their own 64-pip clock. One DanceMoves tick is four pips.

Use one frame ledger for caption state, clears and subtitle sidecars. Keep
structural cues separate from lyrics and optional canonical-text comparison
exact. Short derivatives default to 120 ms quarter-sine endpoint fades; retain
an approved raw seam with `audio.fade_seconds: 0`. Canvas/full visualisers
default to no fades. Never change the source master or stretch audio for frames.

Inspect the encoded poster, caption/scene boundaries and final frames, all
transformed alpha bounds and the destination's current safe areas. Technical
QA and a clean decode do not establish listening approval, musical seams,
rights, platform preview acceptance or public eligibility. Custom scene hooks
must pin their own assets and verify their own painted bounds/collisions.

Contribute focused fixes with current README, synthetic tests and a reproducible
example to https://github.com/kieransimkin/FrameRudiments/pulls. Run the full
FFmpeg/font-enabled suite, ruff, build, strict package checks and an installed
wheel render. Preserve immutable versions and separate publication approvals.
