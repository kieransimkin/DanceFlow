import importlib.util
import base64
import json
from pathlib import Path

import pytest
import yaml

spec=importlib.util.spec_from_file_location('recipes',Path(__file__).parents[1]/'scripts/submit_registry_recipes.py')
recipes=importlib.util.module_from_spec(spec);spec.loader.exec_module(recipes)


def test_baseline_change_preserves_other_ports_and_format():
    before='{"default": {\n    "aaa": {\n      "baseline": "1.0.0",\n      "port-version": 0\n    },\n    "zzz": {\n      "baseline": "2.0.0",\n      "port-version": 1\n    }\n  }}\n'
    inserted=recipes.render_baseline(before,'kieransimkin-dancerudiments','0.2.3')
    assert inserted.replace('    "kieransimkin-dancerudiments": {\n      "baseline": "0.2.3",\n      "port-version": 0\n    },\n','')==before
    updated=recipes.render_baseline(inserted,'kieransimkin-dancerudiments','0.2.4')
    old=json.loads(before)['default'];new=json.loads(updated)['default']
    assert all(new[key]==value for key,value in old.items())
    assert new['kieransimkin-dancerudiments']['baseline']=='0.2.4'


def test_version_history_is_preserved_and_changed_immutable_tree_is_rejected():
    one=recipes.render_versions(None,'a'*40,'0.2.3')
    assert recipes.render_versions(one,'a'*40,'0.2.3')==one
    two=recipes.render_versions(one,'b'*40,'0.2.4')
    assert json.loads(two)['versions'][1]==json.loads(one)['versions'][0]
    with pytest.raises(AssertionError,match='immutable'):
        recipes.render_versions(two,'c'*40,'0.2.3')


def test_conda_refresh_keeps_upstream_dependencies_and_maintainers():
    before = 'context:\n  version: "0.2.3"\nsource:\n  url: https://old.example/source\n  sha256: ' + 'a'*64 + '\nbuild:\n  number: 4\nrequirements:\n  run: [python, upstream-added-dependency]\nextra:\n  recipe-maintainers: [someone, kieransimkin]\n'
    after = recipes.update_conda_source(before, '0.2.4', {'url':'https://files.pythonhosted.org/new', 'sha256':'b'*64})
    assert after[after.index('requirements:'):] == before[before.index('requirements:'):]
    assert yaml.safe_load(after)['build']['number'] == 0
    with pytest.raises(AssertionError, match='format'):
        recipes.update_conda_source(before.replace('  version:', '  renamed:'), '0.2.4', {'url':'https://files.pythonhosted.org/new', 'sha256':'b'*64})


def test_conan_refresh_retains_accepted_versions_patches_and_config():
    configuration = 'versions:\n  "0.2.3": {folder: all}\nextra: preserve\n'
    data = 'sources:\n  "0.2.3": {url: old, sha256: aaa}\npatches:\n  "0.2.3": [{patch_file: fixes.patch}]\n'
    config, updated = recipes.add_conan_version(configuration, data, '0.2.4', {'url':'new', 'sha256':'bbb'})
    assert yaml.safe_load(config)['versions']['0.2.3'] == {'folder':'all'}
    assert yaml.safe_load(config)['extra'] == 'preserve'
    assert yaml.safe_load(updated)['patches'] == yaml.safe_load(data)['patches']
    assert yaml.safe_load(updated)['sources']['0.2.3'] == {'url':'old', 'sha256':'aaa'}
    with pytest.raises(AssertionError, match='source differs'):
        recipes.add_conan_version(config, updated, '0.2.4', {'url':'changed', 'sha256':'bbb'})


