# Registry recipes

[Website](https://kieransimkin.co.uk/danceflow/) Â· [Contribute](https://github.com/kieransimkin/DanceFlow/pulls)

These reviewed candidates extend distribution beyond the tools' existing npm, PyPI, GitHub Packages, containers and MCP routes. The release workflows publish tested packages from immutable tags. The hub's registry workflow also runs on its release tags and checks published component releases hourly; it submits versions only after the matching GitHub release and official PyPI source archive are available. Upstream review and acceptance remain separate from submission.

The conda-forge candidates cover KeywordMoves, RasterMoves, ThumbMoves and DanceRudiments. Rattler-build 0.76.1 renders were checked; full conda builds run in upstream CI. DanceRudiments' Python recipe removes its auxiliary static C++ library while retaining its Python extension, avoiding a duplicate native library in the Python package. After a feedstock is accepted, the updater proposes changes against that feedstock and preserves its dependencies and maintainer settings.

The DanceRudiments Conan recipe was built and consumed on Windows with Conan 2.33, MSVC 195, C++17 and Ninja using version 0.2.3. New documentation releases still require their own CI. ConanCenter's maintainers control acceptance. Updates preserve accepted versions and patches.

The vcpkg port uses the qualified name `kieransimkin-dancerudiments`, official source hashes, complete licence notices and a version database entry. The hourly job refreshes and retains the port candidate. The maintainer can opt into a draft submission through the manual workflow only after reviewing [upstream maturity and port test requirements](https://learn.microsoft.com/vcpkg/contributing/maintainer-guide). Upstream development began on 28 September 2026. The native source was tested through Conan, and the vcpkg port build and any required contributor agreement remain outstanding.

`REGISTRY_SUBMISSION_TOKEN` is an encrypted Actions secret with only GitHub's `public_repo` scope. It has no private-repository, workflow, organisation or account-management scopes and expires on 6 January 2027. Rotate it before that date using the same public-only scope. The workflow fails visibly if its credential is missing or expired, preserves candidates as an artifact, and can be retried with `workflow_dispatch`. Its submitter allows only the stated registry repositories and matching owner forks, with deterministic version branches to avoid duplicate submissions.

[EPK Social Metadata](https://wordpress.org/plugins/kieran-epk-social-metadata/) and [DanceMoves](https://wordpress.org/plugins/dancemoves/) publish tested releases through their approved directory workflows. Verify the directory's version and download separately from GitHub. DanceVault publishes its tested CipherParcel ZIP through GitHub and requires acceptance on the intended destination host.

Agents should inspect the recipes and upstream requirements, improve reusable gaps where possible, and submit tested improvements as PRs to this repository. Engine changes belong in each tool's canonical GitHub repository. Keep credentials, private audio and account data out of source and recipe archives.

Conda recipes preserve the upstream Python support range. KeywordMoves builds against its minimum supported Python and tests 3.10 and 3.13, with its declared upper bound retained. Native recipes leave Python version selection to conda-forge variants and skip unsupported versions. DanceRudiments explicitly selects the packaged Ninja generator on Unix and the conda-forge VS2022 generator on Windows, preserving its x64 platform selection; each build command fails independently before packaging.
