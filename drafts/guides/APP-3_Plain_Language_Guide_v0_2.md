# APP-3 Plain Language Guide

Agentic Process Protocol

## Security Architecture

|                                  |                                                              |
| :------------------------------- | :----------------------------------------------------------- |
| **Version**                      | 0.2 — Draft                                                  |
| **Date**                         | October 2026                                                 |
| **Status**                       | Draft — Pre-Working-Group                                    |
| **Audience**                     | Enterprise security leaders, product leaders, ERP and application teams, AI-platform teams, systems integrators, auditors, and working-group participants |
| **Source document**              | APP-3 (Security Architecture)                                |
| **Purpose**                      | Explain the APP security model in plain language: what it protects, why protection matters, and how security supports credible governed-process evidence. |
| **Normative status**             | Informative. This guide does not define, create, modify, or override normative obligations. |
| **Companion documents**          | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-2 (Core Technical Specification), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles), APP-IG-01 through APP-IG-05 |
| **Suite baseline**               | **APP-2026-10-RC1** (Oct 2026)                               |
| **Manifest**                     | See APP-1 Constitution for the current suite manifest.       |
| **Release rule**                 | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |
| **Version-reference convention** | Companion documents are cited by name only in body prose. The manifest above is the sole non-historical source for companion versions. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** This is an informative plain-language companion to APP-3 (Security Architecture). It restates APP-3's fourteen security domains and cross-cutting security principles for non-specialist readers.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. This guide does not create, modify, or override normative requirements in APP-3 or any other APP document.
>
> **Use this document for:** Non-specialist orientation to APP-3's security domains, outcome-versus-mechanism discipline, and cross-cutting principles.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** APP-3 (authoritative source), APP-1 Article 3 (security normativity discipline), APP-5 (role-based security applicability).

---

## 1. What APP-3 Covers

APP-3 protects the trustworthiness of a governed process.

A process cannot be credibly governed if its instructions can be changed without trace, its participants cannot be identified, its evidence can be fabricated, or detection of a serious event does not affect runtime behaviour.

```text
GOVERNED PROCESS

Approved process instructions
        +
Authorised participants
        +
Trustworthy execution evidence
        +
Meaningful human oversight
        +
Controlled recovery and change
        =
A governance claim that can be relied upon
```

APP-3 is not a general enterprise-security framework and does not replace an organisation’s security programme. It defines the security outcomes needed for the APP governed-process model to remain credible.

---

## 2. The Security Question

APP-2 defines the process blueprint and execution record.

APP-3 asks whether those records can be trusted.

```text
APP-2 QUESTION

What should happen,
and what did happen?


APP-3 QUESTION

Can the process definition, participants,
oversight, and evidence used to answer that
question be trusted?
```

A security failure in a governed process may not look like a conventional system compromise. It can appear as a classification change that avoids human review, an agent acting beyond its intended authority, or an approval surface influenced by untrusted content.

---

## 3. The Protection Model

APP-3 groups its security concerns into fourteen domains, supported by cross-cutting protections.

```text
PROCESS DEFINITION AND CONNECTIONS

S1  Frame Integrity
S2  Transport and Federation


GOVERNANCE EXECUTION

S3  Classification Integrity
S4  Evidence Integrity
S5  Human Oversight Security
S6  Compliance Validation
S7  Orchestration Integrity
S8  Promotion Integrity
S9  Feedback Loop Integrity
S10 Tenant Isolation


DEPLOYMENT AND ECOSYSTEM

S11 Supply Chain Security
S12 L1 Integration Security
S13 Agent Identity
S14 Entity Correlation Security


CROSS-CUTTING PROTECTIONS

Temporal activation ordering
Shared-substrate isolation
Authority reduction patterns
Adversarial verification
Safe-state transition on serious events
```

These domains are connected. A compromised Process Frame can affect classification, compliance, evidence, and oversight at the same time. The domain structure helps teams find the relevant security concern without implying that each concern is isolated.

S13 and S14 are first-class security domains. Their position in the diagram reflects that they span the ecosystem, not that they have lesser normative weight.

---

## 4. Protecting the Process Definition

### Frame integrity

A **Process Frame** is the governed description of how a process is supposed to run. If it can be changed silently, the rest of the governance model becomes unreliable.

```text
LEGITIMATE CHANGE

Authorised person or service
        ↓
Traceable change record
        ↓
Approved new version
        ↓
Participants use the new version


UNSAFE CHANGE

Untraceable modification or rollback
        ↓
Process runs under altered or weaker controls
```

