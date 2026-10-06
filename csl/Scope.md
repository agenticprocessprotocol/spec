# APP Scope

**Version:** 0.3 Draft
**Supersedes:** 0.2 Draft
**Status:** **Draft — not effective until this file is included, at a specific version, in a named, tagged coordinated APP baseline.** Until that inclusion, no contributor is bound by this text and no reader may rely on it as a licensing statement.
**Purpose:** This file is the `Scope.md` companion required by the **Community Specification License 1.0** at §9.13. When effective, it defines the technical scope of the Agentic Process Protocol ("**APP**") for the purpose of bounding a Contributor's Necessary Claims under the licence.
**Effective:** on the first coordinated APP baseline tag that includes this file at a specific version, and thereafter as amended by pull request accepted under `csl/Governance.md` and Normative Suite Control. Iteration prior to that first baseline is drafting, not amendment.

> Under CSL 1.0 §9.13, **changes to Scope do not apply retroactively**. Every change to this file, once effective, is a scope-scoping change with intellectual-property consequences and is reviewed accordingly. Iteration prior to first effectiveness is unbounded; iteration after first effectiveness is a controlled Normative Suite Control operation.

---

## 1. What APP is

The **Agentic Process Protocol** is a governance protocol for enterprise business processes when AI is part of the execution path. It defines the specifications, artefacts, and conformance criteria under which a governed process can be audited across vendor boundaries, regardless of which vendor or AI platform contributes each step.

APP is a coordinated normative suite. This Scope.md governs the suite listed in §2. It does not extend to any document, product, service, or artefact outside that suite.

## 2. Specification documents within scope

The scope of APP for the purpose of CSL 1.0 §9.13 is the technical subject matter of the following documents at the versions and coordinated baselines identified in the repository's `MANIFEST.md`:

**Normative documents:**

- **APP-0** — Protocol Objectives
- **APP-1** — Protocol Constitution
- **APP-2** — Core Technical Specification
- **APP-3** — Security Architecture
- **APP-4** — Entity Correlation Architecture
- **APP-5** — Conformance Profiles

**Informative implementation guides:**

- **APP-IG-01** — Implementor's Guide
- **APP-IG-02** — Cross-Reference Matrix
- **APP-IG-03** — Worked Example
- **APP-IG-04** — Frequently Asked Questions
- **APP-IG-05** — Protocol Objectives Realisation and Assurance Guide

**Successor documents** adopted through the applicable repository governance process — the Normative Suite Control gate under `csl/Governance.md` during interim custody, or Working Group governance thereafter — and identified as part of the APP suite in a coordinated baseline are within scope from the coordinated baseline in which they are adopted.

## 3. Technical subject matter within scope

The following technical subject matter is within scope. Contributor Necessary Claims that read on this subject matter, to the extent required to implement conformant portions of the Specification, are subject to the CSL 1.0 patent licensing commitment (subject to §5 exclusions and to any Contributor Exclusion Notice under CSL 1.0 §3).

- **Governed process specifications.** The structured, AI-consumable representation of a business process — including process steps, deterministic/probabilistic classification per step, compliance obligations, human-oversight requirements, and the boundary between what a human authorises and what an AI system executes.

- **Execution records for governed processes.** The immutable end-to-end record of a governed process execution, including step-level classification outcomes, conformance status, mismatch categorisation, evidence provenance, and trust-boundary annotations. The Specification refers to this record as the *Process Execution Record*.

- **Integration-surface contracts between systems participating in governed process execution.** The schemas, event contracts, and governance-carrying attributes required for one system to hand off, or contribute to, a governed process step in a form that a second system can audit, **as expressly defined by numbered requirements in APP-2, APP-3, or APP-4 at the version identified in the baseline manifest**. Categories named here are illustrative; the specific requirement IDs each category covers are enumerated in the version of the Specification identified in the baseline manifest and controlling on scope questions.

