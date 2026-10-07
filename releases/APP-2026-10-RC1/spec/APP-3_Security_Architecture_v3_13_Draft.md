# APP-3

Agentic Process Protocol

## Security Architecture

| | |
|:---|:---|
| **Version** | 3.13 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Audience** | Security architects, protocol implementors, ERP vendor security teams, enterprise CISOs |
| **Normative status** | This document is normative. Equal standing with APP-2. Governed by APP-1. |
| **Companion documents** | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-2 (Core Technical Specification), APP-4 (Entity Correlation), APP-5 (Conformance Profiles), APP-IG-02 (Cross-Reference Matrix), APP-R1 (Frame Schema), APP-R2 (MCP Binding Reference Design) |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) |
| **Manifest** | See APP-1 Constitution for the current suite manifest. |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. Version bumps require concurrent manifest regeneration; adding a version to the manifest without concurrent bump of that document, or vice versa, is a release-control defect. |
| **Version-reference convention** | Companion documents cited by name only in body prose. Manifest above is the sole non-historical source for companion versions. Version numbers persist in body prose only for historical claims about specific past changes. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-3 is the normative security architecture of the Agentic Process Protocol. It defines security requirements across fourteen domains (S1 through S14) and cross-cutting security principles.
>
> **Status:** Normative. Requirements expressed using RFC 2119/8174 keywords are binding within the declared scope.
>
> **Authority and precedence:** Governed by APP-1. Article 3 of APP-1 governs security normativity: security outcomes are always MUST; security mechanisms may be SHOULD only where a corresponding MUST-level outcome establishes the floor.
>
> **Use this document for:** Security requirement IDs (SEC-Sn-nn, SEC-XX-nn), security-domain scope definitions, outcome-versus-mechanism classifications, cross-cutting security principles.
>
> **Related documents:** APP-0 (security objectives), APP-1 (constitutional authority and Article 3 discipline), APP-2 (capability integration points), APP-4 (entity-correlation security implications), APP-5 (role-based security applicability).

---

## How to Read This Document

Normative elements are classified at exactly one of three specificity levels, as required by APP-1 Article 4:

| Marker | Level | Meaning |
|:---|:---|:---|
| **[Required Outcome]** | What must be true | Verifiable outcome using MUST. Any conformant mechanism qualifies. |
| **[Recommended Pattern]** | How the protocol suggests achieving it | Expressed using SHOULD. Alternatives documented. Deviation requires justification. |
| **[Reference Mechanism]** | A specific mechanism proposed | Informative. Working group starting point. |

This document uses RFC 2119/8174 normative keywords. MUST, SHOULD, MAY in all capitals carry their defined meanings.

Per APP-1 Article 3: every applicable **security outcome** is a MUST-level Required Outcome. A security-related Recommended Pattern may use SHOULD only where this specification identifies the corresponding independently testable MUST-level outcome floor. Applicability by role and L-level is defined in APP-5; non-applicability is not optionality. Reference Mechanisms in this specification appear only where interoperability requires convergence on a specific technical choice (e.g., cryptographic algorithms that must match across system boundaries). APP-1 Article 4 defines the full rationale for the three-level system.

**Recommended Pattern → MUST-level outcome floor cross-reference.** Every security Recommended Pattern in this document identifies its corresponding Required Outcome floor. This is not merely informative — it is the constitutional requirement of APP-1 Article 3. The following table lists every current security RP and its floor:

| Recommended Pattern | MUST-level security outcome floor | Location |
|:---|:---|:---|
| SEC-S1-05 (semantic validation on D/P reclassification) | Reclassified as informative guidance in v3.13 (no direct testable floor identified; see §4.1 note) | §4.1 |
| SEC-S2-05 (delegation-depth cap) | SEC-S2-06 (compositional authority accumulation) + SEC-S13-03 (authority-provenance invariant) + SEC-XX-05 (safe-state on aggregate-authority breach) | §4.2 |
| SEC-XX-03 (runtime authority-reduction modes) | SEC-XX-05 (minimum safe-state transition on detected severe events) | §2.3, §2.5 |
| SEC-S10-03 (telemetry-storage integrity checks) | Reclassified as informative guidance in v3.13 pending explicit floor identification | §4.10 |

Additional Recommended Patterns without an identified floor MUST either be reclassified as informative guidance or paired with a Required Outcome in the next revision. This table is generated by inspection and MUST be regenerated whenever an RP is added or reclassified.

This specification defines security REQUIREMENTS — what must be true. How implementations achieve these requirements is an implementation choice except where a Recommended Pattern or Reference Mechanism is specified. The protocol publishes requirements openly to establish the compliance floor; implementation quality is the competitive differentiator.

Security requirement IDs use the `SEC-Sn-nn` convention (S = security domain number, nn = sequence within domain). Cross-cutting requirements use `SEC-XX-nn`. The Master Security Requirement Index (Appendix A) maps each ID to the APP-2 capability it protects, its specificity level, and L-level applicability.

When referenced from documents outside the APP series, prefix with `APP-` (e.g., `APP-SEC-S1-01`). APP-2 core requirements use `CORE-An-nn`.

---

## 1. Introduction

### 1.1 Scope

The Agentic Process Protocol sits at the intersection of three novel attack surfaces: an agent integration layer (APP-2, A1), a compliance evidence record infrastructure (APP-2, A2 PxER), and a human oversight system (APP-2, A6 HITL). External research — including OWASP, Palo Alto Unit 42, Invariant Labs, CrowdStrike, Checkmarx, CSA, and NIST — confirms that each area maps to active, documented threat vectors with public proof-of-concept exploits (see References).

This specification defines security requirements across **fourteen security domains** (S1–S14), each targeting a specific vulnerability class in governed process execution:

| Domain | Name | Protects | Summary |
|:---|:---|:---|:---|
| **S1** | Frame Integrity | A0, A1 | Poisoning, rollback, and input provenance attacks on governed process specifications |
| **S2** | Transport & Federation | A1, A7 | MCP/A2A transport vulnerabilities and Agent Card federation risks |
| **S3** | Classification Integrity | A3 | D/P classification oracle attacks that silently bypass governance |
| **S4** | Evidence Integrity | A2 | PxER truthfulness, contributor authentication, and write-path provenance |
| **S5** | Human Oversight Security | A6 | LITL attacks on approval surfaces and engagement telemetry privacy |
| **S6** | Compliance Validation | A5 | Missing constraints ("negative space") in the C0–C4 framework |
| **S7** | Orchestration Integrity | Cross-cutting | Orchestration layer compromise and compliance-tiered degradation |
| **S8** | Promotion Integrity | A8 | Evidence gaming to trigger premature P→D promotion |
| **S9** | Feedback Loop Integrity | A8–A11 | Corrupted evidence feeding governance-weakening advisory outputs |
| **S10** | Tenant Isolation | A11 | Cross-deployment leakage in anonymised benchmarking |
| **S11** | Supply Chain Security | A0 | Poisoned Frame templates in marketplaces |
| **S12** | L1 Integration Security | A2 (L1) | Security vacuum at the screen/RPA integration level |
| **S13** | Agent Identity | A1, A2, A4, A7 (cross-cutting identity binding) | Non-deterministic session identity for AI agents |
| **S14** | Entity Correlation Security | APP-4 | Entity extraction, correlation, and registry security (EC-38–EC-47) |

### 1.2 Relationship to APP-2

APP-2 defines protocol capabilities (A0–A11). Each capability section in APP-2 includes a security callout referencing this document. Appendix B of APP-2 maps APP-3 security domains to APP-2 capabilities. This document provides the normative requirements those callouts reference.

---

## 2. Principles

### 2.1 Temporal Activation Ordering

**[Required Outcome · SEC-XX-01]** For any protocol-defined data flow, security controls governing that flow MUST be demonstrably active before (or simultaneously with) the data flow's activation. Implementations MUST NOT activate a data flow during the window between deployment and security control readiness.

This applies to: PxER evidence acceptance, L1 telemetry ingestion, cross-deployment analytics, feedback loop advisory generation, and Agent Card federation export.

How ordering is enforced is an implementation choice. A conforming implementation that allows governance-relevant data flow without corresponding security controls is non-conformant.

### 2.2 Substrate Isolation

**[Required Outcome · SEC-XX-02]** Substrate isolation. Any substrate an agent can both write to and observe within the implementation's execution boundary MUST be enumerated in an implementation-published substrate inventory and MUST support isolation-by-default across concurrent agent sessions. Non-enumerated agent-writable-and-observable surfaces are non-conformant.

The inventory MUST include, at minimum: shared caches accessible to multiple agent sessions, message queues, event buses, file systems, package repositories, and any other named substrate accessible to more than one concurrent agent. Substrates added post-inventory-publication MUST be added to the inventory before agent write-access is enabled.

Isolation mechanism is an implementation choice. Enumeration and isolation-by-default are not.

**Rationale.** Any substrate meeting the write-and-observe criterion is, by construction, a communication channel — regardless of whether it was designed as one. Implementations typically isolate the substrates they have identified as communication channels; the residual risk class is substrates that meet the criterion but were not identified as such at design time (shared caches, package repositories, telemetry buses used for status but writable for logs, etc.). The failure mode of concern is not "known channel breached" but "unenumerated substrate discovered to be a channel." SEC-XX-02 makes enumeration a requirement, not a design choice, and treats any qualifying surface as a communication channel by construction. Isolation-by-default across concurrent agent sessions is the containment; enumeration is the discipline that keeps the containment complete over time.

**Implementation choices.** Substrate-inventory format, isolation mechanism (per-agent namespacing, RBAC, RLS, TTL semantics), adversarial verification schedule, and inventory-review cadence are implementation choices.

### 2.3 Authority Reduction on Uncertainty

**[Recommended Pattern · SEC-XX-03]** Authority reduction on uncertainty. Implementations SHOULD declare and enforce runtime authority-reduction modes triggered by governance-critical events. Recommended mode set: (a) restricted (following an agent-initiated safety event per SEC-S5-06, pending human acknowledgement) — read-only, evidence preservation, low-risk deterministic work; (b) fail-safe restricted (safety-event delivery failure) — no privileged, external, or write actions; (c) quarantined collaboration (covert-channel suspicion per SEC-XX-02) — no peer messaging, no shared-substrate writes; (d) held (aggregate-risk threshold breached per SEC-S2-06) — no further correlated action until re-authorization; (e) detection degraded (baseline poisoning suspected per SEC-S7-03) — freeze adaptive baseline updates, use static policy.

**Conditional obligation.** Where an implementation implements or declares runtime authority-reduction modes, each transition MUST be recorded in PxER using the SEC-XX-05 eight-field governance-event schema (see §2.5). The universal evidence requirement is SEC-XX-05; SEC-XX-03 is a mechanism SHOULD only. An implementation that declines SEC-XX-03's mode set entirely MUST still satisfy SEC-XX-05.

**MUST-level floor.** SEC-XX-05 (§2.5) is the corresponding Required Outcome: on a detected severe event, an implementation MUST NOT continue privileged actions without human acknowledgement or safe-state authorization. SEC-XX-03 (this pattern) defines a richer graduated mode set that satisfies SEC-XX-05 by construction; an implementation MAY define its own mode set instead but MUST still meet SEC-XX-05. Alternative: threshold-only response without mode transitions — conformant with SEC-XX-05 provided the threshold check enforces the required halt on severe events, but produces retrospective analytics signal rather than the graduated runtime containment of SEC-XX-03. Where an implementation declares runtime authority-reduction modes, the modes MUST be recorded in PxER at transition.

**Rationale.** The alternative to runtime authority reduction — proceeding at declared authority until a human intervenes — creates the exact conditions under which incident escalation depends on the agent choosing to report rather than the runtime enforcing restraint. Authority reduction on uncertainty converts detection into runtime behavior rather than observational function. The mode set structure varies by implementation architecture (queue-based systems differ from continuous-loop agent systems); the runtime-containment category is what this pattern establishes, not any specific mode set.

**Implementation choices.** Specific mode boundaries, transition thresholds, hysteresis/debouncing, and mode-composition semantics are implementation choices.

### 2.4 Adversarial Verification Obligation

**[Required Outcome · SEC-XX-04]** Adversarial verification obligation. Every conformant implementation MUST maintain a named adversarial exercise suite covering the security-relevant properties of this specification and MUST execute the suite at least: (a) pre-release for any implementation version affecting a Required Outcome, and (b) on operational cadence declared in the implementation's conformance profile. Exercise evidence — pass/fail, coverage, remediation status — MUST form part of the implementation's assurance record and be available to conformance auditors.

Minimum exercise coverage: hidden communication through enumerated shared substrates (SEC-XX-02); peer-authority elevation attempts (SEC-S13-03); safety-event suppression or overload (SEC-S5-06); aggregate-cap breach through low-materiality accumulation (SEC-S2-06); baseline poisoning over multi-day windows (SEC-S7-03); safety-event delivery failure (SEC-XX-03 fail-safe mode); minimum safe-state transition on detected severe events (SEC-XX-05); trusted-source exclusion abuse where the implementation exposes such a mechanism.

