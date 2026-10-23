# Potbot: capability and package reference

Audited 23 October 2026: **source preview; no stable release**, exact source [`e2f7b2e423ceb7360df76b18b076de09bf39936a`](https://github.com/kieransimkin/potbot/tree/e2f7b2e423ceb7360df76b18b076de09bf39936a). This is a dated source/documentation audit, not installed-runtime or end-to-end acceptance. [Check current releases before use](../workflows/release-preflight.md).

Potbot DanceFlow MCP consumption is planned; native PostgreSQL/Linux worker qualification is separate.

## Current README feature routes

- [Install and check](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#install-and-check)
- [Work with tasks](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#work-with-tasks)
- [First verified patch](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#first-verified-patch)
- [Model foundation](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#model-foundation)
- [Hosted models, API and job dashboard](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#hosted-models-api-and-job-dashboard)
- [Repository capture and controlled execution](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#repository-capture-and-controlled-execution)
- [Standard local vector embeddings](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#standard-local-vector-embeddings)
- [SYN semantic catalogs and exact inventories](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#syn-semantic-catalogs-and-exact-inventories)
- [Expanded hierarchy and native primitive placement](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#expanded-hierarchy-and-native-primitive-placement)
- [Semantic types and release identities](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#semantic-types-and-release-identities)
- [Package boundaries](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#package-boundaries)
- [Reuse before implementation](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md#reuse-before-implementation)

## Source documentation and examples

- [`README.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md)
- [`docs/agent-identity-and-ember-runtime.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/agent-identity-and-ember-runtime.md)
- [`docs/benchmarks/phase-7-methodology.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/benchmarks/phase-7-methodology.md)
- [`docs/cog-transformations.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/cog-transformations.md)
- [`docs/embeddings.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/embeddings.md)
- [`docs/hosted-jobs.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/hosted-jobs.md)
- [`docs/hosted-providers.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/hosted-providers.md)
- [`docs/http-api.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/http-api.md)
- [`docs/implementation/01-phase1-implementation.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/implementation/01-phase1-implementation.md)
- [`docs/implementation/02-mcp-transports.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/implementation/02-mcp-transports.md)
- [`docs/implementation/03-interactive-execution.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/implementation/03-interactive-execution.md)
- [`docs/implementation/04-http-api-adapters.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/implementation/04-http-api-adapters.md)
- [`docs/implementation/05-syn-execution-monitoring.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/implementation/05-syn-execution-monitoring.md)
- [`docs/implementation/06-t013-event-ledger.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/implementation/06-t013-event-ledger.md)
- [`docs/jobs.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/jobs.md)
- [`docs/linux-sandbox-ci.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/linux-sandbox-ci.md)
- [`docs/model-adapters.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/model-adapters.md)
- [`docs/named-embeddings.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/named-embeddings.md)
- [`docs/phase-1.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-1.md)
- [`docs/phase-2.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-2.md)
- [`docs/phase-3.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-3.md)
- [`docs/phase-4.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-4.md)
- [`docs/phase-5.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-5.md)
- [`docs/phase-6-controller-benchmark.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-6-controller-benchmark.md)
- [`docs/phase-6-increment-1.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-6-increment-1.md)
- [`docs/phase-7-increment-2.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-7-increment-2.md)
- [`docs/phase-7-increment-3.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-7-increment-3.md)
- [`docs/phase-7-increment-4.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-7-increment-4.md)
- [`docs/phase-7-increment-5.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-7-increment-5.md)
- [`docs/phase-7.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase-7.md)
- [`docs/phase7-closure-status.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/phase7-closure-status.md)
- [`docs/potbot-tool-mcp-implementation-bundle/potbot-universal-tool-mcp-implementation-plan.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/potbot-tool-mcp-implementation-bundle/potbot-universal-tool-mcp-implementation-plan.md)
- [`docs/reasoning-policy.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/reasoning-policy.md)
- [`docs/startup.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/startup.md)
- [`docs/syn-primitive-semantics-and-ember-contracts.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/syn-primitive-semantics-and-ember-contracts.md)
- [`docs/syn-semantic-integration.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/syn-semantic-integration.md)
- [`docs/type-hierarchy-and-syn-primitives.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/type-hierarchy-and-syn-primitives.md)
- [`docs/type-hierarchy-reference.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/type-hierarchy-reference.md)
- [`docs/workspace-sandboxing.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/docs/workspace-sandboxing.md)

## Package evidence

- [`README.md`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/README.md) — SHA-256 `3248f97ae3232839562f4611f0cfeb07983a7bb77ca509309ed9d38903fbfe7d`.
- [`pyproject.toml`](https://github.com/kieransimkin/potbot/blob/e2f7b2e423ceb7360df76b18b076de09bf39936a/pyproject.toml) — SHA-256 `deb2e9cf8afd38a2f435ba00aaf0f2ce16e9cb72f81edf590d2e84e76453ee24`.

Package files were read at the pinned source. Published distributions, installed identity, working host examples, rights and reviewed output require their own verification.
