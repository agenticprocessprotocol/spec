# APP-2

Agentic Process Protocol

## Core Technical Specification

| | |
|:---|:---|
| **Version** | 5.13 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Audience** | Protocol implementors, agent builder platform teams, ERP vendor architects, enterprise governance teams |
| **Normative status** | This document is normative. Governed by APP-1. |
| **Companion documents** | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles), APP-IG-02 (Cross-Reference Matrix), APP-R1 (Frame Schema), APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) — v5.13 adds illustrative reference pointers from CORE-A1-04 and CORE-A1-05 to APP-R2 and APP-R1 respectively; no normative change. |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |
| **Version-reference convention** | Companion documents cited by name only in body prose. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-2 is the normative core specification of the Agentic Process Protocol. It defines the twelve protocol capabilities (A0 through A11), the four-level maturity model (L1 through L4), the conformance status schema, and cross-cutting requirements for governed process execution.
>
> **Status:** Normative. Requirements expressed using RFC 2119/8174 keywords are binding within the declared scope.
>
> **Authority and precedence:** Governed by APP-1. Peer to APP-0, APP-3, APP-4, and APP-5 within the constitutional frame.
>
> **Use this document for:** Capability definitions and Required Outcome/Recommended Pattern/Reference Mechanism classifications; requirement IDs (CORE-An-nn, CORE-CP-nn, CORE-XX-nn, CORE-L3-nn); maturity-level applicability; protocol boundary reference.
>
> **Related documents:** APP-0 (objectives realised by these capabilities), APP-1 (governing Constitution), APP-3 (security architecture), APP-4 (entity correlation), APP-5 (role-based conformance profiles), APP-IG-02 (cross-reference matrix).

---

## How to Read This Document

Normative elements are classified at exactly one of three specificity levels (APP-1 Article 4):

| Marker | Level | Meaning |
|:---|:---|:---|
| **[Required Outcome]** | What must be true | Verifiable outcome using MUST. Any conformant mechanism qualifies. |
| **[Recommended Pattern]** | How the protocol suggests achieving it | Expressed using SHOULD. Alternatives documented. Deviation requires justification. |
| **[Reference Mechanism]** | A specific mechanism proposed | Informative. Working group starting point. |

This document uses RFC 2119/8174 normative keywords. MUST, SHOULD, MAY in all capitals carry their defined meanings.

Each capability section follows: definition → protocol rationale → normative requirements → recommended approach → implementation choices → security cross-references.

Every normative element carries a requirement ID: `CORE-An-nn` for capability requirements (where A = capability number, nn = sequence), `CORE-CP-nn` for conformance profiles, `CORE-XX-nn` for cross-cutting, and `CORE-L3-nn` for L3-specific. The Master Requirement Index (Appendix D) provides a consolidated lookup.

When referenced from documents outside the APP series, prefix with `APP-` (e.g., `APP-CORE-A0-01`). APP-3 security requirements use `SEC-Sn-nn`. APP-4 entity correlation requirements use `EC-nn`.

---

## 1. Introduction

### 1.1 What This Specification Defines

Two protocols exist for the agentic enterprise infrastructure: MCP (agent-to-tool connectivity) and A2A (cross-platform agent delegation). Neither addresses agent-to-process governance — the structured specification of what should happen across enterprise systems, the durable record of what did happen, and the closed loop between them.

