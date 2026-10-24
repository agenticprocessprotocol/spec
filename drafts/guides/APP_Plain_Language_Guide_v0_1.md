# APP Plain Language Guide

Agentic Process Protocol

## Suite Orientation Companion

|                                  |                                                              |
| :------------------------------- | :----------------------------------------------------------- |
| **Version**                      | 0.1 — Draft                                                  |
| **Date**                         | October 2026                                                 |
| **Status**                       | Draft — Pre-Working-Group. Informative suite-orientation companion. |
| **Audience**                     | Non-technical readers, enterprise process owners, product stakeholders, implementation partners, buyers, auditors, and working-group participants |
| **Parent documents**             | APP-0 (Protocol Objectives), APP-1 (Protocol Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles) |
| **Purpose**                      | Explain, in plain language, what the APP suite is for, how its documents fit together, and where different stakeholders should start reading. |
| **Normative status**             | Informative. This companion does not define, create, modify, or override normative obligations. |
| **Companion documents**          | APP-IG-01 (Implementor’s Guide), APP-IG-02 (Cross-Reference Matrix), APP-IG-03 (Worked Example), APP-IG-04 (FAQ), APP-IG-05 (Protocol Objectives Realisation and Assurance Guide) |
| **Suite baseline**               | **APP-2026-10-RC1** (Oct 2026)                               |
| **Manifest**                     | See APP-1 Constitution for the current suite manifest.       |
| **Release rule**                 | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |
| **Version-reference convention** | Companion documents are cited by name only in body prose. The manifest above is the sole non-historical source for companion versions. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** This is an informative suite-orientation companion for readers who need a plain-language overview of APP, its intended outcomes, document relationships, and suggested reading paths.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. This guide does not create, modify, or override normative requirements or conformance obligations.
>
> **Use this document for:** Understanding the suite's purpose, stakeholder relevance, principal concepts, and where to begin reading.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** APP-0 through APP-5 for authoritative requirements; APP-IG-02 for detailed requirement mappings; the relevant APP implementation guide for implementation guidance.
>
> **Interpretation note:** Examples illustrate possible governed-process scenarios; they do not prescribe a product architecture, deployment topology, implementation mechanism, or legal conclusion.

---

## How to Read This Guide

This guide is for readers who need the shape of APP before reading individual specifications in depth.

Each section follows a simple pattern:

- The business problem.
- Why the topic belongs in a shared protocol.
- What each APP document contributes.
- A small ASCII picture where useful.

The guide stays at the protocol level. It explains the outcomes APP is intended to support, without prescribing how a particular vendor, enterprise, or systems integrator must build its product or deployment.

---

## 1. What APP Is

The Agentic Process Protocol is a shared framework for governing enterprise processes in which humans, AI systems, and business applications work together.

It is designed for situations where a business process crosses system boundaries. A process may begin in an ERP system, involve an AI agent, require human review, continue through a vendor application, and end in another enterprise system.

The core problem is that each participant may hold only part of the story.

```text
WITHOUT A SHARED GOVERNANCE LAYER

AI activity log     ERP transaction     Approval note     Vendor record
       \                  |                  |                 /
        \---------------- separate evidence ------------------/

Question:
Can anyone reliably show what happened across the whole process?


WITH APP

Process definition ---- Process execution ---- Shared evidence ---- Governed improvement
What should happen      What did happen        What can be checked  What should change
```

APP is not a replacement for enterprise applications, workflow engines, AI models, integration platforms, or agent communication standards. It provides the governance layer that helps those systems participate in one accountable process story.

---

## 2. Why It Exists

Enterprise systems have long recorded transactions well.

A purchase order, payroll change, customer record, or approval usually has a reference number, timestamps, and system-level history. These records are useful, but they may not fully explain an AI-assisted or cross-system decision.

For example, a business process may need to show:

- Which steps were routine and rule-based.
- Which steps required judgment.
- Whether a human genuinely reviewed a high-stakes decision.
- Which person or authority authorised an AI action.
- Whether the process ran as designed.
- Whether process controls changed later.
- Whether different systems acted on the same employee, supplier, asset, or transaction.

