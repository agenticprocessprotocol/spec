# APP-1

Agentic Process Protocol

## Protocol Constitution

| | |
|:---|:---|
| **Version** | 1.5 — Draft |
| **Date** | October 2026 |
| **Status** | Draft — Pre-Working-Group |
| **Audience** | All protocol stakeholders: implementors, vendors, enterprises, working group members |
| **Normative status** | This document is normative. It governs all other APP specification documents. |
| **Suite baseline** | **APP-2026-10-RC1** (Oct 2026) — v1.5 recognises the APP-R Illustrative Reference tier in §4 Specification Types and extends the change-impact manifest template to cover it. |
| **Manifest** | APP-0 v0.14 · APP-1 v1.5 · APP-2 v5.13 · APP-3 v3.13 · APP-4 v2.3 · APP-5 v1.10 · APP-IG-01 v1.11 · APP-IG-02 v1.15 · APP-IG-03 v1.11 · APP-IG-04 v0.6 · APP-IG-05 v0.12 · APP-R1 v0.3.0 (schema + notes + example) · APP-R2 v0.3 Draft |
| **Release rule** | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. Version bumps require concurrent manifest regeneration. |
| **Version-reference convention** | Companion documents cited by name only in body prose. Manifest above is the sole non-historical source for companion versions. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** APP-1 is the normative Constitution of the Agentic Process Protocol. It establishes the protocol's governing principles, Priority of Constituencies, invariants, document hierarchy, and governance constraints.
>
> **Status:** Normative. Requirements expressed using RFC 2119/8174 keywords are binding within the declared scope.
>
> **Authority and precedence:** APP-1 prevails where another APP document conflicts with this Constitution. APP-0 through APP-5 and the APP implementation guides must be interpreted consistently with it.
>
> **Use this document for:** Understanding the protocol's decision hierarchy, security-normativity principles, scope boundaries, document precedence, and constitutional amendment constraints.
>
> **Related documents:** APP-0 states enterprise objectives; APP-2 through APP-5 define technical, security, entity-correlation, and conformance requirements; APP-IG documents provide informative implementation and assurance guidance.

---

## 1. Preamble

The Agentic Process Protocol (APP) is an open standard for governing cross-system enterprise processes in which AI agents and humans collaborate. It specifies how governed process specifications are constructed, how execution evidence is assembled across vendor boundaries, how human oversight quality is measured, and how processes improve through governed feedback loops.

This Constitution establishes the principles, constraints, and decision-making hierarchy that govern the protocol itself. Every APP specification document — protocol objectives, core protocol, security architecture, entity correlation architecture, conformance profiles, and implementation guides — must conform to the principles stated here. Where a specification conflicts with this Constitution, the Constitution prevails.

This Constitution is intended to be stable across protocol versions. It may be amended only by the governing body through the procedures referenced in Section 7.

---

## 2. Priority of Constituencies

When design decisions, trade-offs, or conflicts arise, the protocol resolves them according to the following hierarchy. Higher-ranked concerns take precedence over lower-ranked concerns.

- **Regulatory and compliance obligations.** External legal and regulatory requirements are boundary conditions. The protocol must not create structures that make compliance harder to achieve or demonstrate. This is not a constituency but a constraint that overrides all other considerations.

- **Process participants.** Humans who are accountable for governed process outcomes — approvers, decision-makers, and those affected by process decisions. Their safety, informed consent, and ability to exercise genuine oversight take precedence over system convenience.

- **Enterprise process owners.** Organisations deploying governed processes. Their ability to audit, control, and improve processes across vendor boundaries takes precedence over implementor convenience.

- **Platform implementors and vendors.** AI platforms, enterprise system vendors, and system integrators building conformant implementations. Implementation feasibility matters, but not at the expense of governance integrity.

- **Protocol authors.** Specification writers and working group members. Theoretical elegance and architectural purity yield to practical needs of all parties above.