```
┌─────────────────────────────────────────────────────────────┐
│  ENTERPRISE PROCESS (E2E)                                    │
│                                                              │
│  ┌── Agentic Process Protocol ─────────────────────────┐ │
│  │  What SHOULD happen (A0 Process Frame)                  │ │
│  │  What DID happen   (A2 PxER)                            │ │
│  │  Closed loop       (A8–A11 Learning)                    │ │
│  └────────────────────────────────────────────────────────┘ │
│            uses ↓                     ↓ uses                 │
│  ┌── MCP ─────────────────┐  ┌── A2A ────────────────────┐ │
│  │  Agent ↔ Tool           │  │  Agent ↔ Agent             │ │
│  │  connectivity           │  │  cross-platform delegation │ │
│  └─────────────────────────┘  └────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

MCP connects agents to tools. A2A connects agents to each other. The Agentic Process Protocol connects agents to governed processes — the third leg. This specification defines 12 protocol capabilities (A0–A11) that constitute governed process execution (§3), how the protocol adapts to different integration maturity levels (§4), and where the protocol applies (§5).

### 1.2 Relationship to Other APP Documents

| Document | Relationship |
|:---|:---|
| **APP-1 (Constitution)** | Governs this document. Constitution prevails on conflict. |
| **APP-0 (Protocol Objectives)** | Normative peer under APP-1 §4. Defines the five protocol objectives this document's requirements realise. On conflict between APP-0 and APP-2, APP-1 §4 applies: APP-2 requirement gaps trigger either specification evolution or Objective evolution through the APP-0 amendment procedure. |
| **APP-3 (Security Architecture)** | Security requirements for capabilities here. Equal standing. Cross-ref: Appendix B. |
| **APP-4 (Entity Correlation)** | Specifies the entity-correlation extension of A0/A2 artefacts. Equal normative standing; APP-2 core capabilities do not depend on APP-4 but interoperate with it where declared. Cross-ref: APP-4 §1.5(d). |
| **APP-5 series (Conformance Profiles)** | Role-based profiles using §4.4 vocabulary. Defines conformance requirements per participant role (governance orchestrator, telemetry contributor, agent builder platform, enterprise deployer, field deployment) as required by APP-1 Article 5. |
| **APP-IG series (Implementation Guides)** | Informative. Worked examples, agent framework mapping, adoption guidance. |

### 1.3 The Protocol Capability Test

A capability is a protocol concern if: when each deployment implements it differently (or not at all), governance breaks. If an implementation can choose freely without affecting governance quality, the capability is an implementation concern (Appendix C).

---

## 2. Core Concepts

**Process Frame (A0).** The structured, AI-consumable specification of an end-to-end process. Every step, its classification (deterministic or probabilistic), which system executes it, what compliance constraints apply, who is accountable, and how steps depend on each other. The governed blueprint that agents consume.

**D/P Classification (A3).** Every process step is classified as Deterministic (D — rule-based, zero inference) or Probabilistic (P — judgment-dependent, AI reasoning + human oversight). Two types of P-step: task-level P (bounded operation, structured outputs) and orchestration-level P (goal decomposition, plan as output). The difference between intended (Frame) and actual (PxER) classification — the conformance delta — is the primary governance instrument.

**PxER — Process Execution Record (A2).** The durable, immutable, queryable record of how a process instance actually executed. Governance data (D/P track, HITL engagement, compliance evidence, accountability chain) AND transaction references with traceback to source systems.

**L1–L4 Integration Maturity (§4).** L1 (screen/RPA), L2 (API/MCP), L3 (application-enhanced — vendor contributes intra-app telemetry), L4 (AI-native — governance by construction). Same protocol at every level; evidence richness varies.

**Entity Correlation (APP-4).** Cross-system entity tracking from PxER execution data.

---

## 3. Protocol Capabilities

Twelve capabilities (A0–A11). All MUST be standardised to achieve governed process execution.

```
┌─────────────────────────────────────────────────────────────────┐
│  FOUNDATION        A0 Process Frame ←→ A1 Integration Surface  │
│                         ↓                                       │
│  CLASSIFICATION    A3 D/P Classification                        │
│                         ↓                                       │
│  EVIDENCE          A2 PxER (execution record + entity)          │
│                         ↓                                       │
│  GOVERNANCE        A4 Accountability   A5 Compliance (marker)   │
│                    A6 HITL Quality                               │
│                         ↓                                       │
│  CONSUMPTION       A7 Invocation-Mode Parity                    │
│                         ↓                                       │
│  LIFECYCLE         A8 Promotion Provenance   A9 Intent Evolution│
│                    A10 Drift Detection   A11 Process Intelligence│
│                         ↑ closed loop to A0                     │
└─────────────────────────────────────────────────────────────────┘
```

*Note: Capabilities are presented in dependency order rather than numerical order. A3 (D/P Classification) precedes A2 (PxER) because PxER's conformance schema depends on D/P classification concepts. The numerical sequence A0–A11 is the canonical reference order; the presentation order supports progressive understanding.*

---

### 3.1 A0 — Process Frame

**What:** The structured, AI-consumable specification of an end-to-end process — every step, its D/P classification, which system executes it, compliance constraints, accountability, HITL requirements, and dependencies.

**Why protocol:** Without a standardised format, every deployment reinvents process capture. Vendor-specific approaches lack governance attributes. The protocol standardises the format so any platform can invoke a governed process, any application can contribute, and any PxER can trace back.

**[Required Outcome · CORE-A0-01]** A conformant Process Frame MUST include, per step: step identifier, executing system, intended D/P classification, dependency chain, and accountability owner.

**[Recommended Pattern · CORE-A0-02]** A Process Frame SHOULD additionally include: compliance constraints (C0–C4), HITL engagement requirements, D-potential tagging, promotion target, SLA definition, and entity extraction declarations (APP-4). Rationale: enables the full capability set (A3–A11). Alternative: mandatory fields only — conformant but governance-thin.

**[Reference Mechanism · CORE-A0-03]** DAG-JSON as canonical interchange format. Rationale: AI-consumable, governance-attributed, machine-executable. Alternatives: BPMN XML (notation standard, complementary as authoring input — not governance-attributed), DMN (covers D-track decision tables — the protocol's D/P classification goes further by governing the D/P boundary), executable YAML (no governance attribute schema).

**Implementation choices.** How Process Frames are authored — from SOPs, BPMN models, process mining, AI-assisted elicitation, or templates — is an implementation concern. Whether authoring is centralised or delegated is a deployment choice. The protocol standardises the output format.

> **Security.** Frame changes MUST carry tamper-evident signatures. Rollbacks MUST require human approval. Source documents MUST carry provenance metadata. Templates MUST be signed and version-controlled. *(APP-3: Frame Integrity, Input Provenance, Supply Chain Security.)*

---

### 3.2 A1 — Process Frame Integration Surface

**What:** Standardised bidirectional integration between the Process Frame and agent builder tools. The Frame is the configuration master — builders consume governed step definitions, and builder changes flow through a governance gate.

**Why protocol:** Process design and agent development are manually decoupled today. A governance change requires manual rework. The protocol standardises consumption and contribution so governance changes propagate automatically.

**[Required Outcome · CORE-A1-01]** A conformant integration surface MUST support outbound (builders consume Frame), inbound (builder changes through governance gate), and notification (governance changes propagate).

**[Required Outcome · CORE-A1-02]** The inbound governance gate MUST classify incoming changes:

| Classification | Condition | Outcome |
|:---|:---|:---|
| **Governance-complete** | All mandatory attributes present | Merges. PxER tracks provenance. |
| **Partial** | Some but not all mandatory attributes | Routes to enrichment. Human review. |
| **Absent** | No governance attributes | Flagged. Full governance review. |

**[Required Outcome · CORE-A1-03]** Cross-system changes MUST require Process Frame mediation. Intra-system changes MAY merge directly if governance-complete.

**[Recommended Pattern · CORE-A1-04]** MCP Server Profile as the integration transport. Rationale: MCP is the adopted agent-to-tool standard. Alternative: REST/webhook with equivalent capability. *Illustrative reference binding: APP-R2 (MCP Binding Reference Design) — non-normative; implementations may bind the integration surface to MCP in other ways that satisfy the Required Outcomes of A1.*

**[Required Outcome · CORE-A1-05]** Frame schema portability. Frame artifacts MUST conform to a published Frame schema discoverable by consuming implementations. Consuming implementations (agent builders, governance orchestrators receiving Frame mutations from peer implementations) MUST validate received Frame artifacts against the published schema. The schema MUST cover at minimum the mandatory Frame fields declared by CORE-A0-01 plus the governance-critical attributes consumed by A3 (D/P classification), A4 (accountability markers), A5 (compliance authorship markers per CORE-A5-01), and the Frame mutation provenance fields required by APP-3 SEC-S1-02. The published schema is the cross-vendor portability surface — without it, CORE-A1-01 bidirectional integration is structurally limited to within-vendor deployment. *Illustrative reference schema: APP-R1 (Frame Schema) — non-normative; implementations may publish any schema that covers the attributes required above.*

**[Required Outcome · CORE-A1-06]** Agent Card schema. Agent Cards MUST conform to the Agent Card schemas published by the agent-to-agent interoperability standard adopted by the implementation (A2A, or an equivalent agent-to-agent standard). The APP protocol does not redefine Agent Card schema content — this is delegated to the external standard. APP-3 SEC-S2-02 (Agent Card signing) and SEC-S2-04 (export security review) apply regardless of the underlying schema standard. The interop obligation on the implementation is to (a) declare which Agent Card schema standard is adopted, and (b) ensure consumed Agent Cards conform to that declared standard. *(MCP does not define Agent Cards; MCP server metadata work is tracked as a known issue.)*

**Implementation choices.** Which authoring tool is used for which scope, whether a centralised platform or multiple tools contribute, how intra-system vs. cross-system authoring is distributed, where the published Frame schema is hosted (registry, repository, or implementation documentation), and which Agent Card standard is adopted are deployment choices.

> **Security.** Connections MUST use mutual TLS, OAuth 2.1, proof-of-possession tokens. Unsigned/out-of-sequence messages dropped. Agent Cards reviewed before external consumption. *(APP-3: Transport Security, Agent Card Federation.)*

---

### 3.3 A3 — D/P Classification

**What:** Formal boundary between Deterministic (rule-based, zero inference) and Probabilistic (judgment-dependent, AI + human oversight) per step.

**Why protocol:** Without standardised D/P classification, all steps are opaque — governance impossible, costs unnecessarily high. The conformance delta — intended vs. actual D/P — is the primary governance instrument. D-track value is governance-grade reproducibility first: formal auditability, compliance enforcement as architecture, predictable human oversight, reproducible evidence chains.

**[Required Outcome · CORE-A3-01]** Every Process Frame step MUST declare intended D/P classification.

**[Required Outcome · CORE-A3-02]** Every PxER step MUST record actual execution track when observable (via conformance schema, §3.4.1).

**[Required Outcome · CORE-A3-03]** MISMATCH between intended and actual MUST trigger mandatory review with the process owner.

**[Required Outcome · CORE-A3-04]** The protocol MUST distinguish:

- **Task-level P** — bounded operation within a structured flow. Structured outputs, evaluable.
- **Orchestration-level P** — goal decomposition and planning. Plan as output, not evaluable against ground truth.

Both are P-track. They carry different evidence requirements (§3.4.2) and governance obligations (orchestration-level P requires completion gate consideration, §3.5).

**[Recommended Pattern · CORE-A3-05]** D-classified steps SHOULD route to deterministic execution where available. Rationale: identical results on every invocation. Alternative: D-classified steps through AI inference with output validation — conformant but introduces unnecessary cost.

**[Required Outcome · CORE-A3-06]** For compliance-critical steps, D/P classification MUST be independently verified — a single classifier is insufficient where misclassification would bypass human oversight. *(APP-3: Classification Integrity.)*

**Implementation choices.** Whether D-classified steps route to a dedicated deterministic engine is an implementation choice. The governance floor (what any conformant implementation must do) is CORE-A3-01 through CORE-A3-03: declare, record, detect mismatch, escalate. An ERP vendor achieves the floor by declaring D/P in the Process Frame and contributing conformance telemetry at L3. Routing D-steps to a separate deterministic runtime is a ceiling capability, not a floor requirement. An L4 implementation achieves the governance ceiling: MATCH by architectural invariant.

> **Security.** D/P classification is a trust anchor — misclassification bypasses human oversight. CORE-A3-06 requires independent verification on compliance-critical steps. Adversarial test library SHOULD run on every classifier update. *(APP-3: Classification Integrity.)*

---

### 3.4 A2 — Process Execution Record (PxER)

**What:** The end-to-end, immutable, queryable record of how a process instance actually executed. Governance data AND transaction references with traceback to source systems.

**Why protocol:** Without a standardised record, execution evidence is scattered across logs, conversations, and case notes. No auditor can reconstruct the story. No learning system can detect cross-system patterns. For cross-system AI-mediated decisions, PxER is the governing evidence container. External system steps contribute via the A1 integration surface; P-track evidence is captured in PxER by the governance implementation, not replicated into external system records.

A2 is the protocol's evidence backbone. The PxER step record is composed from four sub-specifications, each answering a different trust question:

```
┌─────────────────────────────────────────────────────────────────┐
│  PxER STEP RECORD                                                │
│                                                                  │
│  ┌─ §3.4.1 CONFORMANCE + TRUST ──────────────────────────────┐ │
│  │  Did execution match specification?                         │ │
│  │  What trust boundary was it in?                             │ │
│  └─────────────────────────────────────────────────────────────┘ │
│  ┌─ §3.4.2 P-TRACK EVIDENCE ─────────────────────────────────┐ │
│  │  What actually happened inside P-track steps?               │ │
│  │  (Frame = boundary, PxER = interior)                        │ │
│  └─────────────────────────────────────────────────────────────┘ │
│  ┌─ §3.4.3 EVIDENCE INTEGRITY ───────────────────────────────┐ │
│  │  Can we trust the record itself?                            │ │
│  └─────────────────────────────────────────────────────────────┘ │
│  ┌─ §3.4.4 ENTITY CORRELATION → APP-4 ──────────────────────┐ │
│  │  Which business entities were affected?                     │ │
│  └─────────────────────────────────────────────────────────────┘ │
│  ┌─ §3.4.5 RECOVERY EVIDENCE  (added v5.9) ─────────────────┐ │
│  │  What happened when the primary path deviated?              │ │
│  │  (Recovery is a governance-critical decision path)          │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

Each sub-specification can be read independently. Together they compose a complete governed execution record.

**[Required Outcome · CORE-A2-01]** A conformant PxER MUST assemble an immutable, queryable record per process instance, assembled during execution (APP-1 invariant b), linked to the governing Process Frame version.

**[Required Outcome · CORE-A2-02]** Every PxER step record MUST include: step identifier, executing system, timestamp, and transaction reference to source system.

#### 3.4.0 PxER extension points

The PxER schema defined in this section is the core record. Two Architecture Chapters extend it with named sub-specifications that MUST be treated as part of the PxER record for their applicable roles and L-levels:

| Extension point | Owning specification | Purpose | Applicability |
|:---|:---|:---|:---|
| `entity_refs` | APP-4 EC-07/08/11 | Instance-level entity correlation block | Present when `entity_extract` declared on the Frame step; L2+ implementations MUST support the field even when unpopulated |
| `governance_events` | APP-3 SEC-XX-05 | Safe-state transition record on detected severe governance-critical events (eight-field schema: `triggering_event_id`, `severe_event_class`, `affected_scope`, `state_entered`, `entry_principal`, `entry_timestamp`, `prohibited_actions_baseline`, `exit_condition_declared`; exit event records `exit_principal`, `exit_timestamp`, `exit_disposition`) | MUST be present in PxER whenever a severe event is detected; the eight-field schema is normatively defined in APP-3 SEC-XX-05 and MUST be honoured by PxER assemblers |
| `recovery_evidence` | APP-2 CORE-A2-13 (this specification) | Recovery invocation record attached to the original step | Present when the step invoked a recovery path |

**Bilateral cross-reference rule (per APP-1 §4).** Where an Architecture Chapter defines a PxER extension point (as APP-3 does for `governance_events`), the extension point is a normatively defined PxER sub-specification, not a unilateral security-domain add-on. PxER assemblers MUST honour the extension point's schema as authoritative from its owning specification. Changes to an extension point's schema require concurrent revision of this specification's extension-point registry above per the change-impact manifest in APP-1 §4. This resolves the ambiguity in v5.10 where `governance_events` was referenced by APP-3 without a reciprocal declaration in APP-2.

#### 3.4.1 Conformance and Trust Context

The D/P conformance schema tracks whether each step executed as its Process Frame classification intended. The trust boundary field identifies the trust context. Together they answer: *did the right thing happen, and can we verify it?*

**[Required Outcome · CORE-A2-03]** Every PxER step record MUST carry:

| Field | Definition | Populated |
|:---|:---|:---|
| `dp_classification_intended` | From Process Frame | Always |
| `dp_classification_actual` | From execution telemetry | MAY be null L1/L2 |
| `execution_engine` | Engine that executed the step | MAY be null L1/L2 |
| `conformance_status` | MATCH · MISMATCH · UNVERIFIABLE · DEGRADED | Always |
| `mismatch_type` | See below. When status ≠ MATCH | Conditional |
| `conformance_evidence_method` | TELEMETRY · STATISTICAL · UNVERIFIABLE | Always |
| `trustBoundaryType` | internal · enterprise-external · cross-enterprise-external · unmanaged | Always |

