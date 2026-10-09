import hashlib
import importlib.util
from pathlib import Path
import zipfile

import pytest

spec = importlib.util.spec_from_file_location('pages',Path(__file__).parents[1]/'scripts/prepare_pages.py')
pages = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pages)


def fixture(tmp_path, extra=None):
    archive=tmp_path/'danceflow-arcadians-demos-0.1.2.zip'
    with zipfile.ZipFile(archive,'w') as package:
        package.writestr('index.html','<title>Public example</title>')
        if extra:package.writestr(extra,'outside')
    manifest={'sourceCommit':'a'*40,'version':'0.1.2','assets':{archive.name:{'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}}}
    return archive,manifest


def test_pages_requires_exact_source_and_release_bytes(tmp_path):
    archive,manifest=fixture(tmp_path)
    pages.verify_archive(archive,manifest,'a'*40,'0.1.2')
    with pytest.raises(AssertionError,match='source/version'):
        pages.verify_archive(archive,manifest,'b'*40,'0.1.2')
    manifest['assets'][archive.name]['sha256']='0'*64
    with pytest.raises(AssertionError,match='checksum'):
        pages.verify_archive(archive,manifest,'a'*40,'0.1.2')


def test_even_matching_archives_cannot_write_outside_the_site(tmp_path):
    archive,manifest=fixture(tmp_path,'../outside.html')
    with pytest.raises(AssertionError,match='Unsafe archive path'):
        pages.verify_archive(archive,manifest,'a'*40,'0.1.2')
