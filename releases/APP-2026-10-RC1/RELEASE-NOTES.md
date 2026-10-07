# APP-2026-10-RC1 — Release Notes

**Date:** 2026-10-07
**Status:** Draft Specification under CSL 1.0 §9.6.

This is the **first coordinated APP baseline published to the public repository**. It establishes the baseline citation unit (`APP-2026-10-RC1`), freezes the Specification at the versions listed in `MANIFEST.md`, and makes the CSL 1.0 §9.13 Scope companion effective for implementers of this baseline.

## What this baseline contains

- **Eleven Specification documents** at the versions in `MANIFEST.md`: APP-0 Protocol Objectives, APP-1 Protocol Constitution, APP-2 Core Technical Specification, APP-3 Security Architecture, APP-4 Entity Correlation Architecture, APP-5 Conformance Profiles, and APP-IG-01 to APP-IG-05 implementation guides.
- **Four Plain Language Guides** (informative, outside the Specification).
- **Three legal instruments**: Contribution Terms (CSL 1.0 verbatim), WG Data Handling Charter, Consultation Privacy Notice.
- **One frozen CSL companion**: Scope v0.3, now effective for this baseline under its own effectivity clause.
- **Two accompanying illustrative-reference artefacts** at their first published versions: APP-R1 Process Frame Schema v0.3.0 and APP-R2 MCP Binding Reference Design v0.3 Draft.

## What is new in this baseline

### Three-tier APP corpus taxonomy

APP-1 v1.5 §4 recognises an **APP-R Illustrative Reference tier** alongside the normative APP-0..APP-5 and informative APP-IG-01..APP-IG-05 tiers. Illustrative References are non-normative; implementations may deliver equivalent conformance via other realisations. APP-R1 (Process Frame Schema) and APP-R2 (MCP Binding Reference Design) are the first two Illustrative References.

Consequential updates in this baseline:

- APP-2 v5.13 adds illustrative-reference pointers from CORE-A1-04 and CORE-A1-05 to APP-R2 and APP-R1 respectively. No normative change; no requirement, keyword, or conformance obligation altered.
- APP-5 v1.10 adds a reference-artefact note to §5.2 pointing conformance assessors at APP-R1 and APP-R2 as illustrative artefacts the Specification Dimension tests may be run against. No test ID, procedure, or pass criterion changed.
- APP-IG-01 v1.11 adds §1.4 introducing the Illustrative Reference tier and names the two current reference artefacts.
- APP-IG-05 v0.12 is a patch adding APP-R1 and APP-R2 to the companion documents list and the platform-implementer reading path.

### Editorial corrections included in this baseline

Two editorial defects identified during the pre-publication review are corrected in this baseline. Both are editorial under APP-1 §4 (no normative meaning, requirement ID, RFC keyword, conformance expectation, or cross-reference target changed in substance; the second corrects a broken citation to point at the correct, pre-existing target):

- **APP-5 §5.2 — cross-reference correction.** The citation to "APP-4 §3.4.5" for the five-field EC-17 governance audit now correctly cites APP-4 §3.4.1, which is the section defining EC-17 and listing the five mandated audit fields (authoriser, evidence bundle, reversal path, expiry, audit trail). No conformance obligation changed.
- **csl/Scope.md — closing version label.** The end-of-document label is corrected from "v0.2" to "v0.3" to match the document header. No content change.

### Baseline reference normalisation

All documents in this baseline reference the suite baseline consistently as `APP-2026-10-RC1 (Oct 2026)`. Prior drafts carried mixed references to a provisional `APP-2026-09-RC2` label that was superseded during pre-publication coordination; those references have been normalised across all suite, guide, legal, and reference-design documents.

## Baseline composition decision

The composition of this baseline is recorded in `/decisions/APP-DEC-0002.md`. Approval of that decision record and the publication of this tag constitute the baseline's authoritative inception.

## Known issues

Open items deliberately carried into Working Group formation or a follow-up baseline are listed in `KNOWN_ISSUES.md` in this directory. Each is also opened as a GitHub Issue after publication for public tracking.

## Status, warranties, and reliance

This baseline is published as a **Draft Specification** under CSL 1.0 §9.6 for public consultation and implementation experience. It is not an Approved Specification. Implementation experience and public comments are welcomed through the repository's Issue Forms and Discussions.

Nothing in this baseline is a warranty, representation, or professional advice. Reliance by implementers, conformance assessors, deployers, buyers, auditors, or any other party is at the relying party's own risk and subject to the terms of the Community Specification License 1.0 and the Contribution Terms in this baseline.

## Citation

Cite documents in this baseline using the canonical citation format in `MANIFEST.md`. For example:

> APP-3 Security Architecture v3.13, APP-2026-10-RC1, §S13, tag APP-2026-10-RC1, manifest SHA-256 `e63db4e8619e1563f1e2b4dc7913febdab7d6aa40633b4ddcfe319e8aad48fd3`

## What comes next

The next baseline is prepared in `/drafts/` on the default branch. The present baseline is immutable; changes between baselines flow through the normal `normative-proposal` and `editorial-change` paths governed by APP-1 §4 and the repository's Normative Suite Control.

---

*End of RELEASE NOTES for APP-2026-10-RC1.*