APP-3 addresses four related risks:

- A Process Frame is changed by an unauthorised party.
- A legitimate change cannot be traced to its origin or authoriser.
- A consumer is induced to accept an older, weaker Frame version.
- The source material used to construct a Frame is untrustworthy.

The protocol is concerned with the security outcome: Process Frame changes must be attributable, traceable, and protected against unauthorised rollback. It does not prescribe a single product or storage architecture.

### Transport and federation

Governed processes can involve agents, ERP systems, platform services, and external organisations. Security must protect both the connection and the authority claims carried across it.

```text
MESSAGE OR AGENT CAPABILITY

Who sent this?
        ↓
Can the sender be authenticated?
        ↓
Is the message intact, current, and in sequence?
        ↓
Is the sender acting within its permitted authority?
        ↓
Can the authority be revoked when necessary?
```

APP-3 addresses secure transport, bound credentials, signed Agent Cards, protected stateful sessions, and controls for externally consumed agent capabilities.

It also addresses delegation-chain risk: authority should not become unbounded or untraceable simply because work passes through several agents or systems.

The protocol does not prescribe one transport product or identity platform. Its concern is that a receiving participant can establish the authenticity, integrity, validity, and permitted authority of the interaction.

---

## 5. Protecting Governance Decisions

### Classification integrity

APP-2 distinguishes deterministic work from judgment-dependent work.

```text
DETERMINISTIC WORK

Known rule
        ↓
Repeatable result


JUDGMENT-DEPENDENT WORK

Context and interpretation
        ↓
Decision requiring appropriate evidence
and oversight
```

This distinction is security-sensitive.

If a judgment-dependent activity is falsely represented as deterministic, the process may bypass the oversight, evidence, or accountability appropriate to judgment. APP-3 therefore treats D/P classification as a trust anchor, rather than merely as a technical label.

A process should be able to answer:

```text
Was the step classified as intended?

Was its actual execution consistent with that classification?

If evidence contradicts the stated classification,
was the contradiction surfaced for governance review?
```

### Human oversight security

Human approval is not automatically meaningful.

A reviewer can be influenced by misleading content, hidden instructions, incomplete evidence, or an interface that makes an AI recommendation appear to be verified fact.

```text
WEAK APPROVAL SURFACE

Untrusted content
        ↓
Appears as trusted information
        ↓
Reviewer approves under false confidence


STRONGER APPROVAL SURFACE

Verified evidence is distinguishable
from AI-generated advice
        ↓
Reviewer can make an informed decision
```

APP-3 addresses risks to approval surfaces and to the evidence that indicates whether a human review was genuine. It does not mandate a particular user-interface design; it establishes the security need for trustworthy and meaningful oversight.

### Compliance validation

A process can fail not only by violating a stated control, but also by omitting a control that should have existed.

```text
QUESTION

Does this compliance-relevant process contain
all constraints that should apply?


NOT ONLY

Did it follow the constraints already recorded?
```

This is sometimes called the **negative-space** problem. It matters because a missing control can be harder to identify than a visible violation of an existing one.

APP-3 also treats the recovery path as security-relevant. A process must not use a recovery path to apply compliance controls at a weaker enforcement tier than the primary path it replaces.

---

## 6. Protecting Evidence

### Evidence integrity

A Process Execution Record, or PxER, is useful only if an organisation can trust where it came from, whether it has been altered, and whether contributors were authorised.

```text
TRUSTWORTHY EVIDENCE

Execution occurs
        ↓
Evidence is captured during execution
        ↓
Contributor and write path are identifiable
        ↓
Evidence can be verified and reviewed
```

APP-3 keeps three questions separate because they answer different governance concerns:

| Question                                                 | Why it matters                                               |
| :------------------------------------------------------- | :----------------------------------------------------------- |
| Did the process execute on its intended D/P track?       | This is the conformance question.                            |
| Is a telemetry contribution authentic?                   | This addresses whether evidence is genuine.                  |
| Was the record created through an authorised write path? | This addresses whether an authorised component created or updated the evidence. |

A technical log can be valuable for troubleshooting while still being insufficient as governance evidence.

### Degradation and orchestration integrity

The governance layer can be unavailable, compromised, or operating with reduced visibility. APP-3 treats this as a governance condition, not merely an infrastructure availability issue.

