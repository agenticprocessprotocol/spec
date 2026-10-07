# APP-2026-10-RC1 — Baseline Manifest

**Coordinated baseline:** APP-2026-10-RC1
**Date:** 2026-10-07
**Status:** Draft Specification under CSL 1.0 §9.6. Not yet an Approved Specification.
**Specification licence:** Community Specification License 1.0 (SPDX: `Community-Spec-1.0`), reproduced verbatim at repository root `LICENSE`.
**Informative content licence:** CC-BY-4.0 (Guides, FAQs, informative annexes).
**Accompanying source/schema licence:** Apache-2.0 (schemas, reference designs).

This manifest is the authoritative inventory for this baseline. The machine-readable equivalent is `manifest.json` in this directory, with identical content and per-file SHA-256 hashes. Where this file and `manifest.json` disagree, `manifest.json` controls.

## Canonical citation format

> `APP-<n> <Document title> v<version>, coordinated baseline APP-2026-10-RC1, §<section>, tag APP-2026-10-RC1, manifest SHA-256 <file-hash>`

Example: `APP-3 Security Architecture v3.13, APP-2026-10-RC1, §S13, tag APP-2026-10-RC1, manifest SHA-256 e63db4e8619e1563f1e2b4dc7913febdab7d6aa40633b4ddcfe319e8aad48fd3`

A citation of the GitHub Release URL is not itself a durable citation unit for long-form documents.

## Specification (eleven documents)

The eleven documents listed below collectively constitute the Agentic Process Protocol **Specification** for this baseline. APP-0 to APP-5 are **normative**; APP-IG-01 to APP-IG-05 are **informative** but are part of the Specification per APP-1 §4.

| ID        | Title                                               | Version | Status                     | Normative status | Path                                                         | SHA-256 (first 16) |
| :-------- | :-------------------------------------------------- | :------ | :------------------------- | :--------------- | :----------------------------------------------------------- | :----------------- |
| APP-0     | Protocol Objectives                                 | 0.14    | Draft                      | Normative        | `spec/APP-0_Protocol_Objectives_v0_14_Draft.md`              | `70237317c8bd4126` |
| APP-1     | Protocol Constitution                               | 1.5     | Draft                      | Normative        | `spec/APP-1_Protocol_Constitution_v1_5_Draft.md`             | `08e92965d7ff435f` |
| APP-2     | Core Technical Specification                        | 5.13    | Draft                      | Normative        | `spec/APP-2_Core_Technical_Specification_v5_13_Draft.md`     | `555a3a68b948211c` |
| APP-3     | Security Architecture                               | 3.13    | Draft                      | Normative        | `spec/APP-3_Security_Architecture_v3_13_Draft.md`            | `e63db4e8619e1563` |
| APP-4     | Entity Correlation Architecture                     | 2.3     | Draft                      | Normative        | `spec/APP-4_Entity_Correlation_Architecture_v2_3_Draft.md`   | `d69a78235ebac300` |
| APP-5     | Conformance Profiles                                | 1.10    | Draft                      | Normative        | `spec/APP-5_Conformance_Profiles_v1_10_Draft.md`             | `978639bc3407331e` |
| APP-IG-01 | Implementor's Guide                                 | 1.11    | Draft                      | Informative      | `spec/APP-IG-01_Implementors_Guide_v1_11_Draft.md`           | `537351bfd919d59b` |
| APP-IG-02 | Cross-Reference Matrix                              | 1.15    | Draft                      | Informative      | `spec/APP-IG-02_Cross_Reference_Matrix_v1_15_Draft.md`       | `1929cd4799fa9a53` |
| APP-IG-03 | Worked Example                                      | 1.11    | Draft                      | Informative      | `spec/APP-IG-03_Worked_Example_v1_11_Draft.md`               | `bd2721a001fcd00f` |
| APP-IG-04 | Frequently Asked Questions                          | 0.6     | Draft for Ecosystem Review | Informative      | `spec/APP-IG-04_Frequently_Asked_Questions_v0_6_Draft.md`    | `fd704e35837abbef` |
| APP-IG-05 | Protocol Objectives Realisation and Assurance Guide | 0.12    | Draft                      | Informative      | `spec/APP-IG-05_Protocol_Objectives_Realisation_and_Assurance_Guide_v0_12_Draft.md` | `1613bc6a321c9cfb` |

Full SHA-256 hashes are in `manifest.json`.

## Plain Language Guides (informative companions, outside the Specification)

Plain Language Guides translate the Specification for non-technical readers. They are informative, versioned independently, and **not part of the Specification**. The current baseline publishes four of a planned seven; APP-0, APP-1 and APP-5 Plain Language Guides are tracked as open items in `KNOWN_ISSUES.md`.

