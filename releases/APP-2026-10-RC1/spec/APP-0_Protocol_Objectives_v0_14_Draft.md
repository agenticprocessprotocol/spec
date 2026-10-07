# APP-0

Agentic Process Protocol

## Protocol Objectives

| | |
|:---|:---|
| **Version** | 0.14 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group. |
| **Audience** | Enterprise buyers, auditors, regulators, deployers; implementers seeking outcome-level orientation |
| **Normative status** | Normative. Governed by APP-1. Peer to APP-2, APP-3, APP-4, APP-5 within the constitutional frame (per APP-1 §4). |
| **Companion documents** | APP-1 (Constitution — governs), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles), APP-IG-01 (Implementors Guide), APP-IG-02 (Cross-Reference Matrix), APP-IG-03 (Worked Example), APP-IG-04 (FAQ), APP-IG-05 (Protocol Objectives Realisation and Assurance Guide), APP-R1 (Frame Schema), APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. Version bumps require concurrent manifest regeneration; adding a version to the manifest without concurrent bump of that document, or vice versa, is a release-control defect. |
| **Version-reference convention** | Companion documents cited by name only in body prose. Manifest above is the sole non-historical source for companion versions. Version numbers persist in body prose only for historical claims about specific past changes. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-0 states the outcomes the Agentic Process Protocol makes verifiable for conformant governed processes. It is the enterprise-facing layer of the protocol series.
>
> **Status:** Normative. Requirements expressed using RFC 2119/8174 keywords are binding within the declared scope.
>
> **Authority and precedence:** Governed by APP-1. APP-1 overrides APP-0 on any conflict. APP-5 prevails on conformance-specific matters.
>
> **Use this document for:** Understanding what the protocol makes verifiable at the outcome level; enterprise-buyer orientation; auditor and regulator reference for objective-level outcomes.
>
> **Related documents:** APP-1 (Constitution — governs), APP-2 through APP-5 (realising specifications), APP-IG-05 (objectives realisation and regulatory crosswalks).

---

## 1. Preamble

APP-0 states the outcomes the Agentic Process Protocol makes verifiable for conformant governed processes. It is the enterprise-facing layer of the protocol series: buyers, auditors, regulators, and enterprise deployment teams read APP-0 to understand *what* the protocol makes possible; implementors read APP-2 through APP-5 to understand *how*.

**Coordinated protocol suite.** The Agentic Process Protocol is specified across a coordinated suite of six normative documents (APP-0 through APP-5) and five informative implementation guides (APP-IG-01 through APP-IG-05). Each normative document has a distinct role:

| Document | Role |
|:---|:---|
| **APP-0 (this document)** | States the outcomes the protocol makes verifiable — the enterprise-governance objectives that motivate the technical specification |
| **APP-1 (Constitution)** | Governs the entire suite. Establishes normative principles, Priority of Constituencies, protocol invariants, and precedence rules |
| **APP-2 (Core Technical Specification)** | Defines the 12 protocol capabilities (A0 through A11) and the four integration maturity levels (L1 through L4) |
| **APP-3 (Security Architecture)** | Defines security requirements across 14 domains (S1 through S14) plus cross-cutting principles (SEC-XX-01 through SEC-XX-05) |
| **APP-4 (Entity Correlation Architecture)** | Defines entity correlation requirements (EC-01 through EC-47, plus EC-01a) for cross-system entity tracking |
| **APP-5 (Conformance Profiles)** | Defines role-based conformance requirements for the five participant roles (Governance Orchestrator, Telemetry Contributor, Agent Builder Platform, Enterprise Deployer, Field Deployment) at each L-level |

**Where APP fits.** APP addresses a governance gap that neither model-behaviour codes nor enterprise system integration standards address. Model-behaviour codes (frontier-lab responsible-scaling policies, model provider terms of service, developer conduct guidelines) govern how AI models are built and how they should behave. Enterprise system integration standards (API contracts, EDI, iPaaS conventions) govern how systems exchange data. APP occupies the layer between these: **the governed execution of enterprise processes when AI is part of the execution path**. This layer requires its own protocol because neither model-behaviour codes nor integration standards can, on their own, provide the evidence of authorised action, independent verification, bounded agency, execution-time evidence, and governed change that enterprise process governance requires.