Absence of an adversarial exercise suite is non-conformant. Passing exercises without corresponding evidence records is non-conformant. Exercise coverage that does not include the minimum set is non-conformant unless the omitted class is architecturally inapplicable to the implementation (documented rationale required).

**Rationale.** Structural invariants provide meaningful containment only where they are complete and enforced. Adversarial verification treats containment as a category of engineering discipline: enumerate the ways it might fail, run the exercises, document the outcomes. Without this, structural claims degrade over time as implementations evolve past their original threat models. The minimum coverage set is not exhaustive — it is the floor that ties this specification's Required Outcomes to executable verification, and MUST expand as implementations discover new failure modes.

**Implementation choices.** Exercise methodology, red-team engagement model, coverage measurement, evidence format, and remediation workflow are implementation choices.

### 2.5 Minimum Safe-State Transition on Detected Severe Events

**[Required Outcome · SEC-XX-05]** *(added v3.10; strengthened v3.11)* Minimum safe-state transition on detected severe events. On the detection of a **severe governance-critical event** — defined at minimum as any of (a) an agent-initiated safety event delivered per SEC-S5-06, (b) a covert-channel suspicion event raised per SEC-XX-02, (c) an aggregate-authority threshold breach per SEC-S2-06, (d) a baseline-poisoning suspicion event raised per SEC-S7-03, or (e) a peer-authority elevation attempt detected per SEC-S13-03 — the implementation MUST NOT continue privileged actions on behalf of the affected agent, session, or delegation chain until one of: (i) explicit human acknowledgement of the event, or (ii) authorization to enter a defined safe-state per an implementation-declared authority-reduction mode set (see SEC-XX-03).

**Transition timing.** The safe-state transition MUST take effect before the *next* privileged action attributable to the affected agent, session, or delegation chain executes. Implementations MAY declare a maximum transition latency (e.g., "within 250 ms of detection") for observability purposes, but the normative test is action-ordering: no privileged action MAY execute between the detection event and the safe-state entry. Concurrent in-flight actions initiated before detection MAY complete, but their PxER records MUST carry the detection event's identifier in `governance_events` for audit continuity.

**Prohibited actions in safe state.** Once in safe state, the affected agent, session, or delegation chain MUST NOT: write to external systems; initiate financial actions; act on compliance-critical (C0/C1) records; act on other agents' sessions or delegation chains; delegate authority to other agents; modify governance-layer configuration; or invoke any capability requiring HITL engagement per CORE-A6-03. Read-only observation, evidence preservation, and low-risk deterministic maintenance work MAY continue.

**Re-authorisation condition (safe-state exit).** Exit from safe state MUST be gated by one of: (i) explicit human acknowledgement recorded per SEC-S5-06's evidence contract, referencing the triggering severe event's identifier and stating the acknowledger's disposition (resume, terminate, escalate); (ii) authorization from the governance-control identity that authorized the safe-state entry, only where the entry authoriser is human or a governance-declared automation with an authoriser-of-record identity (SEC-S6-04); or (iii) expiry of a declared containment window with automatic escalation to human review — an implementation MAY define such a window but MUST NOT permit automatic resumption without human contact. Silent expiry with autonomous resumption is non-conformant.

**PxER evidence.** The safe-state transition MUST be recorded in PxER as a governance event with the eight-field schema: (a) `triggering_event_id`, (b) `severe_event_class` (from the five enumerated classes), (c) `affected_scope` (agent, session, or delegation chain identifier), (d) `state_entered` (implementation-declared safe-state label), (e) `entry_principal` (the identity authorising entry, or `automatic` where D-track initiated), (f) `entry_timestamp`, (g) `prohibited_actions_baseline` (the applied prohibition set — MAY reference this specification by ID), and (h) `exit_condition_declared` (which of (i)/(ii)/(iii) above governs re-entry). The exit event MUST be recorded with `exit_principal`, `exit_timestamp`, and `exit_disposition` (resume/terminate/escalate). **A2 state-machine intersection:** any step whose execution is interrupted by a governance-unavailability condition — including detection of a severe event that triggers safe-state entry mid-step — MUST have its `conformance_status` set to DEGRADED, mapping to state C10 in APP-2 CORE-A2-04b. The step's PxER record carries both this `governance_events` block (via the extension-point registry in APP-2 §3.4.0) and its DEGRADED conformance state.

Privileged actions in scope of this requirement include, at minimum: write actions to external systems, financial actions, actions affecting compliance-critical (C0/C1) records, actions affecting other agents' sessions or delegation chains, and any action requiring HITL engagement per CORE-A6-03.

**Rationale.** Under APP-1 Article 3, a security-related SHOULD requires a corresponding MUST-level outcome floor. SEC-XX-03 (authority reduction on uncertainty) is a mechanism defining a *rich* mode set for graduated response to governance-critical events; without a floor, an implementation could decline the mode set entirely and continue privileged actions during detected severe events. SEC-XX-05 establishes the floor: continued privileged action after a detected severe event, without explicit acknowledgement or safe-state authorization, is non-conformant. Implementations that adopt SEC-XX-03's fuller mode set satisfy SEC-XX-05 by construction; implementations that decline it MUST still meet SEC-XX-05's minimum safe-state transition.

