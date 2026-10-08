"""Prepare hash-pinned public Arcadians examples with released tool engines.

Waveform generation uses StemLab 1.3.3, numpy, soundfile and server dependencies.
No source separation or neural models run.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
COMMIT = 'a44045dd267b539f5d25445e2153f4cf2d8f43a8'
ASSETS = {
    'Arcadians - 320kbps.mp3': (11708403, '5a3d17d8b5b27d62a6bb9fa1f654c403db0341da826d650cc282dfa5758ee6de'),
    'cover.jpg': (745386, '8bfeff939c1ffcba7529614263e05d4f1bb59a46e6c13501dbf12349edb047ee'),
    'reference.json': (8601, 'c09cf93d743d78519566b322f924fa40995aa2b108cff1d727bb829b896f0f6a'),
    'canonical.json': (6312, '24b5d1f4d2b6d029df0fa6c6e1e437dbe22a64d416e2a8ff50a1be8c4313628f'),
    'lyrics.txt': (1379, '3211562728d8259f537dba5d29702ba76f00bfeb95258340e066cc5b68e433e0'),
    'canonical-lyric-timing.lrc': (2542, '92b46abc4caf1caa8eddf7c306a9e767f8d0bbefed3b39d38e4b4f96981e9de7'),
}


def prepare(stemlab_root: Path | None = None):
    from stemlab.webui import _waveform_envelope
    from keywordmoves.models import ExecutionContext, PluginRequest
    from keywordmoves.registry import LLMRegistry, PluginRegistry
    public = ROOT / 'demos/public'
    media = public / 'media'
    media.mkdir(parents=True, exist_ok=True)
    records = []
    for name, (size, digest) in ASSETS.items():
        source = 'examples/arcadians/' + name
        url = f'https://raw.githubusercontent.com/kieransimkin/stemlab/{COMMIT}/' + quote(source)
        path = media / ('arcadians.mp3' if name.endswith('.mp3') else name)
        if path.exists():
            data = path.read_bytes()
        elif stemlab_root:
            data = subprocess.check_output(['git', '-C', str(stemlab_root), 'show', f'{COMMIT}:{source}'])
        else:
            with urlopen(Request(url, headers={'User-Agent': 'DanceFlow-example/0.1.0'}), timeout=60) as response:
                data = response.read(size + 1)
        assert len(data) == size and hashlib.sha256(data).hexdigest() == digest, f'Asset identity mismatch: {name}'
        path.write_bytes(data)
        records.append({'file': 'media/' + path.name, 'bytes': size, 'sha256': digest, 'source': url})
    reference = json.loads((media / 'reference.json').read_text('utf-8'))
    waveform = _waveform_envelope(media / 'arcadians.mp3', points=2048)
    fixture = {'title': reference['title'], 'artist': reference['artist'], 'bpm': reference['bpm'],
               'epk': reference['epk_url'], 'duration': waveform['duration_seconds'], 'waveform': waveform,
               'sections': reference['sections'], 'lyrics': reference['lyric_timing'],
               'timing_source': 'Artist-authored reference; not model-inferred beat/downbeat evidence',
               'waveform_source': 'StemLab 1.3.3 waveform envelope of the decoded public MP3'}
    (public / 'arcadians.json').write_text(json.dumps(fixture, ensure_ascii=False) + '\n', encoding='utf-8')
    relative = Path('demos/public/media/lyrics.txt')
    report = PluginRegistry().get('text-library').run(
        PluginRequest(operation='extract-literal', inputs=(relative,), options={'limit': 80}),
        ExecutionContext(llms=LLMRegistry())).to_dict()
    # KeywordMoves records absolute sources. Rebase only that metadata for the
    # public fixture; keep the original result outside the distribution tree.
    (ROOT.parent / 'keywordmoves-original-result.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    report['metadata']['sources'] = ['media/lyrics.txt']
    report['metadata']['source_path_rebase'] = 'Source path made relative for publication; keyword and evidence rows unchanged.'
    (public / 'keywordmoves-example.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    # Vite emits the package's pinned WASM through its asset URL; do not duplicate it.
    licences = public / 'licences'
    licences.mkdir(exist_ok=True)
    for package, filename in [('@kieransimkin/dancemoves', 'DanceMoves.txt'), ('@kieransimkin/dance-rudiments', 'DanceRudiments.txt'), ('react-timeline-sequence', 'ReactTimelineSequence.txt')]:
        shutil.copyfile(ROOT / 'demos/node_modules' / package / 'LICENSE', licences / filename)
    rudiments = ROOT / 'demos/node_modules/@kieransimkin/dance-rudiments'
    shutil.copyfile(rudiments / 'collections/initial/THIRD_PARTY_NOTICES.md', licences / 'DanceRudiments-third-party-notices.md')
    shutil.copyfile(rudiments / 'python/dancerudiments_authoring/packs/THIRD_PARTY_NOTICES.md', licences / 'DanceRudiments-authoring-notices.md')
    # The npm notice references a full BSD notice embedded in generated patterns.
    # Serve the separate source notice too, pinned to the same released version.
    bsd_url = 'https://raw.githubusercontent.com/kieransimkin/DanceRudiments/v0.2.3/collections/initial/sources/d3-ease/LICENSE'
    with urlopen(Request(bsd_url, headers={'User-Agent': 'DanceFlow-example/0.1.0'}), timeout=30) as response:
        bsd_notice = response.read(16384)
    assert b'Copyright' in bsd_notice and b'REDISTRIBUTION' in bsd_notice.upper()
    (licences / 'DanceRudiments-d3-ease-BSD.txt').write_bytes(bsd_notice)
    (public / 'provenance.json').write_text(json.dumps({'website': 'https://kieransimkin.co.uk/danceflow/',
        'source_commit': COMMIT, 'assets': records,
        'music_and_artwork': 'Arcadians by Kieran Simkin, supplied for this demonstration. Music and artwork rights are separate from software licences.',
        'section_loops': 'Artist reference audition ranges; seamless loop acceptance has not been established.'}, indent=2) + '\n', encoding='utf-8')
    print('Verified Arcadians assets; generated real StemLab waveform and KeywordMoves evidence.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stemlab-root', type=Path)
    prepare(parser.parse_args().stemlab_root)
