# Potbot and Unity ecosystem handoffs

Before use, [check official releases and exact runtimes](release-preflight.md). Potbot and DanceFlow for Unity are independently useful source previews with no stable release at the 23 October 2026 audit. Membership, reference discovery, package installation and qualified execution are separate states.

![Supported source and evidence routes](../media/potbot-unity-handoffs.svg)

Generated contract diagram. Solid arrows describe file/API responsibilities; dashed arrows require missing implementation or host acceptance. This image does not prove end-to-end execution.

## Discover without provisioning hosts

Call `danceflow_search` with `{"query":"Unity rig recording"}` or `{"query":"Potbot evidence"}`; follow the returned component and reference calls. `danceflow_component` reports `native_host_required` and source-preview qualification for these components. No execution tool is registered for either host. Run `python examples/ecosystem_discovery.py` from the toolkit checkout for a bounded, no-service discovery example.

## Compose audio and native motion into Unity

1. Reuse reviewed StemLab analysis and exact master/source identity. Export the supported `stemlab.beat-timeline.v1` when variable tempo is needed; unconfirmed BPM remains unconfirmed.
2. Generate or reuse native DanceRudiments `dancerudiments.recording`, rig-profile and rig-motion assets. Retain original sample/pip bounds, dimension names, finite values, recording clock, profile SHA-256 and permitted asset provenance. Do not derive song alignment from a preview clock or candidate score.
3. Install the pinned `com.kieransimkin.danceflow.unity` source in Unity 6. Import a selected sample. Use the canonical importer, `DanceFlowClockBehaviour.UseStemLabTimeline`, explicit `RecordingTimeMapping` and reviewed bone mappings. Do not copy the motion engine into a page or renderer.
4. Run the Unity repository's clock/recording/rigging harnesses and Python fixture/showcase checks. Separately verify actual Unity Editor/PlayMode, shader/GPU output, seek/end/bounds behaviour and any real-character/retargeting route. Retain precise unavailable gates and actual captures.
5. Use FrameRudiments for supported offline composition and DanceMoves for live web playback. A Unity source sample does not replace either engine or establish a WebGL deployment. EPKs link only to verified public examples and preserve privacy, rights and exact public-save gates.

## Compose Potbot without inventing an MCP bridge

Use Potbot's existing native CLI/API for durable tasks, evidence, patch handoffs, usage and worker reconciliation on its qualified host. Its proposed universal tool/MCP consumer is tracked in `docs/potbot-tool-mcp-implementation-bundle/`; do not label those stages implemented or send DanceFlow calls through a fictional adapter. A future consumer must preserve tool schema, workspace, effect/consent, job, receipt and source-clock contracts. Implementation belongs in Potbot, not a second job/database subsystem in the toolkit.

Source package review, `potbot info` and CLI help can run without models or PostgreSQL. Full startup, hosted inference, credentials, database migration and Linux execution acceptance need their own authorised host setup. A registered model name is not qualification. Store downloaded weights and caches beneath the owning project's ignored `models/`.

## Potential problems

- **No stable release:** successful official release queries may return none. Record `no_stable_release`, exact source commit and preview manifest; never call a cached version current or misreport this as a network failure.
- **Unity sample appears complete:** managed/static tests do not establish actual skinning, framebuffer rendering, audio-to-photon timing or external asset permission.
- **MCP feature appears in a plan:** distinguish the hub's discoverable references from Potbot's unimplemented consumer and the Unity Editor host.
- **Package docs drift:** compare catalogue, skill, capability reference, guide, release preflight, wheel and portable ZIP membership; verify installed resource readback rather than only a source tree.

## Deployed WebGL example, separately verified

The [Kandi Boom portal](https://kieransimkin.github.io/DanceFlow.Unity/) and [Unity WebGL player](https://kieransimkin.github.io/DanceFlow.Unity/kandi/) returned HTTP 200 on 23 October 2026. [The deployment workflow](https://github.com/kieransimkin/DanceFlow.Unity/actions/runs/39891902738) succeeded for source `ba3124e0075584d94a54f8e7137fbacdd036b774`; a signed-out headless Edge check loaded the WebGL canvas and visible scene without page exceptions. That scene showed a loading song and a magenta surface under SwiftShader. This is evidence of a deployed executable and an emulated render, not a clean physical-GPU result, verified song playback, accepted retargeting or complete Unity package qualification. The source includes a three-song gallery with independent motion candidates; unknown BPM/phase and mix identity remain explicit.
