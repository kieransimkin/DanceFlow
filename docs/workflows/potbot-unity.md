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

## Qualify the actual native host

| Check | Evidence required | Still separate |
| --- | --- | --- |
| Potbot connectivity | Bounded connection to the intended endpoint; distinguish TCP, authentication challenge and authenticated login | Application provisioning and task execution |
| Potbot application identity | Read-only role/schema checks, required migrations, restricted login and scoped workspace/principal binding | Admin login, model readiness and Linux isolation |
| Unity package installation | Fresh minimal consumer resolving the complete pinned root Git package; read back `packages-lock.json` | A copied subset of source folders or managed harness |
| Unity runtime/GPU | Discovered, passing Editor/PlayMode cases plus actual device identity and framebuffer readback | Synthetic song alignment, real-character retargeting and public WebGL deployment |
| Unity generated scenes | Save and reopen with persistent mesh/material/avatar and recording/profile references; exercise skinning, seeks and finite bounds | A live unsaved scene or transform-only inspection |

Resolve Potbot credentials through the selected native profile without printing values. Compare the saved endpoint with the operator's intended target before connecting. Start with read-only metadata and bounded timeouts; do not turn a successful login into an automatic migration or test-suite target. An administrative account can authenticate while the application correctly refuses it. Application logins must lack RLS bypass, role/database creation, inherited roles and application-object ownership; retain the native guard's refusal as evidence. Use the separately authorised provisioning workflow and an isolated test target for write tests. Compare PostgreSQL/pgvector versions with the qualified source baseline instead of assuming that any installed vector extension is accepted.

An empty editor list or credential status from a restricted execution context does not establish absence on the actual native host. If there is a concrete sandbox/access discrepancy, use the supported native diagnostic in the appropriate authorised context and retain both observations. Do not inspect private application state, change accounts/ACLs or install another host merely to resolve an incomplete diagnostic.

Unity package dependencies must declare every built-in module used by runtime code, rather than relying on a template's transitive modules. Import selected samples explicitly. Keep graphics enabled for GPU acceptance; inspect XML case results as well as the process exit. Missing, skipped and inconclusive required cases remain incomplete. Let `-runTests` finish without `-quit`; use a synchronous render request or supported yield rather than `WaitForEndOfFrame` in Editor batch mode. Preserve actual readback captures with the source/consumer lock, Editor, pipeline and device identity. A clean native GPU check does not repair an older public WebGL build. See [Unity's batch compatibility reference](https://docs.unity.cn/Manual/CLIBatchmodeCoroutines.html) and the canonical Unity repository's native acceptance instructions.

## Potential problems

- **No stable release:** successful official release queries may return none. Record `no_stable_release`, exact source commit and preview manifest; never call a cached version current or misreport this as a network failure.
- **Unity sample appears complete:** managed/static tests do not establish actual skinning, framebuffer rendering, audio-to-photon timing or external asset permission.
- **MCP feature appears in a plan:** distinguish the hub's discoverable references from Potbot's unimplemented consumer and the Unity Editor host.
- **Package docs drift:** compare catalogue, skill, capability reference, guide, release preflight, wheel and portable ZIP membership; verify installed resource readback rather than only a source tree.

## Deployed WebGL example, separately verified

The [Kandi Boom portal](https://kieransimkin.github.io/DanceFlow.Unity/) and [Unity WebGL player](https://kieransimkin.github.io/DanceFlow.Unity/kandi/) returned HTTP 200 on 23 October 2026. [The deployment workflow](https://github.com/kieransimkin/DanceFlow.Unity/actions/runs/39891902738) succeeded for source `ba3124e0075584d94a54f8e7137fbacdd036b774`; a signed-out headless Edge check loaded the WebGL canvas and visible scene without page exceptions. That scene showed a loading song and a magenta surface under SwiftShader. This is evidence of a deployed executable and an emulated render, not a clean physical-GPU result, verified song playback, accepted retargeting or complete Unity package qualification. The source includes a three-song gallery with independent motion candidates; unknown BPM/phase and mix identity remain explicit.
