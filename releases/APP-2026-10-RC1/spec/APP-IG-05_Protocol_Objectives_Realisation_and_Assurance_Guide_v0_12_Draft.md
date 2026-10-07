# APP-IG-05

Agentic Process Protocol

## Protocol Objectives Realisation and Assurance Guide

| | |
|:---|:---|
| **Version** | 0.12 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group. Companion to APP-0. |
| **Audience** | Enterprise buyers, auditors, deployers, implementers, assessors, working-group participants |
| **Normative status** | Informative. Per APP-1 §4, Implementation Guides and Illustrative Reference Artefacts are informative. This document does not create or modify normative obligations. |
| **Companion documents** | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles), APP-IG-01 (Implementors Guide), APP-IG-02 (Cross-Reference Matrix), APP-IG-03 (Worked Example), APP-IG-04 (FAQ), APP-R1 (Frame Schema), APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) — v0.12 is a PATCH adding APP-R1 and APP-R2 to the companion documents, the manifest, and the platform-implementer reading path (§5.3). No change to §1–§4, §6–§11, or §12.1 scope-rebalance rationale. |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. Version bumps require concurrent manifest regeneration across the suite. |
| **Version-reference convention** | Companion documents cited by name only in body prose. Manifest above is the sole non-historical source for companion versions. Version numbers persist in body prose only for historical claims about specific past changes. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-IG-05 is an informative guide for realising and assuring the enterprise governance objectives of the Agentic Process Protocol — how each Objective is read, evidenced, and assured across adopter, assessor, vendor, and buyer roles.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. This document does not create, modify, or override normative requirements in APP-0 through APP-5.
>
> **Use this document for:** Understanding how each Objective is realised across the normative suite; assurance planning; buyer evidence pack preparation; Commitment Profile authorship.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** APP-0 (Objectives realised), APP-1 through APP-5 (realising specifications), APP-IG-02 (detailed requirement traceability).

---

## 1. Purpose and Scope

APP-IG-05 answers the question: *"How does an adopter, assessor, vendor, or buyer read and evidence each APP-0 Objective?"*

It complements APP-0 by carrying the material that supports interpretation, adoption, and assessment without belonging in the normative specification itself:

- **Why the five Objectives.** The design rationale — candidates considered, accepted, merged, or rejected — that APP-0 does not carry in its normative body.
- **How APP-0 fits alongside frontier-lab model-behaviour codes.** The cross-walk comparing APP-0 to the current landscape of frontier-lab commitments, showing where APP composes with them and where it addresses gaps they do not.
- **Worked examples.** How each Objective manifests in real deployment scenarios.
- **Buyer evidence packs.** What questions to ask, what evidence to expect, what "good" looks like at each L-level.
- **Layer composition extended.** Extended explanation of the Model / Governance / Product three-layer architecture.
- **Reading and adoption paths.** Different routes through the APP series for buyers, implementers, assessors, and regulators.

**Not in this guide (v0.11 change).** Technical mapping of APP-0 Objectives and requirement IDs to external standards and regulations (EU AI Act, ISO/IEC 42001, NIST AI RMF, NIST SP 800-207, and others) was carried in §10 through v0.10. From v0.11 that content is out of scope for this guide and is being refactored into a dedicated publication; timing is TBD. See §12.1 for the full change rationale.

This document is informative. Where interpretation conflicts with APP-0 or APP-1 through APP-5, the normative specification prevails.

**Reading order.** Read APP-0 first for the five Objectives at the outcome level. Then read the sections of this guide relevant to your role. Implementers additionally read APP-1 through APP-5. Assessors additionally read APP-5 §4 role matrices and §5 test procedures. Buyers should read §6 (Buyer Evidence Requests) and §8 (Worked Examples) as practical companions to vendor evaluation.

---

## 2. Objective Selection Rationale

This section documents why APP-0 has exactly five Objectives, which candidates were considered and dropped, and how design tensions were resolved. It is transparent record for working-group participants and future amendment discussions.

### 2.1 Selection criteria

APP-0 states the outcomes the protocol delivers. Within the constitutional frame of APP-1, APP-2 through APP-5 realise the Objectives; where realisation requires specification evolution, the gap is flagged rather than the Objective being dropped. Candidates were evaluated against six criteria:

1. **Outcome, not value.** Objectives had to be stateable as testable outcomes ("the system delivers X"), not values ("the system believes in X"). Values drift; outcomes stay honest.
2. **Enterprise buyer legibility.** Each Objective had to answer a question a CIO, CISO, or auditor would actually ask. If a candidate required a five-minute preamble to make sense to an enterprise reader, it was not an Objective.
3. **Realisable in the APP series.** Every Objective must be realisable as testable requirements in APP-2, APP-3, or APP-4 with conformance testing in APP-5 — either currently drafted or realisable through amendment. Where realisation requires APP-2..5 amendment, the gap is recorded; the outcome is not dropped. This preserves anti-motherhood-statement discipline without inverting the constitutional hierarchy.
4. **Grounded in the protocol's foundational commitments.** Every Objective operationalises at least one APP-1 §5 Protocol Invariant — pre-existing or added through amendment. Where an Objective motivates a new Invariant, the case is flagged for consideration in APP-1 evolution.
5. **Distinct outcome.** Two candidates addressing the same underlying enterprise concern were merged. Objectives are not synonyms.
6. **Cross-system by construction.** Objectives had to apply across system boundaries (per APP-1 Invariant 3 as concurrently revised). Candidates that only made sense within a single subsystem's scope were rejected.

### 2.2 Candidates considered

| Candidate | Status | Rationale |
|:---|:---|:---|
| Authorised Action | **Accepted as O-1** | Foundational; every other Objective depends on knowing who acted and with what authority. Grounded in Invariant 3. |
| Independent Verification | **Accepted as O-2** | Combined with "measured human oversight" to produce a single Objective; the two are inseparable in practice. Grounded in Invariant 4. |
| Bounded Agency | **Accepted as O-3** | Absorbed the Temporal Activation Ordering (security controls before data flows) clause; both are outcomes of "what stops the AI." Grounded in Invariant 7. |
| Execution-Time Evidence | **Accepted as O-4** | Directly grounded in Invariant 2, the strongest possible tether. Distinct from O-1/O-2/O-3 in enterprise concern (auditability, not authority or verification). |
| Governed Change | **Accepted as O-5** | Absorbed both the rule-based / judgment-dependent distinction (Invariant 1) and governed feedback loops (Invariant 6). Distinct from O-2 because O-2 is about individual proposals; O-5 is about the system evolving over time. |
| Cross-System Boundary Operation | **Elevated to structural property (APP-0 §5.1)** | Cross-system is a scope property, not an outcome. Elevating to §5 lets every Objective inherit it once rather than restating. |
| Same-Standard-at-Every-L-Level | **Elevated to structural property (APP-0 §5.2)** | A protocol design principle from Invariant 5, not an enterprise-facing outcome. Belongs in framing, not as an Objective. |
| Cybersecurity of governed data flows | **Merged into O-3** | Buyers view "what stops the AI" and "security controls before data flows" as one concern. Separating them created a false distinction. |
| Regulatory Compliance | **Rejected as Objective** | Per APP-1 §2, regulatory obligations are a constraint above all Objectives, not itself an Objective. Handled via APP-0 Appendix C mapping. |
| Model Alignment / Model Behaviour | **Rejected as Objective** | Per APP-1 §6 Non-Goal 3, model behaviour is out of scope. Model layer, not Governance layer. See §4 Layer Composition Extended. |
| Cross-Family Verification | **Merged into O-2 Extended Tier** | This is a mechanism refinement of "independent verification," not a distinct outcome. Also structurally hard to retrofit, so it fits the Extended Tier posture rather than the Universal Floor. Elevating to a top-level Objective would exclude adopters who verify with a same-family model. |
| Frame Integrity / Provenance | **Merged into O-1 and O-4** | Frame integrity is the mechanism by which authorised action and evidence work, not an enterprise-facing outcome. |
| Data Privacy / Retention | **Rejected as Objective** | Privacy is a regulatory constraint (per APP-1 §2 tier 1). Handled via Appendix C regulatory mapping. Elevating privacy to an Objective would confuse regulatory constraint with governance outcome. |
| HITL Quality Measurement | **Merged into O-2** | The "measured, not merely recorded" clause is the operational core of Independent Verification. Splitting would create two Objectives with overlapping realisation. |
| Performance / Latency / Availability | **Rejected** | Quality-of-service concerns, not governance outcomes. Belong to platform SLAs, not the protocol. |
| Explainability / End-User Transparency | **Deferred** | Delivered by O-4 (evidence). No separate Objective needed at current framework scope. May be reconsidered if EU AI Act Article 86 (right to explanation) case law expands scope. |
| Deployment Portability | **Rejected** | An implementation property, not a governance outcome. Belongs to conformance profiles (APP-5), not Objectives. |
| Anti-Deception / Anti-Collusion | **Rejected as Objective; addressed via layer composition** | This is Model-layer language (e.g., in disposition-based frontier-lab codes). APP-0 addresses the Governance layer; deception or collusion of a model is bounded by O-3 (the system stops what the model does) regardless of model disposition. Making it a top-level Objective would conflate layers. |

### 2.3 Design tensions resolved

**Coordinated protocol suite, not retrofit.** APP-0 is introduced concurrently with APP-1 through APP-5 revisions, not bolted onto a frozen corpus. The specification suite is co-designed: APP-0 states outcomes; APP-1 governs; APP-2..5 realise. Where an Objective is not fully realised in current APP-2..5 drafts, the gap is recorded rather than the Objective being dropped.

