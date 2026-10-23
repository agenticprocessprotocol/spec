# APP-4

Agentic Process Protocol

## Entity Correlation Architecture

| | |
|:---|:---|
| **Version** | 2.3 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Audience** | Protocol implementors, agent builder platform teams, ERP vendor architects, enterprise governance teams |
| **Normative status** | This document is normative. Governed by APP-1. Equal standing with APP-2. |
| **Companion documents** | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-5 (Conformance Profiles), APP-IG-02 (Cross-Reference Matrix), APP-R1 (Frame Schema) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |
| **Version-reference convention** | Companion documents cited by name only in body prose. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-4 is the normative entity-correlation architecture of the Agentic Process Protocol. It defines requirements for cross-system entity tracking in governed processes, including the three-class applicability model.
>
> **Status:** Normative. Requirements expressed using RFC 2119/8174 keywords are binding within the declared scope.
>
> **Authority and precedence:** Governed by APP-1. Peer to APP-0, APP-2, APP-3, and APP-5 within the constitutional frame.
>
> **Use this document for:** Entity-correlation requirement IDs (EC-nn), the three-class applicability model, cross-system reference semantics, and status-class enforcement rules.
>
> **Related documents:** APP-0 (objectives), APP-1 (Constitution), APP-2 (PxER entity references), APP-3 (S14 entity-security cross-references), APP-5 (role applicability), APP-IG-02 (traceability).

---

## How to Read This Document

Normative elements are classified at exactly one of three specificity levels (APP-1 Article 4):

| Marker | Level | Meaning |
|:---|:---|:---|
| **[Required Outcome]** | What must be true | Verifiable outcome using MUST. Any conformant mechanism qualifies. |
| **[Recommended Pattern]** | How the protocol suggests achieving it | Expressed using SHOULD. Alternatives documented. Deviation requires justification. |
| **[Reference Mechanism]** | A specific mechanism proposed | Informative. Working group starting point. |

This document uses RFC 2119/8174 normative keywords. MUST, SHOULD, MAY in all capitals carry their defined meanings.

Each section follows: definition → protocol rationale → normative requirements → recommended approach → implementation choices → security cross-references.

Every normative element carries a requirement ID: `EC-nn` for entity correlation requirements. The Master Requirement Index (Appendix D) provides a consolidated lookup. When referenced from documents outside the APP series, prefix with `APP-` (e.g., `APP-EC-01`).

---

## 1. Introduction

### 1.1 What This Specification Defines

APP-2 (Core Technical Specification) defines 12 protocol capabilities (A0–A11) for governed process execution. A0 specifies the Process Frame. A2 specifies the PxER. Together they capture what should happen and what did happen — step by step, across vendor boundaries.

Neither artifact understands the **entities** flowing through those steps. When PxER records "Step 3 executed in System A" and "Step 5 executed in System B," it captures what happened. It does not capture that both steps acted on the same person, the same cost centre, or the same asset — or that the entity state is now inconsistent between the two steps.

Entity correlation closes this gap. It is a first-class protocol capability — equal in standing to the capabilities defined in APP-2 — that defines how governed process execution captures, correlates, and verifies the business entities flowing through process steps. This specification defines the protocol-level requirements for:

- **Declaring** which business entities are involved in each process step (entity correlation requirements on Process Frame steps).
- **Recording** entity references extracted from step execution (entity correlation requirements on PxER step records).
- **Correlating** entity references across steps within governed process instances.
- **Verifying** entity state consistency post-execution.

These capabilities make PxER an entity-aware governance instrument — enabling cross-system and intra-system audit, data consistency detection, compliance-scoped entity lineage, and entity-enriched process intelligence.

### 1.2 The Protocol Capability Test

Entity correlation is a protocol concern because: when each deployment implements entity tracking differently (or not at all), governance quality degrades — regardless of whether a governed process spans multiple systems or operates within a single application.

Consider two scenarios. In a cross-vendor onboarding process spanning HR, IT, and Finance systems, an auditor reconstructing the process must manually correlate entity references across systems — employee IDs, user accounts, cost centre codes — with no standardised method for linking them. In a single-application process where an ERP handles both the hiring action and the payroll setup, the ERP transaction record captures the PO number and the payroll configuration but not the entity relationships that informed either — the reasoning that connected a specific cost centre assignment to a specific benefit election remains invisible in the audit trail.

Both scenarios share the same governance gap: the entities flowing through governed process steps are not captured, correlated, or verified by the execution record. The gap exists wherever processes involve judgment-dependent steps, AI-mediated decisions, or entity state that must be consistent across process steps — whether those steps cross vendor boundaries or module boundaries within a single platform.

Without a standardised approach, every deployment reinvents entity tracking — producing incompatible entity references, non-comparable correlation confidence, and no portable entity-enriched process intelligence.

### 1.3 Relationship to Other APP Documents

| Document | Relationship |
|:---|:---|
| **APP-1 (Constitution)** | Governs this document. Constitution prevails on conflict. |
| **APP-0 (Protocol Objectives)** | Normative peer under APP-1 §4. Entity correlation contributes to the protocol objectives defined in APP-0; on conflict between APP-0 and APP-4, APP-1 §4 applies. |
| **APP-2 (Core Specification)** | This document specifies the entity-correlation extension of A0 (Process Frame) and A2 (PxER) artefacts. Equal normative standing. APP-2 core capabilities do not depend on APP-4 for execution but interoperate with it wherever entity correlation is declared. |
| **APP-3 (Security Architecture)** | Security requirements for entity correlation. Cross-ref: Appendix B. Equal standing. |
| **APP-5 (Conformance Profiles)** | Role-based profiles. Entity correlation conformance obligations by role and L-level are defined by APP-5 per APP-1 Article 5; on conformance conflict, APP-5 prevails. |
| **APP-IG series (Implementation Guides)** | Informative. Worked examples for entity extraction configuration, correlation strategies, and reconciliation patterns. |

### 1.4 Design Principles

Two principles govern the architecture:

**Inference-first.** The primary correlation mechanism discovers entity relationships from execution data — PxER co-occurrence patterns across process instances. No external integration is required. This works from day one with sufficient process volume.

**Cold-start behaviour.** Before an implementation has accumulated sufficient evidence to infer correlations at declared confidence, its correlation state is `no_correlation` (not "low confidence"). During this window: (a) implementations MUST NOT produce inferred-mode correlation claims below the declared evidence threshold (EC-16); (b) implementations MAY operate populated-mode exclusively where populated sources are available; (c) implementations MAY operate without correlation, in which case reconciliation status (EC-22) reports `no_correlation` and correlation-dependent governance capabilities (e.g., cross-system audit acceleration in §2) are declared unavailable until threshold. The evidence threshold at which inferred-mode claims become permitted is an implementation choice; the threshold MUST be declared and documented in the implementation's conformance profile.

**Populated as validation.** Where customers have existing semantic infrastructure (MDM, integration suites, data lakes, or semantic layer platforms), those sources bootstrap and validate inferred correlations. They accelerate confidence but are not prerequisites.

### 1.5 Non-Goals

Four boundaries that prevent scope creep:

(a) **The protocol does not define or own a universal business ontology.** Entity type labels are tenant-scoped. The protocol discovers and tracks entity relationships; it does not define what entities mean.

(b) **The protocol does not replace MDM.** Where MDM exists, the protocol consumes its correlation keys as a populated source. Where MDM does not exist, inference works without it.

(c) **The protocol does not require external semantic infrastructure as a prerequisite.** Vendor knowledge graphs, active metadata platforms, and semantic interchange formats are optional accelerators for the populated path. Inference mode is the default and requires none of them.

(d) **Per-step entity extraction is optional; correlation infrastructure at L2+ is not.** Individual Process Frame steps MAY omit `entity_extract` declarations, and core APP-2 capabilities (A0–A11) MUST function on such steps without entity enrichment (EC-06). This preserves adoption gradients: a deployment can begin governing processes with zero entity extraction and add extraction incrementally. However, the correlation infrastructure — inferred mode (EC-15), populated mode (EC-19), the entity correlation registry (EC-25), and reconciliation (EC-22) — is mandatory at L2+ for conformant implementations. Entity correlation addresses an AI-specific risk vector (§1.6) that is structurally invisible to any single-system observability layer; a governance protocol governing AI-executed processes cannot make the correlation *capability* optional without leaving that risk vector uncovered. What can be calibrated is *scope* (which processes declare entity extraction), not *presence* (whether the implementation supports correlation at all).