**[Required Outcome · CORE-A2-04]** Mismatch types (populated when `conformance_status` is MISMATCH or UNVERIFIABLE):

| Value | Meaning | Governance Action |
|:---|:---|:---|
| `D_intended_P_executed` | D-classified ran through LLM | Escalate — cost leak or implementation gap |
| `P_intended_D_executed` | P-classified ran deterministically | Promotion candidate |
| `D_intended_UNVERIFIABLE` | Intended D, path unobservable | Record gap — flag for retrospective |
| `P_intended_UNVERIFIABLE` | Intended P, path unobservable | Record gap — flag for retrospective |
| `CONFLICT` | Declared execution path contradicts statistical evidence | Classification integrity alert — APP-3 S3 |

**Note on CONFLICT semantics.** CONFLICT is a classification-integrity signal, not merely another mismatch pattern. It applies when statistical evidence (at L3) contradicts the declared or telemetry-reported execution path — including the case where `dp_classification_intended` and `dp_classification_actual` agree but statistical inference indicates neither reflects what actually executed. On CONFLICT, the step's `conformance_status` MUST be set to MISMATCH regardless of the intended/actual agreement, and the integrity signal MUST be escalated per APP-3 S3 (Classification Integrity). CONFLICT is not a compound of the other four mismatch types.

**[Required Outcome · CORE-A2-04a]** When `conformance_status` is DEGRADED, `mismatch_type` MUST be null — governance was absent, so no mismatch classification is possible. The DEGRADED status itself is the governance signal (APP-3 SEC-S7).

**[Required Outcome · CORE-A2-04b]**

Every PxER step record's `conformance_status`, `mismatch_type`, and `conformance_evidence_method` fields together define the state of that step's conformance assessment. The following state matrix specifies the ten conformant combinations of these three fields; PxER assemblers MUST produce only conformant combinations. Every combination not enumerated below is prohibited.

**Derivation rules.** A conformant PxER step record satisfies all eight rules:

- **R1.** When `conformance_status` is MATCH → `mismatch_type` MUST be null. *(From CORE-A2-04.)*
- **R2.** When `conformance_status` is DEGRADED → `mismatch_type` MUST be null. *(From CORE-A2-04a.)*
- **R3.** When `conformance_status` is MISMATCH → `mismatch_type` MUST be one of `D_intended_P_executed`, `P_intended_D_executed`, or `CONFLICT`.
- **R4.** When `conformance_status` is UNVERIFIABLE → `mismatch_type` MUST be one of `D_intended_UNVERIFIABLE` or `P_intended_UNVERIFIABLE`.
- **R5.** When `mismatch_type` is CONFLICT → `conformance_status` MUST be MISMATCH. *(From CORE-A2-04 note.)*
- **R6.** When `conformance_status` is MATCH or MISMATCH → `conformance_evidence_method` MUST be TELEMETRY or STATISTICAL. UNVERIFIABLE evidence method with a definitive status is prohibited — a definite MATCH or MISMATCH determination requires verifiable evidence.
- **R7.** When `conformance_status` is UNVERIFIABLE → `conformance_evidence_method` MUST be UNVERIFIABLE.
- **R8.** When `conformance_status` is DEGRADED → `conformance_evidence_method` MUST be UNVERIFIABLE.

**Conformant states (10):**

| # | conformance_status | mismatch_type | evidence_method | Canonical case |
|:---:|:---|:---|:---|:---|
| C1 | MATCH | null | TELEMETRY | Step executed as intended, directly observed. Canonical L3+ case. |
| C2 | MATCH | null | STATISTICAL | Step executed as intended, statistical inference confirms. L2+ inferred case. |
| C3 | MISMATCH | `D_intended_P_executed` | TELEMETRY | D step ran through agent, observed. Escalate — cost leak or implementation gap. |
| C4 | MISMATCH | `D_intended_P_executed` | STATISTICAL | D step ran through agent, inferred. Same escalation. |
| C5 | MISMATCH | `P_intended_D_executed` | TELEMETRY | P step ran deterministic, observed. Promotion candidate. |
| C6 | MISMATCH | `P_intended_D_executed` | STATISTICAL | P step ran deterministic, inferred. |
| C7 | MISMATCH | `CONFLICT` | STATISTICAL | Statistical evidence contradicts declared/observed path. APP-3 S3 classification-integrity escalation. |
| C8 | UNVERIFIABLE | `D_intended_UNVERIFIABLE` | UNVERIFIABLE | D step, path unobservable at L1/L2 without statistical inference. Canonical L1/L2 default. |
| C9 | UNVERIFIABLE | `P_intended_UNVERIFIABLE` | UNVERIFIABLE | P step, path unobservable at L1/L2. |
| C10 | DEGRADED | null | UNVERIFIABLE | Governance layer unavailable. Retrospective reconciliation per APP-3 SEC-S7-01. |

**Prohibited states.** Every combination not enumerated above is prohibited. Rules R1–R8 are the closed set of prohibitions. A PxER record failing any rule is a specification defect; PxER assemblers MUST reject construction of prohibited states. Illustrative prohibited cases:

- MATCH with any non-null mismatch_type (violates R1)
- MATCH or MISMATCH with UNVERIFIABLE evidence_method (violates R6)
- UNVERIFIABLE with any MISMATCH-family mismatch_type or with null (violates R4)
- DEGRADED with any non-null mismatch_type (violates R2)
- CONFLICT with any conformance_status other than MISMATCH (violates R5)

**Prior deliberation (v5.11 working group).** Three states were considered contested in the initial derivation and resolved to prohibited per working-group decision. Each MAY be re-opened at v1.0 or later if audit-tooling patterns motivate additional evidence_method values:

- **CONFLICT + TELEMETRY as MISMATCH — prohibited.** CONFLICT is defined by mechanism: statistical inference contradicting declared or observed execution. A telemetry-observed mismatch is `D_intended_P_executed` or `P_intended_D_executed`, not CONFLICT. If statistical inference corroborates a telemetry-observed mismatch, the corroboration is recorded in `evidence_refs`; the primary mismatch_type remains D→P or P→D.
- **UNVERIFIABLE + STATISTICAL as an alternative to C8/C9 — prohibited.** A `STATISTICAL_INCONCLUSIVE` evidence_method value was considered to represent "statistical inference attempted, confidence threshold not reached." Not adopted for v5.11 — UNVERIFIABLE covers this case; the diagnostic distinction is deferred pending audit-tooling signal at v1.0.
- **DEGRADED + STATISTICAL for retrospective inference — prohibited.** A distinct `GOVERNANCE_UNAVAILABLE` evidence_method value was considered. Not adopted — UNVERIFIABLE is semantically correct (no verification was possible during governance downtime). Retrospective statistical inference reconstructing behaviour post-outage is recorded as retrospective reconciliation evidence per APP-3 SEC-S7-01, not as the DEGRADED step's evidence_method.

**Cross-references.**

- **APP-3 SEC-XX-05** (severe-event handling): state C10 (DEGRADED) is the primary intersection with the `governance_events` PxER extension point (see §3.4.0).
- **APP-5 §5** conformance tests: T-EVID-04, T-EVID-04a, T-EVID-05, T-EVID-06 test specific state transitions. A T-STATE-* test class is planned for v1.0 to verify complete state-machine coverage.
- **APP-IG-03** worked examples: every worked example maps to a specific row in this table. See APP-IG-03 traceability appendix for the mapping.

**[Required Outcome · CORE-A2-05]** Conformance by maturity level:

- **L1/L2:** `dp_classification_actual` MAY be null. Defaults to UNVERIFIABLE unless statistical inference possible.
- **L3:** Application contributes `execution_engine`. Per-invocation MATCH/MISMATCH. CONFLICT detectable where statistical evidence contradicts declared execution path.
- **L4:** MATCH by architectural invariant.
- **All levels:** When the governance layer is unavailable during step execution, `conformance_status` MUST be set to DEGRADED regardless of integration level. DEGRADED steps are subject to retrospective reconciliation per APP-3 SEC-S7-01.

**[Required Outcome · CORE-A2-11]** For steps with `trustBoundaryType: cross-enterprise-external`, governance is limited to what the governing implementation observes at its boundary. P-track evidence from external enterprise systems is not required or expected as a default. The protocol accommodates D-track-only evidence exchange as the current cross-enterprise interoperability baseline, reflecting the absence of shared trust anchors between independent enterprises. Where a bilateral or multilateral shared trust anchor is established (e.g., an industry consortium evidence exchange, a bilateral P-track evidence attestation agreement), P-track evidence exchange across the boundary is conformant; the trust-anchor mechanism is an implementation choice, not a protocol object.

**[Required Outcome · CORE-A2-12]** For steps with `trustBoundaryType: unmanaged`, PxER MUST record observed invocation only, with an explicit unmanaged marker. No evidence exchange is possible or required.

#### 3.4.2 P-Track Evidence Model

The Process Frame governs what a P-track step must achieve (the boundary). The PxER captures what actually happened (the interior). This is definitional — a fully pre-specified execution path would be D-track.

```
  PROCESS FRAME (A0)              PxER (A2)
  ─────────────────               ─────────────────
  P-track BOUNDARY:               P-track INTERIOR:
  · Must achieve X                · Decision made
  · Under constraints Y           · Business context used
  · With oversight Z              · Governance applied
  · D/P intent declared           · Actual path recorded
```

**[Required Outcome · CORE-A2-06]** The protocol MUST distinguish evidence (governance-grade: decision, context, accountability, controls, outcome) from telemetry (operational: token counts, temperature, latency). A telemetry cross-reference MAY link them. Separate retention policies and access controls MUST apply. *(Retention period requirements: APP-3 SEC-S14-09 defines minimum retention by compliance scope.)*

**[Recommended Pattern · CORE-A2-07]** Task-level P-track evidence: Decision, Business context, Accountability chain (§3.5), Governance controls, Outcome, Provenance marker (D/P, model family, trust boundary), Telemetry cross-reference.

**[Recommended Pattern · CORE-A2-08]** Orchestration-level P-track evidence: Goal, Executed sequence (per-step D/P + outcome refs), Planning rationale, Replanning events, Orchestration accountability (§3.5), Completion assessment, Aggregate oversight quality. *(Note: the goal, executed step sequence with per-step D/P, and replanning events fields within this pattern are elevated to Required Outcome by CORE-A2-08a below.)*

**[Required Outcome · CORE-A2-08a]** Orchestration-level P-track evidence MUST include at minimum: goal, executed step sequence with per-step D/P, and all replanning events with triggers. These fields satisfy the accountability obligation in CORE-A4-04. The remaining fields in CORE-A2-08 (orchestration accountability, completion assessment, aggregate oversight quality) are Recommended Pattern — valuable for governance quality but not required for accountability traceability.

