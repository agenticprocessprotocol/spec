#!/usr/bin/env python3
"""validate_normative_keywords.py — detect normative-keyword changes.

Fails if a diff adds, removes, or modifies lines containing RFC 2119/8174
keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, SHALL, SHALL NOT, MAY,
REQUIRED, RECOMMENDED, OPTIONAL) in normative paths, UNLESS the PR
adds a new change-impact manifest under /changes/APP-*.md. Every normative
change gets its own new manifest: a manifest already on the base branch,
an edit to one, or a renamed one does not count.

Behaviour:
  * On push to main or workflow_dispatch (no diff context): no-op, exits 0.
  * On pull_request: compares BASE_SHA..HEAD_SHA for changed lines.
  * Allowlist for informative paths lives in allowlist.yml.
"""

from __future__ import annotations

import fnmatch
import os
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ROOT, Reporter, diff_added_lines, load_allowlist, main_guard

# Word-boundary match for RFC 2119/8174 keywords. The lowercase form
# in prose is intentionally NOT flagged — only the uppercased normative
# usage, which is the convention.
KEYWORDS = re.compile(
    r"\b(?:MUST(?:\s+NOT)?|SHALL(?:\s+NOT)?|SHOULD(?:\s+NOT)?|MAY|REQUIRED|RECOMMENDED|OPTIONAL)\b"
)


def _is_informative(path: pathlib.Path, allow: dict) -> bool:
    globs = allow.get("normative_keywords", {}).get("informative_paths", []) or []
    try:
        rel = str(path.relative_to(ROOT))
    except ValueError:
        return False
    return any(fnmatch.fnmatch(rel, g) for g in globs)


def _change_manifests_in_pr(base: str, head: str) -> list[pathlib.Path]:
    """Change-impact manifests ADDED by this pull request.

    Every normative change gets its own new manifest. A manifest that
    already exists on the base branch belongs to an earlier change, so
    editing it or renaming it (rename detection is on: -M) does not count.
    """
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=A", "-M", base, head, "--", "changes/"],
            cwd=ROOT, text=True,
        )
    except subprocess.CalledProcessError:
        return []
    found = []
    for line in out.splitlines():
        rel = pathlib.PurePosixPath(line.strip())
        if len(rel.parts) == 2 and fnmatch.fnmatch(rel.name, "APP-*.md") and (ROOT / rel).is_file():
            found.append(ROOT / rel)
    return found


def _run() -> int:
    r = Reporter("normative-keywords")
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    base = os.environ.get("BASE_SHA", "")
    head = os.environ.get("HEAD_SHA", "HEAD")

    if event != "pull_request" or not base:
        print("normative-keywords: no pull_request diff context; nothing to check")
        return r.finish()

    allow = load_allowlist()
    added = diff_added_lines(base, head)

    flagged: list[tuple[pathlib.Path, int, str]] = []
    for path, lineno, text in added:
        if not path.suffix.lower() == ".md":
            continue
        if _is_informative(path, allow):
            continue
        if KEYWORDS.search(text):
            flagged.append((path, lineno, text))

    if not flagged:
        return r.finish()

    manifests = _change_manifests_in_pr(base, head)
    if manifests:
        for path, lineno, text in flagged:
            r.warn(
                f"normative-keyword change detected; change-impact manifest in this PR ({len(manifests)} file(s)): {text.strip()[:200]}",
                file=path,
                line=lineno,
            )
        print("normative-keywords: changes detected; change-impact manifest present — review required but check passes")
        return r.finish()

    for path, lineno, text in flagged:
        r.error(
            f"normative-keyword change requires a change-impact manifest under /changes/APP-XXXX.md added in this PR: {text.strip()[:200]}",
            file=path,
            line=lineno,
        )
    print("normative-keywords: changes detected without a change-impact manifest. See CONTRIBUTING.md §5.4.")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main_guard(_run))