def test_pending_review_lookup_excludes_foreign_forks_and_other_components(monkeypatch):
    def review(number, ref, owner='kieransimkin', fork='kieransimkin/staged-recipes'):
        return {'number':number, 'state':'open', 'user':{'login':owner},
                'head':{'ref':ref, 'repo':{'full_name':fork, 'private':False}}}
    reviews = [review(10, 'danceflow/keywordmoves-0.4.6'),
               review(13, 'danceflow/keywordmoves-0.5.6'),
               review(14, 'danceflow/rastermoves-0.3.4'),
               review(15, 'danceflow/keywordmoves-0.5.7', fork='someone/staged-recipes'),
               review(16, 'danceflow/keywordmoves-0.5.7', owner='someone')]
    def fake_api(path):
        if path.startswith('search/issues?'):
            return {'total_count':len(reviews), 'items':[{'number':r['number']} for r in reviews]}
        return next(r for r in reviews if path.endswith('/'+str(r['number'])))
    monkeypatch.setattr(recipes, 'api', fake_api)
    assert [r['number'] for r in recipes.pending_conda_reviews('keywordmoves')] == [13, 10]


def test_pending_review_updates_source_without_discarding_maintainer_edits(monkeypatch):
    before = 'context:\n  version: "0.5.6"\nsource:\n  url: https://old.example/source\n  sha256: ' + 'a'*64 + '\nbuild:\n  number: 1\nrequirements:\n  run: [python, maintainer-added-dependency]\nextra:\n  recipe-maintainers: [reviewer, kieransimkin]\n'
    paths = {'recipes/keywordmoves/recipe.yaml':before, 'recipes/keywordmoves/build.sh':'reviewed build instructions\n'}
    def fake_api(path):
        filename = path.split('/contents/', 1)[1].split('?', 1)[0]
        return {'content':base64.b64encode(paths[filename].encode()).decode()}
    monkeypatch.setattr(recipes, 'api', fake_api)
    review = {'head':{'repo':{'full_name':'kieransimkin/staged-recipes'}, 'sha':'a'*40}}
    files = recipes.preserve_pending_conda_files('keywordmoves', dict.fromkeys(paths, 'new template'),
        review, '0.5.7', {'url':'https://files.pythonhosted.org/new', 'sha256':'b'*64})
    changed = files['recipes/keywordmoves/recipe.yaml']
    assert yaml.safe_load(changed)['context']['version'] == '0.5.7'
    assert changed[changed.index('requirements:'):] == before[before.index('requirements:'):]
    assert files['recipes/keywordmoves/build.sh'] == paths['recipes/keywordmoves/build.sh']


def test_overflowing_pending_review_query_holds_instead_of_creating_duplicates(monkeypatch):
    monkeypatch.setattr(recipes, 'api', lambda path:{'total_count':101, 'items':[]})
    with pytest.raises(ValueError, match='inspect'):
        recipes.pending_conda_reviews('keywordmoves')


def test_concurrent_review_edit_holds_before_any_mutation(monkeypatch):
    upstream = 'conda-forge/staged-recipes'
    fork = 'kieransimkin/staged-recipes'
    branch = 'danceflow/keywordmoves-0.5.6'
    def fake_api(path, method='GET', data=None):
        assert method == 'GET', 'A concurrent review must not be mutated'
        if path == f'repos/{upstream}':
            return {'default_branch':'main','private':False}
        if '/pulls?' in path:
            return [{'state':'open', 'title':'Add keywordmoves 0.5.6','number':13}]
        if path == f'repos/{fork}':
            return {'private':False, 'fork':True, 'parent':{'full_name':upstream}}
        if path == f'repos/{upstream}/git/ref/heads/main':
            return {'object':{'sha':'u'*40}}
        if '/git/commits/' in path:
            return {'tree':{'sha':'t'*40}}
        if path == f'repos/{fork}/git/ref/heads/{branch}':
            return {'object':{'sha':'b'*40}}
        raise AssertionError(path)
    monkeypatch.setattr(recipes, 'api', fake_api)
    with pytest.raises(ValueError, match='changed during staging'):
        recipes.open_recipe_pr(upstream, branch, {}, 'Add keywordmoves 0.5.7', 'body',
                               expected_review_head='a'*40)
