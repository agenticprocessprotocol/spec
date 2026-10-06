#!/usr/bin/env python3
"""validate_release_integrity.py — two checks in one validator.

Check A — Release PR integrity.
  Fires when the PR changes any file under /releases/APP-YYYY-MM-RCn/.
  Verifies that:
    * No file under a /releases/<baseline>/ directory already present at
      the base ref has been modified (release immutability).
    * manifest.json and MANIFEST.md are both present in each touched
      release directory.
    * The release directory contains RELEASE-NOTES.md and KNOWN_ISSUES.md.
    * CHANGELOG.md has an entry for the baseline id.

Check B — Release Approver sign-off presence.
  Fires when the PR touches a path in the allowlist's
  release_integrity.sign_off_required_paths. Verifies that:
    * The PR body contains a Release Approver sign-off block.
    * The sign-off block's named fields are populated (name, date, and
      a classification picked from the list, not a placeholder).
  This is the enforcement path for GOVERNANCE.md §2.2.
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


# ----------------------------------------------------------------------
# Shared helpers
# ----------------------------------------------------------------------

def _read_changed_paths() -> list[str]:
    f = os.environ.get("CHANGED_PATHS_FILE", "")
    if f and pathlib.Path(f).is_file():
        return [ln.strip() for ln in pathlib.Path(f).read_text(encoding="utf-8").splitlines() if ln.strip()]
    return []


def _read_pr_body() -> str:
    f = os.environ.get("PR_BODY_PATH", "")
    if f and pathlib.Path(f).is_file():
        return pathlib.Path(f).read_text(encoding="utf-8", errors="replace")
    return ""


def _any_match(paths: list[str], globs: list[str]) -> list[str]:
    return [p for p in paths if any(fnmatch.fnmatch(p, g) for g in globs)]


# ----------------------------------------------------------------------
# Check A — release immutability + release-dir integrity
# ----------------------------------------------------------------------

RELEASE_DIR_RE = re.compile(r"^releases/([^/]+)/")


def _check_release_integrity(r: Reporter, changed_paths: list[str]) -> None:
    base = os.environ.get("BASE_SHA", "")
    release_changes = [p for p in changed_paths if p.startswith("releases/")]
    if not release_changes:
        return

    # Group by baseline id (releases/<id>/).
    baselines: dict[str, list[str]] = {}
    for p in release_changes:
        m = RELEASE_DIR_RE.match(p)
        if m:
            baselines.setdefault(m.group(1), []).append(p)

    for baseline, paths in baselines.items():
        rd = ROOT / "releases" / baseline

        # Immutability check: if this baseline directory already existed
        # at the base ref, no file inside may be modified.
        if base:
            try:
                subprocess.check_output(
                    ["git", "cat-file", "-e", f"{base}:releases/{baseline}"],
                    cwd=ROOT, stderr=subprocess.DEVNULL,
                )
                existed_at_base = True
            except subprocess.CalledProcessError:
                existed_at_base = False
            if existed_at_base:
                for p in paths:
                    r.error(
                        f"release directory /releases/{baseline}/ already exists at base ref; must not modify tagged release content",
                        file=ROOT / p,
                    )

        # Integrity: required files present.
        required = ["manifest.json", "MANIFEST.md", "RELEASE-NOTES.md", "KNOWN_ISSUES.md"]
        for req in required:
            if not (rd / req).is_file():
                r.error(f"/releases/{baseline}/ missing required file: {req}", file=rd / req)

        # CHANGELOG mention.
        changelog = ROOT / "CHANGELOG.md"
        if changelog.is_file():
            if baseline not in changelog.read_text(encoding="utf-8"):
                r.warn(f"CHANGELOG.md does not mention baseline id '{baseline}'", file=changelog)
        else:
            r.warn("CHANGELOG.md is missing", file=changelog)


# ----------------------------------------------------------------------
# Check B — Release Approver sign-off field verification
# ----------------------------------------------------------------------

SIGNOFF_HEADER = re.compile(r"(?mi)^##\s*Release Approver sign-off\b")

# The sign-off template fields we require populated:
#   - "I am the Release Approver and I sign off on this change:" NAME
#   - "Date:" YYYY-MM-DD
#   - "Classification sign-off applies to:" one of the listed classes
#
# For editorial-only PRs (no sign-off required by path), it is acceptable
# to write "N/A" in each field.
NAME_FIELD = re.compile(r"(?mi)^\s*-\s*\*\*I am the Release Approver.*?\*\*\s*(.+)$")
DATE_FIELD = re.compile(r"(?mi)^\s*-\s*\*\*Date:\*\*\s*(.+)$")
CLASS_FIELD = re.compile(r"(?mi)^\s*-\s*\*\*Classification sign-off applies to:\*\*\s*(.+)$")

PLACEHOLDER_MARKERS = {"<!--", "<!-", "--", "name", "yyyy-mm-dd", ""}

VALID_CLASS_TOKENS = {"release", "scope", "legal", "schema", "reference", "normative"}


def _is_populated(raw: str) -> tuple[bool, str]:
    """Return (True, value) if the field is actually filled in.
    Comments (<!-- ... --> on the line) are stripped before evaluation.
    """
    # Strip HTML comments.
    stripped = re.sub(r"<!--.*?-->", "", raw, flags=re.DOTALL).strip()
    low = stripped.lower()
    if not stripped or stripped == "<!---->" or low in PLACEHOLDER_MARKERS:
        return False, stripped
    # Reject obvious placeholders.
    if low.startswith("name") or low in {"<name>", "<yyyy-mm-dd>"}:
        return False, stripped
    return True, stripped


def _check_sign_off(r: Reporter, changed_paths: list[str], pr_body: str, allow: dict) -> None:
    globs = (allow.get("release_integrity", {}).get("sign_off_required_paths") or [])
    matched = _any_match(changed_paths, globs)
    if not matched:
        print("release-integrity: no sign-off-required paths touched")
        return

    print(f"release-integrity: sign-off-required paths touched ({len(matched)} file(s))")

    if not pr_body.strip():
        r.error("Release Approver sign-off required but PR body is empty")
        return

    if not SIGNOFF_HEADER.search(pr_body):
        r.error("Release Approver sign-off section not found in PR body; use the PR template.")
        return

    # Extract the sign-off body (from the header to end of document).
    body_slice = pr_body[SIGNOFF_HEADER.search(pr_body).start():]

    name_m = NAME_FIELD.search(body_slice)
    date_m = DATE_FIELD.search(body_slice)
    class_m = CLASS_FIELD.search(body_slice)

    if not name_m:
        r.error("Release Approver sign-off: name field missing")
    else:
        ok, val = _is_populated(name_m.group(1))
        if not ok:
            r.error(f"Release Approver sign-off: name field appears unpopulated: '{val or '(empty)'}'")

    if not date_m:
        r.error("Release Approver sign-off: date field missing")
    else:
        ok, val = _is_populated(date_m.group(1))
        if not ok or not re.search(r"\d{4}-\d{2}-\d{2}", val):
            r.error(f"Release Approver sign-off: date not populated with YYYY-MM-DD: '{val or '(empty)'}'")

    if not class_m:
        r.error("Release Approver sign-off: classification field missing")
    else:
        ok, val = _is_populated(class_m.group(1))
        if not ok:
            r.error("Release Approver sign-off: classification field appears unpopulated")
        else:
            low = val.lower()
            if low == "n/a":
                r.error(
                    "Classification 'N/A' but PR touches sign-off-required paths; "
                    "sign-off cannot be waived by writing N/A on this class."
                )
            elif not any(tok in low for tok in VALID_CLASS_TOKENS):
                r.warn(
                    f"Classification '{val}' did not match any expected token "
                    f"({sorted(VALID_CLASS_TOKENS)}); treat as advisory."
                )

    # Signer must appear in .github/release-approvers.txt as read from the
    # BASE branch. We fetch the base-branch copy so a hostile PR cannot
    # add itself to the list in the same PR.
    if name_m:
        _, name_val = _is_populated(name_m.group(1))
        if name_val and name_val.lower() not in {"n/a", "<name>", ""}:
            authorised = _read_authorised_approvers_from_base()
            if authorised is None:
                r.warn(
                    "could not read .github/release-approvers.txt from base branch; "
                    "signer identity not independently verified for this PR."
                )
            else:
                # Match by: (a) exact @handle in the field; (b) presence of
                # one of the authorised handles anywhere in the field value
                # (allowing "Vaidhya (@handle)" or "Name <handle>" formats).
                matched = any(
                    f"@{h}" in name_val
                    or h.lower() in name_val.lower()
                    for h in authorised
                )
                if not matched:
                    r.error(
                        f"Release Approver sign-off: signer '{name_val}' does not match any handle "
                        f"in .github/release-approvers.txt on the base branch. "
                        f"Authorised handles: {sorted(authorised)}"
                    )


def _read_authorised_approvers_from_base() -> set[str] | None:
    """Read .github/release-approvers.txt from the PR's base ref.

    Returns a set of normalised handles (lowercased, @ stripped), or None if
    the file could not be read. Falls back to the on-disk copy only if the
    base ref is not available (e.g., workflow_dispatch).
    """
    base = os.environ.get("BASE_SHA", "")
    content = ""
    if base:
        try:
            content = subprocess.check_output(
                ["git", "show", f"{base}:.github/release-approvers.txt"],
                cwd=ROOT, text=True, stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            content = ""
    if not content:
        on_disk = ROOT / ".github" / "release-approvers.txt"
        if on_disk.is_file():
            content = on_disk.read_text(encoding="utf-8")
        else:
            return None

    out: set[str] = set()
    for raw in content.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line == "__RA_HANDLE__":
            # Unseeded sentinel: not a real handle.
            continue
        out.add(line.lstrip("@").lower())
    return out or None


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------

def _run() -> int:
    r = Reporter("release-integrity")
    allow = load_allowlist()
    changed = _read_changed_paths()
    pr_body = _read_pr_body()
    _check_release_integrity(r, changed)
    _check_sign_off(r, changed, pr_body, allow)
    return r.finish()


if __name__ == "__main__":
    sys.exit(main_guard(_run))
