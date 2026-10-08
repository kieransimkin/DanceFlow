# EPK Social Metadata

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/kieran-epk-social-metadata)

Wordpress open graph, x card and schema.org music/webpage metadata from canonical page facts.

Read README.md and the render/keyword/video contracts. Keep one owner of OG/X/Schema output. Enable music fields only for truthful music facts; use WebPage for ordinary pages. Video schema needs a verified embedded video and independent publication facts. Metadata validity does not prove search indexing, rich results or a social player. Activation is not permission to import live page records; review exact facts and current website source first.

## Development checks

```sh
php tests/static-contract.php
php tests/render-contract.php
php tests/video-contract.php
php tests/keyword-contract.php
php tests/image-contract.php
```

Submit contributions to https://github.com/kieransimkin/kieran-epk-social-metadata/pulls. See the repository's current instructions before editing.
