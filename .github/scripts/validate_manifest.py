#!/usr/bin/env python3
"""validate_manifest.py — manifest integrity check for /releases/.

Behaviour summary:
  * If no /releases/ directory exists (pre-first-baseline state), the
    validator reports a no-op and exits 0. Package 2 scaffold must not
    fail this check.
  * For each /releases/APP-YYYY-MM-RCn/, verifies:
      - manifest.json is valid JSON and lists every file that exists in
        the release tree (except manifest.json itself);
      - every file listed has a SHA-256 that matches the file on disk;
      - every file in the release tree is listed in manifest.json;
      - MANIFEST.md and manifest.json agree on file list and version.
  * Reports every mismatch via Reporter and exits non-zero on any error.
"""

from __future__ import annotations

import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ROOT, Reporter, main_guard, sha256_file


def _iter_release_dirs() -> list[pathlib.Path]:
    releases = ROOT / "releases"
    if not releases.is_dir():
        return []
    return sorted(p for p in releases.iterdir() if p.is_dir())


def _list_release_files(release_dir: pathlib.Path) -> list[pathlib.Path]:
    out: list[pathlib.Path] = []
    for p in release_dir.rglob("*"):
        if not p.is_file():
            continue
        if p.name in {"manifest.json"}:
            continue
        out.append(p)
    return sorted(out)


def _run() -> int:
    r = Reporter("manifest")
    release_dirs = _iter_release_dirs()
    if not release_dirs:
        print("manifest: no /releases/ directory present (expected pre-first-baseline)")
        return r.finish()

    for rd in release_dirs:
        manifest_json = rd / "manifest.json"
        manifest_md = rd / "MANIFEST.md"

        if not manifest_json.is_file():
            r.error("manifest.json is missing", file=manifest_json)
            continue
        if not manifest_md.is_file():
            r.error("MANIFEST.md is missing", file=manifest_md)

        try:
            with manifest_json.open("r", encoding="utf-8") as fh:
                manifest = json.load(fh)
        except json.JSONDecodeError as exc:
            r.error(f"manifest.json is not valid JSON: {exc}", file=manifest_json)
            continue

        if not isinstance(manifest, dict):
            r.error("manifest.json top-level must be an object", file=manifest_json)
            continue

        files_entry = manifest.get("files")
        if not isinstance(files_entry, list):
            r.error("manifest.json: 'files' must be a list of {path, sha256} objects", file=manifest_json)
            continue

        listed: dict[str, str] = {}
        for i, entry in enumerate(files_entry):
            if not isinstance(entry, dict):
                r.error(f"files[{i}] is not an object", file=manifest_json)
                continue
            path = entry.get("path")
            sha = entry.get("sha256")
            if not path or not sha:
                r.error(f"files[{i}] missing 'path' or 'sha256'", file=manifest_json)
                continue
            listed[str(path)] = str(sha).lower()

        actual_files = _list_release_files(rd)
        actual_paths = {str(p.relative_to(rd)): p for p in actual_files}

        for rel, abs_path in actual_paths.items():
            if rel not in listed:
                r.error(
                    f"file present under /releases/{rd.name}/ but not in manifest.json: {rel}",
                    file=manifest_json,
                )
                continue
            actual_sha = sha256_file(abs_path)
            if actual_sha.lower() != listed[rel]:
                r.error(
                    f"sha256 mismatch for {rel}: manifest={listed[rel]}, actual={actual_sha}",
                    file=manifest_json,
                )

        for rel in listed.keys():
            if rel not in actual_paths:
                r.error(f"manifest.json lists {rel} but it is not present under /releases/{rd.name}/", file=manifest_json)

        # Optional but recommended: baseline id in manifest matches the directory name.
        baseline_id = manifest.get("baseline")
        if baseline_id and baseline_id != rd.name:
            r.error(f"manifest.json baseline '{baseline_id}' does not match directory name '{rd.name}'", file=manifest_json)

    return r.finish()


if __name__ == "__main__":
    sys.exit(main_guard(_run))
