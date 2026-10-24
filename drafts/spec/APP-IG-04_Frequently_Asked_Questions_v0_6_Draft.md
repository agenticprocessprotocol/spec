# APP-IG-04

Agentic Process Protocol

## Frequently Asked Questions

| | |
|:---|:---|
| **Version** | 0.6 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Type** | Informative Implementation Guidance — Topic-Based FAQ |
| **Audience** | AI platform partners · Application & ERP vendors · Agent framework owners · System integrators · Enterprise architects |
| **Companion documents** | APP-0 (Protocol Objectives) · APP-1 (Constitution) · APP-2 (Core Specification) · APP-3 (Security Architecture) · APP-4 (Entity Correlation Architecture) · APP-5 (Conformance Profiles) · APP-IG-01 (Implementor's Guide) · APP-IG-02 (Cross-Reference Matrix) · APP-IG-03 (Worked Example) · APP-R1 (Frame Schema) · APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-IG-04 is an informative topic-based FAQ for the Agentic Process Protocol. It answers common questions about scope, applicability, and adoption across stakeholder roles.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. This document does not create, modify, or override normative requirements in APP-0 through APP-5.
>
> **Use this document for:** Stakeholder-role orientation, common-question reference, terminology-discipline clarifications.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** Full APP suite.

---

## Topics Index

| # | Topic | Status | Inaugural Version |
|:---|:---|:---|:---|
| **1** | **Multi-Application Process Execution** — How Process Frames map to agents, tools, and builders when an end-to-end process spans multiple applications | ✅ Covered (v0.1) | v0.1 |
| 2 | Conformance & Certification — How to declare APP conformance; what gets certified and how | 🔜 Planned | — |
| 3 | Adoption Pathways — Choosing deployment mode and integration maturity; incremental adoption | 🔜 Planned | — |
| 4 | Agent Framework Mapping — How APP maps onto specific agent frameworks and builder ecosystems | 🔜 Planned | — |
| 5 | Cross-System Evidence Assembly — How the cross-system execution record assembles across vendor boundaries | 🔜 Planned | — |
| 6 | Compliance Scope (C0–C4) — How regulatory, industry, customer, and local rules layer in the protocol | 🔜 Planned | — |
| 7 | Security Architecture Overview — What APP-3 protects and how attackers are countered | 🔜 Planned | — |
| 8 | Entity Correlation in Practice — How entities are tracked across systems from execution data | 🔜 Planned | — |

*Topics are added as ecosystem discussions surface recurring questions. Suggestions for new topics — or refinements to existing ones — are welcome.*

---

## How to Read This FAQ

Each topic is self-contained. Read the topic relevant to your question; the others are independent. Within a topic, parts group related questions; questions within a part build on each other. Synthesis statements at the end of each part summarise the load-bearing claim.

Substantive answers reference the authoritative APP series document. This FAQ explains and contextualises; it does not replace the normative specification. For binding language, consult APP-1 through APP-5.

**Per-answer control line (v0.6):** every answer in this FAQ is subject to the following control: *"This answer is informative; where it simplifies a normative rule, the identified normative source prevails."* This is the standing disposition and applies to every Q&A whether or not the line appears in the answer text.

## Terminology Discipline *(v0.6)*

FAQs are often what vendors and enterprise buyers read first, and they are a high-probability source of stale semantic drift. The six terminology patterns below MUST NOT appear in any FAQ answer without qualification, because they simplify a normative rule to the point of contradicting it. This list is authoritative for every topic in this document:

| Prohibited unqualified phrasing | Why it's wrong | Correct phrasing |
|:---|:---|:---|
| "All security requirements MUST" or "Every security requirement uses MUST, not SHOULD" | Contradicts APP-1 Article 3 outcome/pattern distinction and APP-3's own valid Recommended Patterns. | "Every applicable security *outcome* is a MUST-level Required Outcome; security-related Recommended Patterns may use SHOULD only where a corresponding MUST-level outcome floor exists in the same section or a normative cross-reference table." |
| "Entity correlation is optional" | Ambiguous: conflates per-step use optionality with L2+ capability applicability. | "Per-step `entity_extract` is optional (use optionality); L2+ Governance Orchestrator MUST support correlation infrastructure (capability applicability). These are constitutionally different obligations." |
| "Same governance standard at L1–L4" | True at the outcome level; false if read as identical observability or testability. | "The same governance *outcomes* apply at every L-level. What varies is the available observation mechanisms, evidence completeness, and consequently the scope that can be independently demonstrated — each of which must be declared in the conformance scope." |
| "Recovery evidence is a new step in the PxER" | False. Recovery evidence attaches to the original step's PxER record. | "Recovery evidence is a `recovery_evidence` block attached to the original step's PxER record, with monotonic `sequence` for repeat recoveries, and `authorized_by` referencing a named principal per SEC-S6-04." |
| "CONFLICT is one of the mismatch types" | Misleading. CONFLICT is a classification-integrity signal that forces MISMATCH regardless of intended/actual agreement — not a compound of other mismatch types. | "CONFLICT is a classification-integrity signal. When CONFLICT is detected, `conformance_status` MUST be MISMATCH even if `dp_classification_intended` and `dp_classification_actual` agree." |
| "DEGRADED means missing evidence" | False. DEGRADED specifically denotes governance-layer unavailability. | "DEGRADED denotes governance-layer unavailability (per CORE-A2-04a). It is NOT a generic missing-field status; missing-field or malformed-evidence conditions are recorded per the applicable A2 schema and APP-5 profile, not as DEGRADED." |

Authors and reviewers of FAQ answers verify against this table before publication. Answers using unqualified prohibited phrasings are non-conformant with the FAQ's editorial discipline and MUST be rewritten.

---

# Topic 1 — Multi-Application Process Execution

> **Sub-title:** How Process Frames map to agents, tools, and builders across the enterprise.
> **Source:** APP-2 §3.1, §3.2, §3.8, §4.3, §4.4 · APP-IG-01 §6.5
> **Status:** Inaugural topic — v0.1 May 2026 (source snapshots refreshed to Sep 2026 baseline in v0.3)

## Preamble

This topic addresses a question that arises consistently during APP review: **when an end-to-end process spans multiple applications — each offering its own agents, skills, tools, and agent builders — how does APP determine which platform runs which part of the process?**

It is a question with two layers. The **architectural layer** asks how the Process Frame designates step execution. The **market layer** asks whether APP reinforces existing anchor-platform patterns (where one vendor's agent builder dominates a process) or breaks them.

The protocol's answer is structurally neutral on both layers. This topic explains why, and what that neutrality means for adopters depending on their role in the stack.

> *MCP connects agents to tools. A2A connects agents to each other. APP connects agents to governed processes. Three protocols, three different problems, one coherent stack.*

---

## Part A — How APP Designates Step Execution

### Q1.1 Does APP designate which agent builder invokes which step of a process?

**No.** APP is deliberately neutral on builder identity. The Frame names the **executing system** per step (where the step runs in the enterprise landscape) and the step's **D/P classification** (whether it executes deterministically or probabilistically). It does *not* name the agent builder, the orchestrator, or the invocation platform. The mapping from a Frame section to a specific agent builder is an implementation choice at the deployment layer — not a protocol commitment.

This is intentional. A protocol that bound steps to specific builders would calcify the current vendor topology into the standard. APP standardises the contract; the market decides the builder.

### Q1.2 What does the Frame actually specify per step?

Per APP-2, every conformant Process Frame must include, per step:

| Attribute | Determines |
|:---|:---|
| Step identifier | Identity in the process DAG |
| Executing system | Where the step runs in the enterprise landscape |
| Intended D/P classification | Whether the step is rule-based or judgment-dependent |
| Dependency chain | Sequencing and parallelism |
| Accountability owner | Who is answerable |

Recommended additions include compliance constraints, HITL engagement requirements, SLA definitions, and entity declarations. None of these names a builder, a platform, or an orchestrator.

### Q1.3 If the Frame doesn't assign steps to builders, how does a step end up at a specific builder?

Three mechanisms together — none of them is "the Frame assigns it":

1. **Executing-system reality.** If the Frame declares step S executes in a given system, the agents that can execute S are physically constrained to those with reach into that system. In principle, any builder with the right connector qualifies. In practice, the system's native builder has the deepest integration; certified connectors come next; external agent platforms last.

2. **The standardised integration surface.** The Frame is consumed via a contract identical for every builder. Any conformant builder reads the same Frame, invokes the same governance checks, and submits evidence the same way. The protocol grants no builder privileged access to "its own" steps.

3. **The inbound governance gate.** When a builder contributes governance data back to the Frame, the gate classifies the contribution as governance-complete, partial, or absent. Cross-system changes must route through the Frame; intra-system changes may merge directly only when governance-complete. This is the firewall against any builder silently rewriting the Frame for steps it considers its own.

### Q1.4 Is APP a competing orchestration runtime?

**No.** APP is the governance layer that makes orchestration accountable across vendor boundaries. It does not execute steps. It does not route work. It does not own the runtime. APP defines what a governed process must demonstrate — specification fidelity, classification declaration, evidence chain, oversight quality, accountability attribution — and leaves the execution mechanics to whichever platform, framework, or vendor agent invokes the process.

> *Both may orchestrate.* — APP-2, on the relationship between governance implementation and agent system at L2 integration maturity

Multiple realisation patterns are conformant: dedicated orchestrator, native embedding, sidecar/observer, retrospective audit. The protocol does not prescribe.

**Synthesis:** *The Frame is system-aware but builder-agnostic. Builder selection happens at the deployment layer through connector reach and market preference, not through protocol assignment.*

---

## Part B — The Two Market Patterns

### Q1.5 In a process where one platform dominates — an ERP-anchored Order-to-Cash, a CRM-anchored opportunity-to-cash — does APP let that platform's builder anchor the process?

**Yes.** APP explicitly preserves this pattern. At L2 — where most enterprise processes operate today, including ERP-anchored processes typically orchestrated through builders like SAP Joule and CRM-anchored processes typically orchestrated through builders like Salesforce Agentforce — governance and agent system relate as "both may orchestrate." A vendor's agent builder can continue to anchor a process in its own scope, consuming the Frame via the standardised integration surface, invoking its native skills, calling external tools as needed, and contributing execution evidence back.

What APP changes is not who orchestrates. It is what the orchestration produces. Governance attributes attached to the Frame propagate to the anchor builder automatically; the anchor's execution produces a cross-system execution record assembled across all participating systems; the anchor's tool calls into other vendor systems carry governance context. **The anchor builder remains primary. The cross-vendor governance gap closes.**

**Concrete example.** A global manufacturer runs Order-to-Cash dominated by SAP. Joule plays anchor. APP reads as follows: the Frame declares steps with their executing systems (SAP modules, the CRM for customer records, a logistics vendor portal for shipment); the integration surface publishes the Frame to Joule; Joule orchestrates per Frame; the cross-system execution record assembles Joule's execution data alongside records from the CRM and the logistics portal. The anchor pattern continues. The governance surface unifies.

### Q1.6 In a process with no natural anchor — a data-layer-led architecture, multi-cloud, a post-M&A heterogeneous estate — what coordinates the process?

The Frame itself becomes the coordination contract. The Frame is the canonical interchange format; any compliant agent builder reads from it; no platform owns the specification. Each participating builder picks up the sections where its connector reach is deepest. The Frame ensures none silently re-classifies steps, skips governance gates, or fabricates evidence.

This is the segment where APP delivers the largest standalone value: cross-system, compliance-governed, accountability-required processes where no single vendor solves the coordination problem natively.

**Concrete example.** A global insurer runs claims adjudication across a policy/claims platform, a hyperscaler-hosted data lake (fraud signals, actuarial models), a service-management platform (case workflow), and a finance ERP (posting). No vendor has the scope dominance to play anchor. The Frame declares each step with its executing system; multiple agent builders consume the Frame in parallel; the cross-system execution record assembles execution evidence from all participants; the inbound governance gate prevents any one builder from rewriting the spec to suit its model. **The process exists, coherently, because the Frame makes it cohere.**

### Q1.7 Does this mean APP picks winners between agent builders?

**No.** The two market patterns coexist under the same protocol. In dominant-anchor cases, APP consolidates governance across the anchor and the other systems it touches. In no-anchor cases, APP coordinates execution that would otherwise lack a coherent specification. **The protocol's value differs by pattern; its mechanics do not.**

| Dimension | Dominant-Anchor Process | No-Anchor Process |
|:---|:---|:---|
| APP role | Consolidates cross-vendor governance | Provides the coordination contract |
| Primary orchestrator | Vendor's anchor builder | The Frame itself (consumed by multiple builders) |
| Where APP creates new value | Cross-vendor governance evidence, compliance attribution | Process coherence, execution record, governance gates |
| Builder relationship to APP | Anchor reads Frame; APP aggregates | Co-equal participants read Frame; APP coordinates |

**Synthesis:** *APP intentionally fits both market structures. It does not require enterprises to abandon their dominant-platform investments, and it does not require platforms with no natural process dominance to invent one.*

---

## Part C — Will APP Reinforce Anchor-Platform Patterns?

### Q1.8 Will APP reinforce the pattern of the Frame "landing on" specific agent tools per process?

**Not at the protocol layer. At the deployment layer, the pattern may persist where connector economics and existing scope dominance already make it the rational choice — but the protocol contains specific mechanisms that prevent the pattern from hardening into builder lock-in.**

Three design choices preserve neutrality:

1. **Capability-abstraction discipline.** In two of the three deployment modes — packaged native applications and bespoke native builds — the Frame names *capabilities* rather than concrete systems. Concrete system bindings live in a deployment-specific overlay. The same Frame can drive a vendor anchor in one tenant and a different builder in another tenant where the capability resolves against a different system. Frame validation enforces this with a blocking check.

2. **Consumption-mode parity.** The same governance applies regardless of how a step is invoked — copilot interaction, autonomous agent execution, A2A delegation. D/P classification is invariant across modes; agents inherit it from the Frame and cannot override it. No builder can claim a step by re-classifying it as "its kind of work."

3. **Integration surface as governance contract, not exposure.** The integration surface constrains what every builder does *with* the Frame; it does not pre-grant any builder a privileged channel. The bidirectional governance gate is the enforcement mechanism.

### Q1.9 What stops a vendor from extending the Frame schema with vendor-specific attributes, eroding neutrality silently?

The inbound governance gate. Contributions that introduce non-conformant attributes are classified — governance-complete, partial, or absent. Partial and absent contributions route to enrichment and human review. Cross-system changes must route through Frame mediation; intra-system changes may merge directly only when governance-complete.

This is the explicit firewall against vendor-flavoured Frame drift. It also makes vendor extensions **visible** — extensions that go through the gate are subject to review; extensions that bypass the gate are non-conformant and excluded from the cross-system execution record.

### Q1.10 Where does deployment-layer builder anchoring legitimately remain?

Two places:

- **Native protocol embedding.** When a vendor implements APP natively in their application — full protocol conformance with governance by construction — steps in that system are de facto owned by that builder. This is the AI-native maturity case. Cross-system steps still span others, and parity at the boundary is mandatory.

- **Connector economics.** Agents with certified, high-fidelity connectors run their native steps with the lowest cost and latency. Markets sort this. The protocol does not impede the sorting. It denies the winner any *governance* privilege — connector efficiency does not translate to specification authority.

**Synthesis:** *APP is a neutral substrate by design choice, not by accident. Where builder anchoring re-emerges, it does so as a market outcome — not a protocol commitment.*

---

## Part D — What This Means for Adopters

### Q1.11 As an AI platform — what changes for us if our agents adopt APP?

You gain access to the governed process specification your agents consume, the cross-system execution record that produces audit-ready evidence, and variable-fidelity governance that adapts to enterprise systems at any integration depth. **Your agents become regulator-ready without your platform building the governance layer itself.**

You give up nothing structural. APP is not a competing orchestration runtime. Your agents orchestrate as they do today; the protocol provides the specification they read from and the evidence schema they contribute to. The model layer, the agent framework, the orchestration runtime, the developer experience — all remain yours.

### Q1.12 As an application or ERP vendor — what changes for us?

Your agent builder receives governed specifications automatically through the standardised integration surface. Governance changes propagate without custom integration. Your intra-application telemetry enriches the cross-system execution record. **Your platform becomes governance-grade across the processes that cross your boundary.**

You give up nothing within your scope. The protocol governs the space *between* systems — the cross-vendor processes that no single application owns. Your native automation, your in-app workflows, your agent skills continue to operate as designed. APP makes them legible to a governance layer that spans vendors.

### Q1.13 As a system integrator or agent framework owner — what changes for us?

Process design becomes a reusable asset. The Frame is the specification; multiple framework runtimes consume it. SIs that author or operate Frames acquire portable IP. Framework owners that conform to the integration surface participate in any APP-governed process without vendor-specific integration work.

> *Process design becomes a reusable asset deployed in weeks, not a per-project consulting artefact rebuilt from scratch.*

**Synthesis:** *APP shifts value from per-deployment integration to standardised governance infrastructure. Every role in the ecosystem gains. None loses what was theirs.*

---

# Closing Note

The questions in this FAQ are the ones that arise consistently during APP review and ecosystem discussion. The answers reflect the protocol's current published specification (APP-1 through APP-5, plus the APP-IG implementor guidance series) and the design intent behind it.

The protocol is open. A reference implementation exists. Multiple deployment modes are supported. This FAQ grows topic by topic as new questions surface — the Topics Index above tracks both what is covered and what is planned.

Ecosystem reviewers with questions not addressed in any current topic are encouraged to submit them. The aim is for this FAQ to become the canonical reference for the questions that recur across discussions, with each answer grounded in the authoritative APP series.

For topics beyond this FAQ's current scope, consult: **APP-2 (Core Specification)** for protocol capabilities and conformance; **APP-3 (Security Architecture)** for security obligations; **APP-4 (Entity Correlation Architecture)** for cross-system entity tracking; **APP-IG-01 (Implementor's Guide)** for adoption guidance; **APP-IG-02 (Cross-Reference Matrix)** for requirement-level navigation across the normative series; **APP-IG-03 (Worked Example)** for end-to-end deployment illustration.

Feedback from review partners is welcome and informs both subsequent topic additions to this FAQ and subsequent protocol revisions.

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 0.6
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-IG-04 — Frequently Asked Questions.*