**[Reference Mechanism · CORE-A2-09]** Graph-structured storage for P-track execution paths. Rationale: multi-hop queries, variant analysis, drift detection. Alternative: relational with path reconstruction.

#### 3.4.3 Evidence Integrity

**[Required Outcome · CORE-A2-10]** PxER entries MUST be verifiable across three independent dimensions:

| Dimension | Question | Method |
|:---|:---|:---|
| D/P Conformance | Executed on intended track? | Statistical (L2) or telemetry (L3/L4) |
| Evidence Authenticity | Is the contribution authentic? | Async spot-check vs. source records |
| Write-Path Provenance | Was the assembly service authorised? | Signed token vs. independent audit log |

These are complementary. MATCH + unverified authenticity is possible. Verified authenticity + MISMATCH is possible. *(Full requirements: APP-3.)*

#### 3.4.4 Entity Correlation

PxER step records carry optional entity references. Process instances carry entity correlations linking entities across steps and systems. Full architecture: APP-4.

**Implementation choices.** Storage architecture (relational, graph, document), analytics engine, and visualisation are implementation choices.

#### 3.4.5 Recovery Evidence A recovery path is any alternate execution path invoked in response to a deviation from the primary path — mismatch (§3.4.1), drift signal (A10), verification failure (APP-3 SEC-S3-07 disagreement), circuit-breaker trip, exception, incident. Recovery events are governance-critical decision paths: they occur under time pressure, may involve elevated autonomy, and materially affect the accountability chain. Without protocol-standardised recovery evidence, multi-vendor incident reconstruction fails — the same failure class `mismatch_type` (CORE-A2-04) addresses for conformance evidence.

**Structural placement.** A recovery invocation MUST be recorded as a `recovery_evidence` block attached to the original step's PxER record; it MUST NOT be recorded as a new PxER step. The step identifier is preserved. Repeat recoveries on the same step (successive retries, chained fallbacks, or escalation after failed recovery) MUST append additional `recovery_evidence` entries to the same step record with a monotonic `sequence` field starting at 1. Cross-step recovery paths (e.g., an `escalate` outcome that spawns a new governance flow) are recorded as new steps in the escalation flow's own PxER, cross-referenced via `evidence_refs`. This preserves the invariant that PxER step count reflects primary-path execution, not recovery volume.

**Named principal.** The `authorized_by` field MUST reference a named principal identified per APP-3 SEC-S13-01 (agent identity) or SEC-S13-02 (authenticated human identity). A generic agent label (e.g., a role or product name without cryptographic identity binding) MUST NOT satisfy `authorized_by`. Where recovery authorisation is architectural rather than principal-bound (e.g., a D-track retry rule fires automatically), `initiator: D-track` MUST be set and `authorized_by` MUST reference the governance-control identity that owns the retry rule per APP-3 SEC-S6-04.

**[Required Outcome · CORE-A2-13]** When a PxER step invokes a recovery path, the step record MUST include a `recovery_evidence` object with the following fields:

| Field | Definition | Populated |
|:---|:---|:---|
| `path_class` | Category of recovery invoked: `retry`, `fallback`, `escalate`, `undo`, `circuit-break`, `halt`, `degrade` | Always when recovery invoked |
| `initiator` | Layer that initiated recovery: `D-track` (deterministic control), `P-track` (agent decision), `human` (explicit human authorization) | Always |
| `authorized_by` | Named principal (authenticated human identity or agent identity with declared authority scope) per APP-3 SEC-S13 | Always |
| `outcome` | Controlled vocabulary per CORE-A2-14 | Always |
| `evidence_refs` | References to the deviation evidence that triggered recovery: mismatch record, drift signal, verification-disagreement ID, incident ID, exception record | Always |
| `latency_ms` | Time from deviation detection to recovery-outcome recording | Always |
| `sequence` | Monotonic integer starting at 1; identifies the nth recovery invocation on this step | Always (=1 for first recovery on step) |

Recovery events with `initiator: human` are subject to A6 engagement quality requirements. Recovery events with `initiator: P-track` are subject to A4 accountability chain per CORE-A4-06.

**[Required Outcome · CORE-A2-14]** Recovery outcome controlled vocabulary. The `recovery_evidence.outcome` field MUST take exactly one of:

| Value | Meaning | Governance Action |
|:---|:---|:---|
| `recovered` | Deviation resolved; execution can continue on primary path | Record; no further action required |
| `partial` | Deviation resolved incompletely; residual condition remains | Escalate — residual requires human judgment or secondary recovery |
| `failed` | Recovery attempted and did not resolve the deviation | Escalate — original deviation persists; primary path blocked |
| `bypassed` | Recovery skipped by design (recovery not applicable or intentionally not invoked) | Record; bypass rationale MUST appear in `evidence_refs` |
| `self_healed` | Deviation resolved without recovery invocation (transient condition self-corrected) | Record; no further action required |

Outcomes `partial` and `failed` trigger A6 engagement quality requirements at the receiving human authority. Outcome `bypassed` requires an autonomous-decision attestation per CORE-A4-06. Outcome `self_healed` is exempt from A4 accountability chain (no decision was made), but the exemption applies only where the `evidence_refs` field references an observation record (telemetry log, health-check trace, transient-condition signal) that distinguishes self-healing from an unrecorded autonomous recovery decision. Where such observation evidence is unavailable, `outcome` MUST be recorded as `recovered` with `initiator: D-track` or `initiator: P-track` per the actual layer, not `self_healed`.

**Cross-tier interaction with APP-3 SEC-S6-05.** Recovery paths invoked on compliance-critical (C0/C1) steps are subject to enforcement-tier parity: a recovery path MUST NOT invoke compliance controls at a lower enforcement tier than the primary path (APP-3 SEC-S6-05). A recovery path structurally unable to invoke controls at parity MUST record `outcome: bypassed` and block execution on C0/C1 steps per SEC-S7-02 fail-closed.

**Implementation choices.** Recovery-path taxonomy expansion (values within `path_class` beyond the seven enumerated), selection algorithm (which recovery path is chosen for which deviation class), infrastructure (event pipeline, retry orchestration, undo handler internals), and time-to-recovery targets are implementation choices. The evidence schema (CORE-A2-13) and outcome vocabulary (CORE-A2-14) are the normative interop surface.

> **Security.** Recovery paths MUST NOT bypass governance controls at their declared enforcement tier (APP-3 SEC-S6-05). Recovery telemetry MUST be write-authenticated per SEC-S4-05 (six-artifact-class enumeration includes execution-record class).

> **Security.** Contributors MUST authenticate. Spot-checks SHOULD verify against source records. Cross-deployment analytics MUST apply differential privacy. Security controls MUST be active before first PxER records accepted. *(APP-3: Evidence Integrity, Write-Path Auth, Tenant Isolation, Temporal Activation Ordering.)*

---

### Governance: Accountability, Compliance, and Oversight (A4–A6)

### 3.5 A4 — Accountability Architecture

**What:** WHO is responsible at each level — and what EVIDENCE makes accountability defensible. A4 covers both task-level and orchestration-level accountability.

**Why protocol:** Basic accountability (who approved?) is universal. What the protocol standardises is the evidence chain — measured oversight, named accountability per step, complete chain in the execution record.

#### Task-Level Accountability

**[Required Outcome · CORE-A4-01]** Three-layer accountability chain per step:

| Layer | Scope | Evidence |
|:---|:---|:---|
| **Intent** | Who authorised the Process Frame | Frame version, author, approval record |
| **Execution** | On whose behalf, with what identity | Agent-class, authenticated principal, authority scope |
| **Oversight** | Evidence of informed judgment | Engagement telemetry (A6) |

**[Required Outcome · CORE-A4-02]** PxER step attribution MUST distinguish: human execution, AI agent on behalf of human, autonomous AI action — and the authority scope.

**[Recommended Pattern · CORE-A4-03]** Model family and version identifier in PxER provenance marker. Value is forensic accountability anchoring (what system was in effect), not reproducibility. SHOULD pair with model lifecycle policy. Alternative: omit model version from provenance — reduces forensic traceability for post-hoc investigation but simplifies evidence schema; acceptable for low-risk processes where model identity is not a compliance concern.

#### Orchestration-Level Accountability

**[Required Outcome · CORE-A4-04]** When a process is P-orchestrated (orchestration-level P, §3.3), the PxER MUST record: who set the goal, the executed step sequence with per-step D/P, and any replanning events with triggers.

**[Recommended Pattern · CORE-A4-05]** Orchestration completion gate on Process Frame root:

| Tier | Trigger | Evidence |
|:---|:---|:---|
| `none` | Low-risk, D-dominant | No orchestration-level oversight |
| `review` | Moderate-risk | Process owner confirms completion summary |
| `attestation` | High-risk, compliance-critical | Process owner attests with typed justification |

Rationale: per-step HITL is strong; whole-orchestration oversight depends on aggregating step signals. Alternative: step-level aggregation only — adequate for low-risk flows.

#### Recovery-Decision Accountability

**[Required Outcome · CORE-A4-06]** When a recovery path is invoked (per CORE-A2-13), the three-layer accountability chain (CORE-A4-01) MUST apply to the recovery decision:

| Layer | Scope for recovery decisions | Evidence |
|:---|:---|:---|
| **Intent** | Frame authorship of the recovery discipline for this step class — which recovery paths are permitted, under what deviation conditions, with what tier constraints (per SEC-S6-05) | Frame version + recovery-path policy reference |
| **Execution** | Principal that invoked the recovery — human authorizer or agent identity with declared authority scope | Authenticated principal + authority scope (per CORE-A4-02) |
| **Oversight** | Evidence of informed judgment when `recovery_evidence.outcome` is `partial` or `failed` | HITL engagement telemetry (A6) OR autonomous-decision attestation when `outcome: bypassed` |

Recovery invocation MUST NOT discharge the accountability obligation on grounds of time pressure or infrastructure failure. Post-hoc capture of the accountability chain is acceptable only for `outcome: self_healed` (autonomous transient resolution with no decision to attribute).

Rationale: recovery events historically escape governance because they are treated as infrastructure operations rather than governance decisions. The three-layer chain applies uniformly — recovery is a decision path with declared authority, not an exempt class. The pattern extends CORE-A4-01 to a decision class that has not been made explicit in the protocol until v5.9.

