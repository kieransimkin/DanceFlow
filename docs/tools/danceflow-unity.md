# DanceFlow for Unity

[DanceFlow ecosystem](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/DanceFlow.Unity)

The Unity 6 UPM package `com.kieransimkin.danceflow.unity` brings source-bound musical clocks, shader phases, finite DanceRudiments recordings and preview rigged-character playback into Unity. The audited manifest is `0.5.0-preview.1`; it is source, not a stable published release.

Phases 1–3 implement fixed/verified variable tempo, DSP/manual transport, 16-tick/64-pip timing, cues, GPU clock uniforms, DFR1 caches, explicit recording time mappings and song-reactive landscapes. Stage 4 previews typed rig-profile/rig-motion validation, quaternion sampling, reviewed bone mappings and transform/Playables playback.

Install a reviewed commit through Unity Package Manager. Import the opt-in Beat Phase Cube, Shader Clock URP, Song Reactive Landscape or Rigged Character Demos sample. The synthetic rig demo creates two skinned robots with a silent 120-BPM clock. It does not prove real-character retargeting or actual song alignment. External FBX, CMU recordings, audio and weights remain separate rights-controlled inputs.

Read the [source-pinned capability reference](../capabilities/danceflow-unity.md) and [joint workflow](../workflows/potbot-unity.md). Managed/static tests are useful contract evidence; Unity Editor/PlayMode, framebuffer/GPU, licensed WebGL builds, physical timing and real-character acceptance remain separate gates.

![Generated diagram of the supported evidence handoffs](../media/potbot-unity-handoffs.svg)

Generated contract illustration, not Unity rendering evidence. Use the canonical samples to produce actual Editor/GPU captures after the corresponding host acceptance. Discovery never starts Unity or installs its package.

## Deployed WebGL example, separately verified

The [Kandi Boom portal](https://kieransimkin.github.io/DanceFlow.Unity/) and [Unity WebGL player](https://kieransimkin.github.io/DanceFlow.Unity/kandi/) returned HTTP 200 on 23 October 2026. [The deployment workflow](https://github.com/kieransimkin/DanceFlow.Unity/actions/runs/39891902738) succeeded for source `ba3124e0075584d94a54f8e7137fbacdd036b774`; a signed-out headless Edge check loaded the WebGL canvas and visible scene without page exceptions. That scene showed a loading song and a magenta surface under SwiftShader. This is evidence of a deployed executable and an emulated render, not a clean physical-GPU result, verified song playback, accepted retargeting or complete Unity package qualification. The source includes a three-song gallery with independent motion candidates; unknown BPM/phase and mix identity remain explicit.
