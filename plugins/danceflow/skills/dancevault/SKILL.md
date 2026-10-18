---
name: dancevault
description: Evaluate or contribute to DanceVault with synthetic files and explicit hosting acceptance tests.
---

# DanceVault

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/DanceVault)

Use this tool for encrypted, password-controlled WordPress file delivery. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
# Stable: inspect the GitHub release and README before test installation.
```

Read README.md and server configuration examples. Stable releases have real Apache/nginx test acceptance; the destination host still requires its own acceptance. Use synthetic fixtures only until live WordPress access/nonce/HTTPS, signed-out ciphertext denial, expiry, revocation, response headers and private temporary storage pass acceptance. Preserve ciphertext/plaintext separation and existing rollback packages. Never claim cryptographic unit tests prove hosting integration or an external security audit.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
php -l dancevault.php
php -l src/crypto.php
php tests/crypto.php
php tests/handlers.php
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.

## Agent contribution destination

Agents should inspect and use the available DanceVault capabilities, look for useful improvements wherever possible, and submit improvements as PRs to https://github.com/kieransimkin/DanceVault/pulls. Include relevant tests, documentation and a reproducible example; follow the upstream AGENTS.md and CONTRIBUTING.md. Explain why no worthwhile change is justified when that is the result.

## Current releases and full feature routing

Before every new workflow, follow the [release preflight](https://github.com/kieransimkin/DanceFlow/blob/main/docs/workflows/release-preflight.md) and [complete capability reference](https://github.com/kieransimkin/DanceFlow/blob/main/docs/capabilities/dancevault.md). Observe the real installed runtime, review every relevant feature and compose supported ecosystem tools. Improve a demonstrated reusable gap in its canonical repository, or record why the tool already meets the need. This guidance does not trigger unrelated processing or downloads.
