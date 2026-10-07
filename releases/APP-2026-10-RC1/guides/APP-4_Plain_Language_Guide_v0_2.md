# APP-4 Plain Language Guide

Agentic Process Protocol

## Entity Correlation Architecture

|                                  |                                                              |
| :------------------------------- | :----------------------------------------------------------- |
| **Version**                      | 0.2 — Draft                                                  |
| **Date**                         | October 2026                                                 |
| **Status**                       | Draft — Pre-Working-Group                                    |
| **Audience**                     | Enterprise process owners, data and integration leaders, ERP and application teams, AI-platform teams, systems integrators, auditors, and working-group participants |
| **Source document**              | APP-4 (Entity Correlation Architecture)                      |
| **Purpose**                      | Explain how APP captures, links, and verifies business entities across governed process execution in plain language. |
| **Normative status**             | Informative. This guide does not define, create, modify, or override normative obligations. |
| **Companion documents**          | APP-0 (Protocol Objectives), APP-1 (Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-5 (Conformance Profiles), APP-IG-01 through APP-IG-05 |
| **Suite baseline**               | **APP-2026-10-RC1** (Oct 2026)                               |
| **Manifest**                     | See APP-1 Constitution for the current suite manifest.       |
| **Release rule**                 | This document is a coordinated-baseline artefact only when its version and the manifest above both match the suite baseline record. |
| **Version-reference convention** | Companion documents are cited by name only in body prose. The manifest above is the sole non-historical source for companion versions. |

> [!IMPORTANT]
> ## Reader Reference
>
> **Document role:** This is an informative plain-language companion to APP-4 (Entity Correlation Architecture). It restates APP-4's cross-system entity-tracking requirements and the three-class applicability model for non-specialist readers.
>
> **Status:** Informative.
>
> **Authority and precedence:** Informative. This guide does not create, modify, or override normative requirements in APP-4 or any other APP document.
>
> **Use this document for:** Non-specialist orientation to entity-correlation concepts, three-class applicability, and status-class enforcement rules.
>
> **Do not use this document as:** the authoritative source of normative requirements or conformance obligations.
>
> **Related documents:** APP-4 (authoritative source), APP-3 §S14 (entity-security implications).

---

## 1. What APP-4 Covers

APP-4 makes governed process evidence aware of the business entities affected by each process step.

APP-2 can record that a process step ran in an HR, ERP, payroll, CRM, or IT system. APP-4 adds the ability to record and relate the business entities that moved through those steps.

```text
WITHOUT ENTITY CORRELATION

Step 2 ran in HR
        ↓
Step 5 ran in IT
        ↓
Step 8 ran in Payroll

Question:
Did all three steps concern the same employee?


WITH ENTITY CORRELATION

Step 2: Employee record E-1042
        ↓
Step 5: User account U-1042
        ↓
Step 8: Payroll person P-1042

Question:
Do these references represent the same
business entity across the governed process?
```

The goal is not to create a universal business ontology. The goal is to make process evidence capable of showing which entities were involved, how they were related, and whether their state remained consistent across the process.

---

## 2. The Entity-Evidence Gap

Enterprise systems usually store information about their own transactions and records.

An HR system may know about an employee. An identity system may know about a user account. A finance system may know about a cost centre. Each record can be internally valid while the end-to-end process remains difficult to reconstruct.

```text
HR SYSTEM

Employee: EMP-10024


IT SYSTEM

Account: USER-8841


FINANCE SYSTEM

Cost Centre Assignment: CC-309


MISSING QUESTION

Which of these records were related in the same
onboarding process instance?
```

This gap exists in both cross-system and single-application processes.

```text
CROSS-SYSTEM CASE

HR → Identity platform → Payroll


SINGLE-APPLICATION CASE

ERP procurement module → ERP inventory module → ERP finance module
```

A single application can contain multiple modules, asynchronous integrations, different data structures, and separate operational records. Entity correlation helps preserve the relationship between relevant records across those process steps.

---

## 3. What Is an Entity?

An **entity** is a business object or identity that matters to a process.

Examples include:

- Employee.
- Candidate.
- Customer.
- Supplier.
- User account.
- Asset.
- Purchase order.
- Invoice.
- Cost centre.
- Contract.
- Shipment.
- Case.
- Product.
- Financial account.

```text
EMPLOYEE ONBOARDING EXAMPLE

Employee
        +
User account
        +
Laptop asset
        +
Cost centre
        +
Payroll record
```

The same process can affect several entities at once. APP-4 helps record the relevant references and relate them in a way that supports audit, verification, and governed process intelligence.

---

## 4. The Core Model

APP-4 extends the two core APP-2 artefacts:

```text
PROCESS FRAME

What the process is intended to do
        +
Optional declaration of entity information
that may be extracted from a step


PxER

What actually happened
        +
Entity references recorded during execution
        +
Optional correlations linking references
across the process instance
```

The model can be understood in four stages.

```text
1. DECLARE

Identify which entity information a process step
may produce or expose.


2. RECORD

Capture relevant entity references in the execution record.


3. CORRELATE

Link related entity references across steps,
systems, or process instances.


4. VERIFY

Identify whether entity state is aligned,
divergent, unavailable, or otherwise uncertain.
```

---

## 5. Declaring Entity Information

A Process Frame step may include an `entity_extract` declaration.

In plain language, this says:

```text
When this step runs, inspect these fields
for business-entity references.
```

For example:

```text
PROCESS FRAME STEP

Create employee record

Possible entity extraction declaration:

Response field: employee.id
Entity type: employee
Entity role: primary_key
```

An entity extraction declaration identifies:

- The field path in the step response.
- The entity type.
- The role that entity plays in the step.

APP-4 uses three basic roles:

| Role            | Plain-language meaning                                       |
| :-------------- | :----------------------------------------------------------- |
| **primary_key** | The principal entity being acted on in the step.             |
| **context_key** | An entity that provides important operational context.       |
| **reference**   | An entity mentioned or associated with the step, but not the main object of action. |

```text
EXAMPLE: APPROVE EXPENSE CLAIM

Primary entity:
Expense claim EC-904

Context entity:
Cost centre CC-220

Reference entity:
Employee EMP-118
```

The purpose is not to capture every available identifier. It is to capture enough entity context to make the governed process understandable and verifiable.

---

## 6. Use Optionality and Capability Applicability

This is the most important distinction in APP-4.

### Use optionality

A Process Frame step does not have to declare entity extraction.

```text
STEP A

No entity_extract declaration
        ↓
The step can still participate in governed execution.
```

A deployment can start with zero entity extraction declarations and add them gradually. This makes entity enrichment adoptable without blocking core process governance.

### Capability applicability

At L2 and above, an implementation’s ability to perform entity correlation is not optional merely because a particular process does not currently use it.

```text
L2+ IMPLEMENTATION

No current Frame declares entity_extract
        ↓
The implementation still needs the capability
to perform correlation when a governed Frame
does declare entity information.
```

The distinction is:

| Concept                      | Question                                                     | Plain-language answer                                        |
| :--------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Use optionality**          | Does every process step have to extract entities?            | No. Individual steps may omit entity extraction.             |
| **Capability applicability** | Does an L2+ governance implementation need correlation capability? | Yes. The implementation must be able to provide it when called upon. |

```text
OPTIONAL USE

"Do we use entity extraction in this step?"


REQUIRED CAPABILITY AT L2+

"Could this implementation perform correlation
for an eligible step or process scope?"
```

Using the word “optional” without explaining which of these meanings is intended creates confusion. APP-4 separates them deliberately.

---

## 7. Recording Entity References

When a Process Frame step declares entity extraction, the corresponding execution evidence can record entity references in the PxER.

```text
PROCESS STEP

Provision user access


EXECUTION RESPONSE

employee_id: EMP-10024
account_id: USER-8841
application: ERP-FINANCE


PxER ENTITY REFERENCES

Employee: EMP-10024
User account: USER-8841
Application: ERP-FINANCE
```

An entity reference records a usable description of the entity observed during execution.

| Information              | Plain-language purpose                                       |
| :----------------------- | :----------------------------------------------------------- |
| **Entity type**          | Identifies what kind of business object the reference represents. |
| **System-scoped key**    | Identifies the record in the system that produced it.        |
| **Extraction method**    | Identifies how the reference was obtained.                   |
| **Role**                 | Explains whether it is the main entity, context, or a reference. |
| **Confidence indicator** | Can indicate how reliable an extracted reference is where available. |

A system-scoped key is important because the same raw value can have different meanings in different systems.

```text
SYSTEM A

Customer ID: 10024


SYSTEM B

Supplier ID: 10024


THE VALUES MATCH,
BUT THE BUSINESS MEANINGS MAY NOT.
```

APP-4 avoids assuming that equal-looking values across systems automatically identify the same entity.

---

## 8. Correlating Entity References

Entity correlation links entity references across steps.

```text
ONBOARDING PROCESS INSTANCE

HR step:
Employee EMP-10024

        ↓

Identity step:
User account USER-8841

        ↓

Payroll step:
Payroll person PAY-7421

        ↓

CORRELATION

These records are connected to the same
governed onboarding instance.
```

Correlation may be based on two broad sources.

### Inferred correlation

Inferred correlation is derived from execution evidence.

```text
REPEATED OBSERVATION

HR employee EMP-10024 repeatedly co-occurs
with identity account USER-8841 in the same
governed process context.

        ↓

The implementation may infer a relationship,
subject to declared evidence and confidence rules.
```

Inference can help an organisation learn from process execution without requiring a pre-existing master-data system.

### Populated correlation

Populated correlation comes from an existing source of business relationship information.

```text
EXISTING ENTERPRISE SOURCE

Master data system:
Employee EMP-10024 ↔ User account USER-8841

        ↓

APP correlation registry:
Records the source-provided relationship
and its provenance.
```

Sources can include master-data systems, integration platforms, data lakes, semantic layers, or other enterprise records. APP-4 does not replace those systems. It provides a way for governed process evidence to use and reconcile the relationships they provide.

---

## 9. Cold-Start Behaviour

A new implementation may not yet have enough evidence to make reliable inferred-correlation claims.

APP-4 treats this as a normal early condition.

```text
EARLY DEPLOYMENT

Limited execution history
        ↓
Insufficient evidence for reliable inference
        ↓
State: no correlation
```

“No correlation” is not the same as “low confidence.”

```text
NO CORRELATION

The implementation does not yet have enough
basis to claim a relationship.


LOW CONFIDENCE

A relationship claim exists,
but its reliability is weak.
```

The protocol avoids encouraging systems to make premature entity-linking claims merely because some data has been observed.

During this stage, an implementation may use populated correlations if suitable sources are available, or it may operate without available entity correlation for the affected scope.

---

## 10. Reconciliation

Inferred and populated information may agree, disagree, or exist on only one side.

Reconciliation makes these conditions visible.

```text
INFERRED CORRELATION

Employee EMP-10024 ↔ Account USER-8841


POPULATED CORRELATION

Employee EMP-10024 ↔ Account USER-8841


RESULT

Aligned
```

Possible reconciliation outcomes include:

| Status             | Plain-language meaning                                       |
| :----------------- | :----------------------------------------------------------- |
| **aligned**        | Inferred and populated information support the same relationship. |
| **divergent**      | The available sources disagree about the relationship.       |
| **populated_only** | A populated source provides the relationship, but inference does not. |
| **inferred_only**  | Inference identifies a relationship, but no populated source supports it. |
| **error**          | Reconciliation could not be completed, for example because a source was unavailable or unreliable. |

“No correlation” is different from a reconciliation outcome. It is the condition in which the implementation has no relationship claim to reconcile, such as during an early deployment with insufficient evidence.

A divergent result is an operational signal, not an automatic conclusion about which source is correct.

```text
DIVERGENT EXAMPLE

HR record:
Employee EMP-10024 reports to Manager A

Finance assignment:
Employee EMP-10024 linked to Manager B

        ↓

A governed process can surface the difference
for the appropriate operational or governance review.
```

The purpose is to make cross-system inconsistency visible in the context of an actual governed process instance.

---

## 11. Correlation Registry and Drift

Entity relationships can become more useful over time when they are retained with their provenance, confidence, and scope.

```text
PROCESS INSTANCE 1

Employee EMP-10024 ↔ Account USER-8841

        ↓

PROCESS INSTANCE 2

Same relationship observed again

        ↓

ENTITY CORRELATION REGISTRY

Persistent record of the relationship,
where it came from, how confident it is,
and whether it remains valid
```

A correlation may begin as **process-scoped**, meaning it is useful only within the Process Frame where it was discovered. A correlation can later become **global** for the tenant when it has been governed for reuse across relevant processes.

Correlation is not permanent by default. Organisational restructures, migrations, mergers, changed identifiers, and integration failures can cause previously stable relationships to diverge. APP-4 calls this **correlation drift**.

```text
PREVIOUSLY STABLE RELATIONSHIP

Employee EMP-10024 ↔ Account USER-8841

        ↓

New process evidence no longer supports it

        ↓

CORRELATION DRIFT

        ↓

Signal for operational or governance review
```

The registry preserves compounding value across process instances while ensuring that old relationships can be assessed, revised, limited in scope, or retired.

---

## 12. Entity Flow Verification

Correlation answers:

```text
Which business entities were involved,
and how are their records related?
```

Entity flow verification asks a different question:

```text
Did the relevant entity state propagate correctly
between the process steps and systems?
```

For example, an onboarding PxER may show that an HR employee record and a downstream payroll record belong to the same person. Entity flow verification can then assess whether the relevant state was consistent across the process.

```text
HR STEP

Employee EMP-10024
Pay group: Monthly


PAYROLL STEP

Payroll person PAY-7421
Pay group: Monthly


RESULT

The relevant state is consistent
for this entity in this process instance.
```

If the HR and payroll values differ, the result is a governed signal for investigation. Correlation alone establishes the relationship; flow verification checks whether the required state moved through the process as expected.

---

## 13. Why Entity Correlation Matters

### Cross-system audit

Entity-aware PxER records can reduce manual reconstruction work.

```text
AUDIT QUESTION

Which employee-offboarding instances had access
still active more than 24 hours after the HR termination event?


WITHOUT CORRELATION

Manually join HR, identity, workflow,
and ticketing records.


WITH CORRELATION

Query governed process evidence using
linked entity references and timestamps.
```

### Data consistency detection

Entity correlation helps detect cases where related systems hold inconsistent state for the same business object.

```text
HR:
Manager A

ERP:
Manager B

Identity platform:
Manager A

        ↓

Entity correlation makes the inconsistency
visible in the context of the process
that produced or depended on it.
```

### Process intelligence

Entity context can improve process analysis.

```text
QUESTION

Do purchase-order exceptions involving a certain
supplier category have longer cycle times,
more rework, or more frequent human escalation?
```

A process record with relevant entity context can support more precise analysis than isolated step logs alone.

### Discovery of undocumented patterns

Repeated co-occurrence can reveal stable business patterns that are not formally recorded elsewhere.

```text
REPEATED PATTERN

Cost centre CC-220
        +
Benefit plan BP-GOLD
        ↓
Observed consistently across similar process instances.
```

Such a pattern may become a candidate for review, documentation, or more deterministic process treatment. It does not become an approved rule solely because it was observed.

---

## 14. Security and Privacy Boundaries

Entity correlation creates useful visibility, but it must not become a route for excessive exposure.

```text
ENTITY CORRELATION VALUE

Cross-system process understanding


ENTITY CORRELATION RISK

Cross-tenant leakage,
unnecessary schema exposure,
or unauthorised disclosure of entity relationships
```

APP-4 works with APP-3 to protect several boundaries.

### Tenant isolation

Entity data and entity correlations should remain isolated between tenants.

```text
TENANT A

Employee and account correlations


TENANT B

Employee and account correlations


REQUIREMENT OF THE MODEL

No cross-tenant entity linking or disclosure.
```

### Access control inheritance

Entity data contained in a PxER should receive the relevant protections of the PxER rather than becoming an unprotected secondary dataset.

### Cross-enterprise boundaries

When a process crosses enterprise boundaries, a governing implementation can only reliably record what it observes at its own boundary.

```text
ENTERPRISE A
        |
        | boundary-observable interaction
        |
ENTERPRISE B

APP evidence should not claim unrestricted
visibility into Enterprise B's internal data.
```

### Entity extraction configuration

Field paths and extraction configuration can reveal sensitive source-system structure. Access to those declarations needs appropriate control.

---

## 15. What APP-4 Does Not Do

APP-4 has deliberate boundaries.

It does not:

- Define a universal business ontology.
- Require every organisation to use master data management.
- Replace MDM, integration, data-lake, graph, or semantic-platform products.
- Require entity extraction on every process step.
- Assume equal-looking identifiers across systems represent the same entity.
- Require one matching algorithm, graph database, storage model, or correlation engine.
- Provide a legal conclusion about privacy, data protection, sectoral rules, or jurisdiction-specific obligations.

```text
APP-4 DEFINES

The common governance outcomes for entity-aware
process evidence.


IMPLEMENTATIONS CHOOSE

How to extract, normalise, store, match,
reconcile, query, and operationalise that information.
```

---

## 16. How Stakeholders Use APP-4

### Enterprise process and data leaders

Use APP-4 to ask whether high-value processes can be understood at the entity level across the systems involved.

```text
Can the organisation show which employee,
supplier, customer, asset, or transaction
was affected across the full process?
```

### ERP and application teams

Use APP-4 to identify the entity information that an application can contribute to governed execution evidence.

The protocol does not require exposing all application data. It provides a disciplined way to contribute relevant, scoped entity references.

### AI-platform and agent teams

Use APP-4 to ensure that an agent’s activity can be tied to business outcomes, not only to tool calls or model traces.

```text
AGENT OBSERVABILITY

What tool did the agent call?


ENTITY-AWARE GOVERNANCE

What business entity was affected,
and how did that entity relate to other process steps?
```

### Auditors and assessors

Use APP-4 with APP-5 to understand the relevant conformance scope and with APP-3 to evaluate the security of entity data and correlations.

---

## 17. Key Takeaway

APP-4 makes governed process evidence entity-aware.

```text
PROCESS FRAME

What entity information may be relevant


        +

PxER

Which entity references were observed


        +

CORRELATION

How entity references relate across steps
and systems


        +

RECONCILIATION

Whether available relationship information
is aligned, divergent, incomplete, or unavailable


        +

ENTITY FLOW VERIFICATION

Whether relevant entity state moved through
the governed process as expected
```

The result is a governed process record that can explain not only what systems did, but also which business entities were involved and whether their cross-system state remained coherent.

APP-2 defines the core process and evidence model. APP-3 protects the related security boundaries. APP-4 adds entity-aware correlation and verification. APP-5 defines the role- and maturity-specific conformance scope.

---

## Publication status

**Status:** Draft for public consultation
**Suite release:** APP-2026-10-RC1
**Document version:** 0.2
**Normative status:** Informative
**Canonical suite manifest:** See the suite release manifest in the public release repository.
**Change record:** Maintained in the public release repository.

---

*End of APP-4 Plain Language Guide — Entity Correlation Architecture — Plain Language Guide.*
