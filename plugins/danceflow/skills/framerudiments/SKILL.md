---
name: framerudiments
description: Render offline Shorts, Canvas-style videos and lyric visualisers from native DanceRudiments motion and saved StemLab timing or recordings.
---

# FrameRudiments

[DanceFlow](https://kieransimkin.co.uk/danceflow/) Â· [Source](https://github.com/kieransimkin/FrameRudiments)

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
wheel render. Preserve immutable versions and automatic software publication after checks; media schedules and site deployment retain their own requirements.


For rudiment-driven particles, bars, waveform traces, XY paths or spectra, use
the modular `type: "rudiment"` layer and the canonical renderer/spectrum guides.
Select original recording dimensions, bounded history and viewports; keep
waveform traces distinct from PCM. Spectrum requires recoverable StemLab Fourier
calibration, exact frequency ranges and silent-band handling. Retain the hashed
`rudiment-analysis.jsonl` peak/hold reports and verify encoded representative
states. Extend the trusted Python registry for a reusable view rather than
copying sampling, analysis or frame loops. Optional demo generation uses
StemLab 1.6+; saved-recording rendering requires no new model run.

Optional ordered `effects` stages use Butterchurn 2.6.7 and projectM 4.2-dev
at exact source `349b7cc2db312d47cef6be24c6856ced6643a385`. Both process the
complete composed frame, including captions, lyric art, DanceRudiments-moving
sprites and beat-animated atlases, before encoding. Choose either engine or a
chain with original feedback, kaleidoscope and Julia-distortion presets.
Read the canonical [visualiser setup and contract](https://github.com/kieransimkin/FrameRudiments/blob/main/docs/visualisers.md).
Use `visualisers` to inspect pins and explicit `effects-setup` to provision a
runtime. Preserve exact output clocks and PCM from the same trim/repeat/fade
chain as the soundtrack. Retain preset/runtime/bridge hashes and cleanup
receipts. Feedback is sequential; recreate/replay to seek. GPU pixels vary by
driver, and pre-effect text bounds do not prove final legibility or safe zones.
Verify real shader/glyph/sprite feedback and encoded output; keep optional
engine setup, licences and trusted executable presets explicit.