```text
A SIMPLE EXAMPLE: EMPLOYEE ONBOARDING

HR system -------- Background check -------- Human review -------- IT access
Create employee        Return result         Review exception      Provision account

The business needs more than:
"Each system completed its own task."

It may need to show:
"These actions concerned the same employee, followed the approved process,
used the required oversight, and produced evidence during execution."
```

APP exists to make that type of cross-system governance more consistent, reviewable, and portable.

---

## 3. The Main Idea

A governed process has a lifecycle.

```text
1. DEFINE
   What is supposed to happen?

          ↓

2. AUTHORISE
   Who can act, on whose behalf, and within what limits?

          ↓

3. EXECUTE
   Humans, AI agents, and enterprise applications do the work.

          ↓

4. RECORD AND VERIFY
   What happened, and did it follow the intended process?

          ↓

5. REVIEW AND IMPROVE
   What drifted, failed, changed, or became suitable for improvement?
```

APP turns this lifecycle into a shared governance model. It focuses on the process around AI-enabled work, rather than trying to define the AI model itself or replace the business applications that execute the work.

---

## 4. The Five Outcomes

APP-0 explains the enterprise-level outcomes that the rest of the suite is intended to make verifiable.

| Outcome                      | Plain-language question                                      | Why it matters                                               |
| :--------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Authorised Action**        | Who authorised this action, and can that authority be checked? | An AI action should be attributable to a legitimate accountable principal. |
| **Independent Verification** | Can a high-stakes AI judgment be checked through a separate path? | A system should not be the only judge of its own governance-critical decision. |
| **Bounded Agency**           | Is the AI limited to its declared authority, including when conditions become uncertain? | Individually small actions should not combine into an unapproved outcome. |
| **Execution-Time Evidence**  | What evidence was captured while the process was running?    | Evidence assembled only after the event can be incomplete or difficult to trust. |
| **Governed Change**          | How do we know the governance controls themselves were not quietly weakened? | Process safety can decline when approvals, constraints, or oversight settings change without proper review. |

These are the outcomes an enterprise can use to ask: “What should a credible governance claim actually demonstrate?”

---

## 5. The Document Suite

### APP-0: Protocol Objectives

**What it explains:** The governance outcomes APP aims to make demonstrable.

APP-0 is the business-facing entry point to the normative suite. It explains why authorised action, independent verification, bounded agency, execution-time evidence, and governed change matter.

Read APP-0 when the first question is:

```text
What should this protocol make possible for an enterprise,
an auditor, a regulator, or a process owner?
```

---

### APP-1: Protocol Constitution

**What it explains:** The rules that govern the protocol itself.

APP-1 establishes the principles, invariants, boundaries, and decision hierarchy that the rest of the suite must follow.

It sets the order of priority when trade-offs arise:

```text
1. Regulatory and compliance obligations
2. Process participants and people affected by decisions
3. Enterprise process owners
4. Platform implementors and vendors
5. Protocol authors
```

This means convenience for a platform or elegance in a specification does not take priority over compliance, meaningful human oversight, or enterprise auditability.

---

### APP-2: Core Technical Specification

**What it explains:** The common governance information that must be available across a process.

APP-2 defines the core language of governed process execution.

```text
PROCESS FRAME
The governed description of what should happen.

          ↓

PROCESS EXECUTION RECORD
The evidence of what actually happened.

          ↓

GOVERNED IMPROVEMENT
The controlled learning loop between design and execution.
```

A Process Frame describes the process: its steps, expected treatment, accountable parties, dependencies, and relevant governance attributes.

A Process Execution Record, or PxER, provides a durable record of how a specific process instance ran. It connects actual execution back to the governed process definition.

APP-2 also distinguishes between:

- **Rule-based work:** Work where known rules should produce a repeatable result.
- **Judgment-dependent work:** Work where context, interpretation, AI reasoning, or human judgment affects the result.

That distinction helps determine the right oversight, evidence, and review treatment for each step.

---

### APP-3: Security Architecture

**What it explains:** How the process definition, participants, evidence, and governance controls are protected.

APP-3 addresses the security conditions needed for a governance claim to be credible.

