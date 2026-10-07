# APP-DEC-0003 — Known Issues disposition at APP-2026-10-RC1 publication

| Field | Value |
|:---|:---|
| Decision number | APP-DEC-0003 |
| Date | 2026-10-07 |
| Status | Accepted |
| Decided by | Vaidhya, Release Approver (Interim Custodian) |
| Instruments affected | `/releases/APP-2026-10-RC1/KNOWN_ISSUES.md` (reference); GitHub Issue tracker; `/legal/APP_Contribution_Terms_v0_3.md`; `/legal/APP_Consultation_Privacy_Notice_v0_4.md`; `/legal/REVIEW-STATUS.md` |
| Related decisions | APP-DEC-0001 (coordinated baseline initiation), APP-DEC-0002 (RC1 baseline composition) |

## Decision

The ten Known Issues listed in `/releases/APP-2026-10-RC1/KNOWN_ISSUES.md` are opened as GitHub Issues per the commitment in that file. Of the ten:

- **Five are closed at creation** as resolved-at-publication, with resolution comments cross-referenced to this record and to the resolving instruments.
- **Five remain open** as live tracked items for Working Group formation, operational activation, or follow-up releases.

The frozen `KNOWN_ISSUES.md` file in the baseline directory is **unchanged**. It stands as the historical record of what was known at tag time (2026-10-07). This Decision Record and the GitHub Issue tracker are the current-state view.

## Rationale

Four of the ten Known Issues were drafted before the Interim Custodian's position on the underlying question was finalised; publishing them as "open" would misrepresent current state. One (KI-04) was already labelled "deliberate — not an open issue" in the baseline file itself. Converting all ten into Issues without filtering would create credibility noise for the AAIF CTO and analyst audiences who read the live Issue tracker as a signal of project maturity.

Closing resolved items at creation preserves the audit trail (the Issues exist, their resolution is documented) without inflating the live-work count.

## Active Known Issues

The following five Known Issues remain open after this disposition. Each is tracked as a GitHub Issue with the `known-issue` label; items requiring Working Group deliberation also carry the `needs-WG-decision` label.

### KI-05 — Full suite Approved-Specification transition

**Status at RC1:** Open. Working Group not yet formed; interim governance applies. Transition from Draft Specification (CSL 1.0 §9.6) to Approved Specification (§9.2) requires the Draft→Approved process in `csl/Governance.md`. Closed only when the Working Group is formed, convenes under Charter v0.4+, and ratifies the suite.

### KI-07 — Scope.md successor-document route under §2

**Status at RC1:** Open. Current `csl/Scope.md` §2 wording is adequate for interim operation. The procedural wording for the successor-document route is a Working-Group governance decision deferred to post-formation review. Closed when WG ratifies §2 wording.

### KI-08 — MCP binding reference code

**Status at RC1:** Open. APP-R2 MCP Binding Reference Design v0.3 Draft is published as an Illustrative Reference in this baseline. Reference code (a working MCP server implementing the binding) is a separate workstream, scheduled for a follow-up release once an implementation passes the APP-5 CONF-T-02 vectors per APP-R2 §8. Closed when reference code is published.

### KI-09 — Interim-approval differential enforcement audit

**Status at RC1:** Open. Operational tracking. The interim approval policy (1 approval + CODEOWNER + status checks + Release Approver sign-off for sensitive paths) is being exercised on live PRs post-baseline. Audit of actual check behaviour after a cohort of real PRs informs Package 4 (`main` ruleset activation). Closed when Package 4 activation decision is recorded.

### KI-10 — Public consultation first window

**Status at RC1:** Open. Working-Group formation precondition per Charter v0.3 §2 and Runbook §11. The consultation window opens with publication of this baseline. Closed when the window closes with a Decision Record disposing of material comments.

---

## Appendix A — Closed Known Issues (resolved at RC1 publication)

The following five Known Issues are closed at creation. Each is created as a GitHub Issue with the `known-issue` and `resolved-at-publication` labels, with the resolution comment pointing to this record and to the resolving instrument.

### KI-01 — Plain Language Guide gap (APP-0, APP-1, APP-5)

**Original concern:** No standalone Plain Language Guides for APP-0, APP-1, or APP-5.

**Resolution:** Closed — resolved by design. The suite-level `APP_Plain_Language_Guide_v0_1.md` (published at RC1) provides a plain-language orientation to APP-0 Protocol Objectives (dedicated §5 sub-section + full §4 "The Five Outcomes"), APP-1 Protocol Constitution (dedicated §5 sub-section with precedence ladder), and APP-5 Conformance Profiles (dedicated §5 sub-section with L1-L4 maturity levels and example conformance claims). The dedicated APP-2, APP-3, and APP-4 Plain Language Guides exist because those documents have greater technical complexity warranting standalone companions; APP-0, APP-1, and APP-5 are structurally more concise and the suite-level treatment is appropriate.