**Three-class applicability model (normative).** The applicability model is stated normatively in APP-4 with an informative gloss in APP-IG-02. There are three obligation classes with distinct applicability triggers:

| Obligation class | Applicability trigger | L-level scope |
|:---|:---|:---|
| **1. Per-step entity reference production** (EC-07 through EC-11) | Active only when a Frame step declares `entity_extract`. Absence of `entity_extract` on any given step MUST NOT prevent step execution (EC-06). A conformant Governance Orchestrator can operate over Frames with zero `entity_extract` declarations without triggering EC-07/08/09/10/11 obligations. This is **use optionality**. | Applies at any L-level where entity_extract is declared. |
| **2. Correlation infrastructure capability** (EC-15 inferred mode; EC-19 populated mode; EC-25 registry persistence; EC-22 reconciliation) | Mandatory for L2+ Governance Orchestrator conformance regardless of whether any specific Frame declares `entity_extract`. This is an implementation-capability obligation: the runtime MUST be able to perform inferred correlation, populated import, registry persistence, and reconciliation when called upon by a Frame that does declare entity_extract. This is **capability applicability**, not use optionality. | Mandatory at L2+ for Governance Orchestrator role. |
| **3. Entity-correlation-specific security** (EC-38 through EC-47) | Mandatory whenever obligations from class 1 or class 2 apply, and additionally wherever any entity data flows through the implementation, at any L-level. | Applies at any L-level where any entity data flows through the implementation. |

**Terminology discipline.** The suite MUST use **use optionality** to refer to class 1 (whether a Frame declares `entity_extract`) and **capability applicability** to refer to class 2 (whether an L2+ implementation supports correlation). Using "optional" without either qualifier is a documentation defect; the two are constitutionally different obligations.

**Enterprise-buyer question this answers.** *"Does an L2+ Governance Orchestrator have to implement inferred correlation, populated import, reconciliation, and registry persistence even if no process scope in my deployment declares entity_extract?"* — **Yes.** L2+ conformance is capability-based, not usage-based. The obligation is that the runtime CAN perform correlation when invoked, not that any given Frame invokes it. An enterprise that will not use entity correlation at all MAY declare conformance to core APP-2 without entity correlation capability, but that is a distinct L1 conformance scope; L2+ conformance requires the capability.

### 1.6 Why Entity Correlation Becomes Critical with Agents

The use cases in §2 apply to both human-operated and agent-operated processes. When AI agents execute cross-system processes, entity correlation is more critical, not less:

- **Agents lack informal context.** Human operators carry implicit knowledge about entity relationships across systems. Agents execute configured steps. Entity correlation catches entity state divergences that a human would have caught informally.
- **Agent intent does not equal business outcome.** AI observability tools confirm tool calls were made. PxER with entity references confirms what actually happened to business entities across systems. The distinction: observability tracks what the agent thought it did; entity correlation tracks what actually happened.
- **Agent-to-agent handoffs lose informal context.** Human handoffs carry context via conversation. Agent handoffs via A2A or MCP pass structured parameters only. Entity correlation reconstructs context from execution data.
- **Agent execution volume compounds errors faster.** An undetected entity mapping error propagates through hundreds of agent-executed instances before detection. Entity correlation enables anomaly detection on the first statistical deviation.
- **Agent audit requirements are deployment-dependent but structurally stricter.** For AI-executed decisions in jurisdictions or regulated sectors that require explainability (e.g., EU AI Act high-risk system provisions, financial services regulator supervisory expectations for AI-assisted decisions, healthcare regulator provisions on algorithmic decision transparency), entity-enriched PxER provides the cross-system entity lineage that satisfies these deployment-specific regulatory obligations. Regulatory scope and enforcement are jurisdiction- and sector-specific and evolve independently; the architectural point is that when explainability is required, cross-system entity lineage is what allows an audit to reconstruct which entities the AI-executed decision touched and how they related.
- **Comparative process mining reveals different optimisation targets.** For processes transitioning from human to agent execution, PxER captures both. Entity-enriched process mining enables direct comparison — agent-executed instances may complete faster but exhibit higher entity inconsistency rates at specific handoffs. This drives targeted improvement rather than blanket rollback, and is structurally distinct from both single-system process mining and AI observability tooling.

---

## 2. Use Cases

Entity correlation enables six categories of governance capability. These apply to processes spanning multiple systems AND to processes within a single application — the entity evidence gap exists wherever governed process steps touch entities whose relationships and state consistency are not captured by the execution record. Each use case below illustrates both contexts where relevant.

**Cross-system audit acceleration.** PxER links all steps in a process instance to correlated entity sets. Auditors query cross-system compliance relationships — e.g., "all termination instances where access revocation lagged more than 24 hours after HR action" — as native PxER operations rather than manual reconstruction. Within a single application, the same capability links entity references across modules — e.g., connecting the hiring action in an HR module to the cost centre assignment in a finance module, where the ERP transaction record captures both events but not the entity relationship between them.

**Data consistency detection.** The protocol captures entity key fields from each step's execution. Correlation enables detection that entity state diverges between steps for a specific process instance — proactive data integrity detection scoped to governed processes. This applies equally to cross-system divergence (SAP says Manager A, Workday says Manager B for the same person) and intra-system divergence (an HR module's org assignment is inconsistent with the finance module's cost allocation for the same employee within the same ERP).

**Undocumented business rule discovery.** Stable co-occurrence patterns across process instances reveal implicit business rules that exist in tribal knowledge but are not documented in any system configuration. These patterns feed the P→D promotion pipeline (APP-2 A8) as candidate deterministic rules. Within a single application, this surfaces rules that exist between modules — e.g., "cost centre CC:1234 always maps to benefit plan BP:UAE-GOLD" — that no integration flow governs because both modules are in the same system, yet the relationship is maintained manually.

**Post-execution entity flow verification.** Process Frame steps optionally reference the integration flow governing handoffs. Combined with entity references from both steps, post-execution checks verify whether entity state propagated correctly between specific steps in a specific instance. For intra-application processes, this verifies that module-to-module data propagation completed correctly — a gap that even single-vendor applications have when asynchronous batch jobs mediate between modules.

**Compliance-scoped entity lineage.** The C0–C4 compliance framework (APP-2 A5) gains entity-level evidence — linking compliance-relevant entities across steps within governed process instances without requiring compliance teams to manually reconstruct entity relationships. SOX compliance for expense approval, for example, requires tracing who approved, which cost centre, and which GL posting — whether those steps span systems or modules within one system.

**Process intelligence.** PxER timestamps combined with entity references enable process mining: cycle time decomposition, bottleneck identification, variant analysis, rework detection, conformance checking, and SLA tracking — scoped to governed process instances and enriched with entity context. These outputs feed APP-2 A11 (Process Intelligence). For cross-system processes, this provides intelligence structurally impossible for any single-system process mining tool. For intra-system processes, it provides entity-enriched intelligence that goes beyond what ERP event logs alone can deliver — because ERP logs capture step completion but not the entity relationships and state consistency that entity correlation reveals.

**Timing anomaly detection.** PxER captures step timestamps. Without entity correlation, sequence anomalies — a downstream step executing before the upstream step's entity state has propagated — are detectable but not attributable. With entity correlation and optional integration flow references (EC-29), timing analysis gains entity context: "Step 5 executed 2 minutes after Step 3, but the integration flow between them has a 15-minute SLA — the downstream step used stale entity data." This distinguishes integration-lag-attributable anomalies from process logic errors — a structurally distinct capability from global integration monitoring, which tracks sync health but not per-instance entity propagation timing.

---

## 3. Protocol Requirements

