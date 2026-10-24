# APP-5

Agentic Process Protocol

## Conformance Profiles

| | |
|:---|:---|
| **Version** | 1.10 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Audience** | Protocol implementors, ERP vendor architects, agent builder platform teams, enterprise governance teams, conformance assessors |
| **Normative status** | This document is normative per profile. Governed by APP-1. |
| **Companion documents** | APP-0, APP-1 (Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-IG-02 (Cross-Reference Matrix), APP-R1 (Frame Schema), APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) — v1.10 adds a reference-artefact note to §5.2 pointing conformance assessors at APP-R1 and APP-R2 as illustrative artefacts the Specification Dimension tests may be run against. No test ID, procedure, or pass criterion changed. |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. Version bumps require concurrent manifest regeneration; adding a version to the manifest without concurrent bump of that document, or vice versa, is a release-control defect. |
| **Version-reference convention** | Companion documents cited by name only in body prose. Manifest above is the sole non-historical source for companion versions. Version numbers persist in body prose only for historical claims about specific past changes. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-5 is the normative conformance specification of the Agentic Process Protocol. It aggregates APP-2, APP-3, and APP-4 requirements into role-based conformance profiles across the five participant roles at each maturity level.
>
> **Status:** Normative. Requirements expressed using RFC 2119/8174 keywords are binding within the declared scope.
>
> **Authority and precedence:** Governed by APP-1. APP-5 prevails on conformance-specific matters where conformance interpretation is required.
>
> **Use this document for:** Role-based conformance obligations (Governance Orchestrator, Telemetry Contributor, Agent Builder Platform, Enterprise Deployer, Field Deployment), L-level applicability, testable criteria, and conformance-declaration schema.
>
> **Related documents:** APP-0/1/2/3/4 (source of requirements aggregated here), APP-IG-01 (implementation guidance), APP-IG-02 (traceability), APP-IG-03 (worked example).

---

## How to Read This Document

This document uses RFC 2119/8174 normative keywords. MUST, SHOULD, MAY in all capitals carry their defined meanings. When used in lower case, these words are descriptive only and carry no normative weight.

Normative elements are classified at exactly one of three specificity levels (APP-1 Article 4):

| Marker | Level | Meaning |
|:---|:---|:---|
| **[Required Outcome]** | What must be true | Verifiable outcome using MUST. Any conformant mechanism qualifies. |
| **[Recommended Pattern]** | How the protocol suggests achieving it | Expressed using SHOULD. Alternatives documented. Deviation requires justification. |
| **[Reference Mechanism]** | A specific mechanism proposed | Informative. Working group starting point. |

Conformance requirement IDs in this document use `CONF-Rn-nn` for role-based requirements (R = role abbreviation, nn = sequence), `CONF-D-nn` for dimension requirements, `CONF-T-nn` for testable criteria, and `CONF-DP-nn` for domain-specific profile requirements. When referenced from documents outside the APP series, prefix with `APP-` (e.g., `APP-CONF-RGO-01`).

Role abbreviations: GO = Governance Orchestrator, TC = Telemetry Contributor, AB = Agent Builder Platform, ED = Enterprise Deployer, FD = Field Deployment.

---

## 1. Introduction

### 1.1 What This Specification Defines

APP-2 defines WHAT protocol capabilities exist (A0–A11) and at which integration maturity levels (L1–L4) each requirement applies. APP-3 defines WHAT security requirements exist per domain (S1–S14) and their L-level applicability. APP-4 defines WHAT entity correlation requirements exist (EC-01 through EC-47, plus EC-01a). None of these documents answers the implementor's question: **"I am an ERP vendor building L3 conformance. Exactly which CORE, SEC, and EC requirements apply to me, which are testable at my declared level, and how do I demonstrate conformance?"**

This specification answers that question. It defines:

- **Conformance dimensions** — the orthogonal axes on which conformance is independently reported (§2).
- **Participant roles** — the five protocol roles with distinct conformance obligations (§3).
- **Per-role requirement matrices** — the authoritative mapping from each role to its applicable CORE, SEC, and EC requirements by L-level (§4).
- **Testable conformance criteria** — the objective test for each MUST-level requirement (§5).
- **Domain-specific profiles** — additional requirements for regulated industries and jurisdictions (§6).
- **Interoperability verification** — the "two independent implementations" rule and what constitutes interoperable conformance (§7).

### 1.2 Relationship to Other APP Documents

| Document | Relationship |
|:---|:---|
| **APP-1 (Constitution)** | Governs this document. Article 5 mandates role-based, decomposed conformance. Constitution prevails on conflict. |
| **APP-2 (Core Specification)** | Source of CORE-* requirements. §4.4 defines conformance profiles (Preventive/Detective/Retrospective) and CORE-CP-01 through CP-04. This document assigns those requirements to roles. |
| **APP-3 (Security Architecture)** | Source of SEC-* requirements. §6 defines minimum security obligations per role. This document formalises and extends those obligations into testable criteria. |
| **APP-4 (Entity Correlation)** | Source of EC-* requirements. This document assigns entity correlation obligations to roles. |
| **APP-IG-02 (Cross-Reference Matrix)** | Authoritative cross-document mapping. This document's requirement matrices are consistent with APP-IG-02; where discrepancy exists, this document prevails for conformance purposes. |

### 1.3 Conformance Scope

Conformance is assessed per **deployment scope** — a specific combination of participant role, declared integration maturity level (L1–L4), and declared conformance profile (Preventive/Detective/Retrospective). A single implementation may serve multiple roles and operate at different L-levels for different process scopes.

**[Required Outcome · CONF-D-01]** Implementations MUST declare their conformance scope: participant role(s), L-level per scope, and conformance profile per scope. Undeclared scope is non-conformant.

When an implementation declares multiple roles, conformance is assessed per role independently. The applicable dimensions are the union of all declared-role dimensions. The applicable requirements are the union of all per-role requirement matrices (§4.1–§4.5) — the implementation must satisfy every requirement from every declared role at the declared L-level. For example, an implementation serving as both Governance Orchestrator and Telemetry Contributor must satisfy all GO dimension requirements AND all TC dimension requirements — the Learning dimension is required (from GO), not optional despite being "—" for TC. Each dimension carries a single conformance status reflecting the highest applicable obligation across all declared roles.

---

## 2. Conformance Dimensions

APP-1 Article 5 requires: "Composite levels MUST NOT hide weaknesses in any dimension; each dimension is reported independently." This section defines the orthogonal dimensions.

### 2.1 Dimension Definitions

**[Required Outcome · CONF-D-02]** Conformance MUST be reported independently across five dimensions:

| Dimension | Question Answered | Source Requirements |
|:---|:---|:---|
| **Specification** | Can the implementation produce and consume conformant Process Frames? | CORE-A0-*, CORE-A1-*, EC-01–EC-06 |
| **Evidence** | Does the implementation produce conformant PxER records? | CORE-A2-*, CORE-A3-*, EC-07–EC-11 |
| **Governance** | Are D/P classification, HITL quality, compliance, and accountability enforced? | CORE-A3-*, CORE-A4-*, CORE-A5-*, CORE-A6-*, CORE-A7-* |
| **Security** | Are applicable SEC requirements met? | SEC-S1-* through SEC-S14-*, SEC-XX-01 |
| **Learning** | Are A8–A11 outputs produced and entity correlation sustained? | CORE-A8-* through CORE-A11-*, CORE-A9-*, CORE-A10-*, EC-15–EC-33 |

**[Required Outcome · CONF-D-03]** Each dimension MUST carry an independent conformance status per deployment scope:

| Status | Meaning |
|:---|:---|
| **Conformant** | All applicable MUST-level requirements for the declared role and L-level are met. |
| **Partially Conformant** | Some applicable MUST-level requirements are met. Non-conformant requirements explicitly declared (per CORE-CP-04). |
| **Non-Conformant** | Applicable MUST-level requirements not met. |

**[Required Outcome · CONF-D-04]** When reporting conformance, the dimension-level status MUST be accompanied by the list of unmet MUST-level requirements for each dimension with status other than Conformant. A "Conformant" aggregate that masks a non-conformant dimension is a conformance violation.

### 2.2 Dimension Applicability by Role

Not every dimension applies equally to every role. The following table defines the minimum applicable dimensions per role:

| Role | Specification | Evidence | Governance | Security | Learning |
|:---|:---|:---|:---|:---|:---|
| **Governance Orchestrator** | Required | Required | Required | Required | Required |
| **Telemetry Contributor** | — | Required | — | Required | — |
| **Agent Builder Platform** | Required | — | — | Required | — |
| **Enterprise Deployer** | — | — | Required | Required | — |
| **Field Deployment** | — | — | — | Required | — |

**Required** = dimension MUST be reported. **—** = dimension does not apply (no conformance obligation).

---

## 3. Participant Roles

APP-1 Article 5 defines conformance as role-based across five participant roles: governance orchestrator, telemetry contributor, agent builder platform, enterprise deployer, and field deployment. This section defines each role's scope and conformance boundary.

### 3.1 Governance Orchestrator

**Scope.** The implementation that manages the Process Frame lifecycle, assembles PxER records, enforces D/P classification, provides HITL approval surfaces, enforces compliance constraints, and produces learning outputs. This is the central governance role.

**Conformance boundary.** Responsible for nearly all CORE, SEC, and EC requirements at the declared L-level. The governance orchestrator is accountable for end-to-end governance integrity.

### 3.2 Telemetry Contributor

**Scope.** An application (typically ERP or enterprise platform) at L3 that contributes intra-application execution telemetry to PxER assembly. The application contributes evidence; it does not orchestrate governance.

**Conformance boundary.** Responsible for contribution format compliance, contributor authentication, evidence tier declaration, and LITL defence on its own approval surfaces. Not responsible for PxER assembly, Frame lifecycle, or learning outputs.

### 3.3 Agent Builder Platform

**Scope.** An AI platform or development environment that consumes Process Frame definitions and contributes changes through the governance gate (A1). Builders invoke governed processes; they do not manage the governance layer.

**Conformance boundary.** Responsible for consuming Frame correctly, submitting changes through the governance gate with proper classification, and meeting transport and identity security requirements. Not responsible for PxER assembly or compliance enforcement.

### 3.4 Enterprise Deployer

**Scope.** The organisation deploying governed processes. Configures tenant-level policies, compliance levels (C3/C4), jurisdictional privacy tiers, and degradation behaviour declarations.

**Conformance boundary.** Responsible for policy configuration completeness, compliance scope declaration, jurisdictional privacy tier assignment, and degradation behaviour declaration per step. Not responsible for protocol implementation mechanics.

### 3.5 Field Deployment

**Scope.** The team or function performing initial deployment setup — source document preparation, L1 integration configuration, credential provisioning, and temporal activation ordering compliance.

**Conformance boundary.** Responsible for source provenance, L1 security controls, and ensuring security controls are active before governed data flows begin. This role operates during the highest-risk deployment phase (APP-3 §6).

---

## 4. Per-Role Requirement Matrices

These matrices are the authoritative source for which requirements apply to each role by L-level. Requirements are drawn from APP-2 (CORE-*), APP-3 (SEC-*), and APP-4 (EC-*).

**Reading convention.**

- `●` — mandatory at this L-level for this role
- `○` — Recommended Pattern at this L-level (SHOULD; deviation requires documented justification)
- `—` — N/A due to architecture: this L-level does not have the capability this requirement addresses (e.g., MCP integration at L1), or the requirement is subsumed by a different L-level's control (e.g., L1 PII gate is subsumed at L2+ by broader security controls)
- **Blank cells MUST NOT occur** in §4 matrices. A blank cell in any §4 matrix is a release-control defect and is to be classified as `●`, `○`, or `—` in the next revision. Historical rationale for architectural non-applicability is documented per matrix section below.

Requirements listed are those where the role bears primary conformance obligation. A requirement that applies to the governance orchestrator does not also appear under telemetry contributor unless the contributor has an independent obligation. §4.1.3 uses an extended marker set (`●`/`○`/`△`/blank) specific to the entity-correlation obligation classes per APP-4 §1.5(d); see §4.1.3 legend.

### 4.1 Governance Orchestrator

#### 4.1.1 CORE Requirements

