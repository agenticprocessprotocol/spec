# APP Contribution Terms

**Version:** 0.3 Draft
**Effective:** 2026-10-07 (first coordinated baseline publication, APP-2026-10-RC1)
**Coordinated with:** APP-2026-10-RC1
**Baseline license:** Community Specification License 1.0 (SPDX identifier: `Community-Spec-1.0`), reproduced verbatim in Appendix A.

---


## Amendments from v0.2

**v0.3 (2026-10-07) — Activation.** v0.2 was published with Effective: TBD and was never commenced. v0.3 is identical to v0.2 in all substantive respects. The only change is that v0.3 sets the Effective date to **2026-10-07**, coinciding with the first coordinated baseline publication (APP-2026-10-RC1). From 2026-10-07 forward, contributions to the APP Working Group repository are governed by these terms.

The v0.2 text as frozen in `/releases/APP-2026-10-RC1/legal/APP_Contribution_Terms_v0_2.md` is retained as the historical record of what accompanied the first coordinated baseline at tag time. v0.3 is the live, operative version.

Structural review items pending Successor Foundation (AAIF) matriculation discussion are documented separately in `/legal/REVIEW-STATUS.md`.

---

## Preamble

These terms govern intellectual-property rights in contributions to the **Agentic Process Protocol** ("**APP**") specification suite. They adopt the Linux Foundation's **Community Specification License 1.0** ("**CSL 1.0**") verbatim as the operative Working Group license, with an APP-specific wrapper that scopes what "Specification" means, identifies the Interim Custodian, states the matriculation posture, and grants the public a Creative Commons Attribution 4.0 International licence to the published specification text.

Personal data received in the course of contribution is covered by the **APP Consultation Privacy Notice** at `/privacy` and the **APP Working Group Data Handling Charter** at `/charter`. Those documents govern personal data. This document governs the words, ideas, code, and IP rights in your contribution.

By making a contribution to APP, you accept these terms. If you contribute on behalf of an organisation, you confirm you are authorised to bind that organisation.

---

## 1. What this document does

- Adopts CSL 1.0 verbatim as the operative licence for contributions to APP (Appendix A).
- Provides the APP-specific scoping the CSL 1.0 refers to (definition of "Specification"; identification of companion files).
- Identifies the **Interim Custodian** (Vach AI Limited, DIFC) and the matriculation posture toward a **Successor Foundation**.
- Grants the public a **CC BY 4.0** licence to the published specification text.
- Adopts the **Developer Certificate of Origin 1.1** (Appendix B) as the sign-off mechanism for individual contributors.

## 2. Adoption of CSL 1.0

The Working Group adopts the **Community Specification License 1.0** (SPDX: `Community-Spec-1.0`) verbatim as its operative licence. The full text is reproduced in **Appendix A** and is the authoritative version for the purpose of these terms.

If any APP-specific wrapper term in §§1, 3–9 of this document appears to conflict with CSL 1.0 as it governs the rights actually granted, licensed, or reserved by a Contributor or Licensee, CSL 1.0 controls.

## 3. What "Specification" means for APP

The term "**Specification**" as used in CSL 1.0 §9.12 refers, for APP, to:

- **Normative documents:** APP-0 (Protocol Objectives), APP-1 (Protocol Constitution), APP-2 (Core Technical Specification), APP-3 (Security Architecture), APP-4 (Entity Correlation Architecture), APP-5 (Conformance Profiles).
- **Informative implementation guides:** APP-IG-01 (Implementor's Guide), APP-IG-02 (Cross-Reference Matrix), APP-IG-03 (Worked Example), APP-IG-04 (Frequently Asked Questions), APP-IG-05 (Protocol Objectives Realisation and Assurance Guide).
- **Successor documents** adopted by the Working Group as part of the APP specification suite.

Each document is identified in the Working Group repository with its version, its status (**Draft Specification** or **Approved Specification** under CSL 1.0 §§9.6, 9.2), and the coordinated baseline it belongs to (currently **APP-2026-10-RC1**).

## 4. Companion instruments required by CSL 1.0

CSL 1.0 refers to several companion files by convention. For APP, these are:

- **`Scope.md`** — Defines the technical scope of APP for the purpose of CSL 1.0 §9.13 (which bounds a Contributor's Necessary Claims). Published at the root of the Working Group repository.
- **`Governance.md`** — Defines the process by which a Draft Specification is designated an Approved Specification under CSL 1.0 §9.2. Published at the root of the Working Group repository.
- **`Notices.md`** — The mechanism by which Contributors and Implementers indicate acceptance of the Licence (CSL 1.0 §2.1.3.3), issue **Exclusion Notices** (CSL 1.0 §3), and provide notice of withdrawal (CSL 1.0 §2.3). Published at the root of the Working Group repository.

**Launch dependency.** These companion files must be present in the Working Group repository at the point at which these Contribution Terms are declared effective. CSL 1.0 is not fully operative for APP in the absence of `Scope.md`, `Governance.md`, and `Notices.md`.

## 5. How to accept these terms

CSL 1.0 §2.1.3 provides three mechanisms by which a Licensee accepts the Licence. For APP:

1. **CSL 1.0 §2.1.3.1 — Source Code Distributions.** For distribution of an Implementation in source code, include this Licence in the root directory of the source code with the Implementation.
2. **CSL 1.0 §2.1.3.2 — Non-Source Code Distributions.** For distribution of an Implementation in any form other than source code, include this Licence in the documentation, legal notices, notice in the software, and/or other written materials provided with the Implementation.
3. **CSL 1.0 §2.1.3.3 — Via Notices.md.** By issuing a pull request or commit to the Specification repository's `Notices.md` file by the Implementer's authorised representative, identifying the Implementer's name, authorised individual and system identifier, and Specification version.

**Individual Contributors** additionally accompany each contribution to the APP repository with a **Developer Certificate of Origin 1.1** sign-off, in the form `Signed-off-by: Random Developer <random@developer.example>` at the end of each commit message. The full text of the DCO 1.1 is at Appendix B.

**Consultation comments.** Submission of a comment via the APP consultation website (whether through the web form, GitHub Discussions, or GitHub Issues) is a **Contribution** under CSL 1.0 §9.3 and is subject to these terms.

## 6. Public copyright licence for the published Specification

The **published APP specification text**, as issued by the Working Group at each release baseline, is licensed to the public under the **Creative Commons Attribution 4.0 International Public License** ("**CC BY 4.0**"), available at <https://creativecommons.org/licenses/by/4.0/>.

This public copyright licence operates alongside — and does not narrow — the copyright licence Contributors grant to the Working Group under CSL 1.0 §1.1. Its purpose is to make the *published* specification text available for the public to read, quote, reproduce, and prepare derivative works, subject to the CC BY 4.0 attribution requirement.

**Implementations** of the Specification do not require attribution to the Working Group (CSL 1.0 §1.2). CC BY 4.0 attribution is required only for derivative works based on the Specification's *text* (for example, a translation, an excerpted quotation in a book, a redistribution of the specification document with modifications).

## 7. Interim custody and matriculation

**Vach AI Limited**, registered in the Dubai International Financial Centre (DIFC), acts as **Interim Custodian** of the Working Group repository, records, and infrastructure. Interim custody is not ownership; Vach hosts and coordinates the Working Group's work until the Working Group matriculates to an independent standards foundation (the "**Successor Foundation**").

The specific Successor Foundation is a Working Group decision; no matriculation agreement is in place at the effective date of these terms.

**Matriculation posture.** On matriculation to a Successor Foundation, these Contribution Terms will be replaced by the Successor Foundation's equivalent instruments; contributions made under these terms remain valid, with rights transferring intact.

CSL 1.0 §1.1 expressly acknowledges the Working Group's right to submit the Specification to another standards organisation. This matriculation posture is a scheduled application of that acknowledged right.

## 8. Governing law of the APP-specific wrapper terms

The APP-specific wrapper terms in §§1, 3–7, 9 of this document, and their interpretation as APP-specific commitments, are governed by the laws of the **DIFC**. This choice-of-law clause does not:

- alter the interpretation of CSL 1.0 itself, which is not tied to any single jurisdiction and applies uniformly to Contributors and Licensees globally;
- affect any mandatory consumer-protection rights a Contributor may have under the law of their habitual residence; or
- limit a party's rights and remedies under CSL 1.0.

## 9. Amendment

**APP-specific wrapper terms (this document, §§1, 3–8).** Amendments apply to future Contributions only, and do not narrow rights or non-assert commitments already granted. Amendments are published with an effective date and a version increment.

**CSL 1.0 itself (Appendix A).** The text of CSL 1.0 is a Joint Development Foundation instrument and is not amended by this document. If the Joint Development Foundation publishes an updated version of the Community Specification License, the Working Group may adopt it as an amendment to these terms by resolution, published in the repository's `Notices.md`.

**DCO 1.1 (Appendix B).** The DCO is a Linux Foundation instrument and is not amended by this document.

---

## Appendix A — Community Specification License 1.0 (verbatim)

*The text below is reproduced verbatim from the SPDX license listing at <https://spdx.org/licenses/Community-Spec-1.0.html>. The text of this Community Specification License is Copyright 2020 Joint Development Foundation and is licensed under the Creative Commons Attribution 4.0 International License available at <https://creativecommons.org/licenses/by/4.0/>. SPDX-License-Identifier: `CC-BY-4.0`.*

---

**Community Specification License 1.0**

**The Purpose of this License.** This License sets forth the terms under which 1) Contributor will participate in and contribute to the development of specifications, standards, best practices, guidelines, and other similar materials under this Working Group, and 2) how the materials developed under this License may be used. It is not intended for source code.