### 3.1 Entity Extraction Declaration (Process Frame Requirements)

**What:** An optional declaration on Process Frame steps specifying which fields from the step's execution response contain entity-identifying information.

**Why protocol:** Without a standardised declaration format, every implementation extracts different fields at different granularity. Entity references become non-comparable across implementations. The protocol standardises the declaration so any conformant implementation produces interoperable entity references in PxER.

**[Required Outcome · EC-01]** A conformant Process Frame step MAY include an `entity_extract` declaration. When present, it MUST specify per extracted entity: the response field path, an entity type label, and an entity role classification.

**[Required Outcome · EC-01a]** Changes to `entity_extract` declarations on Process Frame steps — including addition, removal, or modification of field paths, entity types, or entity roles — are Frame mutations subject to APP-3 SEC-S1-01 (signing) and SEC-S1-03 (monotonic versioning). Entity extraction configuration changes MUST trigger a Frame version increment.

**[Required Outcome · EC-02]** Entity role classifications MUST include at minimum: `primary_key` (the principal entity identifier for the step), `context_key` (an entity providing operational context), and `reference` (an entity referenced but not acted upon).

**[Recommended Pattern · EC-03]** Entity type labels SHOULD be drawn from a tenant-scoped registry. A recommended canonical vocabulary is provided as a starting point (see Appendix C) but is not enforced. Rationale: prevents label fragmentation within a tenant's process portfolio. Alternative: free-form labels per Process Frame — conformant but degrades downstream analytics comparability.

**[Recommended Pattern · EC-04]** At L2 (API/MCP), `entity_extract` declarations SHOULD be auto-generated from MCP tool return schemas. Rationale: MCP tool declarations include typed return schemas; a one-time mapping from return schema to `entity_extract` configuration eliminates manual per-step configuration. Alternative: manual configuration at L2 — conformant but does not scale.

**[Required Outcome · EC-05]** Entity extraction fidelity MUST follow integration maturity level:

| Level | entity_extract Mechanism | Expected Fidelity |
|:---|:---|:---|
| **L1** (Screen/RPA) | Optional. Manual configuration per step. | Low. Partial coverage. |
| **L2** (API/MCP) | Auto-generated from tool return schemas (EC-04). | Medium-High. Covers declared return fields. |
| **L3** (Application-Enhanced) | Application declares entity references via Telemetry Contribution Protocol. | High. Complete per-app. |
| **L4** (AI-Native) | Native entity semantics. `entity_extract` declaration MAY be omitted where the AI-native surface produces `entity_refs` automatically per EC-07; where present, `entity_extract` MUST be honoured. | Full. Automatic extraction. |

