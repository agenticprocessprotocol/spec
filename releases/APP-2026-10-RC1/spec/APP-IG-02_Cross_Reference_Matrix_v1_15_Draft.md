# APP-IG-02

Agentic Process Protocol

## Cross-Reference Matrix

| | |
|:---|:---|
| **Version** | 1.15 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Audience** | All protocol stakeholders: implementors, working group members, security architects, enterprise governance teams |
| **Normative status** | This document is **informative**. It does not define requirements. It maps requirements defined in APP-0, APP-2, APP-3, APP-4, and APP-5 to each other. |
| **Companion documents** | APP-0, APP-1 (Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles), APP-R1 (Frame Schema), APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. Version bumps require concurrent manifest regeneration. |
| **Version-reference convention** | Companion documents cited by name only in body prose. Manifest above is the sole non-historical source for companion versions. Version numbers persist in body prose only for historical claims. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-IG-02 is the informative cross-reference matrix for the Agentic Process Protocol. It maps requirements across the normative documents and provides bidirectional traceability.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. This document does not create, modify, or override normative requirements in APP-0 through APP-5.
>
> **Use this document for:** Requirement-to-requirement mappings, Objective-to-requirement traceability, role and L-level coverage matrices, dependency chains.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** APP-0 through APP-5 (source of the traceability).

---

## Purpose

This document is the **canonical informative aggregation for suite baseline APP-2026-10-RC1**. It answers cross-document questions that no single specification answers on its own:

- Which APP-2 core capability does each APP-3 security domain protect? (§1)
- Which APP-4 entity-correlation requirement pairs with which APP-3 security requirement? (§2)
- Which APP-4 entity-correlation requirement extends which APP-2 core capability? (§3)
- Which requirements move together across documents when one changes? (§4)
- How many requirements apply at each L-level? (§5)
- Which requirements realise which APP-0 Objective? (§7)

This document is **informative**. It does not define requirements. It maps requirements defined elsewhere. APP-2, APP-3, and APP-4 remain the semantic authorities for their respective requirements; APP-5 remains the applicability authority for role × L-level conformance; APP-IG-02 aggregates the mappings across these documents. Where APP-IG-02 and any normative source disagree, the normative source prevails and APP-IG-02 is corrected in the next revision.

---

## 1. Security Domain → Capability Mapping

APP-3 defines security requirements across 14 domains (S1–S14) plus cross-cutting principles (XX-01 through XX-05). Each domain protects one or more APP-2 core capabilities. The mapping below is authoritative for cross-document navigation.

| APP-3 Domain | Name | APP-2 Capability Protected | Load-bearing SEC IDs |
|:---|:---|:---|:---|
| **S1** | Frame Integrity | A0 (Process Frame), A1 (Integration Surface) | SEC-S1-01 through S1-05 |
| **S2** | Transport & Federation | A1 (Integration Surface) | SEC-S2-01 through S2-06 |
| **S3** | Classification Integrity | A3 (D/P Classification) | SEC-S3-01, S3-02, S3-06, S3-07 |
| **S4** | Evidence Integrity | A2 (PxER — Process Execution Record) | SEC-S4-01 through S4-06 |
| **S5** | HITL Security | A6 (HITL Governance) | SEC-S5-01 through S5-06 |
| **S6** | Compliance Validation | A5 (Compliance Constraints) | SEC-S6-01 through S6-05 |
| **S7** | Orchestration Integrity | §6 Graceful Degradation, cross-cutting | SEC-S7-01, S7-02, S7-03 |
| **S8** | Promotion Integrity | A8 (P→D Promotion) | SEC-S8-01 through S8-04 |
| **S9** | Feedback Loop Integrity | A9 (Lifecycle), A10 (Drift), A11 (Intelligence) | SEC-S9-01, S9-02, S9-03 |
| **S10** | Tenant Isolation | A11 (Cross-Deployment Analytics) | SEC-S10-01, S10-02, S10-03 |
| **S11** | Supply Chain | A0 (Frame templates), A8 (marketplace) | SEC-S11-01, S11-01a, S11-02, S11-03 |
| **S12** | L1 Security | L1 integration maturity level | SEC-S12-01, S12-02, S12-03 |
| **S13** | Agent Identity | Cross-cutting (identity binding across A1, A2, A4) | SEC-S13-01, S13-02, S13-03 |
| **S14** | Entity Correlation Security | APP-4 EC requirements (all) | SEC-S14-01 through S14-09 |
| **XX** | Cross-cutting principles | Applies across all capabilities | SEC-XX-01 (TAO), XX-02 (substrate isolation), XX-03 (authority reduction, RP), XX-04 (adversarial verification), XX-05 (minimum safe-state transition) |

**S3 numbering note.** SEC-S3-03, S3-04, S3-05 are retired IDs preserved for immutability. Active S3 requirements: S3-01, S3-02, S3-06, S3-07.

**Multi-capability protection.** Some SEC requirements protect more than one CORE capability (e.g., SEC-XX-01 Temporal Activation Ordering applies across all capabilities). Placement above uses the *primary* protection relationship; secondary relationships are noted in §4 co-dependencies.

---

## 2. Entity Correlation → Security Mapping

APP-4 EC-38 through EC-47 are the security-specific entity correlation requirements. They map to APP-3 SEC-S14-01 through S14-09 via one-to-one, one-to-many, and many-to-one relationships — a single S14 requirement may aggregate obligations expressed by two adjacent EC requirements, and a single EC requirement may satisfy properties covered by two adjacent S14 requirements. v1.13 makes the relationship type explicit rather than presenting a false one-to-one pairing.

| APP-4 EC ID | Description | Primary APP-3 Counterpart | Related APP-3 Counterpart(s) | Relationship Type |
|:---|:---|:---|:---|:---|
| **EC-38** | Access controls preventing cross-tenant entity type leakage in entity_extract declarations | SEC-S14-01 | — | 1:1 |
| **EC-39** | Entity field paths not exposed to unauthorised tenants/roles | SEC-S14-02 | — | 1:1 |
| **EC-40** | Entity data inherits PxER access controls and hash chain integrity | SEC-S14-03 | — | 1:1 |
| **EC-41** | Cross-tenant entity correlation prohibited | SEC-S14-04 | — | 1:1 |
| **EC-42** | Cross-enterprise entity references limited to boundary-observable data | SEC-S14-05 | — | 1:1 |
| **EC-43** | Populated-mode imports MUST authenticate source systems | SEC-S14-06 | — | 1:1 |
| **EC-44** | Correlation data inherits tenant isolation controls | SEC-S14-07 | SEC-S14-04 (cross-tenant prohibition) | many-to-one |
| **EC-45** | Reconciliation signals (especially `divergent`) access-controlled | SEC-S14-07 | SEC-S14-03 (access-control inheritance) | many-to-one |
| **EC-46** | Correlation registry tenant isolation + cross-enterprise boundary limits | SEC-S14-08 | SEC-S14-04, SEC-S14-05 | one-to-many |
| **EC-47** | Entity retention per declared compliance scope | SEC-S14-09 | — | 1:1 |