**Objective count.** Five was chosen after considering 3, 5, 7, and 9. Precedent range for durable goals-driven standards is 4 to 7 (WCAG POUR = 4; NIST CSF 2.0 Functions = 6; NIST 800-207 Zero Trust tenets = 7; OECD AI Principles = 5). Below 4, coverage of enterprise-governance gaps is incomplete. Above 7, memorability degrades and Objectives start overlapping. Five covers the gaps identified in §3 Model Framework Cross-Walk through merging (Frame integrity into O-1/O-4; cross-family into O-2 extension; TAO into O-3; feedback loops into O-5).

**Outcome vs value framing.** Objectives are stated as outcomes ("the system delivers X"), not values ("the system respects X"). This is the anti-motherhood-statement mechanism: an outcome can be tested; a value cannot.

**Same-standard vs tiered.** Objectives are the same at every L-level per Invariant 5; only evidence richness varies. The Universal Floor / Extended Tier split in APP-0 Appendix A is a Commitment Profile tiering, not an Objective tiering.

**Whose Objectives?** Primary audience is the Enterprise Process Owner (APP-1 constituency 3). Process Participants (constituency 2) benefit through O-2 measured oversight and O-3 boundary enforcement. Objectives are deliberately *not* Vendor Objectives (that is the Product layer, APP-0 Appendix A) and *not* Regulator Objectives (that is the regulatory constraint layer, APP-1 §2 tier 1).

**Naming discipline.** Objective names are two-word noun phrases (Authorised Action; Bounded Agency; Governed Change) to prevent adjective-drift ("Ethical AI," "Responsible AI") and to match enterprise governance-domain vocabulary that predates AI.

### 2.4 What could change in a future revision