**Implementation choices.** Recovery-path selection logic, recovery-agent classification (recovery agents inherit existing APP-3 SEC-S13-03 authority-provenance discipline; no new agent class), and time-to-authorize targets during incident response are implementation choices.

**Implementation choices.** How the completion gate is presented (standalone, embedded, mobile) and whether it compiles to a terminal D-track step are implementation choices.

> **Security.** Agent session identity MUST be non-deterministically bound across steps. *(APP-3: Agent Identity.)*

---

### 3.6 A5 — Inter-System Compliance

**What:** Compliance rules between systems — requirements no single application owns. Within-system compliance remains application-owned and NOT a protocol concern.

**Why protocol:** Cross-system compliance is the gap nobody fills.

**[Required Outcome · CORE-A5-01]** Compliance requirements carried on a Frame step MUST declare an authorship/authority marker from a two-value set:

| Marker value | Meaning |
|:---|:---|
| `external-mandated` | Enterprise-immutable. The deploying enterprise cannot weaken the constraint. |
| `enterprise-authored` | Customer-overridable. The deploying enterprise owns and may modify the constraint. |

Inheritance semantics: a lower-authority constraint MUST NOT silently weaken a higher-authority constraint. A constraint is **weakened** if its enforcement scope is narrowed, its required evidence is reduced, or its applicability condition is made less restrictive.

APP-IG-03 provides a worked authorship model (the C0–C4 taxonomy) that projects onto this marker; implementations MAY use any granularity that projects unambiguously onto the two-value set.

**[Required Outcome · CORE-A5-02]** Process Frame MUST encode applicable compliance levels per step. PxER MUST evidence compliance status per step.

**[Required Outcome · CORE-A5-03]** Where a Frame step carries compliance requirements at multiple authority levels, an `enterprise-authored` constraint MUST NOT weaken (per CORE-A5-01 definition) an `external-mandated` constraint unless the Frame carries a governed-exception record bearing an **authority reference** identifying the governing authority. A receiving system MAY reject an exception record lacking a resolvable authority reference.

**Implementation choices.** The internal authorship model (e.g. C0–C4 granularity), C0 ingestion, C1 authoring, C2 distribution, and the governed-exception mechanism (full schema, approval chain, audit record) are implementation choices. The marker and the authority reference are the only normative interop surfaces.

> **Security.** Compliance validation MUST detect negative space — absent constraints. *(APP-3: Compliance Validation.)*

---

### 3.7 A6 — HITL Engagement Quality

**What:** The engagement mechanism producing oversight evidence for A4. How human-in-the-loop interactions are structured, measured, and reported.

**Why protocol:** Each implementation defines "human in the loop" differently. A6 defines the engagement schema for comparable HITL quality evidence across implementations.

**[Required Outcome · CORE-A6-01]** HITL engagement quality MUST be measured, not merely required (APP-1 invariant d). A human checkpoint is insufficient; evidence of genuine judgment is required.

**[Required Outcome · CORE-A6-02]** HITL engagement records MUST include: decision made, engagement duration, evidence reviewed.

**[Required Outcome · CORE-A6-03]** HITL engagement records MUST carry an **engagement-fidelity marker** indicating the measurement basis applied (at minimum: `acknowledgement-only` / `behavioural-measured`), so a consuming system can compare oversight quality across implementations without assuming a shared capability schedule. *(The former L1–L4 capability-boundary matrix is an illustrative worked maturity model in APP-IG — non-normative. There is deliberately no per-level capability floor at the protocol layer: an implementation running only L1 engagement measurement is conformant provided its marker honestly reads `acknowledgement-only` and A6-01/A6-02 are met. Which capabilities run at which level is implementation-defined differentiation; a consuming system prices in a low-fidelity marker rather than relying on a mandated schedule.)*

**[Recommended Pattern · CORE-A6-04]** Graduated engagement: Lightweight (acknowledge), Content Review (dwell time, scroll depth), Attestation (+ typed justification). Alternative: single level — uniform but misallocated.

**[Recommended Pattern · CORE-A6-05]** Canary injection — fabricated approvals with known-correct answers. Cryptographically randomised schedule. Presentation-layer only: no source system mock transactions.

**Implementation choices.** Approval surface delivery (standalone, embedded, vendor-native, mobile) is an implementation choice.

> **Security.** Approval surfaces MUST NOT use AI-generated content — verified data only, AI commentary separate. Engagement telemetry MUST respect jurisdictional privacy tiers; detailed metrics off by default. *(APP-3: HITL Security, Telemetry Privacy.)*

---

### 3.8 A7 — Consumption-Mode Parity

**What:** The same governance applies regardless of AI-mediated invocation mode — copilot, autonomous agent, or A2A delegation.

**Why protocol:** Without parity, the same process gets different governance depending on caller type.

**[Required Outcome · CORE-A7-01]** Governance treatment (D/P, compliance, HITL, accountability) MUST be identical for all AI-mediated invocation modes entering through the protocol-governed surface. AI-mediated modes include: copilot interaction, autonomous agent execution, and A2A delegation.

**[Required Outcome · CORE-A7-02]** Traffic bypassing the protocol surface is ungoverned. PxER MUST record which paths were governed and which were not.

**[Required Outcome · CORE-A7-03]** Parity by level:

- **L2:** Parity guaranteed for governed surface.
- **L3:** Reporting parity — application reports mode and telemetry for all AI-mediated paths. Enforcement parity for intra-app paths is vendor choice.
- **L4:** Parity by construction.

**Scope note.** Traditional human-initiated screen transactions (a user navigating an ERP transaction screen) are the governance baseline, not a governed path. The protocol does not add governance to already-human processes — it ensures AI-mediated paths receive equivalent or stronger governance. PxER SHOULD record human-initiated transactions when observable (L3 telemetry) for completeness.

**Implementation choices.** How invocation mode is detected is an implementation choice.

> **Security.** A2A/MCP connections MUST meet transport security baseline. Session identity maintained across modes. *(APP-3: Transport Security, Agent Identity.)*

---

### Lifecycle & Learning (A8–A11)

*Close the loop — execution evidence improves processes. Protocol defines governance obligations and portable schemas; implementation mechanics are implementation choices.*

### 3.9 A8 — Promotion Provenance (P→D)

**What:** When a step's D/P classification changes, the protocol requires a standardised promotion event record and classification provenance marker. The governance record of earned determinism — not the pipeline.

**Why protocol:** Without provenance, promoted rules carry no audit trail.

**[Required Outcome · CORE-A8-01]** Classification provenance on Process Frame steps:

| Value | Meaning |
|:---|:---|
| `born` | Authored D from policy. Never P. |
| `extracted_design` | Identified from SOPs at design time. Human validated. |
| `earned_runtime` | Stable patterns from production. Domain experts validated. |
| `declared` | D without promotion event. MUST carry justification. |
| `permanent_P` | Permanently judgment-dependent. Prevents repeated surfacing. MUST carry justification. |

**[Required Outcome · CORE-A8-02]** When provenance is `extracted_design` or `earned_runtime`: evidence count, evidence window, validator role, validation date, demotion conditions, prior classification.

**[Required Outcome · CORE-A8-03]** Three promotion outcomes MUST be representable: promotion to deterministic execution, delegation to source system rule engine (with mirror record), classification as permanently judgment-dependent.

**[Required Outcome · CORE-A8-04]** Frame transition events recorded in A9 lifecycle: transition type, trigger type (design/runtime), prior and new classification, evidence reference, demotion conditions.

**Implementation choices.** Candidate detection, shadow verification, thresholds, catalogue structures, pipeline architecture, scoring — all implementation choices (Appendix C).

> **Security.** No autonomous self-promotion. Evidence integrity verified before advisory outputs generated. *(APP-3: Promotion Integrity, Feedback Loop Integrity.)*

---

### 3.10 A9 — Intent Evolution

**What:** Process Frame lifecycle: Seed → Observed → Validated → Mature.

**Why protocol:** Without lifecycle tracking, specifications drift from reality silently.

**[Required Outcome · CORE-A9-01]** Lifecycle states:

| State | Meaning | Governance Posture |
|:---|:---|:---|
| **Seed** | Authored from documentation/interviews | Advisory |
| **Observed** | Execution data supplements spec | Strengthened |
| **Validated** | Process owner confirmed | Authoritative |
| **Mature** | Statistical confidence from history | Full weight |

**[Required Outcome · CORE-A9-02]** Every transition MUST be recorded with evidence.

**[Required Outcome · CORE-A9-03]** Evidence integrity MUST be verified before lifecycle transition recommendations are generated. Compromised evidence feeding lifecycle transitions produces incorrect governance posture assessments.

**Implementation choices.** Transition detection heuristics are implementation choices.

> **Security.** CORE-A9-03 is a security requirement (APP-1 Article 3). *(APP-3: Feedback Loop Integrity.)*

---

### 3.11 A10 — Drift Detection

**What:** Specification → evidence → verification they match. The third leg.

**Why protocol:** Drift is invisible without a baseline.

**[Required Outcome · CORE-A10-02]** A conformant implementation MUST produce, on a declared cadence, a conformance report detecting divergence between the governing Process Frame specification and observed execution.

**[Recommended Pattern · CORE-A10-01]** Drift signal types SHOULD include process-level (steps skipped/reordered), orchestration-quality (declining HITL engagement), and intent-staleness (spec diverged from execution). Alternative: implementation-specific signal set — adequate for single-deployment. *(Entity-correlation drift remains a Required Outcome via APP-4 EC-32 (L2+), tested by T-LEARN-13; it is not re-asserted here — naming it as one of a fixed four was a redundant duplicate of the EC-32 obligation.)*

**[Recommended Pattern · CORE-A10-03]** Report schema: drift type, affected steps, evidence window, severity, recommended action. Alternative: implementation-specific — adequate for single-deployment.

**Implementation choices.** Detection algorithms, ML models, threshold tuning are implementation choices. Telemetry data correlation (inference latency trends, model version transitions) MAY serve as an additional drift signal; the protocol defines governance-level signals, and implementations MAY augment with operational telemetry.

**[Required Outcome · CORE-A10-04]** Evidence integrity MUST be verified before drift signals are raised. Compromised evidence feeding drift detection produces false signals that erode governance trust.

> **Security.** CORE-A10-04 is a security requirement (APP-1 Article 3). *(APP-3: Feedback Loop Integrity.)*

---

### 3.12 A11 — Process Intelligence

**What:** Conformant implementations surface intelligence outputs — not just collect data.

**Why protocol:** Comparable analytics require consistently structured records.