| ID        | Title                                     | Version | Status | Path                                        | SHA-256 (first 16) |
| :-------- | :---------------------------------------- | :------ | :----- | :------------------------------------------ | :----------------- |
| PLG       | APP Plain Language Guide (suite overview) | 0.1     | Draft  | `guides/APP_Plain_Language_Guide_v0_1.md`   | `58c567c4971a8e0b` |
| APP-2-PLG | APP-2 Plain Language Guide                | 0.2     | Draft  | `guides/APP-2_Plain_Language_Guide_v0_2.md` | `89daabc87b77ecd7` |
| APP-3-PLG | APP-3 Plain Language Guide                | 0.2     | Draft  | `guides/APP-3_Plain_Language_Guide_v0_2.md` | `8d52cba51d11d0f2` |
| APP-4-PLG | APP-4 Plain Language Guide                | 0.2     | Draft  | `guides/APP-4_Plain_Language_Guide_v0_2.md` | `dc4d1fa4d55d21dc` |

## Legal instruments

| ID                 | Title                                   | Version | Status | Path                                            | SHA-256 (first 16) |
| :----------------- | :-------------------------------------- | :------ | :----- | :---------------------------------------------- | :----------------- |
| Contribution Terms | APP Contribution Terms                  | 0.2     | Draft  | `legal/APP_Contribution_Terms_v0_2.md`          | `259a541f5e4fa1de` |
| Charter            | APP Working Group Data Handling Charter | 0.3     | Draft  | `legal/APP_WG_Data_Handling_Charter_v0_3.md`    | `bc510ed0e12417c3` |
| Privacy Notice     | APP Consultation Privacy Notice         | 0.3     | Draft  | `legal/APP_Consultation_Privacy_Notice_v0_3.md` | `17e6daa6dfa5fe4a` |

The Contribution Terms adopt the Community Specification License 1.0 verbatim; the Charter is the Article 26 joint-controller instrument between the Interim Custodian and WG Members; the Privacy Notice governs personal data received through the consultation.

## CSL 1.0 companion (frozen for this baseline)

The CSL 1.0 §9.13 Scope companion is frozen for this baseline. Changes to Scope do not apply retroactively under CSL 1.0 §9.13; implementers of this baseline are bound only by the Scope.md captured here.

| ID    | Title                               | Version | Status                                    | Path           | SHA-256 (first 16) |
| :---- | :---------------------------------- | :------ | :---------------------------------------- | :------------- | :----------------- |
| Scope | APP Scope (CSL 1.0 §9.13 companion) | 0.3     | Draft; effective on inclusion in this tag | `csl/Scope.md` | `919c67b359e23616` |

The live Scope.md at `/csl/Scope.md` on main may be updated for future baselines. Governance.md and Notices.md are not frozen into the baseline directory; they remain at `/csl/` on main. For a point-in-time view of Notices.md at tag, consult the Git tag `APP-2026-10-RC1`.

## Accompanying artefacts (informative, not part of the Specification)

Accompanying artefacts are versioned independently of the coordinated baseline. They are informative. Implementations may deliver equivalent conformance via other realisations.

| ID     | Title                         | Version | Status                       | Type                | Path                                              | SHA-256 (first 16) |
| :----- | :---------------------------- | :------ | :--------------------------- | :------------------ | :------------------------------------------------ | :----------------- |
| APP-R1 | Process Frame Schema          | 0.3.0   | Illustrative Reference       | JSON Schema 2020-12 | `schemas/frame/0.3.0/frame.schema.json`           | `9285b898fd12b720` |
| APP-R1 | Process Frame Schema Notes    | 0.3.0   | Illustrative Reference       | Informative notes   | `schemas/frame/0.3.0/NOTES.md`                    | `cce0908f7728a4ca` |
| APP-R1 | Process Frame Example (valid) | 0.3.0   | Illustrative Reference       | Example             | `schemas/frame/0.3.0/examples/frame.example.json` | `56a18407e4bec713` |
| APP-R2 | MCP Binding Reference Design  | 0.3     | Illustrative Reference Draft | Reference design    | `reference/mcp-server/DESIGN.md`                  | `5da2691733f31dc9` |

APP-R1 and APP-R2 are the first two artefacts under the **APP-R Illustrative Reference tier** recognised in APP-1 v1.5 §4. The three-tier APP corpus is:

- **Normative:** APP-0 to APP-5
- **Informative Specification:** APP-IG-01 to APP-IG-05 (part of the Specification per APP-1 §4)
- **Illustrative Reference:** APP-R1, APP-R2 (not part of the Specification)

Future accompanying artefacts (schemas at higher versions, additional reference designs) will accrete at their canonical paths and be listed in subsequent baseline manifests at the version in effect at that baseline tag.

## Integrity verification

To verify this baseline from a clean checkout:

```bash
git checkout APP-2026-10-RC1
cd releases/APP-2026-10-RC1
sha256sum -c <(python3 -c "
import json
m = json.load(open('manifest.json'))
for section in ('specification','guides','legal','csl_companions','accompanying_artefacts'):
    for f in m[section]:
        print(f\"{f['sha256']}  {f['path']}\")
")
```

Every line should report `OK`. A failure means the frozen content has been tampered with or the manifest has drifted; neither should ever be true for a tagged baseline.