```text
PROCESS INSTRUCTIONS
Can the governing process definition be trusted?

        ↓

PROCESS PARTICIPANTS
Can the organisation verify who or what is acting?

        ↓

HUMAN OVERSIGHT
Can the reviewer rely on the information presented?

        ↓

EXECUTION EVIDENCE
Can the organisation trust the record of what happened?

        ↓

GOVERNANCE CONTROLS
Can important controls be weakened without appropriate review?
```

In plain language, APP-3 helps address risks such as:

- Process instructions being altered or rolled back.
- An agent claiming authority it does not have.
- A judgment-dependent task being treated as routine to avoid stronger oversight.
- Evidence being incomplete, misleading, or untrustworthy.
- Human review becoming ceremonial or being manipulated.
- AI authority continuing unchanged after a severe governance event.
- Agent interactions creating hidden coordination or authority paths.
- Security controls being activated after protected data has already started flowing.

APP-3 is not a product security architecture. It defines the shared security outcomes that must be addressed where they apply.

---

### APP-4: Entity Correlation Architecture

**What it explains:** How a process can show which real-world business entities were affected across systems.

A business process is not only a sequence of steps. It also affects people, suppliers, assets, accounts, cases, contracts, and transactions.

```text
PROCESS VIEW ONLY

Step A -------- Step B -------- Step C

Question:
Did these steps concern the same business entity?


ENTITY-AWARE VIEW

Step A ---- acts on ---- Employee
Step B ---- acts on ---- Employee
Step C ---- acts on ---- Employee

Now ask:
Did every system act on the same person correctly?
```

For example, an employee may have one identifier in HR, another in payroll, and another in IT identity systems.

```text
HR record:        Employee E-417
Payroll record:   Person P-9921
IT record:        Account AD-j.smith

APP-4 helps the governed record represent that these references
relate to the same person within the process context.
```

APP-4 helps make process evidence entity-aware. This can support audit reconstruction, cross-system consistency checks, compliance lineage, and process intelligence.

It does not replace master-data management. It governs the entity-aware evidence needed to understand what a governed process affected.

---

### APP-5: Conformance Profiles

**What it explains:** What a participant must declare and demonstrate when claiming APP conformance.

Not every participant plays the same role in a governed process.

```text
Governance Orchestrator
Applies governance across a process.

Telemetry Contributor
Provides execution evidence from an application or service.

Agent Builder Platform
Builds or configures participating agents.

Enterprise Deployer
Sets process scope, controls, and assurance expectations.

Field Deployment
Applies APP in a particular operating environment.
```

APP-5 maps applicable obligations to those roles and to different integration maturity levels.

| Level  | Plain-language meaning                                       |
| :----- | :----------------------------------------------------------- |
| **L1** | Limited or screen-level participation, with restricted evidence visibility |
| **L2** | API or tool-connected participation                          |
| **L3** | Applications contribute richer execution telemetry and evidence |
| **L4** | Governance is deeply designed into an AI-native environment  |

The important idea is that a conformance claim should be specific.

```text
Not enough:
"We support APP."

More meaningful:
"We claim conformance for this role, at this integration level,
with this evidence capability and these declared limitations."
```

---

## 6. How the Documents Connect

The documents are meant to be read as a coordinated suite.

```text
APP-0
What enterprise governance outcomes should be demonstrable?

        ↓

APP-1
What constitutional principles govern the protocol?

        ↓

APP-2
What common process and execution information is needed?

        ↓

APP-3
How is that governed process protected?

        ↓

APP-4
How does the record stay connected to real-world business entities?

        ↓

APP-5
What must each participant role demonstrate?

        ↓

APP-IG-01 to APP-IG-05
How do readers interpret, trace, apply, test, and assure the suite?
```

The suite has a deliberate division of responsibility:

- APP-0 explains the outcome.
- APP-1 governs the protocol.
- APP-2 defines the core governed-process model.
- APP-3 defines the security requirements.
- APP-4 defines the entity-correlation requirements.
- APP-5 defines conformance by role and integration level.
- The implementation guides support interpretation, adoption, traceability, examples, FAQs, and assurance.

---

## 7. A Running Example

Consider a supplier-payment exception.

```text
1. An ERP system detects an invoice exception.
2. An AI assistant prepares a proposed explanation.
3. A finance manager reviews the exception.
4. A payment system executes or holds the payment.
5. A supplier-management system updates the case.
```

The APP suite helps frame the questions around that process.

