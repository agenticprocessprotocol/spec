#!/usr/bin/env python3
"""validate_dco.py — every commit in a pull request carries a DCO sign-off.

The Developer Certificate of Origin 1.1 is certified by a trailer line in
the commit message:

    Signed-off-by: Full Name <email@example.org>

Checks (pull_request events only):
  * Every non-merge commit in BASE_SHA..HEAD_SHA has at least one
    well-formed `Signed-off-by: Name <email>` trailer.          -> error
  * At least one sign-off on each commit names the commit author's email
    or name.                                                     -> warning
    (Advisory: GitHub noreply addresses, bots and role identities often
    differ from the author field.)

Merge commits are skipped: they carry no new content of their own.
On push or workflow_dispatch there is no PR range, so the check is a no-op.

Commit message text is never printed: commit messages are untrusted input,
and only the commit SHA and a sanitised author name appear in the log.

How to fix a failure: see CONTRIBUTING.md §3 (`git commit --amend --signoff`,
or add the trailer in the web editor's extended description).
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ROOT, Reporter, main_guard

SIGNOFF = re.compile(r"^Signed-off-by:[ \t]+(?P<name>[^<>\r\n]*?\S)[ \t]+<(?P<email>[^<>@\s]+@[^<>\s]+)>[ \t]*$", re.MULTILINE)
SIGNOFF_ANY = re.compile(r"^Signed-off-by:", re.MULTILINE | re.IGNORECASE)
SEP = "\x1e"  # record separator between commits
FS = "\x1f"   # field separator within a commit


def _safe(text: str) -> str:
    """Printable, single-line, no leading workflow-command markers."""
    text = "".join(ch for ch in text if ch.isprintable())
    return text.replace("::", ": :")[:80]


def _commits(base: str, head: str) -> list[dict]:
    fmt = FS.join(["%H", "%P", "%an", "%ae", "%B"]) + SEP
    out = subprocess.check_output(
        ["git", "log", f"--format={fmt}", f"{base}..{head}"],
        cwd=ROOT, text=True, errors="replace",
    )
    commits = []
    for rec in out.split(SEP):
        rec = rec.lstrip("\n")
        if not rec.strip():
            continue
        sha, parents, name, email, body = (rec.split(FS, 4) + [""] * 5)[:5]
        commits.append({
            "sha": sha.strip(),
            "parents": parents.split(),
            "name": name.strip(),
            "email": email.strip().lower(),
            "body": body,
        })
    return commits


def _run() -> int:
    r = Reporter("dco")
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    base = os.environ.get("BASE_SHA", "")
    head = os.environ.get("HEAD_SHA", "") or "HEAD"

    if event != "pull_request" or not base:
        print("dco: no pull_request range; nothing to check")
        return r.finish()

    commits = _commits(base, head)
    checked = 0
    for c in commits:
        short = c["sha"][:7]
        if len(c["parents"]) > 1:
            print(f"dco: {short} is a merge commit; skipped")
            continue
        checked += 1
        signoffs = [(m.group("name").strip(), m.group("email").strip().lower()) for m in SIGNOFF.finditer(c["body"])]
        if not signoffs:
            if SIGNOFF_ANY.search(c["body"]):
                r.error(f"commit {short} (author {_safe(c['name'])}): Signed-off-by trailer is malformed; "
                        f"expected 'Signed-off-by: Full Name <email>'. See CONTRIBUTING.md §3.")
            else:
                r.error(f"commit {short} (author {_safe(c['name'])}): no Signed-off-by trailer. "
                        f"Add one with 'git commit --amend --signoff' (see CONTRIBUTING.md §3).")
            continue
        names = {n.lower() for n, _ in signoffs}
        emails = {e for _, e in signoffs}
        if c["email"] not in emails and c["name"].lower() not in names:
            r.warn(f"commit {short}: no sign-off names the commit author's email or name "
                   f"(author {_safe(c['name'])}); sign-off present.")

    print(f"dco: checked {checked} commit(s) in {base[:7]}..{head[:7] if head != 'HEAD' else 'HEAD'}")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main_guard(_run))
