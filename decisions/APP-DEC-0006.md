# APP-DEC-0006 — Interim rules for release content: content screen, per-artefact clearance, public-source citations

| Field | Value |
|:---|:---|
| Decision number | APP-DEC-0006 |
| Date | 2026-10-24 |
| Status | Accepted |
| Decided by | Vaidhya, Release Approver (Interim Custodian) |
| Applies from | The next coordinated baseline after APP-2026-10-RC1, and every baseline after it |
| Instruments affected | Release preparation (Runbook §2.4); accompanying-artefact publication clearance; review of every pull request (Runbook §2.2) |
| Related | APP-DEC-0002 §4 (RC1 composition and clearance); PR #20 (citations removed from the working drafts); PR #21 (reference-hygiene validator, draft) |

APP-DEC-0005 is reserved for the Phase 2.5 decision on publishing the governance documents.

## Decision

Three rules apply now as interim operating rules. Runbook v1.3 (Phase 3) adopts them unchanged, and the Phase 3 scope is extended to include them.

### Rule 1 — Content screen before every release PR

1. Before a release PR is marked ready, the Custodian runs the reference-hygiene check over the release branch, comparing it with `main`. The check covers every file added under `/releases/<baseline>/`: specification, guides, legal copies and accompanying artefacts.
2. The result must be **0 errors**.
3. The release PR body records, under a *Content screen* heading:
   - the commit SHA screened;
   - the error and warning counts;
   - for each warning: the file, the pattern class and its disposition.

   The matched text itself is never pasted into the PR body.
4. The Release Approver confirms that the *Content screen* section is complete before signing off.

Until the reference-hygiene validator (PR #21) is on `main`, the Custodian runs it from that pull request's branch.

### Rule 2 — Publication clearance per artefact

1. Each accompanying-artefact version listed in a release manifest has its own clearance entry. This covers each schema version under `/schemas/` and each reference-design version under `/reference/`.
2. Each entry states:
   - the artefact path and version;
   - the SHA-256 of every file cleared;
   - the content-screen result for those files;
   - the Release Approver's name and the date.
3. Clearance entries are kept apart from the baseline composition decision. One clearance record per release may hold one section per artefact.
4. Before preparing a release merge, the Custodian checks that every artefact in the manifest's *Accompanying artefacts* section has a clearance entry with matching version and hashes. The Custodian checks that the record exists; it does not assess clearance.

### Rule 3 — Provenance text cites only public sources

Change tables, version histories, notes and rationale digests in any file destined for this repository cite only sources a public reader can open:

- APP documents;
- public decision records;
- Issues and pull requests;
- public external references.

Review provenance that is not public stays outside the repository. If a change can only be understood through such provenance, the public text is rewritten so that it stands on its own. The Custodian applies this rule when reading every diff.

## Rationale

- Provenance text in the published APP-2026-10-RC1 baseline cited sources a public reader cannot open. The citations are in an informative rationale appendix, a classification note and the change tables of the two accompanying artefacts. No requirement text is affected. The release directory is immutable, so the working drafts were corrected instead (PR #20). The accompanying artefacts are corrected in their next versions.
- At RC1, publication clearance for both accompanying artefacts was recorded inside the composition decision (APP-DEC-0002 §4), so their change tables were never screened separately. Rule 2 removes that path. Rule 1 screens the release content mechanically, and Rule 3 states the standard the screen enforces.

## Follow-ups (separate decisions)

- One line in `CONTRIBUTING.md` stating Rule 3 for contributors.
- One entry in the Custodian Instructions *Never-in-repo* list for citations to sources a public reader cannot open.