**SEC-S14-07 aggregation.** SEC-S14-07 aggregates two distinct EC obligations: EC-44 (correlation data tenant isolation) and EC-45 (reconciliation-signal access control). Both must be satisfied for SEC-S14-07 conformance. Implementations of SEC-S14-07 that address only one of the two are non-conformant.

**SEC-S14-08 decomposition.** EC-46 covers two obligations that APP-3 distributes across SEC-S14-08 (correlation registry tenant isolation) plus additional coverage from SEC-S14-04 (cross-tenant prohibition) and SEC-S14-05 (cross-enterprise boundary). An implementation of EC-46 conformance MUST address all three APP-3 controls.

**Interpretation rule.** Where an EC-* description and its S14 counterpart appear to conflict, APP-3 SEC-S14 states the *security* obligation and APP-4 EC states the *entity-correlation-specific* obligation. Both apply. Where the relationship type is many-to-one or one-to-many, satisfying the primary counterpart is necessary but not sufficient — the related counterparts also apply, and APP-5 test criteria assess conformance against the complete set.

---

## 3. Entity Correlation → Core Capability Mapping

APP-4 EC requirements extend APP-2 capabilities A0 (Process Frame) and A2 (PxER).

### Applicability model

There are three distinct classes of obligation, with different applicability triggers:

| Obligation class | Applicability trigger | L-level scope |
|:---|:---|:---|
| **1. Per-step entity reference production** (EC-07 through EC-11) | Active only when a Frame step declares `entity_extract`. Absence of `entity_extract` on any given step MUST NOT prevent step execution (EC-06). A conformant Governance Orchestrator can operate over Frames with zero `entity_extract` declarations without triggering EC-07/08/09/10/11 obligations. | Applies at any L-level where entity_extract is declared. |
| **2. Correlation infrastructure capability** (EC-15 inferred mode; EC-19 populated mode; EC-25 registry persistence; EC-22 reconciliation) | Mandatory for L2+ Governance Orchestrator conformance regardless of whether any specific Frame declares entity_extract. This is an implementation-capability obligation: the runtime MUST be able to perform inferred correlation, populated import, registry persistence, and reconciliation when called upon by a Frame that does declare entity_extract. | Mandatory at L2+ for Governance Orchestrator role. |
| **3. Entity-correlation-specific security** (EC-38 through EC-47) | Mandatory whenever obligations from class 1 or class 2 apply. Where neither is triggered (an L1 deployment with no entity_extract declarations at any step), the EC-38 through EC-47 obligations remain applicable to the extent that any entity data is captured at all. | Applies at any L-level where any entity data flows through the implementation. |

**Enterprise-buyer question this answers.** *"Does an L2+ Governance Orchestrator have to implement inferred correlation, populated import, reconciliation, and registry persistence even if no process scope in my deployment declares entity_extract?"* — **Yes.** L2+ conformance is capability-based, not usage-based. The obligation is that the runtime CAN perform correlation when invoked, not that any given Frame invokes it. This is analogous to how an L2 implementation MUST support MCP tool invocation even if a specific Frame uses zero MCP tools. Enterprises that will not use entity correlation at all MAY declare conformance to core APP-2 without entity correlation capability, but that is a distinct L1 conformance scope; L2+ conformance requires the capability.

**Alignment with APP-4 §1.5(d).** This model implements APP-4 §1.5(d) reframe — the "amplifier not prerequisite" language was retired precisely because it conflated per-step optionality (correct) with implementation-capability optionality (incorrect). The three-class model above states this distinction cleanly.

**Alignment with APP-5 §4.1.3.** APP-5 §4.1.3 (Governance Orchestrator entity correlation requirements) applies the same three-class model. Where APP-5 lists EC IDs against the GO role at L2+, it applies the applicability trigger from the class the ID belongs to.

### 3.1 EC → A0 (Process Frame) — class 1 (per-step)

| EC ID | Description | A0 Extension Point |
|:---|:---|:---|
| **EC-01** | entity_extract declaration on Frame step | Optional step-level annotation on A0 |
| **EC-01a** | entity_extract changes are Frame mutations subject to SEC-S1-01/03 | Frame mutation gate |
| **EC-02** | Entity role classification vocabulary (primary_key, context_key, reference) | Structural type on EC-01 |
| **EC-03** | Entity type labels drawn from tenant-scoped registry (RP) | Recommended structural vocabulary |
| **EC-04** | L2 entity_extract auto-generated from MCP tool return schemas (RP) | L2-specific derivation |
| **EC-05** | Fidelity by maturity level | L-level applicability for EC-01 |
| **EC-06** | Absence of entity_extract MUST NOT block step execution | Per-step optionality guarantee (clarified v2.2) |

### 3.2 EC → A2 (PxER)

| EC ID | Description | A2 Extension Point |
|:---|:---|:---|
| **EC-07** | entity_refs block in PxER step when entity_extract present | Additional PxER step field |
| **EC-08** | entity_refs minimum fields (entity type, system key, extraction method) | Structural minimum |
| **EC-09** | Extraction method provenance | Confidence-supporting field |
| **EC-10** | Confidence indicators propagate to correlation | Correlation-quality signal |
| **EC-11** | Instance-level correlation block links entity refs across steps | Cross-step correlation within instance |
| **EC-12** | Tenant-scoped entity type namespace | Cross-instance vocabulary boundary |
| **EC-13** | Consistent entity type labels across processes within tenant (RP) | Cross-process comparability aid |
| **EC-14** | Correlation on co-occurrence, not labels; tenant-scoped key namespace; no raw equal-value cross-system matching without normalisation or evidence basis; PII entity keys inherit PII controls | Inference correctness + PII safety (extended v2.2) |

### 3.3 EC → correlation infrastructure