**[Recommended Pattern · CORE-A11-01]** The protocol mandates no specific intelligence outputs. Implementations SHOULD derive process intelligence from the PxER corpus (e.g. bottleneck, exception, cost-attribution, promotion-candidate analysis); the specific set is implementation differentiation. *(Aligns A11-01 with the already-RP A11-02 and EC-33. Mineability of the corpus is guaranteed upstream by CORE-A2-01/A2-02 — instance linkage + per-step event fields — so no compensating change is needed.)*

**[Recommended Pattern · CORE-A11-02]** Intelligence output schema SHOULD be standardised for anonymised cross-deployment benchmarking. Rationale: portable intelligence compounds protocol value. Alternative: implementation-specific formats.

**Implementation choices.** Algorithms, visualisation, analytics platform, real-time vs. batch are implementation choices.

> **Security.** Anonymised benchmarking MUST apply differential privacy. Security controls active before first query. *(APP-3: Tenant Isolation, Temporal Activation Ordering.)*

---

## 4. Integration Maturity Model

### 4.1 Why the Protocol Needs Maturity Levels

Enterprise systems exist at radically different integration depths. The protocol is the same at every level (APP-1 invariant e). What varies is data depth and enforcement possible.

```
┌───────────────────────────────────────────────────────────────┐
│  L4  AI-Native      Governance by construction.               │
├───────────────────────────────────────────────────────────────┤
│  L3  App-Enhanced   Intra-app governance via telemetry.       │
│                     MISMATCH detection operational.            │
├───────────────────────────────────────────────────────────────┤
│  L2  API/MCP        Orchestration-level governance.           │
│                     Conformance: STATISTICAL / UNVERIFIABLE.   │
├───────────────────────────────────────────────────────────────┤
│  L1  Screen/RPA     Governed routing + basic execution record.│
└───────────────────────────────────────────────────────────────┘
```

### 4.2 Level Definitions

**Level 1 — Screen Level.** Legacy systems, RPA connectors. Minimal execution record. HITL via governance surface for judgment steps. L1 is for gap-filling in AI-orchestrated processes.

**Level 2 — API/MCP Level.** Modern systems via MCP/A2A/REST. Full orchestration-level governance. D/P conformance: UNVERIFIABLE per-invocation; STATISTICAL where volume permits. HITL measured at governance surface. L2 does NOT expect applications to produce engagement telemetry.

**Level 3 — Application-Enhanced.** Applications contribute intra-app traces, HITL engagement, D/P awareness, compliance evidence. Per-invocation MATCH/MISMATCH operational. L3 is intra-application governance participation — a bounded telemetry integration, not an architectural change.

**[Required Outcome · CORE-L3-01]** L3 telemetry schema. Where the application has P-track governance metadata, an L3-conformant implementation MUST contribute the following fields per step:

| Field | Content |
|:---|:---|
| `execution_engine_class` | deterministic_rules / ai_copilot / ai_autonomous / manual |
| `ai_involvement` | none / advisory / co_pilot / autonomous |
| `human_oversight.occurred` | boolean |
| `human_oversight.engagement_type` | approval / review / attestation / none |
| `conformance.dp_actual` | D / P |
| `confidence_signal` | high / medium / low / not_applicable |

Rationale: closes L2 fidelity gap for high-risk steps. Without normative L3 contribution schema, cross-vendor PxER assembly is structurally infeasible — multi-vendor contribution to one PxER (the L3 value proposition per APP-IG-01 §4) requires field-level interoperability. Implementations that lack P-track governance metadata for a given step MAY omit the contribution for that step (the L3 Floor — D-track telemetry without P-track metadata — remains conformant for steps where P-track metadata is genuinely absent). Field-level extensions beyond the minimum schema are permitted and MUST NOT break consumers parsing the minimum field set.

**Breaking-change note.** CORE-L3-01 was a Recommended Pattern in v5.7 and earlier. Promotion to Required Outcome at v5.8 is a breaking change per APP-1 Article 5. Justification: the L3 cross-vendor contribution value proposition is structurally vacuous without normative field set. No production implementations exist at the time of promotion (protocol is pre-working-group); breaking-change cost is bounded.

**Level 4 — AI-Native.** Governance by construction. Floor and ceiling unified. Frame is the runtime. Entity correlation is a platform primitive.

### 4.3 Agent Model by Maturity Level

Two actors at every level: governance implementation + agent system. Protocol does not prescribe how governance is implemented — only that it meets the declared conformance profile (§4.4).

| Level | Governance Implementation | Agent System | Relationship |
|:---|:---|:---|:---|
| L1 | Manages spec, captures record | RPA bots execute | Governance governs E2E |
| L2 | Manages spec, enforces routing, serves governance surface | AI platform invokes at goal level | Both may orchestrate |
| L3 | + receives intra-app telemetry | + applications report evidence | Collaborative |
| L4 | Embedded in runtime | Agents = consumption mode | Unified |

**Realization patterns.** Dedicated orchestrator, native embedding (L3), sidecar/observer, retrospective audit — all conformant.

### 4.4 Conformance Profiles

**[Required Outcome · CORE-CP-01]** Implementations MUST declare which profile, per scope:

| Profile | Requirement |
|:---|:---|
| **Preventive** | Violations blocked before execution completes |
| **Detective** | Violations flagged within declared SLA |
| **Retrospective** | Violations identified in periodic analysis |

**[Required Outcome · CORE-CP-02]** Multi-profile per scope permitted. Declared profile MUST be honoured.

**[Required Outcome · CORE-CP-03]** Conformance test: (1) Process Frame exists, (2) PxER produced, (3) A3–A11 consistency verified (per the T-GOV-* and T-LEARN-* test suite defined in APP-5 §5.4 and §5.6, applicable requirements only), (4) declared profile met.

**[Required Outcome · CORE-CP-04]** Partial conformance MUST be declared (APP-1 Article 5).

---

## 5. Protocol Applicability

### 5.1 Design Driver

The protocol's design driver is cross-vendor interoperability (APP-1 invariant c). Every normative requirement works across vendor boundaries.

### 5.2 Applicability Within a Single Application

The protocol's artifacts are applicable wherever governed AI execution occurs, including within a single application. The governance gaps the protocol addresses — D/P classification, P-track evidence, HITL quality measurement, accountability attribution — exist within every major enterprise platform.

| Capability | Applicable Intra-App? | What It Adds |
|:---|:---|:---|
| A0 Process Frame | Full | Governance attributes vendor models lack (D/P, compliance, HITL, accountability) |
| A1 Integration Surface | Full | Governance gate for intra-app builder changes |
| A3 D/P Classification | Full | First standardised schema — vendors have ad-hoc separation |
| A2 PxER | Full | P-track evidence vendor records cannot capture |
| A4 Accountability | Full | Three-layer model vs. inadequate vendor attribution |
| A5 Compliance | Partial | C0–C2 applicable; C3–C4 customer policies apply regardless |
| A6 HITL Quality | Full | Engagement measurement no vendor currently provides |
| A7 Parity | Partial | AI-mediated mode parity within application; traditional screens = baseline |
| A8–A11 Learning | Full | Standardised drift detection and intelligence from execution records |

**Full** = fully applicable. **Partial** = applicable but scope narrower intra-app.

The protocol does not replace vendor-internal engines (APP-1 non-goal d). L3 conformance — the intra-application mechanism — is a telemetry integration, not an architectural change. Intra-application adoption is not required for conformance but is the expected consequence of L3/L4 progression and a prerequisite for the cross-vendor governance the protocol enables.

---

## 6. Graceful Degradation

**Compliance-criticality ordinal.** Several requirements tier behaviour by how compliance-critical a step is. The protocol defines a **four-point** compliance-criticality ordinal, most-critical to least:

| Point | Name | Criticality |
|:---|:---|:---|
| **C0** | Regulatory | Highest — externally mandated by law/regulators |
| **C1** | Control-pattern | Enforcement patterns implementing C0 |
| **C2** | Deployment-template | Domain/region packages bridging C1→enterprise |
| **C3C4** | Enterprise | Lowest — corporate policy and local rules (enterprise-owned) |

This ordinal expresses **criticality ranking only** — the scale that CORE-XX-01 (degradation), SEC-S7-02 (degradation), SEC-S3-01 (verification independence), and SEC-S8-03 (promotion approval) threshold against. Four points, not five: no normative requirement draws a boundary between C3 (corporate) and C4 (local) — every consumer treats them as one enterprise band. The informative C0–C4 authorship model (APP-IG-03) sub-divides C3C4 into C3/C4; that distinction is authorship granularity, not criticality, and is not normative here.

The ordinal is distinct from the A5 *overridability* marker (`external-mandated`/`enterprise-authored`, CORE-A5-01): the marker collapses C0/C1/C2 into one `external-mandated` value (correct for overridability — all non-overridable) but cannot express the three-band degradation contract below; the ordinal preserves the criticality cuts that contract needs. A conformant implementation MAY use any internal granularity that projects onto these four ordered points.

**Not a consumer: SEC-S14-09 (retention)** keys on *obligation-source* (regulator / standards-body / enterprise), not criticality rank — a separate authorship-flavoured axis (a standards-body retention can exceed a regulatory one; rank ≠ source). S14-09 retains its obligation-source language; it does not threshold against this ordinal.

**[Required Outcome · CORE-XX-01]** If the governance layer is unavailable, degradation behaviour is compliance-tiered against the criticality ordinal above (APP-3 SEC-S7-02): C0/C1-scoped steps MUST block until governance is restored (fail-closed). C2-scoped steps MUST follow the degradation behaviour declared per step in the Process Frame (fail-closed or fail-open). C3/C4-scoped steps MAY continue ungoverned with a governance-unavailable flag in PxER. PxER gaps for all degraded steps MUST be flagged for retrospective reconciliation.

**[Required Outcome · CORE-XX-02]** Degradation security controls MUST prevent attackers from forcing degradation to bypass compliance-critical governance. *(APP-3: Degradation Security.)*

---

## Appendix A — Protocol Capability Detail by Integration Level