**Reopen criterion:** Expert-review or implementer feedback identifies a specific orientation gap for one of APP-0, APP-1, or APP-5 that the suite PLG does not address.

### KI-02 — Contribution Terms "Effective date" pending

**Original concern:** Contribution Terms v0.2 carried `Effective: [TBD]`.

**Resolution:** Closed — resolved by Contribution Terms v0.3 (`/legal/APP_Contribution_Terms_v0_3.md`), which sets Effective: 2026-10-07 coincident with the APP-2026-10-RC1 tag. Trigger event (first baseline tag) was decided by the Release Approver; no counsel review was required for this operational trigger. Structural review items concerning the Interim Custodian IP posture are documented separately in `/legal/REVIEW-STATUS.md` and are deferred to Successor Foundation (AAIF) matriculation discussion.

**Reopen criterion:** Successor Foundation review identifies a structural issue with the Effective date trigger that requires revision.

### KI-03 — Privacy Notice "Effective date" pending

**Original concern:** Privacy Notice v0.3 carried `Effective date: [TBD]`.

**Resolution:** Closed — resolved by Privacy Notice v0.4 (`/legal/APP_Consultation_Privacy_Notice_v0_4.md`), which sets Effective date: 2026-10-07. `privacy@agenticprocess.org` is a live mailbox on the Vach M365 tenant with delivery verified per OPERATIONS-REGISTRY.md. GDPR review of the Charter and Privacy Notice is a parallel workstream handled by Vach's privacy counsel; it is not a precondition to the effective date for Draft Specification consultation.

**Reopen criterion:** GDPR review or Successor Foundation review identifies a defect that requires revision.

### KI-04 — csl/Governance.md and csl/Notices.md not frozen into baseline directory

**Original concern:** Clarification of why only `csl/Scope.md` is frozen into the baseline directory.

**Resolution:** Closed — not an issue. The original baseline file labelled this as "Deliberate — not an open issue, documented for implementer clarity". Only `csl/Scope.md` is frozen because it is the §9.13 Necessary Claims boundary that must be captured at tag for CSL 1.0 non-retroactivity. `csl/Governance.md` (Draft→Approved process) and `csl/Notices.md` (append-only ledger) remain live at `/csl/`; point-in-time view is available by checking out the Git tag.

**Reopen criterion:** None expected; this is a design clarification.

### KI-06 — Published schema evolution path

**Original concern:** Decision pending on whether APP-R1 Process Frame Schema should be promoted from Illustrative to Normative (CORE-A1-05 published schema).

**Resolution:** Closed — resolved by APP-1 Protocol Constitution v1.5 §4, which introduces the three-tier taxonomy (Normative Specification: APP-0 through APP-5; Informative Specification: APP-IG-01 through APP-IG-05; Illustrative Reference: APP-R-nn). APP-R1 Process Frame Schema v0.3.0 is confirmed as an Illustrative Reference in this baseline. Implementations may deliver equivalent conformance via alternative realisations. Future adoption of APP-R1 (or a successor) as a normative schema is a Working Group decision; it is not an open resolution path, and APP-R1's current status does not create a conformance obligation.

**Reopen criterion:** Working Group decides to promote APP-R1 (or a successor) to Normative status, triggering a schema-change path PR.

---

## Appendix B — Disposition summary table

| KI | Topic | Disposition | GitHub Issue state | Resolution ref |
|:---|:---|:---|:---|:---|
| KI-01 | PLG gap APP-0/1/5 | Closed — resolved by design | Closed at creation | Suite PLG v0.1 §4, §5 |
| KI-02 | Contribution Terms effective date | Closed — resolved | Closed at creation | Contribution Terms v0.3 |
| KI-03 | Privacy Notice effective date | Closed — resolved | Closed at creation | Privacy Notice v0.4 |
| KI-04 | csl/ files frozen scope | Closed — not an issue | Closed at creation | KNOWN_ISSUES.md KI-04 (deliberate label) |
| KI-05 | Approved Specification transition | Open | Open | WG formation |
| KI-06 | Schema evolution path | Closed — resolved | Closed at creation | APP-1 v1.5 §4 three-tier taxonomy |
| KI-07 | Scope §2 successor-document route | Open | Open | WG review |
| KI-08 | MCP reference code | Open | Open | Follow-up release |
| KI-09 | Ruleset activation audit | Open | Open | Package 4 |
| KI-10 | Public consultation first window | Open | Open | WG precondition |

**Totals:** 5 closed, 5 open.

---

*Decided and recorded by Vaidhya, Release Approver, 2026-10-07.*