- **MCP integration surface.** APP-2 specifies the A1 integration surface as Required Outcomes (CORE-A1-01 to A1-03, A1-05, A1-06) and names MCP as a Recommended Pattern transport (CORE-A1-04). APP-3 specifies the Required Outcome security floor for protocol-governed MCP endpoints (SEC-S2-01, referenced as the "MCP Conformance Profile" in APP-2's glossary). These are within scope of this file to the exact extent they are stated as **Required Outcomes** in the versions identified in the baseline manifest. Reference Mechanisms cited within them (specific TLS, OAuth, or DPoP versions) are covered by §4 below.

- **Entity correlation across systems participating in governed process execution.** The mechanisms by which entity references appearing in a governed process are tracked, correlated, and verified across systems, in both inferred and populated modes, to the extent APP-4 defines them.

- **Security requirements protecting governed processes.** Authentication, authorisation, integrity, evidence protection, and cross-system trust-boundary controls specified in APP-3 as Required Outcomes or Recommended Patterns with Required-Outcome floors, at the applicability defined in APP-5.

- **Conformance criteria and test procedures** as specified in APP-5, including role-based conformance profiles, per-integration-maturity-level applicability, and testable criteria for each Required Outcome within scope.

- **Governed change and improvement.** The mechanisms by which execution evidence feeds process improvement subject to human approval, as constrained by APP-1 Invariants and specified in APP-2 and APP-5.

## 4. Reference mechanisms within scope

APP-3 identifies specific mechanisms as **Reference Mechanisms** where cross-vendor interoperability requires convergence on a particular technical choice — for example, cryptographic algorithms whose selection must match across system boundaries. A Reference Mechanism is within scope of this file **only where it is expressly required, expressly designated, or expressly identified as a Reference Mechanism by numbered requirement in the version of APP-3 identified in the baseline manifest**. Mere mention, comparison, background discussion, or informative reference to a mechanism does not bring it within scope.

Substitute or alternative mechanisms that a Contributor may prefer, but which are not expressly required or designated as Reference Mechanisms in the Specification, are **not** brought into scope by their mention or comparison in the Specification.

## 5. Out of scope

The following are **out of scope** of APP. Contributor Necessary Claims that read only on out-of-scope subject matter are not subject to the CSL 1.0 patent licensing commitment for that subject matter, unless the Contributor has separately elected to include them.

### 5.1 Out of scope by constitutional non-goal

Per APP-1 §6, the following are non-goals of the Specification and are out of scope of this file:

- **Workflow engines.** How process steps are routed, scheduled, or executed by any specific engine. APP governs process execution; it does not orchestrate it.
- **Policy languages.** The syntax or interpretation of any regulatory-policy expression language. APP encodes compliance constraints as attributes on process specifications; it does not define, interpret, or adjudicate regulatory policy.
- **Model specifications.** The specification, alignment, evaluation, disposition, or behaviour of any AI model. APP governs how models participate in processes; it does not specify what a model does.
- **Enterprise system integration mechanics.** APP is not a replacement for enterprise system integration. The mechanics by which two systems connect, transport data, or expose functionality remain the concern of the systems and their vendors.

### 5.2 Out of scope by entity-correlation non-goal

Per APP-4 §1.5, the following are non-goals of APP-4 and are out of scope of this file:

- **Universal business ontology.** APP does not define or own a universal ontology of business entity types. Entity type labels are tenant-scoped.
- **Master Data Management replacement.** APP does not replace MDM. Where MDM exists, APP consumes its correlation keys.
- **Mandatory external semantic infrastructure.** APP does not require vendor knowledge graphs, active metadata platforms, or semantic interchange formats as prerequisites; where present, they may be used, but their internal specifications are not APP's subject matter.

### 5.3 Out of scope by design

The following are also out of scope of this file even where the Specification may discuss them illustratively:

- **Deployment patterns, vendor-specific integration details, and market positioning.** Per APP-1 §4, the Constitution never specifies these; illustrative material in informative documents (APP-IG series) does not bring vendor-specific implementations into scope.
- **Quality-of-service properties.** Performance, latency, availability, cost, and other quality-of-service properties of any implementation. These belong to platform service-level agreements.
- **User-interface designs, product names, brand marks, and commercial packaging** of any implementation.
- **Model-behaviour codes and frontier-lab safety frameworks.** APP composes with these at the layer boundary described in APP-IG-05 §3–4 but does not incorporate them into its subject matter.
- **Regulatory frameworks themselves.** APP maps to external laws, regulations, and standards (including but not limited to those referenced informatively in APP-0 Appendix C and APP-IG-05 §10) as technical crosswalks. Those crosswalks are informative technical mappings, not restatements. The named frameworks themselves — at any version, edition, or jurisdiction-specific implementation — are not APP's subject matter and are not brought into scope by their informative citation. Specific versions of external frameworks cited in the Specification are cited for their content at the date of the Specification's publication; subsequent versions are not automatically within scope.
- **Any subject matter identified as informative-only within the Specification**, including reference material that is expressly not intended to constrain implementation choices.

### 5.4 Out of scope by exclusion of source code

APP is a **specification**, not a source-code project. CSL 1.0 is not intended for source code. Any source code that accompanies APP in this repository (samples, schemas, reference designs, reference implementations, tooling) is licensed under **Apache-2.0** or a compatible source-code licence identified in `LICENSE`, and is not within the scope of this file for CSL 1.0 §9.13 purposes. Nothing in this section limits any Contributor's separate rights or licences with respect to accompanying source code.

## 6. Interaction with the Contribution Terms

This file is a companion to the **APP Contribution Terms**, which adopt CSL 1.0 verbatim as the operative Working Group licence. Where the Contribution Terms §3 identifies the Specification documents by ID, this file identifies the technical subject matter that those documents cover for scope purposes.

If there is any inconsistency between this file's identification of scope subject matter and the plain text of the Specification documents identified in §2, the plain text of those Specification documents controls for purposes of what the Specification actually says. This file constrains only the patent-licensing boundary; it does not alter the technical content of the Specification.

**The coordinated baseline manifest is authoritative on which files, at which versions, constitute the Specification.** No untagged draft, working copy, editor's branch, or repository file outside a tagged baseline extends this Scope. A file that appears in the repository but is not listed in the manifest of the effective baseline is not the Specification for the purpose of this Scope.

If there is any inconsistency between this file and CSL 1.0, **CSL 1.0 controls**, in accordance with APP Contribution Terms §2.

## 7. Change discipline

CSL 1.0 §9.13 provides that changes to Scope do not apply retroactively. In practice:

- **Every proposed change to this file is a pull request.** The change is labelled `scope-change` and is treated as a normative change under APP Contribution Terms and the repository's Normative Suite Control gate.
- **The pull request must include** (i) the specific text change, (ii) a rationale statement identifying what subject matter is being added to or removed from scope, and (iii) an assessment of downstream impact on Contributors who have accepted the current version.
- **Approval threshold** for a Scope.md change is the same as the applicable approval threshold for a normative change under `Governance.md`.
- **On acceptance**, the change is effective for Contributions made on or after the effective date recorded in this file's version history. Contributions made under a prior version of Scope.md remain governed by that prior version, per CSL 1.0 §9.13.

## 8. Version history

- **v0.3 — [Draft, September 2026]:** §3 MCP bullet corrected: APP-3 defines a security floor (SEC-S2-01), not a governance profile; A1 integration-surface requirements identified by ID. §5.4 adds reference designs to accompanying non-Specification material. Baseline references aligned to APP-2026-10-RC1.
- **v0.2 — [Draft, September 2026]:** Review incorporation. Explicit not-effective-until-baseline status statement added to header. §2 successor documents wording adjusted to reflect interim governance (no formal WG yet). §3 integration-surface language tied to numbered requirements in the manifest-identified version. §3 adds specific MCP Server Profile treatment. §4 tightened: Reference Mechanisms in scope only where expressly required or designated. §5.3 regulatory-framework references generalised with version-hygiene note. §6 adds manifest-as-authority clause. Iteration prior to first effectiveness clarified as drafting rather than amendment.
- **v0.1 — [Draft, September 2026]:** initial draft. Populated for the coordinated baseline APP-2026-10-RC1. Scope aligned with APP Contribution Terms v0.2 §3 and APP-1 v1.4 §6. Non-goals imported from APP-1 §6, APP-4 §1.5, APP-IG-05 §2.2. Reviewed for consistency with the Specification documents identified in §2 at the versions listed in `MANIFEST.md`.

---

*End of APP Scope v0.2.*