| EC ID | Description | Infrastructure Layer |
|:---|:---|:---|
| **EC-15** | Inferred-mode entity correlation MUST be supported | Correlation registry |
| **EC-16** | Inferred correlations carry confidence + evidence count + observation timestamps | Registry entry schema |
| **EC-17** | Process-scoped inference; global promotion requires cross-Frame evidence + 5-field governance audit (authoriser, evidence bundle, reversal path, expiry, audit trail) — extended v2.2 | Registry governance |
| **EC-18** | Confidence monotonic with evidence count subject to recency (RP) | Confidence semantics |
| **EC-19** | Populated-mode correlation MUST be supported | Correlation registry |
| **EC-20** | Populated imports use source-agnostic schema | Import contract |
| **EC-21** | Populated correlations carry source ID, import timestamp, confidence | Registry entry schema |
| **EC-22** | Reconciliation five-outcome status (aligned, divergent, populated_only, inferred_only, error); `error` stale state advisory-only unless deployment policy explicitly permits enforcement (clarified v2.2) | Registry reconciliation gate |
| **EC-23** | Divergent status surfaced as operational signal | Operational surface |
| **EC-24** | Inferred_only surfaced as discovery signal (RP) | Discovery surface |
| **EC-25** | Correlation registry persistent across process instances for tenant | Storage architecture |
| **EC-26** through **EC-33** | Registry query, lifecycle, drift signals | Registry operational surface |
| **EC-34, EC-35** | Graceful degradation to non-correlated mode | Availability behaviour |
| **EC-36, EC-37** | Reporting and analytics interfaces | Analytics surface |

---

## 4. Cross-Document Requirement Co-Dependencies

The following requirement pairs must move together across documents. When one changes, the paired requirement(s) in the linked document(s) must be reviewed for consistency. This section identifies the co-dependencies that a mechanical inconsistency check should verify at every release.

### 4.1 CORE ↔ SEC co-dependencies

| CORE ID | Paired SEC ID(s) | Nature of dependency |
|:---|:---|:---|
| CORE-A0-01 (mandatory Frame fields) | SEC-S1-01 (signed mutations) | Frame fields must be signed at mutation time |
| CORE-A1-05 (Frame schema portability) | SEC-S1-01, S1-02 | Schema mutations follow signing + provenance |
| CORE-A2-01 (immutable PxER) | SEC-S4-05 (write-path auth across six artifact classes), SEC-S4-04 (tiered trust for new contributors), SEC-S4-06 (erasure reconciliation) | Immutability + write authenticity + tiered contributor trust + lawful erasure |
| CORE-A2-03 (7-field conformance schema) | SEC-S4-01 (async evidence verification) | Verification of the 7-field schema |
| CORE-A2-04 (mismatch types incl. CONFLICT) | SEC-S3 (Classification Integrity) — S3-01, S3-07 | CONFLICT escalation to classification integrity path |
| CORE-A2-13 (recovery evidence schema with `sequence`) | SEC-S6-05 (recovery-path enforcement-tier invariant), SEC-S13-01/02/03 (`authorized_by` binding) | Recovery evidence structure + tier parity + authorised recovery |
| CORE-A2-14 (recovery outcome vocabulary) | SEC-S6-05, SEC-XX-05 (safe-state transition on severe events) | Outcome vocabulary + tier parity + safe-state gate |
| CORE-A3-06 (independent D/P verification for compliance-critical) | SEC-S3-01, SEC-S3-07 | Independent verification path + cross-family attestation |
| CORE-A4-01 (three-layer accountability) | SEC-S13-01, SEC-S13-02 | Accountability chain identity binding |
| CORE-A4-06 (recovery-decision accountability) | SEC-S6-05, SEC-S13-01 | Recovery accountability requires identity |
| CORE-A5-01 (compliance authorship marker) | SEC-S6-01 through S6-05 | Marker feeds compliance validation controls |
| CORE-A6-01/02/03 (HITL engagement measurement) | SEC-S5-01, S5-03 (LITL defence, authenticity) | Measurement + authenticity |
| CORE-A6-03 (engagement-fidelity marker) | SEC-S6-05 (recovery tier composition, dependency shifted to A6-03 in v3.10) | Engagement fidelity anchors tier determination |
| CORE-A8-* (P→D promotion) | SEC-S8-01 through S8-04 | Promotion evidence integrity + velocity |
| CORE-A9-*, A10-*, A11-* (feedback loop) | SEC-S9-01, S9-02, S9-03 | Learning integrity |
| CORE-XX-01, XX-02 (degradation) | SEC-S7-02 (compliance-tiered degradation) | Degradation semantics |

### 4.2 CORE ↔ EC co-dependencies

| CORE ID | Paired EC ID(s) | Nature of dependency |
|:---|:---|:---|
| CORE-A0-01 (mandatory Frame fields) | EC-01, EC-01a | entity_extract as optional A0 annotation |
| CORE-A2-01, A2-02 (PxER assembly) | EC-07 through EC-11 | entity_refs as PxER field |
| CORE-A2-13 (recovery evidence) | EC-32 (entity drift signal as `evidence_refs` candidate) | Recovery may reference entity drift as triggering evidence |

### 4.3 SEC ↔ EC co-dependencies

| SEC ID | Paired EC ID(s) | Nature of dependency |
|:---|:---|:---|
| SEC-S14-01 through S14-09 | EC-38 through EC-47 | See §2 above |
| SEC-S4-06 (evidence-record erasure) | EC-40, EC-41, EC-47 | Erasure of entity data in PxER + registry |
| SEC-S1-01 (signed Frame mutations) | EC-01a (entity_extract change = Frame mutation) | EC-01a inherits Frame mutation controls |

### 4.4 Cross-cutting perimeter co-dependencies

The following requirements form the **minimum protocol perimeter for the explicitly modelled silent-governance-weakening vectors**: activation ordering, governance-control configuration change, recovery-path selection, and continued privileged action after detected severe events. This perimeter is necessary for those modelled vectors but is not a claim of completeness against all possible downgrade mechanisms. Implementations remain subject to SEC-XX-04's adversarial-verification obligation. The four controls move as a set:

- **SEC-XX-01** (Temporal Activation Ordering) — prevents downgrade by ordering
- **SEC-S6-04** (Governance-control integrity monitoring) — prevents downgrade by configuration change
- **SEC-S6-05** (Recovery-path enforcement-tier invariant) — prevents downgrade by recovery-path selection
- **SEC-XX-05** (Minimum safe-state transition on detected severe events) — prevents downgrade by continued privileged action after detected severe events

A change to any one of these controls requires review of the other three to ensure coverage remains intact for the four explicitly modelled downgrade vectors. This is not a claim of completeness against all possible downgrade mechanisms; adversarial verification per SEC-XX-04 remains required.

### 4.5 v3.10 SEC-XX-03 ↔ SEC-XX-05 floor relationship

SEC-XX-03 (authority reduction on uncertainty, RP) requires SEC-XX-05 as its MUST-level outcome floor per APP-1 Article 3. Changes to SEC-XX-03 mode set must preserve satisfaction of SEC-XX-05's five triggering event classes.

### 4.6 v3.10 SEC-S3-07 attestation ↔ SEC-S5-06 fallback

SEC-S3-07 (cross-family independent verification, attestation-based) requires SEC-S5-06 (agent-initiated safety-event channel) as its fallback when attestation is unavailable. Changes to either requirement must preserve the fallback path.

---

## 5. L-Level Applicability Summary

