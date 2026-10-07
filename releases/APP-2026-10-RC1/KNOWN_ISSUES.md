# APP-2026-10-RC1 — Known Issues

This file lists items known at tag time that are deliberately deferred for Working Group resolution, follow-up baselines, or coordination with downstream decisions. Each item is also opened as a GitHub Issue after publication for public tracking and comment.

Known Issue identifiers (`KI-nn`) are stable across baselines; each issue is closed only when a Decision Record or merged change resolves it.

## KI-01 — Plain Language Guide gap (APP-0, APP-1, APP-5)

- **Affects:** Non-technical readership orientation to Objectives, Constitution, and Conformance Profiles.
- **Status:** Open.
- **Description:** The current baseline publishes Plain Language Guides for APP-2, APP-3, APP-4, and a suite-wide overview. No Plain Language Guides exist for APP-0, APP-1, or APP-5. Non-technical readers approaching Objectives, Constitution, or Conformance Profiles have no plain-language entry point.
- **Resolution path:** Editorial work; targeted for a follow-up baseline. Not blocking adoption of this baseline for implementers using the Specification directly.

## KI-02 — Contribution Terms "Effective date" pending

- **Affects:** `legal/APP_Contribution_Terms_v0_2.md`.
- **Status:** Open — counsel.
- **Description:** The Contribution Terms carry `Effective: [TBD — set at first publication of the APP repository]`. The repository is now published. The decision of what event triggers Contribution Terms effectiveness (first baseline tag? First merged contribution? An express notice?) and any interim-period notice between the WP2 scaffold merge and this tag is a legal-instrument question that has been referred to counsel (counsel question Q2 in the pre-publication counsel pack).
- **Resolution path:** Counsel response → Contribution Terms v0.3 PR → next baseline.

## KI-03 — Privacy Notice "Effective date" pending

- **Affects:** `legal/APP_Consultation_Privacy_Notice_v0_3.md`.
- **Status:** Open — counsel.
- **Description:** The Privacy Notice carries `Effective date: [TBD]`. Setting the effective date requires that (a) the privacy@agenticprocess.org delivery path is verified live, and (b) the retention and rights workflows named in the notice are operationally staffed. Deliverability test for the shared mailbox is a Package 4 activity; retention and rights workflow is a Working-Group formation item.
- **Resolution path:** Mailbox delivery test + minimal operational workflow → Privacy Notice v0.4 PR with the effective date set → next baseline.

## KI-04 — csl/Governance.md and csl/Notices.md not frozen into baseline directory

- **Affects:** `csl/Governance.md`, `csl/Notices.md` on the default branch.
- **Status:** Deliberate — not an open issue, documented for implementer clarity.
- **Description:** This baseline freezes only `csl/Scope.md` into the baseline directory, because Scope is the §9.13 Necessary Claims boundary that must be captured at tag for non-retroactivity. Governance.md (Draft→Approved process) and Notices.md (append-only acceptance/exclusion/withdrawal ledger) remain live at `/csl/` on the default branch; a point-in-time view is available by checking out the Git tag `APP-2026-10-RC1`.
- **Resolution path:** Not required; recorded here to pre-empt confusion.

## KI-05 — Full suite Approved-Specification transition

- **Affects:** Whole suite.
- **Status:** Open — Working Group.
- **Description:** The suite is published as a Draft Specification under CSL 1.0 §9.6. Transition to Approved Specification (CSL 1.0 §9.2) requires the Draft→Approved process set out in `csl/Governance.md` and ratification by the Working Group once formed. The Working Group is not yet formed; interim governance applies.
- **Resolution path:** Working Group formation under Charter v0.4 → ratification process → next-but-one or later baseline.

## KI-06 — Published schema evolution path

- **Affects:** `schemas/frame/`.
- **Status:** Open — Working Group.
- **Description:** APP-R1 Process Frame Schema v0.3.0 is published in this baseline as an Illustrative Reference. The decision of whether to adopt it as the CORE-A1-05 published Frame schema (promoting it from Illustrative to Normative), or to retain alternative-realisation freedom, is a Working-Group decision. Until that decision, APP-R1 does not create a conformance obligation.
- **Resolution path:** Working Group deliberation → schema evolution PR (either adoption as normative or formal retention as illustrative) → future baseline.

## KI-07 — Scope.md successor-document route under §2

- **Affects:** `csl/Scope.md` §2 Specification documents list.
- **Status:** Open — Working Group.
- **Description:** `csl/Scope.md` §2 refers to a successor-document route by which a baseline may add or amend Specification documents within the Scope boundary. The precise procedural wording of that route is tied to Working-Group governance, not interim governance. Current wording is adequate for interim operation but will be reviewed on WG formation.
- **Resolution path:** Working Group review of §2 wording → Scope.md v0.4 PR → next baseline.

## KI-08 — MCP binding reference code

- **Affects:** `reference/mcp-server/`.
- **Status:** Open — follow-up release.
- **Description:** APP-R2 MCP Binding Reference Design v0.3 Draft is published in this baseline as a design document. Reference code (a working MCP server implementing the binding) is not yet published. Reference code is a separate workstream from the design document and will be published under `reference/mcp-server/` in a follow-up release once an implementation passes the APP-5 CONF-T-02 vectors against a running instance (per APP-R2 §8).
- **Resolution path:** Implementation + CONF-T-02 pass → reference-code PR → future baseline.

## KI-09 — Interim-approval differential enforcement audit

- **Affects:** Repository `main` branch ruleset.
- **Status:** Open — operational.
- **Description:** The interim approval policy requires `1 approval + CODEOWNER + status checks` across all main-branch PRs, with an **additional** Release Approver sign-off enforced by the `release-integrity` required status check for PRs touching `/releases/**`, `/csl/**`, `/legal/**`, `/schemas/**`, `/reference/**`, or normative-document paths. First baseline is the first exercise of this check at full scope; audit after N real PRs confirms it is behaving as designed, and the `main` ruleset is activated per Work Package 4 of the GitHub Custodian Runbook.
- **Resolution path:** First N post-baseline PRs → audit of actual check behaviour → Work Package 4 ruleset activation. Tracked on the Custodian Dashboard until closed.

## KI-10 — Public consultation first window

- **Affects:** Baseline reception and ratification posture.
- **Status:** Open — Working-Group formation precondition.
- **Description:** Charter v0.3 §2 and the Working-Group formation triggers in the Runbook §11 require a first public consultation window to have closed with a decision record for material comments. The window opens with publication of this baseline. No decision record exists yet.
- **Resolution path:** Open consultation window → closing date set per Working Group formation plan → decision record for material comments → `/decisions/APP-DEC-00NN.md` → Working-Group formation.

## How to raise additional known issues

Use the repository Issue Forms:

- `.github/ISSUE_TEMPLATE/documentation-defect.yml` for defects
- `.github/ISSUE_TEMPLATE/clarification.yml` for ambiguity-only questions
- `.github/ISSUE_TEMPLATE/normative-proposal.yml` for proposed normative changes
- `.github/ISSUE_TEMPLATE/implementation-experience.yml` for implementation feedback

Open an issue on the main repo rather than in this baseline's directory. The release directory is immutable.

---

*End of KNOWN ISSUES for APP-2026-10-RC1.*
