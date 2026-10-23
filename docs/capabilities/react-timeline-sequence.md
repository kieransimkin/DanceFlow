# React Timeline Sequence: capability and package reference

Audited 23 October 2026: **v0.8.0**, exact source [`169edf420bc4eb5c0664a10fb962421a5afe0814`](https://github.com/kieransimkin/react-timeline-sequence/tree/169edf420bc4eb5c0664a10fb962421a5afe0814). This is a dated source/documentation audit, not installed-runtime or end-to-end acceptance. [Check current releases before use](../workflows/release-preflight.md).

## Current README feature routes

- [Before every new workflow](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#before-every-new-workflow)
- [Find your route](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#find-your-route)
- [Install](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#install)
- [Use](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#use)
- [Lane content](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#lane-content)
- [Lyric timing audition](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#lyric-timing-audition)
- [Loop regions and buffered playback](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#loop-regions-and-buffered-playback)
- [Editable keyframe lanes](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#editable-keyframe-lanes)
- [Sample-frame BPM matching and editable timing lanes (v0.4)](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#sample-frame-bpm-matching-and-editable-timing-lanes-v04)
- [Composite audio lanes and display navigation](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#composite-audio-lanes-and-display-navigation)
- [Styling](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#styling)
- [Scope](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#scope)
- [Potential problems](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#potential-problems)
- [The timeline has no usable height](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#the-timeline-has-no-usable-height)
- [Audio plays but cross-origin media fails in some hosts](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#audio-plays-but-cross-origin-media-fails-in-some-hosts)
- [Development](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#development)
- [Coordinated releases and latest-release dependencies](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#coordinated-releases-and-latest-release-dependencies)
- [Agents and contributors](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#agents-and-contributors)
- [Licence](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md#licence)

## Source documentation and examples

- [`README.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md)
- [`docs/ECOSYSTEM.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/docs/ECOSYSTEM.md)
- [`docs/branding/README.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/docs/branding/README.md)
- [`docs/keyframe-lane.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/docs/keyframe-lane.md)
- [`docs/loops.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/docs/loops.md)
- [`docs/lyric-audition.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/docs/lyric-audition.md)
- [`docs/publishing.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/docs/publishing.md)
- [`docs/released-viewers.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/docs/released-viewers.md)
- [`docs/timing-editing.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/docs/timing-editing.md)

## Package evidence

- [`README.md`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/README.md) — SHA-256 `aa03b956ae2423764f3b05d3161ca2f3a5daea3bc686b9ac593af695a895d6af`.
- [`package.json`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/package.json) — SHA-256 `598f2503bd0de7778fb3f90ed655e9b17637e4f65a02c7d3a68d5e47ad7f343a`.
- [`LICENSE`](https://github.com/kieransimkin/react-timeline-sequence/blob/169edf420bc4eb5c0664a10fb962421a5afe0814/LICENSE) — SHA-256 `bc73e5152b5fe1716c5c8b5cb2b83d51b2e5300827bfa580eeb7a07a498aeafc`.

Package files were read at the pinned source. Published distributions, installed identity, working host examples, rights and reviewed output require their own verification.

## Historical detailed reference

The following older index is retained for detailed routes. Its earlier version is historical; the audited source links above identify current documented availability.

# react-timeline-sequence: complete capability reference

Inspected stable source: [v0.4.0](https://github.com/kieransimkin/react-timeline-sequence/releases/tag/v0.4.0), commit `e8ef859126f7d3c9abd07f371cef46b624d36ebc`. This is a dated baseline; [check current releases before every new workflow](../workflows/release-preflight.md).

## Choose and use a route

| Goal | Supported route and evidence |
|---|---|
| Mount real transport | Use the released React timeline and shared audio clock, typed lanes, zoom/pan/seek, buffered playback and sample-frame loops. |
| Inspect/edit timing | Use composite waveform/spectrogram source lanes, display navigation, editable keyframes and sample-frame BPM/lyric/cue timing lanes from the matching released API. Source analysis remains in StemLab. |
| Preserve identity | A drawn imitation or development package is not the released component. Rebuild actual client assets after a compatible package update and verify transport and painted controls. |

## Released reference coverage

Each entry links to the exact released explanation, options, example or limitation. These are documented capabilities, not a claim that every option was run on this computer. Review the relevant source before configuring it.

- [Agents and contributors](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#agents-and-contributors) — `README.md`.
- [Loop regions and buffered playback](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#loop-regions-and-buffered-playback) — `README.md`.
- [Install](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#install) — `README.md`.
- [Use](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#use) — `README.md`.
- [Lane content](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#lane-content) — `README.md`.
- [Styling](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#styling) — `README.md`.
- [Development](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#development) — `README.md`.
- [Scope](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#scope) — `README.md`.
- [Potential problems](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#potential-problems) — `README.md`.
- [The timeline has no usable height](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#the-timeline-has-no-usable-height) — `README.md`.
- [Audio plays but cross-origin media fails in some hosts](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#audio-plays-but-cross-origin-media-fails-in-some-hosts) — `README.md`.
- [Licence](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#licence) — `README.md`.
- [Composite audio lanes and display navigation](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#composite-audio-lanes-and-display-navigation) — `README.md`.
- [Coordinated releases and latest-release dependencies](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#coordinated-releases-and-latest-release-dependencies) — `README.md`.
- [Sample-frame BPM matching and editable timing lanes (v0.4)](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/README.md#sample-frame-bpm-matching-and-editable-timing-lanes-v04) — `README.md`.
- [Loop regions and buffered playback](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/loops.md#loop-regions-and-buffered-playback) — `docs/loops.md`.
- [Use](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/loops.md#use) — `docs/loops.md`.
- [Sample contract](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/loops.md#sample-contract) — `docs/loops.md`.
- [Playback and lifecycle](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/loops.md#playback-and-lifecycle) — `docs/loops.md`.
- [Build and test](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/loops.md#build-and-test) — `docs/loops.md`.
- [Reference](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/loops.md#reference) — `docs/loops.md`.
- [Patch validation](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/loops.md#patch-validation) — `docs/loops.md`.
- [Publishing react-timeline-sequence](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#publishing-react-timeline-sequence) — `docs/publishing.md`.
- [Release destinations](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#release-destinations) — `docs/publishing.md`.
- [npm bootstrap completed](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#npm-bootstrap-completed) — `docs/publishing.md`.
- [GitHub Packages](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#github-packages) — `docs/publishing.md`.
- [Making a release](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#making-a-release) — `docs/publishing.md`.
- [Potential problems](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#potential-problems) — `docs/publishing.md`.
- [npm publication reports an authentication error](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#npm-publication-reports-an-authentication-error) — `docs/publishing.md`.
- [npm 10 exits after showing the browser authentication link](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#npm-10-exits-after-showing-the-browser-authentication-link) — `docs/publishing.md`.
- [npm 12 refuses the release tarball as a Git dependency](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#npm-12-refuses-the-release-tarball-as-a-git-dependency) — `docs/publishing.md`.
- [The GitHub Packages copy has a different import name](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#the-github-packages-copy-has-a-different-import-name) — `docs/publishing.md`.
- [GitHub Packages publishing tries to clone a nonexistent repository](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#github-packages-publishing-tries-to-clone-a-nonexistent-repository) — `docs/publishing.md`.
- [CI reports the Vitest redirect-mock path-traversal advisory](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#ci-reports-the-vitest-redirect-mock-path-traversal-advisory) — `docs/publishing.md`.
- [A local Windows tar smoke test fails inside WinAVR](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/publishing.md#a-local-windows-tar-smoke-test-fails-inside-winavr) — `docs/publishing.md`.
- [Coordinated released-viewer workflow](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#coordinated-released-viewer-workflow) — `docs/released-viewers.md`.
- [Checkout layout and command](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#checkout-layout-and-command) — `docs/released-viewers.md`.
- [Release order and version selection](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#release-order-and-version-selection) — `docs/released-viewers.md`.
- [Latest stable releases, with an auditable build snapshot](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#latest-stable-releases-with-an-auditable-build-snapshot) — `docs/released-viewers.md`.
- [What must be committed together in StemLab](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#what-must-be-committed-together-in-stemlab) — `docs/released-viewers.md`.
- [Publication and Pages verification](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#publication-and-pages-verification) — `docs/released-viewers.md`.
- [Interrupted runs and failures](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#interrupted-runs-and-failures) — `docs/released-viewers.md`.
- [Source of truth](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#source-of-truth) — `docs/released-viewers.md`.
- [This repository's role](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/released-viewers.md#this-repositorys-role) — `docs/released-viewers.md`.
- [Musical clocks and editable timing](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/timing-editing.md#musical-clocks-and-editable-timing) — `docs/timing-editing.md`.
- [Fixed and variable tempo](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/timing-editing.md#fixed-and-variable-tempo) — `docs/timing-editing.md`.
- [Editable lyric lines, words and cues](https://github.com/kieransimkin/react-timeline-sequence/blob/v0.4.0/docs/timing-editing.md#editable-lyric-lines-words-and-cues) — `docs/timing-editing.md`.

## Development differences

The inspected main checkout has different documentation at the following paths. Verify its own matching release before adopting changes beyond the baseline above:

- `README.md`
- `docs/keyframe-lane.md`

## Examples and media

Use the runnable examples and actual screenshots/videos linked from the released references. Keep their documented version/context and distinguish synthetic fixtures, model hypotheses and real captured output. Do not represent a guide link as proof that a model, GPU, physical phone or production host was tested. New decorative generated imagery adds no feature evidence to this reference index.
