# APP-IG-03

Agentic Process Protocol

## Worked Example — End-to-End Governed Process Deployment

| | |
|:---|:---|
| **Version** | 1.11 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Audience** | ERP vendor architects, SI delivery teams, hyperscaler platform teams, enterprise governance teams, conformance assessors |
| **Normative status** | This document is **informative**. It does not define requirements. It illustrates how the protocol manifests in a real deployment. |
| **Companion documents** | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles), APP-IG-01 (Implementor's Guide), APP-IG-02 (Cross-Reference Matrix), APP-R1 (Frame Schema), APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |
| **Version-reference convention** | Companion documents cited by name only in body prose. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-IG-03 is an informative worked example of the Agentic Process Protocol. It illustrates an end-to-end governed process across roles, L-levels, and evidence-emission points.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. Examples illustrate possible governed-process scenarios; they do not prescribe a product architecture, deployment topology, implementation mechanism, or legal conclusion.
>
> **Use this document for:** End-to-end concrete illustration of protocol application, evidence-emission mapping, state-machine walkthrough.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** APP-2/3/4 (illustrated requirements), APP-5 (illustrated conformance obligations).

---

## How to Read This Document

This document is an Implementation Guide — one of the specification types defined in APP-1. It contains no normative requirements. It walks through a single governed process deployment from design through operation, showing where each protocol capability, security control, and entity correlation requirement applies.

The walkthrough follows three deployment phases:

| Phase | Duration | Protocol Capabilities Illustrated |
|:---|:---|:---|
| **Phase 1 — Define & Design** | Weeks 1–6 | A0 (Process Frame), A1 (Integration Surface), A3 (D/P Classification), A5 (Compliance), EC-01–EC-06 (Entity Extraction), SEC-S1 (Frame Integrity) |
| **Phase 2 — Build & Integrate** | Weeks 7–12 | A2 (PxER), A4 (Accountability), A6 (HITL Quality), A7 (Parity), EC-07–EC-11 (Entity References), SEC-S2–S7 (Transport, Evidence, HITL, Orchestration), SEC-S14 (Entity Correlation Security) |
| **Phase 3 — Operate & Evolve** | Ongoing | A8–A11 (Promotion, Lifecycle, Drift, Intelligence), EC-15–EC-33 (Correlation, Registry, Learning), SEC-S8–S9 (Promotion, Feedback Integrity) |

Requirement IDs in brackets (e.g., `CORE-A0-01`, `SEC-S1-01`, `EC-07`) reference the originating normative specification. See APP-IG-02 for cross-document mappings.

---

## 1. Scenario

### 1.1 Context

A 5,000-person financial services firm deploys governed AI-assisted onboarding across six enterprise systems. The deployment operates at **Level 2 (API/MCP)** — the governance orchestrator connects to enterprise applications via API/MCP but does not modify their internal architecture.

### 1.2 Enterprise Landscape

| System | Role | Agent Capability |
|:---|:---|:---|
| **HRIS** (Workday) | Employee records, compensation, benefits | AI agents handle basic admin. Onboarding = manual workflows. |
| **IT Service Management** (ServiceNow) | Laptop provisioning, access tickets | AI agents handle Tier 1 tickets. Provisioning = semi-automated. |
| **Procurement** (SAP Ariba) | Equipment ordering, vendor management | AI handles PO queries. PO creation = manual approval chain. |
| **Identity/Access** (Azure AD) | SSO, RBAC, MFA | Automated provisioning exists but manually triggered. |
| **Collaboration** (Microsoft Teams) | Communication, buddy coordination | AI scheduling. Buddy matching = entirely informal. |
| **Compliance** (GRC tool) | Background checks, regulatory training | Fully manual. Vendor API exists but no agent integration. |

### 1.3 The Governance Gap

Onboarding takes 14–21 days. A coordinator manages it via email, spreadsheets, and six system logins. No single view. No SLA tracking. No visibility into process breakdowns. Two recent compliance findings: new hires accessed systems before background checks cleared — a C0/C1 violation (`CORE-A5-01`).

### 1.4 Participant Roles in This Deployment

| APP-5 Role | Who Plays It |
|:---|:---|
| **Governance Orchestrator** | The governance platform managing Process Frame, PxER assembly, and learning loop |
| **Agent Builder Platform** | LangGraph (cross-system orchestration), Joule Studio (SAP steps), ServiceNow (ticket routing) |
| **Telemetry Contributor** | Not applicable at L2 — no L3 intra-app telemetry in initial deployment |
| **Enterprise Deployer** | The financial services firm's HR Operations and Compliance teams |
| **Field Deployment** | The SI team performing initial setup, credential provisioning, and TAO verification |

---

## 2. Phase 1 — Define & Design (Weeks 1–6)

### 2.1 Process Elicitation and Process Frame Construction (A0)

The governance orchestrator conducts AI-assisted elicitation — interviewing the onboarding coordinator, HR business partner, IT provisioning lead, and compliance officer. Each interview is synthesised into process fragments. Process mining outputs are ingested as complementary inputs.

The output is a **Process Frame** (`CORE-A0-01`) — a structured, AI-consumable specification with mandatory fields per step: step identifier, executing system, intended D/P classification, dependency chain, and accountability owner.

**Illustrative Process Frame (9 steps):**

| Step ID | Step Name | System | D/P | HITL Level | Compliance | Dependencies |
|:---|:---|:---|:---|:---|:---|:---|
| ONB-001 | Create employee record | Workday | D | None | — | — |
| ONB-002 | Initiate background check | GRC | D | None | C1 | — |
| ONB-003 | Submit IT provisioning | ServiceNow | D | None | — | ONB-001 |
| ONB-004 | Create equipment request | SAP Ariba | D | Approval (>$2K) | — | ONB-001 |
| ONB-005 | Provision system access | Azure AD | D | None | C1 | ONB-002 (must pass) |
| ONB-006 | Interpret background check | Governance platform | P | Required (senior HR) | C1 | ONB-002 (result) |
| ONB-007 | Assign onboarding buddy | Governance platform | P | Confirmation | — | ONB-001 |
| ONB-008 | Generate training plan | Governance platform | P | Review | — | ONB-001 |
| ONB-009 | First-week experience check-in | Governance platform | P | Escalation only | — | ONB-001 |

**D/P classification** (`CORE-A3-01`) is the governance anchor. Steps ONB-001 through ONB-005 are deterministic — rule-based, zero inference. Steps ONB-006 through ONB-009 are probabilistic — requiring human judgment, AI-assisted reasoning, or contextual inference. The distinction governs oversight requirements per APP-1 invariant (a).

**Entity extraction declarations** (`EC-01`) are configured on the Process Frame. For this deployment:

| Step | Entity Type | Field Path | Entity Role |
|:---|:---|:---|:---|
| ONB-001 | `person` | `response.employee_id` | primary_key |
| ONB-001 | `cost_centre` | `response.cost_centre_code` | context_key |
| ONB-003 | `person` | `payload.employee_id` | primary_key |
| ONB-005 | `person` | `response.user_principal_name` | primary_key |
| ONB-005 | `org_unit` | `response.access_groups` | context_key |

Entity extraction enables cross-system entity correlation (`EC-07`) — the protocol discovers that ONB-001 (Workday), ONB-003 (ServiceNow), and ONB-005 (Azure AD) all act on the same person without requiring MDM integration (`EC-15`, inference-first principle).

### 2.2 Frame Integrity Controls (SEC-S1)

Before the Process Frame is published:

- Every Frame mutation carries a digital signature linked to the submitter's identity (`SEC-S1-01`). The compliance officer's governance overlay changes and the architect's step definitions are independently signed.
- The mutation provenance chain is append-only (`SEC-S1-02`) — every change, authoriser, and classification is a verifiable link.
- Monotonic version enforcement (`SEC-S1-03`) prevents rollback to weaker constraints — if the compliance officer elevated ONB-005 to require security officer co-approval, that elevation cannot be silently reversed.
- Source document provenance (`SEC-S1-04`) extends the chain to the SOPs and policy documents from which the Frame was constructed.

Entity extraction declaration changes (adding/modifying `entity_extract` on a step) are also Frame mutations (`EC-01a`) subject to the same signing and versioning controls.

### 2.3 Compliance Encoding (A5)

The enterprise deployer configures compliance per step. The normative protocol surface is a **two-value authorship marker** (`CORE-A5-01`): each compliance constraint declares whether it is `external-mandated` (enterprise-immutable) or `enterprise-authored` (customer-overridable). This deployment uses the **C0–C4 taxonomy** as its internal authorship model — a worked granularity that projects onto the marker (see below):

| Step | C0–C4 (internal model) | Marker (protocol surface) | Rationale |
|:---|:---|:---|:---|
| ONB-002 | C1 (platform control pattern) | `external-mandated` | Background check initiation enforces a C0 regulatory control — enterprise cannot weaken it |
| ONB-005 | C1 (platform control pattern) | `external-mandated` | System access blocked until background check clears — hard gate, not enterprise-overridable |
| ONB-006 | C1 (platform control pattern) | `external-mandated` | Background check interpretation for financial services — regulatory |
| ONB-004 | C3 (corporate policy) | `enterprise-authored` | Procurement approval thresholds are enterprise policy — customer-owned and overridable |

**Projection (C0–C4 → marker).** The marker encodes *overridability*, not authorship: {C0, C1, C2} → `external-mandated` (the enterprise cannot weaken them — C1/C2 enforce or package C0 obligations, so they inherit C0's immutability in the weakening direction, even though they are implementation-authored rather than regulator-authored); {C3, C4} → `enterprise-authored` (customer-owned). The customer-overridable boundary falls between C2 and C3. A conformant implementation may use any internal granularity provided it projects unambiguously onto the two values.

> **Note — two normative constructs, one set of labels.** C0–C4 here is the *worked authorship* model (informative). Two separate normative constructs project from it: (1) the **A5 overridability marker** (`external-mandated`/`enterprise-authored`, APP-2 §3.6) shown above; and (2) the **compliance-criticality ordinal** (four-point: C0>C1>C2>C3C4, APP-2 §6) that degradation, promotion, and verification requirements threshold against. The marker has two values (overridability); the ordinal has four ordered points (criticality). The ordinal collapses C3 and C4 into one enterprise band — no normative requirement distinguishes them; the C3-vs-C4 split is *authorship* granularity, real only in this informative worked model. (Retention, SEC-S14-09, is a third axis again — obligation-source — and thresholds against neither construct.) This deployment's C1 background-check gates are both `external-mandated` (overridability) *and* high on the criticality ordinal (fail-closed under degradation) — the constructs answer different questions about the same step.

**Constraint-inheritance integrity** (`CORE-A5-03`). An `enterprise-authored` constraint (e.g. a C3 procurement override) MUST NOT weaken an inherited `external-mandated` constraint (e.g. the C1 background-check gate on ONB-005) unless the Frame carries a governed-exception record bearing an **authority reference**. In this deployment, no such exception exists — the C1 gates are hard.

The compliance officer also configures **jurisdictional privacy tiers** (`SEC-S5-05`) — this deployment uses Tier B (UAE PDPL-equivalent: disclosure + proportionality for engagement telemetry).

**Negative space detection** (`SEC-S6-01`) validates that every compliance-scoped step carries a declared constraint. A Frame for a financial services onboarding process where ONB-005 carries no constraint at all would be flagged as an unresolved compliance risk.

### 2.4 Integration Surface (A1)

The Process Frame is published via the A1 integration surface (`CORE-A1-01`) — bidirectional:

- **Outbound:** The governance orchestrator pushes governed step definitions to agent builders. Joule Studio receives SAP step specifications; ServiceNow receives ticket creation specs; LangGraph consumes the full DAG with D/P routing and HITL gates.
- **Inbound:** When the SAP team modifies a Joule agent for an intra-SAP step, the change passes through the governance gate (`CORE-A1-02`). Changes with complete governance attributes merge directly; changes missing attributes route to enrichment before becoming authoritative.
- **Notification:** When the compliance officer updates a governance overlay (e.g., elevates ONB-005 access provisioning to require security officer co-approval), the Frame change propagates automatically to all connected builders.

The integration surface requires mutual TLS, OAuth 2.1, and DPoP (`SEC-S2-01`). Agent Cards are signed (`SEC-S2-02`) and session integrity is enforced (`SEC-S2-03`).

### 2.5 Temporal Activation Ordering (SEC-XX-01)

The **field deployment** team ensures security controls are active before governed data flows begin. This is the highest-risk deployment phase — PII classification gates (`SEC-S12-01`), credential vaults (`SEC-S12-02`), Frame signing infrastructure, and evidence verification endpoints must all be operational before the first PxER record is accepted. The field deployment team verifies TAO compliance as part of activation (`SEC-XX-01`).

---

## 3. Phase 2 — Build & Integrate (Weeks 7–12)

### 3.1 D-Track Execution and PxER Assembly (A2)

For each process instance, the governance orchestrator assembles an immutable PxER record (`CORE-A2-01`) during execution — not retrospectively. Every step record carries: step identifier, executing system, timestamp, and transaction reference to the source system (`CORE-A2-02`).

**Illustrative PxER step record for ONB-003 (IT provisioning):**

```
step_id:                    ONB-003
executing_system:           servicenow
timestamp:                  2026-04-15T08:23:14Z
transaction_reference:      INC0042917  (ServiceNow ticket ID)
dp_classification_intended: D
dp_classification_actual:   null  (L2 — not observable per-invocation)
conformance_status:         UNVERIFIABLE  (L2 default)
conformance_evidence_method: UNVERIFIABLE
trustBoundaryType:          enterprise-external
mismatch_type:              null

entity_refs:
  - entity_type: person
    system_key: workday::WD-2026-04291
    extraction_method: api_response
    entity_role: primary_key

evidence_tier:              L2-verified  (SEC-S4-02)
verification_status:        pending → verified  (SEC-S4-01)
```

At L2, `dp_classification_actual` may be null — the governance orchestrator knows the intended classification but cannot observe the execution engine directly (`CORE-A2-05`). When per-invocation observation is not possible, `conformance_status` defaults to `UNVERIFIABLE` and `conformance_evidence_method` is `UNVERIFIABLE`. Where the implementation performs cross-Frame statistical inference on classification distributions, evidence method becomes `STATISTICAL` and conformance_status becomes `MATCH` or `MISMATCH` per the inference result; where inference is inconclusive, both fields return to `UNVERIFIABLE`.

**Entity references** (`EC-07`, `EC-08`) are populated from the entity extraction declarations configured in Phase 1. The person entity (Workday worker ID) appears in the PxER step record for ONB-003 even though the step executed in ServiceNow — cross-system entity traceability without MDM.

### 3.2 P-Track Evidence and HITL Quality (A4, A6)

For P-track steps (ONB-006 through ONB-009), the governance orchestrator captures richer evidence.

**ONB-006 — Background Check Interpretation:**

A copilot structures information for the HR partner: risk assessment, precedent lookup, policy guidance, confidence scoring. The copilot never makes the decision — it assists. The human decides.

**HITL approval surfaces are generated from independently verified data, not agent-produced content** (`SEC-S5-01`). Agent reasoning is displayed as advisory — clearly labelled AI-generated, visually separate. This prevents LITL (Lies-in-the-Loop) attacks where malicious content embedded in documents the agent reads could surface on approval screens as legitimate recommendations.

**Engagement quality measurement** (`CORE-A6-01`, `CORE-A6-02`): The PxER records decision, duration, and evidence reviewed — not just "approved." This measures whether the human exercised genuine judgment or rubber-stamped. Canary injection (`CORE-A6-05`, defined in APP-2) verifies oversight quality with cryptographically randomised known items.

**Engagement-fidelity marker** (`CORE-A6-03` — MUST): Every ONB-006 HITL record carries an `engagement_fidelity_marker` field populated by the approval surface at decision time (not reconstructed post-hoc). Per APP-2 §3.7 CORE-A6-03, the marker takes one of two values at minimum: `behavioural-measured` (the partner opened the Decision Surface, reviewed the precedent-lookup panel and confidence scoring, made a deliberate decision — measured by minimum surface-time threshold + interaction signals on the precedent-lookup and risk-assessment widgets; this is the value used when the ONB-006 flow can measure engagement directly at the approval surface) or `acknowledgement-only` (engagement signal reconstructed from acknowledgement without behavioural measurement — e.g., the partner acknowledged the case in the upstream HRIS but did not surface the Decision Surface itself; permitted at Lightweight engagement, NOT permitted at Content Review level which ONB-006 uses; use of `acknowledgement-only` where behavioural measurement was possible is non-conformant). An implementation MAY additionally distinguish sub-values within these two classes (e.g., `unable_to_verify` where engagement-tooling unavailable or per-jurisdiction telemetry suppression prevents measurement); such extensions are not part of the normative interop vocabulary and MUST map to one of the two normative values in exchanged PxER records. **Failure handling.** Where a HITL record is missing the required marker, the implementation records the conformance/evidence failure according to the A2 schema and applicable APP-5 profile — this is an implementation-defined evidence-quality failure, not a `DEGRADED` state. `DEGRADED` per APP-2 CORE-A2-04a denotes governance-layer unavailability, not a malformed HITL record. If working-group discipline determines that hard rejection on missing marker is the correct behaviour, APP-2 and APP-5 should add a normative rule for that; until then, the implementation records the failure and the ONB-006 outcomes with a missing marker are still not elevated as P→D promotion candidates by the closed-loop intelligence (§4.3) — the marker discipline prevents the promotion pipeline from rewarding rubber-stamping.

**Three-layer accountability** (`CORE-A4-01`) per step:

| Layer | ONB-006 Evidence |
|:---|:---|
| **Intent** | Frame version, compliance officer who configured C1 constraint |
| **Execution** | HR partner identity, session-contextual token (`SEC-S13-01`) |
| **Oversight** | Engagement duration, evidence reviewed, confidence at decision, justification text, **`engagement_fidelity_marker` per `CORE-A6-03` (one of `behavioural-measured` / `acknowledgement-only` per APP-2 normative vocabulary)** |

**Session-contextual identity** (`SEC-S13-01`): Each agent session carries a token encoding autonomy level, delegation chain, HITL engagement level, and risk classification — enabling per-session audit traceability.

### 3.3 Degradation Behaviour (CORE-XX-01, SEC-S7-02)

The enterprise deployer declares degradation behaviour per step:

| Step | Compliance Scope | If Governance Unavailable |
|:---|:---|:---|
| ONB-002 | C1 | **Fail-closed** — background check initiation blocks |
| ONB-005 | C1 | **Fail-closed** — system access blocks |
| ONB-004 | C3 | **Fail-open** — procurement continues ungoverned, PxER gap flagged |
| ONB-001 | — | **Fail-open** — employee record creation continues, gap flagged |

An independent signed execution trace (`SEC-S7-01`) runs alongside PxER — recording Frame version, steps executed, HITL checkpoints invoked, and D/P track. Asynchronous reconciliation detects step omission, phantom steps, sequence violations, and HITL bypass.

### 3.4 Entity Correlation at L2 (EC-15, EC-22)

With sufficient process volume (typically 20–50 instances), the entity correlation engine begins discovering relationships:

**Inferred correlation example:** The person entity `workday::WD-2026-04291` co-occurs with `servicenow::USR0042917` across multiple onboarding instances. The correlation registry (`EC-25`) records:

```
entity_a:               workday::WD-2026-04291
entity_b:               servicenow::USR0042917
mode:                   inferred
confidence:             0.87
evidence_count:         34
scope:                  process-scoped  (this Onboarding Frame only)
first_observed:         2026-04-15
last_observed:          2026-06-22
reconciliation_status:  inferred_only (EC-22)
```

The correlation is process-scoped. `scope: global` promotion would require cross-Frame evidence — the correlation observed in Frames other than the one that discovered it — plus the five-field EC-17 governance audit (audit event, principal, timestamp, evidence bundle reference, promotion rationale). Multiple instances of one Frame are not cross-Frame evidence and cannot alone justify `scope: global`.

The `inferred_only` status means no populated source (MDM) has confirmed this correlation — it is a discovery signal (`EC-24`). If the enterprise later connects an MDM source (`EC-19`, `EC-43`), reconciliation produces `aligned` or `divergent` status.

**Entity correlation security** (`SEC-S14-01` through `SEC-S14-08`): Correlation data is tenant-isolated. Cross-tenant queries are prohibited. Cross-enterprise entity references are limited to boundary-observable data. The populated source (if connected) authenticates before contributing correlation data.

### 3.5 Recovery Evidence (CORE-A2-13, CORE-A2-14, CORE-A4-06, SEC-S6-05)

Onboarding processes hit recovery paths routinely: background check services time out, provisioning APIs return transient errors, downstream system updates lag, exception approvals get denied. Wave 1 protocol extensions in APP-2 and APP-3 define protocol-standardised recovery evidence so that these events don't disappear into implementation-specific error logs.

Three worked scenarios below illustrate the recovery evidence discipline: (a) a repeat recovery with monotonic sequence, (b) a self-healed transient with observation evidence, (c) a CONFLICT case where declared and observed classifications agreed but statistical evidence contradicted both.

#### 3.5.1 Scenario A — Repeat recovery with monotonic sequence

**Setup.** ONB-002 (background check initiation) is a C1 D-track step. The step invokes a background-check API that returns a transient rate-limit error. The implementation's D-track retry rule fires automatically.

**First recovery invocation** (attached to the ONB-002 step's PxER record):

```
recovery_evidence: {
  path_class:     "retry",
  initiator:      "D-track",
  authorized_by:  "gov-control::retry-policy-C1-transient",
  outcome:        "failed",
  evidence_refs:  ["exception::rate-limit-2026-06-15T09:42:11Z"],
  latency_ms:     342,
  sequence:       1
}
```

The first retry failed. The step remains blocked (C1 fail-closed). D-track escalates automatically to a second retry with a longer backoff.

**Second recovery invocation** (appended to the same step's PxER record, not a new step):

```
recovery_evidence: {
  path_class:     "retry",
  initiator:      "D-track",
  authorized_by:  "gov-control::retry-policy-C1-transient",
  outcome:        "recovered",
  evidence_refs:  ["exception::rate-limit-2026-06-15T09:42:11Z"],
  latency_ms:     1867,
  sequence:       2
}
```

The step's PxER record now carries two `recovery_evidence` blocks with `sequence: 1` and `sequence: 2`. The step identifier is unchanged; recovery events did not become new steps. The `authorized_by` field references the governance-control identity (`gov-control::retry-policy-C1-transient`) per SEC-S6-04, not a generic label like "system" — a generic label would be non-conformant.

Downstream: the auditor reconstructing this incident sees exactly two retry attempts, the timing of each, and the path from initial failure to eventual success. The recovery event was governance-critical (C1 compliance-scoped) and its evidence is preserved at protocol-standardised granularity across the two-vendor stack.

#### 3.5.2 Scenario B — self_healed with observation evidence

**Setup.** ONB-005 (system access provisioning) is a C1 D-track step. The step queries ServiceNow to confirm the provisioning ticket completed. The initial query returns a stale "pending" status due to an eventually-consistent replication lag between ServiceNow's read replicas. Before D-track can invoke a retry, the next scheduled poll (external to the recovery mechanism) observes the status has advanced to "completed" — the ticket had actually completed but the initial read hit a stale replica.

**Recovery evidence**:

```
recovery_evidence: {
  path_class:     "retry",
  initiator:      "D-track",
  authorized_by:  "gov-control::consistency-check-C1",
  outcome:        "self_healed",
  evidence_refs:  [
    "telemetry::servicenow-replica-lag-2026-06-15T09:47:22Z",
    "observation::status-transition-2026-06-15T09:47:24Z"
  ],
  latency_ms:     2103,
  sequence:       1
}
```

In this scenario no human or agent recovery decision occurred; the transient state self-corrected. The `self_healed` outcome retains detection/control provenance and observation evidence rather than a principal record — `evidence_refs` includes an observation record (`observation::status-transition-2026-06-15T09:47:24Z`) demonstrating that the state genuinely self-corrected rather than being an unrecorded autonomous decision by the D-track layer. The exemption from the A4 accountability chain is an example-level inference from the CORE-A2-14 vocabulary; where APP-2 adopts an explicit rule for `self_healed` handling in a future revision, this scenario should cross-reference it directly.

If the observation record were absent, this recovery would be non-conformant as `self_healed`. The protocol-compliant fallback would be to record `outcome: recovered` with `initiator: D-track`, preserving the accountability chain via the governance-control identity referenced in `authorized_by`.

Downstream: the auditor sees a transient condition that self-corrected within ~2 seconds, with observation evidence proving the state transition. If a similar transient recurs frequently over time (drift signal per CORE-A10-02), the drift signal may promote an infrastructure investigation into ServiceNow replica lag — governance evidence feeding operational reliability improvement without the accountability chain being falsely invoked for events that had no decision.

#### 3.5.3 Scenario C — CONFLICT case: statistical evidence contradicts agreed classification

**Setup.** ONB-004 (procurement item selection, C3-scoped) is declared as D-track in the Process Frame (`dp_classification_intended: D`) because the enterprise deployer configured it as a rule-based catalog lookup. The execution telemetry reports `dp_classification_actual: D` — both sides agree. At L3, however, the statistical inference layer observes that the execution latency distribution, the response pattern, and the field-population variance for this step over the past 200 instances are inconsistent with deterministic rule execution — the distribution matches an LLM-mediated selection path, not a D-track lookup.

This is a **CONFLICT** case: intended and actual both say D, but statistical evidence at L3 contradicts both.

**PxER conformance schema**:

```
dp_classification_intended:   D
dp_classification_actual:     D
execution_engine:             "procurement-catalog-lookup-v3.2"
conformance_status:           MISMATCH
mismatch_type:                CONFLICT
conformance_evidence_method:  STATISTICAL
trustBoundaryType:            internal
```

Per APP-2 CORE-A2-04 clarification: on CONFLICT detection, `conformance_status` is set to MISMATCH regardless of whether intended and actual agreed. CONFLICT is not a compound of the other four mismatch types — it is a classification-integrity signal indicating that neither the intended nor the actual field reflects what actually executed.

**Governance action**: escalated as a classification-integrity alert to APP-3 SEC-S3 (Classification Integrity). The Governance Orchestrator's SEC-S3-01 independent classification path is invoked. The cross-family verification attestation (SEC-S3-07, attestation-based per APP-3) is confirmed — verifier and verified agents are structurally distinct model families with signed independence attestation. The implementation invokes its human-review workflow to determine whether the D-track classifier is drifting or the P-track evidence has quality issues; where the classification integrity alert also raises an agent-initiated safety event, SEC-S5-06 (agent-initiated safety-event channel per APP-3 §4.5) provides the required channel. Human review determines whether:

- (a) the execution engine `procurement-catalog-lookup-v3.2` has been silently replaced with an LLM-mediated version (implementation-side integrity failure);
- (b) an upstream configuration mutation misclassified the step (Frame-integrity failure);
- (c) statistical evidence is itself in error (measurement failure).

The step's downstream P→D promotion pipeline is blocked until the CONFLICT resolves, per SEC-S8-01.

Downstream: the CONFLICT case is exactly the failure mode that "both fields agree" would silently obscure without the CONFLICT semantic. The classification-integrity signal preserves auditability of the divergence even when the surface-level fields reported nothing wrong.

**Cross-tier interaction with recovery**. Note that the CONFLICT in scenario C does not itself invoke a recovery path — CONFLICT is a classification-integrity signal that gates promotion and triggers investigation, not a runtime recovery event. However, if the human review determines that scenario C requires rolling back the affected procurement instances, that rollback would be recorded as recovery events on each affected step's PxER record with `path_class: undo`, `initiator: human`, and the human authoriser's identity in `authorized_by`, satisfying CORE-A4-06's requirement that recovery decisions carry a three-layer accountability chain.

---

## 4. Phase 3 — Operate & Evolve (Ongoing)

### 4.1 Process Intelligence (A11)

This deployment derives the following from the PxER corpus (`CORE-A11-01` — Recommended Pattern: the protocol mandates no specific intelligence outputs; these are this implementation's chosen set): bottleneck identification (ONB-004 procurement is the slowest step), exception pattern analysis (ServiceNow misroutes cluster on the "Analyst" role category), cost attribution (per step, per D/P track), and promotion candidate surfacing. The mineable substrate these draw on — per-step event fields and process-instance linkage — is the normative requirement (`CORE-A2-01`/`A2-02`); *which* analyses an implementation runs on it is differentiation.

**Entity-enriched intelligence** (`EC-33`) transforms analysis from structural to actionable: "Employee entity `person::WD-2026-04291` experienced a 48-hour delay at ONB-004 because the cost centre entity `cost_centre::CC-1234` was assigned to an approval chain that requires VP sign-off for >$5K" — not just "Step ONB-004 was slow."

### 4.2 Drift Detection (A10)

The governance orchestrator monitors the following drift signal types (`CORE-A10-01` — Recommended Pattern post-DR-02; the normative requirement is the divergence report on declared cadence, `CORE-A10-02`, plus entity-correlation drift via `EC-32`). This deployment's chosen signal set:

| Drift Type | Example in This Deployment |
|:---|:---|
| **Process-level** | Steps skipped or reordered — ONB-005 executing before ONB-002 completes would be a compliance violation |
| **Orchestration quality** | Declining HITL engagement on ONB-006 — HR partner decisions getting faster without corresponding complexity reduction |
| **Intent staleness** | Process Frame specifies 7-day SLA but actual execution averages 5 days — Frame may be stale |
| **Entity correlation drift** (`EC-32`) | Previously stable correlation between Workday cost centre and SAP Ariba cost centre diverging — signals an organisational restructure or integration failure |

Evidence integrity is verified before drift signals are raised (`CORE-A10-04`). Compromised evidence feeding drift detection produces false signals that erode governance trust.

### 4.3 P→D Promotion (A8)

After 3 months of operation, PxER data shows: 97% of "minor employment gap < 12 months for non-fiduciary roles" background check cases are cleared by HR partners with no escalation. This pattern is a P→D promotion candidate (`CORE-A8-01`, provenance: `earned_runtime`).

**Promotion governance:**
- Promotion uses only PxER records with `verification_status: verified` (`SEC-S8-01`). Unverified records are excluded.
- Evidence allocated to this promotion evaluation cannot be reused in another (`SEC-S8-02`).
- Because ONB-006 is C1-scoped, dual-human approval is required (`SEC-S8-03`) — the HR director and the compliance officer must both approve the promotion.
- Any advisory recommending reduced governance (this promotion removes human review for qualifying cases) requires elevated approval (`SEC-S9-02`).

If approved, the classification provenance on the affected Frame step changes from P to D with `provenance: earned_runtime`, recording evidence count, evidence window, validator roles, validation date, and demotion conditions (`CORE-A8-02`). The Frame transition event is recorded in A9 lifecycle (`CORE-A8-04`).

**Stable entity correlations** also surface as P→D candidates (`EC-31`): if the inferred correlation between Workday cost centres and SAP Ariba cost centres is stable across 200+ instances, it is a candidate deterministic mapping rule.

### 4.4 The Living System Loop

Over 6 months:

**Month 1–2:** Baseline established. Process runs. PxER corpus builds. Entity correlations begin converging.

**Month 3:** First P→D promotion — "minor employment gap auto-clear" approved for non-fiduciary roles. ONB-006 now handles 40% of cases deterministically. HR partner time freed for complex cases.

**Month 4:** Entity correlation drift detected (`EC-32` — the normative entity-drift requirement, carried in APP-4): cost centre assignments in Workday no longer match SAP Ariba for a specific department — an organisational restructure propagated to Workday but not to SAP. The drift signal triggers investigation before it causes compliance issues downstream.

**Month 5:** ServiceNow routing issue resolved after governance report surfaces 23% misroute rate for "Analyst" role. ServiceNow's own dashboard never surfaced this — it lacks cross-system process context.

**Month 6:** Customer asks to extend to offboarding. New process domain added using existing connectors and entity patterns. Deployment: 3 weeks (vs. 6 weeks for initial onboarding — reusable patterns compound).

---

## 5. Architecture Summary — What Lives Where (L2 Deployment)

```
┌─────────────────────────────────────────────────────────────────┐
│  GOVERNANCE ORCHESTRATOR                                         │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ A0  Process Frame — E2E governance spec with D/P class.    │ │
│  │ A1  Integration Surface — MCP Server (bidirectional)       │ │
│  │ A2  PxER Engine — assembles E2E record with tx refs        │ │
│  │ A3  D/P Classification — conformance delta monitoring      │ │
│  │ A4  Accountability — three-layer chain per step            │ │
│  │ A5  Compliance — authorship marker per step (C0–C4 model)  │ │
│  │ A6  HITL Quality — engagement measurement, canary inject   │ │
│  │ A7  Parity — identical governance across invocation modes  │ │
│  │ A8  Promotion — P→D pipeline with evidence integrity gate  │ │
│  │ A9  Intent Evolution — Frame lifecycle (Seed→Mature)       │ │
│  │ A10 Drift Detection — divergence report + entity drift     │ │
│  │ A11 Process Intelligence — entity-enriched analytics       │ │
│  │ EC  Entity Correlation Registry — inferred + populated     │ │
│  └──────────────────────┬──────────────────────────────────────┘ │
│                          │                                        │
│  ┌───────────────────────▼────────────────────────────────┐      │
│  │  A1 INTEGRATION SURFACE (mTLS + OAuth 2.1 + DPoP)     │      │
│  │  SEC-S2: Transport security on all connections          │      │
│  │  ↓ Frame → Agent Builders (outbound)                   │      │
│  │  ↑ Builder changes → Frame (inbound via governance gate)│      │
│  │  ↔ Notifications (Frame changes propagate)             │      │
│  └───────────────────────┬────────────────────────────────┘      │
│                          │                                        │
│  ENTERPRISE SYSTEMS (L2 — API/MCP, no internal modification)     │
│  ┌──────────┐ ┌───────────┐ ┌──────────┐ ┌────────────────┐    │
│  │ Workday  │ │ ServiceNow│ │ SAP Ariba│ │ Azure AD       │    │
│  │ REST API │ │ MCP Server│ │ REST API │ │ Graph API      │    │
│  └──────────┘ └───────────┘ └──────────┘ └────────────────┘    │
│                                                                   │
│  SECURITY CONTROLS ACTIVE (SEC-XX-01 TAO verified):              │
│  SEC-S1: Frame signing + provenance │ SEC-S4: Evidence integrity │
│  SEC-S5: HITL security + privacy    │ SEC-S7: Orchestration trace│
│  SEC-S13: Session identity binding  │ SEC-S14: Entity correlation│
│                                                                   │
│  DATA OWNERSHIP:                                                 │
│  Vendor systems own: Business records (transactions, tickets)    │
│  Governance orchestrator owns: Process Frame, PxER corpus,       │
│    D/P classification, governance rules, entity correlation      │
│    registry, process intelligence, P→D promotion library         │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Multi-Role Conformance for This Deployment

Per APP-5 §1.3, conformance is assessed per role. For this deployment:

| Role | Declared L-Level | Dimensions Assessed | Key Obligations |
|:---|:---|:---|:---|
| **Governance Orchestrator** | L2 | Specification, Evidence, Governance, Security, Learning | ~95 RO requirements. All 12 capabilities. S1–S14 at L2. |
| **Agent Builder Platform** (LangGraph) | L2 | Specification, Security | 13 RO. Frame consumption, transport security, session identity. |
| **Enterprise Deployer** | L2 | Governance, Security | 8 RO. C3/C4 policy config, privacy tier, degradation declarations. |
| **Field Deployment** (SI team) | L2 | Security | 5 RO. Source provenance, PII gate, credential vault, TAO. |

If the governance orchestrator also serves as agent builder (a common pattern), conformance is assessed per APP-5 §1.3 multi-role rule: applicable dimensions are the union of both roles.

For stakeholder adoption trajectories and customer starting-point variants beyond this worked example, see APP-IG-01 §5.3–§5.5.

---

## Appendix A — Protocol Requirement Traceability

This appendix maps each element of the worked example to the originating normative requirement. Informative — for implementor orientation.

| Example Element | Protocol Requirement(s) | Source Document |
|:---|:---|:---|
| Process Frame with mandatory fields per step | CORE-A0-01 | APP-2 §3.1 |
| D/P classification per step | CORE-A3-01 | APP-2 §3.3 |
| Entity extraction declarations on Frame steps | EC-01, EC-01a, EC-02 | APP-4 §3.1 |
| Frame signing and version enforcement | SEC-S1-01, SEC-S1-03 | APP-3 §4.1 |
| MCP integration surface (bidirectional) | CORE-A1-01, CORE-A1-02 | APP-2 §3.2 |
| Transport security (mTLS, OAuth 2.1, DPoP) | SEC-S2-01 | APP-3 §4.2 |
| Authorship marker per step (C0–C4 worked model projects onto it) | CORE-A5-01, CORE-A5-02 | APP-2 §3.6 |
| Constraint-inheritance integrity (authority-reference) | CORE-A5-03 | APP-2 §3.6 |
| Compliance-tiered degradation | CORE-XX-01, SEC-S7-02 | APP-2 §6, APP-3 §4.7 |
| PxER assembly during execution | CORE-A2-01, CORE-A2-02 | APP-2 §3.4 |
| Conformance + trust schema (7 fields) | CORE-A2-03 | APP-2 §3.4.1 |
| Evidence vs. telemetry distinction | CORE-A2-06 | APP-2 §3.4.2 |
| Entity references in PxER | EC-07, EC-08 | APP-4 §3.2 |
| Three-layer accountability | CORE-A4-01 | APP-2 §3.5 |
| HITL quality measurement | CORE-A6-01, CORE-A6-02 | APP-2 §3.7 |
| LITL defence on approval surfaces | SEC-S5-01 | APP-3 §4.5 |
| Canary injection for engagement quality | CORE-A6-05 | APP-2 §3.7 |
| Session-contextual identity tokens | SEC-S13-01 | APP-3 §4.13 |
| Independent execution trace + reconciliation | SEC-S7-01 | APP-3 §4.7 |
| Evidence verification with declared SLA | SEC-S4-01 | APP-3 §4.4 |
| Inferred entity correlation | EC-15, EC-16 | APP-4 §3.4.1 |
| Entity correlation registry | EC-25, EC-26 | APP-4 §3.5 |
| Reconciliation (five outcomes) | EC-22, EC-23 | APP-4 §3.4.3 |
| Entity correlation security (tenant isolation) | SEC-S14-01 through SEC-S14-08 | APP-3 §4.14 |
| Drift report on cadence (RO); signal types (RP) | CORE-A10-02 (RO), CORE-A10-01 (RP) | APP-2 §3.11 |
| Entity correlation drift | EC-32 | APP-4 §3.7 |
| P→D promotion with evidence integrity | CORE-A8-01, SEC-S8-01, SEC-S8-02 | APP-2 §3.9, APP-3 §4.8 |
| Dual-human for C0/C1 promotion | SEC-S8-03 | APP-3 §4.8 |
| Process intelligence outputs (RP) | CORE-A11-01 (RP) | APP-2 §3.12 |
| Entity-enriched intelligence | EC-33 | APP-4 §3.7 |
| Stable correlations as P→D candidates | EC-31 | APP-4 §3.7 |
| TAO verification during deployment | SEC-XX-01 | APP-3 §2.1 |

### A.1 A2 State Machine Mapping

Every step-record example in this worked example maps to a specific conformant state in APP-2 CORE-A2-04b's ten-state matrix. Each example was verified to correspond to one of the ten conformant states C1–C10, with no example mapping to a prohibited or contested state.

| Example location | Step / scenario | conformance_status | mismatch_type | evidence_method | A2 state |
|:---|:---|:---|:---|:---|:---:|
| §3.1 (L3 example) | ONB-001 approval step | MATCH | null | TELEMETRY | **C1** |
| §3.1 (L2 example) | ONB-003 ServiceNow provisioning | UNVERIFIABLE | `D_intended_UNVERIFIABLE` (inferred) | UNVERIFIABLE | **C8** |
| §3.5 Scenario A | ONB-002 with repeat recovery | MATCH | null | TELEMETRY | **C1** (recovery evidence orthogonal to state) |
| §3.5 Scenario B | ONB-005 `self_healed` transient | MATCH | null | TELEMETRY | **C1** (self_healed is a recovery outcome, orthogonal to state) |
| §3.5 Scenario C | ONB-004 CONFLICT case | MISMATCH | `CONFLICT` | STATISTICAL | **C7** |

**Note on recovery evidence and A2 state.** Recovery evidence (`CORE-A2-13`, `CORE-A2-14`) is orthogonal to the A2 state machine: recovery describes how a step's execution completed after invoking a recovery path, while the A2 state describes the conformance assessment of the step's D/P outcome. A step can be in state C1 (MATCH, TELEMETRY) and simultaneously carry a `recovery_evidence` block indicating the step took a retry path before completing conformantly. The two are recorded in different PxER fields (`conformance_status`/`mismatch_type`/`conformance_evidence_method` for A2 state; `recovery_evidence` block for recovery record) and are assessed independently.

---

## Appendix B — Glossary

Aligned with APP-2 Appendix E. Terms carry the same meaning as in their originating specifications.

| Term | Definition |
|:---|:---|
| **Process Frame** | Structured, AI-consumable governed process specification (`CORE-A0-01`) |
| **PxER** | End-to-end, immutable execution record — governance data + transaction references (`CORE-A2-01`) |
| **D/P Classification** | Formal Deterministic/Probabilistic boundary per step (`CORE-A3-01`) |
| **Bridge Agent** | A configured agent that fills vendor capability gaps for D-track steps at L2 — governed by the Process Frame, connected via the A1 integration surface |
| **P-Track Copilot** | An AI assistant for P-track steps that structures information and surfaces precedents but does not make decisions — the human decides |
| **Conformance Delta** | Intended vs. actual D/P per step — the primary governance instrument (`CORE-A3-02`) |
| **Entity Correlation** | Cross-system entity tracking from PxER execution data — inferred from co-occurrence or populated from external sources (`EC-15`, `EC-19`) |
| **LITL** | Lies-in-the-Loop: attack class where malicious content in AI-read documents poisons HITL approval surfaces. Mitigated by `SEC-S5-01`. |
| **TAO** | Temporal Activation Ordering: security controls active before governed data flows begin (`SEC-XX-01`) |

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 1.11
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-IG-03 — Worked Example.*