Capitalized terms are defined in the License's last section.

**1. Copyright.**

- **1.1. Copyright License.** Contributor grants everyone a non-sublicensable, perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as expressly stated in this License) copyright license, without any obligation for accounting, to reproduce, prepare derivative works of, publicly display, publicly perform, and distribute any materials it submits to the full extent of its copyright interest in those materials. Contributor also acknowledges that the Working Group may exercise copyright rights in the Specification, including the rights to submit the Specification to another standards organization.

- **1.2. Copyright Attribution.** As a condition, anyone exercising this copyright license must include attribution to the Working Group in any derivative work based on materials developed by the Working Group. That attribution must include, at minimum, the material's name, version number, and source from where the materials were retrieved. Attribution is not required for implementations of the Specification.

**2. Patents.**

- **2.1. Patent License.**

  - **2.1.1. As a Result of Contributions.**

    - **2.1.1.1. As a Result of Contributions to Draft Specifications.** Contributor grants Licensee a non-sublicensable, perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as expressly stated in this License) license to its Necessary Claims in 1) Contributor's Contributions and 2) to the Draft Specification that is within Scope as of the date of that Contribution, in both cases for Licensee's Implementation of the Draft Specification, except for those patent claims excluded by Contributor under Section 3.

    - **2.1.1.2. For Approved Specifications.** Contributor grants Licensee a non-sublicensable, perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as expressly stated in this License) license to its Necessary Claims included the Approved Specification that are within Scope for Licensee's Implementation of the Approved Specification, except for those patent claims excluded by Contributor under Section 3.

  - **2.1.2. Patent Grant from Licensee.** Licensee grants each other Licensee a non-sublicensable, perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as expressly stated in this License) license to its Necessary Claims for its Implementation, except for those patent claims excluded under Section 3.

  - **2.1.3. Licensee Acceptance.** The patent grants set forth in Section 2.1 extend only to Licensees that have indicated their agreement to this License as follows:

    - **2.1.3.1. Source Code Distributions.** For distribution in source code, by including this License in the root directory of the source code with the Implementation;

    - **2.1.3.2. Non-Source Code Distributions.** For distribution in any form other than source code, by including this License in the documentation, legal notices, via notice in the software, and/or other written materials provided with the Implementation; or

    - **2.1.3.3. Via Notices.md.** By issuing pull request or commit to the Specification's repository's Notices.md file by the Implementer's authorized representative, including the Implementer's name, authorized individual and system identifier, and Specification version.

  - **2.1.4. Defensive Termination.** If any Licensee files or maintains a claim in a court asserting that a Necessary Claim is infringed by an Implementation, any licenses granted under this License to the Licensee are immediately terminated unless 1) that claim is directly in response to a claim against Licensee regarding an Implementation, or 2) that claim was brought to enforce the terms of this License, including intervention in a third-party action by a Licensee.

  - **2.1.5. Additional Conditions.** This License is not an assurance (i) that any of Contributor's copyrights or issued patent claims cover an Implementation of the Specification or are enforceable or (ii) that an Implementation of the Specification would not infringe intellectual property rights of any third party.

- **2.2. Patent Licensing Commitment.** In addition to the rights granted in Section 2.1, Contributor agrees to grant everyone a no charge, royalty-free license on reasonable and non-discriminatory terms to Contributor's Necessary Claims that are within Scope for: 1) Implementations of a Draft Specification, where such license applies only to those Necessary Claims infringed by implementing Contributor's Contribution(s) included in that Draft Specification, and 2) Implementations of the Approved Specification. This patent licensing commitment does not apply to those claims subject to Contributor's Exclusion Notice under Section 3.

- **2.3. Effect of Withdrawal.** Contributor may withdraw from the Working Group by issuing a pull request or commit providing notice of withdrawal to the Working Group repository's Notices.md file. All of Contributor's existing commitments and obligations with respect to the Working Group up to the date of that withdrawal notice will remain in effect, but no new obligations will be incurred.

