# Potbot

[DanceFlow ecosystem](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/potbot)

Potbot is an evidence-driven coding agent with durable tasks, contracts, artifacts, budgets, model invocation records, PostgreSQL jobs and a REST/WebSocket dashboard. Source `0.5.0.dev2` implements phases 1–4 and the phase 5 foundation. No stable GitHub release was present at the 23 October 2026 audit.

The current flow uses operator-selected tools and scripted proposals. Hosted Claude, OpenAI, Grok, Gemini and EvoLink adapters have explicit disclosure, rate and usage policies. Local model catalogue entries are unqualified until host acceptance succeeds. Linux worker execution requires qualified Bubblewrap/seccomp isolation; Windows CLI discovery does not establish that isolation.

DanceFlow catalogue and skill discovery now cover Potbot. **Potbot consuming DanceFlow MCP remains planned in its own implementation tracker.** Do not infer a live bridge, installation, model readiness or deployment from membership. Use the [source-pinned capability reference](../capabilities/potbot.md) and [joint workflow](../workflows/potbot-unity.md).

![Generated diagram of the supported evidence handoffs](../media/potbot-unity-handoffs.svg)

Generated contract illustration. Dashed routes are planned or require host acceptance; this is not a screenshot of a running Potbot service. Follow the canonical README for actual startup and dashboard examples; no database, credential, provider or model is provisioned by this guide.