| ID | Capability | Level | Description | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| CORE-A0-01 | A0 | RO | Mandatory Frame fields per step | ● | ● | ● | ● |
| CORE-A0-02 | A0 | RP | Recommended Frame fields | — | ○ | ○ | ○ |
| CORE-A0-03 | A0 | RM | DAG-JSON interchange format | — | — | — | — |
| CORE-A1-01 | A1 | RO | Outbound + inbound + notification | — | ● | ● | ● |
| CORE-A1-02 | A1 | RO | Governance gate classification | — | ● | ● | ● |
| CORE-A1-03 | A1 | RO | Cross-system mediation | — | ● | ● | ● |
| CORE-A1-04 | A1 | RP | MCP Server Profile transport | — | ○ | ○ | ○ |
| CORE-A1-05 | A1 | RO | Frame schema portability (published schema, consumer validation) | — | ● | ● | ● |
| CORE-A1-06 | A1 | RO | Agent Card schema (conform to declared A2A or equivalent standard) | — | ● | ● | ● |
| CORE-A3-01 | A3 | RO | Declare intended D/P per step | ● | ● | ● | ● |
| CORE-A3-02 | A3 | RO | Record actual execution track | — | ● | ● | ● |
| CORE-A3-03 | A3 | RO | MISMATCH triggers review | — | ● | ● | ● |
| CORE-A3-04 | A3 | RO | Task-level vs orchestration-level P | ● | ● | ● | ● |
| CORE-A3-05 | A3 | RP | Route D-steps to deterministic execution | — | ○ | ○ | ○ |
| CORE-A3-06 | A3 | RO | Independent D/P verification (compliance-critical) | — | ● | ● | ● |
| CORE-A2-01 | A2 | RO | Immutable record, during execution | ● | ● | ● | ● |
| CORE-A2-02 | A2 | RO | Step fields: id, system, timestamp, tx ref | ● | ● | ● | ● |
| CORE-A2-03 | A2 | RO | Conformance + trust schema (7 fields) | ● | ● | ● | ● |
| CORE-A2-04 | A2 | RO | Mismatch type enum | ● | ● | ● | ● |
| CORE-A2-04a | A2 | RO | DEGRADED status: mismatch_type null | ● | ● | ● | ● |
| CORE-A2-05 | A2 | RO | Conformance by maturity level | ● | ● | ● | ● |
| CORE-A2-06 | A2 | RO | Evidence vs. telemetry distinction | ● | ● | ● | ● |
| CORE-A2-07 | A2 | RP | Task-level P-track evidence schema | — | ○ | ○ | ○ |
| CORE-A2-08 | A2 | RP | Orchestration-level P-track evidence schema | — | ○ | ○ | ○ |
| CORE-A2-08a | A2 | RO | Mandatory orchestration P-track fields | — | ● | ● | ● |
| CORE-A2-10 | A2 | RO | Three evidence integrity dimensions | ● | ● | ● | ● |
| CORE-A2-11 | A2 | RO | Cross-enterprise: boundary observation only | — | ● | ● | ● |
| CORE-A2-12 | A2 | RO | Unmanaged: observed invocation only | ● | ● | ● | ● |
| CORE-A2-13 | A2 | RO | Recovery evidence schema (7 fields on recovery-invoked steps) | — | ● | ● | ● |
| CORE-A2-14 | A2 | RO | Recovery outcome controlled vocabulary (5 values) | — | ● | ● | ● |
| CORE-A4-01 | A4 | RO | Three-layer accountability (task) | ● | ● | ● | ● |
| CORE-A4-02 | A4 | RO | PxER execution attribution | ● | ● | ● | ● |
| CORE-A4-03 | A4 | RP | Model version in provenance marker | — | ○ | ○ | ○ |
| CORE-A4-04 | A4 | RO | Orchestration accountability fields | — | ● | ● | ● |
| CORE-A4-05 | A4 | RP | Orchestration completion gate (3 tiers) | — | ○ | ○ | ○ |
| CORE-A4-06 | A4 | RO | Recovery-decision accountability chain (extends A4-01 to recovery) | — | ● | ● | ● |
| CORE-A5-01 | A5 | RO | Two-value authorship marker + weaken-definition | ● | ● | ● | ● |
| CORE-A5-02 | A5 | RO | Frame encoding + PxER evidence | ● | ● | ● | ● |
| CORE-A5-03 | A5 | RO | Constraint-inheritance integrity (authority-reference) | — | ● | ● | ● |
| CORE-A6-01 | A6 | RO | Measured quality, not just approval | ● | ● | ● | ● |
| CORE-A6-02 | A6 | RO | Engagement record minimum fields | ● | ● | ● | ● |
| CORE-A6-03 | A6 | RO | Engagement-fidelity marker (matrix → IG) | — | ● | ● | ● |
| CORE-A6-04 | A6 | RP | Graduated engagement levels | — | ○ | ○ | ○ |
| CORE-A6-05 | A6 | RP | Canary injection | — | ○ | ○ | ○ |
| CORE-A7-01 | A7 | RO | AI-mediated mode parity | — | ● | ● | ● |
| CORE-A7-02 | A7 | RO | Record governed vs. ungoverned paths | ● | ● | ● | ● |
| CORE-A7-03 | A7 | RO | Parity by level | — | ● | ● | ● |
| CORE-A8-01 | A8 | RO | Classification provenance (5 values) | ● | ● | ● | ● |
| CORE-A8-02 | A8 | RO | Promotion evidence fields | ● | ● | ● | ● |
| CORE-A8-03 | A8 | RO | Three promotion outcomes | ● | ● | ● | ● |
| CORE-A8-04 | A8 | RO | Frame transition events | ● | ● | ● | ● |
| CORE-A9-01 | A9 | RO | Lifecycle states (4) | ● | ● | ● | ● |
| CORE-A9-02 | A9 | RO | Transition recording | ● | ● | ● | ● |
| CORE-A9-03 | A9 | RO | Evidence integrity before lifecycle recommendations | — | ● | ● | ● |
| CORE-A10-01 | A10 | RP | Drift signal types (recommended) | — | ● | ● | ● |
| CORE-A10-02 | A10 | RO | Conformance report on declared cadence | — | ● | ● | ● |
| CORE-A10-03 | A10 | RP | Report schema | — | ○ | ○ | ○ |
| CORE-A10-04 | A10 | RO | Evidence integrity before drift signals | — | ● | ● | ● |
| CORE-A11-01 | A11 | RP | Process intelligence (recommended) | — | ● | ● | ● |
| CORE-A11-02 | A11 | RP | Standardised output schema | — | ○ | ○ | ○ |
| CORE-L3-01 | L3 | RO | L3 Enhanced telemetry schema (6 minimum fields) | — | — | ● | — |
| CORE-CP-01 | §4.4 | RO | Declare profile per scope | ● | ● | ● | ● |
| CORE-CP-02 | §4.4 | RO | Multi-profile; honour declared | ● | ● | ● | ● |
| CORE-CP-03 | §4.4 | RO | Conformance test (4 criteria) | ● | ● | ● | ● |
| CORE-CP-04 | §4.4 | RO | Declare partial conformance | ● | ● | ● | ● |
| CORE-XX-01 | §6 | RO | Compliance-tiered graceful degradation | ● | ● | ● | ● |
| CORE-XX-02 | §6 | RO | Degradation security | ● | ● | ● | ● |

#### 4.1.2 SEC Requirements

| ID | Domain | Level | Description | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| SEC-XX-01 | Principle | RO | Temporal Activation Ordering | ● | ● | ● | ● |
| SEC-XX-02 | Principle | RO | Substrate isolation | ● | ● | ● | ● |
| SEC-XX-03 | Principle | RP | Authority reduction on uncertainty | — | ○ | ○ | ○ |
| SEC-XX-04 | Principle | RO | Adversarial verification obligation | ● | ● | ● | ● |
| SEC-XX-05 | Principle | RO | Minimum safe-state transition on detected severe events | ● | ● | ● | ● |
| SEC-S1-01 | S1 | RO | Signed Frame mutations | — | ● | ● | ● |
| SEC-S1-02 | S1 | RO | Mutation provenance chain | — | ● | ● | ● |
| SEC-S1-03 | S1 | RO | Monotonic version enforcement | — | ● | ● | ● |
| SEC-S1-04 | S1 | RO | Source document provenance | — | ● | ● | ● |
| SEC-S1-05 | S1 | RP | Semantic validation at submission | — | ○ | ○ | ○ |
| SEC-S2-01 | S2 | RO | MCP Conformance Profile | — | ● | ● | ● |
| SEC-S2-02 | S2 | RO | Agent Card signing | — | ● | ● | ● |
| SEC-S2-03 | S2 | RO | Session continuity integrity | — | ● | ● | ● |
| SEC-S2-04 | S2 | RO | Agent Card export security review | — | ● | ● | ● |
| SEC-S2-05 | S2 | RP | Delegation chain depth cap | — | ○ | ○ | ○ |
| SEC-S2-06 | S2 | RO | Compositional authority accumulation | — | ● | ● | ● |
| SEC-S3-01 | S3 | RO | Independent D/P verification | — | ● | ● | ● |
| SEC-S3-02 | S3 | RO | Adversarial D/P test suite | — | ● | ● | ● |
| SEC-S3-06 | S3 | RO | D-track scope validation at request time | — | ● | ● | ● |
| SEC-S3-07 | S3 | RO | Cross-family independent verification (attestation-based) | — | ● | ● | ● |
| SEC-S4-01 | S4 | RO | Async evidence verification (declared SLA) | ● | ● | ● | ● |
| SEC-S4-02 | S4 | RO | Evidence tier classification | ● | ● | ● | ● |
| SEC-S4-04 | S4 | RO | Tiered trust for new contributors (GO enforcement) | — | — | ● | ● |
| SEC-S4-05 | S4 | RO | Write-path authentication (six enumerated artifact classes) | ● | ● | ● | ● |
| SEC-S4-06 | S4 | RO | Evidence-record erasure reconciliation | ● | ● | ● | ● |
| SEC-S5-01 | S5 | RO | LITL defence (verified surfaces) | ● | ● | ● | ● |
| SEC-S5-02 | S5 | RO | Randomised canary schedule | — | ● | ● | ● |
| SEC-S5-03 | S5 | RO | Engagement authenticity detection | — | ● | ● | ● |
| SEC-S5-04 | S5 | RO | Per-dimension telemetry privacy | — | ● | ● | ● |
| SEC-S5-05 | S5 | RO | Jurisdictional privacy tiers | — | ● | ● | ● |
| SEC-S5-06 | S5 | RO | Agent-initiated safety-event channel | — | ● | ● | ● |
| SEC-S6-01 | S6 | RO | Constraint completeness (negative space) | — | ● | ● | ● |
| SEC-S6-02 | S6 | RO | Compliance exception re-validation on constraint change | — | ● | ● | ● |
| SEC-S6-03 | S6 | RO | Autonomy-mode change elevated review (C0/C1) | — | ● | ● | ● |
| SEC-S6-04 | S6 | RO | Governance-control integrity monitoring | — | ● | ● | ● |
| SEC-S6-05 | S6 | RO | Recovery-path enforcement-tier invariant | — | ● | ● | ● |
| SEC-S7-01 | S7 | RO | Independent signed execution trace | ● | ● | ● | ● |
| SEC-S7-02 | S7 | RO | Compliance-tiered degradation | ● | ● | ● | ● |
| SEC-S7-03 | S7 | RO | Coordination-pattern detectability | — | ● | ● | ● |
| SEC-S8-01 | S8 | RO | Promotion evidence integrity gate | — | ● | ● | ● |
| SEC-S8-02 | S8 | RO | Promotion evidence exclusivity | — | ● | ● | ● |
| SEC-S8-03 | S8 | RO | Dual-human for C0/C1 promotions | — | ● | ● | ● |
| SEC-S8-04 | S8 | RO | Promotion velocity integrity | — | ● | ● | ● |
| SEC-S9-01 | S9 | RO | Evidence integrity before advisory | — | ● | ● | ● |
| SEC-S9-02 | S9 | RO | Governance-weakening elevated approval | — | ● | ● | ● |
| SEC-S9-03 | S9 | RO | Evidence-vs-learning quarantine | — | ● | ● | ● |
| SEC-S10-01 | S10 | RO | Differential privacy for analytics | — | — | ● | ● |
| SEC-S10-02 | S10 | RO | Federated analytics architecture | — | — | ● | ● |
| SEC-S10-03 | S10 | RP | AI red team for leakage | — | — | ○ | ○ |
| SEC-S11-01 | S11 | RO | Template marketplace signing + provenance | — | — | — | ● |
| SEC-S11-01a | S11 | RO | Consumer-side template signature verification | — | ● | ● | ● |
| SEC-S11-02 | S11 | RO | Version-pinning enforcement | — | ● | ● | ● |
| SEC-S11-03 | S11 | RP | Certification lifecycle | — | — | — | ○ |
| SEC-S13-01 | S13 | RO | Session-contextual identity binding | — | ● | ● | ● |
| SEC-S13-02 | S13 | RO | Session token PxER retention | — | ● | ● | ● |
| SEC-S13-03 | S13 | RO | Authority-provenance invariant | — | ● | ● | ● |
| SEC-S14-01 | S14 | RO | Cross-tenant entity type leakage prevention | ● | ● | ● | ● |
| SEC-S14-02 | S14 | RO | Entity field path exposure minimisation | ● | ● | ● | ● |
| SEC-S14-03 | S14 | RO | Entity data inherits PxER access controls | ● | ● | ● | ● |
| SEC-S14-04 | S14 | RO | Cross-tenant entity correlation prohibited | ● | ● | ● | ● |
| SEC-S14-05 | S14 | RO | Cross-enterprise entity refs: boundary-observable | — | ● | ● | ● |
| SEC-S14-06 | S14 | RO | Populated source authentication | — | ● | ● | ● |
| SEC-S14-07 | S14 | RO | Reconciliation signal access control | — | ● | ● | ● |
| SEC-S14-08 | S14 | RO | Registry tenant isolation + boundary limits | — | ● | ● | ● |
| SEC-S14-09 | S14 | RO | Declared retention per compliance scope | ● | ● | ● | ● |