- **2.4. Binding Encumbrance.** This License is binding on any future owner, assignee, or party who has been given the right to enforce any Necessary Claims against third parties.

**3. Patent Exclusion.**

- **3.1. As a Result of Contributions.** Contributor may exclude Necessary Claims from its licensing commitments incurred under Section 2.1.1 by issuing an Exclusion Notice within 45 days of the date of that Contribution. Contributor may not issue an Exclusion Notice for any material that has been included in a Draft Deliverable for more than 45 days prior to the date of that Contribution.

- **3.2. As a Result of a Draft Specification Becoming an Approved Specification.** Prior to the adoption of a Draft Specification as an Approved Specification, Contributor may exclude Necessary Claims from its licensing commitments under this Agreement by issuing an Exclusion Notice. Contributor may not issue an Exclusion Notice for patents that were eligible to have been excluded pursuant to Section 3.1.

**4. Source Code License.** Any source code developed by the Working Group is solely subject the source code license included in the Working Group's repository for that code. If no source code license is included, the source code will be subject to the MIT License.

**5. No Other Rights.** Except as specifically set forth in this License, no other express or implied patent, trademark, copyright, or other rights are granted under this License, including by implication, waiver, or estoppel.

**6. Antitrust Compliance.** Contributor acknowledge that it may compete with other participants in various lines of business and that it is therefore imperative that they and their respective representatives act in a manner that does not violate any applicable antitrust laws and regulations. This License does not restrict any Contributor from engaging in similar specification development projects. Each Contributor may design, develop, manufacture, acquire or market competitive deliverables, products, and services, and conduct its business, in whatever way it chooses. No Contributor is obligated to announce or market any products or services. Without limiting the generality of the foregoing, the Contributors agree not to have any discussion relating to any product pricing, methods or channels of product distribution, division of markets, allocation of customers or any other topic that should not be discussed among competitors under the auspices of the Working Group.

**7. Non-Circumvention.** Contributor agrees that it will not intentionally take or willfully assist any third party to take any action for the purpose of circumventing any obligations under this License.

**8. Representations, Warranties and Disclaimers.**

- **8.1. Representations, Warranties and Disclaimers.** Contributor and Licensee represents and warrants that 1) it is legally entitled to grant the rights set forth in this License and 2) it will not intentionally include any third party materials in any Contribution unless those materials are available under terms that do not conflict with this License. IN ALL OTHER RESPECTS ITS CONTRIBUTIONS ARE PROVIDED "AS IS." The entire risk as to implementing or otherwise using the Contribution or the Specification is assumed by the implementer and user. Except as stated herein, CONTRIBUTOR AND LICENSEE EXPRESSLY DISCLAIM ANY WARRANTIES (EXPRESS, IMPLIED, OR OTHERWISE), INCLUDING IMPLIED WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR A PARTICULAR PURPOSE, CONDITIONS OF QUALITY, OR TITLE, RELATED TO THE CONTRIBUTION OR THE SPECIFICATION. IN NO EVENT WILL ANY PARTY BE LIABLE TO ANY OTHER PARTY FOR LOST PROFITS OR ANY FORM OF INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES OF ANY CHARACTER FROM ANY CAUSES OF ACTION OF ANY KIND WITH RESPECT TO THIS AGREEMENT, WHETHER BASED ON BREACH OF CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, AND WHETHER OR NOT THE OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. Any obligations regarding the transfer, successors in interest, or assignment of Necessary Claims will be satisfied if Contributor or Licensee notifies the transferee or assignee of any patent that it knows contains Necessary Claims or necessary claims under this License. Nothing in this License requires Contributor to undertake a patent search. If Contributor is 1) employed by or acting on behalf of an employer, 2) is making a Contribution under the direction or control of a third party, or 3) is making the Contribution as a consultant, contractor, or under another similar relationship with a third party, Contributor represents that they have been authorized by that party to enter into this License on its behalf.

- **8.2. Distribution Disclaimer.** Any distributions of technical information to third parties must include a notice materially similar to the following: "THESE MATERIALS ARE PROVIDED "AS IS." The Contributors and Licensees expressly disclaim any warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to the materials. The entire risk as to implementing or otherwise using the materials is assumed by the implementer and user. IN NO EVENT WILL THE CONTRIBUTORS OR LICENSEES BE LIABLE TO ANY OTHER PARTY FOR LOST PROFITS OR ANY FORM OF INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES OF ANY CHARACTER FROM ANY CAUSES OF ACTION OF ANY KIND WITH RESPECT TO THIS DELIVERABLE OR ITS GOVERNING AGREEMENT, WHETHER BASED ON BREACH OF CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, AND WHETHER OR NOT THE OTHER MEMBER HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."

