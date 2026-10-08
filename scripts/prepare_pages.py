"""Deploy exact tested release assets from the existing allowed main workflow."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import tempfile
import zipfile

try:
    import tomllib
except ImportError:
    import tomli as tomllib

REPO = 'kieransimkin/DanceFlow'


def verify_archive(path: Path, manifest: dict, source: str, version: str):
    assert manifest['sourceCommit'] == source and manifest['version'] == version, 'Release source/version mismatch'
    asset = manifest['assets'][path.name]
    assert path.stat().st_size == asset['bytes'] <= 100_000_000, 'Unexpected demo archive size'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset['sha256'], 'Demo archive checksum mismatch'
    with zipfile.ZipFile(path) as package:
        assert 'index.html' in package.namelist(), 'Missing working playground entry point'
        assert sum(info.file_size for info in package.infolist()) <= 200_000_000, 'Unexpected expanded demo size'
        for info in package.infolist():
            name = PurePosixPath(info.filename)
            assert not name.is_absolute() and '..' not in name.parts and '\\' not in info.filename and ':' not in info.filename, 'Unsafe archive path'
            assert not stat.S_ISLNK(info.external_attr >> 16), 'Archive symlinks are not deployment files'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', required=True)
    parser.add_argument('--expected-source', default='')
    parser.add_argument('--output', type=Path, default=Path('site'))
    args = parser.parse_args()
    assert re.fullmatch(r'v\d+\.\d+\.\d+', args.tag), 'Use an immutable semantic release tag'
    source = subprocess.check_output(['git','rev-parse',f'refs/tags/{args.tag}^{{commit}}'],text=True).strip()
    if args.expected_source:
        assert source == args.expected_source, 'Workflow completion does not match the published tag'
    project = tomllib.loads(subprocess.check_output(['git','show',f'{args.tag}:pyproject.toml'],text=True))['project']
    version = project['version']
    assert project['name'] == 'danceflow-agent-tools' and args.tag == 'v' + version
    archive_name = f'danceflow-arcadians-demos-{version}.zip'
    with tempfile.TemporaryDirectory(prefix='danceflow-pages-') as temporary:
        folder = Path(temporary)
        subprocess.run(['gh','release','download',args.tag,'--repo',REPO,'--dir',str(folder),
                        '--pattern',archive_name,'--pattern','package-manifest.json','--pattern','SHA256SUMS.txt'],check=True)
        manifest = json.loads((folder/'package-manifest.json').read_text())
        checksum = next(line.split()[0] for line in (folder/'SHA256SUMS.txt').read_text().splitlines() if line.split()[-1] == archive_name)
        assert checksum == manifest['assets'][archive_name]['sha256']
        archive = folder/archive_name
        verify_archive(archive,manifest,source,version)
        target = args.output/'playground'
        target.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(archive) as package:
            package.extractall(target)
        landing = subprocess.check_output(['git','show',f'{args.tag}:hosting/github-pages/index.html'])
        (args.output/'index.html').write_bytes(landing)
        (target/'release.json').write_text(json.dumps({'version':version,'sourceCommit':source,'demoArchiveSHA256':checksum,'website':'https://kieransimkin.co.uk/danceflow/'},indent=2)+'\n')
    print(f'Prepared exact tested {args.tag} demo from {source}; existing main deployment policy retained.')


if __name__ == '__main__':
    main()