| Cap. | L1 (Screen/RPA) | L2 (API/MCP) | L3 (App-Enhanced) | L4 (AI-Native) |
|:---|:---|:---|:---|:---|
| **A0** | Mandatory fields only | Full orchestration | + app enrichment | Frame = runtime |
| **A1** | N/A | Profile publishes to builders | + vendor-native bidirectional | Internal by construction |
| **A3** | Defined in Frame | + enforced at orchestration | + app reports path | Guaranteed |
| **A2** | Minimal. UNVERIFIABLE | Orchestration-level. STATISTICAL | + intra-app. MISMATCH | Maximum. MATCH |
| **A4** | Governance surface only | Three-layer. Surface measured | + app engagement | Full. Unbroken |
| **A5** | Frame constraints | Cross-system enforcement | + intra-app evidence | Complete |
| **A6** | Governance surface | + telemetry, fatigue, canary | + app-native | Full |
| **A7** | Single mode | Governed surface | Reporting parity | All paths |
| **A8** | Design-time full | + runtime | Richer evidence | Primitive |
| **A9** | Limited data | Full lifecycle | Richer, faster | Continuous |
| **A10** | Sequence only | Process-level | + intra-step quality | All signals |
| **A11** | Limited | Operational | Rich, all outputs | Full loop |

---

## Appendix B — Security Cross-Reference

The authoritative mapping between APP-2 capabilities and APP-3 security domains is maintained in **APP-IG-02 (Cross-Reference Matrix), §1**. Each capability section in this document includes an inline security callout referencing APP-3 by topic; APP-IG-02 provides the complete requirement-level mapping.

---

## Appendix C — Protocol Boundary: What Is NOT a Protocol Capability

**Protocol-Enabled Optimisations** — implementations choose freely:

| Topic | Why Not Protocol |
|:---|:---|
| P→D pipeline mechanics | Protocol records provenance (A8); detection is differentiator |
| Promotion catalogue structures | Protocol defines provenance, not catalogue |
| Orchestration engine | Protocol defines profiles (§4.4), not mechanism |
| Detection algorithms | Protocol defines signals (A10); algorithms free |
| Analytics platform | Protocol defines outputs (A11); computation free |
| Scoring models / thresholds | Implementation tuning |

**Other implementation concerns** — well-established standards or per-platform choices:

| Topic | Why Not Protocol |
|:---|:---|
| Agent Identity (NHI, crypto certs) | Protocol consumes identity; does not define it |
| Multi-Model Orchestration | Model-agnostic |
| SSO/RBAC/MFA | Infrastructure-level; OIDC/SAML |
| Agent Builder (construction) | Protocol defines integration surface (A1), not tooling |
| Financial Circuit Breakers | Protocol captures evidence; threshold = business decision |
| Decision Observability | Per-model; protocol captures process-level via PxER |

---

## Appendix D — Master Requirement Index

| ID | Capability | Level | Short Description | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| CORE-A0-01 | A0 | RO | Mandatory Frame fields per step | ● | ● | ● | ● |
| CORE-A0-02 | A0 | RP | Recommended Frame fields | | ● | ● | ● |
| CORE-A0-03 | A0 | RM | DAG-JSON interchange format | | | | |
| CORE-A1-01 | A1 | RO | Outbound + inbound + notification | | ● | ● | ● |
| CORE-A1-02 | A1 | RO | Governance gate classification | | ● | ● | ● |
| CORE-A1-03 | A1 | RO | Cross-system mediation | | ● | ● | ● |
| CORE-A1-04 | A1 | RP | MCP Server Profile transport | | ● | ● | ● |
| CORE-A1-05 | A1 | RO | Frame schema portability (published schema, consumer validation) | | ● | ● | ● |
| CORE-A1-06 | A1 | RO | Agent Card schema (conform to declared A2A or equivalent standard) | | ● | ● | ● |
| CORE-A3-01 | A3 | RO | Declare intended D/P per step | ● | ● | ● | ● |
| CORE-A3-02 | A3 | RO | Record actual execution track | | ● | ● | ● |
| CORE-A3-03 | A3 | RO | MISMATCH triggers review | | ● | ● | ● |
| CORE-A3-04 | A3 | RO | Task-level vs orchestration-level P | ● | ● | ● | ● |
| CORE-A3-05 | A3 | RP | Route D-steps to deterministic execution | | ● | ● | ● |
| CORE-A3-06 | A3 | RO | Independent D/P verification on compliance-critical steps | | ● | ● | ● |
| CORE-A2-01 | A2 | RO | Immutable record, during execution | ● | ● | ● | ● |
| CORE-A2-02 | A2 | RO | Step fields: id, system, timestamp, tx ref | ● | ● | ● | ● |
| CORE-A2-03 | A2 | RO | Conformance + trust schema (7 fields) | ● | ● | ● | ● |
| CORE-A2-04 | A2 | RO | Mismatch type enum (5 values) | ● | ● | ● | ● |
| CORE-A2-04a | A2 | RO | DEGRADED status: mismatch_type MUST be null | ● | ● | ● | ● |
| CORE-A2-04b | A2 | RO | A2 state machine (10 conformant × 3-field combinations; 8 derivation rules) | ● | ● | ● | ● |
| CORE-A2-05 | A2 | RO | Conformance by maturity level | ● | ● | ● | ● |
| CORE-A2-06 | A2 | RO | Evidence vs. telemetry distinction | ● | ● | ● | ● |
| CORE-A2-07 | A2 | RP | Task-level P-track evidence schema | | ● | ● | ● |
| CORE-A2-08 | A2 | RP | Orchestration-level P-track evidence schema | | ● | ● | ● |
| CORE-A2-08a | A2 | RO | Mandatory orchestration P-track fields (A4-04 dependency) | | ● | ● | ● |
| CORE-A2-09 | A2 | RM | Graph-structured P-track storage | | | | |
| CORE-A2-10 | A2 | RO | Three evidence integrity dimensions | ● | ● | ● | ● |
| CORE-A2-11 | A2 | RO | Cross-enterprise governance: boundary observation only | | ● | ● | ● |
| CORE-A2-12 | A2 | RO | Unmanaged: observed invocation only, explicit marker | ● | ● | ● | ● |
| CORE-A2-13 | A2 | RO | Recovery evidence schema (7 fields) on recovery-invoked steps | | ● | ● | ● |
| CORE-A2-14 | A2 | RO | Recovery outcome controlled vocabulary (5 values) | | ● | ● | ● |
| CORE-A4-01 | A4 | RO | Three-layer accountability (task) | ● | ● | ● | ● |
| CORE-A4-02 | A4 | RO | PxER execution attribution | ● | ● | ● | ● |
| CORE-A4-03 | A4 | RP | Model version in provenance marker | | ● | ● | ● |
| CORE-A4-04 | A4 | RO | Orchestration accountability fields | | ● | ● | ● |
| CORE-A4-05 | A4 | RP | Orchestration completion gate (3 tiers) | | ● | ● | ● |
| CORE-A4-06 | A4 | RO | Recovery-decision accountability chain | | ● | ● | ● |
| CORE-A5-01 | A5 | RO | Two-value authorship marker + weaken-definition | ● | ● | ● | ● |
| CORE-A5-02 | A5 | RO | Frame encoding + PxER evidence | ● | ● | ● | ● |
| CORE-A5-03 | A5 | RO | Constraint-inheritance integrity (authority-reference) | | ● | ● | ● |
| CORE-A6-01 | A6 | RO | Measured quality, not just approval | ● | ● | ● | ● |
| CORE-A6-02 | A6 | RO | Engagement record minimum fields | ● | ● | ● | ● |
| CORE-A6-03 | A6 | RO | Engagement-fidelity marker (matrix → IG) | | ● | ● | ● |
| CORE-A6-04 | A6 | RP | Graduated engagement levels | | ● | ● | ● |
| CORE-A6-05 | A6 | RP | Canary injection | | ● | ● | ● |
| CORE-A7-01 | A7 | RO | AI-mediated mode parity | | ● | ● | ● |
| CORE-A7-02 | A7 | RO | Record governed vs. ungoverned paths | ● | ● | ● | ● |
| CORE-A7-03 | A7 | RO | Parity by level | | ● | ● | ● |
| CORE-A8-01 | A8 | RO | Classification provenance (5 values) | ● | ● | ● | ● |
| CORE-A8-02 | A8 | RO | Promotion evidence fields | ● | ● | ● | ● |
| CORE-A8-03 | A8 | RO | Three promotion outcomes | ● | ● | ● | ● |
| CORE-A8-04 | A8 | RO | Frame transition events | ● | ● | ● | ● |
| CORE-A9-01 | A9 | RO | Lifecycle states (4) | ● | ● | ● | ● |
| CORE-A9-02 | A9 | RO | Transition recording | ● | ● | ● | ● |
| CORE-A9-03 | A9 | RO | Evidence integrity before lifecycle recommendations | | ● | ● | ● |
| CORE-A10-01 | A10 | RP | Drift signal types (recommended) | | ● | ● | ● |
| CORE-A10-02 | A10 | RO | Conformance report on declared cadence | | ● | ● | ● |
| CORE-A10-03 | A10 | RP | Report schema | | ● | ● | ● |
| CORE-A10-04 | A10 | RO | Evidence integrity before drift signals | | ● | ● | ● |
| CORE-A11-01 | A11 | RP | Process intelligence (recommended) | | ● | ● | ● |
| CORE-A11-02 | A11 | RP | Standardised output schema | | ● | ● | ● |
| CORE-L3-01 | L3 | RO | L3 Enhanced telemetry schema (6 minimum fields) | | | ● | |
| CORE-CP-01 | §4.4 | RO | Declare profile per scope | ● | ● | ● | ● |
| CORE-CP-02 | §4.4 | RO | Multi-profile; honour declared | ● | ● | ● | ● |
| CORE-CP-03 | §4.4 | RO | Conformance test (4 criteria) | ● | ● | ● | ● |
| CORE-CP-04 | §4.4 | RO | Declare partial conformance | ● | ● | ● | ● |
| CORE-XX-01 | §6 | RO | Compliance-tiered graceful degradation | ● | ● | ● | ● |
| CORE-XX-02 | §6 | RO | Degradation security | ● | ● | ● | ● |

**Key:** RO = Required Outcome · RP = Recommended Pattern · RM = Reference Mechanism

**L-level applicability (●):** For RO rows, ● means the requirement is mandatory for conformant implementations at that level. For RP rows, ● means the recommendation is relevant and deviation requires documented justification. For RM rows, applicability is informative — the mechanism is a working group starting point, not level-bound. Empty cells indicate the requirement does not apply at that level (typically because the integration depth does not support it).

**Known Open Issues** (gap reports pending — not yet protocol requirements):

- *Sampling provenance for nested AI activity.* When an external system performs recursive agentic work (multiple LLM calls and tool loops), a single `ai_involvement` enum does not capture depth. Gap report pending: APP-3 / A3.
- *Correlation semantics for long-running A2A tasks.* Multi-turn A2A tasks with delayed completions need richer correlation beyond single-request spans. Gap report pending: APP-4.

