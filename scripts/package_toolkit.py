"""Build deterministic portable plugin archives and checksum manifests."""
from pathlib import Path
import hashlib
import json
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
version = json.loads((ROOT / 'plugins/danceflow/plugin.json').read_text('utf-8'))['version']
dist = ROOT / 'dist'
dist.mkdir(exist_ok=True)
files = sorted([p for directory in ('plugins', 'docs', 'mcp-registry', '.agents', '.claude-plugin')
                for p in (ROOT / directory).rglob('*') if p.is_file() and 'playground' not in p.relative_to(ROOT).parts] +
               [ROOT / name for name in ('README.md', 'CONTRIBUTING.md', 'AGENTS.md', 'LICENSE', 'catalogue.json')])
archive = dist / f'danceflow-agent-toolkit-{version}.zip'
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
    for path in files:
        info = zipfile.ZipInfo('DanceFlow/' + path.relative_to(ROOT).as_posix(), (2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        out.writestr(info, path.read_bytes())
demo = ROOT / 'docs/playground'
if (demo / 'index.html').is_file():
    with zipfile.ZipFile(dist / f'danceflow-arcadians-demos-{version}.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for path in sorted(demo.rglob('*')):
            if path.is_file():
                out.write(path, path.relative_to(demo).as_posix())
manifest = {}
for path in sorted(dist.iterdir()):
    if path.is_file() and path.suffix in ('.zip', '.whl', '.gz'):
        manifest[path.name] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
(dist/'SHA256SUMS.txt').write_text(''.join(f'{v["sha256"]}  {k}\n' for k,v in manifest.items()), encoding='utf-8')
source_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
assert len(source_commit) == 40 and all(c in '0123456789abcdef' for c in source_commit)
(dist/'package-manifest.json').write_text(json.dumps({'version': version, 'sourceCommit': source_commit, 'website': 'https://kieransimkin.co.uk/danceflow/', 'assets':manifest}, indent=2)+'\n', encoding='utf-8')
print(json.dumps(manifest, indent=2))
