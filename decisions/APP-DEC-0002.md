---
decision_id: APP-DEC-0002
title: Baseline composition and inclusion decisions for APP-2026-10-RC1
status: Approved
date: 2026-10-07
approver: "@APPcustodian (Vaidhya, Vach AI Limited, Interim Custodian)"
supersedes: null
superseded_by: null
---

# APP-DEC-0002 — Baseline composition for APP-2026-10-RC1

## 1. Context

APP-2026-10-RC1 is the **first coordinated APP baseline published to the public repository**. The baseline establishes:

- The eleven-document Specification set as of the publication tag.
- The three-tier APP corpus taxonomy (normative APP-0..5; informative APP-IG-01..05 within the Specification; APP-R Illustrative Reference tier outside the Specification), recognised by APP-1 v1.5 §4.
- The first two accompanying Illustrative Reference artefacts: APP-R1 Process Frame Schema v0.3.0 and APP-R2 MCP Binding Reference Design v0.3 Draft.
- The CSL 1.0 §9.13 Scope companion `csl/Scope.md` v0.3 as effective for implementers of this baseline, under its own effectivity rule.

## 2. Decision

The Release Approver approves the composition of APP-2026-10-RC1 as inventoried in `releases/APP-2026-10-RC1/MANIFEST.md` and `releases/APP-2026-10-RC1/manifest.json`. The composition comprises:

- **Specification (11 documents):** APP-0 v0.14, APP-1 v1.5, APP-2 v5.13, APP-3 v3.13, APP-4 v2.3, APP-5 v1.10, APP-IG-01 v1.11, APP-IG-02 v1.15, APP-IG-03 v1.11, APP-IG-04 v0.6, APP-IG-05 v0.12.
- **Guides (informative, outside the Specification; 4 documents):** APP Plain Language Guide v0.1 overview and three per-document Plain Language Guides at v0.2 for APP-2, APP-3, APP-4.
- **Legal instruments (3 documents):** Contribution Terms v0.2, Charter v0.3, Privacy Notice v0.3.
- **CSL 1.0 companion frozen for this baseline (1 document):** Scope v0.3 at `releases/APP-2026-10-RC1/csl/Scope.md`.
- **Accompanying Illustrative Reference artefacts (informative, outside the Specification; 4 files comprising 2 artefact IDs):** APP-R1 Process Frame Schema v0.3.0 package (schema, notes, example); APP-R2 MCP Binding Reference Design v0.3 Draft.

## 3. Editorial corrections approved as part of this decision

The following editorial corrections are approved and included in this baseline. Both are editorial under APP-1 §4 — no normative meaning, requirement ID, RFC 2119/8174 keyword, conformance obligation, or applicability condition changed. The second corrects a broken citation to point at the correct, pre-existing target.

- **APP-5 v1.10 §5.2 — EC-17 cross-reference.** The citation to "APP-4 §3.4.5" is corrected to "APP-4 §3.4.1". APP-4 §3.4.1 is where EC-17 is defined and where the five mandated audit fields (authoriser, evidence bundle, reversal path, expiry, audit trail) are listed. APP-4 has no §3.4.5; the prior citation was broken.
- **csl/Scope.md — closing version label.** The end-of-document label is corrected from "v0.2" to "v0.3" to match the document header. No content change.

## 4. Illustrative Reference tier inclusion (APP-R1, APP-R2)

Decision 2 taken on the Custodian preparation call: APP-R1 and APP-R2 are included in APP-2026-10-RC1 as the first Illustrative Reference artefacts.

**Publication-clearance assessment (per Runbook §2):** Clearance for APP-R1 v0.3.0 and APP-R2 v0.3 Draft is confirmed by the Release Approver on this decision record. The IP review that the retired pre-publication internal release notes referred to has been completed. No separate publication-clearance decision records are generated; this composition decision records the clearance.

**What this means for implementers:** Illustrative Reference artefacts are informative. They do not create a conformance obligation. Implementations may deliver equivalent conformance via other realisations. The future adoption of APP-R1 as the normative CORE-A1-05 published Frame schema (or retention as Illustrative) is a Working Group decision tracked as KI-06 in `KNOWN_ISSUES.md`.

## 5. CSL 1.0 §9.13 non-retroactivity

With this baseline tag, `csl/Scope.md` v0.3 becomes effective for implementers of APP-2026-10-RC1 per its own effectivity clause. Under CSL 1.0 §9.13, changes to Scope do not apply retroactively. Any later Scope.md revision binds only implementers of a later baseline that includes that later Scope.md version at tag.

## 6. Baseline reference normalisation

All documents in this baseline reference the suite baseline consistently as `APP-2026-10-RC1 (Oct 2026)`. Prior-draft references to a provisional `APP-2026-09-RC2` label have been normalised across all suite, guide, legal, and reference-design documents in coordination with the pre-publication parallel sessions. The normalisation is editorial under APP-1 §4.

## 7. Composition items not included in this baseline

The following items were considered during preparation and deliberately not included:

- **Plain Language Guides for APP-0, APP-1, and APP-5.** Not drafted at tag time. Tracked as KI-01.
- **Reference code for APP-R2 MCP Binding.** Design document (APP-R2 v0.3 Draft) is published; working reference code is a separate workstream tracked as KI-08.
- **Separate publication-clearance decision records (APP-DEC-0003, APP-DEC-0004) for APP-R1 and APP-R2.** The Release Approver has determined that the IP review already completed makes separate attestation unnecessary for first-baseline inclusion; publication clearance is folded into this composition decision at §4.

## 8. Approval record

- **Approver:** @APPcustodian (Vaidhya, Vach AI Limited, Interim Custodian).
- **Date of approval:** 2026-10-07.
- **Means of approval:** This decision record, committed in the baseline publication PR, together with the Release Approver sign-off recorded in that PR body.
- **Scope of approval:** The complete composition inventoried in `releases/APP-2026-10-RC1/MANIFEST.md` and `releases/APP-2026-10-RC1/manifest.json`, the editorial corrections in §3, the Illustrative Reference inclusion in §4, and the baseline reference normalisation in §6.

---

*End of APP-DEC-0002.*
