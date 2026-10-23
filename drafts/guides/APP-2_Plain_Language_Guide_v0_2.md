# APP-2 Plain Language Guide

Agentic Process Protocol

## Core Technical Specification

|                                  |                                                              |
| :------------------------------- | :----------------------------------------------------------- |
| **Version**                      | 0.2 — Draft                                                  |
| **Date**                         | October 2026                                                 |
| **Status**                       | Draft — Pre-Working-Group                                    |
| **Audience**                     | Enterprise process owners, product leaders, ERP and application teams, AI-platform teams, systems integrators, auditors, and working-group participants |
| **Source document**              | APP-2 (Core Technical Specification)                         |
| **Purpose**                      | Explain the core APP governed-process model in plain language: what a process is supposed to do, what actually happened, who was accountable, and how the process can improve without weakening governance. |
| **Normative status**             | Informative. This guide does not define, create, modify, or override normative obligations. |
| **Companion documents**          | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles), APP-IG-01 through APP-IG-05 |
| **Suite baseline**               | **APP-2026-10-RC1** (Oct 2026)                               |
| **Manifest**                     | See APP-1 Constitution for the current suite manifest.       |
| **Release rule**                 | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |
| **Version-reference convention** | Companion documents are cited by name only in body prose. The manifest above is the sole non-historical source for companion versions. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** This is an informative plain-language companion to APP-2 (Core Technical Specification). It restates APP-2's protocol capabilities, maturity model, and cross-cutting requirements for non-specialist readers.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. This guide does not create, modify, or override normative requirements in APP-2 or any other APP document.
>
> **Use this document for:** Non-specialist orientation to APP-2's capability model, maturity levels, and conformance status semantics.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** APP-2 (authoritative source), APP-1 (constitutional authority), APP-5 (conformance profiles applying APP-2 capabilities to roles and L-levels).

---

## 1. What APP-2 Covers

APP-2 is the core description of a governed process.

It answers four connected questions:

```text
1. What was meant to happen?

2. What actually happened?

3. Who was responsible for the decisions and actions?

4. What should the organisation learn or improve next?
```

A governed process may involve people, AI agents, ERP systems, workflow tools, APIs, and external services. APP-2 provides a common way to describe the process and preserve a trustworthy account of its execution.

```text
PROCESS DESIGN                  PROCESS EXECUTION

Process Frame                  Process Execution Record
What should happen             What did happen

        \                         /
         \                       /
          ------ Governance ------
                  |
                  v
          Review, learning,
          and controlled change
```

APP-2 does not replace an ERP, workflow engine, agent runtime, integration platform, or process-mining tool. It supplies the governance structure that lets those systems participate in one accountable process.

---

## 2. The Two Core Records

### Process Frame: the governed blueprint

A **Process Frame** describes how a process is intended to run.

It provides a structured description of each step, including:

- The step identifier.
- The system expected to perform the step.
- Whether the work is deterministic or judgment-dependent.
- Dependencies between steps.
- The person or role accountable for the step.

```text
EXAMPLE: PURCHASE-ORDER EXCEPTION

Step 1: Detect an exception
System: ERP
Type: Deterministic
Accountability: Finance operations

        ↓

Step 2: Assess whether the exception is legitimate
System: AI-assisted review service
Type: Judgment-dependent
Accountability: Finance manager

        ↓

Step 3: Release, reject, or escalate
System: Payment platform
Type: Deterministic after authorised decision
Accountability: Treasury operations
```

The Process Frame is not simply a workflow diagram. It carries the governance context required to understand what each step is allowed to do and how it should be reviewed.

### PxER: the governed execution record

A **Process Execution Record**, shortened to **PxER**, records how one actual process instance ran.

```text
PROCESS FRAME
The approved design

        ↓

PROCESS EXECUTION RECORD
The evidence of the actual run

        ↓

QUESTION
Did the actual process follow the approved design?
```

A PxER is built while the process is running, rather than reconstructed later from scattered logs, emails, tickets, and human memory.

At a minimum, its step records identify:

- The step that ran.
- The system that ran it.
- When it ran.
- The source-system transaction or reference.
- The intended execution type.
- The observed execution type where this can be known.
- The resulting conformance state.
- The trust boundary of the evidence.

The PxER makes it possible to investigate a real process instance without relying on one application’s partial view.

### PxER extension points

A PxER is one governed execution record with named extensions for different kinds of evidence.

```text
PxER STEP RECORD

Core execution and conformance information
        +
entity_refs
Business entities observed during the step
        +
governance_events
Serious governance events and safe-state transitions
        +
recovery_evidence
What happened when the primary path deviated
```

APP-4 defines the `entity_refs` extension for entity-aware process evidence. APP-3 defines the `governance_events` extension for severe governance events and safe-state transitions. APP-2 defines `recovery_evidence` for recovery activity associated with the original process step.