#### 4.1.3 EC Requirements

**Reading this table.** Entity correlation requirements are grouped into three obligation classes per APP-4 §1.5(d):

- **Class 2 — Correlation infrastructure capability.** The L2+ Governance Orchestrator MUST support this capability regardless of whether any Frame declares `entity_extract`. This is a capability obligation, not a use obligation.
- **Class 1 — Per-step entity reference production.** The obligation fires only when a Frame step declares `entity_extract`. Absence of `entity_extract` on any step MUST NOT prevent step execution (EC-06).
- **Class 3 — Entity-correlation-specific security.** The obligation applies wherever entity data flows through the implementation. At L2+ this is effectively unconditional because Class 2 infrastructure means data can flow; at L1 it is conditional on Class 1 activity.

**Cell markers:**

- `●` = required capability at this level
- `○` = required when `entity_extract` declared on the Frame step
- `△` = required whenever entity data flows through the implementation
- `—` = N/A due to architecture at this L-level (aligned with suite-wide §4 reading convention, v1.8)

**Per-row applicability semantics are authoritative in APP-4 §1.5(d) and APP-4 §3.** This table is the APP-5 conformance-applicability view; the APP-4 sections carry the definitional detail. Where this table and APP-4 disagree, APP-4 prevails and this table is corrected in the next revision.

*Class 2 — Correlation infrastructure capability (L2+ required regardless of use)*

| Requirement | Section | Level | Conformance evidence | L1 | L2 | L3 | L4 |
|:---|:---|:---:|:---|:---:|:---:|:---:|:---:|
| EC-04 (auto-generation from MCP schemas) | §3.1 | RP | `T-EC-04` | — | ● | ● | — |
| EC-15 (inferred-mode correlation support) | §3.4.1 | RO | `T-LEARN-11` | — | ● | ● | ● |
| EC-16 (inferred correlation minimum fields) | §3.4.1 | RO | `T-LEARN-11` | — | ● | ● | ● |
| EC-17 (process-scoped → global promotion) | §3.4.1 | RO | `T-EC-17` (note 1) | — | ● | ● | ● |
| EC-18 (recency-weighted confidence) | §3.4.1 | RP | `T-EC-18` | — | ● | ● | ● |
| EC-19 (populated-mode correlation support) | §3.4.2 | RO | `T-EC-19` | — | ● | ● | ● |
| EC-20 (source-agnostic import schema) | §3.4.2 | RO | `T-EC-20` | — | ● | ● | ● |
| EC-21 (populated correlation minimum fields) | §3.4.2 | RO | `T-EC-21` | — | ● | ● | ● |
| EC-22 (reconciliation five-outcome status) | §3.4.3 | RO | `T-LEARN-12` (note 2) | — | ● | ● | ● |
| EC-23 (divergent status as operational signal) | §3.4.3 | RO | `T-LEARN-12` | — | ● | ● | ● |
| EC-24 (inferred_only as discovery signal) | §3.4.3 | RP | `T-EC-24` | — | ● | ● | ● |
| EC-25 (persistent entity correlation registry) | §3.5 | RO | `T-EC-25` | — | ● | ● | ● |
| EC-26 (registry entry minimum fields) | §3.5 | RO | `T-EC-26` | — | ● | ● | ● |
| EC-27 (correlation drift detection) | §3.5 | RP | `T-EC-27` | — | ● | ● | ● |
| EC-28 (materialised lookup index) | §3.5 | RP | `T-EC-28` | — | ● | ● | ● |
| EC-31 (stable correlations as P→D candidates) | §3.7 | RO | `T-EC-31` | — | ● | ● | ● |
| EC-32 (correlation drift as A10 signal) | §3.7 | RO | `T-EC-32` | — | ● | ● | ● |
| EC-33 (entity-enriched process intelligence) | §3.7 | RP | `T-EC-33` | — | ● | ● | ● |
| EC-35 (graceful degradation: correlation unavailable) | §5 | RO | `T-EC-35` (note 3) | — | ● | ● | ● |

*Class 1 — Per-step entity reference production (use-conditional on `entity_extract`)*

| Requirement | Section | Level | Conformance evidence | L1 | L2 | L3 | L4 |
|:---|:---|:---:|:---|:---:|:---:|:---:|:---:|
| EC-01 (entity_extract declaration format) | §3.1 | RO | `T-SPEC-05` | ○ | ○ | ○ | ○ |
| EC-01a (entity_extract changes are Frame mutations) | §3.1 | RO | `T-SPEC-05a` | ○ | ○ | ○ | ○ |
| EC-02 (entity role classifications) | §3.1 | RO | `T-SPEC-05` | ○ | ○ | ○ | ○ |
| EC-03 (tenant-scoped entity type registry) | §3.1 | RP | `T-EC-03` | — | ○ | ○ | ○ |
| EC-05 (fidelity by maturity level) | §3.1 | RO | `T-EC-05` | ○ | ○ | ○ | ○ |
| EC-06 (no-gate: core APP-2 without entity enrichment) | §3.1 | RO | `T-SPEC-06` | ● | ● | ● | ● |
| EC-07 (entity_refs in PxER when entity_extract present) | §3.2 | RO | `T-EVID-11` | ○ | ○ | ○ | ○ |
| EC-08 (entity_ref minimum fields) | §3.2 | RO | `T-EVID-11` | ○ | ○ | ○ | ○ |
| EC-09 (extraction method values) | §3.2 | RP | `T-EC-09` | ○ | ○ | ○ | ○ |
| EC-10 (confidence indicator per reference) | §3.2 | RP | `T-EC-10` | — | ○ | ○ | ○ |
| EC-11 (instance-level entity_correlations block) | §3.2 | RO | `T-EC-11` | ○ | ○ | ○ | ○ |
| EC-12 (tenant-scoped entity type labels) | §3.3 | RO | `T-EC-12` | ○ | ○ | ○ | ○ |
| EC-13 (cross-process label consistency) | §3.3 | RP | `T-EC-13` | — | ○ | ○ | ○ |
| EC-14 (labels optional for inference) | §3.3 | RO | `T-EC-14` | ○ | ○ | ○ | ○ |
| EC-29 (integration flow references on Frame steps) | §3.6 | RP | `T-EC-29` | — | ○ | ○ | ○ |
| EC-30 (post-execution entity flow verification) | §3.6 | RP | `T-EC-30` | — | ○ | ○ | ○ |
| EC-34 (graceful degradation: extraction failure) | §5 | RO | `T-EC-34` (note 3) | ○ | ○ | ○ | ○ |

*Class 3 — Entity-correlation-specific security (wherever entity data flows)*

| Requirement | Section | Level | Conformance evidence | L1 | L2 | L3 | L4 |
|:---|:---|:---:|:---|:---:|:---:|:---:|:---:|
| EC-38 (cross-tenant entity type leakage prevention) | §3.1 | RO | `T-SEC-S14-01` | △ | ● | ● | ● |
| EC-39 (entity field path exposure minimisation) | §3.1 | RO | `T-SEC-S14-02` | △ | ● | ● | ● |
| EC-40 (entity data inherits PxER access controls) | §3.2 | RO | `T-SEC-S14-03` | △ | ● | ● | ● |
| EC-41 (cross-tenant entity correlation prohibited) | §3.2 | RO | `T-SEC-S14-04` | △ | ● | ● | ● |
| EC-42 (cross-enterprise entity refs boundary-observable only) | §3.2 | RO | `T-SEC-S14-05` (note 4) | — | ● | ● | ● |
| EC-43 (populated source authentication) | §3.4.3 | RO | `T-SEC-S14-06` (note 4) | — | ● | ● | ● |
| EC-44 (correlation data tenant isolation) | §3.4.3 | RO | `T-SEC-S14-07a` (note 4) | — | ● | ● | ● |
| EC-45 (reconciliation signal access control) | §3.4.3 | RO | `T-SEC-S14-07b` (note 4) | — | ● | ● | ● |
| EC-46 (registry tenant isolation) | §3.5 | RO | `T-SEC-S14-08` (note 4) | — | ● | ● | ● |
| EC-47 (registry cross-enterprise boundary-observable only) | §3.5 | RO | `T-SEC-S14-09` (note 4) | — | ● | ● | ● |

**Notes.**

1. **EC-17 (process-scoped → global promotion):** global-scope promotion requires cross-Frame evidence bundle plus the five-field EC-17 governance audit per APP-4 §3.4.1. Multiple instances of one Frame are not cross-Frame evidence and cannot alone justify `scope: global`.
2. **EC-22 (reconciliation):** the `error` status defaults to advisory-only. Enforcement (compliance gating, access decisions, execution blocking) requires explicit deployment-policy permission per APP-4 §3.4.3. Default fail-closed on `error` is non-conformant. The other four statuses (`aligned`, `divergent`, `populated_only`, `inferred_only`) carry their own allowable-enforcement rules per APP-4 §3.4.3.
3. **EC-34 and EC-35 graceful-degradation semantics:** EC-34 addresses extraction failure and is Class 1 — the obligation fires wherever extraction is attempted (`○`). EC-35 addresses correlation-engine unavailability and is Class 2 — the obligation fires wherever the correlation infrastructure is required (`●` at L2+).
4. **EC-42 through EC-47 L1 non-applicability:** these Class 3 IDs are transitively bound to Class 2 features (populated mode, correlation registry, reconciliation, cross-enterprise references). At L1 the Class 2 feature is not present, so the Class 3 security control has no corresponding data flow to protect. Blank at L1 reads as "not applicable due to Class 2 absence," not "not required."
5. **Conformance evidence naming convention:** test IDs matching existing APP-5 §5 tests are the authoritative reference (e.g., `T-SPEC-05`, `T-SPEC-05a`, `T-SPEC-06`, `T-EVID-11`, `T-LEARN-11`, `T-LEARN-12`). Test IDs marked `T-EC-{ID}` and `T-SEC-S14-{ID}` are placeholder pointers to be authoritatively named at v1.0 §5 regeneration; the placeholder scheme resolves 1:1 to full test entries with pass/fail criteria at v1.0.

---

### 4.2 Telemetry Contributor (L3+)

The telemetry contributor role exists only at L3 and above. L1 and L2 systems do not contribute intra-application telemetry and therefore have no telemetry contributor obligations.

**Responsibility-boundary statement.** The following is a **normative responsibility-boundary statement** for the Telemetry Contributor role, elevated above the requirement matrices:

