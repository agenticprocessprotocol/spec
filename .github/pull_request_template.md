<!--
Welcome, and thank you for the pull request.

Please complete the sections below. Required-check validators will fail
if the required sections are empty or still contain the template
placeholders.

For questions, see /CONTRIBUTING.md.
-->

## Summary

<!-- One or two sentences on what this PR does. -->

## Change classification

<!-- Tick exactly one. Classification determines which validators and
     approval thresholds apply. See /GOVERNANCE.md §2 for the rules. -->

- [ ] **Editorial** — typos, formatting, cross-reference target fixes that do not change meaning
- [ ] **Normative** — modifies a requirement, an RFC 2119/8174 keyword, a conformance obligation, a protocol invariant, a security outcome, or an interpretation affecting implementation or conformance
- [ ] **Schema** — adds, modifies, or deprecates a schema under `/schemas/**`
- [ ] **Scope** — modifies `csl/Scope.md` (IP-relevant; see Scope §7)
- [ ] **Legal / CSL companion** — modifies `/legal/**`, `csl/Governance.md`, or `csl/Notices.md`
- [ ] **Release** — change under `/releases/APP-YYYY-MM-RCn/`
- [ ] **Operations** — workflows, CODEOWNERS, OPERATIONS-REGISTRY, SECURITY-AUTOMATION
- [ ] **Other** — explain:

## Linked issue(s)

<!-- For normative, scope, and schema changes: link the originating issue.
     Normative proposals must begin as a `normative-proposal` Issue Form. -->

Closes #

## Change-impact manifest

<!-- Required for Normative changes. For other classifications, write N/A.
     The manifest is a file at /changes/APP-XXXX.md covering the nine
     fields from APP-1 §4. Template: /changes/_TEMPLATE.md -->

Change-impact manifest path: `/changes/APP-____.md`

## DCO sign-off

<!-- Every commit in this PR must carry a Signed-off-by: trailer.
     See /CONTRIBUTING.md §3 for how to sign off (CLI and web UI).
     The DCO check will fail otherwise. -->

- [ ] All commits in this PR are signed off per the Developer Certificate of Origin 1.1.
- [ ] If this PR implements an idea originated by someone who could not sign off, that person is credited in the PR description above and in the CHANGELOG entry (per `/CONTRIBUTING.md` §3.3).

## AI-authorship disclosure

<!-- See /CONTRIBUTING.md §4 for the disclosure test. Ordinary grammar
     checkers, autocomplete, and translation do NOT require disclosure.
     Substantive normative wording, rationale, or test content generated
     by an AI and NOT independently reviewed does require disclosure. -->

- [ ] No material AI-generated substantive normative wording, rationale, technical analysis, or test content is included that I have not independently reviewed and validated.

OR

- [ ] This PR includes material AI-generated content; the following summarises what and how I reviewed it:

<!-- If the second box is ticked, describe here. -->

## Personal-data acknowledgement

<!-- See /SECURITY.md §4 (Never-in-repo list) for the categories. -->

- [ ] This PR does not include personal data of third parties, sensitive personal data (including of myself where not already public under my chosen GitHub identity), off-platform-collected personal data, credentials, third-party content without a licence check, Interim-Custodian internal material, or any other category listed under *Never-in-repo* in `/SECURITY.md`.

## Required checks

<!-- The following checks are run automatically. The Custodian cannot
     prepare merge until all pass. -->

- [ ] DCO
- [ ] `validate-spec` (manifest, legacy-name, keyword, cross-reference)
- [ ] `validate-schemas` (if PR touches `/schemas/**`)
- [ ] `links`
- [ ] `release-integrity` (if PR touches `/releases/**` or any class requiring Release Approver sign-off below)

---

## Release Approver sign-off

<!-- REQUIRED for the following classes of change:
       - Release (change under /releases/APP-YYYY-MM-RCn/)
       - Scope (change to csl/Scope.md)
       - Legal / CSL companion (change to /legal/**, csl/Governance.md, csl/Notices.md)
       - Schema or reference design (change under /schemas/**, /reference/**)
       - Normative (any of the triggers in Change classification above)

     For editorial and other changes, write "N/A — classification does
     not require Release Approver sign-off" in each field.

     This section is verified by the `release-integrity` check. Empty
     fields on a class that requires sign-off will fail the check.

     Where the Release Approver is also an editor, the Editor approval
     (GitHub review) and this sign-off are DISTINCT governance acts and
     are recorded SEPARATELY. Both are required. -->

- **I am the Release Approver and I sign off on this change:** <!-- Name -->
- **Date:** <!-- YYYY-MM-DD -->
- **Classification sign-off applies to:** <!-- one of: Release / Scope / Legal / Schema / Reference / Normative / N/A -->
- **Decision record (if applicable):** <!-- /decisions/APP-DEC-XXXX.md or N/A -->
- **Confirming:**
  - [ ] Change-impact manifest reviewed and acceptable (for Normative; otherwise N/A).
  - [ ] Linked decision record is current (or N/A).
  - [ ] No open escalations block merge (per `/GOVERNANCE.md` §7).

<!-- End of PR template. -->
