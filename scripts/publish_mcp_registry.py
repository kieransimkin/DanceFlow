"""Explicit, opt-in publication to the official MCP Registry after the PyPI release.

Requires a maintainer-selected mcp-publisher version and SHA-256. Never invoked by
normal package builds; no OpenAI public-directory upload API is assumed.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import tarfile
import tempfile
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen


REGISTRY = "https://registry.modelcontextprotocol.io/v0.1/servers/"
NAME = "io.github.kieransimkin/danceflow"


def fetch_bytes(url: str, maximum: int = 4 * 1024 * 1024) -> bytes:
    with urlopen(url, timeout=30) as response:
        data = response.read(maximum + 1)
    if len(data) > maximum:
        raise ValueError("Response exceeded size limit")
    return data


def fetch_json(url: str) -> dict:
    return json.loads(fetch_bytes(url))


def validate_metadata(data: dict, tag: str) -> str:
    version = data.get("version", "")
    if data.get("name") != NAME or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Unexpected registry identity")
    if tag != f"v{version}":
        raise ValueError("Registry version does not match the release tag")
    if not isinstance(data.get("description"), str) or not 1 <= len(data["description"]) <= 100:
        raise ValueError("MCP registry description must contain 1 to 100 characters")
    packages = data.get("packages", [])
    if len(packages) != 1 or packages[0].get("identifier") != "danceflow-agent-tools":
        raise ValueError("Unexpected package")
    if packages[0].get("registryType") != "pypi" or packages[0].get("version") != version:
        raise ValueError("Package version mismatch")
    if data.get("remotes"):
        raise ValueError("This is a local server, not a hosted endpoint")
    return version


def contains_expected(actual: object, expected: object) -> bool:
    """Allow registry-added defaults/IDs without accepting a changed requested field."""
    if isinstance(expected, dict):
        return isinstance(actual, dict) and all(
            k in actual and contains_expected(actual[k], v) for k, v in expected.items())
    if isinstance(expected, list):
        return isinstance(actual, list) and len(actual) == len(expected) and all(
            contains_expected(a, b) for a, b in zip(actual, expected))
    return actual == expected


def publish(metadata: Path, tag: str, publisher_version: str, publisher_sha256: str) -> None:
    data = json.loads(metadata.read_text(encoding="utf-8"))
    version = validate_metadata(data, tag)
    if os.environ.get("GITHUB_REPOSITORY") != "kieransimkin/DanceFlow":
        raise ValueError("Publishing is restricted to the owning GitHub repository")
    if not re.fullmatch(r"v\d+\.\d+\.\d+(?:[-.a-zA-Z0-9]*)?", publisher_version):
        raise ValueError("Set MCP_PUBLISHER_VERSION to a reviewed upstream release tag")
    if not re.fullmatch(r"[0-9a-fA-F]{64}", publisher_sha256):
        raise ValueError("Set MCP_PUBLISHER_SHA256 to its Linux amd64 tarball SHA-256")
    pypi = f"https://pypi.org/pypi/danceflow-agent-tools/{version}/json"
    for attempt in range(10):
        try:
            package = fetch_json(pypi)
            break
        except HTTPError as exc:
            if exc.code != 404 or attempt == 9:
                raise
            time.sleep(6)
    description = package.get("info", {}).get("description", "")
    if f"mcp-name: {NAME} -->" not in description or not package.get("urls"):
        raise ValueError("Released PyPI package lacks ownership metadata or distributions")
    endpoint = REGISTRY + quote(NAME, safe="") + "/versions/" + quote(version, safe="")
    try:
        existing = fetch_json(endpoint).get("server", {})
    except HTTPError as exc:
        if exc.code != 404:
            raise
        existing = None
    if existing is not None:
        if contains_expected(existing, {k: v for k, v in data.items() if k != "$schema"}):
            print("Matching immutable registry version already published")
            return
        raise ValueError("This immutable registry version exists with different metadata")
    url = ("https://github.com/modelcontextprotocol/registry/releases/download/"
           f"{publisher_version}/mcp-publisher_linux_amd64.tar.gz")
    raw = fetch_bytes(url, 64 * 1024 * 1024)
    if hashlib.sha256(raw).hexdigest() != publisher_sha256.lower():
        raise ValueError("mcp-publisher archive checksum mismatch")
    with tempfile.TemporaryDirectory(prefix="danceflow-mcp-publish-") as directory:
        cwd = Path(directory)
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tar:
            member = tar.getmember("mcp-publisher")
            if not member.isfile() or member.size > 64 * 1024 * 1024:
                raise ValueError("Unexpected publisher binary")
            binary = cwd / "mcp-publisher"
            binary.write_bytes(tar.extractfile(member).read())
            binary.chmod(0o700)
        (cwd / "server.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        subprocess.run([str(binary), "login", "github-oidc"], cwd=cwd, check=True, timeout=120)
        subprocess.run([str(binary), "publish"], cwd=cwd, check=True, timeout=120)
    for attempt in range(10):
        try:
            published = fetch_json(endpoint).get("server", {})
            if published.get("name") == NAME and published.get("version") == version:
                print(f"Verified official MCP Registry publication: {NAME}@{version}")
                return
        except HTTPError as exc:
            if exc.code != 404:
                raise
        if attempt < 9:
            time.sleep(6)
    raise RuntimeError("Publisher returned, but registry read-back did not verify the release")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--tag", required=True)
    args = parser.parse_args()
    publish(args.metadata, args.tag, os.environ.get("MCP_PUBLISHER_VERSION", ""),
            os.environ.get("MCP_PUBLISHER_SHA256", ""))


if __name__ == "__main__":
    main()