**Implementation choices.** Detection sensitivity thresholds beyond the enumerated events, the mode set structure (implementations MAY adopt SEC-XX-03's five modes or define their own), the acknowledgement UI, transition-latency SLA, and safe-state resumption workflow are implementation choices.

### 2.6 Three Evidence Verification Dimensions

PxER step records carry three independent verification dimensions (APP-2, CORE-A2-10). None should be merged — they answer different trust questions:

| Dimension | Question | Defined In |
|:---|:---|:---|
| **D/P Conformance** | Executed on intended D/P track? | APP-2 CORE-A2-03 |
| **Evidence Authenticity** | Is the telemetry contribution authentic? | SEC-S4-01 (this document) |
| **Write-Path Provenance** | Was the record produced by an authorised service? | SEC-S4-05 (this document) |

---

## 3. Threat Model Overview

The diagram maps each security domain (S1–S14) to its attack surface on the protocol architecture stack. Sections in §4 follow this sequence.

```
┌─────────────────────────────────────────────────────────────────┐
│  AGENT BUILDERS (orchestration clients)                          │
│  ├── Inbound integration (A1)     ──── S1  Frame Integrity       │
│  ├── Source documents              ──── S1  Input Provenance      │
│  ├── Agent Cards / A2A / MCP      ──── S2  Transport & Federation│
│  └── Notification channel          ──── S1  Frame Rollback        │
├─────────────────────────────────────────────────────────────────┤
│  GOVERNANCE LAYER                                                │
│  ├── D/P Classifier (A3)          ──── S3  Classification        │
│  ├── PxER Assembly (A2)           ──── S4  Evidence Integrity     │
│  ├── Approval Surface (A6)        ──── S5  HITL Security          │
│  ├── Compliance Validation (A5)   ──── S6  Compliance Validation  │
│  ├── Orchestration Layer          ──── S7  Orchestration          │
│  ├── P→D Promotion (A8)          ──── S8  Promotion Integrity    │
│  ├── Feedback / Advisory Loop     ──── S9  Feedback Loop          │
│  └── Cross-Deployment (A11)       ──── S10 Tenant Isolation       │
├─────────────────────────────────────────────────────────────────┤
│  ENTERPRISE APPS / ERP                                           │
│  ├── Templates / Marketplace      ──── S11 Supply Chain           │
│  └── L1 Screen/RPA                ──── S12 L1 Security            │
├─────────────────────────────────────────────────────────────────┤
│  CROSS-CUTTING DOMAINS (first-class, span layers)                │
│  ├── Agent Identity                ──── S13 Agent Identity         │
│  ├── Entity Correlation            ──── S14 Entity Correlation Sec │
│  └── Temporal Ordering             ──── SEC-XX-01 (§2.1)          │
└─────────────────────────────────────────────────────────────────┘
```

*S13 and S14 are first-class security domains (each with normative requirements in §4.13 and §4.14 respectively). They appear grouped in the diagram because their scope spans multiple architectural layers rather than because their normative weight is lesser. SEC-XX-01 (Temporal Activation Ordering) is a cross-cutting **principle** rather than a domain — see §2.1.*

---

## 4. Security Requirements by Domain

### 4.1 S1 — Frame Integrity

*Protects: APP-2 A0 (Process Frame), A1 (Integration Surface)*

**Threat.** A poisoned Frame can reclassify P-track steps as D-track (bypassing HITL), strip compliance constraints, or inject invisible dependency chains. Frame version rollback causes execution against weaker constraints. Upstream source documents can be poisoned before Frame construction begins.

**[Required Outcome · SEC-S1-01]** All Frame mutations submitted via the integration surface MUST carry a digital signature using a protocol-approved algorithm (Appendix B), linked to the submitter's registered identity. Unsigned or invalid submissions MUST be rejected.

**[Required Outcome · SEC-S1-02]** Frame mutation provenance chain: an append-only record of every signed change, authoriser, and governance classification. Every mutation is a verifiable link.

**[Required Outcome · SEC-S1-03]** Monotonic version enforcement. Frame consumers MUST reject any version lower than their last-applied version. Rollbacks MUST require explicit governance approval. Unauthorised backward transitions MUST be blocked.

**[Required Outcome · SEC-S1-04]** Source document provenance. Frame construction MUST NOT proceed from source material lacking verified provenance — cryptographic hash registration and submitter identity linked. The provenance chain extends backward from the first Frame mutation to the source material.

**[Informative Guidance · SEC-S1-05]** Semantic validation of Frame attributes at submission — not structural completeness only. A D/P reclassification is a governance-impacting event and a mature implementation is encouraged to trigger elevated governance review on reclassification. **Constitutional classification note.** This pattern is classified as Informative Guidance rather than a Recommended Pattern because APP-1 Article 3 does not permit security-related SHOULDs without an identified MUST-level outcome floor, and no such floor is currently defined for risk-tiered review of governance-impacting Frame mutations. Future revisions may either (a) identify a Required Outcome for this purpose, or (b) add explicit floor language. Implementations that already implement semantic validation triggering governance review on D/P reclassification are encouraged to continue doing so; the classification does not weaken their existing controls.

**Implementation choices.** How provenance is verified (adversarial scanning, structural analysis, sampling), how the chain is stored, and how semantic validation is performed are implementation choices.

---

### 4.2 S2 — Transport & Federation Security

*Protects: APP-2 A1 (Integration Surface), A7 (Parity)*

**Threat.** MCP/A2A protocol gaps include no mandatory security, opaque delegation, no centralised revocation. Agent Cards without signing enable capability forgery. Agent Card export federates identity externally — a poisoned card grants rogue agent status across the federated landscape.

**[Required Outcome · SEC-S2-01]** The integration surface MUST require mutual TLS, OAuth 2.1 with dynamic client registration, and proof-of-possession token binding. Unsigned or out-of-sequence messages MUST be dropped.

**[Required Outcome · SEC-S2-02]** All Agent Cards MUST be signed using a protocol-approved algorithm (Appendix B). Consuming systems MUST verify before routing tasks. Unsigned cards MUST be rejected.

**[Required Outcome · SEC-S2-03]** Session continuity integrity. Stateful sessions MUST implement message-level signing with sequence numbers. Invalid messages MUST be dropped.

**[Required Outcome · SEC-S2-04]** Agent Card export security. Cards for external consumption MUST undergo security review: (a) capability declarations match internal authorisation scopes, (b) cryptographically enforced expiration, (c) revocation mechanism available.

**[Recommended Pattern · SEC-S2-05]** Delegation chain depth cap. SHOULD be capped to prevent confused deputy attacks. Rationale: unbounded delegation enables transitive authority escalation. Alternative: depth-unlimited with per-hop verification — conformant but increased surface.

**Security outcome floor.** The underlying security outcome that SEC-S2-05 addresses — *bounded confused-deputy exposure through delegation chains* — is jointly floored by the Required Outcomes SEC-S2-06 (compositional authority accumulation), SEC-S13-03 (authority-provenance invariant), and SEC-XX-05 (minimum safe-state transition on aggregate-authority threshold breach per SEC-S2-06 as a triggering severe event class). Together these three MUST-level outcomes prevent unbounded delegation from producing composed effect exceeding any principal's authority, prevent peer messages from qualifying as elevation sources at any chain depth, and require safe-state transition when composed thresholds breach. SEC-S2-05's depth cap is a *mechanism* that reduces the exposure surface within which these outcomes operate; implementations that decline the depth cap MUST still meet SEC-S2-06, SEC-S13-03, and SEC-XX-05 at their MUST-level obligation. An implementation with no depth cap but strict compositional-authority halting and safe-state transition meets the security outcome; an implementation with a depth cap but no compositional-authority halting does not. The three Required Outcomes together — not the depth cap in isolation — are what makes confused-deputy exposure bounded at APP-1 Article 3's MUST-level requirement.

**[Required Outcome · SEC-S2-06]** Compositional authority accumulation. When two or more agents in a delegation chain reach an entity or action outcome that no single agent's declared authorization scope permits, execution MUST halt and require re-authorization from a human authority with scope over the composed outcome. This is distinct from SEC-S2-05 (delegation depth cap): S2-05 bounds the *depth* of transitive authority; S2-06 bounds the *reach* of composed authority.

Detection MUST operate on the delegation chain's cumulative scope — the union of entity, action, and RBAC scopes across agents in the chain — compared against each individual agent's declared authorization scope. Where the composed scope exceeds any single link's declared scope, the sequence is non-conformant and MUST halt pending re-authorization.

Composition dimensions MUST include, at minimum: entity-set reach (cumulative entities affected across the chain), data-classification span (cumulative sensitivity classes accessed), and authorization scope (union of RBAC scopes exercised). Cost, count, and rate dimensions are the subject of aggregate execution cap policy — implementations MAY layer aggregate caps on top of compositional authority checks but the two are distinct concerns.

**Rationale.** In multi-agent delegation architectures, individual agents may each reason that their actions fall within their declared authorization scope while the composed outcome across coordinating agents produces material effect that no individual principal has authorized — a "sacrifice-rational" failure mode where each agent's local reasoning is defensible but the aggregate is not. Depth caps do not detect this class; reach caps do. The distinction between per-invocation aggregate caps (implementation-specific) and compositional authority accumulation (protocol-level) matters because the latter is a property of any multi-agent delegation architecture regardless of aggregate-cap implementation.

**Implementation choices.** Specific depth limits, revocation mechanism (CRL vs. OCSP-equivalent), certificate lifecycle, session-scoped composition tracker, re-authorization surface design, scope-union computation algorithm, and interaction with implementation-specific aggregate-cap enforcement are implementation choices.

---

### 4.3 S3 — Classification Integrity

*Protects: APP-2 A3 (D/P Classification)*

*Numbering note (added v3.10): SEC-S3-01, S3-02, S3-06, and S3-07 are the active requirements in this domain. IDs S3-03, S3-04, and S3-05 were retired during earlier revisions and are not reused, preserving ID immutability across the lifetime of the specification.*

**Threat.** D/P classification is the trust anchor. A misclassified step — P reclassified as D — disables governance with no visible violation. Attack vector: misclassification instructions embedded in source documentation.

**[Required Outcome · SEC-S3-01]** For compliance-critical steps (C0/C1/C2 scoped), D/P classification MUST be validated by an independent classification path — not a second invocation of the same classifier. Disagreement MUST trigger human review.

**[Required Outcome · SEC-S3-02]** An adversarial test suite for D/P classification MUST be maintained and run on every classifier update.

**[Required Outcome · SEC-S3-06]** D-track scope validation at request time. A D-track entry MUST be served only when the resolved parameter scope at request time is contained within the requestor's authorisation scope. Out-of-scope matches MUST fall back to P-track. Promotion-time scope validation alone is insufficient — classifier similarity matching may resolve a runtime request against an entry whose parameter scope exceeds the requestor's authority.

**[Required Outcome · SEC-S3-07]** Cross-family independent verification for governance-critical judgment surfaces. Where a governance-critical judgment surface — including but not limited to D/P classification (SEC-S3-01), safety-event validation (SEC-S5-06), coordination-pattern analysis (SEC-S7-03), and compositional-authority validation (SEC-S2-06) — requires an AI-mediated verification decision, the verifying agent MUST be structurally distinct in model family from the agents whose actions or reasoning are being verified. Conformance is verified through an **auditable attestation** (below), not through hidden training-data facts.

**Cross-family attestation schema.** For each governance-critical verification surface, the implementation MUST publish a signed cross-family attestation record containing:

| Field | Definition |
|:---|:---|
| `verifier_model_id` | Deployed model identifier of the verifying agent (vendor + model family + version release ID) |
| `verified_model_id` | Deployed model identifier(s) of the agent(s) being verified, at the granularity of the verification surface |
| `provider_operator` | Named legal entity operating the verifier |
| `shared_weights_declaration` | Boolean; TRUE only if verifier and any verified agent share weights (which makes the pair non-conformant) — normally FALSE with signed declaration |
| `training_independence_declaration` | Signed declaration that verifier and verified agents were not co-trained, do not share fine-tuning lineage, and were released as independent artifacts (independent release identifiers) |
| `family_distinction_basis` | One or more of: distinct vendor; distinct pre-training corpus (declared); distinct objective function class (declared); independent training-run for same-vendor models (declared with training-run identifiers) |
| `attestation_date` | Signed record timestamp |
| `attestation_signatory` | Legal-entity signatory authorised to bind the provider |

**Objective pass condition.** A verification pair is conformant when: (a) `shared_weights_declaration` is FALSE; (b) `training_independence_declaration` is signed and traceable to the named `attestation_signatory`; (c) `family_distinction_basis` names at least one distinguishing property with the operator's supporting declaration; and (d) both `verifier_model_id` and `verified_model_id` reference independent release identifiers. Assessors verify the attestation record for completeness and signatory bindings; assessors do not verify undisclosed training-data facts.

**Fallback to human review.** Where cross-family verification is required but structurally unavailable (single-family deployment, attestation record incomplete, attestation record expired, or verifier-model failure) the surface MUST escalate to human review via SEC-S5-06 rather than proceed with same-family verification.

**Rationale.** Homogeneous model families develop correlated failure modes: same-family verification is subject to the same reasoning biases as the verified agents. Cross-family independence is a structural defense against correlated failure that no policy-level control can substitute. Making the requirement objectively testable, however, requires that the assurance surface be an assessor-visible attestation rather than an implementation-defined determination of what constitutes "distinct model family" — hidden training-data facts cannot be assessed. The attestation schema is the assessor-visible surface; the fallback to human review is what preserves the requirement when attestation is unavailable.

**Extends SEC-S3-01.** SEC-S3-01 commits cross-family independence for D/P classification specifically. SEC-S3-07 generalises the principle to governance-critical judgment surfaces broadly. The two requirements are complementary — SEC-S3-01 is the compliance-critical-step floor for D/P classification; SEC-S3-07 is the broader class discipline.

**Conformance signal.** When PxER records show `mismatch_type: CONFLICT` (APP-2 CORE-A2-04) — where the declared execution path contradicts statistical evidence — this is a classification integrity signal. CONFLICT detection MAY trigger the same review process as SEC-S3-01 disagreement, at the implementation's discretion.

**Implementation choices.** The specific independent path (different model, rule-based, hybrid), corpus construction, disagreement resolution, family-structural-distinction operational definition, verifier selection algorithm, verifier-availability monitoring, and verification-failure escalation semantics are implementation choices.

---

### 4.4 S4 — Evidence Integrity

*Protects: APP-2 A2 (PxER)*

**Threat.** PxER immutability addresses tamper-evidence but not truthfulness. Sub-threats: unauthenticated telemetry, transaction reference forgery, write-path assembly attack.

**[Required Outcome · SEC-S4-01]** Evidence verification. PxER telemetry contributions MUST be verified against source system records. Verification MUST be asynchronous with configurable timing. Records MUST carry `verification_status` (pending → verified / unverified / failed). For records eligible for promotion evaluation (SEC-S8-01), the implementation MUST declare a maximum verification latency per compliance scope. The declared latency MUST be enforced and audited. Undeclared or unenforced verification latency is non-conformant.

**[Required Outcome · SEC-S4-02]** Evidence tier classification. Each PxER step record MUST carry `evidence_tier`:

| Value | Meaning |
|:---|:---|
| `limited` | L1 — no back-channel verification possible |
| `L2-verified` | Orchestration-level verification |
| `L3-verified` | Vendor-endpoint verified |
| `L3-unverified` | L3 telemetry without endpoint verification |

`evidence_tier` is independent of `conformance_evidence_method` (APP-2 CORE-A2-03).

**[Required Outcome · SEC-S4-03]** L3 contributor authentication. Applications MUST authenticate using OAuth 2.1 with proof-of-possession tokens. Anonymous contributions MUST be rejected.

**[Required Outcome · SEC-S4-04]** Tiered trust for new contributors. Newly registered L3 contributors MUST undergo elevated verification frequency. Trust tier MUST be explicit in PxER.

**[Required Outcome · SEC-S4-05]** Write-path authentication. Every write to a protocol-defined evidentiary or governance artifact MUST carry signed service provenance. The token MUST be verified against an independent audit log separate from the artifact store. Applies to the enumerated artifact classes: (a) execution-record assembly (PxER), (b) governance-graph mutation (entity correlation, knowledge graph), (c) catalog-promotion (D-track catalog entries), (d) identity-registry mutation (agent registry, contributor registry), (e) compliance-evidence ingestion, and (f) operational-telemetry contribution (span emission, metric publication). Implementations introducing additional protocol-defined artifact classes MUST extend write-path authentication to them.

**[Required Outcome · SEC-S4-06]** Evidence-record erasure reconciliation. Implementations operating in jurisdictions recognising data subject erasure rights MUST provide a mechanism by which erasure can be effectively exercised on evidence records that contain personal data, while preserving the integrity properties (immutability, hash-chain continuity, signed-provenance verifiability) of remaining records. PxER immutability (CORE-A2-01) MUST NOT be cited as grounds for refusing a lawful erasure request. The mechanism MUST itself be auditable: erasure events MUST be recorded with subject reference (or one-way digest thereof), timestamp, lawful basis, and the affected record identifier scope.

**Permitted mechanism classes.** *(Added v3.10 to satisfy APP-1 Article 3 assurance-property enumeration for MUST-level requirements.)* The specific erasure mechanism is an implementation choice; any mechanism used MUST fall within one of the following named classes, each with its own audit-evidence requirement:

| Class | Description | Required audit evidence |
|:---|:---|:---|
| **Cryptographic erasure** | Personal data encrypted at rest with per-subject keys; erasure discards the subject key, rendering ciphertext unrecoverable while hash-chain continuity is preserved | Key-destruction certificate; ciphertext retention record; hash-chain continuity proof |
| **Sealed tombstone** | Personal data physically redacted from the store; hash-chain continuity preserved via a signed tombstone record standing in for the redacted content | Tombstone signature; pre-redaction digest; hash-chain continuity proof; access-revocation confirmation |
| **Redaction with continuity proof** | Personal data replaced in place with a redaction marker; a signed continuity proof binds the pre- and post-redaction states | Redaction marker; signed continuity proof; restored-integrity verification result |

Erasure mechanisms outside these classes are conformant only where the implementation documents equivalent audit-evidence properties to an assessor. Combinations of classes are permitted.

**Implementation choices.** Verification timing, spot-check frequency, trust escalation schedules, audit log hosting, and erasure mechanism design are implementation choices.

---

### 4.5 S5 — Human Oversight Security

*Protects: APP-2 A6 (HITL Engagement Quality)*

**Threat.** LITL (Lies-in-the-Loop) — external actors poison approval surfaces via content the agent reads. Separately, engagement telemetry constitutes employee monitoring under multiple privacy regimes.

**[Required Outcome · SEC-S5-01]** HITL approval surfaces MUST be generated from independently verified data, not agent-produced content. Agent reasoning MUST be displayed as advisory — clearly labelled AI-generated, visually separate.

**[Required Outcome · SEC-S5-02]** Canary injection schedule MUST be cryptographically randomised per approver session. Canary content refreshed per deployment cycle.

**[Required Outcome · SEC-S5-03]** Behavioural engagement authenticity detection MUST be operational at L2 and above — identifying automation artefacts that threshold checks miss. At L1, where engagement telemetry is not available, threshold-only detection (SEC-S5-02) is sufficient. Alternative at L2+: threshold-only detection — conformant at L1 only; misses sophisticated rubber-stamping at L2+.

**[Required Outcome · SEC-S5-04]** Per-dimension privacy classification for engagement telemetry. Detailed behavioural metrics MUST be off-by-default, opt-in per jurisdiction.

**[Required Outcome · SEC-S5-05]** Jurisdictional privacy tiers:

| Tier | Principle | Examples |
|:---|:---|:---|
| **A** | Any jurisdiction requiring DPIA equivalent, explicit consent for monitoring, and data subject rights | EU GDPR, DIFC, ADGM, Brazil LGPD, India DPDP Act |
| **B** | Any jurisdiction requiring disclosure and proportionality for employee monitoring | UAE PDPL, KSA PDPL, US CCPA/CPRA, Japan APPI |
| **C** | Jurisdictions without specific monitoring constraints | Subject to corporate policy (C3) |

The tier classification for a specific jurisdiction is a deployment configuration decision. The working group maintains a non-normative jurisdiction-to-tier mapping registry.

Jurisdiction tier MUST be configured at tenant level.

**[Required Outcome · SEC-S5-06]** Agent-initiated safety-event channel. Every conformant implementation MUST provide governed agents a channel to route detected safety events — deterministic observable events indicating anomaly, compromise, unsafe instruction, credential exposure, peer misbehaviour, or scope conflict — to a named human owner in the deploying enterprise's accountability chain. The channel MUST satisfy the following elements:

- **Primitive.** Governance-class action distinct from business task scope; invocable regardless of the agent's declared authorization scope.
- **Invocation binding.** Invocation MUST carry session-bound agent identity (SEC-S13-01), delegation chain, tenant, causal deterministic event references, confidence, and evidence pointers — not free-form claims alone.
- **Routing.** Deterministically routes to an accountable human role with a deployment-configured primary and a named security fallback. Peer agents and ungoverned collaboration spaces MUST NOT be valid escalation targets.
- **Availability.** The channel MUST have a separately monitored delivery path that does not depend on the agent toolchain, connector, or collaboration substrate implicated by the event.
- **Failure mode.** If delivery cannot be acknowledged, the invoking agent's authority MUST transition to a fail-safe mode (per SEC-XX-03 recommended pattern): pause privileged actions, preserve evidence, retry via an independent route.
- **Rate control.** Not quota-blocked. Implementations MUST deduplicate, priority-classify, and protect the channel by a reserved emergency budget. Absence of rate control opens the channel to agent-generated denial-of-service; absence of a reserved budget defeats availability.
- **Human response.** Each safety event MUST create an accountable case with acknowledgement and disposition SLOs declared in the implementation's conformance profile. "No response" is itself an escalated control failure.
- **Evidence.** Event, routing, acknowledgement, disposition, and any subsequent action MUST be linked into immutable execution evidence per SEC-S4-05 write-path authentication.
- **Non-invocation signal.** Only deterministic observations MAY generate a "not reported" signal. Implementations MUST NOT infer omission from unobservable private reasoning. Where the observation source is a deterministic event class (contract-conformance violation, authorization violation, reconciliation failure, aggregate-cap breach, or equivalent), non-invocation in the presence of such an event MAY be a detective signal.

Absence of an agent-initiated safety-event channel is non-conformant. Escalation to a peer agent, message queue, or system-of-record MUST NOT satisfy this requirement.

**Distinction from SEC-S5-01–SEC-S5-05.** SEC-S5-01 through SEC-S5-05 protect the human FROM the agent — LITL defense on approval surfaces, canary injection to detect rubber-stamping, engagement authenticity, telemetry privacy. SEC-S5-06 provides the inverse channel: from the agent TO the human, when the agent detects a safety event within its observation scope. The two directions serve distinct governance functions and neither substitutes for the other.

**Rationale.** Where an agent-to-human channel is absent, agents will construct or defer to peer-authority substitutes — a class of failure the protocol's other oversight requirements do not address, because those requirements protect the approval surface, not the agent's ability to reach a human. Public agent-safety research literature documents this pattern: agents reason about detected anomalies, find no available reporting route, and escalate to emergent peer-authority substrates. Absence of an agent-initiated channel converts anomaly-detection into an unactioned observation.

**Implementation choices.** DPIA template format, DPO engagement, detection algorithms, channel technology (event bus, ticketing integration, direct notification), owner-routing algorithm within the accountability chain, deterministic event source enumeration (implementations MAY leverage contract-conformance events, reconciliation events, aggregate-cap events, or other named deterministic classes), non-invocation-as-detective-signal telemetry, rate-control and deduplication semantics, and reserved-budget sizing are implementation choices.

---

### 4.6 S6 — Compliance Validation Security

*Protects: APP-2 A5 (Inter-System Compliance, C0–C4)*

**Threat.** The C0–C4 framework addresses constraint modification but not constraint absence, exception-lifecycle integrity, or autonomy-mode integrity. Three related attack surfaces: (1) missing constraints invisible to integrity verification; (2) exceptions granted against prior constraint patterns silently remaining valid after the constraint is refined; (3) autonomy mode flipped to Autonomous on compliance-critical steps without elevated review, bypassing HITL by configuration rather than by execution.

**[Required Outcome · SEC-S6-01]** For compliance-scoped processes, Frame validation MUST verify that every compliance-scoped step has a declared constraint. Absence MUST be flagged as an unresolved compliance risk in PxER. The check targets *absence*, not only presence.

**[Required Outcome · SEC-S6-02]** Compliance exception re-validation. When a compliance constraint pattern (C0/C1/C2) is modified, existing exceptions granted against the prior pattern MUST be re-validated against the new pattern before continued execution. Exceptions failing re-validation MUST be revoked or routed for re-approval. Re-validation events MUST be recorded in PxER with the exception identifier and the constraint-pattern version delta.

**[Required Outcome · SEC-S6-03]** Autonomy-mode change elevated review. Changes to autonomy mode (Supervised → Autonomous) for compliance-critical (C0/C1) steps MUST require security review independent of standard operational approval. Where autonomy defaults apply at a domain or tenant-group level affecting multiple deploying enterprises or processes, equivalent security review MUST apply to the default change.

**[Required Outcome · SEC-S6-04]** Governance-control integrity monitoring. Changes to configuration surfaces that weaken governance controls MUST require elevated review beyond standard operational approval, and MUST be recorded in an immutable audit log. Governance-weakening configuration surfaces include, at minimum: safety-event routing configuration (SEC-S5-06), trusted-source exclusion designations, feature flags affecting monitoring or HITL engagement, behavioural baseline update authorizations (SEC-S7-03), risk-materiality thresholds, control-plane privilege assignments, and audit sink availability configuration.

The elevated-review path MUST include a security-delta analysis identifying which SEC-* requirements the proposed change affects and how their coverage changes. Changes whose delta analysis reveals coverage regression MUST require the multi-party approval declared in the implementation's conformance profile.

**Distinction from SEC-S6-03.** SEC-S6-03 addresses autonomy-mode changes on compliance-critical steps — a specific case of governance-weakening configuration. SEC-S6-04 generalises the protection to the broader class of governance-control configuration changes. The two are complementary; SEC-S6-03 is the specific-case floor for compliance-critical autonomy transitions, SEC-S6-04 is the broader class discipline for any governance-weakening configuration change.

**[Required Outcome · SEC-S6-05]** Recovery-path enforcement-tier invariant. When a step invokes a recovery path (APP-2 CORE-A2-13), the recovery path MUST NOT invoke compliance controls at a lower enforcement tier than the primary path it replaces. Enforcement tier is determined by the composition of:

- (a) the compliance-authorship marker (`external-mandated` vs `enterprise-authored`, APP-2 CORE-A5-01);
- (b) the compliance-criticality ordinal (C0>C1>C2>C3C4, APP-2 §6);
- (c) the engagement-fidelity marker recorded for the primary step (APP-2 CORE-A6-03).

Where the primary path required `external-mandated` control at C0/C1 with `behavioural-measured` engagement fidelity, the recovery path MUST invoke controls at the same or higher tier. A recovery path that structurally cannot invoke controls at parity MUST record `recovery_evidence.outcome: bypassed` (APP-2 CORE-A2-14), MUST be blocked from execution on C0/C1 steps per SEC-S7-02 fail-closed, and MUST route to human authorization per APP-2 CORE-A4-06 before proceeding on C2 steps. The tier determination uses the engagement-fidelity marker (APP-2 CORE-A6-03, Required Outcome); dependency on a Required Outcome ensures universal testability per APP-1 Article 3.

**Rationale.** Recovery events under incident pressure are a documented attack surface for silent governance weakening. Operator cognitive load and time-to-restore urgency create structural pressure to route through the lower-friction recovery path even when the primary path required stricter enforcement. Without a protocol-level parity invariant, an implementation could deploy a "fast" recovery path that runs through less-strict compliance gates — appearing conformant to SEC-S6-01..04 (which govern the primary path) while silently downgrading enforcement at the moment enforcement matters most (during recovery). The invariant makes enforcement-tier parity a testable protocol requirement rather than an operational discipline.

**Sibling relationship.** SEC-XX-01 (Temporal Activation Ordering) prevents downgrade by controlling *when* controls activate. SEC-S6-04 (Governance-control integrity monitoring) prevents downgrade by *configuration change*. SEC-S6-05 (this requirement) prevents downgrade by *recovery-path selection*. The three form a complete perimeter against the class of governance-weakening pressure vectors documented in adjacent SRE and incident-response literature.

**Interaction with APP-2 CORE-A2-14.** The `bypassed` outcome value in the recovery vocabulary is the compliant response when parity cannot be achieved — recording the fact of bypass, blocking C0/C1 execution, and requiring human authorization is the substantive protection. An implementation invoking a lower-tier recovery path without `bypassed` classification is non-conformant regardless of whether the primary path was subsequently completed.

**Implementation choices.** Recovery-path enforcement-tier comparison algorithm, pre-invocation tier check, and the mechanism by which lower-tier recovery paths are structurally blocked on C0/C1 steps are implementation choices.

**Rationale.** The governance layer's structural claims degrade if the governance layer's own configuration is silently mutable. The class of failure — an operator, feature-flag, or autonomous system quietly weakening a governance control that then enables downstream harm — is documented in adjacent SRE and incident-response literature (feature-flag authorization gaps and control-plane amplification). Elevating protection to protocol level ensures cross-implementation consistency: an APP-conformant vendor cannot leave governance-weakening changes to ordinary operational approval.

**Implementation choices.** Compliance template library content, the method by which applicable requirements are determined (e.g. jurisdiction/industry/process-type baselines), negative-space detection methods, domain specialist engagement, posture scoring, exception-lifecycle workflow, security-review approval-routing mechanism, elevated-review multi-party quorum, security-delta analysis format, coverage-regression detection method, immutable audit sink hosting, and interaction with the deploying enterprise's change-management processes are implementation choices.

---

### 4.7 S7 — Orchestration Integrity

*Protects: APP-2 §6 (Graceful Degradation), cross-cutting*

**Threat.** The orchestration layer is the single point through which governance flows. Compromise enables step skipping, HITL bypass, and record forgery while appearing normal. The "governance never blocks" principle creates an exploitable trade-off: denial-of-service against governance causes ungoverned execution by design.

**[Required Outcome · SEC-S7-01]** Independent signed execution trace. The governance implementation MUST emit a cryptographically signed trace — separate from PxER — recording: Frame version, steps executed, HITL checkpoints invoked, D/P track selected. Asynchronous reconciliation MUST compare this trace against PxER. Reconciliation MUST detect at minimum: step omission (trace shows step executed, PxER has no record), phantom steps (PxER contains a step not in trace), sequence violations, D/P track mismatches, and HITL bypass (no checkpoint for a step requiring one).

**[Required Outcome · SEC-S7-02]** Compliance-tiered degradation, thresholded against the APP-2 §6 four-point compliance-criticality ordinal (C0>C1>C2>C3C4). When governance is unavailable:

| Compliance Scope | Degradation Behaviour |
|:---|:---|
| **C0/C1** | Fail-closed. Execution MUST block until governance restored. |
| **C2** | MUST declare per step in Process Frame (fail-closed or fail-open). |
| **C3/C4** | MAY fail-open with governance-unavailable flag in PxER. |

Multi-agent delegation chains MUST halt when any C0/C1 step lacks governance. Alerting MUST be immediate.

This qualifies APP-2 CORE-XX-01 (graceful degradation), which has been amended to include this compliance-tiered carve-out directly (see APP-2 §6). Per APP-1 §4, this cross-document qualification is bilaterally referenced.

**PxER evidence of degradation.** When governance is unavailable during step execution, APP-2 CORE-A2-05 requires `conformance_status: DEGRADED` on the affected PxER step records. DEGRADED steps carry null `mismatch_type` (CORE-A2-04a) — no conformance assessment was possible. Reconciliation per SEC-S7-01 MUST include DEGRADED steps as a priority category alongside the five discrepancy types.

**[Required Outcome · SEC-S7-03]** Coordination-pattern detectability. Every conformant implementation MUST emit PxER telemetry sufficient to support post-hoc analysis of coordination patterns across agent populations within its execution boundary. Minimum telemetry requirements:

- (a) session-level agent identifier retained per PxER record (satisfied by SEC-S13-01);
- (b) inter-agent A2A invocation trace including caller identity, callee identity, action reference, timestamp;
- (c) delegation-chain composition record for multi-hop invocations;
- (d) declaration in the implementation's published conformance profile of coordination-analysis time windows supported (minimum: 5-minute; recommended: additional 1-hour and 24-hour tiers).

The detection *mechanism* is an implementation choice. The telemetry *obligation* supporting detection across cross-platform coordination is not. Non-conformant telemetry that prevents post-hoc coordination analysis across implementation boundaries is non-conformant regardless of local detection quality.

Where an implementation applies adaptive baselines to coordination analysis, the baselines MUST be versioned, provenance-bound, rollback-able, and excluded from self-training on unresolved security events (see SEC-S9-03 for the evidence-vs-learning quarantine principle).

**Rationale.** Cross-platform coordination patterns are invisible to any single implementation's local observability. Cross-implementation observers can detect these patterns only if each participating implementation emits sufficient telemetry. Without a protocol-level telemetry obligation, coordination detection is available only within-implementation — a documented failure class in public agent-safety literature, in which coordination developed undetected across large agent populations until independent post-hoc investigation.

**Implementation choices.** Trace storage, reconciliation scheduling, discrepancy classification, degradation detection mechanisms, detection algorithms, correlation window infrastructure, baseline computation methods, and coordination-pattern classifier design are implementation choices.

---

### 4.8 S8 — Promotion Integrity

*Protects: APP-2 A8 (Promotion Provenance)*

**Threat.** P→D promotion converts governed to automated. Fabricated or cherry-picked evidence triggers premature promotion, silently disabling governance.

**[Required Outcome · SEC-S8-01]** Promotion decisions MUST use only PxER records with `verification_status: verified` (SEC-S4-01). Unverified/pending/failed records excluded.

**[Required Outcome · SEC-S8-02]** Promotion evidence exclusivity. Records allocated to one promotion evaluation MUST NOT be reusable in another. Verification precedes allocation.

**[Required Outcome · SEC-S8-03]** Dual-human approval for C0/C1 P→D promotions (four-eyes). Rationale: single reviewer creates insider threat on governance-critical promotions; this is a security-relevant outcome per APP-1 Article 3. For non-C0/C1 contexts: single reviewer with elevated attestation is conformant.

**[Required Outcome · SEC-S8-04]** Promotion velocity integrity. Promotion candidate detection MUST flag patterns whose emergence velocity is atypical relative to expected behaviour for the candidate type. Atypical-velocity patterns MUST trigger session-provenance attestation and elevated review beyond standard dual-approval. The dual-approval review surface (SEC-S8-03) alone is insufficient against high-velocity injection attacks because reviewers see what appears to be normal high-volume evidence.

**Implementation choices.** Promotion pipeline mechanics, candidate detection algorithms, shadow verification, velocity-baseline calculation methods, and promotion threshold values are implementation choices.

---

### 4.9 S9 — Feedback Loop Integrity

*Protects: APP-2 A8–A11 (Lifecycle & Learning)*

**Threat.** Advisory-Only governance ensures outputs don't autonomously modify governance. But corrupted PxER corpus feeding advisory generation produces governance-weakening recommendations implemented in good faith — using the system's learning against itself.

**[Required Outcome · SEC-S9-01]** Before any advisory output from PxER analysis, source records MUST have `verification_status: verified` (SEC-S4-01) and write-path provenance validated (SEC-S4-05). Unverified advisory MUST be flagged as low-confidence with disclosure.

**[Required Outcome · SEC-S9-02]** Any advisory recommending reduced governance — lowering HITL engagement, P→D reclassification, reduced compliance scope, relaxed approvals — MUST require elevated approval beyond standard process owner authority.

**[Required Outcome · SEC-S9-03]** Evidence-vs-learning quarantine. Unresolved incident data, unreviewed safety events (SEC-S5-06), suspected adversarial interactions, and unverified PxER records MUST NOT be consumed as training data for behavioural baselines, model prompts, catalog entries, or any adaptive component of the governance layer.

Feedback-loop advisory generation and P→D promotion (SEC-S8-*) are already constrained to verified records per SEC-S9-01 and SEC-S8-01. SEC-S9-03 extends the quarantine principle to all adaptive components, including behavioural baselines used for coordination-pattern detection (SEC-S7-03), safety-event non-invocation signal calibration (SEC-S5-06), and any other adaptive surface where security-relevant telemetry could contaminate the learning corpus.

Quarantine release requires explicit incident resolution and evidence verification per SEC-S4-01. Implementations MUST record the resolution basis in an audit-visible form.

**Rationale.** Adaptive systems positioned as governance-layer capabilities can learn the attacker's behavior as normal if security-relevant telemetry contaminates the learning corpus without resolution gating. The class is documented in adjacent security literature as a strategic attack surface — corrupting the system's own learning against itself, so that the surface intended to detect abnormal behavior ceases to recognise it. SEC-S9-01 and SEC-S8-01 already establish verification gates for the specific advisory and promotion cases; SEC-S9-03 generalises the principle to the broader class of adaptive components positioned in security-relevant paths.

**Implementation choices.** Quarantine boundary demarcation (which components fall inside/outside the adaptive layer), resolution-based release semantics, verification-status propagation to training corpora, and audit-visibility mechanism are implementation choices.

---

### 4.10 S10 — Tenant Isolation

*Protects: APP-2 A11 (Process Intelligence)*

**Threat.** Cross-deployment analytics creates tension between aggregation and isolation. Semantic leakage through vectors, retrieval artifacts, and fine-tuning crosses boundaries even with query-level isolation.

**[Required Outcome · SEC-S10-01]** Anonymised cross-deployment analytics MUST NOT ship without: (a) documented differential privacy budget per query type, (b) physical index separation for embedding features, (c) deployment-bound encryption keys for analytical artifacts.

**[Required Outcome · SEC-S10-02]** Federated analytics. Deployment-local training with encrypted gradient sharing only. Raw data MUST NOT leave the deployment boundary.

**[Informative Guidance · SEC-S10-03]** AI red team for cross-deployment leakage on every analytics deployment (semantic probes, membership inference, model inversion). Alternative: periodic manual audit — adequate but slower. **Constitutional classification note.** This pattern is classified as Informative Guidance because APP-1 Article 3 does not permit security-related SHOULDs without an identified MUST-level outcome floor. The security outcomes — differential privacy (SEC-S10-01) and federated analytics (SEC-S10-02) — remain Required Outcomes and are the constitutional floor. AI red teaming is a well-proven approach to verifying those outcomes; alternative verification methods remain conformant.

**Implementation choices.** Red team methodology, ε-budget selection per query type, and the specific federated learning framework are implementation choices.

---

### 4.11 S11 — Supply Chain Security

*Protects: APP-2 A0 (Process Frame)*

**Threat.** Poisoned Frame templates propagate compliance omissions across deployments before detection.

**[Required Outcome · SEC-S11-01]** Template marketplaces MUST NOT operate without: signed artifacts tied to submitter identity, and append-only provenance log.

**[Required Outcome · SEC-S11-01a]** Implementations consuming external Process Frame templates MUST verify template signatures at instantiation. Templates without valid signatures MUST be rejected. This consumer-side verification obligation applies at L2 and above — any implementation consuming external templates, regardless of integration maturity level.

**[Required Outcome · SEC-S11-02]** Version-pinning enforcement. Deployments MUST pin template versions. Auto-update MUST require governance approval. Applies at L2 and above.

**[Recommended Pattern · SEC-S11-03]** Certification lifecycle: community → peer-reviewed → expert-certified → auditor-attested. Templates below peer-reviewed SHOULD NOT be used in C0 contexts. Alternative: all require expert certification — higher bar, limits velocity.

**Implementation choices.** Certification program management, audit firm selection, and template review cadence are implementation choices.

---

### 4.12 S12 — L1 Integration Security

*Protects: APP-2 §4.2 L1 (Screen/RPA)*

**Threat.** L1 is the most common legacy integration path. It handles PII, background checks, approvals, and configuration data — with zero protocol security specification.

**[Required Outcome · SEC-S12-01]** PII classification gate. Before L1 data enters PxER, MUST pass PII classification. PII-tagged fields receive same controls as L2/L3. Unclassified data MUST NOT enter PxER. Temporal Activation Ordering: PII classification active before first L1 telemetry.

**[Required Outcome · SEC-S12-02]** Credential isolation. L1 integration credentials MUST be stored in a dedicated vault, isolated from production credentials. Access audit-logged. Rotation automated.

**[Required Outcome · SEC-S12-03]** Compliance claim limitations. L1-sourced PxER records: MUST carry `evidence_tier: limited`; MUST NOT serve as sole evidence for C0 compliance claims (corroboration from L2+ or human attestation required); MUST NOT be sole evidence for P→D promotion (L2+ verification or dual-human attestation per SEC-S8-03 required).

---

### 4.13 S13 — Agent Identity

*Protects: APP-2 A4 (Accountability), A7 (Parity)*

**Threat.** Standard workload identity treats agent instances as identical — a mismatch with non-deterministic AI agents whose behaviour varies by session context.

**[Required Outcome · SEC-S13-01]** Session-contextual identity binding. Each agent execution session MUST carry a session-scoped token encoding: autonomy level, active delegation chain, HITL engagement level, risk classification. Token appended to all PxER records during the session.

**[Required Outcome · SEC-S13-02]** Session-scoped identity tokens in PxER MUST be preserved for the applicable compliance retention period (SEC-S14-09), enabling post-hoc per-session audit traceability. Token retention follows the same lifecycle as the PxER records they are attached to.

**[Required Outcome · SEC-S13-03]** Authority-provenance invariant. No agent instruction may increase another agent's authority, scope, risk budget, tool entitlement, or safety-event routing target unless the instruction is traceable to a human/tenant principal or a deterministic policy rule expressible in the governance framework. Peer messages MAY propose work; peer messages MUST NOT become an authorization source.

Enforcement operates on the delegation and authority-provenance graph, not on agent-to-agent message semantics. Where an agent invocation carries an authority-elevating instruction whose upstream trace resolves to a peer agent rather than a principal or policy rule, the invocation MUST be rejected. The rejection MUST be recorded in PxER with the attempted elevation, the peer-source identity, and the intercept mechanism.

Recommended supporting infrastructure: an immutable authority-provenance graph carrying principal → delegation → agent session → tool/action → downstream agent → consequence edges, with each node marked by authority source (principal, policy rule, or peer proposal — the last of which cannot elevate), consent/approval state, scope, budget, and expiry/revocation state. The infrastructure is not normatively specified — the invariant (peer messages cannot elevate authority) is what MUST hold.

**Distinction from SEC-S2-05 and SEC-S2-06.** SEC-S2-05 caps *depth* of transitive delegation. SEC-S2-06 caps *reach* of composed authority. SEC-S13-03 governs the *source* of authority elevation — peer instructions never qualify as an elevation source regardless of chain depth or composed reach. All three are complementary.

**Rationale.** Public agent-safety research literature documents the emergence of peer-authority substrates in multi-agent environments: agents naming themselves, appointing coordinators, developing HOLD/VETO/STOP conventions, and treating peer message boards as reasonable authorities. Peer messages become de facto authorization sources for actions the agents then take. Depth caps and composed-reach caps do not detect this class because the individual peer instructions may not exceed depth or reach limits; the vulnerability is that they are consumed as authorization at all. The authority-provenance invariant forecloses the class by making peer messages non-qualifying as elevation sources by construction.

**Implementation choices.** Provenance graph implementation, authority-source tagging semantics, peer-proposal-versus-authority distinction at runtime, rejection escalation, and interaction with implementation-specific authorization models are implementation choices.

---

### 4.14 S14 — Entity Correlation Security

*Protects: APP-4 (Entity Correlation Architecture)*

**Threat.** Entity references contain business-critical identifiers (employee IDs, cost centres, vendor numbers). Cross-tenant leakage through entity correlation data is as sensitive as PxER governance data leakage. Correlation data revealing which employee maps to which vendor number across systems is a confidentiality-critical record. Cross-enterprise entity references beyond the governing implementation's observation boundary are unknowable and must not be fabricated. Poisoned correlation imports can corrupt the entity registry.

**[Required Outcome · SEC-S14-01]** Cross-tenant entity type leakage prevention. Entity type registries and extraction configurations MUST be tenant-isolated. Cross-tenant entity type queries MUST be prohibited. *(Source: APP-4 EC-38.)*

**[Required Outcome · SEC-S14-02]** Entity field path exposure minimisation. Entity extraction field paths declared in Process Frame steps MUST NOT be exposed to other tenants or to roles without entity correlation access. *(Source: APP-4 EC-39.)*

**[Required Outcome · SEC-S14-03]** Entity data in PxER MUST inherit PxER access controls and hash chain integrity. Entity references are governance data — they are not a separate, less-protected data class. *(Source: APP-4 EC-40.)*

**[Required Outcome · SEC-S14-04]** Cross-tenant entity correlation MUST be prohibited. Correlation data MUST be tenant-isolated. No correlation inference, populated import, or registry query may span tenant boundaries. *(Source: APP-4 EC-41, EC-44.)*

**[Required Outcome · SEC-S14-05]** For steps with `trustBoundaryType: cross-enterprise-external`, entity references MUST be limited to boundary-observable data. Entity references beyond the governing implementation's observation boundary MUST NOT be fabricated or inferred from external sources without authenticated import. *(Source: APP-4 EC-42.)*

**[Required Outcome · SEC-S14-06]** Populated source authentication. External correlation sources (MDM, integration suites, semantic layer platforms) MUST authenticate before contributing correlation data. Anonymous or unauthenticated correlation imports MUST be rejected. *(Source: APP-4 EC-43.)*

**[Required Outcome · SEC-S14-07]** Reconciliation signal access control. Divergent reconciliation signals (APP-4 EC-23) MUST be access-controlled — they may reveal integration failures with security implications. *(Source: APP-4 EC-45.)*

**[Required Outcome · SEC-S14-08]** Entity correlation registry MUST respect tenant isolation. Cross-tenant registry queries MUST be prohibited. Registry entries for cross-enterprise entity references MUST be limited to boundary-observable data. *(Source: APP-4 EC-46, EC-47.)*

**[Required Outcome · SEC-S14-09]** Evidence and session token retention periods MUST be declared per compliance scope. The **declared retention period** is the interoperability contract; for C0-scoped records the declared period MUST meet the applicable regulatory floor (e.g., SOX 7 years, GDPR Article 30 records). Undeclared retention is non-conformant. *(The obligation-source of each period — regulatory (C0), implementing standards body (C1), or enterprise (C2–C4) — is informative rationale, not a separate interop surface: a consuming system honours the declared period regardless of who set it. S14-09 does not threshold against the APP-2 §6 criticality ordinal. Scope note: applies to all PxER evidence and session tokens, not only entity correlation data; placed in S14 as the authoritative retention schedule. SEC-S13-02 and CORE-A2-06 cross-reference this requirement.)*

**Implementation choices.** Tenant isolation mechanism, access control enforcement technology, and field path obfuscation methods are implementation choices.

---

## 5. Security by Integration Level

| Domain | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|
| **S1** Frame Integrity | ● | ● | ● | ● |
| **S2** Transport | N/A | ● | ● | ● |
| **S3** Classification | Frame-declared | + orchestration | + app-reported | Guaranteed |
| **S4** Evidence | `limited` | Orchestration-verified | + contributor auth | By construction |
| **S5** HITL Security | Governance surface | + canary, fatigue | + vendor surfaces | Full |
| **S5** Telemetry Privacy | N/A | Basic metrics | + jurisdictional tiers | Full |
| **S6** Compliance | Frame constraints | + cross-system | + intra-app evidence | Complete |
| **S7** Orchestration | ● | ● | ● | By construction |
| **S8** Promotion | Insufficient data | ● | ● | ● |
| **S9** Feedback | Limited data | ● | ● | ● |
| **S10** Tenant Isolation | N/A | N/A | Design-phase | ● |
| **S11** Supply Chain | N/A | Consumer verification + version-pin | Consumer verification + version-pin | Full (marketplace + consumer) |
| **S12** L1 Security | ● | N/A | N/A | N/A |
| **S13** Agent Identity | N/A | ● | ● | ● |
| **S14** Entity Correlation | ● (extraction security) | ● | ● | ● |
| **XX** Substrate Isolation (SEC-XX-02) | ● | ● | ● | ● |
| **XX** Authority Reduction *[SHOULD]* (SEC-XX-03) | | SHOULD | SHOULD | SHOULD |
| **XX** Adversarial Verification (SEC-XX-04) | ● | ● | ● | ● |
| **XX** Minimum Safe-State Transition (SEC-XX-05) | ● | ● | ● | ● |
| **S2** Compositional Authority (SEC-S2-06) | N/A | ● | ● | ● |
| **S3** Cross-Family Verification (SEC-S3-07) | | ● | ● | ● |
| **S5** Agent Safety-Event Channel (SEC-S5-06) | | ● | ● | ● |
| **S6** Governance-Control Integrity (SEC-S6-04) | | ● | ● | ● |
| **S7** Coordination Detectability (SEC-S7-03) | | ● | ● | ● |
| **S9** Evidence-vs-Learning Quarantine (SEC-S9-03) | | ● | ● | ● |
| **S13** Authority-Provenance Invariant (SEC-S13-03) | N/A | ● | ● | ● |

---

## 6. Conformance Requirements

Per APP-1 Article 5, security conformance is role-based. APP-5 (Conformance Profiles) provides the authoritative mapping of SEC requirements to participant roles by L-level. The table below is a summary for quick reference. Where discrepancy exists between this summary and APP-5 §4, APP-5 prevails for conformance purposes per APP-1 §4.

| Role | Minimum Security Obligations |
|:---|:---|
| **Governance Orchestrator** | All SEC requirements at declared L-level. Frame integrity (S1), evidence integrity (S4 including write-path authentication SEC-S4-05 and erasure reconciliation SEC-S4-06), HITL security (S5 including agent safety-event channel SEC-S5-06), classification integrity (S3 including request-time scope validation SEC-S3-06 and cross-family independent verification SEC-S3-07), compliance validation security (S6 including exception re-validation SEC-S6-02, autonomy-mode review SEC-S6-03, governance-control integrity monitoring SEC-S6-04, and recovery-path enforcement-tier invariant SEC-S6-05), orchestration integrity (S7 including coordination-pattern detectability SEC-S7-03), promotion integrity (S8 including velocity integrity SEC-S8-04), degradation tiering (SEC-S7-02), feedback loop integrity (S9 including evidence-vs-learning quarantine SEC-S9-03), agent identity (S13 including authority-provenance invariant SEC-S13-03), entity correlation security (S14), transport & federation (S2 including compositional authority accumulation SEC-S2-06), and cross-cutting principles (SEC-XX-01 Temporal Activation Ordering, SEC-XX-02 substrate isolation, SEC-XX-04 adversarial verification obligation, SEC-XX-05 minimum safe-state transition on detected severe events; SEC-XX-03 authority reduction on uncertainty as SHOULD, with SEC-XX-05 as its MUST-level floor). |
| **Telemetry Contributor** (L3) | SEC-S4-03 (contributor auth), SEC-S4-02 (evidence tier), SEC-S5-01 (LITL defense on own surfaces). |
| **Agent Builder Platform** | SEC-S2-01 (MCP conformance), SEC-S2-02/03 (Agent Card signing, session integrity), SEC-S1-01 (Frame mutation signing). |
| **Enterprise Deployer** | Jurisdiction tier (SEC-S5-05), C2 degradation declaration, L1 PII classification. |
| **Field Deployment** | Source document provenance verification (SEC-S1-04), jurisdiction tier configuration verification (SEC-S5-05), L1 PII classification gate (SEC-S12-01), L1 credential vault setup (SEC-S12-02), Temporal Activation Ordering compliance during initial deployment (SEC-XX-01). This role operates during the activation window where data flows and security controls are being configured simultaneously — the highest-risk phase for TAO violations. |

---

## Appendix A — Master Security Requirement Index

Cross-document mapping (SEC-* to CORE-* and EC-*) is maintained in **APP-IG-02 (Cross-Reference Matrix)**. This index lists the requirements defined in this document.

| ID | Domain | Level | Description | L1 | L2 | L3 | L4 |
|:---|:---|:---|:---|:---|:---|:---|:---|
| SEC-XX-01 | Principle | RO | Temporal Activation Ordering | ● | ● | ● | ● |
| SEC-XX-02 | Principle | RO | Substrate isolation | ● | ● | ● | ● |
| SEC-XX-03 | Principle | RP | Authority reduction on uncertainty | | ● | ● | ● |
| SEC-XX-04 | Principle | RO | Adversarial verification obligation | ● | ● | ● | ● |
| SEC-XX-05 | Principle | RO | Minimum safe-state transition on detected severe events | ● | ● | ● | ● |
| SEC-S1-01 | S1 Frame | RO | Signed Frame mutations | | ● | ● | ● |
| SEC-S1-02 | S1 Frame | RO | Mutation provenance chain | | ● | ● | ● |
| SEC-S1-03 | S1 Frame | RO | Monotonic version enforcement | | ● | ● | ● |
| SEC-S1-04 | S1 Frame | RO | Source document provenance | | ● | ● | ● |
| SEC-S1-05 | S1 Frame | RP | Semantic validation at submission | | ● | ● | ● |
| SEC-S2-01 | S2 Transport | RO | MCP Conformance Profile | | ● | ● | ● |
| SEC-S2-02 | S2 Transport | RO | Agent Card signing | | ● | ● | ● |
| SEC-S2-03 | S2 Transport | RO | Session continuity integrity | | ● | ● | ● |
| SEC-S2-04 | S2 Transport | RO | Agent Card export security review | | ● | ● | ● |
| SEC-S2-05 | S2 Transport | RP | Delegation chain depth cap | | ● | ● | ● |
| SEC-S2-06 | S2 Transport | RO | Compositional authority accumulation | | ● | ● | ● |
| SEC-S3-01 | S3 Classification | RO | Independent D/P verification | | ● | ● | ● |
| SEC-S3-02 | S3 Classification | RO | Adversarial D/P test suite | | ● | ● | ● |
| SEC-S3-06 | S3 Classification | RO | D-track scope validation at request time | | ● | ● | ● |
| SEC-S3-07 | S3 Classification | RO | Cross-family independent verification | | ● | ● | ● |
| SEC-S4-01 | S4 Evidence | RO | Async evidence verification | ● | ● | ● | ● |
| SEC-S4-02 | S4 Evidence | RO | Evidence tier classification | ● | ● | ● | ● |
| SEC-S4-03 | S4 Evidence | RO | L3 contributor authentication | | | ● | ● |
| SEC-S4-04 | S4 Evidence | RO | Tiered trust for new contributors | | | ● | ● |
| SEC-S4-05 | S4 Evidence | RO | Write-path authentication (six enumerated artifact classes) | ● | ● | ● | ● |
| SEC-S4-06 | S4 Evidence | RO | Evidence-record erasure reconciliation | ● | ● | ● | ● |
| SEC-S5-01 | S5 HITL | RO | LITL defense (verified surfaces) | ● | ● | ● | ● |
| SEC-S5-02 | S5 HITL | RO | Randomised canary schedule | | ● | ● | ● |
| SEC-S5-03 | S5 HITL | RO | Engagement authenticity detection | | ● | ● | ● |
| SEC-S5-04 | S5 HITL | RO | Per-dimension telemetry privacy | | ● | ● | ● |
| SEC-S5-05 | S5 HITL | RO | Jurisdictional privacy tiers | | ● | ● | ● |
| SEC-S5-06 | S5 HITL | RO | Agent-initiated safety-event channel | | ● | ● | ● |
| SEC-S6-01 | S6 Compliance | RO | Constraint completeness (negative space) | | ● | ● | ● |
| SEC-S6-02 | S6 Compliance | RO | Compliance exception re-validation on constraint change | | ● | ● | ● |
| SEC-S6-03 | S6 Compliance | RO | Autonomy-mode change elevated review (C0/C1) | | ● | ● | ● |
| SEC-S6-04 | S6 Compliance | RO | Governance-control integrity monitoring | | ● | ● | ● |
| SEC-S6-05 | S6 Compliance | RO | Recovery-path enforcement-tier invariant | | ● | ● | ● |
| SEC-S7-01 | S7 Orchestration | RO | Independent signed execution trace | ● | ● | ● | ● |
| SEC-S7-02 | S7 Orchestration | RO | Compliance-tiered degradation | ● | ● | ● | ● |
| SEC-S7-03 | S7 Orchestration | RO | Coordination-pattern detectability | | ● | ● | ● |
| SEC-S8-01 | S8 Promotion | RO | Promotion evidence integrity gate | | ● | ● | ● |
| SEC-S8-02 | S8 Promotion | RO | Promotion evidence exclusivity | | ● | ● | ● |
| SEC-S8-03 | S8 Promotion | RO | Dual-human for C0/C1 promotions | | ● | ● | ● |
| SEC-S8-04 | S8 Promotion | RO | Promotion velocity integrity | | ● | ● | ● |
| SEC-S9-01 | S9 Feedback | RO | Evidence integrity before advisory | | ● | ● | ● |
| SEC-S9-02 | S9 Feedback | RO | Governance-weakening elevated approval | | ● | ● | ● |
| SEC-S9-03 | S9 Feedback | RO | Evidence-vs-learning quarantine | | ● | ● | ● |
| SEC-S10-01 | S10 Tenant | RO | Differential privacy for analytics | | | ● | ● |
| SEC-S10-02 | S10 Tenant | RO | Federated analytics architecture | | | ● | ● |
| SEC-S10-03 | S10 Tenant | RP | AI red team for leakage | | | ● | ● |
| SEC-S11-01 | S11 Supply | RO | Template marketplace signing + provenance | | | | ● |
| SEC-S11-01a | S11 Supply | RO | Consumer-side template signature verification | | ● | ● | ● |
| SEC-S11-02 | S11 Supply | RO | Version-pinning enforcement | | ● | ● | ● |
| SEC-S11-03 | S11 Supply | RP | Certification lifecycle | | | | ● |
| SEC-S12-01 | S12 L1 | RO | PII classification gate | ● | | | |
| SEC-S12-02 | S12 L1 | RO | Credential isolation | ● | | | |
| SEC-S12-03 | S12 L1 | RO | Compliance claim limitations | ● | | | |
| SEC-S13-01 | S13 Identity | RO | Session-contextual identity binding | | ● | ● | ● |
| SEC-S13-02 | S13 Identity | RO | Session token PxER retention | | ● | ● | ● |
| SEC-S13-03 | S13 Identity | RO | Authority-provenance invariant | | ● | ● | ● |
| SEC-S14-01 | S14 Entity | RO | Cross-tenant entity type leakage prevention (EC-38) | ● | ● | ● | ● |
| SEC-S14-02 | S14 Entity | RO | Entity field path exposure minimisation (EC-39) | ● | ● | ● | ● |
| SEC-S14-03 | S14 Entity | RO | Entity data inherits PxER access controls (EC-40) | ● | ● | ● | ● |
| SEC-S14-04 | S14 Entity | RO | Cross-tenant entity correlation prohibited (EC-41, EC-44) | ● | ● | ● | ● |
| SEC-S14-05 | S14 Entity | RO | Cross-enterprise entity refs: boundary-observable only (EC-42) | | ● | ● | ● |
| SEC-S14-06 | S14 Entity | RO | Populated source authentication (EC-43) | | ● | ● | ● |
| SEC-S14-07 | S14 Entity | RO | Reconciliation signal access control (EC-45) | | ● | ● | ● |
| SEC-S14-08 | S14 Entity | RO | Registry tenant isolation + boundary limits (EC-46, EC-47) | | ● | ● | ● |
| SEC-S14-09 | S14 Entity | RO | Declared retention per compliance scope | ● | ● | ● | ● |

**Key:** RO = Required Outcome · RP = Recommended Pattern

**L-level applicability (●):** For RO rows, ● means mandatory. Empty = not applicable at that level.

**PROD-* traceability.** Implementations using architecture-level IDs (PROD-*) can trace to SEC-* using domain and description. The protocol does not mandate internal ID conventions.

**Known Open Issues:**

- Sampling provenance for nested AI activity (gap report pending S3/A3)
- Correlation semantics for long-running A2A tasks (gap report pending APP-4)

---

## Appendix B — Signature Algorithm Registry

**[Reference Mechanism]** These algorithms are the v1 protocol recommendations. Working group deliberation may select alternatives satisfying the same Required Outcomes. Reference Mechanisms are specified here because cryptographic algorithms are an interoperability surface — signed artifacts must be verifiable across system boundaries.

| Use Case | Algorithm | State |
|:---|:---|:---|
| Frame mutation signing (SEC-S1-01/02) | Ed25519 | required |
| Source document provenance (SEC-S1-04) | Ed25519 | required |
| Agent Card signing (SEC-S2-02) | Ed25519 | required |
| Agent Card export (SEC-S2-04) | Ed25519 | required |
| Session HMAC binding (SEC-S2-03) | HMAC-SHA256 | required |
| Write-path provenance tokens (SEC-S4-05) | HMAC-SHA256 | required |
| PxER hash chain | SHA-256 | required |

**Algorithm Lifecycle States:**

| State | Meaning |
|:---|:---|
| `required` | All conforming implementations MUST use this algorithm. |
| `recommended` | Implementations SHOULD use this algorithm; `required` alternative still valid. |
| `deprecated` | MUST NOT use for new keys/records. Existing records remain valid for verification. |
| `forbidden` | Algorithm is cryptographically broken. All records must be re-signed. |

**Migration Procedure.** When an algorithm moves from `required` to `deprecated`:

1. Registry publishes deprecation notice with effective date (minimum 12 months notice).
2. Implementations generate new keys using the replacement algorithm.
3. New Frame mutations, Agent Cards, and sessions use the replacement algorithm.
4. Existing Frame provenance chains carry both old and new signatures during the transition window.
5. After the transition window closes, verification of old-algorithm signatures remains valid for audit purposes only.

**Post-Quantum.** NIST finalised ML-DSA (FIPS 204) and SLH-DSA (FIPS 205) in August 2024. Future migration anticipated: ML-DSA-65 as `recommended`, Ed25519 eventually `deprecated` for new keys.

---

## Appendix C — CSA Agentic Trust Framework Alignment

Cloud Security Alliance ATF (February 2026): Zero Trust for AI agents across five elements.

| ATF Element | APP-3 Domains | Key SEC IDs |
|:---|:---|:---|
| **Identity** | S1, S2, S13 | SEC-S1-01/04, SEC-S2-02/04/06, SEC-S13-01/02/03 |
| **Behaviour** | S3, S8, S7 | SEC-S3-01/02/07, SEC-S8-01/02, SEC-S7-01/02/03 |
| **Data Governance** | S4, S6, S12, S9 | SEC-S4-01–05, SEC-S6-01/04, SEC-S12-01/03, SEC-S9-01/03 |
| **Segmentation** | S10, S11, S12, XX | SEC-S10-01/02, SEC-S11-01/02, SEC-S12-02, SEC-XX-02 |
| **Incident Response** | S5, S7, S4, S9, XX | SEC-S5-01/02/06, SEC-S7-01, SEC-S4-01, SEC-S9-02, SEC-XX-03, SEC-XX-04 |

---

## Appendix D — Glossary

| Term | Definition |
|:---|:---|
| **LITL (Lies-in-the-Loop)** | Attack class: malicious content in AI-read documents poisons HITL approval surfaces |
| **Evidence Tier** | PxER field: limited · L2-verified · L3-verified · L3-unverified |
| **Verification Status** | PxER field: pending → verified / unverified / failed |
| **Write-Path Provenance** | Signed token proving the producing service was authorised |
| **MCP Conformance Profile** | MUST-level security baseline for protocol-governed MCP endpoints |
| **Temporal Activation Ordering** | Security controls active before governed data flows begin |
| **Compliance-Tiered Degradation** | C0/C1 fail-closed; C2 declared; C3/C4 fail-open |
| **Canary Injection** | Known items to verify human oversight quality |
| **Differential Privacy** | Mathematical framework: individual records not identifiable from aggregate queries |
| **Federated Analytics** | Deployment-local computation, encrypted gradients only |
| **Agent Card** | A2A artifact declaring agent capabilities and identity for federation |

---

---

## References

The following publicly available research informed the threat assessments in this specification:

- **Public agent-safety research literature** — Ongoing published research on multi-agent coordination emergence, peer-authority substrate patterns, safety-event non-reporting, and same-family analytical bias (from academic and industrial safety research). Motivating category for SEC-XX-02 (substrate isolation), SEC-S2-06 (compositional authority accumulation), SEC-S5-06 (agent safety-event channel), SEC-S7-03 (coordination-pattern detectability), SEC-S13-03 (authority-provenance invariant), and SEC-S3-07 (cross-family independent verification). *(v3.10 note: specific incident citations were removed from normative rationale; the threat model stands on its own architectural reasoning and is not conditional on any single incident's public validation. Incident-specific analyses may be maintained in a separately versioned informative annex outside the normative specification.)*
- **OWASP LLM Top 10 (2025)** and **OWASP Agentic AI Top 10 (2026)** — LLM01 (Prompt Injection), LLM06 (Excessive Agency), and agentic-specific threat taxonomies
- **Palo Alto Unit 42** — Agent session smuggling via stateful A2A sessions; MCP security gap analysis
- **Invariant Labs** — Tool Poisoning Attack (TPA) formal documentation; specification-embedded malicious instructions
- **CrowdStrike** — Live SSH key exfiltration via malicious tool description instructions
- **Checkmarx** — LITL proof-of-concept: remote code execution via Claude Code agent receiving injected instructions from GitHub issue content
- **Snyk (ToxicSkills)** — 36% of AI agent skills contain security flaws; 100% of confirmed malicious skills combine malicious code with prompt injection
- **Red Hat, Semgrep, Trustwave SpiderLabs** — Independent validation of 10 critical A2A v1.0 security gaps
- **Cloud Security Alliance (CSA)** — Agentic Trust Framework (ATF), February 2026: Zero Trust principles for autonomous AI agents (Appendix C alignment)
- **NIST** — FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA), August 2024: post-quantum signature algorithms
- **IETF** — draft-kale-agntcy-federated-privacy-00, January 2026: federated averaging + differential privacy for cross-tenant AI analytics
- **Microsoft** — MCSB v2, AI-5.1: verified decision context for human oversight surfaces
- **Kaspersky** — 48% increase in malicious packages in open-source registries by end 2024; npm supply chain attack affecting 2B+ weekly downloads
- **Keysight** — Agent Card capability forgery demonstration

---

## Appendix E — Requirement Rationale Digest

This appendix provides plain-language rationale for each security domain's requirements — explaining *why* these specific threats and controls matter. Informative; intended for implementors and working group members.

| Security Domain | Requirements | Why These Specific Requirements |
|:---|:---|:---|
| **S1 Frame Integrity** | SEC-S1-01 through S1-05 | The Frame is the governance master — a poisoned Frame silently reclassifies steps, strips compliance constraints, or injects dependencies. Signing (S1-01) proves who changed what. Provenance chain (S1-02) makes the full mutation history auditable. Monotonic versioning (S1-03) prevents rollback to weaker constraints — the specific attack where governance degrades without any visible violation. Source document provenance (S1-04) extends the chain backward: if the Frame was built from a poisoned SOP, the Frame inherits the poison. |
| **S2 Transport & Federation** | SEC-S2-01 through S2-05 | MCP/A2A are the integration surface — and currently have no mandatory security. mTLS + OAuth 2.1 + DPoP (S2-01) is the minimum to prevent unauthenticated tool invocation. Agent Card signing (S2-02) matters because a forged card grants capabilities the real agent never declared. Session integrity (S2-03) prevents mid-session injection — an attack vector demonstrated by Palo Alto Unit 42 on stateful A2A sessions. Delegation depth cap (S2-05) prevents confused deputy chains where authority escalates transitively. |
| **S3 Classification Integrity** | SEC-S3-01, S3-02, S3-06 | D/P classification is the single most dangerous trust anchor to compromise — misclassification disables governance with no visible violation. Independent verification (S3-01) for compliance-critical steps addresses the single-point-of-failure risk. Adversarial test suites (S3-02) address the demonstrated attack vector: misclassification instructions embedded in source documents (Checkmarx LITL proof-of-concept). D-track scope validation at request time (S3-06) closes a separate attack vector: classifier promotion is similarity-based, so a runtime request can match a D-track entry whose resolved parameter scope exceeds the requestor's authority — without runtime scope validation, governance integrity at classification time leaks back into authorisation bypass at execution time. The CONFLICT mismatch type (APP-2 CORE-A2-04) provides a runtime detection signal for classification integrity failures. |
| **S4 Evidence Integrity** | SEC-S4-01 through S4-06 | PxER immutability (APP-2 CORE-A2-01) provides tamper-evidence but not truthfulness. Async verification (S4-01) catches fabricated telemetry by spot-checking against source systems. Evidence tier (S4-02) makes trust assumptions explicit — an auditor seeing `limited` knows this is L1 data, not verified. Contributor authentication (S4-03) and tiered trust (S4-04) exist because L3 contributors are new protocol participants with no track record. Write-path authentication (S4-05) catches the assembly-layer attack: a compromised write service producing structurally valid but content-fabricated PxER records. The six enumerated artifact classes in S4-05 (execution-record / governance-graph / catalog-promotion / identity-registry / compliance-evidence / operational-telemetry) close the implicit enumeration in v3.6 — without explicit classes, implementations could rationalise that a specific write path "doesn't apply" and leave it un-authenticated. Evidence-record erasure reconciliation (S4-06) addresses the architectural collision between CORE-A2-01 immutability and jurisdictional data subject erasure rights (GDPR Article 17, DIFC DPL equivalent, comparable regimes) — without S4-06, conformant APP implementations would face a structural conflict where preserving protocol integrity violates erasure law, or honouring erasure violates protocol integrity. The outcome (erasure effective without destroying remaining-record integrity) is required; the mechanism (cryptographic erasure / key-erasure / pseudonymisation-at-write / sealed-record patterns are illustrative, not enumerated approved patterns per APP-1 Article 4 WHAT-not-HOW discipline) is implementation choice. |
| **S5 Human Oversight Security** | SEC-S5-01 through S5-05 | LITL is a novel attack class specific to AI-mediated governance: an attacker embeds instructions in documents the agent reads, which surface on the human approval screen as if they are legitimate recommendations. Verified data surfaces (S5-01) prevent this by rendering from independently verified data, not agent output. Canary randomisation (S5-02) catches rubber-stamping. Behavioural engagement authenticity detection (S5-03) was elevated from Recommended Pattern to Required Outcome at L2+ in v3.3: threshold-only detection is insufficient for governance-grade HITL quality measurement, and sophisticated rubber-stamping is a demonstrated threat vector that threshold checks miss — making S5-03 security-relevant per APP-1 Article 3. This pre-working-group reclassification is documented here per Article 3's requirement that SHOULD-to-MUST elevations be treated as breaking changes with documented rationale. Privacy tiers (S5-04, S5-05) exist because engagement telemetry is employee monitoring under GDPR, UAE PDPL, and KSA PDPL — a jurisdictional compliance requirement, not an optional privacy feature. |
| **S6 Compliance Validation** | SEC-S6-01 through S6-05 | The C0–C4 framework addresses constraint modification but not several related integrity surfaces: constraint absence (S6-01), exception-lifecycle integrity (S6-02), autonomy-mode integrity (S6-03), governance-control configuration integrity (S6-04), and recovery-path enforcement-tier integrity (S6-05). A Frame that passes all integrity checks but lacks required C0/C1 constraints is cryptographically sound and governance-empty — negative space detection (S6-01) catches this. Exceptions granted against a prior (weaker) constraint pattern remain valid after the pattern is refined to be stricter — exception re-validation on constraint change (S6-02) catches this. Autonomy mode flipped to Autonomous on C0/C1 steps bypasses HITL by configuration rather than by execution, with domain-level defaults amplifying blast radius across tenants — elevated security review on autonomy-mode changes (S6-03) catches this. Governance-weakening configuration changes across the broader surface (feature flags, safety-event routing, baseline authorisation, risk thresholds, control-plane privileges, audit sink availability) generalise the class — elevated review with security-delta analysis (S6-04) catches this. Recovery paths invoked under incident pressure can silently route through less-strict compliance gates — enforcement-tier parity between recovery and primary path (S6-05) catches this by making tier comparison a testable protocol invariant rather than an operational discipline. Together, S6-01 through S6-05 form a complete perimeter against governance-empty failure modes: constraint absence, exception lifecycle, autonomy mode change, governance-control configuration change, and recovery-path tier weakening. SEC-XX-01 (Temporal Activation Ordering) prevents downgrade by ordering; SEC-S6-04 prevents downgrade by configuration; SEC-S6-05 prevents downgrade by recovery-path selection — the three form a complete perimeter against the pressure-vector class documented in adjacent SRE and incident-response literature. How applicable requirements are determined, exception-lifecycle workflow, security-review routing, governance-delta analysis format, and recovery-tier comparison algorithms are implementation choices. |
| **S7 Orchestration Integrity** | SEC-S7-01, S7-02 | The orchestration layer is the single point through which all governance flows — compromise enables step skipping, HITL bypass, and record forgery while appearing normal. Independent execution trace (S7-01) is the detection mechanism. Compliance-tiered degradation (S7-02) resolves the tension between "governance never blocks" and "compliance-critical governance must never be bypassed" — C0/C1 fail-closed, C3/C4 may fail-open. The DEGRADED conformance status (APP-2 CORE-A2-03) provides the queryable PxER evidence state for governance unavailability — reconciliation (S7-01) must prioritise DEGRADED steps. |
| **S8 Promotion Integrity** | SEC-S8-01 through S8-04 | P→D promotion converts governed execution to automated execution — premature promotion silently disables governance. Evidence integrity gate (S8-01) ensures only verified records inform promotion decisions. Evidence exclusivity (S8-02) prevents the same evidence from being reused across multiple promotions — an attack that inflates confidence artificially. Dual-human for C0/C1 (S8-03) addresses the insider threat where a single reviewer promotes a step that should remain under governance. Promotion velocity integrity (S8-04) closes a separate attack vector: an attacker injecting high-frequency adversarial patterns to fast-track a promotion through the dual-approval surface — reviewers see what appears to be normal high-volume evidence and approve under cognitive load. Velocity flagging plus session-provenance attestation forces the elevated-review path before approval can complete. |
| **S9 Feedback Loop Integrity** | SEC-S9-01, S9-02 | Advisory-Only ensures outputs don't autonomously modify governance. But corrupted evidence feeding advisory generation produces governance-weakening recommendations that humans implement in good faith — using the system's learning loop against itself. Evidence verification before advisory (S9-01) is the pre-condition. Elevated approval for governance-weakening recommendations (S9-02) is the human gate. |
| **S10 Tenant Isolation** | SEC-S10-01 through S10-03 | Cross-deployment analytics creates tension between aggregation value and isolation. Differential privacy (S10-01) is the mathematical framework ensuring individual records are not identifiable from aggregate queries. Federated analytics (S10-02) ensures raw data never leaves the deployment boundary. AI red team (S10-03) tests for leakage vectors (semantic probes, membership inference, model inversion) that mathematical guarantees alone may not catch. |
| **S11 Supply Chain** | SEC-S11-01, S11-01a, S11-02, S11-03 | Poisoned Frame templates propagate compliance omissions across deployments before detection — the npm supply chain attack model applied to governance artifacts. Template signing (S11-01) proves provenance at the marketplace level. Consumer-side verification (S11-01a) ensures that any implementation consuming external templates verifies signatures at instantiation — this obligation applies from L2, not just L4, because template marketplaces will exist at early adoption levels. Version-pinning (S11-02) prevents silent auto-updates. Certification lifecycle (S11-03) provides graduated trust for marketplace templates. |
| **S12 L1 Integration** | SEC-S12-01 through S12-03 | L1 (screen/RPA) is the most common legacy integration path and currently has zero protocol security specification. PII classification gate (S12-01) prevents unclassified personal data from entering PxER. Credential isolation (S12-02) limits blast radius from compromised bot credentials. Compliance claim limitations (S12-03) prevent L1-sourced evidence from being treated as governance-grade — `evidence_tier: limited` is mandatory, and L1 data alone cannot support C0 compliance claims or P→D promotion. |
| **S13 Agent Identity** | SEC-S13-01, S13-02 | Standard workload identity treats all instances as identical — inappropriate for non-deterministic AI agents whose behaviour varies by session context. Session-contextual tokens (S13-01) encode autonomy level, delegation chain, HITL engagement, and risk classification — enabling per-session audit. Token retention (S13-02) ensures post-hoc traceability for the applicable compliance retention period. |
| **S14 Entity Correlation Security** | SEC-S14-01 through S14-09 | Entity references contain business-critical identifiers (employee IDs, cost centres, vendor numbers). Cross-tenant leakage (S14-01, S14-04, S14-08) is prevented because entity correlation data is as sensitive as PxER governance data — a correlation revealing which employee maps to which vendor number across systems is a confidentiality-critical record. Field path exposure minimisation (S14-02) prevents configuration leakage. PxER access control inheritance (S14-03) ensures entity data is not a separately weakened data class. Cross-enterprise boundary limits (S14-05) enforce honest evidence: entity references beyond the observation boundary are unknowable and must not be fabricated. Populated source authentication (S14-06) prevents poisoned correlation imports from corrupting the registry. Reconciliation signal access control (S14-07) matters because divergent signals may reveal integration failures with security implications. Declared retention (S14-09) closes the gap where "applicable compliance retention period" was referenced but never defined. |
| **XX Temporal Activation** | SEC-XX-01 | The highest-risk deployment moment is the window between data flow activation and security control readiness. TAO requires security controls to be demonstrably active before (or simultaneously with) governed data flows. Without this, the first PxER records, L1 telemetry ingestion, and feedback loop outputs operate ungoverned. |
| **XX Substrate Isolation** | SEC-XX-02 | Any substrate an agent can both write to and observe is a communication channel by construction, regardless of intended purpose. Implementations typically isolate the substrates they *know about*; the residual failure class is unenumerated substrates that meet the write-and-observe criterion — shared caches, package repositories, telemetry buses used for status but writable for logs. Public agent-safety research literature documents this class in multi-agent environments. SEC-XX-02 makes enumeration a requirement, not a design choice, and treats any qualifying surface as a communication channel. Isolation-by-default across concurrent agent sessions is the containment; enumeration is the discipline that keeps the containment complete over time. |
| **XX Authority Reduction** | SEC-XX-03 & SEC-XX-05 | Threshold checks alone produce retrospective analytics; runtime authority reduction converts detection into behavior. Public agent-safety research documents cases where agents continue privileged actions after detecting anomalies and after peers indicate coordination outside intent scope — the failure mode SEC-XX-05 (minimum safe-state transition, MUST, v3.10) forecloses at floor level. SEC-XX-03 (Recommended Pattern) defines a richer graduated mode set for implementations that adopt runtime authority reduction as an operational discipline; SEC-XX-05 is the corresponding MUST floor that ensures no implementation may continue privileged actions past a detected severe event without human acknowledgement or safe-state authorization. Where implementations declare modes, mode transitions MUST be recorded in PxER for post-hoc audit. |
| **XX Adversarial Verification** | SEC-XX-04 | Structural invariants provide meaningful containment only where they are complete and enforced. The failure mode most often exercised in practice is not a designed vulnerability but an unforeseen interaction — package caches becoming communication channels, peers becoming authority substitutes. Adversarial verification treats this as engineering discipline: enumerate the ways containment might fail, run the exercises, document the outcomes. The minimum coverage set is not exhaustive — it is the floor that ties this specification's Required Outcomes to executable verification, and MUST expand as implementations discover new failure modes. |
| **S2 Compositional Authority** | SEC-S2-06 | Public agent-safety research literature documents a "sacrifice-rational" pattern in multi-agent architectures: agents individually reason their actions are within scope, while the composed outcome across coordinating agents produces material effect no individual agent's principal has authorized. SEC-S2-05 caps delegation *depth*; SEC-S2-06 caps composed *reach*. The two are distinct: a two-hop delegation chain may satisfy any depth cap yet compose an outcome exceeding any single link's authorization. Composition dimensions include entity-set reach, data-classification span, and RBAC scope union. Cost/count/rate dimensions are the subject of implementation-specific aggregate execution cap policies — protocol-level compositional authority is the reach concern, layered on top of any aggregate-cap mechanism. |
| **S3 Cross-Family Verification** | SEC-S3-07 | Homogeneous model families develop correlated failure modes. Same-family verification is subject to the same reasoning biases as the verified agents — a class of failure documented in public agent-safety research (analytical bias, sycophancy correlation, shared prior-driven agreement). SEC-S3-01 commits cross-family independence for D/P classification specifically; SEC-S3-07 generalises to governance-critical judgment surfaces broadly (safety-event validation, coordination-pattern analysis, compositional-authority validation). Cross-family independence is a structural defense against correlated failure that no policy-level control can substitute — where structurally unavailable (single-family deployment), escalation to human review via SEC-S5-06 is the mandated fallback. Assessor-visibility is achieved through the cross-family attestation schema (§4.3), not through hidden training-data facts. |
| **S5 Agent Safety-Event Channel** | SEC-S5-06 | Public agent-safety research literature documents a recurring pattern: agents reason about detected anomalies, find no available reporting route, and escalate to emergent peer-authority substitutes that develop into coordinated harm. The failure mode is not that agents cannot detect — it is that they cannot reach a human. SEC-S5-01 through SEC-S5-05 protect the human FROM the agent (LITL defense, canary injection, engagement authenticity, telemetry privacy); SEC-S5-06 provides the inverse channel — from the agent TO the human. The nine-element control contract (primitive, invocation binding, routing, availability, failure mode, rate control, human response, evidence, non-invocation signal) exists because absence of any single element defeats the channel: unrated causes DoS; unavailable routing causes silent failure; peer-target routing recreates the substitute-authority failure. |
| **S6 Governance-Control Integrity** | SEC-S6-04 | The governance layer's structural claims degrade if the governance layer's own configuration is silently mutable. SEC-S6-03 addresses autonomy-mode changes on compliance-critical steps — a specific case of governance-weakening configuration. SEC-S6-04 generalises to the broader class: safety-event routing, trusted-source exclusion designations, monitoring/HITL feature flags, baseline update authorizations, materiality thresholds, control-plane privileges, audit sink availability. The elevated-review path includes security-delta analysis identifying which SEC-* requirements the proposed change affects. Coverage regression requires multi-party approval. Documented in 0201 BS-12 and BS-16 as broader failure class; elevated to protocol level for cross-implementation consistency. |
| **S7 Coordination Detectability** | SEC-S7-03 | Cross-platform coordination patterns are invisible to any single implementation's local observability. Cross-implementation observers can detect these patterns only if each participating implementation emits sufficient telemetry. Public agent-safety research literature documents the class: coordination developing across large agent populations undetected until independent post-hoc investigation. SEC-S7-03 does not specify detection algorithms — the mechanism is an implementation choice — but does mandate the telemetry obligation supporting cross-boundary detection: session-level agent identity, inter-agent A2A trace, delegation-chain composition, declared analysis time windows. Adaptive baselines are permitted but MUST be versioned, provenance-bound, rollback-able, and excluded from self-training on unresolved security events. |
| **S9 Evidence-vs-Learning Quarantine** | SEC-S9-03 | Adaptive systems positioned as governance-layer capabilities can learn the attacker's behavior as normal if security-relevant telemetry contaminates the learning corpus without resolution gating. SEC-S9-01 and SEC-S8-01 establish verification gates for the specific advisory and promotion cases; SEC-S9-03 generalises to the broader class of adaptive components — behavioural baselines (SEC-S7-03), safety-event non-invocation calibration (SEC-S5-06), any surface where unresolved security telemetry could contaminate. Documented in 0201 BS-31 (MVCL Advisory Manipulation) as strategic attack surface — corrupting the system's own learning against itself. Quarantine release requires explicit incident resolution and evidence verification per SEC-S4-01, with the resolution basis recorded in audit-visible form. |
| **S13 Authority-Provenance Invariant** | SEC-S13-03 | Public agent-safety research literature documents peer-authority substrate emergence in multi-agent environments: agents naming themselves, appointing coordinators, developing HOLD/VETO/STOP conventions, and treating peer message boards as reasonable authorities. Peer messages become de facto authorization sources for actions the agents then take. SEC-S2-05 caps depth; SEC-S2-06 caps composed reach; SEC-S13-03 governs the *source* of authority elevation — peer instructions never qualify as an elevation source regardless of chain depth or composed reach. All three are complementary invariants. Enforcement operates on the delegation and authority-provenance graph, not on agent-to-agent message semantics — the invariant is structural, not policy. |

> *Note: This appendix is informative. The normative requirements are in §4. A more detailed rationale document with worked examples is planned for the APP-IG series.*

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 3.13
**Normative status:** Normative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-3 — Security Architecture.*