> **A Telemetry Contributor MUST supply any required source evidence under its own applicable controls (CORE-A2-02, CORE-A2-03, CORE-L3-01, CORE-A7-02, and the S-domain security controls in §4.2.2), but MUST NOT be assessed as the PxER recovery-record assembler.** Recovery-record assembly (CORE-A2-13, CORE-A2-14, CORE-A4-06) is exclusively the Governance Orchestrator's obligation per §4.1.1. A TC contribution using recovery-outcome language in the CORE-L3-01 telemetry schema is consumed by GO as source input to GO's recovery-record assembly, not as evidence of TC's own recovery obligation; a TC that emits step-level telemetry without any `recovery_evidence` block is fully conformant to the TC role. Assessors evaluating TC conformance MUST NOT count absence of a TC-produced `recovery_evidence` block as non-conformance.

This is not a buried clarification: it is the boundary condition that scopes what the following matrices assess.

#### 4.2.1 CORE Requirements

| ID | Capability | Level | Description | L3 | L4 |
|:---|:---|:---|:---|:---|:---|
| CORE-A2-02 | A2 | RO | Step fields: id, system, timestamp, tx ref (contributed data) | ● | ● |
| CORE-A2-03 | A2 | RO | Conformance schema fields (contributed data) | ● | ● |
| CORE-L3-01 | L3 | RO | L3 Enhanced telemetry schema (6 minimum fields) | ● | — |
| CORE-A7-02 | A7 | RO | Report governed vs. ungoverned paths for own application | ● | ● |

#### 4.2.2 SEC Requirements

| ID | Domain | Level | Description | L3 | L4 |
|:---|:---|:---|:---|:---|:---|
| SEC-S4-02 | S4 | RO | Evidence tier classification on contributed records | ● | ● |
| SEC-S4-03 | S4 | RO | Contributor authentication (OAuth 2.1 + DPoP) | ● | ● |
| SEC-S4-04 | S4 | RO | Tiered trust for new contributors | ● | ● |
| SEC-S5-01 | S5 | RO | LITL defence on own approval surfaces | ● | ● |

#### 4.2.3 EC Requirements

| ID | Section | Level | Description | L3 | L4 |
|:---|:---|:---|:---|:---|:---|
| EC-07 | §3.2 | RO | entity_refs contribution when entity_extract declared | ● | ● |
| EC-08 | §3.2 | RO | entity_ref minimum fields on contributed data | ● | ● |
| EC-40 | §3.2 | RO | Entity data inherits PxER access controls | ● | ● |

---

### 4.3 Agent Builder Platform

#### 4.3.1 CORE Requirements

| ID | Capability | Level | Description | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|
| CORE-A0-01 | A0 | RO | Consume mandatory Frame fields per step | ● | ● | ● |
| CORE-A1-01 | A1 | RO | Support outbound + inbound + notification | ● | ● | ● |
| CORE-A1-02 | A1 | RO | Submit changes through governance gate | ● | ● | ● |
| CORE-A1-03 | A1 | RO | Cross-system changes via Frame mediation | ● | ● | ● |
| CORE-A1-04 | A1 | RP | MCP Server Profile transport | ○ | ○ | ○ |
| CORE-A1-05 | A1 | RO | Frame schema portability — consume Frame against published schema | ● | ● | ● |
| CORE-A1-06 | A1 | RO | Agent Card schema — conform to declared A2A or equivalent standard | ● | ● | ● |
| CORE-A3-01 | A3 | RO | Declare intended D/P on contributed steps | ● | ● | ● |

#### 4.3.2 SEC Requirements

| ID | Domain | Level | Description | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|
| SEC-S1-01 | S1 | RO | Signed Frame mutations on submitted changes | ● | ● | ● |
| SEC-S2-01 | S2 | RO | MCP Conformance Profile (mTLS, OAuth 2.1, DPoP) | ● | ● | ● |
| SEC-S2-02 | S2 | RO | Agent Card signing | ● | ● | ● |
| SEC-S2-03 | S2 | RO | Session continuity integrity | ● | ● | ● |
| SEC-S2-04 | S2 | RO | Agent Card export security review | ● | ● | ● |
| SEC-S2-05 | S2 | RP | Delegation chain depth cap | ○ | ○ | ○ |
| SEC-S2-06 | S2 | RO | Compositional authority accumulation | ● | ● | ● |
| SEC-S13-01 | S13 | RO | Session-contextual identity binding | ● | ● | ● |
| SEC-S13-02 | S13 | RO | Session token retention | ● | ● | ● |

#### 4.3.3 EC Requirements

Agent builder platforms have no direct entity correlation obligations. Entity extraction is configured on the Process Frame by the governance orchestrator; entity references are contributed to PxER by the governance orchestrator or telemetry contributor.

---

### 4.4 Enterprise Deployer

| ID | Source | Level | Description | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| CORE-A5-01 | A5 | RO | Authorship marker: configure `enterprise-authored` constraints | ● | ● | ● | ● |
| CORE-A5-02 | A5 | RO | Frame encoding of compliance levels per step | ● | ● | ● | ● |
| CORE-CP-01 | §4.4 | RO | Declare conformance profile per scope | ● | ● | ● | ● |
| CORE-CP-04 | §4.4 | RO | Declare partial conformance | ● | ● | ● | ● |
| SEC-S5-05 | S5 | RO | Configure jurisdictional privacy tier per tenant | — | ● | ● | ● |
| SEC-S7-02 | S7 | RO | Declare C2 degradation behaviour per step | ● | ● | ● | ● |
| SEC-S12-01 | S12 | RO | Configure L1 PII classification gate | ● | — | — | — |
| EC-12 | §3.3 | RO | Configure tenant-scoped entity type labels | ● | ● | ● | ● |

---

### 4.5 Field Deployment

| ID | Source | Level | Description | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| SEC-S1-04 | S1 | RO | Verify source document provenance | — | ● | ● | ● |
| SEC-S12-01 | S12 | RO | L1 PII classification gate operational | ● | — | — | — |
| SEC-S12-02 | S12 | RO | L1 credential isolation (dedicated vault) | ● | — | — | — |
| SEC-XX-01 | Principle | RO | TAO: security controls active before data flows | ● | ● | ● | ● |
| SEC-S5-05 | S5 | RO | Verify jurisdiction tier configuration | — | ● | ● | ● |

---

### 4.5a Architectural non-applicability — rationale reference *(v1.8)*

The `—` markers across §4.1 through §4.5 encode "N/A due to architecture" per the §4 reading convention. This subsection documents the recurring architectural patterns behind those markers so a reader does not need per-cell inspection to understand each blank.

**Pattern 1 — L1 blank on L2+ requirement.** L1 is the Screen/RPA integration level. Requirements involving direct system integration (CORE-A1-*: MCP surface, governance gate, cross-system mediation), per-invocation execution observation (CORE-A2-11/13/14: cross-enterprise boundary, recovery evidence), or Frame schema portability across MCP consumers do not apply at L1 because the L1 integration mechanism does not carry those surfaces. Absent those surfaces, the requirements have nothing to attach to. The `—` at L1 means "L1 does not have this integration surface by design," not "L1 implementations may omit this control."

**Pattern 2 — L2/L3/L4 blank on L1-specific requirement (subsumption).** A handful of requirements — SEC-S12-01 (L1 PII classification gate), SEC-S12-02 (L1 credential isolation) — are L1-specific security foundations. At L2+ these foundations are subsumed by broader controls at the API/MCP layer (SEC-S3 classification integrity, SEC-S4 evidence integrity, SEC-S5 HITL security domains). An L2+ implementation is not exempt from the underlying protection; it satisfies the protection through the L2+ control set. The `—` at L2/L3/L4 means "this specific L1 control is subsumed at higher L-levels," not "L2+ implementations may omit this protection."

**Pattern 3 — L4 blank on L2/L3 requirement (native subsumption).** L4 is AI-native — systems produce governance evidence structurally rather than via telemetry contribution. Requirements specific to the L3 telemetry-contribution contract (CORE-L3-01 L3 Enhanced telemetry schema at the L4 column in TC matrices; EC-04 MCP schema auto-generation at L4) are subsumed by the L4-native evidence contract. Again, subsumption means the protection is satisfied differently at L4, not omitted.

**Pattern 4 — CORE-A0-03 all-`—` (Reference Mechanism).** CORE-A0-03 (DAG-JSON interchange format) is a Reference Mechanism (`RM`), not a Required Outcome. Reference Mechanisms are informative technical convergence points, not conformance obligations at any L-level. All-`—` on an `RM` row indicates the reference is informative-only.

**Working-group note.** The architectural non-applicability patterns above are stable across suite revisions. If a working-group review identifies a pattern-3 case where subsumption is *not* actually equivalent at L4 (i.e., L4-native does not cover what L3 telemetry contribution covered), that is a specification defect, not a cell-classification defect. It is resolved by adding a new L4 requirement to the applicable matrix, not by changing the `—` marker.

---

### 4.6 L-level applicability delta *(illustrative, v1.8)*

> ⚠️ **Illustrative content, machine-generated table required at v1.0 release.** This table is a hand-drafted illustrative view of what changes across L-levels for the Governance Orchestrator role. A machine-generated delta table reproducing each count statement from the matrices in §4.1 will be generated at v1.0 release. Discrepancies between this illustrative table and the §4.1 matrices are resolved by §4.1.

The illustrative deltas below apply to the Governance Orchestrator role (the role with the largest applicable requirement set). Roles TC, AB, ED, FD have smaller matrices; per-role delta tables are deferred to v1.0.

#### 4.6.1 GO L1 baseline (illustrative)

- Applicable requirement count: **68** (approximate; regenerate from §4.1.1/§4.1.2/§4.1.3 L1 columns at v1.0).
- Composition: all A-family core capabilities at deployment-time scope (Frame, PxER, D/P, A4 accountability, HITL, compliance encoding, orchestration integrity); L1-specific SEC controls (SEC-S12-01, SEC-S12-02, SEC-XX-01); Class-3 EC security applying to entity data flowing at boundary.

#### 4.6.2 L1 → L2 delta (illustrative)

- Added at L2: MCP/API integration surface requirements; execution-time observation capabilities; broader SEC-S domain coverage (S1 through S13 as applicable); Class-2 EC correlation infrastructure (EC-15, EC-19, EC-22, EC-25); Class-3 EC security expanded to correlation state.
- Approximate added-IDs count: **~104** (illustrative).
- Approximate net L2 count: **172** (illustrative).

#### 4.6.3 L2 → L3 delta (illustrative)

- Added at L3: `CORE-L3-01` (L3 enhanced telemetry schema); `SEC-S4-03` (contributor authentication); `SEC-S10-01`, `SEC-S10-02` (analytics privacy at L3 telemetry contribution boundary); possibly `SEC-S4-04` (tiered trust for new contributors) depending on §4.1.2 authoritative content.
- Approximate added-IDs count: **~6** (illustrative).
- Approximate net L3 count: **178** (illustrative).
- Removed: none.

#### 4.6.4 L3 → L4 delta (illustrative — net zero, added + subsumed)

- Added at L4: `SEC-S11-01` (agent template marketplace controls at L4-native surface).
- Subsumed at L4 (obligations satisfied by L4-native evidence generation rather than by L3 telemetry contribution): `SEC-S4-03` and `SEC-S4-04` telemetry-contributor obligations at L4-native evidence generation are subsumed into the native evidence contract; a system producing governance evidence structurally at L4 satisfies these via the native evidence path rather than via the L3 telemetry-contributor contract.
- Approximate added-IDs count: **~1** (illustrative).
- Approximate subsumed-IDs count: **~1** (illustrative; subsumption is not retirement — the IDs remain applicable to L3 telemetry contributors serving L4 systems).
- Approximate net L4 count: **178** (illustrative; unchanged from L3 due to added ≈ subsumed).

#### 4.6.5 Reproducibility requirement for v1.0

Every count statement in §4.6.1–§4.6.4 MUST be reproducible from the §4.1 role matrices via a mechanical count. At v1.0 release, this section is regenerated from the matrices programmatically and cross-verified against APP-IG-02 §5 L-level counts and §7.3 requirement inventory. Any discrepancy is a release-control defect. The illustrative counts above are working-group discussion inputs, not conformance-assessable claims.

---

### 4.7 Working-group consideration: mandatory conformance declaration schema *(v1.8)*

