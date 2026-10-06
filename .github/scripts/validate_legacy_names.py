#!/usr/bin/env python3
"""validate_legacy_names.py — flag residual PGP references outside allowlist.

The protocol was renamed from Process Governance Protocol (PGP) to
Agentic Process Protocol (APP) in the rename cascade. Historical
references in version-history sections are approved exceptions; new
unapproved uses must be caught.

Checks:
  * No file in the repository (except approved paths) has 'PGP' in its name.
  * No markdown file in the published surfaces contains an unallowlisted
    use of 'PGP-' or 'PGP'.
  * Allowlisted contexts: see .github/scripts/allowlist.yml 'legacy_names'.
"""

from __future__ import annotations

import fnmatch
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ROOT, Reporter, iter_markdown_files, load_allowlist, main_guard

PGP_WORD = re.compile(r"\bPGP\b")
PGP_DOCID = re.compile(r"\bPGP-[0-9A-Z]+\b")


def _is_file_allowlisted_for_path(path: pathlib.Path, allow: dict) -> bool:
    globs = allow.get("legacy_names", {}).get("file_globs", []) or []
    rel = str(path.relative_to(ROOT))
    return any(fnmatch.fnmatch(rel, g) for g in globs)


def _line_matches_context(line: str, allow: dict) -> bool:
    patterns = allow.get("legacy_names", {}).get("context_patterns", []) or []
    return any(re.search(pat, line) for pat in patterns)


def _run() -> int:
    r = Reporter("legacy-names")
    allow = load_allowlist()

    # 1. Filename check: no file (anywhere) should have "PGP" in its name
    # except files explicitly covered by the allowlist file globs.
    forbidden_name_dirs = ["drafts", "releases", "guides", "csl", "legal", "changes"]
    for top in forbidden_name_dirs:
        d = ROOT / top
        if not d.is_dir():
            continue
        for p in d.rglob("*"):
            if p.is_file() and "PGP" in p.name:
                r.error(f"filename contains 'PGP': {p.name}", file=p)

    # 2. Line-level check inside markdown files, honouring allowlist.
    for md in iter_markdown_files():
        file_allow = _is_file_allowlisted_for_path(md, allow)
        try:
            text = md.read_text(encoding="utf-8", errors="strict")
        except (UnicodeDecodeError, OSError) as exc:
            r.warn(f"could not read file: {exc}", file=md)
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            if not (PGP_WORD.search(line) or PGP_DOCID.search(line)):
                continue
            # If the file is in an allowlisted globset, additionally require
            # the specific line to match a context pattern.
            if file_allow and _line_matches_context(line, allow):
                continue
            # Otherwise it's a violation.
            r.error(
                f"found 'PGP' reference outside the allowlist: {line.strip()[:200]}",
                file=md,
                line=lineno,
            )

    return r.finish()


if __name__ == "__main__":
    sys.exit(main_guard(_run))