```text
GOVERNANCE LAYER AVAILABLE

Normal governed execution


GOVERNANCE LAYER DEGRADED

Execution may need to pause,
continue under declared restrictions,
or be reconciled afterward,
depending on the process context
```

The appropriate response depends on the importance of the affected step. A low-risk activity may continue with an explicit governance limitation. A compliance-critical action may require a stricter response rather than proceeding without the required controls.

---

## 7. Safe-State Behaviour

A serious governance event cannot be treated only as a notification for someone to review later.

```text
SERIOUS EVENT DETECTED

Examples:
- Agent-initiated safety event
- Suspected covert agent communication
- Aggregate authority threshold breach
- Suspected poisoning of an adaptive baseline
- Attempted peer-authority elevation

        ↓

SAFE-STATE RESPONSE

No further privileged action for the affected scope
until accountable acknowledgement
or safe re-authorisation
```

The central rule is that no additional privileged action should occur for the affected agent, session, or delegation chain between detection of a serious event and entry into the safe state.

Examples of activity that should be blocked in the safe state include:

- Writing to external systems.
- Initiating financial actions.
- Acting on compliance-critical records.
- Affecting another agent’s session or delegation chain.
- Delegating authority to another agent.
- Changing governance-layer configuration.
- Invoking an action that requires human-in-the-loop engagement.

Read-only observation, evidence preservation, and low-risk deterministic maintenance can remain possible where the declared safe-state design permits them.

Leaving the safe state requires accountable acknowledgement or re-authorisation. It should not silently expire into autonomous resumption.

A credible record of the transition should allow later review to determine:

- What event triggered the safe state.
- Which agent, session, or delegation chain was affected.
- What restrictions applied.
- Who or what authorised entry.
- What condition governed exit.
- Who authorised exit and what happened next.

---

## 8. Adversarial Verification

Security claims need evidence that they were tested against attempts to bypass them.

```text
SECURITY CONTROL
        ↓
Adversarial exercise
        ↓
Pass, fail, coverage, and remediation evidence
        ↓
Assurance record available for review
```

APP-3 requires a named adversarial exercise suite for the security-relevant properties of the implementation. The suite is run before releases that affect required security outcomes and on an implementation-declared operational cadence.

Examples include testing for:

- Hidden agent communication through shared infrastructure.
- Attempts to raise peer authority.
- Suppression of safety events.
- Accumulated low-impact actions that exceed an aggregate threshold.
- Attempts to poison an adaptive baseline.

The aim is not to claim that a system is invulnerable. It is to ensure that key containment assumptions are actively tested and that the outcomes are retained as assurance evidence.

---

## 9. Preventing Authority Drift

Agentic systems can act through delegation chains, tool calls, sessions, and interactions with other agents.

A single action may appear acceptable in isolation while becoming unsafe in aggregate.

```text
SMALL ACTIONS

Action A: low impact
Action B: low impact
Action C: low impact

        ↓

COMBINED EFFECT

Accumulated authority or risk exceeds
what should be permitted without review
```

APP-3 addresses the need to preserve authority provenance: an organisation should be able to reconstruct what authority an agent had, where it came from, and whether a chain of delegated actions remained within acceptable bounds.

This is particularly important where an agent can affect external systems, financial activity, compliance-critical records, other agents, or governance-layer configuration.

---

## 10. Protecting Improvement Loops

Governed processes can improve from repeated execution, but learning and optimisation can become routes for governance weakening if evidence is manipulated or recommendations become unreviewed changes.

```text
VALID IMPROVEMENT PATH

Execution evidence
        ↓
Analysis
        ↓
Recommendation
        ↓
Governed review
        ↓
Approved Process Frame change


UNSAFE PATH

Manipulated evidence
        ↓
Automated recommendation
        ↓
Silent weakening of process governance
```

APP-3 protects several points in this cycle:

- **Promotion integrity:** prevents weak or manipulated evidence from prematurely converting judgment-dependent work into deterministic work.
- **Feedback-loop integrity:** prevents corrupted evidence from producing governance-weakening recommendations.
- **Tenant isolation:** prevents cross-deployment intelligence from exposing one tenant’s data or governance information to another.

The protocol does not prohibit learning. It protects the conditions under which learning informs accountable change.

---

## 11. Supply Chain and L1 Security

### Supply-chain security

A Process Frame template can influence many processes and many deployments. A compromised template can spread harmful changes at scale.

```text
TEMPLATE OR MARKETPLACE ITEM

One source artefact
        ↓
Used by multiple organisations or teams
        ↓
Potentially affects many governed processes
```