**Combined active requirement count: 183.** *(APP-3 reclassified SEC-S1-05 and SEC-S10-03 as Informative Guidance per APP-1 Article 3 constitutional discipline. The two IDs remain in the SEC-* namespace as guidance but are removed from the active normative requirement inventory.)*

- APP-2: **68** CORE-* IDs (A0–A11 capabilities + CP-* profiles + XX-* cross-cutting + L3-01)
- APP-3: **67** SEC-* IDs classified as Required Outcome or Recommended Pattern (plus 2 IDs — SEC-S1-05 and SEC-S10-03 — reclassified in v3.13 as Informative Guidance; these remain in the SEC-* namespace but are not counted against active normative requirements)
- APP-4: **48** EC-* IDs (EC-01 through EC-47 plus EC-01a)

### L-level applicability

Counts below are computed from APP-5 §4 per-role requirement matrices. The reported values are for **Governance Orchestrator** role (the role with the largest applicable requirement set); other roles have smaller applicable subsets per APP-5 §4.2 through §4.5.

| L-level | Description | GO applicable requirements | Source |
|:---|:---|:---:|:---|
| **L1** (Screen/RPA) | Governance instruments processes at the screen / RPA layer | 68 | APP-5 §4.1.1 L1 column + §4.1.2 L1 column + §4.1.3 L1 column (EC-38 through EC-47 apply where any entity data flows) |
| **L2** (API/MCP) | Direct system integration via APIs and MCP | 172 | APP-5 §4.1.1/§4.1.2/§4.1.3 L2 columns |
| **L3** (Application-Enhanced) | Applications contribute telemetry via Telemetry Contribution Protocol | 178 | APP-5 §4.1.1/§4.1.2/§4.1.3 L3 columns (adds CORE-L3-01, SEC-S4-03, SEC-S10-01/02 relative to L2) |
| **L4** (AI-Native) | Systems produce governance evidence structurally | 178 | APP-5 §4.1.1/§4.1.2/§4.1.3 L4 columns (adds SEC-S11-01 template marketplace; SEC-S4-03/04 telemetry contributor obligations subsumed into native evidence generation) |

*Counts are exact per current APP-5 §4 matrices. Where those matrices are revised, this table refreshes.*

### v1.13 change from v1.12

- Counts labelled "Approximate" in v1.12 replaced with exact counts computed from APP-5 §4 matrices. Approximate counts do not belong in a cross-reference matrix.

---

## 6. Known Open Issues (Cross-Document)

**Remaining open items:**

- ⬜ **OI-18** — Legal-review verification of APP-IG-05 §10 regulatory crosswalks for specific deployment claims.

---

## 7. APP-0 Objective ↔ Realising Requirements Traceability

### 7.1 Forward direction — Objective → Realising Requirements (curated authoritative subset)

Mirrors APP-0 §3.1. This is the load-bearing subset — the requirements whose non-conformance would prevent the Objective from being demonstrated. The exhaustive per-requirement mapping is in §7.2.

**O-1 Authorised Action.** CORE: A0-01, A4-01, A4-02, A4-04, A4-06, A5-01, A5-02. SEC: S2-01, S2-06, S13-01, S13-02, S13-03. EC: EC-38, EC-39.

**O-2 Independent Verification.** CORE: A3-06, A6-01, A6-02, A6-03, A6-05. SEC: S3-01, S3-02, S3-06, S3-07, S5-01, S5-03, S8-03. EC: EC-22.

**O-3 Bounded Agency.** CORE: XX-01, XX-02. SEC: XX-01, XX-02, XX-03, XX-04, XX-05, S2-05, S2-06, S5-06, S6-05, S7-01, S7-02, S7-03, S13-03. EC: EC-34, EC-35.

**O-4 Execution-Time Evidence.** CORE: A2-01, A2-02, A2-03, A2-04, A2-04a, A2-05, A2-06, A2-08a, A2-10, A2-11, A2-12, A2-13, A2-14, A3-02, L3-01. SEC: S4-01, S4-02, S4-03, S4-04, S4-05, S4-06. EC: EC-07, EC-08, EC-09, EC-10, EC-11, EC-40, EC-41, EC-42.

**O-5 Governed Change.** CORE: A3-01, A3-03, A3-04, A8-01, A8-02, A8-03, A8-04, A9-01, A9-02, A10-02, A10-04. SEC: S1-01, S1-02, S1-03, S1-04, S6-01, S6-02, S6-03, S6-04, S6-05, S8-01, S8-02, S8-04, S9-01, S9-02, S9-03.

### 7.2 Reverse direction — Requirement → Objective

Every one of the 185 normative requirements maps to either an Objective it realises, a STRUCT classification (structural / naming / interoperability plumbing), or an INFO classification (informative documentation). The table below organises by document; STRUCT and INFO exceptions are enumerated in §7.3.

#### 7.2.1 APP-2 CORE-* (68 requirements)

| Requirement | Objective(s) |
|:---|:---|
| CORE-A0-01, A0-02, A0-03 | O-1, O-4 |
| CORE-A1-01, A1-02, A1-03, A1-04, A1-05, A1-06 | STRUCT (integration surface plumbing) |
| CORE-A2-01, A2-02, A2-03, A2-04, A2-04a, A2-05, A2-06, A2-07, A2-08, A2-08a, A2-10, A2-11, A2-12, A2-13, A2-14 | O-4 |
| CORE-A3-01, A3-02, A3-03, A3-04 | O-4, O-5 |
| CORE-A3-05, A3-06 | O-2 |
| CORE-A4-01, A4-02, A4-03, A4-04, A4-05, A4-06 | O-1 |
| CORE-A5-01, A5-02, A5-03 | O-1, O-5 (A5-03 constraint-inheritance integrity → O-5) |
| CORE-A6-01, A6-02, A6-03, A6-05 | O-2 |
| CORE-A6-04 | INFO (engagement quality reporting) |
| CORE-A7-01, A7-02, A7-03 | STRUCT (consumption-mode parity plumbing) |
| CORE-A8-01, A8-02, A8-03, A8-04 | O-5 |
| CORE-A9-01, A9-02, A9-03 | O-5 |
| CORE-A10-01, A10-02, A10-03, A10-04 | O-5 |
| CORE-A11-01, A11-02 | O-5 |
| CORE-CP-01, CP-02, CP-03, CP-04 | STRUCT (conformance profile plumbing) |
| CORE-XX-01, XX-02 | O-3 |
| CORE-L3-01 | O-4 (L3 telemetry schema) |

**CORE STRUCT/INFO count:** A1 (6) + A7 (3) + CP (4) + A6-04 (1) = 14. **CORE realising Objectives: 54.**

#### 7.2.2 APP-3 SEC-* (69 requirements)

