#!/usr/bin/env python3
"""validate_reference_hygiene.py — every citation in published content
must resolve to a public source.

Background
----------
Change tables, version histories, notes and rationale digests must not
cite documents, registers or labels that a reader of this public
repository cannot open. This validator looks for the *shapes* such
citations take (a document number followed by a section marker, a
register-style identifier, a docket-style number, and so on). It never
lists the literal names of non-public documents: the repository is
public, so a literal list would itself disclose them.

Pattern classes (generic shapes only)
-------------------------------------
  doc-number        a 4-digit document number cited with a section,
                    annex, version or register marker
  register-id       a register-style identifier, e.g. AB-C-12
  docket-number     a docket-style number, e.g. 123456-1234
  zone-label        a zone label, Z1..Z3
  tier-label        a distribution-tier label, e.g. T3-Word
  process-wording   wording about an internal disclosure process
  named-register    "<Capitalised words> Register"
  vendor-name       the interim custodian's organisation name (names
                    are read from allowlist.yml; scope-limited)

Scope (from allowlist.yml 'reference_hygiene')
----------------------------------------------
  error_globs     every match is an error
  warn_globs      every match is a warning (frozen release content)
  frozen_records  accepted records: matches warn, except on lines this
                  PR adds, which error
  skip_globs      never scanned (files that name the custodian
                  legitimately)
  Anything not matched by a glob is not scanned.

Environment (optional, set by the workflow on pull requests)
------------------------------------------------------------
  BASE_SHA, HEAD_SHA   used to find lines added to frozen records.
"""

from __future__ import annotations

import fnmatch
import os
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ROOT, Reporter, load_allowlist, main_guard

# --------------------------------------------------------------------- #
# Pattern classes. Generic shapes only; never add literal names here.
# --------------------------------------------------------------------- #

PATTERNS: dict[str, re.Pattern[str]] = {
    # The lookbehind stops matches inside IDs such as APP-DEC-0003 or
    # version strings such as 1.0003.
    "doc-number": re.compile(r"(?<![-\w.])0\d{3}[a-z]?\b.{0,20}?(Annex|§|[A-Z]{2,4}-\d|v\d)"),
    "register-id": re.compile(r"\b[A-Z]{1,3}-[A-Z]-?\d{2}[A-Z]?\b"),
    "docket-number": re.compile(r"\b\d{6}-\d{4}\b"),
    "zone-label": re.compile(r"\bZ[1-3]\b"),
    "tier-label": re.compile(r"\bT\d-[A-Z][a-z]+\b"),
    # "internal architecture" is deliberately absent: the specs use it
    # legitimately.
    "process-wording": re.compile(
        r"(?i)\b(IP review|IP screen|claim[- ]scope|trade secret|internal (design|release note)s?)\b"
    ),
    "named-register": re.compile(r"\b([A-Z][A-Za-z0-9-]* ){1,4}Register\b"),
}


def _vendor_pattern(names: list[str]) -> re.Pattern[str] | None:
    names = [n for n in (names or []) if str(n).strip()]
    if not names:
        return None
    alt = "|".join(re.escape(str(n).strip()) for n in names)
    return re.compile(rf"(?i)\b({alt})\b")


# --------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------- #

def _match_any(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) for g in globs or [])


def _tracked_files() -> list[str]:
    """Tracked files plus untracked, non-ignored files, so a local run
    also catches files not yet committed. CI checkouts hold only
    tracked files, so the two sets are the same there."""
    out = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT
    )
    return sorted(p for p in out.decode("utf-8", "replace").split("\0") if p)


def _added_lines(base: str, head: str) -> dict[str, set[int]]:
    """Map path -> set of line numbers (in HEAD) added since BASE."""
    if not base:
        return {}
    try:
        patch = subprocess.check_output(
            ["git", "diff", "--unified=0", "--no-color", base, head or "HEAD"],
            cwd=ROOT, text=True, errors="replace",
        )
    except subprocess.CalledProcessError:
        return {}
    added: dict[str, set[int]] = {}
    cur: str | None = None
    lineno = 0
    hunk = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")
    for ln in patch.splitlines():
        if ln.startswith("+++ "):
            cur = ln[6:] if ln.startswith("+++ b/") else None
            continue
        m = hunk.match(ln)
        if m:
            lineno = int(m.group(1))
            continue
        if ln.startswith("+") and cur is not None:
            added.setdefault(cur, set()).add(lineno)
            lineno += 1
        elif not ln.startswith("-"):
            lineno += 1
    return added


def _allowed(cls: str, token: str, rel: str, cfg: dict) -> bool:
    for pat in (cfg.get("id_allowlist", {}) or {}).get(cls, []) or []:
        if re.search(pat, token):
            return True
    for exc in cfg.get("exceptions", []) or []:
        if exc.get("class") == cls and fnmatch.fnmatch(rel, exc.get("path", "")) and exc.get("reason"):
            return True
    return False


# --------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------- #

def _run() -> int:
    r = Reporter("reference-hygiene")
    cfg = (load_allowlist().get("reference_hygiene") or {})
    if not cfg:
        r.error("allowlist.yml has no 'reference_hygiene' section; scope is undefined")
        return r.finish()

    error_globs = cfg.get("error_globs", [])
    warn_globs = cfg.get("warn_globs", [])
    skip_globs = cfg.get("skip_globs", [])
    frozen = cfg.get("frozen_records", [])
    vendor_re = _vendor_pattern(cfg.get("vendor_names", []))
    vendor_globs = cfg.get("vendor_scope_globs", [])

    added = _added_lines(os.environ.get("BASE_SHA", ""), os.environ.get("HEAD_SHA", ""))

    scanned = 0
    for rel in _tracked_files():
        if _match_any(rel, skip_globs):
            continue
        if _match_any(rel, frozen):
            level = "frozen"
        elif _match_any(rel, error_globs):
            level = "error"
        elif _match_any(rel, warn_globs):
            level = "warn"
        else:
            continue

        path = ROOT / rel
        try:
            text = path.read_text(encoding="utf-8", errors="strict")
        except (UnicodeDecodeError, OSError):
            continue  # binary or unreadable: not prose, not scanned
        scanned += 1

        patterns = dict(PATTERNS)
        if vendor_re is not None and _match_any(rel, vendor_globs):
            patterns["vendor-name"] = vendor_re

        new_lines = added.get(rel, set())
        for lineno, line in enumerate(text.splitlines(), start=1):
            for cls, pat in patterns.items():
                for m in pat.finditer(line):
                    token = m.group(0)
                    if _allowed(cls, token, rel, cfg):
                        continue
                    # The matched text is deliberately not printed: CI logs
                    # of a public repository are public, and a list of
                    # matches would gather every finding in one place.
                    msg = f"[{cls}] at column {m.start() + 1} — cite a public source or remove the citation"
                    if level == "error" or (level == "frozen" and lineno in new_lines):
                        r.error(msg, file=path, line=lineno)
                    else:
                        r.warn(msg, file=path, line=lineno)

    print(f"reference-hygiene: scanned {scanned} file(s)")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main_guard(_run))
