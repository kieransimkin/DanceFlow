"""Version discovery must work without importing the optional server stack."""
import os
from pathlib import Path
import subprocess
import sys
try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 uses the declared development dependency.
    import tomli as tomllib

from danceflow_agents import __version__


def test_version_without_site_packages():
    env=dict(os.environ, PYTHONPATH=str(Path(__file__).resolve().parents[1]/'src'))
    result=subprocess.run([sys.executable,'-S','-m','danceflow_agents.server','--version'],
                          env=env,capture_output=True,text=True,timeout=20)
    assert result.returncode==0,result.stderr
    assert result.stdout.strip()==__version__


def test_runtime_version_matches_distribution_metadata():
    project = tomllib.loads((Path(__file__).resolve().parents[1] / "pyproject.toml").read_text(encoding="utf-8"))
    assert __version__ == project["project"]["version"]


def test_agent_discovery_copy_matches_current_identity():
    root = Path(__file__).resolve().parents[1]
    project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    version = project["project"]["version"]
    overview = (root / "docs/mcp-ecosystem.md").read_text(encoding="utf-8")
    toolkit = (root / "docs/capabilities/toolkit.md").read_text(encoding="utf-8")
    server = (root / "src/danceflow_agents/server.py").read_text(encoding="utf-8")

    assert f"Version {version} packages" in overview
    assert f"DanceFlow toolkit {version}: current integration" in toolkit
    assert "Discover all 17 components" in server