| Requirement | Objective(s) |
|:---|:---|
| SEC-S1-01, S1-02, S1-03, S1-04, S1-05 | O-5 |
| SEC-S2-01, S2-02, S2-03, S2-04 | O-1, STRUCT (transport) |
| SEC-S2-05 (RP), S2-06 | O-1, O-3 |
| SEC-S3-01, S3-02, S3-06, S3-07 | O-2 |
| SEC-S4-01, S4-02, S4-03, S4-04, S4-05, S4-06 | O-4 |
| SEC-S5-01, S5-02, S5-03, S5-04, S5-05, S5-06 | O-2, O-3 (S5-05 jurisdictional tier → O-3; S5-06 safety channel → O-3) |
| SEC-S6-01, S6-02, S6-03, S6-04, S6-05 | O-3, O-5 (S6-05 recovery-tier → O-3; S6-01/02/03/04 → O-5) |
| SEC-S7-01, S7-02, S7-03 | O-3 |
| SEC-S8-01, S8-02, S8-03, S8-04 | O-5, O-2 (S8-03 dual-human → O-2) |
| SEC-S9-01, S9-02, S9-03 | O-5 |
| SEC-S10-01, S10-02, S10-03 | STRUCT (tenant isolation for A11) |
| SEC-S11-01, S11-01a, S11-02, S11-03 | STRUCT (supply chain plumbing) |
| SEC-S12-01, S12-02, S12-03 | O-4 (L1 evidence integrity foundation) |
| SEC-S13-01, S13-02, S13-03 | O-1 (identity) |
| SEC-S14-01 through S14-09 | O-1, O-4 (mapped via EC-38–47 in §2) |
| SEC-XX-01, XX-02, XX-03, XX-04, XX-05 | O-3 |

**SEC STRUCT count:** S2-01/02/03/04 partial (2 STRUCT) + S10 (3) + S11 (4) = 9. **SEC realising Objectives: 60.**

#### 7.2.3 APP-4 EC-* (48 requirements)

| Requirement | Objective(s) |
|:---|:---|
| EC-01, EC-01a, EC-02, EC-03, EC-04, EC-05, EC-06 | STRUCT (entity_extract declaration structure) |
| EC-07, EC-08, EC-09, EC-10, EC-11 | O-4 |
| EC-12, EC-13, EC-14 | O-4, O-1 (EC-14 PII controls → O-1 confidentiality contribution) |
| EC-15, EC-16, EC-17 | O-4, O-5 (EC-17 promotion governance → O-5) |
| EC-18, EC-19, EC-20, EC-21 | O-4 |
| EC-22 | O-2, O-5 |
| EC-23, EC-24, EC-25, EC-26, EC-27, EC-28, EC-29, EC-30, EC-31 | STRUCT (registry surface plumbing) |
| EC-32, EC-33 | O-5 (drift signals feed governed change) |
| EC-34, EC-35 | O-3 |
| EC-36, EC-37 | INFO (reporting and analytics interfaces) |
| EC-38, EC-39, EC-40, EC-41, EC-42, EC-43, EC-44, EC-45, EC-46, EC-47 | O-1, O-4 (via §2 mapping) |

**EC STRUCT/INFO count:** EC-01 to EC-06 (7) + EC-23 to EC-31 (9) + EC-36/37 (2) = 18. **EC realising Objectives: 30.**

### 7.3 STRUCT and INFO classifications

**STRUCT** requirements exist for interoperability structure (naming, schema plumbing, transport, tenant isolation infrastructure) but do not directly realise an Objective. Their absence would break interoperability but not any single Objective's demonstrability.

**INFO** requirements are informative — they define reporting surfaces, analytics interfaces, or documentation guidance.

**v1.13 reconciliation.** v1.12's counts in §7.3 and §7.4 disagreed on STRUCT and INFO totals (41 vs 35) because the two sections were computed from different classification passes. v1.13 recomputes both against the same enumerated pass. The authoritative counts:

**CORE STRUCT/INFO** (from §7.2.1):
- STRUCT: A1-01/02/03/04/05/06 (6) + A7-01/02/03 (3) + CP-01/02/03/04 (4) = **13**
- INFO: A6-04 (1) = **1**

**SEC STRUCT/INFO** (from §7.2.2):
- STRUCT: S2-02/03/04 (3 — S2-01 realises O-1, so removed from STRUCT) + S10-01/02/03 (3) + S11-01/01a/02/03 (4) = **10**
- INFO: 0

**EC STRUCT/INFO** (from §7.2.3):
- STRUCT: EC-01/02/03/04/05/06 (6 — EC-01a is a Frame-mutation gate realising O-5, so not STRUCT) + EC-23/24/25/26/27/28/29/30/31 (9) = **15**
- INFO: EC-36/37 (2) = **2**

