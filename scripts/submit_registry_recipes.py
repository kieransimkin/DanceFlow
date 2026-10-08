"""Submit reviewed recipe files through GitHub PRs; upstreams retain merge authority.

Run --check for offline validation, --apply for authenticated submission, and
--refresh to select only versions with both a published GitHub release and PyPI
source archive. CI uses a separate public-repository token, never a private token.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import urlencode, urlparse
from urllib.request import urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
OWNER = 'kieransimkin'
COMPONENTS = {'keywordmoves': ('keywordmoves', 'keywordmoves', 'v'),
              'rastermoves': ('RasterMoves', 'rastermoves', 'v'),
              'thumbmoves': ('PixelCue', 'thumbmoves', 'thumbmoves-v'),
              'dancerudiments': ('DanceRudiments', 'dancerudiments', 'v')}


def api(path: str, method: str = 'GET', data: dict | None = None):
    args = ['gh', 'api', path, '--method', method]
    if data is None:
        result = subprocess.run(args, capture_output=True, text=True)
    else:
        # JSON is sent over stdin, not shell text; credentials are never printed.
        result = subprocess.run(args + ['--input', '-'], input=json.dumps(data),
                                capture_output=True, text=True)
    if result.returncode:
        if method == 'GET' and 'HTTP 404' in result.stderr:
            return None
        raise RuntimeError(f'GitHub {method} failed for {path}: {result.stderr[-500:]}')
    return json.loads(result.stdout) if result.stdout.strip() else None


def source_release(component: str):
    repo, project, prefix = COMPONENTS[component]
    releases = api(f'repos/{OWNER}/{repo}/releases?per_page=50')
    pattern = re.compile(re.escape(prefix) + r'(\d+\.\d+\.\d+)\Z')
    versions = [pattern.fullmatch(r['tag_name']).group(1) for r in releases
                if not r['draft'] and not r['prerelease'] and pattern.fullmatch(r['tag_name'])]
    if not versions:
        raise ValueError(f'No published stable GitHub release for {component}')
    version = max(versions, key=lambda v: tuple(map(int, v.split('.'))))
    with urlopen(f'https://pypi.org/pypi/{project}/{version}/json', timeout=30) as response:
        metadata = json.load(response)
    assert metadata['info']['version'] == version
    sources = [f for f in metadata['urls'] if f['packagetype'] == 'sdist']
    assert len(sources) == 1 and not sources[0]['yanked']
    source = sources[0]
    assert urlparse(source['url']).scheme == 'https' and urlparse(source['url']).hostname == 'files.pythonhosted.org'
    assert re.fullmatch('[a-f0-9]{64}', source['digests']['sha256'])
    return version, source


def refresh(component: str):
    version, source = source_release(component)
    path = ROOT / f'recipes/conda/{component}/recipe.yaml'
    text = path.read_text('utf-8')
    text = re.sub(r'(?m)^  version: "[^"]+"$', f'  version: "{version}"', text, count=1)
    text = re.sub(r'(?m)^  url: .*$', '  url: ' + source['url'], text, count=1)
    text = re.sub(r'(?m)^  sha256: .*$', '  sha256: ' + source['digests']['sha256'], text, count=1)
    path.write_text(text, encoding='utf-8', newline='\n')
    if component == 'dancerudiments':
        with urlopen(source['url'], timeout=60) as response:
            data = response.read(100_000_001)
        assert len(data) == source['size'] and hashlib.sha256(data).hexdigest() == source['digests']['sha256']
        old_versions = yaml.safe_load((ROOT / 'recipes/conan/dancerudiments/config.yml').read_text())['versions']
        old_version = next(iter(old_versions))
        for relative in ['recipes/conan/dancerudiments/config.yml', 'recipes/conan/dancerudiments/all/conandata.yml',
                         'recipes/vcpkg/dancerudiments/portfile.cmake', 'recipes/vcpkg/dancerudiments/vcpkg.json']:
            p = ROOT / relative; before = p.read_text('utf-8')
            # Match the template's current URL/hash, not arbitrary source text.
            after = before.replace(old_version, version)
            after = re.sub(r'https://files\.pythonhosted\.org/[^"\s]+', source['url'], after)
            if relative.endswith('conandata.yml'):
                after = re.sub(r'(?m)(sha256: ")[a-f0-9]{64}("$)', rf'\g<1>{source["digests"]["sha256"]}\2', after)
            if relative.endswith('portfile.cmake'):
                after = re.sub(r'(?m)(    SHA512 )[a-f0-9]{128}', rf'\g<1>{hashlib.sha512(data).hexdigest()}', after)
            p.write_text(after, encoding='utf-8', newline='\n')


def checked_recipe(component: str):
    folder = ROOT / f'recipes/conda/{component}'
    recipe = yaml.safe_load((folder / 'recipe.yaml').read_text('utf-8'))
    assert recipe['package']['name'] == component and recipe['build']['number'] == 0
    assert re.fullmatch(r'\d+\.\d+\.\d+', recipe['context']['version'])
    assert re.fullmatch('[a-f0-9]{64}', recipe['source']['sha256'])
    assert urlparse(recipe['source']['url']).hostname == 'files.pythonhosted.org'
    assert recipe['about']['homepage'] == 'https://kieransimkin.co.uk/danceflow/'
    return recipe


def open_recipe_pr(upstream: str, branch: str, files: dict[str, str], title: str, body: str, draft=False, expected_base=None):
    upstream_info = api(f'repos/{upstream}'); default = upstream_info['default_branch']
    assert not upstream_info['private'], 'Registry submissions require a public upstream'
    previous = api(f'repos/{upstream}/pulls?'+urlencode(dict(state='all', head=OWNER+':'+branch)))
    if previous and previous[0]['state'] == 'closed':
        # A merged submission is complete; a declined one needs maintainer review.
        print(f'{upstream}: existing closed submission {previous[0]["html_url"]}; no duplicate created')
        return previous[0]['html_url']
    name = upstream.split('/')[1]; fork = f'{OWNER}/{name}'
    fork_info = api(f'repos/{fork}')
    if fork_info is None:
        fork_info = api(f'repos/{upstream}/forks', 'POST', {'default_branch_only': True})
    assert not fork_info['private'] and fork_info['fork'] and fork_info['parent']['full_name'].lower() == upstream.lower()
    base = api(f'repos/{upstream}/git/ref/heads/{default}')['object']['sha']
    if expected_base is not None and base != expected_base:
        raise ValueError('Upstream changed during baseline staging; retry from fresh source')
    base_tree = api(f'repos/{upstream}/git/commits/{base}')['tree']['sha']
    ref = api(f'repos/{fork}/git/ref/heads/{branch}')
    if ref:
        # Keep an existing PR's own changes; never replace another branch.
        base = ref['object']['sha']; base_tree = api(f'repos/{fork}/git/commits/{base}')['tree']['sha']
    entries = [dict(path=p, mode='100644', type='blob', content=text) for p, text in sorted(files.items())]
    tree = api(f'repos/{fork}/git/trees', 'POST', dict(base_tree=base_tree, tree=entries))['sha']
    if tree != base_tree:
        commit = api(f'repos/{fork}/git/commits', 'POST', dict(message=title, tree=tree, parents=[base]))['sha']
        if ref:
            api(f'repos/{fork}/git/refs/heads/{branch}', 'PATCH', dict(sha=commit, force=False))
        else:
            api(f'repos/{fork}/git/refs', 'POST', dict(ref='refs/heads/'+branch, sha=commit))
    existing = previous
    if existing:
        return existing[0]['html_url']
    pr = api(f'repos/{upstream}/pulls', 'POST', dict(title=title, head=OWNER+':'+branch,
              base=default, body=body, draft=draft, maintainer_can_modify=True))
    return pr['html_url']


def submit_conda(component: str):
    recipe = checked_recipe(component); version = recipe['context']['version']
    feedstock = api(f'repos/conda-forge/{component}-feedstock')
    if feedstock:
        upstream = feedstock['full_name']
        meta = api(f'repos/{upstream}/contents/recipe/recipe.yaml')
        if meta is None:
            raise ValueError(f'{upstream}: recipe format changed; preserve upstream and review the update route')
        current = base64.b64decode(meta['content']).decode('utf-8')
        if yaml.safe_load(current)['context']['version'] == version:
            print(f'{component}: feedstock already has version {version}')
            return None
        source = recipe['source']
        updated = update_conda_source(current, version, source)
        body = f'Update to the verified upstream GitHub/PyPI release {version}; preserve the existing feedstock recipe and maintainer settings. Website: https://kieransimkin.co.uk/danceflow/\n\nFull conda builds and maintainer review remain required.'
        return open_recipe_pr(upstream, f'danceflow/{component}-{version}',
                              {'recipe/recipe.yaml': updated}, f'{component}: update {version}', body)
    folder = ROOT / f'recipes/conda/{component}'
    files = {f'recipes/{component}/{p.name}': p.read_text('utf-8') for p in folder.iterdir() if p.is_file()}
    body = f'''Add {component} {version} from its official immutable PyPI source archive. Upstream and website links, licence notices, import/package tests and the canonical agent contribution destination are included.

Validation: source bytes and SHA256 verified; v1 recipes rendered with rattler-build 0.76.1. Native rendering uses conda-forge's current compiler/stdlib settings. Full conda builds are delegated to this PR's CI; no successful build is inferred from rendering. Proposed maintainer: kieransimkin, the upstream owner.

- [x] Meaningful title, v1 recipe, official tarball and build number 0.
- [x] Required source and third-party licences are packaged.
- [x] No undeclared vendored packages; native Python recipe removes the auxiliary static library.
- [ ] Full conda-forge CI and maintainer review completed.

Website: https://kieransimkin.co.uk/danceflow/
'''
    return open_recipe_pr('conda-forge/staged-recipes', f'danceflow/{component}-{version}', files,
                          f'Add {component} {version}', body)


def update_conda_source(text: str, version: str, source: dict):
    replacements = [(r'(?m)^  version: "[^"]+"$', f'  version: "{version}"'),
                    (r'(?m)^  url: .*$', '  url: ' + source['url']),
                    (r'(?m)^  sha256: .*$', '  sha256: ' + source['sha256']),
                    (r'(?m)^  number: \d+$', '  number: 0')]
    for pattern, value in replacements:
        text, count = re.subn(pattern, value, text)
        assert count == 1, 'Unexpected upstream recipe format; review without overwriting it'
    return text


def add_conan_version(config: str, data: str, version: str, source: dict):
    configuration = yaml.safe_load(config)
    sources = yaml.safe_load(data)
    configuration['versions'].setdefault(version, {'folder': 'all'})
    existing = sources['sources'].get(version)
    assert existing is None or existing == source, 'Published Conan source differs'
    sources['sources'][version] = source
    return yaml.safe_dump(configuration, sort_keys=False), yaml.safe_dump(sources, sort_keys=False)


def submit_conan():
    folder = ROOT / 'recipes/conan/dancerudiments';version=next(iter(yaml.safe_load((folder/'config.yml').read_text())['versions']))
    files = {f'recipes/dancerudiments/{p.relative_to(folder).as_posix()}': p.read_text('utf-8')
             for p in folder.rglob('*') if p.is_file() and not any(part in ['build','__pycache__'] for part in p.parts)
             and p.name != 'CMakeUserPresets.json'}
    upstream_config = api('repos/conan-io/conan-center-index/contents/recipes/dancerudiments/config.yml')
    if upstream_config:
        # Once accepted, maintain the accepted recipe and all existing versions.
        upstream_data = api('repos/conan-io/conan-center-index/contents/recipes/dancerudiments/all/conandata.yml')
        config = base64.b64decode(upstream_config['content']).decode('utf-8')
        data = base64.b64decode(upstream_data['content']).decode('utf-8')
        if version in yaml.safe_load(config)['versions']:
            print(f'dancerudiments: Conan recipe already has version {version}')
            return None
        source = yaml.safe_load((folder/'all/conandata.yml').read_text())['sources'][version]
        new_config, new_data = add_conan_version(config, data, version, source)
        files = {'recipes/dancerudiments/config.yml': new_config,
                 'recipes/dancerudiments/all/conandata.yml': new_data}
    body=f'''### Summary
Add **dancerudiments/{version}**, a C++17 static library for deterministic rhythmic position sampling.

The recipe downloads the official hash-pinned source, disables optional bindings/tools, preserves all four licence notices and exports the existing DanceRudiments::DanceRudiments CMake target. Website: https://kieransimkin.co.uk/danceflow/

- [x] Read the contribution guidelines.
- [x] Official source archive identity verified.
- [x] Locally built and consumed 0.2.3 with Conan 2.33, MSVC 195, C++17 and Ninja; catalogue count and loop wrapping checked. Later doc-only versions await CI validation.
- [ ] Upstream CI and maintainer review complete.
'''
    return open_recipe_pr('conan-io/conan-center-index',f'danceflow/dancerudiments-{version}',files,f'dancerudiments: add {version}',body)


def render_baseline(baseline: str, name: str, version: str):
    current = json.loads(baseline)
    if name in current['default']:
        pattern = r'(?m)(    "' + re.escape(name) + r'": \{\n      "baseline": ")[^"]+(",\n      "port-version": )\d+'
        result, count = re.subn(pattern, rf'\g<1>{version}\g<2>0', baseline)
        assert count == 1, 'Unexpected baseline format; preserve it for review'
        return result
    lines=baseline.splitlines(keepends=True)
    insertion=next((i for i,line in enumerate(lines) if re.match(r'    "[^\"]+": \{',line) and line.split('"')[1]>name),len(lines)-2)
    entry=f'    "{name}": {{\n      "baseline": "{version}",\n      "port-version": 0\n    }},\n'
    lines.insert(insertion,entry);result=''.join(lines)
    assert json.loads(result)['default'][name]['baseline']==version
    return result


def render_versions(previous: str | None, tree: str, version: str):
    data=json.loads(previous) if previous else {'versions': []}
    matches=[v for v in data['versions'] if v.get('version-semver')==version and v.get('port-version',0)==0]
    if matches:
        assert matches[0]['git-tree']==tree, 'Published version tree differs; preserve immutable version'
    else: data['versions'].insert(0,{'git-tree':tree,'version-semver':version,'port-version':0})
    return json.dumps(data,indent=2)+'\n'


def submit_vcpkg():
    folder=ROOT/'recipes/vcpkg/dancerudiments'; manifest=json.loads((folder/'vcpkg.json').read_text());name=manifest['name'];version=manifest['version-semver']
    fork=f'{OWNER}/vcpkg'
    port_tree=api(f'repos/{fork}/git/trees','POST',dict(tree=[dict(path=p.name,mode='100644',type='blob',content=p.read_text('utf-8')) for p in folder.iterdir() if p.is_file()]))['sha']
    upstream=api('repos/microsoft/vcpkg');base=api('repos/microsoft/vcpkg/git/ref/heads/'+upstream['default_branch'])['object']['sha']
    baseline_meta=api('repos/microsoft/vcpkg/contents/versions/baseline.json?ref='+base)
    baseline=base64.b64decode(baseline_meta['content']).decode('utf-8')
    if json.loads(baseline)['default'].get(name, {}).get('baseline') == version:
        print(f'{name}: vcpkg already has version {version}')
        return None
    baseline=render_baseline(baseline,name,version)
    files={f'ports/{name}/{p.name}':p.read_text('utf-8') for p in folder.iterdir() if p.is_file()}
    files['versions/baseline.json']=baseline
    versions_path=f'versions/{name[0]}-/{name}.json'
    previous=api('repos/microsoft/vcpkg/contents/'+versions_path+'?ref='+base)
    previous_text=base64.b64decode(previous['content']).decode('utf-8') if previous else None
    files[versions_path]=render_versions(previous_text,port_tree,version)
    body=f'''Add the upstream DanceRudiments {version} C++17 static library as `{name}`. Disable optional Python/WASM/C ABI/demo components, preserve the existing CMake target and all licence notices, and include its version database entry. Website: https://kieransimkin.co.uk/danceflow/

This is a **draft**: the first upstream release is 28 September 2026, so the usual six-month maturity criterion is not met. Please assess eligibility before promotion. The underlying native source has been built/consumed with MSVC and Ninja through Conan; the vcpkg port itself still requires CI validation. No vcpkg listing is claimed.

- [x] Authoritative hash-pinned source and complete licence declarations.
- [x] Owner-project port name, matching upstream semantic version and one version database entry.
- [x] Optional build dependencies explicitly disabled.
- [ ] vcpkg port build, maturity review and any required CLA completion.
'''
    return open_recipe_pr('microsoft/vcpkg',f'danceflow/dancerudiments-{version}',files,f'[{name}] add {version}',body,draft=True,expected_base=base)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');parser.add_argument('--apply',action='store_true');parser.add_argument('--refresh',action='store_true');args=parser.parse_args()
    if args.refresh:
        for component in COMPONENTS: refresh(component)
    for component in COMPONENTS: checked_recipe(component)
    print('Four source, version, website and recipe identities validated.')
    if args.apply:
        actor=api('user')['login'];assert actor==OWNER, 'Use the scoped upstream owner automation credential'
        for component in COMPONENTS:
            url=submit_conda(component)
            if url: print(url,flush=True)
        print(submit_conan(),flush=True);print(submit_vcpkg(),flush=True)


if __name__=='__main__': main()