These extensions do not create separate process records. They add relevant evidence to the same PxER so an assessor can understand the execution, its entities, its recovery activity, and any governance interruption together.

---

## 3. Deterministic and Judgment Work

APP-2 separates process work into two broad categories.

| Type                  | Plain-language meaning                                       | Example                                                  |
| :-------------------- | :----------------------------------------------------------- | :------------------------------------------------------- |
| **Deterministic (D)** | A known rule should produce a repeatable result.             | Check whether an invoice total matches a purchase order. |
| **Probabilistic (P)** | The result depends on context, interpretation, judgment, or AI reasoning. | Decide whether an invoice exception is legitimate.       |

This distinction matters because not all work needs the same governance.

```text
DETERMINISTIC WORK

Input + rule
     |
     v
Repeatable result


JUDGMENT-DEPENDENT WORK

Input + context + interpretation
     |
     v
Decision requiring evidence,
accountability, and appropriate oversight
```

APP-2 also distinguishes two forms of judgment-dependent work:

- **Task-level P:** a bounded judgment within a structured process.
- **Orchestration-level P:** planning or decomposing a broader goal, where the plan itself is an output.

For example, classifying a single document may be task-level P. Designing the sequence of actions required to resolve an unusual customer case may be orchestration-level P.

---

## 4. The Conformance Question

Every governed step has an intended classification in its Process Frame.

Where observable, the PxER records what kind of execution actually occurred.

```text
INTENDED: D
ACTUAL:   D

Result: MATCH
```

```text
INTENDED: D
ACTUAL:   P

Result: MISMATCH
Reason: a step expected to be rule-based used judgment or inference
```

The key governance question is:

```text
Did the process execute as the approved Process Frame said it should?
```

APP-2 uses four high-level conformance states:

| State            | Meaning                                                      |
| :--------------- | :----------------------------------------------------------- |
| **MATCH**        | Available telemetry or statistical evidence supports that the step followed its intended classification. |
| **MISMATCH**     | Available evidence shows that execution differed from the intended classification. |
| **UNVERIFIABLE** | The execution path cannot be determined with available evidence. The record distinguishes whether the step was intended to be deterministic or judgment-dependent. |
| **DEGRADED**     | Governance availability was interrupted during the step. This is not merely missing data; it records a governance-layer condition. |

A separate integrity signal can arise when statistical evidence contradicts a declared or reported execution path. This is a **CONFLICT**: it is treated as a mismatch because the evidence calls the stated classification into question.

A mismatch is not automatically proof of wrongdoing. It is a governance signal: the process owner needs to understand why the step ran differently from the approved design.

---

## 5. Evidence Is Not Telemetry

A useful distinction in APP-2 is the difference between **evidence** and **telemetry**.

| Information type | Main purpose                                                 | Example                                                      |
| :--------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Evidence**     | Supports accountability, audit, review, and governance decisions. | The decision, approver, applicable rule, and source transaction reference. |
| **Telemetry**    | Supports technical observation and troubleshooting.          | Latency, resource use, retry counts, debug events, or service-health metrics. |

Both are valuable, but they are not interchangeable.

```text
Telemetry may tell an engineering team:

"The API call took 2.4 seconds."

Evidence may tell an auditor:

"The payment hold was released by this authorised person,
after reviewing this exception, under this approved process version."
```

A system can have abundant technical logs and still lack governance-quality evidence.

---

## 6. Accountability and Human Review

APP-2 treats accountability as more than identifying the final approver.

A governed step can require evidence across three layers:

```text
1. INTENT
   Who defined the process and applicable constraints?

2. EXECUTION
   Who or what performed the action?

3. OVERSIGHT
   Who reviewed a judgment-dependent action,
   what information was reviewed,
   and was the review meaningful?
```

This matters when AI contributes to a process.

A record that says only “approved” is often inadequate. A credible oversight record may need to show the decision made, the time spent, the evidence reviewed, and whether the review reflected real engagement rather than automatic confirmation.

```text
WEAK OVERSIGHT RECORD

"Approved by Manager A"


STRONGER GOVERNANCE RECORD

"Manager A reviewed the exception,
considered the cited evidence,
recorded a decision,
and the process preserved the applicable context."
```

APP-2 does not prescribe one user interface for human review. It establishes the governance need: oversight quality must be measurable, not assumed.

---

## 7. Compliance and Recovery

### Compliance context

A process may contain constraints that cannot be treated as ordinary business preferences.

For example:

```text
A background check must clear
before privileged system access is provisioned.
```

APP-2 distinguishes constraints that are externally mandated from constraints the enterprise can change itself. This supports a crucial governance question:

```text
Did a later configuration change weaken a control
that should not have been weakened?
```

The protocol does not determine the law in a particular jurisdiction. It provides a way for governed processes to carry and evidence applicable constraints.

### Recovery is part of the process

Processes do not always follow their primary path.

