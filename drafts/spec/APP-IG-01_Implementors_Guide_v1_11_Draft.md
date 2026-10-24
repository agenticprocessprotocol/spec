# APP-IG-01

Agentic Process Protocol

## Implementor's Guide — ERP Vendor & Platform Adoption

| | |
|:---|:---|
| **Version** | 1.11 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Audience** | ERP vendor architecture teams, hyperscaler platform teams, system integrators, enterprise CTOs, ISV technical leads |
| **Normative status** | This document is **informative**. It does not define requirements. It helps implementors understand what the protocol asks without reading the full specification. |
| **Companion documents** | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles), APP-IG-02 (Cross-Reference Matrix), APP-R1 (Frame Schema), APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) — v1.11 adds §1.4 introducing the APP-R Illustrative Reference tier and names the two current reference artefacts (APP-R1, APP-R2). |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |
| **Version-reference convention** | Companion documents cited by name only in body prose. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-IG-01 is an informative implementation guide for the Agentic Process Protocol. It provides orientation for teams building conformant implementations.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. This document does not create, modify, or override normative requirements in APP-0 through APP-5.
>
> **Use this document for:** Implementation orientation, role scope guidance, adoption patterns, access-posture taxonomy for procurement selection.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** APP-2 (primary normative reference), APP-5 (conformance profiles), APP-IG-03 (worked example).

---

## How to Read This Document

This document is an Implementation Guide — one of the specification types defined in APP-1. It contains no normative requirements. Where it references protocol requirements, it uses the requirement IDs defined in APP-2 (`CORE-*`), APP-3 (`SEC-*`), and APP-4 (`EC-*`). The authoritative definition of each requirement lives in the originating specification.

The document is organised for role-based reading:

| If you are... | Start with... |
|:---|:---|
| An ERP vendor architect evaluating conformance | §4 (What Conformance Means), §6.1 (ERP Vendor FAQ) |
| A hyperscaler platform team | §5.2 (What Each Stakeholder Keeps vs Gains), §6.2 (Hyperscaler FAQ) |
| An agent builder platform (LangGraph, Copilot Studio, Agents SDK) | §6.5 (Agent Builder Platform FAQ), Appendix A (Role Cross-Reference) |
| A system integrator planning delivery | §5.3 (Adoption Trajectories), §6.4 (SI FAQ) |
| An enterprise CTO evaluating the protocol | §3 (Protocol Applicability), §5.1 (Neutrality Framework) |
| An enterprise CISO evaluating security | §6.3 (CISO FAQ — APP-3 security domains), §7.2 (Trust Boundaries) |
| An ISV technical lead | §5.3 (ISV Trajectory), §6.5 (Agent Builder Platform FAQ) |
| A field deployment team (initial setup, source document preparation) | §7.2 (Trust Boundaries), APP-5 §4.5 (FD obligations), APP-3 §6 (FD security role) |

---

## 1. Introduction

### 1.1 Purpose

The Agentic Process Protocol (APP) defines how governed process specifications are constructed, how execution evidence is assembled across vendor boundaries, how human oversight quality is measured, and how processes improve through governed feedback loops. The normative specifications — APP-2 (Core), APP-3 (Security), APP-4 (Entity Correlation) — define *what* conformant implementations produce. This guide helps implementors understand what the protocol asks of them in practical terms: what changes, what doesn't, what the adoption path looks like, and what value each participant gains.

### 1.2 Scope

This guide covers adoption guidance for the five primary implementor roles recognised constitutionally in APP-1 Article 5 and operationally defined by APP-5: governance orchestrator, telemetry contributor, agent builder platform, enterprise deployer, and field deployment. It does not cover protocol internals, security mechanism design, or entity correlation algorithms — those are implementation choices documented outside the protocol series.

### 1.3 Relationship to Other APP Documents

| Document | What It Provides | What This Guide Adds |
|:---|:---|:---|
| **APP-2 (Core Specification)** | 12 protocol capabilities (A0–A11), maturity model (L1–L4), conformance profiles | Worked examples of what each capability means for an ERP vendor or platform team at each maturity level |
| **APP-3 (Security Architecture)** | 14 security domains (S1–S14) plus temporal activation ordering (XX), security requirements per capability | Practical security integration guidance — what an ERP vendor's security team needs to evaluate |
| **APP-4 (Entity Correlation)** | Entity extraction, correlation, verification requirements | When and why entity correlation matters for intra-app and cross-app governance |
| **APP-IG-02 (Cross-Reference Matrix)** | Inter-document requirement mappings | This guide references APP-IG-02 for detailed requirement-to-requirement traceability |

### 1.4 Reference Implementations (APP-R Series)

APP-1 §4 recognises an informative tier of Illustrative Reference Artefacts (APP-R series) that sits alongside the normative specifications and the implementation guides. An APP-R artefact is a non-normative reference realisation of a specific normative requirement — a reference schema, a reference binding, a worked example of a concrete representation. It illustrates one way the requirement can be satisfied; implementations may deliver equivalent conformance via other realisations and are not disadvantaged for choosing differently.

Two reference artefacts land with the current baseline:

| Artefact | Realises | What implementors use it for |
|:---|:---|:---|
| **APP-R1 (Frame Schema)** | CORE-A1-05 Frame schema portability | A JSON Schema 2020-12 realisation of the published Frame schema requirement. Implementors may validate their own Frame instances against it, publish it as their own schema realisation, or use it as a starting point for a derivative schema that covers the same required attributes. |
| **APP-R2 (MCP Binding Reference Design)** | CORE-A1-04 MCP Server Profile Recommended Pattern | A reference binding of the A1 integration surface onto MCP primitives (resources, methods, notifications, tool façades) with the security binding wired through APP-3 SEC-S1/S2/S13/XX. Implementors may use it as a reference for an MCP-based implementation of A1, or adopt a different binding that satisfies the Required Outcomes of A1. |

Reference artefacts carry no conformance obligation of their own. The conformance obligations in APP-5 apply to the implementation, not to the reference artefact. An implementation that departs from APP-R1 or APP-R2 is conformant if its own realisation satisfies the APP-5 tests for the requirements concerned.

---

## 2. Why the Protocol Exists: The Governance Gap

### 2.1 The Evidence Asymmetry

Enterprise software evolved with a structural asymmetry in its evidence architecture. Deterministic tasks — purchase orders, journal entries, approval workflows — were designed from inception as numbered, retrievable transaction records inside ERP engines. A purchase order has a PO number. A journal entry has a document number. These records are addressable, field-level auditable, regulatory by design, relationally structured, and accountability-attributed. They are not audit trails overlaid on execution — they *are* the execution record.

Judgment-dependent tasks — vendor selection rationale, interview scoring decisions, risk assessments, exception handling — had no equivalent primary record inside ERP. The system recorded the *outcome* of the judgment (the approved PO number, the selected candidate) but not the judgment itself. This was not a gap in prior eras — humans were the judgment engine, and their cognition was not instrumented.

### 2.2 How AI Changed the Equation

As AI capabilities moved from bounded ML classification (invoice OCR, attrition prediction) through conversational navigation (natural language queries against semantic layers) to agentic orchestration (LLM-planned multi-step process execution), the evidence asymmetry deepened rather than closed. At each stage, AI-mediated judgment produced richer outputs feeding into ERP transaction records, but the reasoning chain — why a particular action was taken, what alternatives were considered, what confidence level applied — remained in parallel registers: developer observability logs, LLM tracing tools, and analytics data stores structurally disconnected from the ERP transaction record.

By 2025–2026, every major enterprise platform converged on a hybrid model: deterministic execution for reliability where the step sequence is knowable, probabilistic reasoning where genuine judgment is required. Salesforce introduced guided determinism with finite state machines governing execution paths. Workday's Sana platform built on the principle that AI only works in the enterprise when connected to trusted, deterministic systems. ServiceNow embedded AI agents within a deterministic workflow fabric. Oracle formalised dual orchestration patterns — Workflow Agents (deterministic) and Supervisor+Agents (LLM-orchestrated).