**9. Definitions.**

- **9.1. Affiliate.** "Affiliate" means an entity that directly or indirectly Controls, is Controlled by, or is under common Control of that party.
- **9.2. Approved Specification.** "Approved Specification" means the final version and contents of any Draft Specification designated as an Approved Specification as set forth in the accompanying Governance.md file.
- **9.3. Contribution.** "Contribution" means any original work of authorship, including any modifications or additions to an existing work, that Contributor submits for inclusion in a Draft Specification, which is included in a Draft Specification or Approved Specification.
- **9.4. Contributor.** "Contributor" means any person or entity that has indicated its acceptance of the License 1) by making a Contribution to the Specification, or 2) by entering into the Community Specification Contributor License Agreement for the Specification. Contributor includes its Affiliates, assigns, agents, and successors in interest.
- **9.5. Control.** "Control" means direct or indirect control of more than 50% of the voting power to elect directors of that corporation, or for any other entity, the power to direct management of such entity.
- **9.6. Draft Specification.** "Draft Specification" means all versions of the material (except an Approved Specification) developed by this Working Group for the purpose of creating, commenting on, revising, updating, modifying, or adding to any document that is to be considered for inclusion in the Approved Specification.
- **9.7. Exclusion Notice.** "Exclusion Notice" means a written notice made by making a pull request or commit to the repository's Notices.md file that identifies patents that Contributor is excluding from its patent licensing commitments under this License. The Exclusion Notice for issued patents and published applications must include the Draft Specification's name, patent number(s) or title and application number(s), as the case may be, for each of the issued patent(s) or pending patent application(s) that the Contributor is excluding from the royalty-free licensing commitment set forth in this License. If an issued patent or pending patent application that may contain Necessary Claims is not set forth in the Exclusion Notice, those Necessary Claims shall continue to be subject to the licensing commitments under this License. The Exclusion Notice for unpublished patent applications must provide either: (i) the text of the filed application; or (ii) identification of the specific part(s) of the Draft Specification whose implementation makes the excluded claim a Necessary Claim. If (ii) is chosen, the effect of the exclusion will be limited to the identified part(s) of the Draft Specification.
- **9.8. Implementation.** "Implementation" means making, using, selling, offering for sale, importing or distributing any implementation of the Specification 1) only to the extent it implements the Specification and 2) so long as all required portions of the Specification are implemented.
- **9.9. License.** "License" means this Community Specification License.
- **9.10. Licensee.** "Licensee" means any person or entity that has indicated its acceptance of the License as set forth in Section 2.1.3. Licensee includes its Affiliates, assigns, agents, and successors in interest.
- **9.11. Necessary Claims.** "Necessary Claims" are those patent claims, if any, that a party owns or controls, including those claims later acquired, that are necessary to implement the required portions (including the required elements of optional portions) of the Specification that are described in detail and not merely referenced in the Specification.
- **9.12. Specification.** "Specification" means a Draft Specification or Approved Specification included in the Working Group's repository subject to this License, and the version of the Specification implemented by the Licensee.
- **9.13. Scope.** "Scope" has the meaning as set forth in the accompanying Scope.md file included in this Specification's repository. Changes to Scope do not apply retroactively. If no Scope is provided, each Contributor's Necessary Claims are limited to that Contributor's Contributions.
- **9.14. Working Group.** "Working Group" means this project to develop specifications, standards, best practices, guidelines, and other similar materials under this License.

*The text of this Community Specification License is Copyright 2020 Joint Development Foundation and is licensed under the Creative Commons Attribution 4.0 International License available at <https://creativecommons.org/licenses/by/4.0/>.*

*SPDX-License-Identifier: `CC-BY-4.0`*

---

## Appendix B — Developer Certificate of Origin 1.1 (verbatim)

*The text below is reproduced verbatim from <https://developercertificate.org/>.*

---

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

---

---

## Document status

**Status:** Draft for public consultation
**Version:** 0.2
**Effective date:** [TBD — publication conditional on `Scope.md`, `Governance.md`, and `Notices.md` being present in the Working Group repository per §4 launch dependency]
**Related suite release:** APP-2026-10-RC1
**Change record:** Maintained in the public release repository.

---

*End of APP Contribution Terms v0.3.*
