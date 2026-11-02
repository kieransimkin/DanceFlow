"""Keep pytest fixtures off stale Windows temp paths and synced checkouts.

Windows: a unique %LOCALAPPDATA%/DanceFlow/pytest-tmp/direct-* run root.
Other platforms: the git-ignored .pytest-tmp/ under the checkout.
Explicit --basetemp or PYTEST_DEBUG_TEMPROOT always wins.
"""
from __future__ import annotations

import hashlib
import os
import shutil
import uuid
from collections.abc import Mapping
from pathlib import Path

import pytest


def default_temp_root(
    checkout: Path, *, environment: Mapping[str, str] | None = None, platform: str | None = None
) -> Path:
    """Choose a user-owned, non-synchronised Windows location for test data."""
    current_environment = os.environ if environment is None else environment
    platform = os.name if platform is None else platform
    checkout = Path(checkout).resolve()
    if platform == "nt":
        base = Path(current_environment.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local")
        return base / checkout.name / "pytest-tmp"
    return checkout / ".pytest-tmp"


def _new_run_root(checkout: Path) -> Path:
    """Return a fresh root so a killed run can never poison the next run."""
    checkout = checkout.resolve()
    key = hashlib.sha256(str(checkout).casefold().encode("utf-8")).hexdigest()[:12]
    return default_temp_root(checkout) / (
        f"direct-{key}-{os.getpid()}-{uuid.uuid4().hex}"
    )


def _probe_temp_root(root: Path) -> None:
    """Require create/read/atomic-rename/delete before collection starts."""
    root.mkdir(mode=0o700, parents=True, exist_ok=False)
    probe = root / "probe"
    renamed = root / "probe-renamed"
    try:
        probe.write_text("pytest-temp-probe", encoding="utf-8")
        if probe.read_text(encoding="utf-8") != "pytest-temp-probe":
            raise OSError(f"pytest temp probe readback failed: {root}")
        probe.rename(renamed)
    finally:
        renamed.unlink(missing_ok=True)
        probe.unlink(missing_ok=True)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config) -> None:
    """Redirect only pytest's default tmp_path/tmp_path_factory fixtures."""
    if config.getoption("basetemp") is not None:
        return
    if os.environ.get("PYTEST_DEBUG_TEMPROOT"):
        return
    root = _new_run_root(Path(config.rootpath))
    _probe_temp_root(root)
    os.environ["PYTEST_DEBUG_TEMPROOT"] = str(root)
    config._inicache["cache_dir"] = str(root / "cache")
    cleanup = getattr(config, "add_cleanup", None)
    if cleanup is not None:
        cleanup(lambda: shutil.rmtree(root, ignore_errors=True))
