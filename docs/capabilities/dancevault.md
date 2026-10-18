# DanceVault: complete capability reference

Inspected stable source: [v1.0.1](https://github.com/kieransimkin/DanceVault/releases/tag/v1.0.1), commit `879369fd866deb60daa450052dcb710b1df38708`. This is a dated baseline; [check current releases before every new workflow](../workflows/release-preflight.md).

## Choose and use a route

| Goal | Supported route and evidence |
|---|---|
| Accept the host | Stable releases include real Apache/nginx test acceptance, but a destination production host still needs its own documented security/storage acceptance. |
| Encrypt and deliver | Use the documented encrypted container, source/container hashes, password-controlled recipient route, expiry/revocation, range/stream and rate-limit contracts. |
| Verify access | Test authorised recipient behaviour and protected storage without exposing private data, passwords or plaintext fallback. Directory publication, plugin installation and private delivery are distinct actions. |

## Released reference coverage

Each entry links to the exact released explanation, options, example or limitation. These are documented capabilities, not a claim that every option was run on this computer. Review the relevant source before configuring it.

- [Agents and contributors](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/README.md#agents-and-contributors) — `README.md`.
- [Security model](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/README.md#security-model) — `README.md`.
- [Usage](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/README.md#usage) — `README.md`.
- [Acceptance and development](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/README.md#acceptance-and-development) — `README.md`.
- [CI and release publication](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/README.md#ci-and-release-publication) — `README.md`.
- [Hosting acceptance and operating requirements](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/hosting-acceptance.md#hosting-acceptance-and-operating-requirements) — `docs/hosting-acceptance.md`.
- [Reproduce](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/hosting-acceptance.md#reproduce) — `docs/hosting-acceptance.md`.
- [What the tests establish](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/hosting-acceptance.md#what-the-tests-establish) — `docs/hosting-acceptance.md`.
- [Before each production installation](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/hosting-acceptance.md#before-each-production-installation) — `docs/hosting-acceptance.md`.
- [Potential problems](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/hosting-acceptance.md#potential-problems) — `docs/hosting-acceptance.md`.
- [WordPress.org directory review](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/wordpress-org.md#wordpressorg-directory-review) — `docs/wordpress-org.md`.
- [Reviewable scanner context](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/wordpress-org.md#reviewable-scanner-context) — `docs/wordpress-org.md`.
- [Publication after approval](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/wordpress-org.md#publication-after-approval) — `docs/wordpress-org.md`.
- [Potential problems](https://github.com/kieransimkin/DanceVault/blob/v1.0.1/docs/wordpress-org.md#potential-problems) — `docs/wordpress-org.md`.

## Examples and media

Use the runnable examples and actual screenshots/videos linked from the released references. Keep their documented version/context and distinguish synthetic fixtures, model hypotheses and real captured output. Do not represent a guide link as proof that a model, GPU, physical phone or production host was tested. New decorative generated imagery adds no feature evidence to this reference index.