*Example: A proposed change improves auditability for enterprise process owners (#3) but increases implementation burden for platform vendors (#4). The change is adopted. A different proposal improves architectural elegance (#5) but reduces the quality of human oversight (#2). The proposal is rejected.*

---

## 3. Articles

### Article 1 — Interoperability Is the Governing Purpose

The protocol exists to enable independently-built systems to participate in governed processes together. Every normative element must serve interoperability, safety, or both. Where interoperability requires implementation-level specificity, the protocol provides it. Where it does not, the protocol specifies the required outcome and leaves the mechanism to implementations.

*Design implication: The protocol specifies signing algorithms for cross-system verification (interoperability requires agreement) but does not specify how an implementation stores its governance artifacts internally (no interoperability concern).*

### Article 2 — Normative Language Serves Interoperability and Safety

The protocol uses RFC 2119/8174 normative keywords (MUST, SHOULD, MAY). These keywords, when they appear in all capitals, carry their defined meanings. When used in lower case, these words are descriptive only and carry no normative weight. MUST is reserved for requirements essential to interoperability or safety. It is never used to mandate implementation methods or internal architecture where the protocol has no interoperability concern. SHOULD marks approaches that the working group considers well-proven; implementors who deviate must understand and document the trade-offs. MAY marks genuinely optional capabilities; implementations that omit a MAY feature must interoperate with implementations that include it.

### Article 3 — Security Outcomes Are Strict; Mechanisms May Be Recommended

Every normative security **outcome** MUST use MUST. Optional security within an applicable scope is no security.

Security-related Recommended Patterns MAY use SHOULD only where both of the following hold: (a) the associated Required Outcome establishes an independently testable security floor, and (b) the pattern is a mechanism for achieving that floor, not the floor itself. A security-relevant SHOULD without a corresponding MUST-level outcome floor is non-conformant with this Article.

**Explicit cross-reference requirement.** Every security-related Recommended Pattern MUST cite, in the same section or a normative cross-reference table, the Required Outcome(s) that establish its floor. This makes constitutional compliance directly reviewable rather than a matter of interpretation. Where a Recommended Pattern cannot identify its Required Outcome floor, the Recommended Pattern MUST be reclassified as informative guidance until such a floor is defined.

**Applicability is not optionality.** The set of security outcomes applicable to a given implementation is a function of its declared role and integration maturity level, as defined in APP-5 (Conformance Profiles). An outcome that does not apply at a given L-level — because that level's integration depth cannot support the mechanism — is fully MUST at every level where it does apply. Ecosystem scaling is achieved by calibrating *applicability*, not by weakening *strictness within an applicable scope*.

The protocol starts strict and may relax specific security outcomes in future versions only with evidence that the relaxation does not reduce governance integrity. The protocol MUST NOT introduce security-relevant behaviour as SHOULD and later elevate it to MUST without treating the change as a breaking change and providing a migration pathway.

### Article 4 — Three Levels of Specificity

Every normative element in the protocol is classified at exactly one of three levels. These levels determine how much implementation freedom the protocol grants.

| **Level** | **Definition** | **Example** |
|:---|:---|:---|
| **Required Outcome** | What must be true. Expressed as a verifiable outcome using MUST. Any mechanism that achieves this outcome is conformant. | "Governance artifact integrity must be verifiable." |
| **Recommended Pattern** | How the protocol suggests achieving the outcome. Expressed using SHOULD. Alternatives are documented with rationale. Deviation requires documented justification. | "Signed provenance tokens using a registry-approved algorithm. See Appendix for alternatives." |
| **Reference Mechanism** | A specific mechanism the initial specification proposes. Informative. Published as a starting point for working group deliberation. Implementations may use any mechanism that satisfies the Required Outcome. | "Ed25519 is the v1 recommended algorithm. Rationale: [...]. Alternatives considered: [...]." |

Where the protocol specifies a Recommended Pattern or Reference Mechanism, the specification **MUST** document the rationale for the recommendation and identify known alternative approaches that achieve the same Required Outcome. This enables informed deliberation by the working group and informed deviation by implementors.

### Article 5 — Conformance Is Role-Based and Decomposed

The protocol defines requirements per participant role, not per implementation. Roles include governance orchestrator, telemetry contributor, agent builder platform, enterprise deployer, and field deployment. Each role has specific, testable conformance requirements. Conformance is further decomposed into orthogonal dimensions so that a single blended conformance level does not mask strengths in one area and weaknesses in another. Composite levels MUST NOT hide weaknesses in any dimension; each dimension is reported independently.

Every MUST-level requirement MUST be objectively testable. No protocol capability advances to *Recommended* status without at least two independent interoperable implementations and a passing conformance test suite. Conformance testing infrastructure is developed alongside the specification, not after deployment. Partial conformance MUST be explicitly declared; undeclared non-conformance is a conformance violation.

### Article 6 — Extend Safely, Evolve Deliberately

The protocol defines formal extension points. All extensions must be safely ignorable by conformant implementations and must not break interoperability when unsupported. The protocol core is kept small — elements needed by the majority of implementations — with formal profiling mechanisms for domain-specific and deployment-specific requirements.

Protocol elements may be deprecated but MUST NOT be removed while any active conformant implementation depends on them, as demonstrated by the conformance program. Protocol invariants (Section 5) are never deprecated.

---

## 4. Specification Types

The APP document series comprises the following specification types. Each type has a defined normative status and update cadence.

| **Type** | **Purpose** | **Normative Status** |
|:---|:---|:---|
| **Protocol Constitution (APP-1)** | Governing principles, Priority of Constituencies, protocol invariants, specification type definitions. Stable across versions. | Normative. Overrides all other APP documents. |
| **Protocol Objectives (APP-0)** | Enterprise-level Required Outcomes the protocol delivers. Outward-facing. Every requirement in APP-2 through APP-5 MUST be traceable to an Objective. Governed by APP-1 Priority of Constituencies (§2) and Protocol Invariants (§5). | Normative. Peer to APP-2, APP-3, APP-4, APP-5. |
| **Core Technical Specification (APP-2)** | Protocol capabilities, schemas, maturity model, and normative requirements. The WHAT of governed process execution. | Normative. |
| **Architecture Chapters (APP-3, APP-4, ...)** | Domain-specific protocol requirements: security architecture, entity correlation. Equal standing with the Core Specification. | Normative. |
| **Conformance Profiles (APP-5, ...)** | Role-based and domain-specific conformance definitions. Define what each participant role must implement for a given deployment context. | Normative per profile. |
| **Implementation Guides (APP-IG series)** | Adoption guidance and worked examples. Help implementors understand what the protocol asks without reading the full specification. | Informative. |
| **Illustrative Reference Artefacts (APP-R series)** | Non-normative reference realisations of specific normative requirements — reference schemas, reference bindings, worked examples of concrete representation. Illustrate one way a requirement can be satisfied; implementations may deliver equivalent conformance via other realisations. Each APP-R artefact cites the normative requirement(s) it realises. | Informative. Non-normative; carries no conformance obligation and makes no conformance claim. |

**Precedence between normative documents of equal standing.** Where a conflict exists between APP-2 and an Architecture Chapter (APP-3, APP-4) that cannot be resolved by reading both documents together: (a) On security-specific matters, the Architecture Chapter defining the security requirement prevails. (b) On conformance-specific matters — which requirements apply to which role at which L-level — APP-5 prevails. (c) On all other matters, the conflict MUST be resolved through the working group process before either document is ratified. Where a normative document explicitly qualifies a requirement in another normative document, the qualification MUST be cross-referenced in both documents. Unilateral qualification without bilateral cross-reference is not normatively effective.

**Change-impact manifest requirement.** A normative change to any APP-0 through APP-5 document is not eligible for ratification unless the change-impact manifest below identifies every affected normative and informative document, the required edits, and unresolved deviations. This is the operational enforcement of the bilateral cross-reference rule above. Every normative revision proposal MUST include:

| Change field | Required content |
|:---|:---|
| Changed requirement IDs | Exact IDs and semantic delta (added / removed / semantically changed / reclassified) |
| Affected normative documents | APP-0 through APP-5 — which documents require concurrent revision |
| Affected informative documents | APP-IG-01 through APP-IG-05 — which guides require concurrent revision; APP-R series — which illustrative reference artefacts require concurrent revision |
| Cross-reference updates | IDs, sections, and reciprocal links that must be updated |
| APP-5 applicability impact | Role × L-level applicability additions or removals |
| Traceability impact | APP-IG-02 §7 Objective mapping, STRUCT/INFO/Objective-realising status changes |
| Test impact | New or amended APP-5 conformance tests (T-* IDs added or revised) |
| Migration impact | Backwards compatibility and version-negotiation implications for adopters |
| Suite baseline regeneration | New suite manifest version and the artefacts that must be regenerated concurrently |

This manifest is the practical control that prevents independent evolution of normative documents from becoming independent contradiction. Working groups reviewing a proposed revision reject any submission that does not carry the full manifest.

**Precedence for APP-0 conflicts.** Where a conflict exists between APP-0 Objectives and a downstream specification (APP-2 through APP-5), the conflict MUST be resolved through the working group process. APP-0 states outcomes; APP-2 through APP-5 realise them. Where a downstream specification cannot realise a stated Objective, either the specification evolves to close the gap or the Objective evolves through the APP-0 amendment procedure. APP-1 (Constitution) overrides APP-0 on any conflict, consistent with APP-1's constitutional supremacy over all other APP documents. APP-5 prevails on conformance-specific matters — which requirements apply to which role at which L-level.

The Constitution never specifies deployment patterns, vendor-specific integration details, or market positioning. These live in Implementation Guides (informative) and in implementor documentation outside the protocol series.

---

## 5. Protocol Invariants

The following properties are fundamental to the protocol and will not change across versions. Future versions may refine how these properties are expressed, but must not eliminate or contradict them. Protocol invariants may only be amended through the constitutional amendment process.

- The protocol distinguishes between rule-based and judgment-dependent process steps, and this distinction governs oversight requirements.

- Governance evidence is assembled during execution, not reconstructed retrospectively from event logs.

- The protocol is designed for governance across system boundaries — including boundaries between independent vendors, between different products from a single vendor, between an enterprise's own systems and third-party AI, and between subsystems within a single vendor's estate that participate in distinct governance roles. Cross-vendor interoperability is the protocol's design target. Single-vendor adoption is a permitted deployment topology when the same governance standard applies; the protocol does not offer a reduced governance standard for internal deployments, and a single-vendor adopter is not credited with cross-vendor interoperability by adoption alone.

- Human oversight quality is measured, not merely required. The presence of a human checkpoint is insufficient; the protocol requires evidence that the human exercised genuine judgment.

- The same protocol governs at every integration maturity level. What varies is evidence richness, not the governance standard.

- Governed processes improve through feedback loops. Execution evidence feeds process improvement. This learning mechanism is itself governed — it MUST NOT autonomously modify governance without human approval.

- Security controls MUST be demonstrably active before the governed data flows they protect. The protocol does not permit race conditions between data flow activation and security control deployment.

---

## 6. Non-Goals

The protocol explicitly does not address the following. These boundaries prevent scope creep and clarify the protocol's relationship to adjacent standards and systems.

- **The protocol is not a workflow engine.** It governs process execution; it does not orchestrate it. How steps are routed, scheduled, or executed is an implementation concern.

- **The protocol is not a policy language.** It encodes compliance constraints as governance attributes on process specifications; it does not define, interpret, or adjudicate regulatory policy.

- **The protocol is not a model specification.** It governs how AI models participate in processes; it does not specify model behaviour, alignment, or evaluation.

- **The protocol is not a replacement for enterprise system integration.** It governs the spaces between systems. Intra-system process execution is the vendor's domain.

- **The protocol is not an agent orchestration framework.** It integrates with agent orchestration frameworks (MCP, A2A) but does not compete with them. It adds governance to agent interactions; it does not define how agents communicate or delegate.

---

## 7. Governance

The protocol is designed for eventual governance by a neutral foundation consistent with established neutral open-standards governance practices. The Constitution does not define bespoke governance procedures. Instead, it establishes the following constraints that any governance structure must satisfy:

**Open participation.** Protocol development is open to all stakeholders. Contribution is merit-based. Financial contribution does not confer technical authority.

**Separation of concerns.** Financial and policy governance is separate from technical governance. A Technical Steering Committee (or equivalent) governs specification decisions; a governing board governs organisational and financial decisions.

**Rough consensus and demonstrated interoperability.** Specification advancement requires demonstrated interoperability, not voting majorities. The working group seeks consensus; where consensus cannot be reached, the Priority of Constituencies hierarchy governs.

**Constitutional amendment.** This Constitution may be amended only through a process requiring broad consensus of the governing body. Amendments to Protocol Invariants require the highest threshold of agreement the governance structure defines.

**Transitional amendment procedure.** Until a neutral foundation is established, constitutional amendments require documented consensus of at least two-thirds of active working group members, with a minimum 30-day review period. Protocol Invariant amendments require three-quarters consensus. This transitional procedure is superseded upon establishment of the foundation governance structure.

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 1.4
**Normative status:** Normative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-1 — Protocol Constitution.*
