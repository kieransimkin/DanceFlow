"""Read official runtime releases before a workflow; never install or deploy."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from importlib import metadata
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.request import Request, urlopen

# ThumbMoves has a separate release stream inside PixelCue. Documentation-only
# tags deliberately do not match these runtime prefixes.
COMPONENTS = (
    ("StemLab", "stemlab", "v", "danceflow-stemlab"),
    ("DanceRudiments", "DanceRudiments", "v", "dancerudiments"),
    ("FrameRudiments", "FrameRudiments", "v", "framerudiments"),
    ("DanceMoves", "DanceMoves", "v", None),
    ("KeywordMoves", "keywordmoves", "v", "keywordmoves"),
    ("RasterMoves", "RasterMoves", "v", "rastermoves"),
    ("LikenessForge", "LikenessForge", "v", "likenessforge"),
    ("PixelCue", "PixelCue", "v", "pixelcue"),
    ("PrismMoves", "PrismMoves", "v", "prismmoves"),
    ("ThumbMoves", "PixelCue", "thumbmoves-v", "thumbmoves"),
    ("React Timeline Sequence", "react-timeline-sequence", "v", None),
    ("MediaSlide", "react-mediaslide", "v", None),
    ("EPK Social Metadata", "kieran-epk-social-metadata", "v", None),
    ("DanceVault", "DanceVault", "v", None),
    ("WorkflowMoves", "WorkflowMoves", "v", None),
    ("Potbot", "potbot", "v", "potbot"),
    ("DanceFlow for Unity", "DanceFlow.Unity", "v", None),
    ("DanceFlow toolkit", "DanceFlow", "v", "danceflow-agent-tools"),
)


def stable_version(tag: str, prefix: str = "v") -> tuple[int, int, int] | None:
    match = re.fullmatch(re.escape(prefix) + r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", tag)
    return tuple(map(int, match.groups())) if match else None


def latest_runtime(releases: list[dict], prefix: str = "v") -> dict | None:
    candidates = [(stable_version(r.get("tag_name", ""), prefix), r) for r in releases
                  if not r.get("draft") and not r.get("prerelease")]
    candidates = [(version, row) for version, row in candidates if version is not None]
    return max(candidates, key=lambda item: item[0])[1] if candidates else None


def official_releases(repository: str) -> list[dict]:
    """Use supported gh auth when available; otherwise the public GitHub API."""
    if repository not in {item[1] for item in COMPONENTS}:
        raise ValueError("Unknown DanceFlow repository")
    endpoint = f"repos/kieransimkin/{repository}/releases?per_page=100"
    if shutil.which("gh"):
        # GitHub emits UTF-8 JSON. Relying on the Windows console code page can
        # make a valid release body fail decoding before json.loads sees it.
        result = subprocess.run(["gh", "api", "--paginate", "--slurp", endpoint],
                                capture_output=True, text=True, encoding="utf-8",
                                errors="strict", timeout=90)
        if result.returncode:
            # Do not copy arbitrary remote bodies or authentication diagnostics
            # into a shareable report.
            raise OSError(f"GitHub release query failed (exit {result.returncode})")
        pages = json.loads(result.stdout)
        return [release for page in pages for release in page]
    releases = []
    for page in range(1, 11):
        request = Request("https://api.github.com/" + endpoint + f"&page={page}",
                          headers={"Accept": "application/vnd.github+json", "User-Agent": "DanceFlow-release-check"})
        with urlopen(request, timeout=20) as response:
            batch = json.load(response)
        releases.extend(batch)
        if len(batch) < 100:
            return releases
    raise OSError("Release pagination exceeded the bounded query; no latest version inferred")


def compare_version(installed: str | None, released: str) -> str:
    if installed is None:
        return "not_observed"
    current = stable_version("v" + installed)
    latest = stable_version("v" + released)
    if current is None or latest is None:
        return "unverified_identity"
    if current == latest:
        return "current"
    return "update_available" if current < latest else "ahead_of_release"


def check_releases(installed: dict[str, str] | None = None, fetch=official_releases) -> dict:
    overrides = installed or {}
    repositories = {}
    rows = []
    for name, repository, prefix, distribution in COMPONENTS:
        row = {"component": name, "repository": f"https://github.com/kieransimkin/{repository}",
               "installed": overrides.get(name), "installed_scope": "explicit observation" if name in overrides else "this Python environment"}
        if name not in overrides and distribution:
            try:
                row["installed"] = metadata.version(distribution)
            except metadata.PackageNotFoundError:
                pass
        try:
            if repository not in repositories:
                try:
                    repositories[repository] = fetch(repository)
                except Exception as exc:
                    repositories[repository] = exc
            releases = repositories[repository]
            if isinstance(releases, Exception):
                raise releases
            release = latest_runtime(releases, prefix)
            if release is None:
                row.update(status="no_stable_release", released=None,
                           reason="Official query succeeded; no stable runtime release exists. Source previews require a pinned commit and separate qualification.")
                rows.append(row)
                continue
            version = release["tag_name"][len(prefix):]
            row.update(released=version, tag=release["tag_name"], url=release["html_url"],
                       published_at=release.get("published_at"),
                       assets=[{"name":a["name"], "url":a["browser_download_url"],
                                "size":a["size"], "digest":a.get("digest")} for a in release.get("assets",[])],
                       status=compare_version(row["installed"],version))
        except Exception as exc:
            row.update(status="unavailable", reason=type(exc).__name__ + ": official release could not be verified")
        rows.append(row)
    return {"schema":"danceflow.release-check.v1", "checked_at":datetime.now(timezone.utc).isoformat(),
            "scope":"Fresh official release queries; installed identities cover only the selected environment or explicit observations.",
            "components":rows,
            "limits":["No installation, source mutation, model download, WordPress save or deployment was performed.",
                      "Package registry acceptance, exact artifact bytes, compatibility and actual feature operation require separate verification.",
                      "An unavailable query is not evidence that a cached release is current."]}


def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True,help="New JSON receipt; existing files are preserved")
    parser.add_argument("--installed",type=Path,help="JSON mapping component names to freshly observed versions")
    args=parser.parse_args(argv)
    if args.output.exists():
        parser.error("Choose a new output path; release receipts are not overwritten")
    installed=json.loads(args.installed.read_text(encoding="utf-8-sig")) if args.installed else {}
    if not isinstance(installed,dict) or any(not isinstance(k,str) or not isinstance(v,str) for k,v in installed.items()):
        parser.error("Installed observations must be a JSON object of string names and versions")
    report=check_releases(installed)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    for row in report["components"]:
        print(f'{row["component"]}: {row["status"]}; installed={row["installed"] or "unobserved"}; released={row.get("released","unavailable")}')
    return 2 if any(row["status"]=="unavailable" for row in report["components"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