**Enterprise reader path.** Enterprise buyers and auditors seeking to understand what APP provides read this document first, then APP-IG-05 (Protocol Objectives Realisation and Assurance Guide) for realisation depth including regulatory crosswalks (EU AI Act, ISO/IEC 42001, NIST AI RMF, NIST SP 800-207 Zero Trust). Technical implementors read APP-1 (Constitution) → APP-2 (Core Specification) → APP-3/4 (Security/Entity Correlation) → APP-5 (Conformance Profiles). Implementor guidance is in APP-IG-01 (Implementor's Guide) with worked examples in APP-IG-03.

**Structural properties inherited from APP-1.** Four properties of APP-1's protocol invariants (§5) surface at the outcome level and matter for enterprise-buyer decision-making. These are restated at §5 of this document.

---

## 2. Enterprise Governance Objectives

The protocol makes five outcomes verifiable for conformant governed processes. Each Objective is a Required Outcome per APP-1 Article 4 — the protocol's realising specifications (APP-2 through APP-5) exist to make each Objective demonstrable through evidence, not merely asserted through documentation.

### O-1 — Authorised Action

**Statement.** Every action taken by an AI system within a governed process is traceable to a principal authorised to take it, at the scope required by the action, and the authority provenance is verifiable independently of the acting agent.

**Enterprise meaning.** When an AI agent acts on behalf of a person, department, or system within a governed process, the enterprise can demonstrate — to an internal auditor, an external assessor, or a regulator — who authorised the action, what the scope of that authorisation was, and that the authorisation chain was not constructed after the fact. Authority flows from named principals through delegation chains whose composition can be inspected; peer messages between agents do not qualify as authority sources; recovery paths preserve the accountability chain.

**Load-bearing property.** Actions without traceable, verifiable authority provenance are non-conformant regardless of whether they produced desirable outcomes.

### O-2 — Independent Verification

**Statement.** Governance-critical judgments made by AI systems within a governed process are verifiable by an independent path, and disagreement between the primary and independent paths triggers documented human review.

**Enterprise meaning.** For decisions the enterprise treats as compliance-critical or otherwise high-stakes, the protocol makes the verification path a structural property, not an operational discipline. Classification decisions, safety-event validations, coordination-pattern analyses, and compositional-authority validations are subject to cross-family independent verification with signed attestation records that assessors can review without hidden training-data facts. Where independent verification is structurally unavailable, escalation to human review is the mandated fallback.

**Load-bearing property.** A governance-critical judgment supported only by the same reasoning path that produced it is not verified for O-2 purposes.

### O-3 — Bounded Agency

**Statement.** AI agent authority within a governed process is bounded by construction — by declared scope, by delegation-chain depth and composed reach, by substrate isolation, by minimum safe-state transitions on detected severe events, and by compliance-tiered graceful degradation on governance-layer unavailability.

**Enterprise meaning.** Agents operating within governed processes cannot expand their reach through composition, cannot use shared substrates as covert authority channels, cannot continue privileged actions past detected severe events without human acknowledgement, and cannot bypass compliance controls when infrastructure degrades. Bounded agency is expressed as a structural property enforced by the runtime, not as a policy expectation.

**Load-bearing property.** An agent operating at nominally correct authority scope but whose composed effect exceeds any single principal's scope, or whose runtime state permits privileged action after a severe event, violates O-3 regardless of correct per-step behaviour.

### O-4 — Execution-Time Evidence

**Statement.** Governance evidence for a governed process is assembled during execution — not reconstructed from event logs after the fact — and captures the intended track, actual execution, HITL engagement quality, recovery events, and compliance status at the granularity required for retrospective verification.

**Enterprise meaning.** The protocol's evidence record (PxER — Process Execution Record) is a durable, immutable, queryable record produced as processes execute. It captures what the enterprise needs to demonstrate governance: D/P classification per step (was this rule-based or judgment-dependent?), conformance status per step (did execution match intent?), HITL engagement fidelity (did the human genuinely engage or merely acknowledge?), recovery events (when the primary path failed, what was done and by whom?), and compliance evidence (did compliance-critical controls activate at the required tier?). Recovery evidence, added in v5.9, closes the "what happened between the failure and the resolution" gap that traditional event logs typically leave.

**Load-bearing property.** Evidence that requires reconstruction from disparate event logs after the fact is not O-4 conformant, because such reconstruction cannot demonstrate that the evidence existed at the moment of execution or that it has not been silently altered since.

### O-5 — Governed Change

**Statement.** Every change to the governed process itself — Frame mutations, D/P classifications, compliance constraints, autonomy modes, adaptive-learning artefacts, governance-control configurations — is authenticated, versioned, and subject to human approval at the tier appropriate to the change's governance impact.

**Enterprise meaning.** The protocol treats the *governance layer's own configuration* as governance-critical. Feature flags that weaken safety controls, autonomy-mode changes that convert Supervised steps to Autonomous ones, promotion of P-track patterns to D-track rules, adaptive-learning updates to the classification models — all pass through elevated review with security-delta analysis. The class of failure this addresses is silent governance weakening: an operator, a feature flag, or an autonomous system quietly relaxing a control that then permits downstream harm. O-5 makes governance-layer configuration change a first-class conformance surface.

**Load-bearing property.** Changes that alter the governed process without leaving an authenticated, versioned, human-approved record are non-conformant regardless of whether the changes were made in good faith.

### Objectives synthesis

The five Objectives together answer five distinct enterprise-governance questions:

| Question the enterprise must answer | Objective |
|:---|:---|
| Who authorised this action, and can I verify it? | O-1 Authorised Action |
| Can I trust the AI's judgment on compliance-critical decisions? | O-2 Independent Verification |
| Are the AI's actions bounded, and does the bounding hold under pressure? | O-3 Bounded Agency |
| What evidence do I have that the process actually executed as governed? | O-4 Execution-Time Evidence |
| How do I know the governance layer itself hasn't been silently weakened? | O-5 Governed Change |

The Objectives are not aspirational. Each is realised by specific normative requirements in APP-2 through APP-5, mapped in §3.

---

## 3. Realisation Mapping

Each Objective is realised by a set of normative requirements across APP-2 (CORE-*), APP-3 (SEC-*), and APP-4 (EC-*). The table below is the **curated authoritative subset** — the load-bearing requirements that make each Objective demonstrable. The exhaustive reverse mapping (every requirement → Objective it realises) is maintained in APP-IG-02 §7.2.

### 3.1 Load-bearing requirements per Objective

**O-1 Authorised Action.**
- **CORE**: A0-01 (mandatory Frame fields including identity), A4-01 (three-layer accountability chain), A4-02 (PxER execution attribution distinguishing human / AI-on-behalf / autonomous), A4-04 (orchestration accountability fields), A4-06 (recovery-decision accountability chain), A5-01 (compliance-authorship marker), A5-02 (Frame encoding + PxER evidence)
- **SEC**: S2-01 (MCP conformance profile), S2-06 (compositional authority accumulation cap), S13-01 (session-contextual identity binding), S13-02 (session token PxER retention), S13-03 (authority-provenance invariant — peer messages non-qualifying as elevation sources)
- **EC (indirect — identity-scoping contribution to authorisation integrity)**: EC-38 (cross-tenant entity type leakage prevention — prevents an agent authorised for tenant A from acting on tenant B's entities), EC-39 (entity field path exposure minimisation — bounds the scope over which an agent's authorisation applies). These EC controls do not themselves *establish* authority; they *bound the scope* over which authority applies, which is a necessary property of O-1 in multi-tenant deployments. Enterprises without multi-tenant scope may treat EC-38/EC-39 as O-4 confidentiality controls; the O-1 assignment reflects their role in multi-tenant authorisation-scope integrity.

**O-2 Independent Verification.**
- **CORE**: A3-06 (independent D/P verification for compliance-critical steps), A6-01 (measured HITL quality, not just approval), A6-02 (engagement record minimum fields), A6-03 (engagement-fidelity marker with normative vocabulary), A6-05 (canary injection)
- **SEC**: S3-01 (independent D/P verification), S3-02 (adversarial D/P test suite), S3-06 (D-track scope validation at request time), S3-07 (cross-family independent verification, attestation-based), S5-01 (LITL defence), S5-03 (engagement authenticity detection), S8-03 (dual-human for C0/C1 promotions)
- **EC (independent-source verification of entity claims)**: EC-22 (five-outcome reconciliation with divergent-status escalation) — where entity_extract is declared and a populated MDM source is connected, EC-22 provides an independent verification path for the entity claims an AI system made, with `divergent` status raising an operational signal that a governance-critical AI judgment (about which entities a step affected) disagrees with a populated authoritative source. This is O-2 realisation for the entity-claim class of governance-critical judgment. Enterprises without entity correlation deployed may treat EC-22 as O-5 governed-change signal for the correlation-drift class; the O-2 assignment reflects its role in independent verification of entity-scope claims where correlation is deployed.

**O-3 Bounded Agency.**
- **CORE**: XX-01 (compliance-tiered graceful degradation), XX-02 (degradation security)
- **SEC**: XX-01 (Temporal Activation Ordering), XX-02 (substrate isolation), XX-03 (authority reduction on uncertainty, RP), XX-04 (adversarial verification obligation), XX-05 (minimum safe-state transition on detected severe events), S2-05 (delegation chain depth cap, RP), S2-06 (compositional authority accumulation), S5-06 (agent-initiated safety-event channel), S6-05 (recovery-path enforcement-tier invariant), S7-01 (independent signed execution trace), S7-02 (compliance-tiered degradation), S7-03 (coordination-pattern detectability), S13-03 (authority-provenance invariant)
- **EC**: EC-34 (graceful degradation to non-correlated mode), EC-35 (correlation-unavailable behaviour)

**O-4 Execution-Time Evidence.**
- **CORE (Required Outcomes — load-bearing)**: A2-01 (immutable record during execution), A2-02 (step field minimums), A2-03 (7-field conformance schema), A2-04 (mismatch type enum including CONFLICT), A2-04a (DEGRADED status semantics), A2-05 (conformance by maturity level), A2-06 (evidence vs telemetry distinction), A2-08a (mandatory orchestration P-track fields), A2-10 (three verification dimensions), A2-11 (cross-enterprise boundary observation), A2-12 (unmanaged: observed invocation only), A2-13 (recovery evidence schema, 7 fields including sequence / clarified v5.10), A2-14 (recovery outcome controlled vocabulary, 5 values), A3-02 (record actual execution track), L3-01 (L3 telemetry schema)
- **SEC (Required Outcomes — load-bearing)**: S4-01 (async evidence verification with declared SLA), S4-02 (evidence tier classification), S4-03 (contributor authentication OAuth 2.1 DPoP), S4-04 (tiered trust for new contributors), S4-05 (write-path authentication across six enumerated artifact classes), S4-06 (evidence-record erasure reconciliation with assurance enumeration)
- **EC (Required Outcomes — load-bearing)**: EC-07 (entity_refs in PxER when entity_extract present), EC-08 (entity ref minimum fields), EC-11 (instance-level correlation block), EC-40 (PxER entity_refs security), EC-41 (entity data access controls), EC-42 (entity references inherit hash chain integrity)
- **EC (Recommended Patterns — supporting)**: EC-09 (extraction method provenance, RP — a confidence-supporting field enriching but not gating O-4 evidence assembly), EC-10 (confidence indicators, RP — signal quality enrichment for correlation but not required for evidence assembly). These are enrichment mechanisms; O-4 conformance does not require them, but implementations that support entity correlation SHOULD include them for downstream correlation quality.

**RO vs RP distinction.** The bulleting above distinguishes Required Outcomes (load-bearing for Objective demonstrability under APP-1 Article 4) from Recommended Patterns (supporting mechanisms that enrich but do not gate demonstrability). An implementation that satisfies all Required Outcomes above realises the Objective; an implementation that also satisfies the Recommended Patterns realises the Objective at a higher fidelity but is not more conformant. This distinction applies to all Objectives: any RP-marked requirement in the load-bearing lists above is a supporting mechanism, not a floor. The RO/RP status of each ID is authoritatively classified in the source specification: APP-2 uses `Required Outcome` / `Recommended Pattern`; APP-3 uses `Required Outcome` / `Recommended Pattern` / `Informative Guidance`; APP-4 uses `Required Outcome` / `Recommended Pattern`. A future revision may add the suffix inline; it is deferred here to avoid duplicating status information the source specifications already carry authoritatively.

**Curated-mapping exclusion note.** The load-bearing lists per Objective above are the **curated subset** for enterprise-buyer orientation, not the exhaustive traceability. EC-43 through EC-47 (entity retention, populated-mode imports, correlation registry isolation, entity data access controls) are relevant enabling and security controls but are not curated as load-bearing for O-1/O-4 in this §3.1 subset. Their exhaustive indirect relationships to Objectives are maintained in APP-IG-02 §7.2. Similarly, EC-17 (global inference promotion audit) affects governed change (O-5) via its five-field governance audit but is not curated in the O-5 load-bearing list; APP-IG-02 §7.2 reverse mapping is authoritative for the full inventory. The curated subset trades exhaustiveness for enterprise-buyer legibility.

**APP-3 Recommended Pattern reclassifications.** SEC-S1-05 (semantic validation on D/P reclassification) and SEC-S10-03 (AI red team) are classified as Informative Guidance in APP-3 per APP-1 Article 3 constitutional discipline. Neither is in this §3.1 curated load-bearing list.

**O-5 Governed Change.**
- **CORE**: A3-01 (declare intended D/P per step), A3-03 (MISMATCH triggers review), A3-04 (task-level vs orchestration-level P), A8-01 (classification provenance, 5 values), A8-02 (promotion evidence fields), A8-03 (three promotion outcomes), A8-04 (Frame transition events), A9-01 (lifecycle states), A9-02 (transition recording), A10-02 (conformance report on declared cadence), A10-04 (evidence integrity before drift signals)
- **SEC**: S1-01 (signed Frame mutations), S1-02 (mutation provenance chain), S1-03 (monotonic version enforcement), S1-04 (source document provenance), S6-01 (constraint completeness / negative space), S6-02 (compliance exception re-validation on constraint change), S6-03 (autonomy-mode change elevated review C0/C1), S6-04 (governance-control integrity monitoring), S6-05 (recovery-path enforcement-tier invariant), S8-01 (promotion evidence integrity gate), S8-02 (promotion evidence exclusivity), S8-04 (promotion velocity integrity), S9-01 (evidence integrity before advisory), S9-02 (governance-weakening elevated approval), S9-03 (evidence-vs-learning quarantine)

### 3.2 Recovery evidence perimeter cross-note

Wave 1 protocol extensions (APP-2 and APP-3) add recovery evidence as a first-class governance surface. Recovery events touch O-1 (recovery decisions carry accountability chains — CORE-A4-06), O-3 (recovery paths cannot invoke controls at a lower enforcement tier than the primary path — SEC-S6-05), and O-4 (recovery invocations produce structured evidence attached to the original step's PxER record — CORE-A2-13/14). The recovery-evidence perimeter is completed by three sibling controls that together prevent silent governance weakening:

| Control | Prevents downgrade by |
|:---|:---|
| SEC-XX-01 (Temporal Activation Ordering) | *Ordering* — controls active before data flows begin |
| SEC-S6-04 (Governance-control integrity monitoring) | *Configuration change* — configuration changes routed through elevated review |
| SEC-S6-05 (Recovery-path enforcement-tier invariant) | *Recovery-path selection* — recovery paths cannot silently route through lower-strictness gates |

Together, these three controls form a **core perimeter** against the class of governance-weakening pressure vectors documented in adjacent SRE and incident-response literature. The perimeter is "core" in the sense that these three controls address the three classes of downgrade vector explicitly modelled in the APP threat model (ordering, configuration change, recovery-path selection); it is not "complete" in the sense that no threat model formally enumerates all possible downgrade vectors — implementations should treat the three controls as necessary but not sufficient for defence against silent governance weakening, and layer implementation-specific detection and response mechanisms on top per APP-3 SEC-XX-04's adversarial-verification obligation.

### 3.3 Traceability status

Traceability mapping is maintained in APP-IG-02 §7 and is reconciled against the current normative indexes at each release. The **combined active requirement count** for APP-2 (68 CORE-*) + APP-3 (67 SEC-*) + APP-4 (48 EC-*) is **183 requirements**. SEC-S1-05 and SEC-S10-03 are classified as Informative Guidance per APP-1 Article 3 constitutional discipline; they remain in the SEC-* namespace but are outside the active normative requirement inventory. Of the 183 active requirements, APP-IG-02 §7.2 maps the load-bearing subset to Objectives; the remaining requirements are STRUCT (structural / naming / interoperability plumbing without direct Objective realisation — 38 IDs per §7.3) or INFO (informative classification on load-bearing IDs — 3 IDs per §7.3).

**Coverage claim.** APP-IG-02 restores the traceability inventory and the role × L-level coverage analysis. Enterprise buyers and auditors reviewing APP-0 should treat the requirement-count arithmetic as reconciled (see APP-IG-02 §7.3 reconciliation table) and the role × Objective coverage as classified into direct realisation / configuration responsibility / enabling control / not applicable (APP-IG-02 §7.6.2). Per-Objective classification decisions may be revised in v1.0 based on stakeholder review.

Every Objective has applicable realising requirements at every declared role × L-level scope where the role's dimension responsibilities require it — verified in APP-IG-02 §7.6 against APP-5 §4 per-role matrices. Structural asymmetries (some Objectives concentrated in Governance Orchestrator + Enterprise Deployer; others in Governance Orchestrator + Telemetry Contributor) reflect the dimension applicability structure per APP-5 §2.2, not missing requirements.

---

## 4. Priority of Constituencies

Aligned with APP-1 §2. When design decisions, trade-offs, or conflicts arise, the protocol resolves them according to the following hierarchy. Higher-ranked concerns take precedence over lower-ranked concerns.

- **Regulatory and compliance obligations.** External legal and regulatory requirements are boundary conditions. The protocol must not create structures that make compliance harder to achieve or demonstrate. This is not a constituency but a constraint that overrides all other considerations.

- **Process participants.** Humans who are accountable for governed process outcomes — approvers, decision-makers, and those affected by process decisions. Their safety, informed consent, and ability to exercise genuine oversight take precedence over system convenience.

- **Enterprise process owners.** Organisations deploying governed processes. Their ability to audit, control, and improve processes across vendor boundaries takes precedence over implementor convenience.

- **Platform implementors and vendors.** AI platforms, enterprise system vendors, and system integrators building conformant implementations. Implementation feasibility matters, but not at the expense of governance integrity.

- **Protocol authors.** Specification writers. Theoretical elegance and architectural purity yield to practical needs of all parties above.

*Enterprise interpretation.* APP-0's Objectives are framed from the enterprise process owner's perspective (constituency 3) — the level at which governance is deployed, audited, and improved — while remaining subject to regulatory constraint (constituency 1) and to process-participant safety (constituency 2). Where an Objective realisation would ease implementor burden (constituency 4) at the cost of participant oversight quality or enterprise auditability, APP-1's precedence rule resolves against the ease.

---

## 5. Structural Framing

Four properties of APP-1's protocol invariants (APP-1 §5) surface at the outcome level and matter for enterprise-buyer decision-making. These are the properties an enterprise deployer relies on when evaluating whether APP will remain stable across implementations, vendors, and time.

### 5.1 Selected structural properties

**(i) Cross-vendor operation is the protocol's design target; single-vendor adoption is a permitted deployment topology.** APP is designed for governance across system boundaries — between independent vendors, between a vendor's own products, between an enterprise's systems and third-party AI, and between subsystems within one vendor's estate that participate in distinct governance roles. Enterprises adopting APP with a single vendor receive the same governance standard as multi-vendor deployments; the protocol does not offer a reduced governance standard for internal deployments, and single-vendor adopters are not credited with cross-vendor interoperability by adoption alone.

**(ii) Governance evidence is assembled during execution, not reconstructed retrospectively.** The evidence property that makes the protocol enforceable is that PxER is a durable record produced *while processes execute*. Evidence reconstructed from event logs after the fact cannot demonstrate that the evidence existed at the moment of execution, nor that it has not been silently altered. This property is inherited from APP-1 §5 invariant (b) and is what makes O-4 (Execution-Time Evidence) verifiable rather than aspirational.

**(iii) Human oversight quality is measured, not merely required.** The protocol treats the presence of a human checkpoint as necessary but not sufficient. Where HITL engagement is required, the protocol requires evidence that the human exercised genuine judgment — measured via engagement-fidelity markers (CORE-A6-03 with normative vocabulary `behavioural-measured` / `acknowledgement-only`), engagement authenticity detection (SEC-S5-03), and canary injection (CORE-A6-05). This property is inherited from APP-1 §5 invariant (d).

**(iv) The same protocol governs at every integration maturity level. What varies is evidence richness, not the governance standard.** L1 through L4 represent progressively deeper integration between the governance layer and the systems being governed. At L1, the enterprise governance layer instruments processes at the screen / RPA layer; at L4, the systems being governed are AI-native and produce governance evidence structurally. What changes across L1–L4 is the *fidelity* of evidence the protocol can capture; what does not change is the governance standard that must be met to claim conformance. This property is inherited from APP-1 §5 invariant (e). **Observability qualifier.** The invariant preserves the required governance *outcome* per Objective; the available observation mechanisms, evidence completeness, and consequently the scope that can be independently demonstrated vary by L-level and declared role. At L1, per-invocation conformance status is typically UNVERIFIABLE (no direct execution observability); at L2 the same status applies unless statistical inference is deployed; at L3 intra-application telemetry supports MATCH/MISMATCH determination per invocation; at L4 systems produce governance evidence structurally. The Objectives are the same at every L-level; the mechanisms by which each is demonstrated — and therefore the residual evidence limitations that must be declared in the conformance scope — differ.

### 5.2 Why these four (and not the other three)

APP-1 §5 contains seven invariants. The four surfaced above are the ones that matter directly to enterprise buyers and auditors evaluating APP adoption. The other three APP-1 invariants are equally normative but sit closer to the technical realisation and are addressed in §3 Realisation Mapping rather than restated here:

| APP-1 §5 invariant | Handled in APP-0 |
|:---|:---|
| Rule-based vs judgment-dependent step distinction (D/P classification) | §3 O-4 requirements (A3-01, A3-02, A3-04) |
| Governed feedback loops without autonomous governance modification | §3 O-5 requirements (A9-*, A10-*, S9-03) |
| Security controls active before governed data flows (Temporal Activation Ordering) | §3 O-3 requirements (SEC-XX-01) |

Enterprise buyers who need to understand these three invariants at the outcome level should read APP-IG-05 §12 (Evidence Richness at L1–L4) for the cross-level treatment and APP-IG-01 §6.3 for the CISO-oriented security framing.

### 5.3 What these properties mean for procurement

Together, the four surfaced properties tell an enterprise buyer four things about APP as an adoption target:

1. **Vendor portability** — the enterprise is not locked into any single vendor for governance; changing vendors preserves the governance standard.
2. **Audit defensibility** — the evidence that supports governance claims is contemporaneous with execution and durable, not reconstructed under time pressure.
3. **Oversight authenticity** — the enterprise can demonstrate that human oversight was substantive, not performative.
4. **Adoption gradient** — the enterprise can start at any integration maturity level and improve evidence richness incrementally without changing the governance standard it commits to.

---

## Appendix A — Recommended Commitment Profile Template (Informative)

## Appendix A — Recommended Commitment Profile Template (Informative)

This appendix is informative. It provides a template that enterprise deployers, ISVs, or platform vendors can adapt when publishing an APP conformance commitment. The template is organised as a **Universal Floor** (commitments any conformant implementation makes) and **Extended Tier** commitments (additional commitments an implementation may make for compliance-critical or regulated deployments).

**Applicability qualifier.** Every commitment below applies only where the underlying requirement is applicable to the adopter's declared role × L-level scope per APP-5 §4. For example, SEC-XX-05 (minimum safe-state transition) is Universal Floor for O-3 for roles that run agents at runtime (Governance Orchestrator, Agent Builder Platform) at all L-levels; for roles that configure or verify safe-state policy without runtime action (Enterprise Deployer, Field Deployment), the commitment applies as configuration/verification obligation rather than runtime honouring. Adopters publishing their conformance commitment should qualify each commitment with the role × L-level scope in which it applies.

Adopters are encouraged to publish their commitments at the granularity that matches their audit surface. APP-IG-05 §11 provides illustrative language and worked examples.

### A.1 Universal Floor

| Commitment area | Universal Floor commitment |
|:---|:---|
| **Authorised action (O-1)** | Every action within a governed process is attributable to a named principal per APP-3 SEC-S13. Peer messages are not accepted as authority elevation sources. Delegation-chain composed reach is bounded per APP-3 SEC-S2-06. |
| **Independent verification (O-2)** | Compliance-critical D/P classifications are validated by an independent classification path per APP-3 SEC-S3-01. Cross-family independence for governance-critical judgment surfaces is supported by signed attestation per APP-3 SEC-S3-07, or falls back to human review via SEC-S5-06. |
| **Bounded agency (O-3)** | Runtime authority reduction on detected severe events per APP-3 SEC-XX-05 (minimum safe-state transition — v3.11 strengthened with transition timing, prohibited actions in safe state, re-authorisation exit condition, and eight-field PxER schema). Substrate isolation per SEC-XX-02. Compliance-tiered graceful degradation per CORE-XX-01/02 and SEC-S7-02. |
| **Execution-time evidence (O-4)** | PxER assembled during execution per APP-2 A2. Immutable, queryable, linked to Frame version. Conformance schema (7 fields) recorded per step. Recovery evidence (schema per CORE-A2-13, vocabulary per CORE-A2-14) recorded when recovery paths are invoked. |
| **Governed change (O-5)** | Frame mutations signed per APP-3 SEC-S1-01. Governance-control configuration changes routed through elevated review per SEC-S6-04. Autonomy-mode changes on compliance-critical steps subject to elevated review per SEC-S6-03. |
| **Security perimeter** | Temporal Activation Ordering (SEC-XX-01), adversarial verification obligation (SEC-XX-04), evidence-vs-learning quarantine (SEC-S9-03), evidence-record erasure reconciliation with declared assurance class (SEC-S4-06). |
| **Conformance transparency** | Conformance profile declared per scope (CORE-CP-01). Multi-profile per scope permitted (CORE-CP-02). Partial conformance explicitly declared per CORE-CP-04 — no silent non-conformance. |

### A.2 Extended Tier

Extended Tier commitments layer on top of the Universal Floor. Adopters targeting regulated deployments (BFSI, healthcare, jurisdictional compliance regimes) or high-assurance postures may commit to any subset of the following:

| Extended commitment | Realising requirements |
|:---|:---|
| **Dual-human approval for C0/C1 P→D promotion** | APP-3 SEC-S8-03 (base) + BFSI domain profile elevation to MUST |
| **Cross-family independent verification universally** | APP-3 SEC-S3-07 across all governance-critical judgment surfaces, not only D/P classification |
| **Behavioural HITL measurement universal** | CORE-A6-03 `behavioural-measured` marker on all HITL records (no `acknowledgement-only` fallback) |
| **Recovery path enforcement-tier parity guaranteed** | APP-3 SEC-S6-05 with no `bypassed` outcomes permitted on compliance-critical (C0/C1) steps |
| **Compositional authority halt at threshold** | APP-3 SEC-S2-06 with published composition-detection thresholds and re-authorisation SLA |
| **Adaptive baseline provenance transparency** | APP-3 SEC-S7-03 with published baseline lifecycle, rollback capability, and provenance records |
| **Jurisdictional privacy tier lock** | APP-3 SEC-S5-05 with declared per-jurisdiction tier and no override |
| **Enhanced retention beyond regulatory floor** | APP-3 SEC-S14-09 with declared retention exceeding the regulatory minimum for the applicable compliance scope |

### A.3 Commitment publication guidance

Commitments are meaningful to auditors and regulators only when they are published, versioned, and testable. Adopters SHOULD publish commitments as machine-readable conformance statements (per APP-5 CONF-D-06), including:

- Implementation name and version
- Role(s) declared (per APP-5 §1.2 — Governance Orchestrator, Telemetry Contributor, Agent Builder Platform, Enterprise Deployer, Field Deployment)
- L-level per scope
- Universal Floor commitments (typically identical across scopes)
- Extended Tier commitments per scope
- Testable criteria references (APP-5 §5)
- Assessment authority (self-assessed / peer-assessed / third-party-assessed)

---

## Appendix B — Layer Composition (Informative)

## Appendix B — Layer Composition (Informative)

This appendix is informative. It orients enterprise buyers to how APP composes with the other layers of an AI-enabled enterprise stack. APP-IG-05 §3 provides the extended framework cross-walk for adopters mapping APP to their existing governance frameworks.

### B.1 Three architectural layers

Enterprise deployments of AI-enabled processes involve three architectural layers. Each layer has its own concerns and its own set of standards, codes, or protocols. APP occupies one of these layers and interfaces with the other two.

| Layer | Concerns | Standards / codes / protocols | Where APP fits |
|:---|:---|:---|:---|
| **Model layer** | Model behaviour, training data, alignment, safety properties of the model itself | Frontier-lab responsible-scaling policies (Anthropic RSP, OpenAI Preparedness Framework, Google DeepMind Frontier Safety Framework), model provider terms of service, developer conduct guidelines | APP is downstream of the model layer. APP does not certify model behaviour; it governs how the model's outputs are used in enterprise processes. |
| **Governance layer** | Process governance, evidence, oversight quality, cross-system compliance, entity correlation | **APP** (this specification). ISO/IEC 42001 as the AI Management System frame within which APP-conformant implementations operate. NIST AI RMF as risk-management guidance. | This is APP's home layer. APP-2 through APP-5 define the governance mechanism; APP-0 states the outcomes. |
| **Product layer** | Enterprise applications, ERPs, agent builders, orchestration runtimes, transaction systems | ERP vendors (SAP, Oracle, Workday, etc.), agent frameworks (proprietary and open), MCP and A2A as interoperability protocols at this layer | APP is upstream of the product layer. APP-conformant implementations may run *within* an ERP or an agent framework; the product remains vendor-defined but participates in a governed process. |

### B.2 Layer composition properties

The three layers compose without merging responsibilities:

- **Model-layer failures** (jailbreaks, unauthorised model actions, novel-capability emergence) are not made harmless by governance-layer compliance. Enterprises adopting APP still depend on model-layer safety guarantees from their model providers.
- **Governance-layer failures** (governance evidence not captured, oversight not verified, recovery not recorded) are not repaired by product-layer robustness. A rock-solid ERP that emits no governance evidence is non-conformant regardless of its operational reliability.
- **Product-layer failures** (integration bugs, data quality issues, UX confusion) are not evidence of governance failure per se, but they are subject to governance-layer detection through PxER conformance signalling (MISMATCH, DEGRADED, CONFLICT).

### B.3 Why the layer distinction matters for procurement

Enterprise procurement decisions often conflate the three layers. A common mistake is to evaluate an AI-enabled enterprise system entirely on its model-layer properties ("Is the model safe?") or entirely on its product-layer properties ("Is the ERP reliable?") — leaving governance-layer capability unassessed. APP conformance is the procurement instrument for the governance layer specifically. An enterprise buying an APP-conformant implementation is buying governance-layer capability; it must separately evaluate the model-layer properties of any model the implementation uses and the product-layer properties of any product the implementation runs within.

---

## Appendix C — Regulatory Framework Considerations (Informative)

## Appendix C — Regulatory Framework Considerations (Informative)

This appendix is informative and orientation-only. It indicates how the five APP-0 Objectives relate to widely-referenced regulatory frameworks. **Detailed technical crosswalks are in APP-IG-05 §10** (Article-by-Article for EU AI Act; Clause-by-Clause for ISO 42001; Function-by-Function for NIST AI RMF; Tenet-by-Tenet for NIST SP 800-207).

### C.1 Objective-level indicative mappings

| Objective | EU AI Act (indicative) | ISO/IEC 42001 (indicative) | NIST AI RMF (indicative) |
|:---|:---|:---|:---|
| **O-1 Authorised Action** | Articles 14 (human oversight), 26 (deployer obligations) | Clause 8 (operation), A.9 (data for AI systems), A.10 (information for interested parties) | Govern-1, Manage-2 |
| **O-2 Independent Verification** | Articles 15 (accuracy, robustness, cybersecurity), 43 (conformity assessment) | Clause 9 (performance evaluation), A.6 (AI risk assessment) | Measure-1, Measure-2 |
| **O-3 Bounded Agency** | Articles 9 (risk management), 15 (accuracy, robustness, cybersecurity), 16 (obligations of providers) | Clause 6 (planning), A.5 (leadership commitment for AI), A.6 (risk assessment) | Govern-4, Manage-4 |
| **O-4 Execution-Time Evidence** | Articles 12 (record-keeping), 20 (technical documentation) | Clause 7.5 (documented information), Clause 8.1 (operational planning and control) | Measure-2, Measure-3, Manage-3 |
| **O-5 Governed Change** | Articles 17 (quality management system), 16 (provider obligations), 43 (conformity assessment) | Clause 6 (planning of changes), Clause 8.1, Clause 9.3 (management review) | Govern-3, Govern-5 |

### C.2 Zero Trust alignment (NIST SP 800-207)

APP-3 aligns with NIST SP 800-207 Zero Trust principles at the governance-layer scope. Session-scoped identity binding (SEC-S13-01), per-request authorisation (SEC-S3-06), continuous authenticity verification (SEC-S5-03), and least-privilege authority reduction (SEC-XX-03 with MUST floor SEC-XX-05) are the load-bearing APP requirements that realise Zero Trust tenets at the AI-agent boundary.

### C.3 Assurance limits

This appendix remains orientation-only. **APP conformance evidence may support obligation assessment; it does not establish legal compliance.** Regulatory obligations are jurisdiction- and sector-specific, evolve independently of the protocol, and require legal interpretation appropriate to the specific deployment. Adopters engage qualified counsel and applicable conformity assessment bodies for authoritative compliance determinations. The mappings above and in APP-IG-05 §10 are technical starting points for that legal work, not substitutes for it.

**Legal-review status.** The regulatory crosswalks in APP-IG-05 §10 (including EU AI Act Articles, ISO 42001 Clauses, NIST AI RMF Functions, NIST SP 800-207 Tenets) have **not** received the legal-review verification identified as OI-18 in APP-IG-02 §6. Enterprise buyers and auditors using this Appendix or APP-IG-05 §10 for procurement decisions should treat the technical mappings as adopter starting points and independently verify against current regulatory text as interpreted by qualified counsel. Specific dates and enforcement schedules cited in APP-IG-05 §10 (including EU AI Act Annex III enforcement timing) are drawn from public regulatory sources but have not been independently verified for this appendix's purposes.

---

## Appendix D — Document Status (Transitional)

*This appendix is transitional scaffolding for the pre-Working-Group draft.*

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 0.14
**Normative status:** Normative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-0 — Protocol Objectives.*