APP-3 addresses the need to establish trust in reusable Process Frame artefacts and the sources from which they originate.

### L1 integration security

L1 environments use screen-level or robotic-process automation integration. These environments may provide less direct visibility into internal application activity than API-connected or application-enhanced environments.

```text
L1 EXAMPLE

Bot observes a screen
        ↓
Bot performs an interaction
        ↓
Governance evidence may be less direct
than evidence from an integrated application
```

The protocol does not treat lower visibility as a reason to make weak claims. It requires the implementation to handle the limits of that evidence honestly and securely.

---

## 12. Agent and Entity Security

### Agent identity

For a governed process, it is not enough to know that an action occurred. The record may need to show which agent, session, or delegation chain acted and what authority supported that action.

```text
ACTION
        ↓
Which agent or session acted?
        ↓
What authority did it have?
        ↓
Who authorised that authority?
        ↓
Can the chain be reconstructed later?
```

Without identity and authority continuity, an organisation may know that a system performed an action but be unable to establish the accountable path that enabled it.

### Entity correlation security

APP-4 allows governed processes to capture and correlate business entities, such as employees, suppliers, accounts, assets, cases, and transactions.

That can substantially improve auditability, but it introduces additional security responsibilities.

```text
ENTITY-AWARE PROCESS EVIDENCE

HR employee identifier
        ↕
IT account identifier
        ↕
Payroll person identifier
```

The correlation data must be protected by appropriate access controls, isolated between tenants, and limited at cross-enterprise trust boundaries. Entity correlation should improve visibility without creating a new route for unauthorised disclosure.

---

## 13. Security by Integration Level

APP supports different integration depths, from screen-level automation to API-connected systems and AI-native environments.

| Level                         | Plain-language security position                             |
| :---------------------------- | :----------------------------------------------------------- |
| **L1 — Screen/RPA**           | The governance layer has limited direct visibility into internal application activity. Security must prevent limited observability from becoming an unacknowledged governance blind spot. |
| **L2 — API/MCP**              | Connected systems need trustworthy transport, identity, authority boundaries, and reliable evidence exchange. |
| **L3 — Application-Enhanced** | Applications contribute richer internal evidence, increasing the importance of contributor authentication and evidence verification. |
| **L4 — AI-Native**            | Governance evidence can be produced structurally within the environment, but accountability and security controls remain necessary. |

The desired security outcome is consistent across levels:

```text
A conformance claim should be honest about what can be
observed, verified, protected, and demonstrated
at the declared integration depth.
```

---

## 14. How Stakeholders Use APP-3

### Security leaders

Use APP-3 to assess security questions that arise specifically in governed AI-enabled processes.

- Can process definitions be silently weakened?
- Can an agent accumulate authority beyond its intended scope?
- Can a human approval surface be manipulated?
- Can a PxER be trusted?
- Does a detected severe event lead to a safe operational response?

### Application, ERP, and platform teams

Use APP-3 to distinguish the required security outcome from the implementation approach.

The protocol describes the security condition that needs to be true. It does not require every participant to use the same product, security architecture, runtime, or operational procedure.

### Assessors and enterprise buyers

Use APP-3 with APP-5.

APP-3 defines the security outcomes. APP-5 identifies which requirements apply to a claimed role and integration level. A credible assessment needs both: the applicable outcome and a clear statement of who is claiming conformance.

---

## 15. Where APP-3 Stops

APP-3 does not replace:

- Enterprise identity, access-management, and key-management programmes.
- Secure software-development practices.
- Product-specific threat modelling.
- Incident response, regulatory reporting, or legal obligations.
- Cloud, network, endpoint, and application-security baselines.
- Security architecture for concerns outside the governed-process scope.

Its purpose is focused: protect the integrity of the governance claims created through APP processes.

---

## 16. Key Takeaway

APP-3 makes governed-process security operational.

```text
TRUSTWORTHY PROCESS GOVERNANCE REQUIRES

Protected process instructions
        +
Identifiable and bounded participants
        +
Secure human oversight
        +
Authentic and authorised evidence
        +
Controlled recovery and improvement
        +
Safe response when serious governance events are detected
```

APP-2 defines the governed process and its execution record. APP-3 protects the integrity of that definition, execution, evidence, and response. APP-4 extends the model to entity-aware process evidence, and APP-5 defines role-specific conformance claims.

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 0.2
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-3 Plain Language Guide — Security Architecture — Plain Language Guide.*
