# DanceVault

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/DanceVault)

Experimental encrypted, password-controlled wordpress file delivery.

Read README.md and server configuration examples. This is experimental: Apache/nginx integration acceptance is pending. Use synthetic fixtures only until live WordPress access/nonce/HTTPS, signed-out ciphertext denial, expiry, revocation, response headers and private temporary storage pass acceptance. Preserve ciphertext/plaintext separation and existing rollback packages. Never claim cryptographic unit tests prove hosting integration or an external security audit.

## Development checks

```sh
php -l dancevault.php
php -l src/crypto.php
php tests/crypto.php
php tests/handlers.php
```

Submit contributions to https://github.com/kieransimkin/DanceVault/pulls. See the repository's current instructions before editing.
