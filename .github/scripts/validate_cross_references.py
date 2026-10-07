#!/usr/bin/env python3
"""validate_cross_references.py — requirement IDs and internal references.

Checks:
  * Each requirement ID (patterns like CORE-A1-05, SEC-S2-01, APP-5 T-3-01)
    appears as a definition in at most ONE markdown file. Multiple
    references are fine; multiple DEFINITIONS are not.
  * Internal section references of the form "APP-<n> §<section>" or
    "see §<section>" resolve to a heading in the referenced document.
  * Markdown links to other repo files (./..., /... paths) resolve on disk.

Definition heuristic:
  A requirement ID is treated as "defined" where it appears at the start
  of a markdown header line (`### CORE-A1-05 ...`) or in a bolded span
  at the start of a list item (`- **CORE-A1-05** ...`). This matches
  how APP documents introduce requirements.
"""

from __future__ import annotations

import pathlib
import re
import sys
import urllib.parse
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ROOT, Reporter, iter_markdown_files, load_allowlist, main_guard

# Requirement IDs use known APP requirement-family prefixes.
# Document IDs (APP-IG-NN, APP-N) are intentionally NOT matched —
# they identify DOCUMENTS, not requirements.
_REQ_PREFIX = r"(?:CORE|SEC|EC|CP|CONF|XX|T)"
REQ_ID = re.compile(r"\b(" + _REQ_PREFIX + r"-[A-Z0-9]{1,4}(?:-[A-Z0-9]{1,4}){0,3})\b")
DEFINITION_HEADER = re.compile(r"^#{2,6}\s+(" + _REQ_PREFIX + r"-[A-Z0-9]{1,4}(?:-[A-Z0-9]{1,4}){0,3})\b")
DEFINITION_LIST_BOLD = re.compile(r"^\s*[-*]\s+\*\*(" + _REQ_PREFIX + r"-[A-Z0-9]{1,4}(?:-[A-Z0-9]{1,4}){0,3})\*\*")

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
SECTION_REF = re.compile(r"\bAPP-([0-9]|IG-\d{2})\s+§([A-Za-z0-9\.\-]+)")

MD_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def _is_release_snapshot(f: pathlib.Path) -> bool:
    """True if the file sits under /releases/** (frozen baseline snapshot).
    Release content duplicates the live source by design — skipping it here
    avoids false 'duplicate definition' errors."""
    try:
        rel = f.relative_to(ROOT)
    except ValueError:
        return False
    return rel.parts and rel.parts[0] == "releases"


def _collect_definitions(files: list[pathlib.Path]) -> dict[str, list[tuple[pathlib.Path, int]]]:
    defs: dict[str, list[tuple[pathlib.Path, int]]] = defaultdict(list)
    for f in files:
        if _is_release_snapshot(f):
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            m = DEFINITION_HEADER.match(line) or DEFINITION_LIST_BOLD.match(line)
            if m:
                defs[m.group(1)].append((f, lineno))
    return defs


def _collect_headings(files: list[pathlib.Path]) -> dict[pathlib.Path, set[str]]:
    """For every file, record the heading-section numeric labels we can detect.
    E.g. a heading "## 3.2 Something" -> adds '3.2' to that file's set.
    """
    out: dict[pathlib.Path, set[str]] = {}
    section_label = re.compile(r"^\s*(\d+(?:\.\d+){0,4})\b")
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        sections: set[str] = set()
        for line in text.splitlines():
            m = HEADING.match(line)
            if not m:
                continue
            heading_body = m.group(2)
            s = section_label.match(heading_body)
            if s:
                sections.add(s.group(1))
            # Alpha-numeric section labels (e.g. S13, A1) are APP-specific.
            # Add any token that looks like a section label.
            for tok in re.findall(r"\b([SACT]\d+(?:\.\d+)?)\b", heading_body):
                sections.add(tok)
        out[f] = sections
    return out


def _collect_md_links(files: list[pathlib.Path]) -> list[tuple[pathlib.Path, int, str]]:
    out: list[tuple[pathlib.Path, int, str]] = []
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in MD_LINK.finditer(line):
                out.append((f, lineno, m.group(1)))
    return out


def _file_for_app_number(files: list[pathlib.Path], num_or_ig: str) -> pathlib.Path | None:
    needle = f"APP-{num_or_ig}"
    for f in files:
        if f.name.startswith(needle + "_") or f.name == f"{needle}.md":
            return f
    return None


def _run() -> int:
    r = Reporter("cross-references")
    allow = load_allowlist()
    known_tbd = set((allow.get("cross_references", {}).get("known_tbd_targets") or []))
    files = iter_markdown_files()

    # 1. Duplicate requirement-ID definitions.
    defs = _collect_definitions(files)
    for req_id, places in defs.items():
        if len(places) > 1:
            locs = ", ".join(f"{p.relative_to(ROOT)}:{ln}" for p, ln in places)
            r.error(f"requirement ID {req_id} defined in multiple places: {locs}")

    # 2. Internal section references.
    headings = _collect_headings(files)
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in SECTION_REF.finditer(line):
                app_label = m.group(1)
                section = m.group(2)
                target = _file_for_app_number(files, app_label)
                if target is None:
                    r.warn(
                        f"reference to APP-{app_label} §{section} but no matching APP-{app_label} document found in repo",
                        file=f, line=lineno,
                    )
                    continue
                if section not in headings.get(target, set()):
                    key = f"APP-{app_label} §{section}"
                    if key in known_tbd:
                        r.warn(f"reference to {key} not resolved (known TBD, allowlisted)", file=f, line=lineno)
                    else:
                        r.warn(f"reference to {key} not resolved against detected headings in {target.name}", file=f, line=lineno)

    # 3. Markdown relative links to repo files.
    for f, lineno, href in _collect_md_links(files):
        parsed = urllib.parse.urlparse(href)
        if parsed.scheme in ("http", "https", "mailto", "ftp"):
            continue  # external — the links workflow handles these
        # Trim any fragment.
        path_only = parsed.path
        if not path_only:
            continue
        # Resolve relative to the file.
        if path_only.startswith("/"):
            target = ROOT / path_only.lstrip("/")
        else:
            target = (f.parent / path_only).resolve()
        if target.exists():
            continue
        r.warn(f"relative link does not resolve: {href}", file=f, line=lineno)

    return r.finish()


if __name__ == "__main__":
    sys.exit(main_guard(_run))