This convergence solved execution drift. What it has not solved — and what the protocol addresses — is the governance gap: no standardised way to specify which steps require human judgment and which are fully deterministic (D/P classification), no cross-system execution evidence record capturing both tracks, no measured human oversight quality, no accountability architecture spanning vendor boundaries, and no closed-loop mechanism connecting execution evidence back to process improvement.

### 2.3 What the Protocol Adds

The protocol defines twelve capabilities (A0–A11) that constitute governed process execution (APP-2 §3). These capabilities exist at the protocol level — above any single vendor's implementation — because the governance gap is structural: it exists wherever processes involve AI-mediated decisions, whether those processes span multiple applications or operate within a single platform.

The protocol's primary evidence artifact — PxER (Process Execution Record) — captures governance data alongside references to source-system transaction records (`CORE-A2-01` through `CORE-A2-12`). For ERP vendors, PxER supplements existing transaction records. ERP transaction tables remain the primary business record — the PO number, the journal entry, the approval chain. PxER adds the governance dimension that ERP records structurally cannot capture: D/P conformance per step, P-track decision evidence, measured HITL engagement quality, cross-system compliance status, and accountability attribution across the three-layer model (intent, execution, oversight). PxER references ERP transactions via traceback fields; it does not duplicate or replace them.

---

## 3. Protocol Applicability

### 3.1 Cross-Application Processes

Cross-application processes are the protocol's primary design target (APP-2 §5.1). When a governed process spans SAP, Workday, ServiceNow, and email — each with independent transaction records, compliance enforcement, and no shared governance authority — no single vendor can provide end-to-end governance. The protocol fills this gap.

Six characteristics make cross-application processes the highest-priority target: independent entity representations across systems, no shared entity authority without MDM, integration-mediated handoffs with latency and transformation, regulatory accountability spanning system boundaries (SOX, EU AI Act), AI agent execution amplifying the gap (agents lack the informal cross-system context humans carry), and agent-to-agent handoffs losing context that human handoffs preserve through conversation.

When AI agents execute cross-system processes via A2A or MCP, the protocol's evidence architecture captures the end-to-end governance chain. Evidence completeness depends on integration maturity (L1–L4) and source-system contribution depth — detailed in §4. For cross-enterprise B2B integration (processes spanning separate enterprises), trust boundaries limit evidence exchange. Cross-enterprise interactions operate on a D-track-by-default basis under current assurance assumptions — each party's execution record captures its own side; no shared governance context exists unless explicitly negotiated via protocol mechanisms (`CORE-A2-11`, `CORE-A2-12`).

For detailed cross-application entity correlation requirements, see APP-4 §4.3.

### 3.2 Within a Single Application

The governance gaps the protocol addresses — D/P classification, P-track evidence, HITL quality measurement, accountability attribution — exist within every major enterprise platform, not only across vendor boundaries (APP-2 §5.2).

Consider an ERP platform processing a performance review: the manager opens the review form (deterministic), enters ratings (judgment-dependent), receives an AI-suggested development plan (probabilistic), sends notification (deterministic), receives employee acknowledgment (deterministic), and routes to HR review (judgment-dependent). Six steps, five within the ERP, one inter-system. The ERP transaction record captures the approved ratings and the completed review — but not whether the manager genuinely engaged with the AI suggestion, whether the AI suggestion was appropriate for the employee's context, or whether the HR reviewer exercised independent judgment or rubber-stamped.

The protocol's capabilities add governance value within this single-application process:

- **D/P classification** (`CORE-A3-01`) declares which steps are deterministic and which require judgment — a distinction no ERP vendor currently makes at per-step granularity in their agent builder output.
- **Conformance tracking** (`CORE-A3-02`, `CORE-A3-03`) records whether each step actually executed on the track it was classified for. If step 1 is D-classified but the ERP routed it through an LLM, the conformance delta is captured and flagged.
- **HITL engagement quality** (`CORE-A6-01` through `CORE-A6-05`) measures whether the manager's and HR reviewer's engagement was genuine — dwell time, scroll depth, evidence reviewed — not just that they clicked "approve."
- **Accountability attribution** (`CORE-A4-01` through `CORE-A4-05`) captures three layers: who specified the process (intent), what executed each step (execution engine — rule engine vs LLM), and who exercised oversight (oversight quality).

Intra-application adoption is not required for protocol conformance. L3 intra-application telemetry is *not* a prerequisite for L2 cross-vendor governance; it is the prerequisite for high-fidelity visibility and independently attributable intra-application evidence across participating applications. The protocol does not replace vendor-internal process engines (APP-1 non-goal d). L3 conformance — the intra-application integration level — is a telemetry integration (`CORE-L3-01`), not an architectural change.

Note that compliance constraints at C3 (corporate policies) and C4 (local rules) per `CORE-A5-01` apply regardless of whether a process is intra-system or cross-system. A Workday-only HCM process subject to UAE labour law Article 120 still requires the compliance constraint to be encoded in the Process Frame and evidenced in PxER — even though the process never crosses a vendor boundary.

---

## 4. What Conformance Means by Integration Level

### 4.1 Worked Example: ERP-Heavy Process

**Performance Review (SAP SuccessFactors + Email)**

```
Step 1: Manager opens review form ──── [D] ── SAP SF  (intra)
Step 2: Manager enters ratings ──────── [P] ── SAP SF  (intra)
Step 3: AI suggests development plan ── [P] ── SAP SF  (intra, AI-assisted)
Step 4: Send notification to employee ─ [D] ── Email   (inter)
Step 5: Employee acknowledges ────────── [D] ── SAP SF  (intra)
Step 6: HR reviews completion ────────── [P] ── SAP SF  (intra)
```

Six steps. Five are intra-SAP. One is inter-system (email). This is a representative ERP-heavy process.

### 4.2 Evidence by Integration Level

**At L2 (governance orchestrator manages the E2E process):**

The governance orchestrator manages the Process Frame (`CORE-A0-01`) for the end-to-end process. It orchestrates Step 4 (the inter-system step) via API/MCP. Steps 1, 2, 3, 5, 6 execute inside SAP — the orchestrator captures a boundary-observed completion signal, where available ("SAP completed Step N at timestamp T"), and has no visibility into *how* each step executed. **Evidence-source qualifier (v1.9):** at L2, completion signals are boundary-observed rather than authoritatively verified. Source-asserted completion is not the same as independently verified completion; conformance evidence at this level is subject to the trust posture between the orchestrator and the executing system.

| Evidence Dimension | Source | Coverage |
|:---|:---|:---|
| Step 4 (email): API call, params, response, timing | Orchestration telemetry | Full |
| Steps 1–6: completion timestamps | Orchestration boundary | Timestamp only |
| D/P conformance | Step 4: STATISTICAL. Steps 1–6: UNVERIFIABLE | Low for intra-system |
| HITL engagement (Steps 2, 3, 6) | Not measured — inside SAP UI | None |

Protocol value at L2: the Process Frame captures the E2E specification including governance attributes. Step 4's inter-system compliance — for example, "notification must go to employee's personal email per local data protection law, not just corporate" — is enforced at orchestration level. But 83% of the process (5 of 6 steps) is a governance blind spot.

**At L3 (SAP contributes telemetry):**

SAP implements the Telemetry Contribution Protocol (a standardised event schema defined in `CORE-L3-01` by which L3 applications contribute intra-app execution data to PxER assembly) — reporting, per step:

| Field | Content | Example |
|:---|:---|:---|
| `execution_engine` | What executed the step | `"sap_sf_rule_engine"` or `"sap_joule_llm"` |
| `dp_classification_actual` | D or P actual execution | `"D_RULE"` or `"P_LLM"` |
| `engagement_metrics` | If HITL: dwell, scroll, decision | `{dwell_ms: 34000, scroll_pct: 85}` |
| `compliance_evidence` | If applicable | `{sox_sod_check: "PASS"}` |
| `transaction_ref` | SAP transaction ID | `"SF_PERF_2026_004821"` |

| Evidence Dimension | Source | Coverage |
|:---|:---|:---|
| All steps: execution engine, timing, transaction ref | SAP Telemetry Protocol | Full |
| D/P conformance | Per-invocation MATCH/MISMATCH via `execution_engine` | Operational |
| HITL engagement (Steps 2, 3, 6) | SAP reports dwell, scroll from its approval UI | Measured |

Protocol value at L3: visibility into the 83% that was previously opaque. D/P conformance checks become operational: if Step 1 is D-classified in the Frame but SAP reports it executed through an LLM inference engine, a MISMATCH is detected and review triggered (`CORE-A3-03`). Governance evidence can now quantify: "3 of 6 steps are P-track in SAP. 2 show consistent patterns suggesting deterministic potential."

### 4.3 The L2→L3 Visibility Delta

*Illustrative scenario arithmetic; not a protocol performance claim. The percentages depend on how "visibility" is defined in the denominator (here: fraction of step-level execution facts captured in PxER) and the specific process mix. Actual visibility gains vary by application, integration surface, and process type.*

```
┌──────────────────────────────────────────────────────────────┐
│  PROCESS GOVERNANCE VISIBILITY (illustrative)                 │
│                                                               │
│  L2:  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ █████████  │
│        SAP steps (timestamp only)                 Email step  │
│        ~20% governance visibility (illustrative)   (full)     │
│                                                               │
│  L3:  ████████████████████████████████████████████ █████████  │
│        SAP steps (execution engine, D/P,          Email step  │
│        engagement, compliance, tx ref)            (full)      │
│        ~95% governance visibility (illustrative)              │
│                                                               │
│  ERP vendor effort: one telemetry protocol integration        │
│  Illustrative delta: 75 percentage points more visibility     │
│  in this specific scenario                                    │
└──────────────────────────────────────────────────────────────┘
```

This visibility delta illustrates what makes the protocol's L3 proposition practical in scenarios where the enterprise governs SAP-heavy processes: substantially more governance coverage, achieved via a bounded, well-specified telemetry integration on the ERP side — not a platform migration. The specific numbers are scenario-specific illustrations, not general protocol performance claims.

### 4.4 What the ERP Vendor Does — and Does Not Do — at L3