- If a Model-layer framework adds executable-policy-at-enforcement or per-workflow evidence to its scope, the Model Framework Cross-Walk in §3 updates. Objectives would likely remain stable.
- If regulatory frameworks introduce new mandatory outcome categories, APP-0 Appendix C mapping expands; Objectives may not.
- If working-group deliberation surfaces a genuine outcome not addressable within the current five, a sixth Objective may be added under the two-thirds amendment threshold per APP-1 §7. The bar for addition is genuine outcome distinctness, not compositional refinement.
- If an Objective motivates an APP-1 §5 Invariant addition (a stability commitment not yet in APP-1's seven Invariants), the case is documented here for consideration in the next APP-1 revision.

---

## 3. Model Framework Cross-Walk

This section summarises the current landscape of frontier-lab model-behaviour codes and their relationship to APP-0 Objectives. It supports the layer composition described in APP-0 Appendix B by making the composition concrete against real published frameworks. This section updates as frameworks revise; APP-0 Objectives themselves are stable across framework evolution.

### 3.1 Current frameworks

| Framework | Publisher | Structural type | Primary mechanism |
|:---|:---|:---|:---|
| Responsible Scaling Policy | Anthropic | Threshold-based | Capability Thresholds (e.g., CBRN uplift, autonomous AI R&D, cyber) → Required Safeguards |
| Preparedness Framework | OpenAI | Threshold-based | Tracked Categories (e.g., Biological & Chemical, Cybersecurity, AI Self-improvement) at Low / Medium / High / Critical |
| Frontier Safety Framework | Google DeepMind | Threshold-based | Critical Capability Levels + Alert Thresholds; deceptive-alignment as a distinct capability level |
| Humanist AI Code of Conduct | Microsoft | Disposition-based | Behavioural red lines (no goal-setting, no shutdown-resistance, no deception / collusion / self-reinforcement) |

Framework details reflect published or publicly disclosed status at the time of this document. Adopters should verify current versions before citing specifics; framework version details are subject to independent verification.

### 3.2 Common themes across all four

Two themes are present in all four frameworks:

- **Human-oversight preservation** as a design goal.
- **Public disclosure** of the framework itself.

### 3.3 Common themes across three of four (threshold-based only)

- CBRN safeguards.
- Cyber offensive capability limits.
- Autonomy / self-improvement limits.
- Escalation thresholds triggering safeguard requirements.
- Weight and model security proportionate to capability.

These are absent or only implicit in the disposition-based framework, which does not use capability thresholds.

### 3.4 Enterprise-governance concerns not addressed at Model layer

The following concerns arise at the process-execution boundary and are not addressed by any current frontier-lab model-behaviour code. APP-0 Objectives address them at the Governance layer:

| Enterprise concern | Addressed by |
|:---|:---|
| Verification of governance-critical judgments across independent verifiers or model families | O-2 (Extended Tier commitment) |
| Enterprise identity, purpose, delegated authority across systems | O-1 |
| Executable policy at enforcement points inside enterprise workflows | O-1, O-2, O-3 |
| Per-workflow execution-time evidence | O-4 |
| Behaviour continuity across model weight updates | O-3 (Governance-layer controls independent of model disposition) |
| Boundary enforcement independent of model disposition | O-3 |
| Governance of change across multi-model orchestration | O-5 |

### 3.5 Structural fault line

Three of the four frameworks are threshold-based: capability evaluations gate release. One is disposition-based: it commits to what the model *is like* behaviourally. APP-0 is neither — it operates at the Governance layer via system-level controls whose effect is independent of model disposition. This structural distinction is why APP-0 composes with any of the four frontier-lab frameworks. The Model layer and Governance layer address complementary concerns.

### 3.6 Evolution note

Frontier-lab frameworks version frequently. This section reflects the frameworks as observed at the time of this document. APP-0 Objectives are stable across framework evolution; only this section updates on framework revisions. Adopters and assessors should treat this section as orientation and verify current framework details against primary sources.

---

## 4. Layer Composition Extended

APP-0 Appendix B introduces three layers: Model, Governance, Product. This section expands the composition with additional detail for readers new to the layer distinction.

### 4.1 Why three layers, not two

An "AI system commitment" collapses three distinct scopes:

- What the model itself will do (Model layer).
- What the system using the model delivers as governance outcomes (Governance layer).
- What a specific vendor's deployment commits to (Product layer).

These have different accountable parties, different assessment methods, and different failure modes. Collapsing them into one layer creates procurement checkboxes that are difficult to evidence and easy to fabricate.

### 4.2 How the layers compose in a governed enterprise deployment

A well-governed enterprise deployment stacks all three:

- The Model layer states that the underlying model was built and released against a safety policy.
- The Governance layer states that the process governing the model's use delivers the five Objectives.
- The Product layer states that a specific vendor's deployment realises both underlying layers with declared commitments.

None is sufficient alone. A Model-layer commitment does not resolve enterprise identity or emit per-workflow evidence. A Governance-layer commitment does not constrain how the model was built or trained. A Product-layer commitment without either underlying layer is a marketing artefact.

### 4.3 How the layers fail differently

Each layer fails in a distinctive way:

- **Model layer failure:** a model exhibits behaviour outside its safety-policy commitments — capability drift, deceptive-alignment signals, jailbreak effectiveness. Discovered through evaluation.
- **Governance layer failure:** an action executes without proper authorisation, verification, boundary enforcement, evidence, or change control. Discovered through incident investigation or audit.
- **Product layer failure:** a vendor's specific deployment falls short of what its Commitment Profile claims. Discovered through independent assessment or customer testing.

Each layer's assessment methods differ. APP-5 conformance evidence assesses the Governance layer; frontier-lab framework disclosures assess the Model layer; independent product assessment assesses the Product layer.

### 4.4 What each layer contributes and does not

Model-layer controls do not, by themselves, establish cross-system enterprise authority, execution evidence, or process-level governance. These are Governance-layer concerns.

Governance-layer controls do not build the model or specify its behaviour; they constrain the consequences of whatever behaviour the model exhibits.

Product commitments are most credible when supported by independently verifiable Governance-layer evidence and, where applicable, Model-layer disclosures.

---

## 5. Reading and Adoption Paths

Different roles read the APP series in different orders. This section provides suggested paths.

### 5.1 Enterprise buyer / auditor / regulator

1. **APP-0** — the five Objectives, buyer questions, layer composition.
2. **APP-IG-05 §3** — how APP-0 relates to frontier-lab model-behaviour codes.
3. **APP-IG-05 §6** — buyer evidence packs per Objective.
4. **Vendor Commitment Profile** — the specific deployment's commitments.
5. **APP-5** (targeted) — conformance evidence for the roles and scopes the vendor claims.

### 5.2 Enterprise deployer

1. **APP-0** — the five Objectives.
2. **APP-1** — constitutional principles, Priority of Constituencies.
3. **APP-5 §3.4** — Enterprise Deployer role and its conformance obligations.
4. **APP-IG-02** — cross-reference matrix locating specific requirements.
5. **APP-IG-05 §8** — deployment worked examples.

### 5.3 Platform implementer or vendor

1. **APP-1** — constitutional principles.
2. **APP-2, APP-3, APP-4** — normative requirements.
3. **APP-5** — role, L-level, profile, and applicable requirement matrices.
4. **APP-R1, APP-R2** — illustrative reference artefacts (Frame Schema; MCP Binding Reference Design). Non-normative; useful as starting points when realising CORE-A1-05 (schema portability) and CORE-A1-04 (MCP transport) respectively, or as benchmarks when departing from them.
5. **APP-0** — outcome-level orientation for external communication with buyers.
6. **APP-IG-05 §2** — Objective Selection Rationale for context on why the outcomes are what they are.
7. **APP-IG-05 §10** — illustrative Commitment Profile language.

### 5.4 Conformance assessor

1. **APP-5** — testable criteria, per-role matrices, interoperability rules.
2. **APP-1** — constitutional principles governing assessment.
3. **APP-0** — outcome-level context for what the assessment is proving.
4. **APP-IG-02** — authoritative source-mapping for cross-document requirements.
5. **APP-IG-05 §11** — evidence richness expectations at each L-level.

---

## 6. Buyer Evidence Requests

This section provides per-Objective templates for enterprise buyer conversations, RFPs, and vendor due diligence. For each Objective, it covers: what evidence to request; what evaluation questions to ask; what "good" looks like at each L-level; and common red flags.

**How to use this section.** In a vendor evaluation, walk through each of the five Objectives and use the templates below as a checklist for what to ask, what evidence to expect back, and how to interpret the responses. The templates are conservative — buyers should expand the request set based on their specific risk profile and regulatory context.

**Cross-reference to normative content.** Each Objective's evidence template cites the APP-0 §3 realising requirements and APP-5 tests. Vendor evidence should reference these IDs; a Commitment Profile that names outcomes without pointing to APP-5 evidence is a red flag (see APP-0 Appendix A discipline).

**Wave 1 recovery-evidence addendum.** For O-1, O-3, and O-4 evidence-request templates, buyers should additionally ask for recovery-evidence artefacts per APP-2 CORE-A2-13 (recovery_evidence schema) and CORE-A2-14 (outcome vocabulary), and for demonstration of recovery-path enforcement-tier parity per APP-3 SEC-S6-05. Recovery events are historically where evidence integrity, accountability, and enforcement discipline are most likely to lapse; the Wave 1 additions make these testable at the protocol layer.

### 6.1 O-1 Authorised Action

**Evidence to request from vendor:**
- The vendor's identity resolution architecture: how a governed action is bound to a resolved acting identity, including where cross-vendor identity is federated and where it is native.
- Sample PxER records showing the three-layer accountability chain (CORE-A4-01): intent authority, execution authority, oversight authority.
- Session token schema and retention policy (SEC-S13-01, SEC-S13-02): what fields are encoded (autonomy level, delegation chain, HITL engagement level, risk classification), and how long they are retained.
- Delegation graph inspection interface: how the vendor demonstrates that no agent has been given authority by a peer instruction alone (SEC-S13-03 authority-provenance invariant).
- Composed-authority halt evidence (SEC-S2-06): sample cases where composed authority in a delegation chain triggered halt-for-re-authorisation.
- **Recovery-decision accountability evidence (CORE-A4-06):** sample records showing the three-layer accountability chain applied to a recovery decision itself — who authored the recovery policy (intent), which instance executed the recovery decision (execution), and who is accountable for the recovery-policy oversight.

**Evaluation questions:**
- "For a governed action in your product, can you show me the acting identity, the authority chain, and the source of each delegation step?"
- "How does your system detect when composed authority in a multi-agent chain exceeds any single agent's declared scope?"
- "What happens when a peer agent instructs another agent to take an action outside its declared authorisation?"
- "How do you handle identity resolution when the governed process crosses vendors — for example, when an AI in your product acts on data from another vendor's system?"
- "When a recovery path is invoked mid-execution, who is accountable for authorising the recovery — and can you show me that chain?"

**What good looks like at each L-level:**
- **L1:** Basic identity binding on each governed action. Session tokens exist but may be human-only. Delegation chain unavailable.
- **L2:** Session tokens for AI agents include autonomy level and delegation chain. Composed-authority halt implemented but may be reactive, not preventive. Recovery-decision accountability chain (CORE-A4-06) enforced.
- **L3:** Full delegation-invariant triad (depth, reach, source) implemented. Cross-family identity resolution native for multi-vendor deployments. Authority-provenance invariant enforced structurally. Recovery-decision accountability extends across cross-vendor recovery paths.
- **L4:** L3 plus marketplace-scale identity federation, cross-tenant identity isolation, and formal delegation graph invariant checks. Recovery-decision accountability extends across marketplace-scale recovery federation.

**Red flags:**
- Vendor claims "identity-based governance" but cannot show the three-layer accountability chain in sample PxER records.
- Session tokens lack autonomy level, delegation chain, or risk classification fields.
- Vendor accepts peer-to-peer authority elevation without traceable governance framework rule or human/tenant principal source.
- Compositional authority halt is described as "future roadmap" rather than active enforcement.
- Recovery decisions are invisible in audit records ("we retried and it worked") with no authorship trace.

### 6.2 O-2 Independent, Measured Verification

**Evidence to request from vendor:**
- The vendor's verification architecture for governance-critical judgment surfaces: which surfaces are AI-mediated, which are policy-mediated, and how independence is enforced (SEC-S3-01, SEC-S3-07).
- Model-family composition of the verification stack: for AI-mediated verification on governance-critical surfaces, which model families are used for the actor vs. the verifier, and how family independence is verified structurally.
- HITL engagement records showing the engagement-fidelity marker (CORE-A6-03): sample records with both `acknowledgement-only` and `behavioural-measured` markers, and the criteria used to assign each.
- Canary injection evidence (SEC-S5-02): how frequently, on what basis, and with what detection outcomes.
- Behavioural authenticity detection metrics (SEC-S5-03): what patterns trigger authenticity concerns and how they are actioned.

**Evaluation questions:**
- "Which of your governance-critical judgment surfaces are AI-mediated, and for each, what model family verifies the actor's model family?"
- "When a human approves a governance-critical action in your product, what evidence do you preserve that the human actually exercised judgment rather than clicking through?"
- "How do you detect rubber-stamp approval patterns, and what happens when they are detected?"
- "How do you handle verification when the process risk is low? Is there a risk-based tier structure, or is the same independence bar applied uniformly?"

**What good looks like at each L-level:**
- **L1:** Basic independent verification on high-risk actions. HITL records may be present but engagement quality not measured.
- **L2:** Measured HITL engagement with engagement-fidelity markers. Canary injection at random intervals. Cross-family verification for the most sensitive judgment surfaces.
- **L3:** SEC-S3-07 cross-family verification enforced structurally across all governance-critical judgment surfaces. Adversarial verification obligations (SEC-XX-04) met for all AI-mediated verification surfaces.
- **L4:** L3 plus multi-family verification quorum on the highest-risk surfaces. Behavioural detection tuned to detect emerging rubber-stamp patterns before they become systemic.

**Red flags:**
- Vendor claims "independent verification" but the verifier is the same model family (or same weights) as the actor.
- HITL evidence contains approvals with no engagement fidelity marker, or engagement duration consistently at the shortest possible interaction time.
- Canary injection either does not exist or is deterministic (attackers can predict it).
- Vendor cannot answer whether authenticity detection at L2+ is behavioural or only threshold-based.

### 6.3 O-3 Bounded Agency

**Evidence to request from vendor:**
- Circuit breaker inventory: what triggers halt, what defines the halt scope, and how re-authorisation is required (SEC-S7-01, SEC-S7-02).
- Temporal Activation Ordering evidence (SEC-XX-01): how the vendor demonstrates that security controls are active before governed data flows begin.
- Substrate isolation architecture (SEC-XX-02): what shared substrates exist between agents, how they are governed, and how covert-channel suspicion is detected.
- Coordination-pattern detection outputs (SEC-S7-03): how the vendor detects and responds to emergent coordination behaviour across multiple agents.
- Agent-initiated safety-event channel logs (SEC-S5-06): sample events, response times, and containment outcomes.
- Fail-closed evidence for C0/C1 steps: what happens when the governance layer becomes unavailable during a governed C0/C1 step (CORE-XX-01, SEC-S7-02).
- **Recovery-path enforcement-tier parity evidence (SEC-S6-05):** sample cases showing that recovery paths meet or exceed the enforcement tier of the primary path they replace, and demonstration of the `bypassed` outcome response (CORE-A2-14) when parity cannot be achieved.

**Evaluation questions:**
- "When an agent in your product exceeds its authorised scope, what stops it? Is the stopping mechanism deterministic, or does it depend on the agent's own compliance?"
- "How do you prevent hidden communication between agents through shared substrates like memory, event streams, or coordination channels?"
- "What happens to a compliance-critical action if the governance layer becomes unavailable mid-execution?"
- "Have you seen emergent coordination behaviour across your agents that no single agent's authorisation permitted? What signals detected it?"
- "What are the containment modes your system enters on safety events? Can I inspect the mode taxonomy?"
- "When a recovery path is invoked under pressure, how do you guarantee the recovery does not silently downgrade the compliance tier of the primary path?"

**What good looks like at each L-level:**
- **L1:** Basic circuit breakers on high-risk actions. Fail-closed on the most critical steps.
- **L2:** Comprehensive circuit breaker inventory with defined halt scopes. Substrate isolation enforced for enumerated shared substrates. Compliance-tiered graceful degradation across C0/C1/C2/C3/C4. Recovery-path enforcement-tier parity (SEC-S6-05) enforced.
- **L3:** SEC-S7-03 coordination-pattern detection active. Agent-initiated safety-event channels operational (SEC-S5-06). Authority reduction on uncertainty implemented (SEC-XX-03). Recovery-perimeter completeness verified against declared pressure vectors.
- **L4:** L3 plus multi-agent-scale coordination behavior modelling and containment. Marketplace-scale substrate isolation guarantees.

**Red flags:**
- Vendor describes "safety through model training" as the primary boundary enforcement mechanism.
- Circuit breakers exist but their halt scope is undefined or overlapping (unclear what actually stops).
- No answer or vague answer to the substrate isolation question — vendor does not have a clear model of what shared surfaces its agents can use to coordinate.
- Fail-closed on C0/C1 steps is described as configurable per-deployment rather than a fixed protocol requirement.
- Governance layer unavailability during a governed step is described as a "degradation to best-effort" rather than a hard halt.
- Recovery paths bypass compliance controls without recording the `bypassed` outcome.

### 6.4 O-4 Execution-Time Evidence

**Evidence to request from vendor:**
- Sample PxER records for at least one governed process instance, showing: mandatory step fields per CORE-A2-02, the 7-field conformance schema per CORE-A2-03, evidence tier per SEC-S4-02, and verification status per SEC-S4-01.
- Evidence assembly architecture: how the vendor demonstrates that PxER is assembled during execution (CORE-A2-01), not reconstructed from event logs after the fact.
- Write-path provenance evidence (SEC-S4-05): the six enumerated artifact classes and their signed service provenance verification against independent audit logs.
- Three evidence integrity dimensions (CORE-A2-10): sample verification outputs across D/P conformance, evidence authenticity, and write-path provenance.
- Erasure reconciliation evidence (SEC-S4-06): sample erasure event records with subject reference or one-way digest, timestamp, lawful basis, and affected record identifier scope.
- **Recovery evidence schema (CORE-A2-13) and outcome vocabulary (CORE-A2-14):** sample PxER records with the 6-field recovery_evidence object populated (path_class, initiator, deviation_class, outcome, attempt_count, authorization_ref) and outcome values drawn from the CORE-A2-14 5-value vocabulary (recovered / partial / failed / bypassed / self_healed).

**Evaluation questions:**
- "Can you show me the PxER for a specific transaction I select? What fields are populated at what stage of execution?"
- "How do you demonstrate that PxER is assembled during execution rather than reconstructed after the fact from event logs?"
- "For each of the three evidence integrity dimensions, what verification is applied and how frequently?"
- "How do you handle lawful erasure of subject data while preserving the hash-chain integrity of unaffected records?"
- "Can I verify a PxER independently of your platform — do I get the artefacts I need to reconstruct verification myself?"
- "When a recovery path fires mid-execution, what recovery_evidence do you assemble, and how is the outcome vocabulary enforced?"

**What good looks like at each L-level:**
- **L1:** Basic PxER with mandatory fields. Evidence tier may be limited. Verification status tracked.
- **L2:** Full 7-field conformance schema. Three evidence integrity dimensions verified. Signed write-path provenance for critical artifact classes. Recovery events carry the CORE-A2-13 schema with CORE-A2-14 outcome vocabulary.
- **L3:** L3 Enhanced telemetry schema (CORE-L3-01) with 6 minimum fields. Elevated verification frequency for new L3 contributors. Cross-tenant evidence isolation enforced. Recovery evidence carried through cross-vendor recovery paths with declared trust-tier provenance.
- **L4:** Marketplace-scale evidence federation with cross-vendor evidence linkage. Independent third-party evidence verification supported. Recovery evidence federated across marketplace-scale recovery paths.

**Red flags:**
- PxER records generated only on process completion, not during execution.
- Evidence integrity dimensions collapsed into a single score (masking weakness in one dimension per APP-5 §2.1).
- Write-path provenance covers some artifact classes but not the enumerated six (SEC-S4-05).
- Vendor cannot demonstrate erasure without also compromising hash-chain integrity of unaffected records.
- Evidence artefacts are proprietary formats that cannot be verified independently of the vendor's platform.
- Recovery evidence is a free-text log rather than the structured CORE-A2-13 schema.

### 6.5 O-5 Governed Change

**Evidence to request from vendor:**
- Promotion (P→D) lifecycle records (CORE-A8-01 through A8-04): sample promotions showing classification provenance (5 values), evidence fields, promotion outcomes, and Frame transition events.
- Dual-human approval evidence for C0/C1 promotions (SEC-S8-03): sample cases and audit trail.
- Velocity anomaly detection (SEC-S8-04): what velocity is considered atypical, how it is detected, and what happens on detection (session provenance + elevated review path).
- Governance-control integrity monitoring (SEC-S6-04): how the vendor detects tampering with the governance-control surface itself.
- Evidence-vs-learning quarantine architecture (SEC-S9-03): how the vendor separates the evidence store from the learning surface and prevents compromise of one from propagating to the other.
- Rubber-stamp detection (SEC-S5-03 for HITL; broader for approval patterns): metrics on approval patterns and actions taken on detected rubber-stamp behaviour.

**Evaluation questions:**
- "How does a rule move from probabilistic execution to deterministic execution in your product? What governance approval is required?"
- "How do you detect when your governance controls have been tampered with, and what is the response path?"
- "How do you separate the evidence you rely on for auditing from the evidence that feeds your learning loops? Can you show me the boundary architecturally?"
- "When a promotion process runs at an atypically high velocity, what happens? Is dual-approval automatically blocked, or is it a soft signal?"
- "What is your process for detecting and responding to systemic rubber-stamp approval patterns across your approver base?"

**What good looks like at each L-level:**
- **L1:** Basic classification provenance and promotion evidence. Manual review of promotions.
- **L2:** Full A8 promotion lifecycle with three outcomes representable. Dual-human approval on C0/C1 promotions. Frame transition events recorded.
- **L3:** SEC-S8-04 velocity anomaly detection active with elevated review path enforcement. SEC-S6-04 governance-control integrity monitoring active. SEC-S9-03 evidence-vs-learning quarantine enforced structurally.
- **L4:** L3 plus cross-tenant learning boundary enforcement, formal governance-control tamper detection, and marketplace-scale change governance.

**Red flags:**
- Promotion lifecycle records missing classification provenance or promotion evidence fields.
- Dual-human approval on C0/C1 promotions is described as configurable per-deployment rather than a hard requirement.
- Vendor cannot explain the boundary between the evidence store and the learning surface — the two are conflated architecturally.
- Governance-control integrity monitoring is described as "future roadmap" rather than active.
- Vendor has no metrics on rubber-stamp approval patterns and no policy for detecting or responding to them.

### 6.6 Cross-Objective evidence hygiene

**Cross-Objective questions** for any vendor evaluation, regardless of specific Objective focus:

- **Conformance declaration.** "What is your declared conformance scope per APP-5 §1.3 — participant role(s), L-level per scope, and conformance profile (Preventive / Detective / Retrospective)?"
- **Multi-role declaration.** "If you declare multiple roles (e.g., Governance Orchestrator + Telemetry Contributor), is your applicable dimension set the union of the roles' dimensions, and are you satisfying every requirement from every declared-role matrix?"
- **Partial conformance declaration.** "Are there any MUST-level requirements you do not fully meet? If so, are they explicitly declared per CORE-CP-04?"
- **Verifiable conformance assertion.** "Can you produce a signed conformance assertion per APP-5 §7.4 CONF-T-06 that I can verify without re-running the test suite?"

**Universal red flags** across all Objectives:

- Vendor cannot cite specific APP-2 / APP-3 / APP-4 requirement IDs when describing controls.
- Vendor's Commitment Profile is not bound to APP-5 test IDs (violates the APP-0 Appendix A discipline).
- Vendor claims "APP conformance" without a declared role, L-level, or profile.
- Vendor treats "APP conformance" as a certification badge rather than a scope-specific, dimension-decomposed conformance declaration.
- Vendor's sustained-evidence expectation is a single point-in-time attestation rather than sustained conformance over a defined period.

---

## 7. Section Index

| Section | Status | Notes |
|:---|:---|:---|
| **§8 Worked Examples** | Complete v0.10 | Two scenarios covering all five Objectives, including Wave 1 recovery-path extension. |
| **§9 Objective-Specific Evidence Packs** | **RETIRED v0.5** | Subsumed into §6 (Buyer Evidence Requests). See §9 disposition below. |
| **§10 Illustrative Commitment Profile Language** | Complete v0.10; renumbered v0.11 | Three vendor archetypes with Wave 1 recovery commitments integrated. (Was §11 through v0.10.) |
| **§11 Guidance on Evidence Richness at L1–L4** | Complete v0.10; renumbered v0.11 | Per-Objective evidence-richness maturity map with Wave 1 additions integrated. (Was §12 through v0.10.) |

**v0.11 scope change.** The former §10 Regulatory Crosswalks (Detailed) has been removed in v0.11. Standards and regulatory crosswalks are being refactored into a dedicated publication (timing TBD) and are out of scope for this guide going forward.

---

## 8. Worked Examples

Two scenarios illustrate how the five Objectives play out in concrete deployment contexts. Both scenarios are constructed for illustrative purposes; they do not describe any specific vendor or product.

### 8.1 Cross-vendor procure-to-pay (P2P) process

**Scenario setup.** A manufacturing enterprise deploys a governed procure-to-pay process spanning four vendors:

- **Vendor A (Enterprise ERP):** system of record for purchase orders, vendor master data, and invoice records. L2 integration maturity.
- **Vendor B (AI Orchestrator):** governance orchestrator for the AI-augmented P2P workflow. L3 integration maturity.
- **Vendor C (Agent Builder Platform):** hosts the invoice-classification agent and vendor-matching agent. L2 integration maturity, working towards L3.
- **Vendor D (Entity Resolution Service):** provides authoritative vendor identity resolution across the ERP, agent platform, and external counterparty sources.

The governed process: an invoice arrives via email → invoice-classification agent (Vendor C) → vendor-matching agent (Vendor C, verified by Vendor B's independent classification path) → three-way match against PO in ERP (Vendor A) → human approver reviews high-value invoices (via Vendor B's HITL surface) → payment authorised in ERP.

**Objective realisation in this scenario:**

*O-1 Authorised Action.* The invoice-classification agent (Vendor C) acts against a session-scoped identity token (SEC-S13-01) that encodes: the tenant (this enterprise), the autonomy level (L2 default), the delegation chain (Vendor B → Vendor C's agent runtime), and the risk classification (invoices below the enterprise threshold execute autonomously; above the threshold require HITL). When the vendor-matching agent proposes a match to a supplier record in Vendor D's entity resolution service, the resulting authority to write to the ERP invoice record is checked against the compositional authority accumulation invariant (SEC-S2-06): the agent-in-Vendor-C has authority to *match*; the orchestrator-in-Vendor-B has authority to *commit*; neither has both alone. The commit halts pending Vendor B's orchestration completion gate (CORE-A4-05).

*O-2 Independent, Measured Verification.* Invoice classification (Vendor C's AI model) is a governance-critical judgment surface: the classification determines whether the invoice flows through the autonomous path or the HITL path. SEC-S3-07 requires the verifying classifier to be structurally distinct in model family from the actor classifier. In practice: Vendor C uses one model family for classification; Vendor B's independent verification path uses a different model family for the verification decision. Where the two disagree, the invoice routes to HITL. The HITL surface itself (invoice review by a human approver in Vendor B's interface) records an engagement-fidelity marker (CORE-A6-03): `behavioural-measured` when the reviewer's engagement passes authenticity detection (SEC-S5-03); `acknowledgement-only` when it does not. Approval patterns showing systematically low engagement fidelity trigger elevated review, breaking the rubber-stamp cycle.

*O-3 Bounded Agency.* The three-way match against the ERP (Vendor A) is bounded: the agent can *read* PO records and *propose* the match, but cannot *write* the payment authorisation itself. That write is executed by Vendor B's orchestrator with distinct authorisation (SEC-S13-03: authority-provenance invariant — no peer agent can elevate another agent's write authority). If Vendor B detects that Vendor C's agent has proposed matches at atypical velocity (SEC-S7-03 coordination-pattern detectability), the containment path enters "restricted" mode (SEC-XX-03): the agent can continue reading but its match proposals require elevated human review until re-authorisation. Temporal Activation Ordering (SEC-XX-01) is verified continuously: the write-path authentication (SEC-S4-05) must be active before any P-track evidence flow to Vendor B; if the security control lags, the write halts and DEGRADED status is recorded (CORE-A2-04a).

*O-4 Execution-Time Evidence.* The Process Execution Record (PxER) is assembled during execution across all four vendors, not reconstructed from event logs. Each step record (CORE-A2-02) records the acting identity (from Vendor C or Vendor B's session token), timestamp, transaction reference (the PO ID from Vendor A, plus the entity references from Vendor D), and conformance status. The three evidence integrity dimensions (CORE-A2-10) are verified separately: D/P conformance (was the intended track actually executed?), evidence authenticity (write-path provenance per SEC-S4-05 for each artifact class: PxER records, HITL records, promotion records, drift signal records, model version markers, and entity registry entries), and cross-tenant isolation (SEC-S14-04). When the auditor asks "what happened on invoice #12345?", the answer is a signed, verifiable PxER instance record with entity_correlations block (EC-11) resolving the vendor identity across all four systems.

*O-5 Governed Change.* Over several months of operation, the vendor-matching agent's success rate on a specific class of vendors (repeat suppliers with stable master data) becomes empirically stable. This makes it a candidate for P→D promotion (CORE-A3-01 through A3-04; EC-31 stable correlations as P→D candidates). Vendor B's promotion pipeline runs the following gates: (a) evidence integrity gate — the underlying P-track evidence must pass SEC-S8-01 before promotion is considered; (b) promotion evidence exclusivity — the same match cannot be simultaneously counted as autonomous execution evidence and as P→D promotion evidence (SEC-S8-02); (c) dual-human approval for any promotion touching C0 or C1 constraints (SEC-S8-03) — in this scenario, promoting a compliance-relevant vendor-matching rule is C1 and triggers dual-human; (d) velocity integrity — if promotions run at atypically high velocity (SEC-S8-04), session provenance is elevated for review. Meanwhile, the evidence-vs-learning quarantine (SEC-S9-03) ensures that if Vendor C's classifier is compromised, the compromised outputs do not silently propagate into Vendor B's learning surface: the learning path reads from a separate, verified evidence store.

**What the buyer sees in evaluation.** The enterprise's procurement director asks Vendor B: *"Walk me through invoice #12345 end-to-end."* Vendor B pulls the signed PxER instance record, shows the four-vendor evidence chain, points to the specific SEC-S3-07 cross-family verification decision that routed this invoice, shows the HITL engagement-fidelity marker, and demonstrates the compositional authority halt-and-re-authorise event. This is the answer the auditor asked about — assembled during execution, cross-vendor verifiable, backed by APP-5 conformance evidence at each vendor's declared L-level.

#### 8.1.1 Recovery-path scenario extension (Wave 1)

Consider a variant where invoice #12345 begins normal processing but the vendor-matching agent (Vendor C) times out mid-execution due to an upstream API failure. Vendor B's orchestrator detects the deviation and invokes the recovery path.

The Wave 1 recovery-evidence protocol extension activates:

- **Recovery evidence assembly (CORE-A2-13).** Vendor B's PxER step record for the failed match now includes a `recovery_evidence` object with six fields: `path_class` (identifies the recovery path taken — say, `retry-with-backoff`), `initiator` (P-track, since the orchestrator triggered the retry autonomously), `deviation_class` (identifies what triggered recovery — upstream timeout), `outcome` (per CORE-A2-14 vocabulary), `attempt_count`, and `authorization_ref` (linking to the applicable A4-06 accountability chain if human authorisation was required).

- **Recovery outcome vocabulary (CORE-A2-14).** After two retries, the vendor-matching agent succeeds on attempt three. The outcome is recorded as `recovered`. Had the retries all failed, the outcome would be `failed` and Vendor B's A6 engagement quality requirements would activate at the receiving human authority. Had the recovery path lacked capacity to invoke the required compliance controls at parity with the primary path (say, if the retry backoff meant the compliance-check agent could not be re-invoked in time), the outcome would be `bypassed` and the invoice would be blocked from C0/C1 execution per SEC-S7-02 fail-closed.

- **Recovery-decision accountability (CORE-A4-06).** Because this invoice is compliance-relevant (VAT-registered supplier), the recovery decision to retry vs. escalate to human review passes through A4-06's three-layer accountability chain applied to the recovery decision: intent (Frame authorship of the retry policy), execution (the orchestrator instance that made the retry decision), and oversight (the accountable enterprise governance role approving the retry policy). Compare this to the historical failure mode where recovery decisions were invisible in audit records — the chain now names who authorised the retry policy, who executed the retry, and who is accountable for oversight.

- **Enforcement-tier invariant (SEC-S6-05).** Before invoking the retry path, Vendor B's orchestrator verifies enforcement-tier parity: the retry path invokes the same compliance-check agent (or an equivalent-tier substitute) with the same `external-mandated` control tier and the same Attestation-level HITL that the primary path would have used. If parity cannot be achieved — say, if the compliance-check agent is fully unavailable and no substitute is registered — the retry path invokes A2-14 outcome `bypassed`, blocking C0/C1 execution, routing to human authorisation per CORE-A4-06 on C2 steps. This closes the SRE-classical failure mode where recovery under pressure silently downgrades to a lower-tier alternative.

**What the auditor sees.** Auditor asks Vendor B: *"What happened when invoice #12345 timed out mid-processing?"* Vendor B pulls the PxER step record showing recovery_evidence: two failed attempts recorded, outcome recovered on attempt three, path_class retry-with-backoff, enforcement-tier parity verified, no C0/C1 blocking. The auditor's evidence is complete; the historical black hole of "we retried, it worked" is now audit-answerable.

### 8.2 Single-vendor extending to multi-vendor: HR employee onboarding

**Scenario setup.** A large services organisation deploys AI-augmented employee onboarding, starting with single-vendor adoption at L2 and extending to multi-vendor at L3.

- **Phase 1 (L2, single-vendor):** all onboarding steps run inside one HR platform vendor (Vendor X). Vendor X hosts the CV-parsing agent, the role-matching agent, and the compliance-check agent, all operating on Vendor X's own model family. Governance orchestrator role and Agent Builder Platform role are both Vendor X.
- **Phase 2 (L3, multi-vendor):** the enterprise adds Vendor Y (Independent Verification Service) providing a distinct-family classifier for the compliance-check surface, and Vendor Z (Background Check Provider) for cross-enterprise verification of candidate credentials.

Both phases target the same APP-0 Objectives; what changes is evidence richness.

**Phase 1 (L2, single-vendor) — what evidence looks like:**

*O-1 Authorised Action.* Session tokens (SEC-S13-01) are present for every agent action. The delegation chain is fully within Vendor X's estate, so cross-vendor SEC-S2-06 compositional authority halts are trivially internal — but they still fire when composed authority would exceed any single agent's scope (e.g., an agent trained to parse CVs cannot compose with an agent trained to verify education credentials to produce a hiring recommendation without human re-authorisation). Vendor X's Commitment Profile declares single-vendor adoption per APP-0 §5.1; conformance evidence is per APP-5 Governance Orchestrator role at L2.

*O-2 Independent, Measured Verification.* SEC-S3-07 cross-family verification poses a design question: is the compliance-check agent (Vendor X model family A) verified by another Vendor X model family (family B, structurally distinct)? Yes — Vendor X commits to family-distinct verification internally, meeting SEC-S3-07 without needing an external vendor. HITL engagement fidelity (CORE-A6-03) is recorded for every human approval on high-risk hires.

*O-3 Bounded Agency.* Substrate isolation (SEC-XX-02) applies across Vendor X's agent runtime: even though all agents are from Vendor X, they don't share memory, coordination surfaces, or event streams beyond what's declared and monitored. Coordination-pattern detectability (SEC-S7-03) is active internally: if Vendor X's agents begin to coordinate in emergent ways not intended by the declared workflow, the pattern is detected and reviewed.

*O-4 Execution-Time Evidence.* PxER assembly during execution is entirely within Vendor X's storage — but the L2 evidence structure is complete: three evidence integrity dimensions verified (CORE-A2-10), evidence tier classified (SEC-S4-02), write-path authenticated for the six artifact classes (SEC-S4-05). The evidence is not marketplace-federated because there's only one vendor to federate with, but it is independently verifiable within Vendor X's platform.

*O-5 Governed Change.* The role-matching agent's confidence on a subset of role types (e.g., standard engineering roles for which the enterprise has historical hiring data) grows stable. Vendor X's promotion pipeline runs, dual-human approval fires for any promotion touching immigration/right-to-work compliance (C0/C1). Evidence-vs-learning quarantine (SEC-S9-03) is enforced within Vendor X's platform: the learning surface reads from a separate verified evidence store.

**Phase 2 (L3, multi-vendor) — what changes in evidence:**

The Objectives remain the same. What changes is evidence richness:

*O-1.* Session tokens now cross vendor boundaries. Vendor Y and Vendor Z bring their own session identity, federated through Vendor X's orchestrator. The delegation chain shows all three vendors explicitly. SEC-S2-06 compositional authority halts fire on cross-vendor compositions — a Vendor Y verification proposal combined with a Vendor Z background check result composing into a hiring recommendation requires human re-authorisation.

*O-2.* Cross-family verification is now genuinely cross-vendor: Vendor Y provides the independent verification classifier, structurally distinct from Vendor X's family. This satisfies SEC-S3-07 with stronger evidence (different vendor, different weights, different training data — the disagreement space is larger and the shared failure mode surface is smaller).

*O-3.* Substrate isolation now includes explicit cross-vendor isolation. If Vendor Y and Vendor Z had a shared substrate (a common data broker, an event log they both wrote to), that substrate would need to be governed. Coordination-pattern detectability now spans three-vendor coordination.

*O-4.* Evidence is now L3-tier: enhanced telemetry schema (CORE-L3-01) with the six minimum fields, tiered contributor trust for Vendor Y (which is new — SEC-S4-04), cross-tenant evidence isolation enforced across all three vendors (SEC-S10-01).

*O-5.* Promotions now involve three vendors' evidence. Frame transition events (CORE-A8-04) fire as promotion outcomes cross vendor boundaries. Governance-control integrity monitoring (SEC-S6-04) becomes cross-vendor: tampering with any of Vendor X, Y, or Z's control surface is detected.

**What this scenario illustrates.** The Objectives don't change between Phase 1 and Phase 2. The Commitment Profile the enterprise can publish changes: Phase 1 is a Universal Floor profile; Phase 2 extends into Extended Tier commitments (native cross-vendor evidence, cross-family verification beyond mandated surfaces). The buyer, auditor, and regulator ask the same questions at both phases — the answers get richer as the deployment matures.

**Wave 1 recovery-evidence applicability.** Wave 1 recovery-evidence additions (CORE-A2-13, CORE-A2-14, CORE-A4-06, SEC-S6-05) apply at L2+, so both phases exhibit recovery evidence assembly and enforcement-tier parity for recovery paths within their respective L-level applicability envelope. In Phase 1 the recovery evidence is within Vendor X's own estate; in Phase 2 recovery events crossing to Vendor Y or Vendor Z carry recovery evidence federated across the trust-tier boundaries per SEC-S4-04.

---

## 9. Objective-Specific Evidence Packs — Disposition

**Retired v0.5.** After completing §6 (Buyer Evidence Requests) in v0.2 and the Evidence Richness section (then §12, now §11 after v0.11 renumbering) in v0.3, the intended scope of §9 substantially overlaps with existing sections:

- **Demand-side templates for buyers**: covered in §6 with per-Objective evidence request patterns, evaluation questions, L1–L4 good indicators, and red flags.
- **Normative evidence schemas**: defined in APP-2 (A2 fields, A4 accountability chain, A6 engagement records), APP-3 (S4 write-path artifact classes, S5 telemetry privacy tiers), APP-4 (EC-07 through EC-11 entity references in PxER). Duplicating these schemas in an APP-IG-05 §9 would create a drift risk without adding value.
- **L-level-specific evidence structures**: covered in §11 with per-Objective maturity mapping.

A separate document focused on implementer-side reference evidence packs — sample filled PxER JSON, sample Frame declarations, sample Commitment Profiles with real vendor content — is potentially valuable but belongs outside this guide. A future informative companion focused on reference evidence packs may be authored under working-group direction.

§7 index reflects the retirement.

---

## 10. Illustrative Commitment Profile Language

This section provides sample Commitment Profile language for three common vendor archetypes. Samples are illustrative only; each vendor's actual Profile must reflect its own capabilities, declared conformance scope, and APP-5 conformance evidence. All samples assume the vendor publishes both the Profile and the underlying APP-5 conformance evidence per APP-0 Appendix A discipline.

Wave 1 recovery-evidence additions from v0.4 are integrated into the Universal Floor commitments (italicised inline where they extend a base commitment). Recovery-path commitments do not change the tier structure — the four Wave 1 requirements (CORE-A2-13, CORE-A2-14, CORE-A4-06, SEC-S6-05) sit in the Universal Floor, not the Extended Tier.

### 10.1 Sample Profile — Agent Builder Platform vendor

*Vendor archetype: hosts developer-built AI agents on a shared platform. Declared conformance role: Agent Builder Platform. Declared L-level: L3 for hosted agents; L2 for the platform's own governance orchestration.*

> **APP Commitment Profile — [Vendor Name] Agent Builder Platform**
>
> **Conformance scope:** Agent Builder Platform role at L3 for hosted agents; Governance Orchestrator role at L2 for platform-native workflows. Compliant conformance profile: Detective + Preventive (per APP-5 §1.3).
>
> **Universal Floor commitments (Appendix A.1):**
>
> - *Authorised Action.* Every governed action executed by a hosted agent on our platform is bound to a session-scoped agent identity encoding autonomy level, active delegation chain, HITL engagement level, and risk classification per SEC-S13-01. Cross-agent compositional authority accumulation halts and requires human re-authorisation per SEC-S2-06. Peer instructions never elevate authority per SEC-S13-03. *Recovery-path decisions extend the same three-layer accountability chain per CORE-A4-06 — recovery-initiated actions are attributable to the same intent-execution-oversight chain as primary-path actions.*
> - *Independent, Measured Verification.* Where hosted agents perform governance-critical judgments (D/P classification of compliance-relevant actions, safety-event validation, compositional-authority validation, and coordination-pattern analysis per APP-3 SEC-S3-07), the verifying agent is drawn from a structurally distinct model family maintained by the platform. Human oversight quality is measured via engagement-fidelity markers per CORE-A6-03.
> - *Bounded Agency.* Security controls are demonstrably active before hosted-agent data flows begin (Temporal Activation Ordering per SEC-XX-01). Shared substrates between hosted agents are governed per SEC-XX-02: no unsanctioned shared memory, event streams, or coordination channels. Coordination patterns across hosted agents are monitored per SEC-S7-03; anomalous patterns trigger authority reduction per SEC-XX-03. *Recovery paths for hosted-agent workflows are subject to enforcement-tier parity per SEC-S6-05: recovery cannot downgrade the compliance tier of the primary path. Where parity cannot be achieved, the recovery is classified `bypassed` and blocked from C0/C1 execution.*
> - *Execution-Time Evidence.* Process Execution Records for hosted agent activity are assembled during execution (CORE-A2-01). All three evidence integrity dimensions are verified (CORE-A2-10). Write-path provenance is signed for all six artifact classes per SEC-S4-05. *Recovery events on hosted-agent workflows include the recovery_evidence schema per CORE-A2-13 with outcome from the CORE-A2-14 vocabulary — recovery paths are audit-answerable at the same rigour as primary-path execution.*
> - *Governed Change.* Promotion of hosted agent rules from probabilistic to deterministic execution requires: evidence integrity gate (SEC-S8-01), exclusivity (SEC-S8-02), dual-human approval for C0/C1-scoped promotions (SEC-S8-03), and velocity integrity checks (SEC-S8-04). Governance-control integrity is monitored per SEC-S6-04. Evidence store is quarantined from the learning surface per SEC-S9-03.
>
> **Not yet committed:** Full Extended Tier native cross-vendor evidence federation is roadmapped for [target release]. Current conformance is L3 within platform boundaries; L4 marketplace-scale evidence federation is not claimed.
>
> **Conformance evidence:** [link to signed APP-5 conformance assertion per APP-5 §7.4 CONF-T-06].
> **Assertion frequency:** Sustained conformance evidence renewed [quarterly / on each release cycle / annually per audit cycle].

### 10.2 Sample Profile — Enterprise ERP vendor extending to AI

*Vendor archetype: existing enterprise ERP with L2 AI integration overlay. Declared conformance role: Enterprise Deployer + Governance Orchestrator (at boundary between ERP and third-party AI).*

> **APP Commitment Profile — [Vendor Name] ERP with AI Governance**
>
> **Conformance scope:** Governance Orchestrator role at L2 (brownfield deployment overlaying existing ERP). Compliant conformance profile: Retrospective + Detective (per APP-5 §1.3). Cross-vendor claim: governs boundary between our ERP and third-party AI vendors declared in the customer's supplier list.
>
> **Universal Floor commitments (Appendix A.1):**
>
> - *Authorised Action.* Authorisation to write to the ERP invoice, PO, or vendor-master records requires resolved acting identity from the calling AI system. Cross-vendor identity federation is handled per our published integration profile.
> - *Independent, Measured Verification.* We host an independent verification path drawn from a different model family than the calling AI system for governance-critical judgments landing in the ERP. Where third-party AI vendors self-verify with the same model family, our overlay flags the SEC-S3-07 gap and either applies additional review or blocks the action.
> - *Bounded Agency.* Third-party AI writing to our ERP is subject to write-path authorisation checks. Composed authority across the third-party AI + our ERP surface halts on threshold breach and requires human re-authorisation. *Where third-party AI enters a recovery path (e.g., retry after a failed ERP write), we verify enforcement-tier parity per SEC-S6-05 at our boundary: the retry path must meet the same compliance-tier requirements as the primary path, or the retry is blocked from posting compliance-relevant records.*
> - *Execution-Time Evidence.* PxER is assembled during execution across the ERP boundary. Third-party AI evidence is imported into our evidence store with declared trust tier per SEC-S4-02. Cross-enterprise entity references are limited to boundary-observable data per SEC-S14-05. *Recovery events on cross-vendor writes are captured in the recovery_evidence schema per CORE-A2-13 with outcome per CORE-A2-14 — recovery paths land in the ERP audit trail with the same evidence completeness as primary writes.*
> - *Governed Change.* Changes to AI-driven ERP write patterns (new integration templates, new invoice classification rules) go through our governed template lifecycle (SEC-S11-01a, SEC-S11-02) with version-pinning and dual-human approval for compliance-relevant templates.
>
> **Not yet committed:** L3 enhanced telemetry across all third-party AI paths (SEC-CORE-L3-01) is limited to certified AI vendors on our published integration list. Non-certified AI vendors integrate under L2 evidence only.
>
> **Conformance evidence:** [link to signed APP-5 conformance assertion].
> **Assertion frequency:** Sustained conformance evidence renewed annually with the ERP release cycle; individual integration certifications renewed per certified vendor's cycle.

### 10.3 Sample Profile — Standalone AI Governance Overlay

*Vendor archetype: brownfield governance overlay for existing enterprise deployments with heterogeneous AI. Declared conformance role: Governance Orchestrator. Declared L-level: L2 across all monitored systems; L3 available for systems with native integration.*

> **APP Commitment Profile — [Vendor Name] AI Governance Overlay**
>
> **Conformance scope:** Governance Orchestrator role at L2 across monitored enterprise systems; L3 uplift available for systems that expose our native integration surface. Compliant conformance profile: Detective (per APP-5 §1.3). Cross-vendor scope: the enterprise's declared AI vendor list.
>
> **Universal Floor commitments (Appendix A.1):**
>
> - *Authorised Action.* We attach a governance overlay session identity to every AI action observed via our monitoring integrations. Where the underlying AI vendor exposes a native identity, we federate; where it does not, we synthesize a governance identity bound to the observable authorisation chain.
> - *Independent, Measured Verification.* We host a cross-family verification service for governance-critical judgments landing in monitored systems. Enterprises may configure the verification scope by risk classification; SEC-S3-07 mandated surfaces are always verified regardless of configuration.
> - *Bounded Agency.* We provide a policy engine that halts AI actions exceeding declared boundaries. Halts are deterministic, external to the AI, and do not depend on the AI's own compliance. Coordination-pattern detection is active across the monitored surface. *When a monitored AI vendor invokes a recovery path, our overlay verifies enforcement-tier parity per SEC-S6-05 at the observed boundary. Recovery paths that would downgrade the enforcement tier are flagged and blocked from C0/C1-scoped operations.*
> - *Execution-Time Evidence.* Our overlay assembles PxER records at the boundary between the AI and downstream enterprise systems. We do not modify the underlying AI vendor's internal evidence — we add a boundary evidence layer that meets O-4 at the monitored boundary. *Recovery events observed at the boundary are captured with the CORE-A2-13 recovery_evidence schema and CORE-A2-14 outcome vocabulary. Where we cannot observe recovery events (fully-internal recovery), we declare this limitation in the CONF-D-05 conformance statement.*
> - *Governed Change.* Our overlay's own policy changes, template promotions, and rule updates are subject to governed change discipline: version-pinning, dual-human approval for compliance-relevant changes, evidence-vs-learning quarantine.
>
> **Explicit L1 scope declaration:** For monitored surfaces where we cannot observe internal AI evidence, we operate at L1 with SEC-S12-03 compliance claim limitations. In particular, L1-only monitored surfaces cannot support O-4 execution-time evidence claims; the overlay records this limitation in CONF-D-05 conformance statement as partially conformant.
>
> **Conformance evidence:** [link to signed APP-5 conformance assertion].

**Notes on all three profiles.**

- Each profile is bound to a declared conformance role, L-level, and profile (Preventive / Detective / Retrospective) per APP-5 §1.3.
- Each profile explicitly states what is NOT committed, following the discipline that undeclared non-conformance is a conformance violation (CORE-CP-04).
- Each profile references APP-5 conformance evidence rather than substituting for it (per APP-0 Appendix A discipline).
- No profile claims regulatory discharge; Appendix C of APP-0 remains the authority on the regulatory-conformance boundary.

---

## 11. Guidance on Evidence Richness at L1–L4

Per APP-1 §5 Invariant 5, the same protocol governs at every integration maturity level. What varies across levels is evidence richness, not the governance standard. This section provides concrete guidance on what evidence buyers should expect at each L-level and what "good" evidence looks like as the deployment matures.

The five Objectives (O-1 through O-5) apply identically at every L-level. The tables below describe what each Objective's evidence artefact looks like as L-level rises. Assessors and buyers can use this as a maturity map.

Wave 1 recovery-evidence additions (CORE-A2-13, CORE-A2-14, CORE-A4-06, SEC-S6-05) are L2+ applicability and appear as bold rows in the tables where they apply. L1 rows generally do not carry Wave 1 additions.

### 11.1 O-1 Authorised Action — evidence richness by L-level

| L-level | What evidence looks like |
|:---|:---|
| **L1** | Basic identity binding on each governed action. Session tokens (SEC-S13-01) may be human-only or trivial for AI. Delegation chain is generally unavailable or unidimensional. Compositional authority halt is enforceable only for simple cases. **Recovery-decision accountability not required at L1** (CORE-A4-06 L2+). |
| **L2** | Session tokens include autonomy level and declared delegation chain. SEC-S2-06 compositional authority halt is enforced across observable chains. Cross-vendor authority federation begins to appear where the enterprise has declared it. **Recovery-decision accountability chain (CORE-A4-06) enforced: recovery events with P-track or human initiator carry the full three-layer accountability chain (intent, execution, oversight) applied to the recovery decision itself.** |
| **L3** | Full delegation-invariant triad (depth per SEC-S2-05, reach per SEC-S2-06, source per SEC-S13-03) enforced structurally. Cross-family identity resolution native for multi-vendor deployments. Authority-provenance invariant enforced structurally (peer messages cannot elevate authority). **Recovery-decision accountability extends across cross-vendor recovery paths.** |
| **L4** | L3 plus marketplace-scale identity federation, cross-tenant identity isolation with formal proof, and delegation graph invariant checks. Cross-enterprise identity boundary observation applied to all cross-enterprise steps. **Recovery-decision accountability extends across marketplace-scale recovery federation.** |

**Common failure across L-levels.** At any L-level, an implementation that logs a bare "user X authorised" without the delegation chain, autonomy level, or authority source is not meeting O-1 — the log looks like evidence but does not answer "who was acting through the AI, and did they have the authority?"

### 11.2 O-2 Independent, Measured Verification — evidence richness by L-level

| L-level | What evidence looks like |
|:---|:---|
| **L1** | Basic independent verification on high-risk actions. HITL records may be present but engagement quality not measured. SEC-S3-07 cross-family verification may not apply if no AI-mediated verification is used on governance-critical surfaces. |
| **L2** | Measured HITL engagement with engagement-fidelity markers per CORE-A6-03. Canary injection (SEC-S5-02) at random intervals. Cross-family verification for the most sensitive judgment surfaces (subset of SEC-S3-07 mandated surfaces). |
| **L3** | SEC-S3-07 cross-family verification enforced structurally across all governance-critical judgment surfaces. Adversarial verification obligations (SEC-XX-04) met for all AI-mediated verification surfaces. Behavioural authenticity detection (SEC-S5-03) active. |
| **L4** | L3 plus multi-family verification quorum on the highest-risk surfaces. Behavioural detection tuned to detect emerging rubber-stamp patterns before they become systemic. Cross-vendor verification federation. |

**Common failure across L-levels.** An implementation claiming "independent verification" whose verifier is the same model family (or worse, the same weights) as the actor is not meeting O-2, regardless of L-level. This is a categorical failure, not a maturity gap.

*Wave 1 note: recovery-evidence additions do not extend O-2. This table is unchanged from v0.3.*

### 11.3 O-3 Bounded Agency — evidence richness by L-level

| L-level | What evidence looks like |
|:---|:---|
| **L1** | Basic circuit breakers on high-risk actions. Fail-closed on the most critical (C0) steps. SEC-XX-01 Temporal Activation Ordering observed but may not be verified continuously. **Recovery-path enforcement-tier invariant not required at L1** (SEC-S6-05 L2+). |
| **L2** | Comprehensive circuit breaker inventory with defined halt scopes. Substrate isolation (SEC-XX-02) enforced for enumerated shared substrates. Compliance-tiered graceful degradation across C0/C1/C2/C3/C4 per CORE-XX-01 and SEC-S7-02. **Recovery-path enforcement-tier parity (SEC-S6-05) enforced: recovery paths meet or exceed the enforcement tier of the primary path they replace; non-parity recovery paths record CORE-A2-14 `bypassed` outcome and block C0/C1 execution.** |
| **L3** | SEC-S7-03 coordination-pattern detection active. Agent-initiated safety-event channels operational (SEC-S5-06). Authority reduction on uncertainty implemented (SEC-XX-03). Independent execution trace (SEC-S7-01) verified. **Recovery-path enforcement-tier parity operational across all governance-critical surfaces; recovery-perimeter completeness (SEC-XX-01 + SEC-S6-04 + SEC-S6-05) verified against declared pressure vectors.** |
| **L4** | L3 plus multi-agent-scale coordination behaviour modelling and containment. Marketplace-scale substrate isolation guarantees with cross-tenant proof. **Recovery-path enforcement-tier parity operational across marketplace-scale recovery federation.** |

**Common failure across L-levels.** An implementation whose bounded-agency mechanism relies on the agent's compliance to stop itself is not meeting O-3, regardless of L-level. Circuit breakers must be external to and independent of the agent whose actions they bound. An additional failure mode: an implementation whose recovery paths silently downgrade compliance controls (invoke a lower-tier substitute under incident pressure) is not meeting O-3 either — SEC-S6-05 enforcement-tier parity is a categorical requirement at L2+; the `bypassed` outcome value (CORE-A2-14) is the compliant response when parity cannot be achieved, but bypassing without recording it is the categorical failure.

### 11.4 O-4 Execution-Time Evidence — evidence richness by L-level

| L-level | What evidence looks like |
|:---|:---|
| **L1** | Basic PxER with mandatory fields per CORE-A2-02. Evidence tier (SEC-S4-02) may be limited. Verification status tracked per CORE-A2-03. Boundary observation for cross-enterprise steps only (CORE-A2-11). L1 compliance claim limitations apply (SEC-S12-03). **Recovery_evidence schema not required at L1** (CORE-A2-13/14 L2+). |
| **L2** | Full 7-field conformance schema (CORE-A2-03). Three evidence integrity dimensions verified (CORE-A2-10). Signed write-path provenance for the six enumerated artifact classes (SEC-S4-05). Erasure reconciliation (SEC-S4-06) supported. **Recovery events on governed steps carry the recovery_evidence schema per CORE-A2-13 with the 6 mandatory fields (path_class, initiator, deviation_class, outcome, attempt_count, authorization_ref) and outcome from the 5-value CORE-A2-14 vocabulary (recovered / partial / failed / bypassed / self_healed).** |
| **L3** | L3 Enhanced telemetry schema (CORE-L3-01) with the 6 minimum fields. Elevated verification frequency for new L3 contributors (SEC-S4-04). Cross-tenant evidence isolation enforced (SEC-S10-01). Differential privacy for analytics (SEC-S10-01) active. **Recovery evidence carried through cross-vendor recovery paths with declared trust-tier provenance.** |
| **L4** | Marketplace-scale evidence federation with cross-vendor evidence linkage. Independent third-party evidence verification supported. Cross-vendor evidence integrity dimensions verified end-to-end. **Recovery evidence federated across marketplace-scale recovery paths.** |

**Common failure across L-levels.** An implementation whose PxER is generated on process completion (from event logs), not during execution, is not meeting O-4 regardless of L-level. Reconstruction is not assembly; the two produce different evidence with different integrity properties. Additionally: an implementation whose recovery evidence is a free-text log rather than the structured 6-field schema per CORE-A2-13 fails multi-vendor recovery reconstruction, and vendor-invented outcome values (outside the CORE-A2-14 5-value vocabulary) are non-conformant regardless of intent.

### 11.5 O-5 Governed Change — evidence richness by L-level

| L-level | What evidence looks like |
|:---|:---|
| **L1** | Basic classification provenance (CORE-A8-01) and promotion evidence (CORE-A8-02). Manual review of promotions. Lifecycle states (CORE-A9-01) tracked. |
| **L2** | Full A8 promotion lifecycle with three outcomes representable (CORE-A8-03). Dual-human approval on C0/C1 promotions (SEC-S8-03). Frame transition events (CORE-A8-04) recorded. Compliance exception re-validation on constraint change (SEC-S6-02). Autonomy-mode change elevated review (SEC-S6-03). **Recovery-path selection changes (which recovery paths a step may invoke, under what deviation classes, with what tier constraints) governed by A4-06 recovery-decision accountability chain; recovery policy modifications are Governed Change events subject to the same discipline as any other change to control logic.** |
| **L3** | SEC-S8-04 velocity anomaly detection active with elevated review path enforcement. SEC-S6-04 governance-control integrity monitoring active. SEC-S9-03 evidence-vs-learning quarantine enforced structurally. Certification lifecycle (SEC-S11-03) supported. **Recovery-perimeter integrity (SEC-XX-01 + SEC-S6-04 + SEC-S6-05) monitored: changes to recovery-path enforcement configuration flagged for review through the same elevated-review path as governance-control changes.** |
| **L4** | L3 plus cross-tenant learning boundary enforcement, formal governance-control tamper detection, and marketplace-scale change governance with cross-vendor promotion evidence. |

**Common failure across L-levels.** An implementation whose learning surface reads directly from the evidence store without a quarantine boundary is not meeting O-5, regardless of L-level. The SEC-S9-03 quarantine is not a maturity feature — it's a categorical requirement whenever learning connections exist.

### 11.6 What buyers should expect from vendor L-level uplift roadmaps

A vendor moving from L2 to L3 conformance should be able to articulate:

- Which SEC-S* requirements gain new applicability (typically SEC-S4-03/04, SEC-S3-07 scope expansion, SEC-S7-03, SEC-S8-04, SEC-S9-03).
- Which CORE-* enhancements apply (CORE-L3-01 enhanced telemetry, elevated CORE-A6-03 engagement-fidelity requirements).
- Which evidence integrity dimensions gain new depth (typically cross-tenant isolation, contributor authentication, cross-family verification structural enforcement).
- What the associated APP-5 conformance test-set expansion looks like.

Vendors unable to articulate this uplift roadmap should be treated as claiming an L-level they cannot substantiate.

**Wave 1 recovery-perimeter specific.** Wave 1 recovery-evidence requirements (CORE-A2-13, CORE-A2-14, CORE-A4-06, SEC-S6-05) are L2+ baseline; vendors claiming L2 conformance must be able to demonstrate all four. Vendors should be able to articulate their complete recovery perimeter: which SEC-* / CORE-* requirements form the perimeter against governance-weakening pressure vectors (SEC-XX-01, SEC-S6-04, SEC-S6-05), what recovery path taxonomy their `path_class` values enumerate, how they map deviation classes to recovery paths, and how their `bypassed` outcome response operates.

---

## 12. Document Status (Transitional)

### 12.1 v0.11 scope-rebalance change summary

**Change class:** Scope rebalance within APP-2026-10-RC1 — removes §10 Regulatory Crosswalks and renumbers subsequent sections. No normative changes; no change to any requirement ID or Objective definition.

**What changed:**

- **§10 Regulatory Crosswalks removed.** The former §10 (Regulatory Crosswalks (Detailed)) covered EU AI Act, ISO/IEC 42001, NIST AI RMF, and NIST SP 800-207 at article/clause level across approximately 400 lines. Standards and regulatory crosswalks are being refactored into a dedicated publication; timing is TBD. Pending that publication, standards and regulatory mapping is out of scope for this guide.
- **Section renumbering.** §11 (Illustrative Commitment Profile Language) → §10. §12 (Guidance on Evidence Richness at L1-L4) → §11. §13 (Document Status) → §12. All subsection numbering updated accordingly.
- **Pointer updates.** §1 Purpose and Scope regulatory-crosswalks bullet replaced with a brief deferral note. §5.1 Enterprise buyer / auditor / regulator path point 4 (previously "APP-IG-05 §10 regulatory crosswalks") removed; subsequent points renumbered. §5.3 and §5.4 path numbering updated for renumbered §10 and §11. §7 Section Index §10 row removed; §11 and §12 rows renumbered and annotated with pre-v0.11 numbers for reader continuity.
- **Front matter.** Suite baseline label unchanged at APP-2026-10-RC1 and baseline note trimmed to the scope-rebalance characterisation. Manifest line updates APP-IG-05 to v0.11.
- **Historical references preserved.** §9 (Objective-Specific Evidence Packs — Disposition) retains its historical narrative about v0.3-v0.5 scope decisions; section-number references within it updated to reflect current numbering with parenthetical "(then §12, now §11)" where needed for reader orientation.

**OI-18 disposition.** The former §10 opening carried OI-18 (legal-review verification of the regulatory crosswalk mappings). OI-18 is closed here with the §10 removal; any corresponding counsel-review scope follows the forthcoming dedicated publication rather than this guide.

**Compensation.** Any downstream reference to "APP-IG-05 §10 regulatory crosswalks" in APP-0 through APP-5 or in APP-IG-01 through APP-IG-04 should be removed or redirected; the standards-and-regulatory topic is not covered elsewhere in the current APP suite baseline.

### 12.2 v0.12 APP-R integration change summary

**Change class:** PATCH within APP-2026-10-RC1 — reflects the APP-R Illustrative Reference tier recognised in APP-1 §4 v1.5 and the two reference artefacts (APP-R1, APP-R2) now in the suite manifest. No normative change, no requirement ID change, no Objective-realisation content change.

**What changed:**

- **Front matter.** Companion documents list extended with APP-R1 and APP-R2. Normative-status note refined to mention Illustrative Reference Artefacts alongside Implementation Guides as informative tiers. Manifest line updated with new companion versions (APP-1 v1.5, APP-2 v5.13, APP-5 v1.10, APP-IG-01 v1.11, APP-IG-05 v0.12) and new APP-R1 v0.3.0 and APP-R2 v0.3 Draft entries.
- **§5.3 Platform implementer or vendor reading path.** New step 4 pointing to APP-R1 and APP-R2 as illustrative reference artefacts; subsequent steps renumbered. No change to §5.1, §5.2, or §5.4.
- **§6–§11 unchanged.** Buyer evidence requests, worked examples, commitment profile language, evidence richness guidance all unchanged.

**Compensation.** None required for other APP-IG documents or normative companions; APP-1 §4 is the single authoritative source for the APP-R tier definition and this document inherits from it rather than restating it.

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 0.12
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-IG-05 — Protocol Objectives Realisation and Assurance Guide.*
