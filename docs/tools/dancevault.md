# DanceVault

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/DanceVault)

Stable encrypted, password-controlled WordPress file delivery.

Read README.md and server configuration examples. Stable 1.0.x releases include real Apache/nginx acceptance on the supported WordPress/PHP test matrix. A destination production host still needs its own acceptance. Use synthetic fixtures only until live WordPress access/nonce/HTTPS, signed-out ciphertext denial, expiry, revocation, response headers and private temporary storage pass acceptance. Preserve ciphertext/plaintext separation and existing rollback packages. Never claim cryptographic unit tests prove hosting integration or an external security audit.

## Development checks

```sh
php -l dancevault.php
php -l src/crypto.php
php tests/crypto.php
php tests/handlers.php
```

Submit contributions to https://github.com/kieransimkin/DanceVault/pulls. See the repository's current instructions before editing.

## Full feature workflow

[Read the released feature references](../capabilities/dancevault.md) and [check current releases before every new run](../workflows/release-preflight.md). Consider the whole ecosystem, use and improve applicable shared capabilities, and keep actual runtime/output evidence separate from availability.