A downstream system may time out, an approval may be denied, an external service may return an error, or an exception may require an alternate route.

```text
PRIMARY PATH

Submit request
     |
     v
External service times out
     |
     v
RECOVERY PATH

Retry, escalate, compensate,
or move to a safe alternative
```

APP-2 treats recovery as governance-relevant because it can change what happens under time pressure.

A recovery record helps explain:

- Which recovery path was used.
- Who or what initiated it.
- Which authority allowed it.
- What evidence supported it.
- Whether it succeeded, failed, was bypassed, or resolved without intervention.
- Whether this was the first recovery attempt or a later one.

Recovery evidence belongs to the original step’s record. It does not turn the recovery into a separate process step.

---

## 8. Four Integration Levels

APP-2 recognises that enterprises do not all have the same integration depth.

| Level                         | Plain-language description                                   | Typical evidence position                                    |
| :---------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **L1 — Screen/RPA**           | Governance is added around screen-based or robotic-process interactions. | Limited direct visibility into internal application activity. |
| **L2 — API/MCP**              | Systems connect through APIs or agent-to-tool integration.   | Stronger transaction-level evidence, but not always full internal observability. |
| **L3 — Application-Enhanced** | Applications contribute richer execution telemetry directly. | Better ability to assess what happened inside participating applications. |
| **L4 — AI-Native**            | Governance evidence is produced structurally within the environment. | The strongest opportunity for governance by construction.    |

The goal does not change by maturity level.

```text
The governance outcome stays the same:

Can the enterprise show what was intended,
what happened, who was accountable,
and what evidence supports that account?
```

What changes is the richness and directness of the available evidence.

---

## 9. Learning Without Silent Weakening

A governed process should improve over time, but improvement must not become an unreviewed way to weaken controls.

APP-2 supports a controlled learning loop.

```text
PROCESS FRAME
Approved process design

        ↓

PxER RECORDS
Evidence from real executions

        ↓

ANALYSIS
Patterns, drift, recurring failures,
and possible improvement opportunities

        ↓

GOVERNED CHANGE
Review, approval, traceability,
and an updated Process Frame
```

The protocol supports several connected activities:

- Identifying recurring patterns that may justify a more deterministic process design.
- Recording how and why a classification changed.
- Tracking the maturity and lifecycle of a process definition.
- Detecting drift between expected and actual execution.
- Producing process intelligence from governed execution evidence.

The essential safeguard is that evidence may inform a recommendation, but evidence does not silently rewrite the approved process.

---

## 10. Where APP-2 Stops

APP-2 provides the common governance model. It does not define every adjacent concern.

| Topic                                                     | Primary APP source |
| :-------------------------------------------------------- | :----------------- |
| Enterprise governance outcomes                            | APP-0              |
| Constitutional principles and document precedence         | APP-1              |
| Security controls for governed-process risks              | APP-3              |
| Entity references and cross-system entity correlation     | APP-4              |
| Participant roles, conformance scope, and testable claims | APP-5              |

APP-2 also does not prescribe:

- A particular AI model or agent framework.
- A particular workflow engine.
- A single database, event store, or logging architecture.
- A vendor-specific API or product integration.
- A universal business ontology.
- Legal conclusions for a particular organisation or jurisdiction.

Its purpose is narrower and foundational: establish the shared process-and-evidence model required for accountable AI-enabled enterprise execution.

---

## 11. A Short Example

Consider an employee onboarding process.

```text
1. Create employee record
2. Start background check
3. Request equipment
4. Provision access
5. Review any background-check exception
6. Confirm the final onboarding state
```

A Process Frame defines the intended steps, dependencies, responsible systems, classifications, constraints, and accountable parties.

```text
PROCESS FRAME

Create employee record      D
Start background check      D
Request equipment           D
Provision access            D, only after check passes
Review exception            P, with human review
Confirm final state         D
```

A PxER then records the actual execution.

```text
PROCESS EXECUTION RECORD

Background check started:      yes
Access provisioned:            after check cleared
Exception review required:     no
Evidence assembled:            during execution
Frame version used:            recorded
Source transactions:           linked
```

If access is provisioned before the required check clears, the PxER gives the enterprise a basis to investigate the execution, identify the accountable control path, and improve the process without relying on disconnected application logs.

---

## 12. Key Takeaway

APP-2 creates a shared governance language for enterprise processes involving AI, people, and applications.

```text
PROCESS FRAME
What should happen

        +

PxER
What did happen

        +

ACCOUNTABILITY
Who was responsible

        +

CONFORMANCE
Did execution follow the approved design

        +

GOVERNED LEARNING
How can the process improve without weakening controls
```

This is the core APP model. APP-3 protects it, APP-4 makes it entity-aware, and APP-5 defines what different participants must demonstrate when claiming conformance.

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 0.2
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-2 Plain Language Guide — Core Technical Specification — Plain Language Guide.*