*(Clarified v2.2: L4's "no extraction needed" in prior wording was ambiguous. L4 surfaces produce entity references natively without requiring a per-step `entity_extract` declaration on the Process Frame, but the resulting `entity_refs` block in PxER remains mandatory per EC-07 whenever entity references are produced. An L4 surface that produces `entity_refs` without an `entity_extract` declaration is conformant; an L4 surface that omits `entity_refs` altogether is not.)*

**[Required Outcome · EC-06]** Absence of `entity_extract` on a Process Frame step MUST NOT prevent that step from participating in governed process execution. Core APP-2 capabilities (A0–A11) MUST function on individual steps without entity enrichment. This is a per-step obligation on core APP-2 execution — it does not relieve L2+ implementations of the requirement to support the entity correlation infrastructure (inferred mode EC-15, populated mode EC-19, registry EC-25, reconciliation EC-22); see §1.5(d) for the distinction between per-step extraction (optional) and correlation infrastructure (mandatory at L2+).

**Implementation choices.** How `entity_extract` declarations are authored — from MCP schemas, manual configuration, AI-assisted discovery, or templates — is an implementation concern. The canonical vocabulary contents beyond the recommended starting set are a deployment choice. Whether entity extraction is centralised or delegated per domain is an implementation concern.

> **Security.**
> **[Required Outcome · EC-38]** Access controls MUST prevent cross-tenant entity type leakage in entity extraction declarations.
> **[Required Outcome · EC-39]** Entity field paths in `entity_extract` declarations MUST NOT expose source system schema details beyond what is necessary for extraction.
> *(APP-3: Entity Extraction Security.)*

---

### 3.2 Entity References in PxER (Execution Record Requirements)

**What:** An optional block on PxER step records containing entity references extracted during execution, plus a process-instance-level entity correlation block linking entities across steps within the instance.

**Why protocol:** Without standardised entity references in PxER, entity data is scattered across source system responses and lost after step execution. The protocol standardises the reference format so entity-enriched PxER records are queryable and comparable across implementations.

**[Required Outcome · EC-07]** When a Process Frame step includes an `entity_extract` declaration (EC-01), the corresponding PxER step record MUST include an `entity_refs` block containing the extracted entity references.

**[Required Outcome · EC-08]** Each entity reference in `entity_refs` MUST include: entity type label, system-scoped entity key, and extraction method.

**[Recommended Pattern · EC-09]** Extraction method values SHOULD include at minimum: `mcp_response` (extracted from MCP tool response), `api_response` (extracted from REST/GraphQL/SOAP API response at L2), `telemetry` (contributed by L3 application), `bot_capture` (extracted from L1 bot output), and `constructed` (assembled by L4 platform). Rationale: extraction method provenance supports confidence assessment. Alternative: single undifferentiated method — conformant but reduces correlation quality assessment.

**[Recommended Pattern · EC-10]** Each entity reference SHOULD include a confidence indicator. Rationale: confidence varies by extraction method and integration maturity level. Downstream consumers (correlation, analytics, compliance) benefit from knowing reference reliability. Alternative: binary present/absent — conformant but prevents confidence-weighted correlation.

**[Required Outcome · EC-11]** PxER records MUST support an optional process-instance-level `entity_correlations` block linking entity references across steps within the instance. When present, each correlation MUST include: the correlated entity keys, the correlation mode (inferred, populated, or reconciled), and the evidence supporting the correlation.

**[Reference Mechanism · EC-36]** The v1 entity reference block structure per PxER step record:

| Field | Type | Required | Description |
|:---|:---|:---|:---|
| `entity_type` | string | Yes | Tenant-scoped entity type label (EC-12) |
| `system_key` | string | Yes | System-scoped entity identifier (e.g., "PERNR:00012345") |
| `extraction_method` | enum | Yes | How extracted: mcp_response, api_response, telemetry, bot_capture, constructed (EC-09) |
| `confidence` | enum | No | high, medium, low (EC-10) |
| `role` | enum | Yes | primary_key, context_key, reference (EC-02) |

Rationale: a standardised block structure is an interoperability surface — entity references must be parseable across implementations for cross-system correlation. Alternatives: implementations may use different field names or additional fields provided the Required Outcome fields (EC-08) are present and semantically equivalent.

**Implementation choices.** Entity reference storage architecture (relational, graph, document) is an implementation concern. How entity keys are normalised across systems is an implementation concern. Whether correlation is computed synchronously during PxER assembly or asynchronously in batch is an implementation concern.

> **Security.**
> **[Required Outcome · EC-40]** PxER entity data MUST inherit PxER access controls.
> **[Required Outcome · EC-41]** Cross-tenant entity correlation MUST be prohibited.
> **[Required Outcome · EC-42]** Entity references for steps with `trustBoundaryType: cross-enterprise-external` MUST be limited to what the governing implementation observes at its boundary.
> *(APP-3: Tenant Isolation, Evidence Integrity.)*

---

### 3.3 Entity Type Namespace

**What:** Scoping rules for entity type labels that prevent downstream confusion while avoiding a mandated global ontology.

**[Required Outcome · EC-12]** Entity type labels MUST be scoped to a tenant namespace. The protocol MUST NOT mandate a global entity type ontology.

**[Recommended Pattern · EC-13]** Tenants operating multiple process definitions SHOULD use consistent entity type labels for the same concepts across processes. A tenant-level entity type registry SHOULD provide the coordination mechanism. Rationale: label consistency across processes within a tenant enables cross-process correlation promotion (§3.5) and comparable analytics. Alternative: per-process entity type labels — conformant but limits cross-process intelligence.

**[Required Outcome · EC-14]** Entity type labels MUST be optional for inference-mode correlation (§3.4). The correlation mechanism MUST operate on co-occurrence of entity key values, not labels. Labels improve downstream usability but MUST NOT be prerequisites for inference.

**Key-namespace and matching rules.** To prevent identifier collision and privacy leakage in cross-system correlation:

- (a) **Tenant-scoped key namespace.** Every entity key value used for correlation MUST be qualified by a tenant-scoped namespace identifier. Raw key values MUST NOT be matched across tenants under any circumstance. Cross-tenant correlation is out of scope for this specification.
- (b) **No raw equal-value cross-system matching.** Within a tenant, correlation across systems MUST NOT be performed on raw equal-value matching of entity key values alone. Cross-system correlation MUST use one of: (i) a declared normalisation function (registered per source system, versioned, auditable) applied before matching; (ii) an evidence basis of at least the declared inferred-mode evidence threshold (EC-16, EC-17), where co-occurrence — not string equality — is the correlation signal; or (iii) a populated-mode correlation from a source authenticated per EC-43.
- (c) **PII entity keys.** Entity key values that constitute or contain personal data MUST inherit the tenant's PII handling controls (retention, access, erasure per SEC-S4-06). Raw PII values MUST NOT be used as inferred-mode correlation keys without either a documented lawful basis and access control, or a one-way transformation (hash with tenant-scoped salt) applied before storage in the correlation registry.

**Implementation choices.** The specific canonical vocabulary, how labels are managed, and whether type aliases are supported are implementation choices. Whether entity types are derived from MCP tool schemas, manually configured, or AI-assisted is an implementation choice.

---

### 3.4 Correlation Modes

**What:** Two complementary modes for establishing cross-system entity correlations, with a reconciliation mechanism when both are active.

**Why protocol:** Without standardised correlation modes, implementations cannot distinguish between runtime-discovered relationships (confidence builds with volume) and externally-sourced relationships (confidence from authoritative source). The distinction matters for governance — an inferred correlation with 3 instances of evidence carries different weight than an MDM-sourced correlation.

#### 3.4.1 Inferred Mode

**[Required Outcome · EC-15]** Conformant implementations MUST support inferred-mode entity correlation: discovering cross-system entity relationships from PxER entity reference co-occurrence patterns across process instances.

**[Required Outcome · EC-16]** Inferred correlations MUST carry: a confidence indicator, evidence count (number of process instances supporting the inference), first-observed and last-observed timestamps, and the process scope in which the correlation was discovered.

**[Required Outcome · EC-17]** Inferred correlations MUST start process-scoped — confined to the Process Frame where they were discovered. Promotion to global scope (reusable across processes for that tenant) MUST require the same entity correlation appearing across multiple Process Frames.

**Global-scope promotion governance.** Global-scope promotion is a tenant-level operational change that widens the surface across which a correlation applies. Every global promotion MUST record:

- (a) **Authoriser.** Named principal (authenticated human identity per APP-3 SEC-S13-02, or a governance-control identity per SEC-S6-04 where promotion is D-track automated against declared tenant policy) that authorised promotion. Anonymous or unattributed promotion is non-conformant.
- (b) **Evidence bundle.** Snapshot of the promotion evidence at authorisation time: which Process Frames the correlation appeared across, evidence counts per Process Frame, first-observed and last-observed timestamps per Process Frame, aggregate confidence.
- (c) **Reversal path.** A documented mechanism to withdraw global scope, restoring the correlation to process-scoped state. Withdrawal MUST record the withdrawing principal, the reason class (`erroneous`, `stale`, `security_concern`, `tenant_policy_change`, `other`), and the effective timestamp. Withdrawal MUST propagate to downstream consumers within the implementation-declared propagation SLA.
- (d) **Expiry.** Global-scope promotions MUST carry an expiry timestamp or a documented tenant-policy basis for permanence. Expired promotions revert to process-scoped state automatically unless renewed with a fresh evidence bundle and authoriser record.
- (e) **Audit trail.** All four fields (authoriser, evidence bundle, reversal events, expiry) MUST be queryable via the tenant's correlation registry for the applicable compliance retention period per SEC-S14-09.

Implementation choice: the specific promotion authorisation workflow (four-eyes review, automatic against declared policy, tenant-admin approval, or hybrid) is an implementation choice; the audit fields above are the interop surface.

**[Recommended Pattern · EC-18]** Confidence SHOULD increase monotonically with evidence count, subject to recency weighting and drift detection. Rationale: recent evidence is more relevant than historical evidence for evolving entity relationships. Alternative: unweighted evidence count — conformant but slower to detect stale correlations.

#### 3.4.2 Populated Mode

**[Required Outcome · EC-19]** Conformant implementations MUST support populated-mode entity correlation: importing entity correlation keys from external sources.

**[Required Outcome · EC-20]** Populated-mode imports MUST use a source-agnostic schema. The protocol does not prescribe which external sources are supported — MDM exports, integration suite mapping tables, data warehouse dimension tables, semantic layer platforms, or file imports are all conformant sources.

**[Required Outcome · EC-21]** Populated correlations MUST carry: source identifier, import timestamp, and populated confidence.

#### 3.4.3 Reconciliation

**[Required Outcome · EC-22]** When both inferred and populated correlations exist for the same entity pair, implementations MUST produce a reconciliation status with at minimum five outcomes:

| Status | Condition | Interpretation | Allowable enforcement |
|:---|:---|:---|:---|
| `aligned` | Inferred agrees with populated | High confidence. Both runtime evidence and external source confirm. | MAY be used for enforcement decisions (compliance gating, access decisions, execution blocking). |
| `divergent` | Inferred disagrees with populated | Anomaly: either stale external mapping or genuine integrity issue. | MUST surface as an operational signal (EC-23). MAY be used for enforcement only where deployment policy explicitly permits action on `divergent` and states the intended interpretation (stale-external vs integrity-issue). Otherwise advisory only. |
| `populated_only` | Populated exists, no inferred | Entity in external mapping but never co-occurs in process execution. | Advisory only unless deployment policy explicitly permits enforcement on this status. |
| `inferred_only` | Inferred exists, no populated | Undocumented entity relationship discovered from execution. | Advisory only unless deployment policy explicitly permits enforcement. Discovery-signal treatment recommended (EC-24). |
| `error` | Reconciliation could not complete | Populated source unavailable, corrupt data, or timeout. MUST carry a reason code. MUST revert to last known status with a staleness timestamp. | **Stale reconciliation state is advisory only and MUST NOT be used for enforcement (compliance gating, access decisions, execution blocking) unless the deployment policy explicitly permits it for the specific enforcement class, and the reliance on stale state is recorded in PxER or the correlation registry as evidence. Absent explicit deployment-policy permission, systems consuming a `error`-status correlation MUST fall back to their non-correlation-dependent decision path.** A default fail-closed interpretation of `error` (blocking execution absent policy) is non-conformant. |

**Enforcement-consequence rule.** For every status, the default MUST be advisory-only unless the deployment policy explicitly permits enforcement for that status class. This prevents implementations from defaulting to either fail-open (ignoring `divergent` risk signals) or fail-closed (blocking on `error` without policy). The deployment policy's enforcement declarations for each status MUST be recorded in the implementation's conformance profile.

**[Required Outcome · EC-23]** The `divergent` status MUST be surfaced as an operational signal. Both interpretations — stale external mapping and genuine integrity issue — are operationally valuable.

**[Recommended Pattern · EC-24]** The `inferred_only` status SHOULD be surfaced as a discovery signal — undocumented cross-system relationships that no external source has documented. These are candidates for the P→D promotion pipeline (APP-2 A8) when stable. Rationale: the highest-value correlations are often those nobody knew existed. Alternative: treat `inferred_only` the same as other statuses — conformant but misses the discovery opportunity.

**Implementation choices.** Inference algorithms, confidence scoring models, co-occurrence detection methods, and reconciliation logic are implementation choices. Whether reconciliation runs in real-time or batch is an implementation choice. Correlation storage architecture (dedicated registry, integrated into PxER store, or external) is an implementation choice.

> **Security.**
> **[Required Outcome · EC-43]** Populated-mode imports MUST authenticate source systems.
> **[Required Outcome · EC-44]** Correlation data MUST inherit tenant isolation controls.
> **[Required Outcome · EC-45]** Reconciliation signals (especially `divergent`) MUST be access-controlled — they may reveal integration failures with security implications.
> *(APP-3: Tenant Isolation, Entity Correlation Security.)*

---

### 3.5 Entity Correlation Registry

**What:** A persistent store of entity correlations — both inferred and populated — that is queryable across process instances.

**Why protocol:** Without a durable correlation store, each process instance re-discovers entity relationships from scratch. Cross-process queries ("show all processes affecting this entity") require re-inference. The registry enables entity-scoped governance queries and cross-process correlation reuse.

**[Required Outcome · EC-25]** Conformant implementations MUST maintain an entity correlation registry that persists correlations across process instances.

**[Required Outcome · EC-26]** Registry entries MUST include: correlation identifier, entity type, correlated system keys, correlation mode (inferred/populated/reconciled), confidence, evidence count, scope (process-scoped or global), and timestamps (first-observed, last-observed).

**[Reference Mechanism · EC-37]** The v1 registry entry structure:

| Field | Type | Required | Description |
|:---|:---|:---|:---|
| `correlation_id` | string | Yes | Unique identifier |
| `entity_type` | string | Yes | Tenant-scoped entity type label |
| `keys` | array | Yes | Correlated system keys (system + key per entry) |
| `mode` | enum | Yes | inferred, populated, reconciled |
| `confidence` | decimal | Yes | 0.0–1.0 |
| `evidence_count` | integer | Yes | Process instances supporting inference |
| `scope` | enum | Yes | process-scoped (+ frame_id) or global |
| `first_observed` | timestamp | Yes | First evidence |
| `last_observed` | timestamp | Yes | Most recent evidence |
| `populated_source` | string | No | Source identifier when mode = populated or reconciled |
| `reconciliation_status` | enum | No | aligned, divergent, populated_only, inferred_only, error (when both modes active; per EC-22) |

Rationale: a standardised registry entry structure enables portable entity correlation data and cross-implementation registry queries. Alternatives: implementations may use different field names or additional fields provided the Required Outcome fields (EC-26) are present and semantically equivalent.

**[Recommended Pattern · EC-27]** The registry SHOULD support correlation drift detection — identifying when previously stable correlations begin diverging, as a signal for either entity lifecycle changes or integration failures. Rationale: correlations are not static; entity relationships evolve as organisations restructure, employees transfer, and systems change. Alternative: static registry without drift detection — conformant but stale correlations degrade governance quality over time.

**[Recommended Pattern · EC-28]** High-confidence global correlations SHOULD be materialised into a lookup index for PxER assembly-time enrichment. Rationale: the full registry is not designed for real-time query loads; a materialised lookup supports assembly-time correlation without registry query overhead. Alternative: direct registry query during PxER assembly — conformant for low-volume deployments.

**Implementation choices.** Registry storage technology, compaction/garbage-collection policies, materialisation strategy, and query interface are implementation choices. Whether the registry is a dedicated artifact or integrated into existing entity stores is an implementation choice.

> **Security.**
> **[Required Outcome · EC-46]** Registry access MUST respect tenant isolation. Cross-tenant queries MUST be prohibited.
> **[Required Outcome · EC-47]** Registry entries for cross-enterprise entity references MUST be limited to boundary-observable data.
> *(APP-3: Tenant Isolation.)*

---

### 3.6 Entity Flow Verification

**What:** Post-execution verification that entity state propagated correctly between cross-system process steps.

**Why protocol:** PxER confirms that steps completed. Entity correlation confirms which entities were involved. Neither confirms that the entity state in System B reflects the outcome of the step in System A. Entity flow verification closes this gap — detecting that cross-system entity propagation actually occurred for each process instance.

**[Recommended Pattern · EC-29]** Process Frame steps involved in cross-system entity handoffs SHOULD optionally reference the integration flow governing the handoff. Rationale: integration flow references enable attribution of entity propagation failures to specific integration paths, including per-instance integration lag detection and SLA attribution — a structurally distinct capability from global integration monitoring. Alternative: entity flow verification without integration flow references — conformant but loses the ability to detect integration-lag-attributable entity propagation failures per process instance, relying instead on global integration health monitoring which cannot scope to individual governed process instances.

> *Classification note: the internal architecture design (0112 Annex B §5.3) classifies integration flow references as an Architectural Commitment. This protocol classifies them as [Recommended Pattern] because the open protocol cannot mandate how implementations reference integration flows — the interoperability surface is the entity flow verification outcome (EC-30), not the specific reference mechanism. The working group should be aware of this deliberate reclassification.*

**[Recommended Pattern · EC-30]** Post-execution entity flow verification SHOULD compare entity key field values across correlated steps to detect propagation failures. Rationale: entity references from adjacent steps in the same process instance, combined with correlation registry data, provide the inputs for instance-scoped consistency checking. Alternative: no post-execution verification — conformant but relies on external integration monitoring for propagation assurance.

**Implementation choices.** Verification algorithms, timing (synchronous vs. asynchronous), SLA definitions for propagation latency, and alerting thresholds are implementation choices. Whether verification invokes source system APIs to confirm current entity state or relies solely on PxER-captured data is an implementation concern.

---

### 3.7 Connection to Learning Capabilities (A8–A11)

Entity correlation produces signals that feed multiple APP-2 lifecycle capabilities.

**[Required Outcome · EC-31]** Stable inferred entity correlations MUST be representable as P→D promotion candidates (APP-2 A8). When a cross-system entity pattern is consistently stable across a sufficient evidence window, it is a candidate deterministic rule.

**[Required Outcome · EC-32]** Entity correlation drift (EC-27) MUST be representable as a drift signal type within APP-2 A10 (Drift Detection). Entity-level drift — previously stable correlations diverging — is a governance signal distinct from process-level and orchestration-quality drift.

**[Recommended Pattern · EC-33]** Entity-enriched PxER data SHOULD feed APP-2 A11 (Process Intelligence) outputs: entity-scoped bottleneck identification, entity flow variant analysis, cross-system SLA tracking per entity type, and rework detection attributable to specific entity handoff failures. Rationale: entity context transforms process intelligence from structural (step-level) to actionable (entity-level). Alternative: process intelligence without entity enrichment — conformant with APP-2 but misses the entity dimension.

**Implementation choices.** How promotion candidates are surfaced from entity patterns (algorithm, scoring, threshold) is an implementation choice. How entity drift signals are delivered to A10 consumers (push vs. pull, frequency, format) is an implementation choice. How entity-enriched intelligence outputs are structured for A11 consumers (report schema, query interface, real-time vs. batch computation) is an implementation choice.

---

## 4. Applicability

### 4.1 Design Driver

The entity correlation architecture's design driver is governed process enrichment. The protocol's interoperability mandate (APP-1 invariant c) means every normative requirement works across vendor boundaries. But the entity evidence gap — entities flowing through governed process steps without being captured, correlated, or verified — exists wherever governed processes touch entities with relationships that are not already fully recorded. This includes cross-vendor processes (the primary design target), cross-module processes within a single application, and any governed process where AI-mediated decisions affect entity state.

### 4.2 Applicability Within a Single Application

The entity correlation architecture is applicable within a single application wherever governed AI execution touches multiple entity domains that are independently managed within that application.

| Capability | Applicable Intra-App? | What It Adds |
|:---|:---|:---|
| Entity extraction (EC-01) | Full | Standardised entity reference capture regardless of process scope |
| Entity references in PxER (EC-07) | Full | Entity-enriched execution records for intra-app governance |
| Correlation modes (EC-15, EC-19) | Partial | Inferred mode applicable where intra-app modules have independent entity representations; populated mode applicable where intra-app master data provides correlation keys |
| Entity flow verification (EC-29) | Partial | Applicable where intra-app modules hand off entity state through asynchronous mechanisms |
| Learning connections (EC-31–33) | Full | Entity-enriched drift detection and process intelligence apply regardless of process scope |

**Full** = fully applicable. **Partial** = applicable but scope narrower intra-app.

Many enterprise applications — ERP platforms especially — have independently managed entity representations across modules (HR, Finance, Procurement). Entity correlation adds governance value wherever entity state must be consistent across module boundaries, regardless of whether those boundaries cross vendor lines.

The protocol does not replace intra-application entity management. L3 conformance enables intra-application entity correlation participation through the Telemetry Contribution Protocol. Intra-application entity correlation is not required for conformance but is the expected consequence of L3/L4 progression.

### 4.3 Cross-Application Applicability

Cross-application entity correlation is the primary design target. Six characteristics make cross-application processes the highest-value target for entity correlation:

- **Independent entity representations.** Each system maintains its own identifiers, schemas, and lifecycle rules for the same real-world entities.
- **No shared entity authority.** Unlike intra-app modules that may share a common master, cross-application entities have no single source of truth unless MDM exists.
- **Integration-mediated handoffs.** Entity state propagates through integration flows with latency, transformation, and potential failure — none of which are visible to individual applications.
- **Regulatory accountability spans systems.** Compliance obligations (SOX, EU AI Act) require entity-level traceability across the full process — not just within individual applications.
- **Agent-mediated execution amplifies the gap.** AI agents executing cross-system processes (§1.6) need entity consistency verification that no single system can provide.
- **Process mining requires entity context.** Cross-system process mining (APP-2 A11) without entity correlation produces structural analysis only. Entity correlation makes it actionable.

The protocol's entity correlation requirements are designed to be valuable in both contexts, with cross-application processes delivering the highest marginal governance improvement.

### 4.4 Maturity Level Behaviour

| Level | Entity Extraction | Correlation Capability | Value Delivered |
|:---|:---|:---|:---|
| **L1** (Screen/RPA) | Manual configuration. Partial coverage. | Inference from sparse data — slow convergence. | Basic cross-system entity traceability for primary entities. |
| **L2** (API/MCP) | Auto-generated from MCP tool schemas. Good coverage. | Inference converges faster from richer entity data per step. | Cross-system entity correlation, data consistency detection, timing anomaly attribution. |
| **L3** (App-Enhanced) | Application declares entity references via telemetry. Rich typing. | High confidence from first instance. | Full entity-aware governance. Post-execution consistency verification. Compliance-scoped entity lineage. |
| **L4** (AI-Native) | Built-in. Entity semantics are first-class. | Entity correlation is a platform primitive. | All of the above by construction. |

Populated-mode entity correlation (EC-19) is orthogonal to integration maturity level — it depends on the customer's semantic infrastructure maturity, not the application's integration depth.

---

## 5. Graceful Degradation

**[Required Outcome · EC-34]** If entity extraction fails for a step, PxER step records MUST still be produced without entity references. Entity extraction failure MUST NOT block PxER assembly or governed process execution.

**[Required Outcome · EC-35]** If the correlation engine is unavailable, PxER records MUST still contain per-step entity references (when extraction succeeds). Instance-level correlation MUST be flagged for retrospective reconciliation.

**Implementation choices.** Retry cadence for retrospective correlation when the engine returns, alerting thresholds for extraction failures, and duration thresholds before degraded-mode PxER records trigger governance escalation are implementation choices.

---

## Appendix A — Entity Correlation Detail by Integration Level

| Cap. | L1 (Screen/RPA) | L2 (API/MCP) | L3 (App-Enhanced) | L4 (AI-Native) |
|:---|:---|:---|:---|:---|
| **Entity extraction** | Manual. 1–2 key entities per critical step. | Auto from MCP schemas. All declared return fields. | App declares rich typed refs. | Built-in. First-class. |
| **PxER entity refs** | Partial. Primary keys only. | Good. Typed extraction. | Complete. Full semantic. | Full. By construction. |
| **Inferred correlation** | Slow convergence. High volume needed. | Moderate convergence. | Fast. High confidence early. | Primitive. Instant. |
| **Populated correlation** | File import if available. | File/API import. | + app-contributed refs. | + platform semantics. |
| **Reconciliation** | Limited value (sparse inference). | Core operating mode. | Full value. | Full by construction. |
| **Entity flow verification** | Not supported (no integration refs). | Post-execution checks on entity keys. | + app-reported propagation. | Verified by construction. |
| **Process intelligence** | Entity-limited. | Entity-enriched, cross-system. | Full entity-enriched. | Full. Native. |

---

## Appendix B — Security Cross-Reference

The authoritative mapping between APP-4 entity correlation requirements and APP-3 security domains is maintained in **APP-IG-02 (Cross-Reference Matrix), §2**. Each normative section in this document includes an inline security callout with numbered EC requirements (EC-38 through EC-47); APP-IG-02 provides the complete cross-document mapping.

APP-3 incorporates entity-correlation-specific security requirements as S14 (Entity Correlation Security), with SEC-S14-01 through SEC-S14-09. Two reciprocal tables below make the bilateral cross-reference explicit per APP-1 §4 (v2.3 addition).

### B.1 S14 → EC forward mapping

| APP-3 SEC ID | APP-4 Requirements | Summary |
|:---|:---|:---|
| SEC-S14-01 | EC-38 | Cross-tenant entity type leakage prevention |
| SEC-S14-02 | EC-39 | Entity field path exposure minimisation |
| SEC-S14-03 | EC-40 | Entity data inherits PxER access controls and hash chain integrity |
| SEC-S14-04 | EC-41, EC-44 | Cross-tenant correlation prohibited; correlation data tenant-isolated |
| SEC-S14-05 | EC-42 | Cross-enterprise entity references limited to boundary-observable data |
| SEC-S14-06 | EC-43 | External correlation sources MUST authenticate |
| SEC-S14-07 | EC-44, EC-45 | Correlation data tenant isolation + reconciliation signal access control (SEC-S14-07 aggregates two EC obligations) |
| SEC-S14-08 | EC-46 | Correlation registry tenant isolation + cross-enterprise boundary limits |
| SEC-S14-09 | EC-47 | Declared retention per compliance scope |

### B.2 EC → S14 reciprocal mapping

Each EC requirement states the S14 controls that apply to it, satisfying the bilateral cross-reference rule. The reciprocal table:

| APP-4 EC ID | All applicable APP-3 SEC-S14 controls | Relationship |
|:---|:---|:---|
| EC-38 | SEC-S14-01 | 1:1 |
| EC-39 | SEC-S14-02 | 1:1 |
| EC-40 | SEC-S14-03 | 1:1 |
| EC-41 | SEC-S14-04 | 1:1 |
| EC-42 | SEC-S14-05 | 1:1 |
| EC-43 | SEC-S14-06 | 1:1 |
| EC-44 | SEC-S14-04, SEC-S14-07 | many-to-one (EC-44 addresses both cross-tenant prohibition AND correlation-data isolation) |
| EC-45 | SEC-S14-07 | 1:1 primary; SEC-S14-03 also relevant for access-control inheritance |
| EC-46 | SEC-S14-08 | 1:1 primary; SEC-S14-04 and SEC-S14-05 also apply for cross-tenant and cross-enterprise aspects |
| EC-47 | SEC-S14-09 | 1:1 |

**Interpretation rule.** Where an EC ID's row lists multiple SEC-S14 controls, the implementation MUST satisfy all listed controls. Where a SEC-S14 ID's row (§B.1) lists multiple EC requirements, the SEC-S14 requirement aggregates those EC obligations and implementations of the SEC-S14 control MUST address all listed EC obligations. The two tables are equivalent semantically and MUST remain consistent; discrepancies between them are release-control defects.

**Bilateral cross-reference rule.** Changes to any row in either table require concurrent update in both, in APP-3 SEC-S14 body, and in APP-IG-02 §2, per the APP-1 §4 change-impact manifest.

---

## Appendix C — Recommended Canonical Entity Type Vocabulary

This vocabulary provides a recommended starting set of entity type labels for use in `entity_extract` declarations (EC-01) and `entity_refs` blocks (EC-07). It is **informative, not normative** — tenants MAY extend, rename, or replace this vocabulary entirely.

**Relationship to implementation entity models.** This vocabulary defines protocol-level semantic labels for entity references in PxER. It is independent of any implementation's internal entity schema — whether an implementation uses a canonical entity model, a federated model, or no formal entity model at all. Implementations that maintain their own entity schemas (e.g., shared core entity models, knowledge graphs, or MDM systems) will have their own entity definitions with richer property sets and governance rules. This vocabulary serves a narrower purpose: providing comparable entity type labels across implementations for interoperable entity correlation.

**No minimum entity set required.** The protocol does not mandate a minimum set of entity types for conformance. EC-06 establishes that core APP-2 capabilities MUST function without entity enrichment. Entity extraction is valuable in proportion to process governance needs — a deployment governing only procurement processes may use `vendor`, `contract`, and `transaction` and never reference `person`. The vocabulary is a coordination aid, not a conformance gate.

| Entity Type | Description | Common Systems |
|:---|:---|:---|
| `person` | Individual (employee, contractor, applicant) | HR, Identity, Payroll |
| `org_unit` | Organisational unit, department, team | HR, Finance, IT |
| `cost_centre` | Cost allocation unit | Finance, HR, Procurement |
| `location` | Physical or virtual address / site | HR, Facilities, Procurement |
| `asset` | Physical or digital asset | IT, Facilities, Finance |
| `contract` | Legal agreement | Procurement, Legal, HR |
| `transaction` | Financial transaction | Finance, Procurement |
| `vendor` | External supplier | Procurement, Finance |
| `customer` | External customer | CRM, Finance |
| `project` | Project or programme | PM, Finance, HR |
| `account` | Financial account | Finance |
| `calendar_period` | Fiscal, calendar, or custom time period | Finance, HR, Compliance |

---

## Appendix D — Master Requirement Index

| ID | Section | Level | Short Description | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| EC-01 | §3.1 | RO | entity_extract declaration format | ● | ● | ● | ● |
| EC-01a | §3.1 | RO | entity_extract changes are Frame mutations (S1-01, S1-03) | ● | ● | ● | ● |
| EC-02 | §3.1 | RO | Entity role classifications | ● | ● | ● | ● |
| EC-03 | §3.1 | RP | Tenant-scoped entity type registry | | ● | ● | ● |
| EC-04 | §3.1 | RP | Auto-generation from MCP schemas | | ● | ● | |
| EC-05 | §3.1 | RO | Fidelity by maturity level | ● | ● | ● | ● |
| EC-06 | §3.1 | RO | No-gate: core APP-2 without entity enrichment | ● | ● | ● | ● |
| EC-07 | §3.2 | RO | entity_refs in PxER when entity_extract present | ● | ● | ● | ● |
| EC-08 | §3.2 | RO | entity_ref minimum fields | ● | ● | ● | ● |
| EC-09 | §3.2 | RP | Extraction method values | ● | ● | ● | ● |
| EC-10 | §3.2 | RP | Confidence indicator per reference | | ● | ● | ● |
| EC-11 | §3.2 | RO | Instance-level entity_correlations block | ● | ● | ● | ● |
| EC-12 | §3.3 | RO | Tenant-scoped entity type labels | ● | ● | ● | ● |
| EC-13 | §3.3 | RP | Cross-process label consistency | | ● | ● | ● |
| EC-14 | §3.3 | RO | Labels optional for inference | ● | ● | ● | ● |
| EC-15 | §3.4.1 | RO | Inferred-mode correlation support | | ● | ● | ● |
| EC-16 | §3.4.1 | RO | Inferred correlation minimum fields | | ● | ● | ● |
| EC-17 | §3.4.1 | RO | Process-scoped → global promotion | | ● | ● | ● |
| EC-18 | §3.4.1 | RP | Recency-weighted confidence | | ● | ● | ● |
| EC-19 | §3.4.2 | RO | Populated-mode correlation support | | ● | ● | ● |
| EC-20 | §3.4.2 | RO | Source-agnostic import schema | | ● | ● | ● |
| EC-21 | §3.4.2 | RO | Populated correlation minimum fields | | ● | ● | ● |
| EC-22 | §3.4.3 | RO | Reconciliation five-outcome status | | ● | ● | ● |
| EC-23 | §3.4.3 | RO | Divergent status as operational signal | | ● | ● | ● |
| EC-24 | §3.4.3 | RP | Inferred_only as discovery signal | | ● | ● | ● |
| EC-25 | §3.5 | RO | Persistent entity correlation registry | | ● | ● | ● |
| EC-26 | §3.5 | RO | Registry entry minimum fields | | ● | ● | ● |
| EC-27 | §3.5 | RP | Correlation drift detection | | ● | ● | ● |
| EC-28 | §3.5 | RP | Materialised lookup index | | ● | ● | ● |
| EC-29 | §3.6 | RP | Integration flow references on Frame steps | | ● | ● | ● |
| EC-30 | §3.6 | RP | Post-execution entity flow verification | | ● | ● | ● |
| EC-31 | §3.7 | RO | Stable correlations as P→D candidates | | ● | ● | ● |
| EC-32 | §3.7 | RO | Correlation drift as A10 signal type | | ● | ● | ● |
| EC-33 | §3.7 | RP | Entity-enriched process intelligence | | ● | ● | ● |
| EC-34 | §5 | RO | Graceful degradation: extraction failure | ● | ● | ● | ● |
| EC-35 | §5 | RO | Graceful degradation: correlation unavailable | ● | ● | ● | ● |
| EC-36 | §3.2 | RM | Entity reference block structure (v1) | ● | ● | ● | ● |
| EC-37 | §3.5 | RM | Registry entry structure (v1) | | ● | ● | ● |
| EC-38 | §3.1 | RO | Cross-tenant entity type leakage prevention | ● | ● | ● | ● |
| EC-39 | §3.1 | RO | Entity field path exposure minimisation | ● | ● | ● | ● |
| EC-40 | §3.2 | RO | Entity data inherits PxER access controls | ● | ● | ● | ● |
| EC-41 | §3.2 | RO | Cross-tenant entity correlation prohibited | ● | ● | ● | ● |
| EC-42 | §3.2 | RO | Cross-enterprise entity refs: boundary-observable only | | ● | ● | ● |
| EC-43 | §3.4.3 | RO | Populated source authentication | | ● | ● | ● |
| EC-44 | §3.4.3 | RO | Correlation data tenant isolation | | ● | ● | ● |
| EC-45 | §3.4.3 | RO | Reconciliation signal access control | | ● | ● | ● |
| EC-46 | §3.5 | RO | Registry tenant isolation | | ● | ● | ● |
| EC-47 | §3.5 | RO | Registry cross-enterprise: boundary-observable only | | ● | ● | ● |

**Key:** RO = Required Outcome · RP = Recommended Pattern · RM = Reference Mechanism

**L-level applicability (●):** For RO rows, ● means the requirement is mandatory for conformant implementations at that level. For RP rows, ● means the recommendation is relevant and deviation requires documented justification. For RM rows, applicability is informative — the mechanism is a working group starting point. Empty cells indicate the requirement does not apply at that level.

**Note:** L1 supports entity extraction (EC-01, EC-07), security (EC-38–41), and graceful degradation (EC-34, EC-35) but does not support correlation inference (EC-15–EC-28) due to insufficient integration depth. L1 entity references are captured in PxER for downstream analysis but correlation is computed from L2+ data.

**Known Open Issues** (gap reports pending — not yet protocol requirements):

- *Correlation semantics for long-running A2A tasks.* Multi-turn A2A tasks with delayed completions need richer correlation beyond single-request spans. Gap report pending.
- *Cross-enterprise entity correlation.* For steps with `trustBoundaryType: cross-enterprise-external`, entity correlation is limited to boundary-observable data. A future protocol extension could define a negotiated entity reference exchange for B2B governed processes. Gap report pending.
- *Sampling provenance for nested entity extraction.* When an external system performs recursive agentic work, entity references may be extracted from intermediate rather than final results. Gap report pending.

---

## Appendix E — Protocol Boundary: What Is NOT a Protocol Capability

**Protocol-Enabled Capabilities** — implementations choose freely:

| Topic | Why Not Protocol |
|:---|:---|
| Correlation inference algorithms | Protocol requires inferred mode (EC-15); detection method is differentiator |
| Reconciliation engine logic | Protocol requires five-outcome reconciliation (EC-22); algorithm is free |
| Registry storage technology | Protocol requires persistence (EC-25); technology is free |
| Process mining algorithms | Protocol defines intelligence outputs (APP-2 A11); computation is free |
| Confidence scoring models | Protocol requires confidence indicator (EC-10); model is free |

**Other implementation concerns** — well-established standards or per-platform choices:

| Topic | Why Not Protocol |
|:---|:---|
| MDM integration adapters | Protocol defines source-agnostic import (EC-20); adapters are per-source |
| Semantic layer connectors (OSI, vendor-specific) | Protocol consumes correlation keys; connector technology is free |
| Entity type vocabulary management UI | Protocol defines namespace (EC-12); tooling is free |
| Correlation visualisation | Protocol defines queryable registry (EC-25); presentation is free |
| Graph vs. relational storage | Protocol defines required fields (EC-26); storage architecture is free |

---

## Appendix F — Glossary

| Term | Definition |
|:---|:---|
| **entity_extract** | Process Frame per-step declaration of which response fields contain entity-identifying information |
| **entity_refs** | PxER per-step block containing extracted entity references |
| **entity_correlations** | PxER per-instance block linking entity references across steps and systems |
| **Entity Correlation Registry** | Persistent store of entity correlations across process instances |
| **Inferred correlation** | Entity relationship discovered from PxER co-occurrence patterns. Confidence builds with volume. |
| **Populated correlation** | Entity relationship imported from external source (MDM, integration suite, data lake, semantic layer). |
| **Reconciled correlation** | Entity relationship where both inferred and populated modes are active and reconciliation status is determined. |
| **Entity role** | Classification of an entity reference: primary_key, context_key, or reference. |
| **Entity type** | Tenant-scoped label classifying the business concept an entity represents (person, org_unit, cost_centre, etc.). |
| **Correlation drift** | Detection that previously stable entity correlations are diverging — signal for entity lifecycle changes or integration failures. |
| **Entity flow verification** | Post-execution check that entity state propagated correctly between cross-system process steps. |
| **Process-scoped correlation** | Correlation confined to the Process Frame where it was discovered. |
| **Global correlation** | Correlation promoted from process-scoped to reusable across any process for the tenant. |

## Appendix G — Requirement Rationale Digest

This appendix provides plain-language rationale for each requirement group — explaining *why* specific fields and capabilities are required, not just *what* they are. This is intended for implementors, enterprise architects, and working group members evaluating requirements during deliberation.

| Requirement Group | Requirements | Why These Specific Fields / Capabilities |
|:---|:---|:---|
| **Entity extraction declaration** | EC-01, EC-02, EC-05, EC-06 | Without declaring which response fields contain entity-identifying information, entity references are lost after step execution. The entity type label and role classification (primary_key, context_key, reference) enable downstream consumers to distinguish the principal entity a step acts upon from contextual entities referenced in passing — a distinction that matters for correlation confidence, audit scoping, and compliance lineage. L-level fidelity (EC-05) ensures the protocol does not mandate capabilities that lower integration levels cannot support. The no-gate requirement (EC-06) prevents entity correlation from becoming a deployment prerequisite that blocks core governance value. |
| **Entity references in PxER** | EC-07, EC-08, EC-09, EC-10, EC-11 | Entity references must be in PxER — not in source system logs — because PxER is the governed execution record that auditors and compliance teams query. Extraction method provenance (EC-09) enables confidence assessment: an entity reference extracted from a typed MCP response carries higher confidence than one parsed from bot screen output. Confidence indicators (EC-10) propagate this distinction to downstream correlation. The instance-level correlation block (EC-11) links entity references across steps within a single process execution — the atomic unit of governed process audit. |
| **Entity type namespace** | EC-12, EC-13, EC-14 | Tenant-scoped namespaces (EC-12) prevent entity type label collisions across tenants while avoiding a mandated global ontology that would be politically infeasible in a multi-vendor protocol. Cross-process consistency (EC-13) enables the highest-value analytics: querying all processes affecting a specific entity type across a tenant's process portfolio. Labels being optional for inference (EC-14) ensures that inference-mode correlation works even when entity types are not yet configured — preserving the inference-first principle. |
| **Correlation modes** | EC-15–EC-24 | Two modes exist because enterprise customers have radically different semantic infrastructure maturity. Inference mode (EC-15) delivers value with zero external dependencies — the protocol discovers entity relationships from execution data alone. Populated mode (EC-19) accelerates and validates inference where customers have MDM, integration suites, or data lakes. The five reconciliation outcomes (EC-22) are not arbitrary — each has distinct operational value: `aligned` confirms high confidence, `divergent` surfaces anomalies, `populated_only` identifies dead mappings, `inferred_only` discovers undocumented business rules, and `error` captures operational failures (source unavailable, corrupt data, timeout) that would otherwise leave reconciliation status undefined. |
| **Entity correlation registry** | EC-25–EC-28 | Without persistence, each process instance re-discovers entity relationships from scratch — losing the compounding value of correlation confidence that builds across instances. The registry fields (EC-26) are the minimum needed to answer the governance questions: which entities are correlated, how confident are we, where was this discovered, and is it still valid? Drift detection (EC-27) matters because entity relationships are not static — organisational restructures, system migrations, and business changes alter correlations. |
| **Entity flow verification** | EC-29, EC-30 | PxER confirms steps completed. Entity correlation confirms which entities were involved. Neither confirms that entity state actually propagated between steps. Integration flow references (EC-29) and post-execution verification (EC-30) close this gap — detecting that the Workday pay group matches what the SAP org assignment predicts, for a specific process instance, for a specific employee. |
| **Learning connections** | EC-31–EC-33 | Entity correlation data feeds APP-2's learning loop. Stable entity patterns are promotion candidates (EC-31) — converting implicit business rules into explicit deterministic rules. Entity drift is a governance signal (EC-32) distinct from process-level drift. Entity-enriched intelligence (EC-33) transforms process mining from structural (step-level) to actionable (entity-level). |
| **Graceful degradation** | EC-34, EC-35 | Entity correlation must never block business execution. Extraction failures produce PxER records without entity data — degraded but functional. Correlation engine unavailability produces PxER records with per-step entity references but without instance-level correlation — retrospective reconciliation is possible. |
| **Security** | EC-38–EC-47 | Entity references contain business-critical identifiers (employee IDs, cost centres, vendor numbers). Cross-tenant leakage (EC-38, EC-41, EC-44, EC-46) is prevented because entity correlation data is as sensitive as PxER governance data — a correlation revealing which employee maps to which vendor number across systems is a confidentiality-critical record. Cross-enterprise boundary limits (EC-42, EC-47) enforce honest evidence: entity references beyond the governing implementation's observation boundary are unknowable and must not be fabricated. Populated source authentication (EC-43) prevents poisoned correlation imports from corrupting the registry. Reconciliation signal access control (EC-45) matters because `divergent` signals may reveal integration failures with security implications. |
| **Reference Mechanisms** | EC-36, EC-37 | The entity reference block structure (EC-36) and registry entry structure (EC-37) are interoperability surfaces — entity references and correlations must be parseable across implementations for cross-system governance. These are v1 proposals for working group deliberation; alternatives using different field names or additional fields are conformant provided Required Outcome fields are semantically equivalent. |

> *Note: This appendix is informative. The normative requirements are in §3. A more detailed rationale document with worked examples will be provided in the APP-IG series (Implementation Guides).*

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 2.3
**Normative status:** Normative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-4 — Entity Correlation Architecture.*