---

## Appendix E — Glossary

| Term | Definition |
|:---|:---|
| **Process Frame** | Structured, AI-consumable governed process specification |
| **PxER** | End-to-end, immutable execution record — governance data + transaction references |
| **D/P Classification** | Formal Deterministic/Probabilistic boundary per step |
| **Task-level P** | Bounded probabilistic operation. Evaluable. |
| **Orchestration-level P** | Goal decomposition. Plan as output. Not evaluable. |
| **Conformance Delta** | Intended vs. actual D/P — primary governance instrument |
| **D/P Conformance Schema** | 7-field PxER step record (§3.4.1). `conformance_status`: MATCH · MISMATCH · UNVERIFIABLE · DEGRADED. `mismatch_type` (5 values): D_intended_P_executed · P_intended_D_executed · D_intended_UNVERIFIABLE · P_intended_UNVERIFIABLE · CONFLICT. When DEGRADED, mismatch_type is null. |
| **Trust Boundary Type** | internal · enterprise-external · cross-enterprise-external · unmanaged |
| **Evidence vs. Telemetry** | Evidence = accountability. Telemetry = debugging. |
| **Classification Provenance** | born · extracted_design · earned_runtime · declared · permanent_P |
| **Conformance Profile** | Preventive · Detective · Retrospective |
| **Governance Floor / Ceiling** | Floor: declare, record, detect, escalate. Ceiling: MATCH by construction (L4). |
| **C0–C4** | Compliance authorship: Regulatory → Local Rules |
| **HITL** | Human-in-the-Loop. Measured quality, not just approval. |
| **Orchestration Completion Gate** | none · review · attestation |
| **L1–L4** | Screen/RPA · API/MCP · App-Enhanced · AI-Native |
| **Telemetry Contribution Protocol** | Standardised event schema by which L3 applications contribute intra-app execution data to PxER assembly |
| **MCP Conformance Profile** | MUST-level security baseline for protocol-governed MCP endpoints: mutual TLS, OAuth 2.1, DPoP. Defined in APP-3 |
| **LITL (Lies-in-the-Loop)** | Attack class where malicious content embedded in AI-read documents poisons HITL approval surfaces. Mitigated by rendering surfaces from verified data. Defined in APP-3 |

---

## Appendix F — Requirement Rationale Digest

This appendix provides plain-language rationale for each capability's requirements — explaining *why* specific fields and capabilities are required. Informative; intended for implementors and working group members evaluating requirements during deliberation.

| Capability | Requirements | Why These Specific Requirements |
|:---|:---|:---|
| **A0 Process Frame** | CORE-A0-01 through A0-03 | Without a standardised Frame format, every deployment reinvents process capture. The mandatory fields (step ID, executing system, intended D/P, dependency chain, accountability owner) are the minimum needed for any governance query: what should happen, who is responsible, what track, in what order. Recommended fields (A0-02) enable the full capability set but are not gate requirements. DAG-JSON (A0-03) is a Reference Mechanism because interchange format is an interoperability surface requiring agreement. |
| **A1 Integration Surface** | CORE-A1-01 through A1-04 | The three interaction patterns (outbound, inbound, notification) are necessary and sufficient for bidirectional governance propagation. The governance gate classification (A1-02) exists because unstructured builder contributions without governance attributes create a gap that grows silently. MCP Server Profile (A1-04) is Recommended Pattern because MCP is the adopted standard, but REST alternatives are conformant. |
| **A3 D/P Classification** | CORE-A3-01 through A3-06 | D/P classification is the trust anchor. Declaring intended classification (A3-01) and recording actual (A3-02) produces the conformance delta — the primary governance instrument. MISMATCH triggering review (A3-03) is Required because silent misclassification bypasses governance without visible violation. The task-level vs. orchestration-level P distinction (A3-04) matters because they carry different evidence requirements and governance obligations. Independent verification on compliance-critical steps (A3-06) addresses the single-classifier-as-trust-anchor risk. |
| **A2 PxER** | CORE-A2-01 through A2-14 | PxER is the evidence backbone. Immutability during execution (A2-01) enforces APP-1 invariant b. The 7-field conformance schema (A2-03) answers two questions: did the right thing happen (D/P conformance), and can we verify it (trust boundary). The conformance assessment uses 4 conformance statuses (MATCH, MISMATCH, UNVERIFIABLE, DEGRADED) and 5 mismatch types (A2-04) — 9 distinct values across two fields that together classify every combination of intended/actual/observable/available. CONFLICT detects the adversarial case (system reports compliance but statistical evidence contradicts); DEGRADED captures the infrastructure failure case (governance layer unavailable). Evidence vs. telemetry distinction (A2-06) matters because they have different retention policies, access controls, and governance weight. Cross-enterprise boundary observation (A2-11) and unmanaged markers (A2-12) are honest about evidence limits at trust boundaries. Recovery evidence schema (A2-13) and outcome vocabulary (A2-14) close the recovery-event evidence gap: without protocol-standardised recovery vocabulary, multi-vendor incident reconstruction fails at the recovery-path boundary — the same failure class `mismatch_type` addresses for conformance. Recovery is a governance-critical decision path with time-pressure risks; the seven-field schema (path class, initiator, authorized_by, outcome, evidence_refs, latency_ms, sequence) is the minimum needed for auditor reconstruction, including differentiation of first-attempt from repeat recovery. The five-value outcome vocabulary is exhaustive for recovery termination states — `self_healed` is distinguished from `recovered` because the former had no decision to attribute; `bypassed` is distinguished from `failed` because the former was a design choice, not an attempted-and-failed action. |
| **A4 Accountability** | CORE-A4-01 through A4-06 | Three-layer accountability (intent, execution, oversight) is necessary because "who approved?" is insufficient — it conflates authority, execution identity, and oversight quality. Orchestration accountability (A4-04) is Required because P-orchestrated processes need goal-setter and replanning attribution that task-level accountability does not capture. Orchestration completion gate (A4-05) is Recommended because whole-orchestration oversight is valuable but the right tier depends on risk. Recovery-decision accountability (A4-06) extends the three-layer chain to recovery events — historically escaped governance because treated as infrastructure. The v5.9 extension makes explicit that recovery is a decision path with declared authority, not an exempt class. Time pressure does not discharge the accountability obligation; only `outcome: self_healed` (autonomous transient resolution) is exempt because no decision was made. |
| **A5 Compliance** | CORE-A5-01, A5-02, A5-03 | The interop contract for cross-system compliance is a two-value authorship marker (`external-mandated` / `enterprise-authored`) — the minimum a foreign system needs to know whether a constraint is enterprise-immutable or customer-overridable, plus per-step compliance evidencing (A5-02) and constraint-inheritance integrity (A5-03: an enterprise-authored constraint cannot silently weaken an external-mandated one without a governed-exception record carrying an authority reference). The C0–C4 taxonomy is a worked authorship model (see APP-IG-03) that projects onto the marker — it is implementation granularity, not the protocol surface. Within-system compliance remains the application's domain. |
| **A6 HITL Quality** | CORE-A6-01 through A6-05 | Measured quality, not just approval (A6-01) is a protocol invariant (APP-1 invariant d). Minimum engagement fields (A6-02) — decision, duration, evidence reviewed — are the minimum needed to distinguish genuine judgment from rubber-stamping. The engagement-fidelity marker (A6-03) lets a consuming system compare oversight quality across implementations without assuming a shared capability schedule; the former L1–L4 capability matrix is now an illustrative maturity model in APP-IG (non-normative), since *which* capabilities run at *which* level is implementation differentiation, not an interop contract. Graduated engagement (A6-04) and canary injection (A6-05) are Recommended because they improve measurement but their specific implementation is a design choice. |
| **A7 Parity** | CORE-A7-01 through A7-03 | Without parity, the same process gets different governance depending on caller type — a compliance gap that regulators will flag. A7-01 requires identical governance for AI-mediated modes. A7-02 requires recording which paths were governed — ungoverned traffic must be visible. A7-03 defines parity by level because L2 guarantees on governed surface, L3 adds intra-app reporting, and L4 achieves parity by construction. |
| **A8–A11 Learning** | CORE-A8-01 through A11-02 | Classification provenance (A8) answers "how did this step become deterministic?" — the question regulators will ask. Five provenance values are exhaustive for the classification origin. Lifecycle states (A9) track specification maturity from seed to mature — without this, specs drift from reality silently. Drift detection closes the loop between specification and evidence: the divergence report on declared cadence (A10-02) is the Required Outcome; the specific drift signal *types* (A10-01) are Recommended, since two systems detecting different signal types do not break cross-system governance (entity-correlation drift remains Required via APP-4 EC-32, not re-asserted here). Process intelligence (A11-01) is Recommended, not mandated — no intelligence output crosses a system boundary as a wire contract; the mineable corpus (A2-01/A2-02) is the actual interop substrate. |
| **Cross-cutting** | CORE-XX-01, XX-02, CP-01 through CP-04 | Graceful degradation (XX-01) is compliance-tiered: C0/C1 steps fail-closed (governance integrity overrides availability for regulatory-critical steps), C2 follows the declared degradation behaviour per step, and C3/C4 may fail-open (governance MUST NOT block business execution for non-regulatory steps). Degradation security (XX-02) prevents forced degradation to bypass compliance. Conformance profiles (CP-01–04) enforce APP-1 Article 5: role-based, decomposed, partial conformance declared. |

> *Note: This appendix is informative. The normative requirements are in §3. A more detailed rationale document with worked examples is planned for the APP-IG series.*

---

## Appendix G — HITL Capability Maturity Model (Informative)

*Non-normative. (DR-02 DR2-D1.) The former CORE-A6-03 L1–L4 capability-boundary matrix is retained here as an illustrative maturity model — a typical capability progression, NOT a conformance requirement. The normative A6-03 surface is the engagement-fidelity marker (§3.7); which capabilities an implementation runs at which level is implementation-defined differentiation. A consuming system prices in the declared fidelity marker rather than relying on this schedule. Pending migration to a designated APP-IG topic (backlog).*

| Capability | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|
| Engagement measurement (inter-system) | ● | ● | ● | ● |
| Canary injection (inter-system) | Limited | ● | ● | ● |
| Engagement measurement (intra-system) | — | — | ● | ● |
| Canary injection (intra-system) | — | — | Vendor choice | ● |
| Cross-surface fatigue detection | — | Governance surface | + vendor surfaces | ● |

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 5.12
**Normative status:** Normative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-2 — Core Technical Specification.*