**Required for L3 conformance** *(in this illustrative profile, subject to APP-5's current role × L-level matrix — refer to APP-5 §4 for the authoritative applicability determination for each requirement ID)*:

- Implement the Telemetry Contribution Protocol event schema
- Report `execution_engine` and `dp_classification_actual` per step
- Report `transaction_ref` for traceback to the ERP's own transaction records
- Authenticate telemetry per APP-3 requirements (SEC-S4 evidence integrity)

**Recommended for higher L3 maturity:**

- Report HITL engagement metrics from approval UIs (`CORE-A6-02`)
- Report compliance evidence for intra-system compliance steps (`CORE-A5-01`)
- Support entity extraction for governed process steps (`EC-01`)

**Does not need to do:**

- Change internal process engine or routing
- Adopt D/P runtime separation internally
- Enforce external governance attributes on internal processes
- Modify approval UX design
- Accept external orchestration of intra-system steps
- Replace internal transaction records with PxER

The L3 ask is a telemetry integration — not an architectural change. The ERP vendor reports what happened; the protocol assembles the governed record. The ERP vendor's transaction tables remain the authoritative business record. PxER adds governance evidence that those tables structurally cannot capture.

### 4.5 Vendor Access Posture

> *Informative procurement taxonomy — not an APP conformance dimension. Access posture is a vendor architectural characteristic that materially affects what evidence is reachable; it is not itself a requirement. If future revisions promote the declaration concept into normative form, it will appear in APP-5's conformance-declaration schema; until then, adopters use this taxonomy for procurement selection, not for conformance claims.*

Beyond the L1–L4 integration maturity dimension (§4.2), implementors face a second dimension that determines what governance evidence a downstream enterprise can actually reach: how the vendor exposes its runtime to protocol integration. Three access postures recur across enterprise application vendors:

| Posture | Pattern | Governance evidence path |
|:---|:---|:---|
| **Open Direct** | Vendor exposes agent identity, session state, and telemetry contribution surfaces to the enterprise's governance orchestrator directly. Enterprise-owned identity provider authenticates the agent; telemetry writes into the enterprise's PxER pipeline via a documented contract. | L2+ conformance is achievable end-to-end at the enterprise level. `SEC-S4-05` write-path provenance is direct. |
| **Mediated** | Vendor exposes agents only through the vendor's own orchestration surface; the vendor's platform is always the immediate caller. Enterprise sees evidence about the vendor's agent, not about the underlying model or delegated action. | L2 conformance is achievable at the vendor surface. `CORE-A2-11` cross-enterprise boundary and APP-3 S13 identity-binding requirements apply at the vendor boundary; evidence attribution beyond that boundary depends on the vendor's own conformance to `SEC-S4-05` (write-path provenance) and `CORE-A2-08` (orchestration-level P-track evidence). |
| **Closed** | Vendor does not expose agent identity, session state, or telemetry contribution surfaces to any external orchestrator. Governance evidence about vendor-executed steps is not reachable by the enterprise. | L1 (boundary observation) is the only achievable level. `CORE-A2-12` unmanaged trust boundary applies. Conformance statement should declare this scope limitation per `CONF-D-05`. |

Access posture is a vendor architectural choice, not a protocol requirement. Implementors selecting between vendors for a governance-critical step should evaluate the target vendor's posture as part of the integration decision. The protocol accommodates all three postures at their respective conformance levels; the enterprise's overall conformance profile is the aggregate across every vendor participating in the process.

**Interaction with L1–L4.** Access posture and integration maturity are orthogonal. A vendor may be Open Direct at L2 and remain L2 (no L3 telemetry contribution) or advance to L3. A vendor operating Mediated may still support L3 within its own boundary. Enterprise conformance declarations SHOULD surface both dimensions when scope is declared per `CONF-D-01`.

**Attribution across mediation.** Under Mediated posture, the immediate caller recorded in the trace is the vendor's orchestration surface rather than the underlying model or the delegated actor. Preserving trace-back to the responsible actor across the mediation boundary is an open interoperability question — see APP-IG-02 §6 (Known Open Issues).

---

## 5. Stakeholder Adoption Guide

### 5.1 Protocol Neutrality Framework

The protocol's adoption depends on perceived neutrality across stakeholder groups with competing interests. Four dimensions determine whether a stakeholder considers the protocol credible — not just whether the specification is open, but whether governance of the standard, implementation independence, commercial implications, and data flow architecture all pass scrutiny.

| Dimension                                                                                                                                  . | What Stakeholders Evaluate                                                                                                                            . | Protocol Design Response |
|:---|:---|:---|
| **Governance of the specification** | Who decides what enters v2, v3? | Vendor-authored during production-proof phase. Contribution to multi-stakeholder body once production-validated (APP-1 §7). Governance transitions are pre-committed, not aspirational. |
| **Implementation independence** | Does using the protocol require any specific product? | The protocol is implementable by ERP vendors (L3), hyperscalers (hosting), ISVs (L4), and SIs (deployment) independently. The specification is the standard; any conformant implementation qualifies. |
| **Commercial independence** | Does protocol adoption advantage any single product? | The protocol defines the governance floor. Implementation advantages above the floor — such as specific runtime architectures — are not encoded in the specification. No implementation is privileged by the protocol design. |
| **Data architecture** | Does the protocol route enterprise data through any originator's infrastructure? | The protocol does not require enterprise data to flow to a protocol originator. PxER stores governance metadata (D/P classification, engagement metrics, compliance evidence, accountability chain) and transaction references — not copies of enterprise transactional data. ERP systems remain the source of truth for business data. **Implementations MUST disclose their actual governance-data flow, hosting, and processor roles in their deployment documentation** — the protocol design does not itself guarantee non-routing; only the specific implementation architecture does. Any vendor — ERP, hyperscaler, ISV, or specialist — can build PxER capture, storage, analytics, and process intelligence tooling. The protocol defines the evidence schema and requirements; the tooling market is an open competitive surface. Enterprises choose whichever implementation offers the best value for their governance needs, subject to disclosed data flow, hosting, and processor architecture. |

### 5.2 What Each Stakeholder Keeps vs Gains

| Stakeholder | What They Keep (Not Threatened) | What the Protocol Adds |
|:---|:---|:---|
| **ERP Vendor** | Proprietary knowledge graph, agent builder, domain model, intra-system governance, transaction record authority | Cross-system governance composition; their governance data becomes more valuable in E2E context |
| **Hyperscaler** | Infrastructure, identity, data platform, agent runtime | Process governance layer they don't need to build; complements MCP/A2A with process semantics |
| **SI / Consulting** | Delivery methodology, client relationships, domain expertise | Reusable Process Frame library; repeatable governance assessment methodology; recurring governance revenue |
| **Enterprise (CIO)** | Vendor choices, existing investments, technology strategy | Vendor-neutral governance; audit readiness; vendor negotiation leverage via conformance transparency |
| **Enterprise (CISO)** | Security architecture, identity policies, perimeter controls | Process-level governance containment (not just infrastructure-level monitoring) |

### 5.3 Adoption Trajectories by Implementor Role

**ERP Vendor (SAP / Salesforce / Workday archetype)**

| Phase | Activities | Protocol Capabilities Engaged |
|:---|:---|:---|
| **Evaluate** | Assess protocol specification. Map existing capabilities (Skills/Agents, Agent Script, Illuminate) to D/P terminology. Internal architecture assessment. | None — evaluation only |
| **Benefit at L2** | No ERP vendor action required. A governance orchestrator manages the E2E process using the ERP's existing API/MCP surface. The ERP vendor's customers gain cross-system governance visibility for inter-system steps immediately. Intra-ERP steps captured at boundary level only (timestamp, completion status). | None — governance orchestrator handles L2 externally |
| **Pilot L3** | Telemetry contribution on 1–2 process types within own boundary. Validate governance evidence enrichment value. Test Process Frame integration with agent builder. | A1 (inbound), A2 (L3 telemetry), A3 (conformance reporting) |
| **GA L3** | Publish L3 conformance. Conformance schema produces governance gap visibility for customers. | A1–A6 at L3 |
| **Domain extensions** | Co-develop domain-specific Process Frame templates. Contribute domain expertise to compliance content (C2). Shape protocol evolution via standards body participation. | A0 (domain templates), A5 (C2 content), ecosystem |

**Hyperscaler (Azure / GCP archetype)**

| Phase | Activities | Protocol Capabilities Engaged |
|:---|:---|:---|
| **Evaluate** | Assess protocol as managed service candidate. Map to existing infrastructure (identity, data platform, agent runtime). | None — evaluation only |
| **Infrastructure integration** | Protocol metadata in agent deployments. Agent deployments carry Process Frame references. Existing HITL infrastructure extended with engagement schema. | A1 (hosting), A4/A6 (engagement infrastructure) |
| **Managed service** | Platform-native protocol hosting. PxER storage on platform infrastructure. Compliance integration with platform data governance. | Full L2 hosting |
| **Platform service** | Process governance as a platform capability. Marketplace for Process Frame templates. Cross-tenant benchmarking infrastructure. | Ecosystem enablement |

**System Integrator (Big 4 / boutique archetype)**

| Phase | Activities | Protocol Capabilities Engaged |
|:---|:---|:---|
| **Methodology development** | Train delivery teams on Process Frame authoring. Develop governance assessment methodology. Build initial Process Frames for pilot customers. | A0 (frame authoring) |
| **Pilot deployments** | First L2 customer deployments. Validate delivery methodology. Establish PxER-based outcome measurement. | A0–A6 at L2 |
| **Library-based delivery** | Reusable Process Frame library by industry vertical. Governance assessment as repeatable methodology. | A0 (library), A5 (C2 templates) |
| **Managed governance service** | Ongoing governance monitoring, compliance updates (C0 regulatory changes), Frame evolution advisory. Recurring revenue model. | A9–A11 (learning, evolution) |

**ISV (Vertical SaaS / Overlay Application archetype)**

| Phase | Activities | Protocol Capabilities Engaged |
|:---|:---|:---|
| **Consume at L2** | ISV application participates in governed processes via existing API/MCP surface. No ISV action required — governance orchestrator manages. | None — governed externally |
| **Contribute at L3** | ISV implements Telemetry Contribution Protocol for ISV-owned execution steps. Reports execution engine, D/P classification, transaction refs. | A2 (L3 telemetry), A3 (conformance reporting) |
| **Build on L4 SDK** | ISV builds new application on an L4-compliant platform. Full Process Frame integration, dual D/P runtime, domain-specific compliance templates. | All (L4) |
| **Domain contribution** | Domain-specific Process Frame templates. C2 compliance content for ISV's vertical. Marketplace certification. | A0 (domain templates), A5 (C2 content) |

### 5.4 Agent Model Realization Patterns

The protocol is deliberately pattern-neutral — APP-2 §4.3 establishes that the governance implementation and the agent system are two distinct actors at every maturity level, with the relationship between them free to vary. Four realization patterns have emerged in practice. All four are conformant; the choice reflects platform architecture and organisational boundaries, not protocol obligation.

**Dedicated orchestrator.** A standalone governance platform owns the Process Frame, assembles the PxER, and mediates interactions between agent builders. Enterprise systems and agent frameworks integrate via the A1 surface but remain architecturally independent. Typical for mixed-vendor environments where no single platform is a natural governance authority. Highest neutrality and clearest accountability separation — at the cost of one more integration surface.

**Native embedding.** The governance layer operates inside the primary execution platform. Process Frame and PxER are first-class constructs in the platform's own runtime. Applicable when an ERP vendor or AI-native platform elects to treat the protocol as a built-in capability rather than an external integration. Reduces integration friction; requires the platform to evidence neutrality through conformance reporting (`CORE-CP-01` through `CORE-CP-04`) rather than architectural separation.

**Sidecar / observer.** A governance component runs alongside an existing orchestration platform, consuming its telemetry and assembling protocol-conformant evidence without replacing the orchestrator. Useful for brownfield deployments where the existing orchestrator is not being replaced but governance-conformant evidence is required. Evidence completeness depends on what the orchestrator exposes — typically starts at Retrospective or Detective conformance and moves toward Preventive as observability deepens.

**Retrospective audit.** PxER assembly runs against historical execution data rather than concurrent with execution. Conformance is Retrospective-only by construction. Useful for establishing governance on existing deployments before operational integration is feasible. Produces audit-grade evidence but cannot enforce Preventive or Detective conformance on the audited processes.

Most L2 deployments begin with the dedicated-orchestrator or sidecar pattern. L3 progression typically shifts the intra-application portion toward native embedding while retaining a dedicated orchestrator for cross-system processes. L4-native platforms collapse the distinction — governance is embedded in the runtime by construction.

### 5.5 Customer Starting Points and Expected Value

The protocol's entity correlation architecture (APP-4) operates across a wide range of customer semantic infrastructure maturity. Inferred correlation (`EC-15`) is always available — discovered from PxER co-occurrence without external dependency. Populated correlation (`EC-19`) layers in where customer sources exist. The four common starting configurations:

| Customer Reality | Default Mode | Populated Path | Incremental Value |
|:---|:---|:---|:---|
| **No MDM, no integration suite** | Inferred-only. Entity extraction from MCP tool responses at L2. | File/API import if any mapping tables can be exported. Otherwise inference-only. | Cross-system entity traceability, anomaly detection, undocumented business rule discovery from first viable process volume. |
| **Integration suite in place** (MuleSoft, Boomi, SAP IS) | Inferred mode runs in parallel. | Integration mapping tables exported; Process Frame steps optionally reference integration flows. | Above, plus per-instance propagation verification and integration lag attribution. |
| **EDW / data lake** (Snowflake, Databricks) | Inferred mode runs in parallel. | Dimension or join tables imported via the standard correlation import interface. | Above, plus higher-confidence correlations from EDW entity resolution feeding reconciliation. |
| **Mature MDM + semantic layer** | Inferred mode runs in parallel; reconciliation engine active. | MDM golden records imported. Populated source authenticates per `SEC-S14-06`. | Above, plus stale-mapping detection when inferred diverges from populated — an operational signal neither MDM nor integration monitoring produces. |

The design principle is consistent across all four: **normalise inputs, not source systems**. Implementations define a small number of input shapes — entity extraction declarations on the Process Frame, a correlation import schema — and customer deployment maps whatever infrastructure exists into those shapes. No per-vendor adapters, no customer-class-specific architecture.

The inference-first default protects against a common adoption misconception: that entity correlation requires MDM or an integration platform. It does not. For most deployments, the highest-value transition is from no entity tracking to inferred-only correlation — every subsequent maturation adds incremental depth rather than core capability.

---

## 6. Implementor FAQ

### 6.1 ERP Vendor Technical

**Q: Why would I adopt a protocol that makes my governance data portable?**

It does not make your business data portable. Your knowledge graph stays proprietary. Your agent builder stays proprietary. Your domain model is your competitive advantage. The protocol standardises the *governance wrapper* — D/P classification, compliance constraints, HITL requirements, accountability — that enables cross-system composition. Your process domain intelligence feeds the Process Frame; the protocol makes that intelligence composable across vendor boundaries where it currently stops. Your transaction records remain the authoritative source for business data; PxER references them, not replaces them. And the tooling that captures, stores, and analyses PxER data is an open market — any vendor, including you, can build the governance analytics offering for your customer base. Enterprises will choose whichever solution delivers the best value.

**Q: Can't I extend my agent framework to govern cross-system processes via A2A/MCP?**

You can orchestrate cross-system. You cannot govern cross-system — four ceilings apply. (1) Governance authority stops at your application boundary: you cannot enforce that a step in another vendor's system follows D/P classification from your Process Frame. (2) PxER assembly requires telemetry from systems you don't control. (3) Inter-system compliance constraints spanning two vendors cannot be owned by either vendor. (4) When a process spans multiple ERP platforms, the "primary orchestrator" question creates disputes that only a neutral governance layer resolves.

**Q: What does L3 adoption actually require from my engineering team?**

Three things: (1) add `execution_engine` and D/P classification to your agent builder's telemetry output — declaring which runtime executed each step; (2) emit that telemetry via the Telemetry Contribution Protocol (a standardised event schema); (3) optionally, consume Process Frame resources via the MCP Server Profile (`CORE-A1-04`) to receive governance change propagation. Item 1 is the core commitment. Items 2–3 use infrastructure (MCP, event schemas) you are already building. See §4.4 for the complete L3 requirements.

**Q: Does the protocol require dual D/P runtimes?**

No. The protocol requires that you *declare* D/P per step (`CORE-A3-01`) and *record* what actually executed (`CORE-A3-02`). Whether your platform routes D-classified steps to a rule engine or still uses LLM inference is your implementation choice. The conformance schema honestly records the result. Over time, the governance evidence quantifies the cost and governance implications of non-native execution — creating transparency for enterprise customers, but not protocol non-compliance.

**Q: Can my enterprise-wide agent registry become the governed agent catalog?**

Yes — and this is a natural adoption path. The protocol defines governance attributes for agent identities: accountability chain, delegation scope, autonomy level, and behavioural baseline (`CORE-A4-01` through `CORE-A4-05`; APP-3 S13 Agent Identity). If you operate an enterprise-wide agent registry or catalog — as SAP (LeanIX), Salesforce (Agentforce registry), Workday, and Microsoft (Copilot Studio) are building — integrating protocol governance attributes into your registry entries makes your catalog the enterprise's governed agent surface. Agent deployments registered in your catalog carry Process Frame references, declared conformance profiles, and measurable oversight requirements. This is a competitive differentiator: the first enterprise agent registry with protocol-conformant governance attributes becomes the default for enterprises requiring governed AI deployment.

**Q: Can we start with Retrospective-only conformance?**

Yes. The protocol defines three conformance profiles — Preventive (violations blocked before execution completes), Detective (violations flagged within declared SLA), and Retrospective (violations identified in periodic analysis) — declared per scope (`CORE-CP-01`). Multi-profile per scope is permitted (`CORE-CP-02`). An ERP vendor can begin with a Retrospective profile for L3 telemetry contribution and progress to Detective or Preventive as integration matures. Partial conformance is valid but must be explicitly declared (`CORE-CP-04`, per APP-1 Article 5). Undeclared non-conformance is a conformance violation.

**Q: How does governance apply to a whole P-orchestrated flow, not just individual steps?**

The protocol defines an orchestration completion gate (`CORE-A4-05`, Recommended Pattern) with three tiers: *none* (default, low-risk D-dominant flows), *review* (process owner confirms structured completion summary), and *attestation* (process owner attests with typed justification that the orchestrated sequence was appropriate). The gate is declared in the Process Frame at authoring time based on process risk classification. This addresses the concern that per-step HITL is insufficient for complex P-orchestrated processes — the gate provides whole-orchestration oversight. See also §7.3 for the conformance delta as the primary governance instrument across individual steps.

### 6.2 Hyperscaler / Cloud Platform

**Q: We already have identity, data governance, and agent runtime. Why do we need this?**

You have the plumbing. You don't have the process semantics. Your data platform knows the enterprise's data model; it doesn't know that UAE Article 120 requires notification before termination across two separate systems, or that background checks must precede provisioning per labour law. Process governance requires process domain expertise built from decades of ERP knowledge, not from cloud infrastructure. The protocol is the process governance layer on your infrastructure — adopt it rather than building process domain expertise from scratch, just as the industry adopted container orchestration standards rather than building proprietary alternatives.

**Q: Can we host protocol implementations as a managed service?**

Yes — and this is the natural positioning. You provide identity, data, infrastructure, and agent runtime. A protocol implementation provides process governance. The protocol is infrastructure-neutral; platform hosting is a deployment choice.

**Q: How does the protocol relate to our agent runtime and registry?**

Your agent runtime (Azure AI Foundry, Google Agent Engine, AWS AgentCore) manages agent lifecycle — registry, monitoring, scaling. The protocol adds process governance attributes to that lifecycle: agents carrying Process Frame references, declared D/P classification, conformance profiles, and measured oversight requirements (`CORE-A4-01` through `CORE-A4-05`; APP-3 S13). Specifically, agent registration entries gain three-layer accountability attribution (intent owner, execution identity, oversight quality), session-contextual identity tokens encoding autonomy level and active delegation chain (`SEC-S13-01`), and declared conformance profile per scope. Your agent registry can integrate these attributes, making it the enterprise's governed agent surface — the same adoption path available to ERP vendors with their own registries.

**Q: How does EU AI Act compliance affect the managed service proposition?**

The AI Act's August 2026 enforcement deadline for high-risk AI systems (Annex III categories including HR/recruitment, credit scoring, critical infrastructure) requires risk assessment, monitoring documentation, and human oversight evidence. PxER constitutes the compliance evidence record the Act requires: D/P classification maps to risk tiers (`CORE-A3-01`), PxER is the monitoring documentation, and A6 engagement quality provides the human oversight evidence (`CORE-A6-01`). Hosting PxER storage and protocol infrastructure as a managed service positions your platform as the enterprise's AI governance compliance layer — not just compute and identity. For enterprises operating in Annex III-covered domains, this is a near-term compliance requirement, not a future consideration.

### 6.3 Enterprise (CTO / CISO)

**Q: How does this relate to EU AI Act compliance?**

The AI Act (effective August 2026 for high-risk systems, Annex III categories) requires risk assessment, monitoring, and human oversight — but has published no guidance specifically addressing AI agents, autonomous tool use, or runtime behaviour. The protocol provides all three at the process level: D/P classification maps to risk tiers, PxER is the compliance evidence record, and A6 engagement quality provides documented evidence of informed human oversight (`CORE-A6-01` through `CORE-A6-05`). The conformance delta — intended vs actual D/P per step — is a concrete compliance instrument where none currently exists for process-level AI governance.

**Q: How does the protocol's security architecture map to our existing security controls?**

APP-3 defines 14 security domains (S1–S14) plus temporal activation ordering (XX), each targeting a specific vulnerability class in governed process execution. These are designed to layer on top of — not replace — your existing security infrastructure. Key domains for CISO evaluation: S1 (Frame Integrity) addresses poisoning and rollback attacks on governed process specifications. S2 (Transport & Federation) covers MCP/A2A transport vulnerabilities. S5 (Human Oversight Security) addresses attacks on approval surfaces and engagement telemetry privacy. S7 (Orchestration Integrity) covers governance bypass through forced degradation. S13 (Agent Identity) defines non-deterministic session identity for AI agents. S14 (Entity Correlation Security) protects cross-system entity references — tenant isolation, populated source authentication, cross-enterprise boundary limits, and retention. XX (Temporal Activation Ordering) addresses the highest-risk deployment window: the period between data flow activation and security control readiness. Your identity infrastructure (Entra ID, Okta, etc.) provides the authentication layer; the protocol adds process-governance-scoped authorisation and accountability on top.

**Q: What about approval surface integrity — can AI-generated content manipulate human approvers?**

This is a recognised attack class. APP-3 S5 defines requirements for ensuring that human approval surfaces render from verified governance data, not from AI-produced content that may contain embedded manipulation. The protocol requires that approval surfaces are architecturally isolated from AI-generated content streams — the human reviewer sees verified context, not content an AI agent could influence. Engagement telemetry (dwell time, scroll depth, canary detection) provides measurable evidence of whether oversight was genuine.

**Q: How does the protocol handle evidence integrity and tamper detection?**

APP-3 S4 (Evidence Integrity) defines requirements for PxER truthfulness, contributor authentication, and write-path provenance. Governance evidence must be verifiable as unmodified after assembly — a protocol invariant (APP-1 invariant b). For telemetry contributed by L3 applications, contributor authentication requirements ensure that evidence originates from the declared source system (`SEC-S4`). Newly registered L3 contributors face elevated verification frequency (`SEC-S4-04`) until trust is established. See APP-IG-02 for the complete mapping between S4 requirements and APP-2 capability A2.

**Q: What happens when the governance layer is unavailable — does business execution stop?**

No. The protocol explicitly requires that governance does not block business execution (`CORE-XX-01`). However, degradation is compliance-tiered (`SEC-S7-02`): C0/C1 compliance-critical processes (regulatory, protocol-mandated) fail closed — execution halts rather than proceeding ungoverned. C3/C4 processes (corporate policies, local rules) may fail open with PxER gaps flagged for retrospective reconciliation. Degradation security controls (`CORE-XX-02`) prevent attackers from forcing degradation to bypass compliance-critical governance. See §7.2 for the trust boundary model that governs evidence completeness during normal and degraded operation.

**Q: How does the protocol handle AI agent identity and session security?**

APP-3 S13 (Agent Identity) defines session-contextual identity requirements for AI agents. Each agent session carries a token encoding autonomy level, active delegation chain, and HITL engagement level (`SEC-S13-01`). These tokens must be retained for compliance-relevant periods (`SEC-S13-02`). This is the protocol's answer to the "Know Your Agent" requirement: every agent action in a governed process is attributable to a specific session context with declared scope and authority, not just a service account credential.

**Q: How can we report AI governance posture at board level?**

The protocol's Preventive / Detective / Retrospective conformance profile vocabulary (`CORE-CP-01`) maps directly to the risk management language boards use. An enterprise can report: "Our SAP integration operates at L3 with a Detective conformance profile; our cross-system processes operate at L2 with Retrospective conformance. 78% of process steps have MATCH conformance status; 12% show MISMATCH requiring remediation." This is concrete, measurable governance reporting — not qualitative assurance. The conformance delta (`CORE-A3-02`, `CORE-A3-03`) provides the quantitative foundation.

### 6.4 System Integrator

**Q: How does this change my delivery model?**

Today: per-engagement process capture, per-deployment agent configuration, per-customer governance design — all rebuilt from scratch. With the protocol: Process Frame libraries provide common process patterns pre-built. Delivery shifts from construction to configuration — customise overlays on validated frames. The governance assessment (gap analysis → Process Frame design → L2 deployment) becomes a repeatable methodology, not a bespoke consulting engagement.

**Q: What new service lines does the protocol enable?**

Five categories beyond traditional delivery:

*Governance-as-a-Service.* Ongoing monitoring of conformance deltas, compliance updates (C0 regulatory changes propagated through Process Frames), Frame evolution advisory, and drift detection analysis (`CORE-A9-01`, `CORE-A10-01`). This is recurring revenue — not project-based.

*Protocol Conformance Assessment and Certification.* Enterprises will need independent assessment of whether their AI governance meets protocol conformance requirements. SIs can develop certification methodology and become trusted assessors — analogous to SOC 2 audit practices.

*AI Cost Optimisation.* The conformance delta data (intended D vs actual P) directly quantifies where enterprises are spending LLM inference on steps that could execute deterministically. SIs can offer optimisation engagements identifying high-value promotion candidates from PxER evidence — a data-driven service, not opinion-based consulting.

*PxER Analytics and Process Intelligence.* PxER data is a rich source for process mining, bottleneck identification, cross-system SLA tracking, and comparative analysis of agent-executed vs human-executed process instances (`CORE-A11-01`). SIs can build analytics practices on PxER data — offering insights that no single vendor's transaction records can provide because PxER spans vendor boundaries.

*Cross-Vendor Governance Benchmarking.* Enterprises operating multi-ERP estates want to compare governance maturity across vendors. Protocol conformance provides a standardised measurement framework. SIs can benchmark across their client base (anonymised, per APP-3 `SEC-S10` tenant isolation requirements) and offer industry-specific governance maturity insights.

*C2 Compliance Template Authorship.* SIs are the natural authors of C2 (Deployment Templates) compliance packages (`CORE-A5-01`) — industry-specific and region-specific compliance content that enterprises deploy within Process Frames. C2 template libraries by vertical (financial services, healthcare, manufacturing) and jurisdiction (EU, GCC, APAC) represent a distinct licensing revenue line and a barrier-to-entry for competing SI practices.

**Q: How does the Process Frame lifecycle affect delivery milestones?**

Process Frames have a four-state lifecycle: Seed → Observed → Validated → Mature (`CORE-A9-01`). A Frame delivered as a project artifact starts at Seed. It progresses to Observed once execution evidence accumulates, and to Validated once the process owner confirms the Frame accurately represents the governed process (`CORE-A9-02`). This lifecycle affects SI engagement scoping: the initial delivery produces a Seed Frame; achieving Validated status requires a post-deployment observation period and process owner sign-off — creating a natural follow-on engagement. Evidence integrity must be established before lifecycle recommendations are generated (`CORE-A9-03`).

**Q: What should we know about deploying L3 telemetry integrations for ERP vendors?**

Newly registered L3 telemetry contributors face elevated verification frequency under APP-3 evidence integrity requirements (`SEC-S4-04`) until the contributor establishes a trust baseline. This affects delivery timelines: plan for a trust-establishment period during production cutover where contributed evidence undergoes more frequent integrity checks before reaching steady-state verification cadence.

**Q: Does the protocol depend on OSI (Open Semantic Interchange) or any other semantic layer standard?**

No. APP-4's populated correlation mode is source-agnostic (`EC-19`). The standard import interface consumes correlation keys from MDM exports, integration suite mapping tables, EDW dimension tables, or CSV files — whatever the customer has. OSI-compliant semantic layers are one future consumption path that may simplify adoption for customers already on OSI-native platforms, but the protocol does not require OSI and does not privilege OSI over any other populated source. Inferred mode (`EC-15`), which most deployments start with, requires no populated source at all. For SI delivery planning: treat customer semantic infrastructure as an accelerator, not a prerequisite — the populated mode question is independent of L-level and can be sequenced separately.

### 6.5 Agent Builder Platform

**Q: What does the protocol's integration surface expose to my agent framework?**

The protocol defines three interaction patterns through the A1 integration surface (`CORE-A1-01`): outbound (governance orchestrator pushes governed step definitions to agent builders), inbound (agent builders submit execution results and builder changes through the governance gate), and notification (governance propagates Frame changes to registered consumers). The MCP Server Profile (`CORE-A1-04`, Recommended Pattern) is the transport mechanism — your framework consumes Process Frame resources via MCP to receive governed step definitions, D/P classification, compliance constraints, and HITL requirements per step.

**Q: What is the governance gate and how does it affect builder contributions?**

The governance gate (`CORE-A1-02`) classifies builder contributions by governance impact. Unstructured builder changes without governance attributes create gaps that grow silently — the gate ensures that changes to governed processes carry D/P classification, compliance scope, and accountability attribution before entering the governed process specification. Your agent builder's output must include these governance attributes when contributing to protocol-governed processes.

**Q: What session identity requirements apply to my agents?**

APP-3 S13 requires session-contextual identity tokens (`SEC-S13-01`) encoding autonomy level, active delegation chain hash, and HITL engagement level. Each agent session in a governed process carries this token — it's the protocol's mechanism for attributing AI-mediated decisions to specific execution contexts with declared scope. Tokens must be retained for compliance-relevant periods (`SEC-S13-02`). Your framework must generate and attach these tokens when agents execute governed process steps.

**Q: How does consumption-mode parity affect copilot vs autonomous agent vs A2A modes?**

The protocol requires identical governance treatment regardless of how a governed process step is invoked — whether through a copilot UI, an autonomous agent, an A2A delegation, or a traditional screen (`CORE-A7-01`). Your framework must ensure that the same D/P classification, HITL requirements, and compliance constraints apply to a step regardless of which consumption mode triggered it. Ungoverned invocation paths must be recorded as such (`CORE-A7-02`).

**Q: Does entity correlation matter more for agentic processes than for human-operated ones?**

Yes — structurally, not just incrementally. Six reasons compound: agents lack the tribal knowledge a human coordinator carries implicitly; agent intent (what the LLM trace shows the agent meant to do) diverges from business outcome (what actually happened to cross-system entities); agent-to-agent handoffs via A2A/MCP pass structured parameters only, losing the informal context human handoffs carry; agent execution volume makes errors compound across hundreds of instances before detection; regulatory explainability increasingly requires entity-enriched audit trails, not just tool-call logs; and agents exhibit different failure modes (API rate limits, retry storms) that process mining on PxER can reveal. The distinction matters architecturally: guardrails platforms constrain what agents are *allowed* to do (pre-conditions on tool calls); entity correlation validates what they *actually did* to business entities across systems (post-conditions on entity state). APP-4 entity correlation combined with A11 process intelligence is the integration point between LLM observability (what the agent thought) and business system state (what happened) — a position that neither LLM-tracing tools nor single-system process mining can occupy.

---

## 7. Evidence Architecture for Implementors

### 7.1 The D/P Evidence Asymmetry

The protocol's evidence architecture addresses a structural problem, not a feature gap. In traditional ERP systems, D-track tasks were first-class numbered transaction records by design — addressable, field-level auditable, regulatory-grade. P-track tasks (all human judgment before AI, all AI-mediated reasoning now) had no equivalent primary record. The P-track inference — whether from ML models, copilots, or agents — was captured in parallel registers: analytics stores, developer observability tools, LLM tracing platforms — structurally disconnected from the ERP transaction record.

PxER bridges this asymmetry. For each governed process instance, PxER assembles: D/P classification (intended and actual) per step, the execution engine that processed each step, HITL engagement evidence, compliance status, accountability attribution, and traceback references to source-system transaction records (`CORE-A2-01` through `CORE-A2-12`).

For ERP vendors, PxER is a governance supplement. The ERP's transaction records remain the business system of record — PxER references them via traceback and adds the governance dimensions those records cannot capture. For AI-native platforms operating at L4, PxER is the primary execution record assembled by construction. The protocol accommodates both models through the integration maturity framework (L1–L4).

### 7.2 Trust Boundaries

When a governed process crosses platform boundaries, evidence completeness depends on the trust relationship between systems (APP-2 Glossary, `CORE-A2-11`, `CORE-A2-12`):

| Trust Context | Evidence Model | PxER Coverage |
|:---|:---|:---|
| **Internal** | Governance orchestrator and execution surface share a governed boundary | Full — evidence assembled by construction |
| **Enterprise-external** | Agent from within the enterprise boundary calls an external application via A2A/MCP with enterprise IT-authorised credentials | PxER complete for governed side; external system may contribute telemetry at L3 |
| **Cross-enterprise-external** | Off-boundary SaaS vendor's agent via A2A/MCP; no shared governance context | PxER complete for governed side; external decision chain limited to protocol-level metadata |
| **Unmanaged** | Unregistered agent with no protocol identity; detected behaviourally | PxER captures observations only; external chain unknowable |

For outbound interactions (a governed agent calling external systems), the same trust contexts apply in reverse. PxER captures the governed side's decision chain; the external system's transaction record has no back-reference to PxER — two evidence chains that the protocol's integration maturity model progressively connects (L2→L3→L4).

### 7.3 The Conformance Delta as Governance Instrument

The protocol requires every Process Frame to declare each step's intended D/P classification (`CORE-A3-01`) and every PxER to record the actual classification (`CORE-A3-02`). The difference — the conformance delta — concentrates governance value. A step classified D but executed through an LLM reveals a cost leak or implementation gap. A step classified P but consistently producing identical outputs is a candidate for deterministic treatment. This delta is queryable across every process instance, making governance a continuous, evidence-based feedback loop rather than a static declaration.

The protocol defines four conformance statuses per step — MATCH, MISMATCH, UNVERIFIABLE, and DEGRADED (`CORE-A2-03`) — and five mismatch types that classify the specific divergence: `D_intended_P_executed` (D-classified ran through LLM — escalate), `P_intended_D_executed` (P-classified ran deterministically — promotion candidate), `D_intended_UNVERIFIABLE` (intended D, path unobservable — record gap), `P_intended_UNVERIFIABLE` (intended P, path unobservable — record gap), and `CONFLICT` (declared execution path contradicts statistical evidence — classification integrity alert, APP-3 S3) (`CORE-A2-04`). Each carries distinct governance implications and escalation requirements. When `conformance_status` is DEGRADED (governance layer unavailable during execution), `mismatch_type` is null — no assessment was possible (`CORE-A2-04a`). DEGRADED steps are subject to retrospective reconciliation per APP-3 SEC-S7-01. The conformance evidence method — TELEMETRY, STATISTICAL, or UNVERIFIABLE — records how the status was determined.

### 7.4 Minimum Viable Implementation for Entity Correlation

For implementors planning their first entity correlation deployment, the minimum data captured per governed process step to enable inferred-mode correlation (`EC-15`) is small:

| Data Point | Required? | Source |
|:---|:---|:---|
| System identifier (which system executed the step) | Yes | Already in Process Frame (`CORE-A0-01`) |
| Operation type (read / write / approve / notify) | Yes | Already in Process Frame |
| 1–3 key entity field values from the step's response payload | **Yes — this is the new capture** | Declared via `EC-01` entity extraction; recorded in PxER via `EC-07` |
| Completion timestamp | Yes | Already in PxER (`CORE-A2-01`) |
| D/P classification | Recommended | Already in Process Frame |
| Compliance scope (C0–C4) | Recommended | Already in Process Frame |

With only this minimum stack, inferred-mode correlation delivers co-occurrence analysis, anomaly detection, undocumented business rule discovery, and cross-system process mining. Entity type labels (`EC-02`) are optional but strongly recommended — trivial to add at L2 (derivable from MCP tool schemas) and they materially improve downstream usability for analytics and copilot queries. Everything beyond the minimum — full entity attribute sets, integration flow references, semantic federation — is enrichment that raises actionability but is not required for core value.

### 7.5 The P→D and Entity Correlation Structural Parallel

The protocol's promotion pipeline (`CORE-A8-01`) and APP-4's entity correlation inference engine are structurally parallel. Both observe PxER evidence, detect stable patterns, validate confidence, and feed candidates into a governed promotion or registry. P→D promotion converts stable P-track behaviour into deterministic rules; entity correlation inference converts stable co-occurrence into a durable cross-system entity relationship. They share pattern detection, confidence scoring, and drift monitoring infrastructure — entity correlation is an additional consumer of the evidence plane, not a parallel system. Implementations that get one right earn substantial architectural leverage for the other.

---

## Appendix A — Protocol Requirement Cross-Reference by Implementor Role

This appendix maps APP-2, APP-3, and APP-4 requirements to implementor roles. **APP-5 §4 is the authoritative source for per-role requirement matrices. This table is a simplified summary for navigation purposes.** The authoritative inter-document mapping is APP-IG-02.

| Implementor Role | Primary Capabilities | Key APP-2 Requirements | APP-3 Security Domains | APP-4 Entity Requirements |
|:---|:---|:---|:---|:---|
| **Governance Orchestrator** | A0, A1, A2, A3, A4, A5, A6, A7 | CORE-A0-01 through A7-03, CORE-CP-01 through CP-04 | S1 (Frame Integrity), S4 (Evidence Integrity), S5 (HITL Security), S7 (Orchestration Integrity), S14 (Entity Correlation Security) | EC-01, EC-07 (extraction into PxER), EC-15 (inferred correlation), EC-29 (entity flow verification) |
| **Telemetry Contributor (L3 ERP)** | A2 (contribute), A3 (report), A6 (engagement) | CORE-A2-03, A3-02, A6-02, CORE-L3-01 | S4 (Evidence Integrity — contributor authentication, SEC-S4-04 tiered trust), S12 (L1 Security) | EC-01 (entity extraction), EC-07 (entity refs in PxER) |
| **Agent Builder Platform** | A1, A3, A7 | CORE-A1-01 through A1-04, A3-01, A7-01 through A7-03 | S2 (Transport), S13 (Agent Identity — SEC-S13-01, SEC-S13-02) | — (no direct entity correlation obligations) |
| **Enterprise Deployer** | A0, A5, A9, A10, A11 | CORE-A0-01, A5-01, A9-01 through A9-03, A10-01, A11-01, CORE-CP-01 through CP-04 | S6 (Compliance Validation), S10 (Tenant Isolation) | EC-31 (stable correlations as promotion candidates), EC-32 (entity drift as A10 signal), EC-33 (entity-enriched process intelligence) |
| **Field Deployment** | — (activation phase) | — | S1-04 (source provenance), S5-05 (jurisdiction tier), S12-01 (PII gate), S12-02 (credential vault), XX-01 (TAO) | — |
| **ISV (L2/L3)** *(not a formal APP-5 role — represents a common implementation pattern combining TC + AB obligations)* | A1 (consume), A2 (contribute at L3), A7 | CORE-A1-01, A2-03, A7-01 | S2 (Transport), S4 (Evidence Integrity) | EC-01 (entity extraction) |

For the complete requirement-level mapping, see APP-IG-02 (Cross-Reference Matrix).

---

## Appendix B — Glossary

Aligned with APP-2 Appendix E. Terms defined here carry the same meaning as in APP-2.

| Term | Definition |
|:---|:---|
| **Process Frame** | Structured, AI-consumable governed process specification (`CORE-A0-01`) |
| **PxER** | Process Execution Record — governance data + transaction references. Supplements ERP transaction records at L2/L3; primary record at L4 (`CORE-A2-01`) |
| **D/P Classification** | Formal Deterministic/Probabilistic boundary per step (`CORE-A3-01`) |
| **Conformance Delta** | Intended vs. actual D/P per step — primary governance instrument (`CORE-A3-02`, `CORE-A3-03`) |
| **Conformance Status** | MATCH · MISMATCH · UNVERIFIABLE · DEGRADED (`CORE-A2-03`). DEGRADED = governance layer unavailable during execution. |
| **Mismatch Type** | D_intended_P_executed · P_intended_D_executed · D_intended_UNVERIFIABLE · P_intended_UNVERIFIABLE · CONFLICT (`CORE-A2-04`). CONFLICT = declared path contradicts statistical evidence. When DEGRADED, mismatch_type is null (`CORE-A2-04a`). |
| **Conformance Profile** | Preventive · Detective · Retrospective. Declared per scope (`CORE-CP-01`). Partial conformance must be declared (`CORE-CP-04`) |
| **Orchestration Completion Gate** | none · review · attestation. Declared per Frame based on process risk (`CORE-A4-05`) |
| **Telemetry Contribution Protocol** | Standardised event schema by which L3 applications contribute intra-app execution data to PxER assembly (`CORE-L3-01`) |
| **MCP Server Profile** | MCP used as the A1 integration transport (Recommended Pattern, `CORE-A1-04`). Security baseline: APP-3 `SEC-S2-01`. |
| **Trust Boundary Type** | internal · enterprise-external · cross-enterprise-external · unmanaged (`CORE-A2-11`, `CORE-A2-12`) |
| **L1–L4** | Integration maturity: Screen/RPA · API/MCP · App-Enhanced · AI-Native |
| **HITL** | Human-in-the-Loop. Measured quality, not just approval (`CORE-A6-01`) |
| **C0–C4** | Compliance authorship taxonomy: Regulatory → Local Rules (`CORE-A5-01`). C3/C4 apply regardless of process scope |
| **Classification Provenance** | born · extracted_design · earned_runtime · declared · permanent_P (`CORE-A8-01`) |
| **Frame Lifecycle** | Seed → Observed → Validated → Mature (`CORE-A9-01`) |
| **Evidence vs. Telemetry** | Evidence = accountability-grade, retained. Telemetry = debugging-grade, ephemeral (`CORE-A2-06`) |

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 1.10
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-IG-01 — Implementor's Guide.*
