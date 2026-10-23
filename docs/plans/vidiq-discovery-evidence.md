# What vidIQ's distribution teaches the DanceFlow plan

Primary-source review, 23 October 2026. This is a comparison of visible distribution and packaging choices. It does not establish the private reason a vendor or model recommended vidIQ, nor demonstrate that DanceFlow has been approved.

![Generated diagram separating provider packaging, host discovery and user outcomes](../media/vidiq-discovery-evidence.svg)

*Generated explanatory illustration. Arrows are proposed measurement boundaries, not observed conversion rates or a representation of a vendor's ranking algorithm. This static research has no new runtime interaction to record; capture actual host setup and task execution during the experiments below.*

## Verified observations and their limits

| Observation | Primary evidence | Implication for DanceFlow |
| --- | --- | --- |
| vidIQ has a published OpenAI listing with task examples, a connected app, skills and support/privacy links. | [OpenAI listing](https://openai.com/business/plugins/vidiq/) | Prepare a complete task-led product and reviewer package. A public MCP endpoint alone does not establish this distribution state. |
| Its hosted MCP endpoint is public and uses account authorization. Its guides provide separate ChatGPT, Claude and other-client setup paths. | [MCP guide](https://vidiq.com/mcp/), [support instructions](https://support.vidiq.com/en/articles/15082430-vidiq-mcp) | Reduce setup friction on each supported host; keep local/remote architecture and publisher eligibility as explicit decisions. |
| Its own Claude guide links a connector listing and explains manual connection as another route. The directory connector exposes a narrower tool surface. | [Claude guide](https://vidiq.com/claude/), [support instructions](https://support.vidiq.com/en/articles/15082430-vidiq-mcp) | Test each host/connection route separately. The Claude directory destination could not be independently fetched in this review; provider documentation is the evidence for that listing. |
| A public repository distributes manifests, skills and a marketplace, while the hosted service is separate. | [Pinned repository revision](https://github.com/vid-io/vidiq-mcp/tree/a6e806e9e6ffd9cbd482e5f529f4ef0d358849a3), [MCP configuration](https://github.com/vid-io/vidiq-mcp/blob/a6e806e9e6ffd9cbd482e5f529f4ef0d358849a3/.mcp.json) | Maintain portable source and explicit installation routes alongside any vendor submissions. A provider-owned marketplace is distinct from a vendor-curated marketplace. |
| The repository manifest and marketplace describe concrete creator jobs and include subject/task keywords. | [Manifest](https://github.com/vid-io/vidiq-mcp/blob/a6e806e9e6ffd9cbd482e5f529f4ef0d358849a3/plugin.json), [marketplace](https://github.com/vid-io/vidiq-mcp/blob/a6e806e9e6ffd9cbd482e5f529f4ef0d358849a3/.claude-plugin/marketplace.json) | Use ordinary task language and capability-backed keywords consistently across manifests, skill descriptions and examples. This is wording evidence, not demand or proof of ranking impact. |
| Its guided workflows describe intended inputs/results, account requirements, costs and approval boundaries. | [Skills catalogue](https://vidiq.com/agent-skills/), [onboarding source](https://github.com/vid-io/vidiq-mcp/blob/a6e806e9e6ffd9cbd482e5f529f4ef0d358849a3/skills/vidiq-get-started/SKILL.md) | Help users reach one useful result; make unavailable dependencies, costs and consequential actions visible. Do not copy its provider-specific permissions into DanceFlow. |

The inspected public repository identifies version `0.2.1` and 14 workflows; the public skills page describes 12 workflows, while the installed OpenAI distribution inspected locally identifies package version `9.0.0` and 12 skill folders. These are different distribution surfaces and version namespaces. They cannot establish chronological age or exact tool parity. The MCP landing page and support article also differ in tool counts and platform coverage. Record the exposed tools on the actual route before promising a capability; do not infer a broken integration or failed approval from these differences alone.

OpenAI's documented discovery route includes name search and direct listing links. Enhanced placement or proactive suggestions may depend on demonstrated utility and user satisfaction; developers cannot request that treatment. Its specific reason for recommending vidIQ, reviewer scores, retention data, contracts and search-ranking weights remain unknown. [Distribution guidance](https://developers.openai.com/plugins/deploy/app-review).

## Comparison with Metricool

Metricool likewise has an [OpenAI plugin listing](https://openai.com/business/plugins/metricool/) and a documented [remote MCP connection](https://help.metricool.com/how-to-connect-metricools-mcp-eqp9h). Both providers supply an existing domain product through an authenticated integration with a clear user job. vidIQ adds a particularly visible public skills/marketplace and client-specific instruction trail. This small, selected sample supports product and onboarding hypotheses; it cannot isolate what caused either recommendation or prove that every recommended provider needs the same architecture.

## Immediate improvements

The source audit found actionable defects independent of recommendation experiments. These changes belong to the `0.1.18` candidate; require normal CI and release readback before calling them released.

| Priority | Concrete change | Acceptance evidence |
| --- | --- | --- |
| P0 | Align marketplace and MCP launcher versions with the plugin. Both marketplace entries advertised `0.1.15` and the Claude launcher pinned `0.1.12` while manifests identified `0.1.17`. | Validator compares both marketplace versions and both launcher pins with the canonical manifest/project version. |
| P0 | Replace the 39/40-character OpenAI short descriptions with the same 29-character description. | Both interfaces agree and satisfy the current 30-character final-submission limit. This fixes one listing defect, not overall eligibility. |
| P1 | Align descriptions, capabilities and task keywords across portable, Codex and Claude manifests. Remove the stale fifteen-component claim. | Validator checks shared metadata and the existing seventeen-component catalogue/skills/docs contract. |
| P1 | Use three task examples: song analysis, lyric-video rendering and media-clock web effects. | Prompts are distinct, bounded by documented field limits and refer to existing component roles; runtime prerequisites remain explicit. |
| P1 | Make setup produce the relevant operation, actual runtime state and smallest missing prerequisite. | Updated setup skill routes discovery-only requests without unnecessary file access, downloads or paid analysis. Live first-task conversion remains unmeasured. |
| P1 | Retain this comparison and reproducible tests in the approval plan and continuing review. | Public sources, pinned revision, uncertainty and experiment outcomes remain separately recorded. |

The [current OpenAI final-submission constraints](https://developers.openai.com/plugins/deploy/submission-errors) also cover identity, scans, auth, policies and reviewer evidence. Passing local metadata checks does not waive those requirements.

## Research that can change the next decision

The [versioned intent corpus](fixtures/discovery-intents-v1.json) contains 30 positive routing hypotheses across all seventeen components and ten negative controls. Every outcome starts as `not_run`. It is preparation for host trials, separate from OpenAI's exact reviewer test-case counts and from proof that an agent selects a tool correctly.

| Question | Bounded next experiment | Decision and limitation |
| --- | --- | --- |
| Which product route can genuinely qualify? | Read existing publisher/portal records and current local/remote eligibility; compare the same three jobs. | Choose remote, eligible local MCP or deliberate skills-only packaging before hosting work. Unknown portal state remains a dependency. |
| Do task descriptions improve selection? | Freeze 40 prompts with held-out paraphrases and near misses; compare baseline and candidate on one host at a time. | Measure correct routing, false triggers and completed tasks. Manual metadata review is not an agent-selection result. |
| Does setup prevent abandonment? | Clean allowed installation; record prerequisite discovery, first useful output, elapsed time and exact failure. | Improve the highest observed friction; distinguish install, authorization, runtime readiness and completion. |
| What language has actual demand? | Import authorized native query/referral evidence with source, dates, unit and market. | Prioritize relevant intents from measured evidence; local phrase counts and third-party estimates remain separate. |
| Can an uninstalled agent find and suggest it? | After listing eligibility, use matched unfamiliar sessions with no brand, URL or installation hint. | Record directory availability, discovery, suggestion and user consent separately. A branded example only tests explicit invocation. |
| Do clients ingest MCP Registry entries? | Check each client's primary documentation and verify one lookup/install path. | Claim only the tested path. A public Registry record is not universal auto-discovery. |
| Which surface is current and useful? | Record exact installed package, manifest hash, exposed tools and supported operations for each host/route. | Detect scope drift and observe reliability; avoid summing unrelated catalogue counts. |
| What supports repeat use and distribution? | Compare complete consented windows of task success, failures, latency, return use and user feedback. | Investigate usefulness and satisfaction without inferring private vendor weights or causality. |

For Potbot, these findings reinforce its existing [discovery strategy](https://github.com/kieransimkin/potbot/blob/main/docs/implementation/plugin-discovery-strategy.md): capture provenance, host/transport, actual tool surface, setup prerequisites, cost and permission state in candidate evidence; rank by task fit and observed quality; keep retrieval, admission, user-approved installation and runtime qualification separate. No owned-project preference, automatic installation or completion of T04 stages is established by this research.

The weekly research goal should compare both vidIQ and Metricool, refresh the source snapshot, keep the experiment backlog small and update strategy only when evidence changes. No paid provider call, private channel analysis or model download was needed for this review.
