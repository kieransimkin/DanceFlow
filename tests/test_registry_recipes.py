import importlib.util
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
