"""Version discovery must work without importing the optional server stack."""
import os
from pathlib import Path
import subprocess
import sys

from danceflow_agents import __version__


def test_version_without_site_packages():
    env=dict(os.environ, PYTHONPATH=str(Path(__file__).resolve().parents[1]/'src'))
    result=subprocess.run([sys.executable,'-S','-m','danceflow_agents.server','--version'],
                          env=env,capture_output=True,text=True,timeout=20)
    assert result.returncode==0,result.stderr
    assert result.stdout.strip()==__version__
