import json
from types import SimpleNamespace

import danceflow_agents.releases as release_module
from danceflow_agents.releases import check_releases, compare_version, latest_runtime, official_releases, stable_version


def release(tag, **kwargs):
    return dict(tag_name=tag,html_url='https://github.com/kieransimkin/PixelCue/releases/tag/'+tag,assets=[],**kwargs)


def test_runtime_selection_ignores_documentation_and_prereleases():
    rows=[release('readme-policy-v99.0.0'),release('v0.9.1'),release('v1.0.0',prerelease=True),
          release('v1.1.0',draft=True),release('thumbmoves-v0.1.2'),release('v0.9.0')]
    assert latest_runtime(rows)['tag_name']=='v0.9.1'
    assert latest_runtime(rows,'thumbmoves-v')['tag_name']=='thumbmoves-v0.1.2'
    assert latest_runtime([release('docs-v1.0.0')]) is None
    assert stable_version('v01.2.3') is None


def test_installed_identity_does_not_imply_registry_or_runtime_acceptance():
    assert compare_version(None,'1.2.3')=='not_observed'
    assert compare_version('1.2.2','1.2.3')=='update_available'
    assert compare_version('1.2.3','1.2.3')=='current'
    assert compare_version('1.2.4','1.2.3')=='ahead_of_release'
    assert compare_version('1.2.3+development','1.2.3')=='unverified_identity'


def test_shared_repository_fetched_once_and_prefixes_stay_distinct():
    calls=[]
    def fetch(repo):
        calls.append(repo)
        return [release('v0.9.1'),release('thumbmoves-v0.1.2')]
    report=check_releases({'PixelCue':'0.9.1','ThumbMoves':'0.1.0'},fetch)
    rows={r['component']:r for r in report['components']}
    assert calls.count('PixelCue')==1
    assert rows['PixelCue']['status']=='current'
    assert rows['ThumbMoves']['status']=='update_available'
    assert rows['ThumbMoves']['released']=='0.1.2'
    assert rows['MediaSlide']['repository']=='https://github.com/kieransimkin/react-mediaslide'


def test_network_failure_retains_unavailable_without_cached_success():
    def fail(repo):
        raise OSError('private proxy diagnostic that must not be copied')
    report=check_releases({'StemLab':'1.8.0'},fail)
    assert all(row['status']=='unavailable' for row in report['components'])
    assert all('private' not in row['reason'] for row in report['components'])


def test_preview_without_stable_release_is_distinct_from_failed_query():
    def fetch(repo):
        if repo in {'potbot', 'DanceFlow.Unity'}:
            return [release('v0.5.0-preview.1', prerelease=True)]
        return [release('v1.0.0'), release('thumbmoves-v0.1.2')]
    rows = {row['component']: row for row in check_releases(fetch=fetch)['components']}
    for name in ('Potbot', 'DanceFlow for Unity'):
        assert rows[name]['status'] == 'no_stable_release'
        assert rows[name]['released'] is None
        assert 'Official query succeeded' in rows[name]['reason']
    assert rows['MediaSlide']['status'] != 'no_stable_release'


def test_gh_release_json_is_decoded_as_utf8(monkeypatch):
    seen = {}
    payload = [[release('v3.4.0', name='Café — motion')]]

    monkeypatch.setattr(release_module.shutil, 'which', lambda command: 'gh.exe')

    def run(args, **kwargs):
        seen.update(kwargs)
        return SimpleNamespace(returncode=0, stdout=json.dumps(payload, ensure_ascii=False))

    monkeypatch.setattr(release_module.subprocess, 'run', run)
    rows = official_releases('DanceMoves')

    assert rows[0]['name'] == 'Café — motion'
    assert seen['encoding'] == 'utf-8'
    assert seen['errors'] == 'strict'