| APP document | Question in the example                                      |
| :----------- | :----------------------------------------------------------- |
| **APP-0**    | Can the enterprise prove authority, oversight, evidence, bounded action, and controlled change? |
| **APP-1**    | If speed conflicts with meaningful review, whose interest takes priority? |
| **APP-2**    | What was the intended process, what actually happened, and did execution match the process definition? |
| **APP-3**    | Can the enterprise trust the AI identity, approval surface, process instructions, and evidence record? |
| **APP-4**    | Did the ERP invoice, supplier case, and payment instruction refer to the same supplier and transaction? |
| **APP-5**    | Which participant provides what evidence at the declared integration level? |

The goal is not to make every system identical. The goal is to make governance information sufficiently shared and reliable across different systems.

---

## 8. The Implementation Guides

The APP-IG series is informative. These documents help readers use the normative suite without changing its requirements.

| Guide                                                        | Plain-language purpose                                       |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **APP-IG-01: Implementor’s Guide**                           | Helps ERP vendors, platforms, systems integrators, and enterprise technology teams understand adoption and role-specific implications. |
| **APP-IG-02: Cross-Reference Matrix**                        | Provides detailed mapping between requirements, capabilities, security domains, entity requirements, objectives, roles, and tests. |
| **APP-IG-03: Worked Example**                                | Shows how the documents apply together in a concrete governed-process scenario. |
| **APP-IG-04: FAQ**                                           | Addresses common questions about scope, interpretation, and adoption. |
| **APP-IG-05: Protocol Objectives Realisation and Assurance Guide** | Helps buyers, auditors, deployers, and assessors connect APP objectives to assurance evidence and implementation claims. |

---

## 9. Reading Paths

### Enterprise leaders, process owners, and buyers

Start with:

1. This guide.
2. APP-0 for the five governance outcomes.
3. APP-IG-05 for assurance and evidence questions.
4. APP-5 for the meaning of a role- and maturity-specific conformance claim.
5. APP-IG-03 for an end-to-end example.

### ERP vendors, AI platforms, and systems integrators

Start with:

1. This guide.
2. APP-1 for constitutional principles and protocol boundaries.
3. APP-2 for core process and evidence concepts.
4. APP-3 for applicable security outcomes.
5. APP-4 where entity-aware process evidence is in scope.
6. APP-5 for role and maturity-level obligations.
7. APP-IG-01 and APP-IG-02 for implementation interpretation and traceability.

### Auditors and assessors

Start with:

1. APP-0 to identify the outcome being assessed.
2. APP-5 to identify the claimed role, integration level, and applicable obligations.
3. APP-IG-05 to understand expected assurance evidence.
4. APP-IG-02 to trace detailed mappings.
5. The relevant APP-2, APP-3, and APP-4 requirements for the declared scope.

### Working-group participants

Start with:

1. APP-1 for constitutional principles, precedence, invariants, and change discipline.
2. APP-0 for the intended enterprise outcomes.
3. APP-2 through APP-5 for detailed requirements and role applicability.
4. APP-IG-02 to identify cross-document impact.
5. The applicable change-impact manifest for any proposed normative revision.

---

## 10. What APP Does Not Do

APP has clear boundaries.

- It does not replace a workflow engine or define how work is scheduled.
- It does not replace enterprise system integration standards.
- It does not define how an AI model is trained, aligned, or evaluated.
- It does not replace agent communication frameworks.
- It does not replace master-data management.
- It does not determine whether an organisation satisfies a particular law or regulation.
- It does not make a product safe merely because the product uses APP terminology.
- It does not prescribe one vendor architecture or internal implementation method.

APP focuses on governed process execution: the shared process definition, authority, oversight, evidence, cross-system accountability, and controlled evolution surrounding AI-enabled enterprise work.

---

## 11. The Key Takeaway

A credible governed process needs more than an AI agent, a workflow, and a collection of logs.

```text
A shared process definition
        +
Clear authority and accountability
        +
Meaningful human oversight where needed
        +
Evidence captured while the process runs
        +
Security protecting the instructions and record
        +
Entity awareness across systems where relevant
        +
A specific and testable conformance claim
```

That is the role of the APP suite.

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 0.1
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP Plain Language Guide — Plain Language Guide.*