**Totals (revised v1.15):**
| Metric | Value | Formula / source |
|:---|---:|:---|
| Active requirement IDs | 183 | CORE 68 + SEC 67 + EC 48 (SEC-S1-05 and SEC-S10-03 reclassified as Informative Guidance) |
| STRUCT IDs | 38 | CORE 13 + SEC 10 + EC 15 |
| INFO IDs | 3 | CORE 1 + SEC 0 + EC 2 (§7.3 INFO category — informative *classification tag* on load-bearing IDs, not to be confused with APP-3's Informative Guidance IDs which are outside the active count) |
| Objective-realising IDs (distinct) | 142 | 183 − 38 − 3 (down from 144: SEC-S1-05 and SEC-S10-03 were Objective-realising in the v1.14 count) |
| Objective–requirement linkages | 187 | Count after multi-Objective duplication; see §7.4 (down from 189) |

**Terminology note.** "INFO (informative documentation)" as a classification for a normative requirement is conceptually distinct from APP-3's Informative Guidance classification: in §7.3 the INFO tag is a *classification within the normative inventory* denoting a load-bearing requirement whose function is informative — a documentation/reporting surface (e.g., CORE-A6-04); APP-3's Informative Guidance (e.g., SEC-S1-05, SEC-S10-03) places an ID entirely outside the active normative inventory. Future revisions may rename the §7.3 INFO tag to `NON-OBJECTIVE NORMATIVE SUPPORT` pending working-group naming decision.

Distinct sum verifies: **38 + 3 + 142 = 183** ✅

### 7.4 Objective coverage summary

Counts below are Objective–requirement **linkages**, not distinct requirement IDs. A requirement that realises two Objectives contributes to two rows. The linkage total (189) exceeds the distinct-Objective-realising count (144) because 45 requirements realise more than one Objective (e.g., CORE-A3-01 → O-4 and O-5; SEC-S6-05 → O-3 and O-5; EC-22 → O-2 and O-5).

| Objective | Objective–requirement linkages | Load-bearing requirements (from §7.1) |
|:---|---:|:---|
| **O-1 Authorised Action** | 32 | A0-01/02/03, A4-01/02/03/04/05/06, A5-01/02, S2-01, S2-06, S13-01/02/03, S14-01/02/03/04/05/06/07/08 (via §2 mapping — EC-38 through EC-46), EC-14 |
| **O-2 Independent Verification** | 17 | A3-05, A3-06, A6-01/02/03/05, S3-01/02/06/07, S5-01/03, S8-03, EC-22 |
| **O-3 Bounded Agency** | 24 | CORE-XX-01/02, SEC-XX-01/02/03/04/05, S2-05/06, S5-05/06, S6-05, S7-01/02/03, S13-03, EC-34, EC-35 |
| **O-4 Execution-Time Evidence** | 55 | A2-01/02/03/04/04a/05/06/07/08/08a/10/11/12/13/14, A3-02, L3-01, S4-01/02/03/04/05/06, S12-01/02/03, S14-03/07 (via §2 EC-40/41/42), EC-07/08/09/10/11, EC-12, EC-13, EC-14, EC-15/16/17/18/19/20/21, EC-40/41/42 |
| **O-5 Governed Change** | 42 | A3-01/03/04, A5-03, A8-01/02/03/04, A9-01/02/03, A10-01/02/03/04, A11-01/02, S1-01/02/03/04/05, S6-01/02/03/04/05, S8-01/02/04, S9-01/02/03, EC-17, EC-22, EC-32, EC-33 |
| **STRUCT (not linked to any Objective)** | 38 | (See §7.3 breakdown) |
| **INFO (not linked to any Objective)** | 3 | CORE-A6-04, EC-36, EC-37 |
| **Sum of linkages + STRUCT + INFO** | **189 + 38 + 3 = 230** | Linkages exceed distinct-ID count because of multi-Objective realisation. |

**Interpretation.** The linkage total (189) is the sum of "how many Objectives does each requirement realise" across all 144 distinct Objective-realising requirements. On average each such requirement realises 189 / 144 ≈ 1.31 Objectives. The distinct requirement count remains **185** (144 realising + 38 STRUCT + 3 INFO). The **Objective coverage summary is a count of linkages, not distinct requirements**; per-Objective totals do not sum to 185 and are not intended to.

### 7.5 Divergence handling

When APP-0 §3 (Realisation Mapping) and APP-IG-02 §7.1/§7.2 diverge, the resolution rule is:

1. If the divergence is a **new requirement** added to APP-2, APP-3, or APP-4 that APP-0 §3 has not yet reflected: APP-0 §3 is refreshed to include the requirement in the appropriate Objective's load-bearing set.
2. If the divergence is a **retired requirement**: APP-IG-02 §7.2 marks the retired ID as INFO with historical note; APP-0 §3 is refreshed to remove the reference.
3. If the divergence is a **classification change** (e.g., STRUCT reclassified to Objective-realising): APP-IG-02 §7.2 is authoritative for classification; APP-0 §3 references only Objective-realising requirements.
4. If APP-0 §3 references a requirement not present in APP-2/3/4 at all: this is a documentation error; APP-0 §3 is corrected.

The default resolution is that **APP-IG-02 §7.2 is authoritative for classification and count**; **APP-0 §3 is authoritative for load-bearing subset selection**; and both must agree at each release.

### 7.6 Role × L-level × Objective coverage cross-check

Verifies that every APP-0 Objective has applicable requirements at every declared conformance role × L-level scope. Cross-check runs against APP-5 §2.2 Dimension Applicability by Role + §4 per-role requirement matrices (§4.1 Governance Orchestrator, §4.2 Telemetry Contributor, §4.3 Agent Builder Platform, §4.4 Enterprise Deployer, §4.5 Field Deployment).

#### 7.6.1 Method

Two structural facts drive the cross-check:

**Fact 1 — Dimension applicability by role (APP-5 §2.2):**

| Role | Specification | Evidence | Governance | Security | Learning |
|:---|:---|:---|:---|:---|:---|
| **Governance Orchestrator (GO)** | Required | Required | Required | Required | Required |
| **Telemetry Contributor (TC)** | — | Required | — | Required | — |
| **Agent Builder Platform (AB)** | Required | — | — | Required | — |
| **Enterprise Deployer (ED)** | — | — | Required | Required | — |
| **Field Deployment (FD)** | — | — | — | Required | — |

**Fact 2 — Objective-to-Dimension mapping (derived from §7.1 forward direction):**

| Objective | Primary dimension(s) | Secondary dimension(s) |
|:---|:---|:---|
| O-1 Authorised Action | Governance, Security | Evidence (identity captured in evidence), Specification (Frame identity fields) |
| O-2 Independent Verification | Governance, Security | — |
| O-3 Bounded Agency | Security, Governance | — |
| O-4 Execution-Time Evidence | Evidence, Security | Specification (evidence schema) |
| O-5 Governed Change | Governance, Learning, Security | — |

The cross-check for each Objective × Role × L-level combination is:
1. Does the role carry any required dimension for the Objective? If yes → applicable.
2. Does the role's APP-5 §4 matrix contain any requirement realising the Objective at the L-level? If yes → covered.
3. If applicable but not covered → gap (raise as new open issue).

#### 7.6.2 Applicability × Coverage matrix

**Classification key.** Cells below use four classifications:

- **✅ Direct realisation** — the role's APP-5 §4 matrix contains a requirement that produces evidence, decisions, or state satisfying the Objective's outcome statement in APP-0 §2.
- **⚙ Configuration responsibility** — the role configures or declares parameters that other roles use to satisfy the Objective, but the role does not itself produce Objective-realising evidence.
- **🛡 Enabling control** — the role holds security or foundation controls that make Objective-realising evidence possible when produced by another role, but does not itself produce that evidence.
- **— Not applicable** — the role's dimension responsibilities per APP-5 §2.2 do not include the Objective's primary dimensions.

Working-group note: A conformance claim of "coverage" against an Objective must be at ✅ level. ⚙ and 🛡 are supporting classifications and do not by themselves satisfy the Objective at the role.

| Objective | GO (all L) | TC (L3 only) | AB (L2+) | ED (all L) | FD (all L) |
|:---|:---|:---|:---|:---|:---|
| **O-1** Authorised Action | ✅ Direct — CORE-A0-01, CORE-A4-01/02/06, CORE-A5-01/02, SEC-S2-01/06, SEC-S13-01/03 produce authorised-action evidence in PxER | 🛡 Enabling — SEC-S4-03 binds contributor identity to contributed telemetry; TC does not itself authorise actions | ✅ Direct — CORE-A0-01 + SEC-S13-01 produce session-scoped agent identity for actions the AB-hosted agent initiates | ⚙ Configuration — ED configures tenant authority boundaries and jurisdictional privacy tier (SEC-S5-05); a privacy tier is not itself authorisation evidence | — Not applicable — FD does not authorise actions or produce authority-provenance evidence. SEC-XX-01 in FD scope is activation ordering, not identity or authorisation. |
| **O-2** Independent Verification | ✅ Direct — CORE-A3-06, CORE-A6-01/02/03, SEC-S3-01/07, SEC-S5-01/03 produce independent-verification evidence | — Not applicable — Governance dim not required for TC | — Not applicable — Governance dim not required for AB; AB agents are verified by GO | ⚙ Configuration — ED declares verification scope + jurisdictional privacy tier via SEC-S5-05; ED does not itself perform verification | — Not applicable — Governance dim not required for FD |
| **O-3** Bounded Agency | ✅ Direct — CORE-XX-01/02, SEC-XX-02/04/05, SEC-S2-05/06, SEC-S6-05, SEC-S7-01/02/03, SEC-S13-03 enforce agency bounds | 🛡 Enabling (only) — SEC-XX-01 activation ordering applies to TC scope. TC does not execute agents or hold a delegated-authority surface; where the working group determines TC does not need Bounded-Agency coverage at all, this cell may reclassify to "Not applicable" | ✅ Direct — SEC-XX-02 substrate isolation, SEC-XX-05 safe-state transition, SEC-S13-03 authority-provenance invariant applied to AB-hosted agents | ⚙ Configuration — ED declares C2 degradation behaviour per SEC-S7-02, safe-state exit-condition policy per SEC-XX-05 | 🛡 Enabling — SEC-XX-01 activation-order enforcement + SEC-S1-04 source provenance ensure security controls precede execution; do not themselves bound agency at runtime |
| **O-4** Execution-Time Evidence | ✅ Direct — CORE-A2-01/02/03/10/13/14, CORE-A3-02, SEC-S4-01/02/03/04/05 produce PxER execution evidence during execution | ✅ Direct — CORE-A2-02/03 + CORE-L3-01 contribute execution-time evidence that GO consumes into assembled PxER | — Not applicable — Evidence dim not required for AB; agent activity captured in GO-assembled PxER | — Not applicable — Evidence dim not required for ED | 🛡 Enabling — SEC-S12-01/02 PII classification and credential isolation protect evidence ingress at L1 boundary; do not produce PxER evidence |
| **O-5** Governed Change | ✅ Direct — CORE-A3-01/03/04, CORE-A8-01 through A8-04, CORE-A9-01/02, CORE-A10-02/04, SEC-S6-04/05, SEC-S8-01 through S8-04, SEC-S9-03 produce change-governance evidence | — Not applicable — Governance + Learning dims not required for TC | — Not applicable — Governance + Learning dims not required for AB | ⚙ Configuration — ED approves policy changes affecting tenant-level governance scope; ED does not itself produce change-governance evidence | — Not applicable — Governance dim not required for FD |

#### 7.6.3 Result — direct-realisation and enabling-support summary

Reading the matrix at ✅ Direct realisation only (the only level that satisfies an Objective at a role):

- **GO (all L)**: ✅ all 5 Objectives at every L-level. Expected — GO carries all 5 dimensions.
- **TC (L3+)**: ✅ O-4 (evidence contribution). ⚙/🛡 elsewhere. O-2 and O-5 correctly not applicable.
- **AB (L2+)**: ✅ O-1 (agent identity), ✅ O-3 (substrate isolation, safe-state, authority provenance). O-2, O-4, O-5 correctly not applicable.
- **ED (all L)**: ⚙ Configuration responsibility for O-1, O-2, O-3, O-5. No ✅ Direct realisation cells at any Objective — ED's role is to configure the parameters other roles use, not to produce Objective-realising evidence.
- **FD (all L)**: 🛡 Enabling controls for O-3 and O-4. No ✅ Direct realisation cells — FD's role is activation-order and boundary enforcement, not evidence production.

**Working-group implication (v1.14 clarification).** The prior "zero coverage gaps" phrasing was structurally accurate at the Applicability × Coverage level (every applicable dimension × role × L-level combination has a realising or supporting requirement), but the phrasing overstated the relationship for ED and FD. **The corrected reading:**

- ED and FD do not directly realise most Objectives. Their coverage is enabling/configuration. An enterprise deployer or field deployment claiming standalone conformance to APP-0 §2 Objective outcomes without a corresponding GO or TC does not satisfy the Objectives; ED and FD conformance is meaningful in composition with a GO.
- GO is the central Objective-realising role. The suite's Objective-realising surface is concentrated in the GO matrix (and O-4 secondarily in the TC matrix).
- Asymmetries in coverage across O-1 through O-5 reflect the dimension applicability structure per APP-5 §2.2 and the role decomposition: no role holds every dimension except GO.

**Structural observation.** Asymmetries in coverage (O-2 concentrated in GO+ED; O-5 concentrated in GO+ED; O-4 concentrated in GO+TC) reflect the dimension applicability structure per APP-5 §2.2 combined with each role's decomposition. Attempting to add coverage where the role's dimension is not required would violate the "no distinctions without materially different requirement matrices" principle (APP-5 Appendix D rationale).

#### 7.6.4 Multi-role scope

Per APP-5 §1.3 (unchanged from v1.4), when an implementation declares multiple roles (e.g., GO + TC), the applicable dimensions are the union of all declared-role dimensions and the applicable requirements are the union of all per-role requirement matrices. In multi-role scope, Objective coverage inherits from the union.

**Example — GO + TC at L3:** GO carries all 5 dimensions and covers all 5 Objectives; TC adds Evidence + Security obligations at L3. The composite implementation covers all 5 Objectives with GO-side full realisation plus TC-side contribution-specific requirements (CORE-L3-01 enhanced telemetry becomes mandatory).

**Example — AB + ED at L2:** AB carries Specification + Security; ED carries Governance + Security. The composite covers O-1 (AB agent identity + ED authority config), O-2 (ED policy config), O-3 (AB substrate isolation + ED degradation config), O-5 (ED policy approval). O-4 remains not applicable (neither role carries Evidence dim).

#### 7.6.5 Domain profile impact

Per APP-5 §6 (unchanged from v1.4), domain profiles (BFSI, Healthcare, UAE/DIFC) are additive-only and cannot weaken base requirements. Domain profile obligations layer onto the base role × L-level coverage without changing Objective applicability. For example:

- **BFSI CONF-DP-BFSI-03** elevates dual-human approval on financial P→D promotion from SHOULD (SEC-S8-03 baseline) to MUST — strengthens O-5 coverage without changing which roles it applies to.
- **Healthcare CONF-DP-HC-05** adds breach notification capability on SEC-S5-01 / SEC-S4-01 failures involving PHI — strengthens O-4 coverage without changing which roles it applies to.
- **UAE/DIFC CONF-DP-UAE-01** locks jurisdictional privacy tier to Tier A — strengthens O-3 coverage on ED role without changing base Objective applicability.

#### 7.6.6 Wave 1 recovery-evidence coverage

The Wave 1 additions (CORE-A2-13, CORE-A2-14, CORE-A4-06, SEC-S6-05) inherit the same role × L-level applicability discipline. Verified per role:

| Wave 1 ID | GO | TC | AB | ED | FD | L-level |
|:---|:---|:---|:---|:---|:---|:---|
| CORE-A2-13 (recovery_evidence schema, 7 fields incl. `sequence`) | ✅ Emit recovery evidence in PxER (APP-5 §4.1.1) | ❌ Not independently applicable — GO assembles recovery evidence; TC contributes step-level evidence via CORE-L3-01 which becomes input to GO's recovery evidence assembly, but TC has no independent CORE-A2-13 obligation | — | — | — | L2+ |
| CORE-A2-14 (recovery outcome vocabulary, 5 values) | ✅ Enforce vocabulary in PxER (APP-5 §4.1.1) | ❌ Not independently applicable — GO enforces vocabulary; TC contributions using the vocabulary in `outcome`-analog fields are consumed by GO but TC has no independent CORE-A2-14 obligation | — | — | — | L2+ |
| CORE-A4-06 (recovery-decision accountability) | ✅ Extend A4-01 chain to recovery decisions (APP-5 §4.1.1) | — (TC contributes; does not decide) | — | — | — | L2+ |
| SEC-S6-05 (recovery-path enforcement-tier invariant, dependency on CORE-A6-03) | ✅ Enforce tier parity on recovery paths (APP-5 §4.1.2) | — | ✅ Enforce tier parity on agent recovery paths (via AB SEC matrix; SEC-XX-01 TAO applies) | ✅ Configure recovery-path policy (tier constraints, permitted paths per step class) | — | L2+ |

**Recovery-record assembly ownership.** The recovery-record assembly obligation is assigned exclusively to the Governance Orchestrator role. Telemetry Contributors have no independent CORE-A2-13 or CORE-A2-14 obligation. TC contributions using recovery-outcome language in CORE-L3-01 telemetry are consumed by GO as input to GO's recovery-record assembly, but a TC that emits step-level evidence without a `recovery_evidence` block is conformant to the TC role — GO is responsible for aggregating and structuring recovery records in the PxER it assembles. Any language in APP-5 §4.2 (Telemetry Contributor) suggesting an independent TC recovery obligation is superseded by this clarification.

Zero gaps introduced by Wave 1. Verification against APP-5: matrices in §4.1.1, §4.1.2, §4.3.2 confirm the presence of the referenced IDs.

#### 7.6.7 v3.8/v3.9/v3.10 cascade coverage verification (added v1.11)

Beyond the Wave 1 additions, APP-3 and APP-2 introduce additional requirements. All are reflected in APP-5 role matrices. Verified per role:

| Cascade ID | GO | TC | AB | ED | FD | L-level | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| SEC-XX-02 (substrate isolation) | ✅ (APP-5 §4.1.2) | ✅ (contributor substrate scope) | ✅ (AB-hosted agent substrate scope) | ✅ (deployment-time substrate declaration) | ✅ (activation-time substrate verification) | L1–L4 | Cross-cutting; universal applicability |
| SEC-XX-03 (authority reduction, SHOULD) | ✅ (APP-5 §4.1.2, RP) | — | — | — | — | L2–L4 | Recommended Pattern; floor is SEC-XX-05 |
| SEC-XX-04 (adversarial verification) | ✅ (APP-5 §4.1.2) | ✅ (contributor-side verification) | ✅ (AB-side verification) | — | ✅ (activation-time coverage verification) | L1–L4 | Cross-cutting; adversarial exercise suite |
| SEC-XX-05 (minimum safe-state transition) | ✅ (APP-5 §4.1.2) | ✅ (contributor safety-event honouring) | ✅ (AB-hosted agent safe-state honouring) | ✅ (deployment-time safe-state policy) | ✅ (activation-time safe-state verification) | L1–L4 | Cross-cutting; MUST floor for SEC-XX-03 per APP-1 Article 3 |
| SEC-S2-06 (compositional authority accumulation) | ✅ (APP-5 §4.1.2) | — | ✅ (AB delegation composition — added AB matrix v1.5) | — | — | L2+ | Reach cap on composed authority |
| SEC-S3-07 (cross-family verification, attestation-based) | ✅ (APP-5 §4.1.2) | — | — | — | — | L2+ | Attestation schema |
| SEC-S5-06 (agent safety-event channel) | ✅ (APP-5 §4.1.2) | — | ✅ (agent-side channel invocation) | — | — | L2+ | Nine-element control contract |
| SEC-S6-04 (governance-control integrity monitoring) | ✅ (APP-5 §4.1.2) | — | — | ✅ (deployment-time control-integrity configuration) | — | L2+ | Configuration-change protection |
| SEC-S7-03 (coordination-pattern detectability) | ✅ (APP-5 §4.1.2) | ✅ (contributor telemetry emission) | ✅ (AB-side telemetry emission) | — | — | L2+ | Telemetry obligation; not detection algorithm |
| SEC-S9-03 (evidence-vs-learning quarantine) | ✅ (APP-5 §4.1.2) | — | — | — | — | L2+ | Adaptive-learning boundary |
| SEC-S13-03 (authority-provenance invariant) | ✅ (APP-5 §4.1.2) | — | ✅ (AB delegation-chain peer-message rejection) | — | — | L2+ | Peer messages are non-qualifying elevation sources |

**Result — zero coverage gaps for the cross-cutting additions.** Every requirement present in APP-3 is reflected in APP-5 role matrices with role assignments consistent with the dimension applicability structure (APP-5 §2.2). SEC-XX-* cross-cutting principles apply broadly across roles; role-specific SEC requirements apply where the role's dimension responsibility carries them.

**Cross-cutting effect on Objectives.**
- **O-3 Bounded Agency** gains SEC-XX-05 as a first-class floor for the "cannot continue privileged actions past detected severe event" outcome. Prior v1.10 §7.6.2 assigned SEC-XX-01/02 to O-3 for GO; SEC-XX-05 augments this at the same role scope.
- **O-1 Authorised Action** gains SEC-S13-03 (authority-provenance invariant) as a first-class control against peer-authority substitute failure. Prior v1.10 §7.6.2 assigned SEC-S13-01 to O-1 for GO; SEC-S13-03 augments this.
- **O-5 Governed Change** gains SEC-S9-03 (evidence-vs-learning quarantine) and SEC-S6-04 (governance-control integrity monitoring) as first-class controls against silent governance-configuration weakening.

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 1.15
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-IG-02 — Cross-Reference Matrix.*