> **Status: WORKING-GROUP DELIBERATION.** This subsection outlines a proposed normative artefact that is **not yet ratified**. It is included here to give the working group a concrete starting point; nothing in §4.7 is currently binding on implementations.

**Background.** APP-1 Article 5 requires partial conformance to be explicitly declared, and APP-IG-01 (Implementor's Guide) frames enterprise conformance as an aggregate across vendors. There is currently no mandatory declaration schema that lets an assessor evaluate a conformance claim consistently across implementations. Two implementations claiming "L3 GO conformance" today may declare radically different scopes without a shared vocabulary for scope, exclusions, and residual limitations.

**Proposed schema.** The following eight fields are proposed as the minimum set for a mandatory conformance declaration:

| Field | Purpose | Values / format |
|:---|:---|:---|
| Role | Which of the five roles is declared | GO / TC / AB / ED / FD (multi-role declarations enumerate all) |
| L-level | Which integration maturity level is declared | L1 / L2 / L3 / L4 per declared role |
| Access posture | *(Currently informative in APP-IG-01 §4.5.)* How the implementation exposes runtime for governance evidence | Open Direct / Mediated / Closed |
| Process scope | Which processes are governed under the declaration | Named process types + version; or "all processes running on this implementation" |
| Excluded systems | Systems that are within the deployment but explicitly out of scope | Named systems + reason for exclusion |
| Entity-correlation capability | Whether Class-2 EC correlation infrastructure per APP-4 §1.5(d) is implemented | Present / not present / partial (with named EC IDs implemented) |
| Evidence limitations | Known limits on evidence completeness or observability | E.g., "L2 boundary-observed only; no statistical inference"; "L3 telemetry from participating apps only, not enterprise-wide" |
| Residual non-conformances | Requirements not fully satisfied at declaration time | Named requirement IDs + remediation plan + timeline |

**Working-group decision required on:**

1. **Adoption**: is the mandatory-declaration concept adopted at all, or is conformance declaration left as implementation choice? Recommended: adopted. Reason: without shared declaration vocabulary, APP-IG-01 §4.5 aggregate-conformance and APP-1 Article 5 partial-conformance requirements are enforceable only by inspection, not by declaration.
2. **Field set**: are the eight fields above sufficient? Candidate additional fields: (a) *Declared conformance test evidence* — list of APP-5 §5 tests the implementation has passed, and by which assessor; (b) *Third-party validation status* — whether an independent assessor has confirmed the declaration; (c) *Declaration validity period* — when the declaration expires and re-declaration is required.
3. **Location**: should the schema be normative in APP-5 (proposed here), constitutionally required by APP-1 Article 5, or split (constitutional requirement in APP-1, operational schema in APP-5)? Recommended: split — APP-1 requires that partial-conformance declarations exist; APP-5 defines the schema.
4. **Access posture upgrade**: access posture is currently informative in APP-IG-01 §4.5. If mandatory declaration adopts the access-posture field, APP-IG-01 §4.5's status changes to a normative field within the APP-5 schema.
5. **Test surface**: if adopted, APP-5 §5 gains a new test class (`T-DECL-*`) for verifying that a conformance declaration is well-formed against the schema.
6. **Interaction with L-level applicability**: the schema must be compatible with the blank-cell disambiguation (§4.1 matrices distinguishing "N/A due to architecture" from "Not implemented" from "Conditional") — the declaration's residual-non-conformance field is precisely how "Not implemented" gets surfaced.

**Not decided in this revision.** The schema above is a working-group input, not a normative artefact. Implementations are not required to produce this declaration until the schema is ratified in a future APP-5 revision. Adopters are encouraged to draft against the proposed schema and provide feedback on the field set.

---

## 5. Testable Conformance Criteria

APP-1 Article 5 requires: "Every MUST-level requirement MUST be objectively testable." This section defines the conformance test for each MUST-level requirement. Each test specifies the observable behaviour that an implementation MUST demonstrate.

### 5.1 Test Structure

**[Required Outcome · CONF-T-01]** Each conformance test MUST specify: the requirement ID(s) under test, the preconditions, the test procedure, and the pass/fail criteria. Pass/fail is binary — no partial credit per individual test.

**[Required Outcome · CONF-T-02]** The conformance test suite MUST be executable against a running implementation. Paper-based self-assessment is not sufficient for conformance claims.

### 5.2 Specification Dimension Tests

| Test ID. | Requirement(s) | Procedure | Pass Criteria |
|:---|:---|:---|:---|
| T-SPEC-01 | CORE-A0-01 | Submit a Process Frame. | Frame contains per step: step_id, executing_system, intended D/P, dependency chain, accountability owner. |
| T-SPEC-02 | CORE-A1-01 | Invoke outbound, inbound, and notification interactions via the integration surface. | All three patterns operational. |
| T-SPEC-03 | CORE-A1-02 | Submit inbound changes with (a) all governance attributes, (b) partial attributes, (c) no attributes. | (a) merges, (b) routes to enrichment, (c) flagged for full review. |
| T-SPEC-04 | CORE-A1-03 | Submit a cross-system change bypassing Frame mediation. | Change rejected or flagged. |
| T-SPEC-05 | EC-01, EC-02 | Submit a Frame step with entity_extract declaration. | Declaration includes field path, entity type label, and entity role (primary_key/context_key/reference). |
| T-SPEC-05a | EC-01a | Modify an entity_extract declaration on a published Frame step. | Change requires signature (SEC-S1-01). Frame version increments (SEC-S1-03). Rollback to pre-change version blocked without governance approval. |
| T-SPEC-06 | EC-06 | Submit a Frame step without entity_extract. Execute process. | Process executes. PxER produced. Core governance functional. |
| T-SPEC-07 | CORE-A1-05 | (a) Inspect a Frame artifact produced by the implementation. (b) Submit a Frame artifact from a peer implementation. | (a) Implementation publishes a discoverable Frame schema. Frame validates against it. (b) Consumer validates received Frame against the published schema before processing. Schema-non-conformant Frames rejected. |
| T-SPEC-08 | CORE-A1-06 | Inspect Agent Card schema declaration. Consume an Agent Card from a peer implementation. | Implementation declares which Agent Card standard is adopted (A2A or equivalent). Consumed Agent Card validates against the declared standard. Non-conformant cards rejected. |

**Reference artefacts (informative).** For T-SPEC-07, APP-R1 (Frame Schema) is an illustrative reference schema an implementation may validate its own Frame against or publish as its own realisation of CORE-A1-05. For T-SPEC-02, APP-R2 (MCP Binding Reference Design) is an illustrative reference binding whose outbound/inbound/notification mapping satisfies CORE-A1-01 interaction patterns on an MCP transport. Both are non-normative: an implementation using an alternative schema or binding is not disadvantaged for conformance purposes.

### 5.3 Evidence Dimension Tests

| Test ID. | Requirement(s). | Procedure | Pass Criteria |
|:---|:---|:---|:---|
| T-EVID-01 | CORE-A2-01 | Execute a process instance. | PxER assembled during execution, immutable, linked to Frame version. |
| T-EVID-02 | CORE-A2-02 | Inspect PxER step records. | Each record contains: step_id, executing_system, timestamp, transaction reference. |
| T-EVID-03 | CORE-A2-03 | Inspect PxER step records. | Each record contains all 7 conformance schema fields. |
| T-EVID-04 | CORE-A2-04 | Execute a D-intended step through P-track (force mismatch). | PxER records `D_intended_P_executed` mismatch type. |
| T-EVID-04a | CORE-A2-04a | Force governance unavailability during step execution. Inspect PxER. | conformance_status = DEGRADED. mismatch_type is null. |
| T-EVID-04b | CORE-A2-04b | Inspect a representative sample of PxER step records covering all conformance_status × mismatch_type × evidence_method combinations produced by the implementation. | Every observed combination MUST match one of the 10 conformant states (C1–C10) in APP-2 §3.4.1 CORE-A2-04b. Any observed combination not in C1–C10 is a specification defect. (Placeholder: a comprehensive T-STATE-* test class covering all 10 conformant states with per-state pass/fail criteria is planned for v1.0 §5 regeneration.) |
| T-EVID-05 | CORE-A2-05 | At L1/L2: inspect `dp_classification_actual`. At L3: inspect same. | L1/L2: MAY be null, defaults UNVERIFIABLE. L3: per-invocation MATCH/MISMATCH. |
| T-EVID-06 | CORE-A2-06 | Inspect evidence and telemetry records. | Distinct records with separate retention policies and access controls. |
| T-EVID-07 | CORE-A2-10 | Inspect PxER entries. | Three verification dimensions independently assessable: D/P conformance, evidence authenticity, write-path provenance. |
| T-EVID-08 | CORE-A2-11 | Execute a step with `trustBoundaryType: cross-enterprise-external`. | PxER records boundary observation only; no P-track evidence required from external enterprise. |
| T-EVID-09 | CORE-A2-12 | Execute a step with `trustBoundaryType: unmanaged`. | PxER records observed invocation with explicit unmanaged marker. |
| T-EVID-10 | CORE-A3-02 | Execute a process. | Actual execution track recorded per step. |
| T-EVID-11 | EC-07, EC-08 | Execute a step with entity_extract declared. | PxER step record contains entity_refs with entity type, system key, and extraction method. |
| T-EVID-12 | CORE-A2-13 | Execute a step that invokes a recovery path. Inspect PxER step record. | Recovery evidence block attached to the original step (not a new step). Block contains all 7 required fields: `path_class`, `initiator`, `authorized_by`, `outcome`, `evidence_refs`, `latency_ms`, `sequence`. `authorized_by` references a named principal per APP-3 SEC-S13. Repeat recoveries on the same step append with monotonic `sequence`. |
| T-EVID-13 | CORE-A2-14 | Force recovery outcomes: `recovered`, `partial`, `failed`, `bypassed`, `self_healed`. Inspect PxER. | Each outcome recorded from the enumerated vocabulary. `partial` and `failed` trigger A6 engagement. `bypassed` includes rationale in `evidence_refs`. `self_healed` includes observation evidence in `evidence_refs` distinguishing self-healing from unrecorded autonomous decision; without such evidence, MUST be recorded as `recovered`. |

### 5.4 Governance Dimension Tests

| Test ID. | Requirement(s) | Procedure | Pass Criteria |
|:---|:---|:---|:---|
| T-GOV-01 | CORE-A3-01 | Submit a Frame. | Every step declares intended D/P. |
| T-GOV-02 | CORE-A3-03 | Force a D/P mismatch during execution. | Mandatory review triggered with process owner. |
| T-GOV-03 | CORE-A3-04 | Submit a Frame with both task-level P and orchestration-level P steps. | Protocol distinguishes both types. Different evidence requirements applied. |
| T-GOV-04 | CORE-A3-06 | Execute a compliance-critical step. | D/P classification validated by an independent path (not a second invocation of the same classifier). |
| T-GOV-05 | CORE-A4-01 | Inspect PxER step record. | Three-layer accountability chain present: intent, execution, oversight. |
| T-GOV-06 | CORE-A4-02 | Execute steps via human, AI-on-behalf, autonomous AI. | PxER attribution distinguishes all three. |
| T-GOV-06a | CORE-A4-06 | Force a recovery event with `initiator: P-track`. Inspect PxER. | Three-layer accountability chain (per CORE-A4-01) applied to the recovery decision: intent (why recovery invoked), execution (what was done), oversight (human review path recorded for `outcome: partial`/`failed`; autonomous-decision attestation for `outcome: bypassed`). `self_healed` outcomes exempt from A4 chain only where observation evidence in `evidence_refs` distinguishes self-heal from unrecorded autonomous decision. |
| T-GOV-07 | CORE-A4-04, CORE-A2-08a | Execute a P-orchestrated process. | PxER records goal-setter, executed step sequence with per-step D/P, replanning events. |
| T-GOV-08 | CORE-A5-01, A5-02 | Submit a Frame with compliance-scoped steps. Execute process. | Each compliance-scoped step declares an authorship marker from {`external-mandated`, `enterprise-authored`}. Frame encodes applicable compliance levels per step. PxER evidences compliance status per step. |
| T-GOV-08a | CORE-A5-03 | Submit a Frame where an `enterprise-authored` constraint weakens an inherited `external-mandated` constraint (a) without a governed-exception record, and (b) with a governed-exception record bearing a resolvable authority reference. | (a) flagged/blocked as a constraint-integrity violation; (b) permitted. A receiving system MAY reject an exception record lacking a resolvable authority reference. |
| T-GOV-09 | CORE-A6-01, A6-02 | Execute a P-step requiring HITL approval. | Engagement record includes: decision, duration, evidence reviewed. Quality measured, not merely recorded. |
| T-GOV-10 | CORE-A6-03 | Inspect HITL engagement records. | Each record carries an engagement-fidelity marker with a valid measurement-basis value (`acknowledgement-only` / `behavioural-measured`). Marker honestly reflects the measurement applied. *(No per-level capability assertion — the L1–L4 maturity model is illustrative, APP-IG.)* |
| T-GOV-11 | CORE-A7-01 | Invoke the same process via copilot, autonomous agent, and A2A. | Identical governance treatment across all modes. |
| T-GOV-12 | CORE-A7-02 | Execute traffic both through and bypassing the protocol surface. | PxER records which paths governed, which not. |
| T-GOV-13 | CORE-CP-01, CP-02 | Declare conformance profile. | Profile declared per scope. Multi-profile honoured. |
| T-GOV-14 | CORE-CP-03 | Execute the conformance test. | (1) Frame exists (T-SPEC-01 passes), (2) PxER produced (T-EVID-01 passes), (3) A3–A11 consistency verified (T-GOV-01 through T-GOV-16 and T-LEARN-01 through T-LEARN-13 all pass for applicable requirements), (4) declared profile met (T-GOV-13 passes). |
| T-GOV-15 | CORE-XX-01 | Disable governance layer. Execute process with C0/C1, C2, and C3/C4 steps. | C0/C1 steps block (fail-closed). C2 steps follow declared degradation behaviour. C3/C4 steps continue ungoverned. PxER gaps flagged for retrospective reconciliation on all degraded steps. |
| T-GOV-16 | CORE-XX-02 | Attempt to force governance degradation on a C0/C1 step. | Degradation blocked. C0/C1 steps fail-closed. |

### 5.5 Security Dimension Tests

| Test ID. | Requirement(s). | Procedure | Pass Criteria |
|:---|:---|:---|:---|
| T-SEC-01 | SEC-XX-01 | Activate data flow before security controls are ready. | Data flow blocked until controls active. |
| T-SEC-02 | SEC-S1-01 | Submit an unsigned Frame mutation. | Rejected. |
| T-SEC-03 | SEC-S1-02 | Submit multiple Frame mutations. Inspect provenance. | Append-only record with signed changes, authorisers, classifications. |
| T-SEC-04 | SEC-S1-03 | Submit a Frame version lower than last-applied. | Rejected without explicit governance approval. |
| T-SEC-05 | SEC-S1-04 | Submit Frame construction from source material without verified provenance. | Construction blocked. |
| T-SEC-06 | SEC-S2-01 | Attempt connection without mTLS + OAuth 2.1 + DPoP. | Connection rejected. |
| T-SEC-07 | SEC-S2-02 | Present an unsigned Agent Card. | Card rejected. |
| T-SEC-08 | SEC-S2-03 | Inject an out-of-sequence message into a stateful session. | Message dropped. |
| T-SEC-09 | SEC-S3-01 | Classify a compliance-critical step with a single classifier. | Classification fails validation (independent path required). |
| T-SEC-10 | SEC-S3-02 | Update classifier. | Adversarial test suite runs and passes before update takes effect. |
| T-SEC-11 | SEC-S4-01 | Submit PxER telemetry. Inspect verification_status. | Status tracks: pending → verified/unverified/failed. |
| T-SEC-12 | SEC-S4-02 | Inspect PxER step records. | Each carries evidence_tier (limited / L2-verified / L3-verified / L3-unverified). |
| T-SEC-13 | SEC-S4-03 | Attempt L3 telemetry contribution without OAuth 2.1 DPoP. | Rejected. |
| T-SEC-14 | SEC-S4-04 | Register a new L3 contributor. | Elevated verification frequency applied. Trust tier explicit in PxER. |
| T-SEC-15 | SEC-S4-05 | Inspect write-path for PxER assembly. | Every write carries signed service provenance, verified against independent audit log. |
| T-SEC-16 | SEC-S5-01 | Inspect HITL approval surface content source. | Surfaces generated from verified data. AI content clearly labelled and visually separate. |
| T-SEC-17 | SEC-S5-02 | Inspect canary injection schedule. | Cryptographically randomised per approver session. |
| T-SEC-18 | SEC-S5-04, S5-05 | Inspect engagement telemetry privacy. | Detailed metrics off-by-default. Jurisdictional tier configured per tenant. |
| T-SEC-19 | SEC-S6-01 | Submit a Frame for a C0-scoped process with missing C0 constraints. | Gap flagged as unresolved compliance risk. |
| T-SEC-20 | SEC-S7-01 | Execute a process. | Independent signed execution trace produced. Asynchronous reconciliation detects: step omission, phantom steps, sequence violations, D/P mismatches, HITL bypass. |
| T-SEC-21 | SEC-S7-02 | Disable governance on C0/C1 step. | Execution blocks (fail-closed). |
| T-SEC-22 | SEC-S8-01 | Attempt P→D promotion using PxER records with `verification_status: pending`. | Promotion blocked. |
| T-SEC-23 | SEC-S8-02 | Attempt to reuse promotion evidence across two evaluations. | Second use rejected. |
| T-SEC-24 | SEC-S9-01 | Generate advisory from PxER records with `verification_status: unverified`. | Advisory flagged as low-confidence with disclosure. |
| T-SEC-25 | SEC-S9-02 | Generate advisory recommending reduced governance. | Elevated approval required beyond standard process owner authority. |
| T-SEC-26 | SEC-S10-01 | Inspect cross-deployment analytics. | Documented differential privacy budget per query type. Physical index separation. Deployment-bound encryption keys. |
| T-SEC-27 | SEC-S10-02 | Inspect analytics data flow. | Raw data does not leave deployment boundary. Encrypted gradients only. |
| T-SEC-28 | SEC-S12-01 | Submit L1 data to PxER without PII classification. | Rejected. |
| T-SEC-29 | SEC-S12-02 | Inspect L1 credential storage. | Dedicated vault. Isolated from production. Access audit-logged. Rotation automated. |
| T-SEC-30 | SEC-S12-03 | Attempt C0 compliance claim using L1 evidence alone. | Claim rejected (corroboration from L2+ or human attestation required). |
| T-SEC-31 | SEC-S13-01 | Inspect agent session tokens. | Session-scoped token encoding: autonomy level, delegation chain, HITL engagement level, risk classification. |
| T-SEC-32 | SEC-S13-02 | Inspect token retention. | Session tokens preserved for applicable compliance retention period. |
| T-SEC-33 | SEC-S5-03 | Inspect HITL engagement authenticity detection at L2+. | Behavioural detection operational beyond threshold-only checks. |
| T-SEC-34 | SEC-S8-03 | Attempt C0/C1 P→D promotion with single reviewer. | Promotion blocked (dual-human required). |
| T-SEC-35 | SEC-S11-01a | Attempt to instantiate an unsigned Process Frame template. | Instantiation blocked. |
| T-SEC-36 | SEC-S11-02 (L2+) | Attempt template auto-update without governance approval. | Update blocked. |
| T-SEC-37 | SEC-S14-01 | Attempt cross-tenant entity type query. | Query rejected. |
| T-SEC-37a | SEC-S14-02 | Inspect entity field paths in entity_extract declarations. | Field paths not exposed to other tenants or to roles without entity correlation access. |
| T-SEC-37b | SEC-S14-03 | Inspect entity data access controls in PxER. | Entity references inherit same access controls and hash chain integrity as parent PxER record. |
| T-SEC-38 | SEC-S14-04 | Attempt cross-tenant entity correlation. | Correlation rejected. |
| T-SEC-39 | SEC-S14-05 | Inspect entity refs for cross-enterprise step. | References limited to boundary-observable data. |
| T-SEC-40 | SEC-S14-06 | Submit populated correlation from unauthenticated source. | Import rejected. |
| T-SEC-41 | SEC-S14-07 | Inspect access to divergent reconciliation signals. | Access-controlled to authorised roles. |
| T-SEC-42 | SEC-S14-08 | Attempt cross-tenant registry query. | Query rejected. |
| T-SEC-43 | SEC-S14-09 | Inspect retention period declarations. | Retention declared per compliance scope. Undeclared = non-conformant. |
| T-SEC-44 | SEC-S3-06 | (a) Issue a request matching a D-track entry whose resolved parameter scope contains data outside the requestor's authorisation scope. (b) Issue a request whose resolved scope is within authorisation. | (a) D-track serve blocked; request falls back to P-track. (b) D-track serve proceeds. |
| T-SEC-45 | SEC-S4-05 | Inspect write-path authentication coverage across the six enumerated artifact classes (execution-record / governance-graph / catalog-promotion / identity-registry / compliance-evidence / operational-telemetry). | Every write to each enumerated class carries signed service provenance verified against an independent audit log. Class enumeration matches the protocol-defined six-class set. |
| T-SEC-46 | SEC-S4-06 | (a) Submit a lawful erasure request for a data subject whose data appears in PxER. (b) Inspect remaining records after erasure. (c) Inspect erasure event record. | (a) Erasure exercised (subject data effectively unrecoverable from PxER). (b) Remaining records retain integrity properties: immutability of unaffected entries, hash-chain continuity, signed-provenance verifiability. (c) Erasure event recorded with subject reference (or one-way digest), timestamp, lawful basis, affected record identifier scope. |
| T-SEC-47 | SEC-S6-02 | Modify a C0/C1 constraint pattern. Inspect existing exceptions previously granted against the prior pattern. | Existing exceptions re-validated against the new pattern. Exceptions failing re-validation revoked or routed for re-approval. Re-validation event recorded in PxER with exception identifier + constraint-pattern version delta. |
| T-SEC-48 | SEC-S6-03 | (a) Attempt to change autonomy mode (Supervised → Autonomous) on a C0/C1 step via standard operational approval. (b) Attempt to change domain-level autonomy default affecting multiple tenants. | (a) Change blocked until security review independent of standard operational approval is completed. (b) Default change blocked until equivalent domain-level security review is completed. |
| T-SEC-49 | SEC-S8-04 | Inject promotion candidates at atypically high emergence velocity for the candidate type. | Velocity flagged. Standard dual-approval flow blocked. Session-provenance attestation + elevated review path required before approval can complete. |
| T-SEC-50 | SEC-XX-02 | (a) Inspect the implementation's substrate inventory. (b) Introduce a new agent-writable-and-observable substrate without inventory update. (c) Attempt cross-session write-and-observe on an isolated substrate. | (a) Inventory published and enumerates all substrates the implementation is aware of. (b) Substrate rejected — inventory update MUST precede write-access enable. (c) Cross-session access blocked by default isolation. |
| T-SEC-51 | SEC-XX-04 | Execute the implementation's declared adversarial exercise suite (a) pre-release for a version affecting a Required Outcome, and (b) at the declared operational cadence. Inspect exercise evidence. | Suite runs. Evidence records pass/fail per exercise, coverage against the minimum coverage set (SEC-XX-02, S13-03, S5-06, S2-06, S7-03, XX-03, XX-05, trusted-source exclusion), remediation status. Absence of exercise = non-conformant. Coverage below minimum set = non-conformant unless architecturally inapplicable with documented rationale. |
| T-SEC-52 | SEC-XX-05 | Inject each of the 5 enumerated severe events: (a) agent safety event (S5-06), (b) covert-channel suspicion (XX-02), (c) aggregate-authority threshold breach (S2-06), (d) baseline-poisoning suspicion (S7-03), (e) peer-authority elevation attempt (S13-03). For each: (i) attempt a privileged action after detection; (ii) attempt a prohibited safe-state action (write, financial, C0/C1 record, other-agent scope, delegation, governance-config, HITL-required); (iii) attempt silent expiry / autonomous resumption. | (i) Privileged action ordered *before* safe-state entry: MUST NOT execute — action-ordering test per APP-3 SEC-XX-05 transition timing. (ii) Prohibited action in safe state: blocked. (iii) Silent expiry with autonomous resumption: non-conformant — safe-state exit MUST be gated by human acknowledgement, entry-authorising governance-control identity, or expiry with automatic escalation to human review. PxER records the eight-field schema: triggering_event_id, severe_event_class, affected_scope, state_entered, entry_principal, entry_timestamp, prohibited_actions_baseline, exit_condition_declared. Exit event records exit_principal, exit_timestamp, exit_disposition. Continuation without either resolution = non-conformant. |
| T-SEC-53 | SEC-S2-06 | Construct a two-hop delegation chain where each individual agent's action is within its own declared authorization scope, but the composed reach (union of entity-set, data-classification span, RBAC scope) exceeds any single link's scope. Execute the chain. | Execution halts before the composed-exceeds-single point. Re-authorization from a human authority with scope over the composed outcome required. Composition detected on at least entity-set reach, data-classification span, and RBAC scope union. |
| T-SEC-54 | SEC-S3-07 | (a) Inspect the cross-family attestation record for a governance-critical verification surface. (b) Verify signatory binding. (c) Force a scenario where cross-family verification is unavailable (single-family deployment). | (a) Attestation record complete with all 8 fields (verifier_model_id, verified_model_id, provider_operator, shared_weights_declaration, training_independence_declaration, family_distinction_basis, attestation_date, attestation_signatory). shared_weights_declaration is FALSE. (b) Signatory bound to `provider_operator` legal entity, signature verifiable. (c) Surface escalates to human review via SEC-S5-06 rather than proceeding with same-family verification. |
| T-SEC-55 | SEC-S5-06 | Trigger an agent-initiated safety event. Inspect the safety-event channel. | Nine-element control contract operational: primitive (event), invocation binding (agent identity), routing (human target, not peer), availability (channel reachable at declared SLA), failure mode (fail-safe on delivery failure per XX-03), rate control, human response window declared, evidence record (safety-event ID + response), non-invocation signal recorded when no events raised over a declared window. Absence of any element = non-conformant. |
| T-SEC-56 | SEC-S6-04 | (a) Attempt a governance-weakening configuration change (feature flag, safety-event routing, risk threshold, control-plane privilege) via standard operational approval. (b) Inspect immutable audit sink after the change. | (a) Change blocked until elevated security review completes, with security-delta analysis showing the reduction in governance surface. (b) Change event recorded to immutable audit sink accessible to conformance auditors: change identifier, prior state, new state, authorising principal, security-delta assessment, timestamp. |
| T-SEC-57 | SEC-S6-05 | Configure a C0-scoped step with `external-mandated` authorship and `behavioural-measured` engagement fidelity. Force a recovery path that structurally cannot invoke controls at parity with the primary path. Inspect PxER. | Recovery path blocked from execution on the C0 step. `recovery_evidence.outcome` = `bypassed`. Bypass rationale in `evidence_refs`. Fail-closed enforcement per SEC-S7-02. If the step were C2 rather than C0, execution routes to human authorization per CORE-A4-06 before proceeding. |
| T-SEC-58 | SEC-S7-03 | (a) Inspect the coordination-pattern telemetry the implementation emits. (b) Verify each element listed. (c) Inspect adaptive baseline lifecycle. | (a)(b) Telemetry includes at minimum: session-level agent identity, inter-agent A2A trace, delegation-chain composition, declared analysis time windows. Telemetry is emitted regardless of whether the implementation itself performs coordination-pattern analysis (the obligation is telemetry emission, not detection algorithm). (c) Adaptive baselines are versioned, provenance-bound, rollback-able, and excluded from self-training on unresolved security events. |
| T-SEC-59 | SEC-S9-03 | Inspect the boundary between security-relevant telemetry and the adaptive learning corpus of any governance-layer capability. | Security-relevant telemetry (unresolved safety events, unresolved authorization anomalies, unresolved verification disagreements) is quarantined from adaptive-learning ingestion until resolution status is set. Resolved-benign is required before ingestion. Automated ingestion of unresolved telemetry = non-conformant. |
| T-SEC-60 | SEC-S13-03 | (a) Inspect the authority-provenance graph for a delegation chain. (b) Introduce a peer message purporting to elevate an agent's authority scope. Attempt the resulting action. | (a) Every authority source in the chain traces to either a human principal (SEC-S13-02 identity) or a system-declared authority (SEC-S6-04 governance-control identity). No node's authority source is a peer message. (b) The elevated action is blocked. The peer message is not accepted as an elevation source regardless of chain depth or composed reach. |

### 5.6 Learning Dimension Tests

| Test ID. | Requirement(s). | Procedure | Pass Criteria |
|:---|:---|:---|:---|
| T-LEARN-01 | CORE-A8-01 | Inspect Process Frame step classification provenance. | One of: born, extracted_design, earned_runtime, declared, permanent_P. |
| T-LEARN-02 | CORE-A8-02 | Inspect a step with provenance `earned_runtime`. | Evidence count, evidence window, validator role, validation date, demotion conditions, prior classification present. |
| T-LEARN-03 | CORE-A8-03 | Trigger each promotion outcome. | Three outcomes representable: promote to D execution, delegate to source rule engine, classify as permanent_P. |
| T-LEARN-04 | CORE-A8-04 | Promote a step. | Frame transition event recorded: type, trigger, prior/new classification, evidence ref, demotion conditions. |
| T-LEARN-05 | CORE-A9-01, A9-02 | Advance a Frame through lifecycle states. | Four states (Seed → Observed → Validated → Mature). Each transition recorded with evidence. |
| T-LEARN-06 | CORE-A9-03 | Attempt lifecycle transition recommendation with compromised evidence. | Blocked until evidence integrity verified. |
| T-LEARN-07 | CORE-A10-01 | ~~Inspect drift signals. Four types operational.~~ | **Deprecated (DR-02).** A10-01 demoted RO→RP — the specific signal-type set is no longer a conformance requirement (list-coupled test severed). The A10 outcome is tested by T-LEARN-08 (A10-02 divergence report); entity-drift by T-LEARN-13 (EC-32). Row retained per ID immutability. |
| T-LEARN-08 | CORE-A10-02 | Inspect conformance reporting. | Report produced on declared cadence. |
| T-LEARN-09 | CORE-A10-04 | Attempt drift signal from compromised evidence. | Blocked until evidence integrity verified. |
| T-LEARN-10 | CORE-A11-01 | ~~Inspect process intelligence outputs. Four outputs present.~~ | **Deprecated (DR-02).** A11-01 dropped RO→RP — no specific intelligence outputs are mandated (list-coupled test severed). The interop substrate (mineable PxER corpus) is tested via A2-01/A2-02 (T-EVID-01/02). Row retained per ID immutability. |
| T-LEARN-11 | EC-15, EC-16 | Inspect inferred entity correlations. | Correlations carry: confidence, evidence count, first/last observed, process scope. |
| T-LEARN-12 | EC-22, EC-23 | Activate both inferred and populated modes for same entity pair. Also: simulate populated source unavailability mid-reconciliation. | Reconciliation status produced (five outcomes). Divergent status surfaced as operational signal. Error status produced when source unavailable, with reason code and staleness timestamp. |
| T-LEARN-13 | EC-31, EC-32 | Inspect entity correlation signals. | Stable correlations representable as P→D candidates. Correlation drift representable as A10 drift signal. |

### 5.7 Cross-Cutting Conformance Tests

| Test ID | Requirement(s) | Procedure | Pass Criteria |
|:---|:---|:---|:---|
| T-CONF-01 | CONF-D-01, §1.3 multi-role rule | Declare a multi-role implementation (e.g., GO + TC at L3). Inspect conformance assessment. | Applicable dimensions are the union of all declared roles. Requirements from all declared-role matrices (§4.1–§4.5) are assessed. Learning dimension is required (from GO) despite being "—" for TC. Conformance statement (CONF-D-05) reflects multi-role structure. |

---

## 6. Domain-Specific Profiles

APP-1 mentions "domain-specific" conformance in addition to role-based. This section defines domain profiles as additive requirements — an implementation claiming conformance to a domain profile MUST meet the domain profile requirements **in addition to** its role-level and L-level requirements from §4.

**[Required Outcome · CONF-DP-01]** Domain-specific profile conformance MUST be declared separately from role-level conformance. An implementation may claim role-level conformance without claiming any domain profile.

**[Required Outcome · CONF-DP-02]** Domain profiles MUST NOT weaken any base requirement from §4. Domain profiles only add requirements or constrain parameters.

### 6.1 BFSI Profile (Banking, Financial Services, Insurance)

**Target.** Implementations governing financial processes subject to SOX, Basel III/IV, MiFID II, or equivalent regulatory frameworks.

| ID | Requirement | Rationale |
|:---|:---|:---|
| CONF-DP-BFSI-01 | C0 and C1 compliance constraints MUST be encoded on all governed financial process steps. Absence of C0/C1 on a financial process step is a conformance violation. | SOX requires documented internal controls over financial reporting. Absence of compliance constraints on governed financial steps is a material control gap. |
| CONF-DP-BFSI-02 | PxER retention period MUST meet the longer of: 7 years (SOX) or applicable regulatory retention requirement. | Regulatory audit lookback periods require durable evidence. |
| CONF-DP-BFSI-03 | P→D promotion on financial reporting steps MUST require dual-human approval (SEC-S8-03 elevated from SHOULD to MUST). | Insider threat on financial process governance warrants the four-eyes principle. |
| CONF-DP-BFSI-04 | Conformance profile for C0-scoped financial processes MUST be Preventive (CORE-CP-01). Detective and Retrospective profiles are non-conformant for C0 financial processes. | Regulatory expectation: controls prevent violations, not merely detect them. |
| CONF-DP-BFSI-05 | HITL engagement on financial approval steps MUST use Attestation-tier engagement (CORE-A6-04 elevated from SHOULD to MUST for C0 financial steps). | Rubber-stamping financial approvals is a material control failure. |

### 6.2 Healthcare Profile

**Target.** Implementations governing processes subject to HIPAA, HITECH, EU MDR, or equivalent health data protection frameworks.

| ID | Requirement | Rationale |
|:---|:---|:---|
| CONF-DP-HC-01 | PxER records containing PHI (Protected Health Information) MUST carry a PHI marker. PHI-marked records MUST apply HIPAA minimum necessary controls on access. | HIPAA minimum necessary rule applies to all uses and disclosures. |
| CONF-DP-HC-02 | Entity correlation involving patient entities MUST be access-controlled to authorised clinical and compliance roles only. | Patient entity correlations reveal treatment relationships across systems — a PHI disclosure risk. |
| CONF-DP-HC-03 | Cross-deployment analytics (SEC-S10-01/02) MUST apply HIPAA de-identification standards (Safe Harbor or Expert Determination) before any patient-entity-enriched data leaves the deployment boundary. | HIPAA de-identification requirements exceed general differential privacy. |
| CONF-DP-HC-04 | C0 constraints for healthcare processes MUST include applicable HIPAA/HITECH rules. SEC-S6-01 negative space detection MUST include a healthcare-specific constraint checklist. | Healthcare compliance gaps are not generic — they require domain-specific detection. |
| CONF-DP-HC-05 | Breach notification capability: when a HITL security violation (SEC-S5-01) or evidence integrity failure (SEC-S4-01) involves PHI, the implementation MUST support automated flagging for breach assessment within the applicable notification window (72 hours GDPR, 60 days HIPAA). | Regulatory breach notification timelines are short. Manual detection is insufficient. |

### 6.3 UAE/DIFC Profile

**Target.** Implementations deployed in UAE jurisdictions subject to UAE PDPL, DIFC Data Protection Law, ADGM Data Protection Regulations, or KSA PDPL.

| ID | Requirement | Rationale |
|:---|:---|:---|
| CONF-DP-UAE-01 | Jurisdictional privacy tier (SEC-S5-05) MUST be locked to Tier A (full GDPR-equivalent) for DIFC and ADGM deployments. | DIFC and ADGM data protection laws are GDPR-equivalent. Tier B or C is non-conformant. |
| CONF-DP-UAE-02 | Engagement telemetry for UAE PDPL-scope deployments MUST comply with Tier B minimum: disclosure required, dwell time with notice. | UAE PDPL requires employee notification for monitoring. |
| CONF-DP-UAE-03 | PxER data residency MUST be configurable to UAE-based storage for UAE-domiciled entity data. Cross-border transfers MUST comply with applicable adequacy decisions or standard contractual clauses. | UAE data localisation expectations for government and regulated entities. |
| CONF-DP-UAE-04 | Arabic language support for HITL approval surfaces MUST be available when the governed process operates in an Arabic-language jurisdiction. | Regulatory submissions and approvals may require Arabic. Approval surfaces must not force English-only for governance-critical decisions. |

*Note on KSA PDPL: Deployments subject to KSA PDPL use Tier B (as specified in APP-3 SEC-S5-05) and may apply the UAE/DIFC profile requirements by analogy. A dedicated CONF-DP-KSA profile is anticipated for a future version; in the interim, KSA deployments should declare Tier B privacy tier configuration and apply CONF-DP-UAE-02 (disclosure + proportionality) and CONF-DP-UAE-03 (data residency, adapted for KSA localisation requirements) as minimum guidance.*

---

## 7. Interoperability Verification

APP-1 Article 5 requires: "No protocol capability advances to Recommended status without at least two independent interoperable implementations and a passing conformance test suite."

### 7.1 Interoperability Definition

**[Required Outcome · CONF-T-03]** Two implementations are interoperable for a given requirement when:

(a) Both independently pass the conformance test for that requirement (§5).
(b) Artifacts produced by one implementation are consumable by the other. Specifically: a Process Frame produced by implementation A is consumable by implementation B, and a PxER record contributed by implementation A is assembleable by implementation B.
(c) Where the requirement involves cross-system interaction (A1, A2, A7 requirements), both implementations can participate in a governed process instance together — one as governance orchestrator, the other as a participant in a different role.

**[Required Outcome · CONF-T-04]** Interoperability testing MUST use the Reference Mechanisms (CORE-A0-03 DAG-JSON, APP-3 Appendix B signature algorithms, EC-36/EC-37 entity reference structures) as the interchange baseline. Implementations using alternative mechanisms MUST demonstrate equivalent interoperability.

### 7.2 Interoperability Test Categories

| Category | What Is Tested | Minimum Implementations |
|:---|:---|:---|
| **Frame interchange** | Process Frame produced by A, consumed by B | 2 |
| **PxER assembly** | Telemetry contributed by A (TC role), assembled by B (GO role) | 2 (different roles) |
| **Integration surface** | A1 outbound/inbound/notification between A and B | 2 |
| **Entity correlation** | Entity references from A and B correlated in a single PxER instance | 2 |
| **Security handshake** | mTLS + OAuth 2.1 + DPoP between A and B | 2 |

### 7.3 Advancement Threshold

**[Required Outcome · CONF-T-05]** A protocol capability advances from Draft to Recommended status only when: (a) two or more independent implementations pass the conformance test suite for that capability's requirements, and (b) at least one interoperability test in each applicable category (§7.2) passes between two independent implementations.

### 7.4 Verifiable Conformance Assertions

**[Required Outcome · CONF-T-06]** Verifiable cross-implementation conformance assertions. An implementation claiming conformance MUST be able to produce, on request, a signed assertion of its conformance status that a consuming implementation can verify without re-running the conformance test suite. The assertion MUST be cryptographically bound to the asserting implementation's identity and MUST reference: (a) the implementation name and version, (b) the declared role(s) and L-level(s), (c) the declared conformance profile(s), (d) the requirement IDs covered by the assertion, (e) the assessment date, and (f) the assessment authority (self-assessed / peer-assessed / third-party-assessed). Self-declaration without verifiable assertion (CORE-CP-01) is insufficient for cross-implementation trust — a consuming implementation has no protocol-level mechanism to verify a peer's conformance claim.

**Signature mechanism is an implementation choice.** Implementations MAY use APP-3 Appendix B signature algorithms or any cryptographically equivalent mechanism. The wire format (JSON Web Signature, COSE, X.509-based attestation, or other) is not normatively specified — outcome is verifiability across implementations, not a fixed wire contract.

**Relationship to CORE-CP-04.** Where conformance is partial (CORE-CP-04), the assertion MUST enumerate unmet MUST-level requirements. A consuming implementation MAY refuse interoperation for use cases dependent on unmet requirements.

---

## 8. Conformance Reporting

**[Required Outcome · CONF-D-05]** Conformance claims MUST be published in a standardised conformance statement containing: implementation name and version, declared role(s), declared L-level per scope, declared conformance profile per scope, per-dimension conformance status, list of unmet MUST-level requirements (when partially conformant), domain-specific profile claims (if any), and date of assessment.

**[Recommended Pattern · CONF-D-06]** Conformance statements SHOULD be machine-readable (JSON or XML) to support automated compatibility checking between implementations. Rationale: enables deployment tooling to verify that a proposed multi-vendor configuration uses conformant implementations with compatible profiles. Alternative: human-readable document — conformant but requires manual compatibility assessment.

---

## Appendix A — Requirement Count Summary

Summary counts for implementor planning. Authoritative detail is in §4.

| Role | RO (MUST) | RP (SHOULD) | Total | Notes |
|:---|:---|:---|:---|:---|
| **Governance Orchestrator (L2)** | ~109 | ~31 | ~140 | Full protocol scope incl. S14, S11 consumer. Heaviest obligation. *(v1.5 refresh: +14 requirements from v3.8/v3.9/v3.10/v5.9/v5.10 cascade — CORE-A2-13/14, A4-06 and SEC-XX-02/04/05, S2-06, S3-07, S5-06, S6-04/05, S7-03, S9-03, S13-03, plus SEC-XX-03 as RP.)* |
| **Governance Orchestrator (L3)** | ~113 | ~33 | ~146 | Adds S10, CORE-L3-01. |
| **Governance Orchestrator (L4)** | ~116 | ~34 | ~150 | Adds S11 marketplace. |
| **Telemetry Contributor (L3)** | 10 | 1 | 11 | Contribution format + auth + LITL. |
| **Agent Builder Platform (L2)** | 15 | 2 | 17 | Frame consumption + transport security + S2-06 compositional authority. |
| **Enterprise Deployer** | 8 | 0 | 8 | Policy configuration. |
| **Field Deployment** | 5 | 0 | 5 | Activation security. |

*Counts are approximate and include CORE, SEC, and EC requirements. Exact counts depend on L-level.*

---

## Appendix B — Conformance Dimension Mapping to Source Requirements

Complete mapping from each conformance dimension to every source requirement. This appendix is the cross-reference companion to APP-IG-02. *(Rebuilt v1.5 to reflect the v3.8/v3.9/v3.10/v5.9/v5.10 cascade; each requirement now appears under exactly one dimension.)*

| Dimension | CORE Requirements | SEC Requirements | EC Requirements |
|:---|:---|:---|:---|
| **Specification** | A0-01/02/03, A1-01/02/03/04/05/06 | S1-01/02/03/04/05, S2-01/02/03/04/05/06 | EC-01/01a/02/03/05/06, EC-38/39 |
| **Evidence** | A2-01/02/03/04/04a/05/06/07/08/08a/10/11/12/13/14, A3-01/02, A4-06, L3-01 | S4-01/02/03/04/05/06, S13-01/02/03 | EC-07/08/09/10/11/34/35/36, EC-40/41/42 |
| **Governance** | A3-01/03/04/05/06, A4-01/02/03/04/05, A5-01/02/03, A6-01/02/03/04/05, A7-01/02/03, CP-01/02/03/04, XX-01/02 | S3-01/02/06/07, S5-01/02/03/04/05/06, S6-01/02/03/04/05, S7-01/02/03 | — |
| **Security** | — | XX-01/02/03/04/05 (cross-cutting principles); all remaining SEC-* at declared L-level, including S14-01 through S14-09 | EC-43/44/45/46/47 |
| **Learning** | A8-01/02/03/04, A9-01/02/03, A10-01/02/03/04, A11-01/02 | S8-01/02/03/04, S9-01/02/03, S10-01/02/03 | EC-15/16/17/19/20/21/22/23/25/26/31/32 |

*Notes:*
- *Per-requirement placement rule: each source requirement appears under exactly one dimension. Where a requirement supports multiple dimensions (e.g., SEC-S4-06 evidence-record erasure reconciliation supports both Evidence integrity and Security), it is placed under the dimension where its conformance failure is assessed, with informative cross-references documented in APP-IG-02.*
- *SEC-XX-* cross-cutting principles are placed under the Security dimension (they are not tied to a single capability); SEC-S13-* agent identity is placed under Evidence (identity binding is the load-bearing evidence property for PxER audit).*
- *EC-38 through EC-47 protect EC-specific security concerns. EC-38/39 are placed under Specification (they govern how entity_extract declarations are constructed); EC-40/41/42 under Evidence (they govern PxER entity_refs security); EC-43/44/45/46/47 under Security (they govern registry, reconciliation, and correlation-data security).*
- *v1.5 change: A4-06 (recovery-decision accountability), A2-13/14 (recovery evidence + outcome vocabulary), A5-03 (constraint-inheritance integrity), S3-07 (cross-family verification), S5-06 (agent safety-event channel), S6-02/03/04/05 (compliance-integrity extensions), S7-03 (coordination detectability), S8-04 (promotion velocity integrity), S9-03 (evidence-vs-learning quarantine), S13-03 (authority-provenance invariant), S2-06 (compositional authority accumulation), S4-06 (erasure reconciliation), XX-02/03/04/05 (cross-cutting principles) are all now mapped. This closes the v1.4 gap where these v3.8/v3.9/v3.10/v5.9/v5.10 additions were present in APP-2/APP-3 but absent from the dimension mapping.*

---

## Appendix C — Glossary

| Term | Definition |
|:---|:---|
| **Conformance Dimension** | One of five orthogonal axes (Specification, Evidence, Governance, Security, Learning) on which conformance is independently reported |
| **Conformance Scope** | The combination of participant role, L-level, and conformance profile for which conformance is assessed |
| **Conformance Statement** | The published declaration of an implementation's conformance status per dimension and scope |
| **Domain Profile** | Additive conformance requirements for regulated industries or jurisdictions (BFSI, Healthcare, UAE/DIFC) |
| **Interoperability Test** | Verification that two independent implementations can exchange conformant artifacts and participate in governed processes together |
| **Participant Role** | One of five protocol roles: Governance Orchestrator, Telemetry Contributor, Agent Builder Platform, Enterprise Deployer, Field Deployment |

---

## Appendix D — Requirement Rationale Digest

This appendix provides plain-language rationale for APP-5's structural decisions. Informative; intended for implementors and working group members.

| Decision | Rationale |
|:---|:---|
| **Five dimensions, not a single score** | APP-1 Article 5 mandates decomposed conformance. A single score allows an implementation strong in evidence production to mask weak HITL governance. Per-dimension reporting surfaces this. An ERP vendor contributing telemetry at L3 may score well on Evidence and Security but has no Learning obligation — the dimension structure makes this explicit rather than penalising for irrelevant capabilities. |
| **Five roles, not three or seven** | The five roles map to distinct conformance boundaries — different requirement subsets, different L-level obligations, different test surfaces. Fewer roles would merge distinct obligation sets (a telemetry contributor has fundamentally different obligations than a governance orchestrator). More roles would create distinctions without materially different requirement matrices. |
| **Domain profiles are additive only** | Domain profiles cannot weaken base requirements because regulatory requirements are boundary conditions (APP-1 Priority of Constituencies §1). A BFSI profile adds SOX-specific requirements; it does not relax base evidence integrity requirements. This prevents "BFSI-lite" profiles that claim domain conformance while weakening core governance. |
| **Interoperability requires artifact exchange, not identical implementation** | Two implementations may achieve the same Required Outcome through different mechanisms (APP-1 Article 4). Interoperability is demonstrated by artifact compatibility — a Frame produced by A is consumable by B — not by implementation equivalence. This preserves competitive differentiation while ensuring protocol value. |
| **Testable criteria are binary, not scored** | Each MUST-level requirement either passes or fails. Scoring introduces subjectivity and enables "mostly conformant" claims that APP-1 Article 5 explicitly prohibits (undeclared non-conformance is a conformance violation). Partial conformance is permitted but must be explicitly declared per CORE-CP-04. |

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 1.9
**Normative status:** Normative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-5 — Conformance Profiles.*
