# APP-DEC-0001 — Adoption of Work Package 2 public governance scaffold

**Decision date:** <YYYY-MM-DD — set at PR merge>
**Decision maker:** Vaidhya (Release Approver, interim custodian — Vach AI Limited)
**Supersedes:** none
**Status:** Proposed — becomes Accepted when the Work Package 2 PR is merged.

---

## Context

The `agenticprocessprotocol/spec` repository was established as an empty public repository in Work Package 1 (identity and access — organisation, teams, 2FA, co-maintainer path confirmed). Work Package 2 adds the public governance scaffold — the files that make the repository usable for public consultation under the Community Specification License 1.0 (CSL 1.0) adopted verbatim by the APP Contribution Terms v0.2.

This decision records the adoption of that scaffold as the governance baseline for public consultation.

## Decision

Adopt the scaffold contained in the Work Package 2 bundle, consisting of:

- Root policy files: `README.md`, `LICENSE` (CSL 1.0 verbatim, byte-identical to APP Contribution Terms Appendix A), `CONTRIBUTING.md`, `GOVERNANCE.md`, `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1 verbatim), `SECURITY.md`, `SECURITY-AUTOMATION.md`, `CHANGELOG.md`, `OPERATIONS-REGISTRY.md`.
- CSL 1.0 companion files under `/csl/`: `Scope.md` (verbatim from APP Scope v0.3), `Governance.md`, `Notices.md`.
- Apache-2.0 licence files for accompanying artefact directories: `/schemas/LICENSE`, `/reference/LICENSE`, `/tools/LICENSE`.
- GitHub configuration under `.github/`: `CODEOWNERS` (ownership matrix per Custodian Instructions §5), `pull_request_template.md` (with Release Approver sign-off block for differential approval per §4), `dependabot.yml`.
- Four Issue Forms plus `config.yml`: `documentation-defect`, `clarification`, `normative-proposal`, `implementation-experience`.
- Four CI workflows: `validate-spec`, `links`, `validate-schemas`, `release-integrity` (with third-party actions pinned to commit SHA).
- Six validator scripts under `.github/scripts/` plus `common.py`, `allowlist.yml`, and `requirements.txt`.
- `/changes/_TEMPLATE.md` for change-impact manifests.
- This decision record.

## Rationale

1. **CSL 1.0 operability requires the three `/csl/` companion files.** `Scope.md` bounds Contributor Necessary Claims (§9.13); without it, patent commitments collapse to each Contributor's own contributions. `Governance.md` defines the Draft → Approved transition (§9.2). `Notices.md` is the mechanism for acceptance, exclusion, and withdrawal notices (§§2.1.3.3, 2.3, 3).
2. **LICENSE must be byte-identical to Contribution Terms Appendix A** so that there is no ambiguity about which text governs. Any divergence between LICENSE and the Contribution Terms would create a legal interpretation question we have no reason to invite.
3. **Dual-sign-off differential approval is implemented via `release-integrity`** check, not via multiple branch-protection rules, because GitHub branch rulesets do not support path-aware differential approval counts natively.
4. **Validators are repo-local Python scripts** rather than third-party GitHub Apps, keeping the supply-chain surface minimal at launch. The one third-party App (Probot DCO) is subject to the admission checklist in `SECURITY-AUTOMATION.md` §2 at Package 4 installation.
5. **The `csl/Scope.md` adopted here is Draft and not effective** until included in a named, tagged coordinated APP baseline (Package 3). This decision adopts the file into the repository; it does not make it effective as a Scope statement.
6. **Co-maintainer path confirmed per §4 Option A.** Bhavna Krishnan in `@agenticprocessprotocol/editors`, 2FA enabled, invite accepted. Package 4 ruleset activation remains gated on this condition continuing to hold.

## Consequences

### Positive

- Repository is usable for public consultation on APP Draft Specifications.
- Governance posture (dual sign-off, CODEOWNERS matrix, validator coverage) satisfies the Custodian Instructions.
- Matriculation to a Successor Foundation is simplified: all governance artefacts are in-repo rather than in a private inbox.
- Record-keeping — Operations Registry, Decisions log — is set up to track every subsequent change.

### Carry-forward items (not resolved in this decision)

The following issues are known at adoption and are explicitly deferred to Work Package 3:

1. **Baseline reference in `APP_Contribution_Terms_v0_2.md`** cites `APP-2026-09-RC2`; the current target baseline is `APP-2026-10-RC1`. Correct before the first baseline tag.
2. **End-of-document version label in APP Scope v0.3** reads "End of APP Scope v0.2." (header reads v0.3). The file is copied verbatim into `csl/Scope.md`; the typo carries forward and is corrected in the next Scope revision.
3. **Four counsel questions** (Q1–Q4 per project tracking) are not resolved at this decision and are deferred to counsel engagement in parallel with Work Package 3.
4. **Suite baseline version mismatch across spec documents** is a Work Package 3 issue, not a Work Package 2 issue.
5. **Broken cross-reference in APP-5 citing non-existent APP-4 §3.4.5** is a Work Package 3 issue.

Each of the above becomes its own decision record in `/decisions/` when resolved.

### Risks

- **SHA pins on third-party actions were set from best-known-good values at bundle preparation time.** If any SHA is incorrect, the first PR run surfaces the mismatch as a workflow-not-found error; recoverable via a trivial `str_replace` PR. Dependabot keeps the pins current afterward.
- **Validators have been self-tested but have not run on this repository's CI.** First real exercise is this Work Package 2 PR itself; any CI-specific environment issues surface on the PR run.

## Related

- Work Package 1 completion: logged in Appendix A of `APP_GitHub_Runbook_v1_1.md`.
- Work Package 2 preparation: this decision.
- Work Package 3 (baseline publication): will reference this decision in `MANIFEST.md`.
- Working Group formation trigger: `GOVERNANCE.md` §5.

---

*Decision records are append-only. If this decision is later superseded, add a new record referencing this one; do not edit this file.*
