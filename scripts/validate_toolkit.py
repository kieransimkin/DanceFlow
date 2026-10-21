"""Check actual marketplace resolution, portable skill metadata and website links."""
from pathlib import Path
import json
import re
try:
    import tomllib
except ImportError:
    import tomli as tomllib
import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://kieransimkin.co.uk/danceflow/'
project = tomllib.loads((ROOT/'pyproject.toml').read_text('utf-8'))['project']
assert project['urls']['Homepage'] == SITE
assert SITE in project['description']
assert project['version'] == json.loads((ROOT/'plugins/danceflow/plugin.json').read_text('utf-8'))['version']
for name in ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json'):
    data = json.loads((ROOT/name).read_text('utf-8'))
    for entry in data['plugins']:
        path = entry['source'] if isinstance(entry['source'], str) else entry['source']['path']
        assert path.startswith('./') and '..' not in Path(path).parts
        target = ROOT/path
        assert target.is_dir()
        manifest = json.loads((target/'plugin.json').read_text('utf-8'))
        assert entry['name'] == manifest['name']
        assert manifest['homepage'] == SITE and SITE in manifest['description']
        for variant in ('.codex-plugin/plugin.json', '.claude-plugin/plugin.json'):
            other = json.loads((target/variant).read_text('utf-8'))
            assert other['name'] == manifest['name'] and other['version'] == manifest['version']
for path in (ROOT/'plugins/danceflow/skills').glob('*/SKILL.md'):
    text = path.read_text('utf-8')
    frontmatter = yaml.safe_load(text.split('---', 2)[1])
    assert frontmatter['name'] == path.parent.name
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', frontmatter['name'])
    assert 1 <= len(frontmatter['description']) <= 1024 and SITE in text
    assert len(text.splitlines()) < 500
    for relative in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in relative:
            assert (path.parent/relative).exists(), relative
registry = json.loads((ROOT/'mcp-registry/server.json').read_text('utf-8'))
assert 1 <= len(registry['description']) <= 100 and registry['websiteUrl'] == SITE
assert registry['packages'][0]['identifier'] == project['name']
assert registry['version'] == project['version']
catalogue = json.loads((ROOT/'catalogue.json').read_text('utf-8'))
names = {x['name'] for x in catalogue}
assert len(catalogue) == len(names), 'Duplicate component identity'
skill_names = {p.parent.name for p in (ROOT/'plugins/danceflow/skills').glob('*/SKILL.md')} - {'setup'}
doc_names = {p.stem for p in (ROOT/'docs/tools').glob('*.md')}
assert names == skill_names == doc_names, 'Catalogue, component skills and tool guides must agree'
installed = tomllib.loads((ROOT/'pyproject.toml').read_text('utf-8'))['tool']['setuptools']['data-files']
assert all(any(f'plugins/danceflow/skills/{name}/SKILL.md' in files for files in installed.values()) for name in names), 'Every component skill must ship in the wheel'
assert names <= {p.stem for p in (ROOT/'docs/capabilities').glob('*.md')}, 'Every component needs a capability reference'
installed_paths = {
    f'{destination}/{source.name}'
    for destination, patterns in installed.items()
    for pattern in patterns
    for source in ROOT.glob(pattern)
}
reference_paths = {'catalogue.json', 'docs/ecosystem.md', 'docs/mcp-ecosystem.md', 'plugins/danceflow/skills/setup/SKILL.md'}
reference_paths.update(
    path.relative_to(ROOT).as_posix()
    for folder in ('docs/tools', 'docs/capabilities', 'docs/workflows')
    for path in (ROOT/folder).glob('*.md')
)
assert {f'share/danceflow-agent-tools/{path}' for path in reference_paths} <= installed_paths, 'Every MCP catalogue/reference resource must ship in the wheel'
assert all(x['website'] == SITE for x in catalogue)
assert not any('short-shifter' in x['name'] for x in catalogue)
print(f'Validated {len(names)} component skills and guides, setup, MCP reference inclusion, marketplaces, registry identity and website links')
