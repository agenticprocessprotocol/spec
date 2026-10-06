"""Shared helpers for APP specification validators.

Design goals:
 - No network access, no external services.
 - Fail with a clear, parseable message that names the file and the
   specific condition that failed.
 - Non-zero exit on any failure; zero exit only when all checks pass.
 - Readable by a non-Python-expert reviewer: structure is simple,
   comments are explanatory, no clever metaprogramming.
"""

from __future__ import annotations

import hashlib
import os
import pathlib
import re
import subprocess
import sys
from typing import Iterable, Sequence

import yaml  # PyYAML

# --------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------- #

# Validators are called from the repo root in CI (`python .github/scripts/...`).
# When invoked locally they may be called from .github/scripts/. We resolve
# the repo root by walking up until we see a .github directory.
def repo_root() -> pathlib.Path:
    here = pathlib.Path.cwd().resolve()
    for parent in [here] + list(here.parents):
        if (parent / ".github").is_dir() and (parent / "LICENSE").exists():
            return parent
    # Fallback: assume cwd is the root.
    return here


ROOT = repo_root()
SCRIPTS_DIR = ROOT / ".github" / "scripts"
ALLOWLIST_PATH = SCRIPTS_DIR / "allowlist.yml"


# --------------------------------------------------------------------- #
# File discovery
# --------------------------------------------------------------------- #

MD_EXTENSIONS = {".md"}
JSON_EXTENSIONS = {".json"}


def iter_markdown_files(
    include: Iterable[str] = ("drafts", "guides", "releases", "csl", "legal", "changes", "decisions"),
    exclude_names: Iterable[str] = (".git", "node_modules", ".github"),
) -> list[pathlib.Path]:
    """Return markdown files under the given top-level directories.

    Also includes top-level README/CONTRIBUTING/etc.
    """
    out: list[pathlib.Path] = []
    exclude_names = set(exclude_names)
    # Top-level markdown files.
    for p in ROOT.iterdir():
        if p.is_file() and p.suffix.lower() in MD_EXTENSIONS:
            out.append(p)
    # Specified subdirectories.
    for name in include:
        d = ROOT / name
        if not d.is_dir():
            continue
        for p in d.rglob("*"):
            if any(part in exclude_names for part in p.parts):
                continue
            if p.is_file() and p.suffix.lower() in MD_EXTENSIONS:
                out.append(p)
    return sorted(out)


def iter_schema_files() -> list[pathlib.Path]:
    schemas_dir = ROOT / "schemas"
    if not schemas_dir.is_dir():
        return []
    return sorted(p for p in schemas_dir.rglob("*.json") if "examples" not in p.parts)


# --------------------------------------------------------------------- #
# Hashing
# --------------------------------------------------------------------- #

def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# --------------------------------------------------------------------- #
# Git diff helpers
# --------------------------------------------------------------------- #

def changed_files_since(base_sha: str, head_sha: str = "HEAD") -> list[pathlib.Path]:
    if not base_sha:
        return []
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", base_sha, head_sha],
            cwd=ROOT,
            text=True,
        )
    except subprocess.CalledProcessError:
        return []
    return [ROOT / line for line in out.splitlines() if line.strip()]


def diff_added_lines(base_sha: str, head_sha: str = "HEAD") -> list[tuple[pathlib.Path, int, str]]:
    """Return (file, line_number_after, text) for lines added in the diff."""
    if not base_sha:
        return []
    try:
        patch = subprocess.check_output(
            ["git", "diff", "--unified=0", base_sha, head_sha, "--", "*.md"],
            cwd=ROOT,
            text=True,
        )
    except subprocess.CalledProcessError:
        return []

    added: list[tuple[pathlib.Path, int, str]] = []
    cur_path: pathlib.Path | None = None
    cur_lineno = 0
    hunk_header = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")
    for line in patch.splitlines():
        if line.startswith("+++ b/"):
            cur_path = ROOT / line[len("+++ b/"):].strip()
            continue
        m = hunk_header.match(line)
        if m:
            cur_lineno = int(m.group(1))
            continue
        if line.startswith("+") and not line.startswith("+++"):
            if cur_path is not None:
                added.append((cur_path, cur_lineno, line[1:]))
            cur_lineno += 1
        elif not line.startswith("-"):
            cur_lineno += 1
    return added


# --------------------------------------------------------------------- #
# Allowlist
# --------------------------------------------------------------------- #

def load_allowlist() -> dict:
    if not ALLOWLIST_PATH.is_file():
        return {}
    with ALLOWLIST_PATH.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


# --------------------------------------------------------------------- #
# Reporter
# --------------------------------------------------------------------- #

class Reporter:
    """Collects validator findings and prints a human- and machine-friendly summary."""

    def __init__(self, validator_name: str) -> None:
        self.name = validator_name
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str, *, file: pathlib.Path | None = None, line: int | None = None) -> None:
        prefix = _prefix(file, line)
        self.errors.append(f"{prefix}{msg}")

    def warn(self, msg: str, *, file: pathlib.Path | None = None, line: int | None = None) -> None:
        prefix = _prefix(file, line)
        self.warnings.append(f"{prefix}{msg}")

    def finish(self) -> int:
        """Print summary and return an exit code. Non-zero if errors exist."""
        for w in self.warnings:
            print(f"::warning title={self.name}::{w}")
        for e in self.errors:
            print(f"::error title={self.name}::{e}")
        total = len(self.errors)
        if total:
            print(f"\n{self.name}: {total} error(s), {len(self.warnings)} warning(s)")
            return 1
        print(f"{self.name}: OK ({len(self.warnings)} warning(s))")
        return 0


def _prefix(file: pathlib.Path | None, line: int | None) -> str:
    if file is None:
        return ""
    try:
        rel = file.relative_to(ROOT)
    except ValueError:
        rel = file
    if line is not None:
        return f"{rel}:{line}: "
    return f"{rel}: "


# --------------------------------------------------------------------- #
# Convenience
# --------------------------------------------------------------------- #

def main_guard(entry_point) -> int:
    """Thin wrapper for validators' main(). Returns an exit code."""
    try:
        return entry_point()
    except Exception as exc:  # noqa: BLE001 — final guard, must not raise
        print(f"::error title=validator-crash::Unexpected error: {exc}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 2


# Standalone sanity check when common.py is invoked directly.
if __name__ == "__main__":
    print(f"ROOT = {ROOT}")
    print(f"Markdown files: {len(iter_markdown_files())}")
    print(f"Schema files:   {len(iter_schema_files())}")
    print(f"Allowlist:      {'yes' if ALLOWLIST_PATH.is_file() else 'absent'}")
