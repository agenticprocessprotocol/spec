# CSL 1.0 Governance Companion

**Version:** 0.1 Draft
**Status:** Draft — not effective until this file is included, at a specific version, in a named, tagged coordinated APP baseline. Until that inclusion, the Specification exists only as Draft Specification under CSL 1.0.
**Purpose:** This file is the `Governance.md` companion required by the **Community Specification License 1.0** (CSL 1.0). CSL 1.0 §9.2 defines an **Approved Specification** by reference to "the accompanying Governance.md file." This file provides that reference for the Agentic Process Protocol ("APP").

> This file governs the CSL 1.0 **Draft → Approved** transition only. The broader community governance of the repository — roles, review process, decision authority, Working Group formation trigger — is in [`/GOVERNANCE.md`](../GOVERNANCE.md). The two are kept separate because CSL 1.0 refers to this one by name.

---

## 1. Current status of the Specification

As of the version of this file in the current baseline, all APP documents in the suite identified in [`csl/Scope.md`](Scope.md) §2 have the status of **Draft Specification** under CSL 1.0 §9.6. **No APP document has been designated an Approved Specification.**

Draft Specification status provides the Draft-Specification patent grants under CSL 1.0 §2.1.1.1 and §2.2(1). The Approved-Specification grants under CSL 1.0 §2.1.1.2 and §2.2(2) apply only when and if a document is designated Approved under §3 below.

---

## 2. Interim-custody posture

APP is under **interim custody** by Vach AI Limited pending matriculation to a Successor Foundation. During interim custody there is no Working Group with ratified membership rules; decision authority on normative changes rests with the Release Approver, who signs off per [`/GOVERNANCE.md`](../GOVERNANCE.md) §2.

**No designation of Approved Specification is made during interim custody.** The Approved-Specification designation is reserved for the Working Group's quorum procedure after Working Group formation (see §4). The project maintains well-tagged, well-manifest-controlled Draft Specifications under coordinated baselines (e.g., `APP-2026-10-RC1`); these are citable, versioned Draft Specifications under CSL 1.0 and have the Draft-Specification patent grants attached.

---

## 3. Approval process — to be used after Working Group formation

Once the Working Group is formed (see §4), the designation of a Draft Specification as an **Approved Specification** proceeds as follows:

### 3.1 Candidate selection

- A Draft Specification is proposed for Approved designation by a sponsoring editor via a pull request to this file, adding the proposed candidate to §5.
- The candidate must be a tagged coordinated baseline: a specific tag, a specific manifest, and a specific set of document versions.

### 3.2 Public review window

- The candidate is announced in GitHub Discussions and on the project website, and remains open for public comment for **no less than thirty (30) calendar days** before the designation vote.
- Material comments received in the window are addressed on the record. The specific disposition of each is recorded under `/decisions/`.

### 3.3 Approval vote

- The designation decision is a **supermajority vote of the Working Group** — specifically, approval by **two-thirds (2/3) of Working Group Members entitled to vote**, with a quorum of **at least half (50%)**, in the vote mechanism established by the Working Group under the Charter v0.4 or later.
- Approval must be of the specific tagged baseline, specific manifest, and specific document versions.
- Members may vote against or abstain. No single Member has a veto.

### 3.4 Exclusion window

- CSL 1.0 §3.2 permits a Contributor to issue an Exclusion Notice prior to a Draft Specification becoming Approved. The project operates an **Exclusion window of no less than thirty (30) calendar days** following the approval vote and preceding the Approved designation taking effect, during which Contributors may file Exclusion Notices into `csl/Notices.md`.
- Where an Exclusion Notice is filed in the window, the Working Group may elect to proceed, to re-draft, or to re-vote. The chosen path is recorded under `/decisions/`.

### 3.5 Designation

- If no eligible Exclusion Notice is filed in the §3.4 window, or the Working Group elects to proceed, the Release Approver (or the Working Group's designated signer after matriculation) creates the Approved Specification designation by:
  - Updating this file §6 Version History to record the approval.
  - Updating [`csl/Notices.md`](Notices.md) with the designation entry.
  - Updating `/releases/<baseline-id>/RELEASE-NOTES.md` to show Approved status.
  - Tagging the baseline accordingly (naming convention `APP-<year>-<month>-APPROVED-<n>` or equivalent, decided at Working Group formation).
- From that point, the baseline's documents have the status of **Approved Specification** under CSL 1.0 §9.2 and the Approved-Specification patent grants under §2.1.1.2 and §2.2(2) attach.

### 3.6 Scope at designation

The patent-licensing commitments at Approval are bounded by the version of [`csl/Scope.md`](Scope.md) included in the approved baseline's manifest. Changes to Scope made after approval do not apply retroactively to that approved baseline (CSL 1.0 §9.13).

---

## 4. Working Group formation prerequisites

Section 3 is only effective once the Working Group is formed. Formation requires **all** of the following, as recorded in [`/GOVERNANCE.md`](../GOVERNANCE.md) §5:

1. Charter v0.4 or later ratified with clear membership rules.
2. Minimum three organisationally-independent maintainers with write access.
3. AAIF or equivalent neutral custodian formally designated.
4. Contribution Terms v0.3 or later published with a CLA option available.
5. First public consultation window closed with a decision record for material comments.

Until all five are true, no Approved designation is made. The project continues to produce Draft Specifications under coordinated baselines, which are citable, versioned, and carry Draft-Specification patent grants.

---

## 5. Current and candidate designations

### 5.1 Approved Specifications

*(None at the version of this file in the current baseline.)*

### 5.2 Candidates for designation

*(None currently proposed.)*

---

## 6. Version history

- **v0.1 — Draft (October 2026):** initial draft covering interim custody posture, approval process to be used at and after Working Group formation, prerequisites alignment with `/GOVERNANCE.md` §5, and Scope snapshot alignment at approval.

---

## 7. Changes to this file

This file is a CSL 1.0 companion with intellectual-property consequences. Changes:

- Are submitted as a pull request labelled `csl-governance-change`.
- Require Release Approver sign-off per [`/GOVERNANCE.md`](../GOVERNANCE.md) §2.2.
- Changes that affect how the Draft → Approved transition operates, or that bind approvals already made, require WG consensus post-formation and are not retroactive.

---

*This file exists to satisfy CSL 1.0's reference to a Governance.md companion. The binding community-governance document for the repository is `/GOVERNANCE.md`.*
