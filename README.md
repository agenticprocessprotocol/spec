# Agentic Process Protocol (APP)

A governance protocol for enterprise business processes when AI is part of the execution path. APP defines the specifications, artefacts, and conformance criteria under which a governed process can be audited across vendor boundaries, regardless of which vendor or AI platform contributes each step.

This repository is the public home of the APP specification suite. It is maintained under the interim custody of **Vach AI Limited** (DIFC), pending matriculation to a Successor Foundation. See [`GOVERNANCE.md`](GOVERNANCE.md) and the [Working Group Data Handling Charter](https://agenticprocess.org/charter) for the custody and governance posture.

---

## Current state

The repository is in **public consultation**. The coordinated baseline is being prepared; **no coordinated APP baseline has been tagged yet**. Until the first baseline is tagged, documents in `/drafts/` are not citable as the Specification.

- Current baseline tag: *(none — pending Work Package 3)*
- Target first baseline: **APP-2026-10-RC1**
- Document count: 11 (6 normative + 5 informative guides) — see `/csl/Scope.md` §2

Once the baseline is tagged, the authoritative source will be the files under `/releases/APP-2026-10-RC1/` and the corresponding GitHub Release. Draft files under `/drafts/` are editing surfaces; they are not citable.

---

## Where to look

| If you want to… | Go to |
|---|---|
| **Cite the Specification** | `/releases/<baseline-id>/` (immutable) + the GitHub Release page for that tag |
| **Read the current draft** | `/drafts/spec/` and `/drafts/guides/` (editing surfaces; not citable) |
| **Understand the licensing** | [`LICENSE`](LICENSE) + [`csl/Scope.md`](csl/Scope.md) + [`csl/Governance.md`](csl/Governance.md) + [`csl/Notices.md`](csl/Notices.md) |
| **Contribute** | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| **Report a vulnerability** | [`SECURITY.md`](SECURITY.md) — **not** a GitHub Issue |
| **Follow governance** | [`GOVERNANCE.md`](GOVERNANCE.md) + the Charter |
| **Ask a question** | GitHub Discussions |
| **Report a documentation defect** | GitHub Issues (`documentation-defect` form) |
| **Propose a normative change** | GitHub Issues (`normative-proposal` form) |

---

## Canonical citation format

The authoritative citation unit for an APP document is the baseline-tagged file hash, not a GitHub Release UI URL. Cite as:

> `APP-<n> <Document title> v<version>, coordinated baseline <baseline-id>, §<section>, tag <baseline-id>, manifest SHA-256 <hash>`

Example:

> `APP-3 Security Architecture v3.13, APP-2026-10-RC1, §S13, tag APP-2026-10-RC1, manifest SHA-256 a1b2c3…`

The `manifest SHA-256` is the hash of that file as recorded in `/releases/<baseline-id>/manifest.json`. The GitHub Release URL is a convenience pointer; the tag + manifest hash are the durable citation.

---

## Licence

- **Specification text** (normative documents and informative guides): licensed to Contributors under the **Community Specification License 1.0** ([SPDX: Community-Spec-1.0](https://spdx.org/licenses/Community-Spec-1.0.html)); made available to the public additionally under the **Creative Commons Attribution 4.0 International Licence** (CC BY 4.0).
- **Accompanying code, schemas, reference designs, and tooling** (`/schemas/**`, `/reference/**`, `/tools/**`): **Apache License 2.0**. See `LICENSE` in each directory.
- **CSL 1.0 companion files** (`csl/Scope.md`, `csl/Governance.md`, `csl/Notices.md`) are required under CSL 1.0 §9.13 and §9.2. Changes to `csl/Scope.md` have intellectual-property consequences; see that file's §7 for the change discipline.

See [`LICENSE`](LICENSE) for the full CSL 1.0 text and the mapping of accompanying licences.

---

## Interim custody and matriculation

The Interim Custodian is **Vach AI Limited** (DIFC, Dubai). Interim custody is **not ownership**. The intended beneficiary of the Working Group's records and infrastructure is a not-for-profit standards foundation to be designated by resolution of the Working Group (the **Successor Foundation**).

Personal data received through consultation is governed by the [Consultation Privacy Notice](https://agenticprocess.org/privacy) and the [Working Group Data Handling Charter](https://agenticprocess.org/charter). Those documents govern personal data; the files in this repository govern intellectual-property rights in contributions.

On matriculation, custody of the repository, tags, releases, and governance records will transfer to the Successor Foundation. The governance posture is maintained to make that transfer a file transfer, not an archaeology exercise.

---

## Governance posture (interim)

- **Decision authority** for normative changes rests with the Release Approver pending Working Group formation. Normative changes require a completed change-impact manifest and dual sign-off (one Editor approval + Release Approver sign-off) per `GOVERNANCE.md`.
- **Co-maintainer** co-reviews pull requests to `main`. GitHub's "approval other than last pusher" rule means at least two accountable individuals touch every change.
- **Ruleset activation blocked pending co-maintainer confirmation.** Until the co-maintainer is confirmed in the editors team with 2FA, branch-protection enforcement operates in a reduced mode; see `GOVERNANCE.md` §4.
- **Working Group formation trigger** is defined in `GOVERNANCE.md`. Until all five conditions are met, interim rules apply.

---

## Security and privacy

- **Vulnerability reports** go through GitHub's private vulnerability reporting first; `security@agenticprocess.org` is the backup channel. **Do not open a public issue for a suspected security defect.** See [`SECURITY.md`](SECURITY.md).
- **Privacy inquiries** go to `privacy@agenticprocess.org`. The Consultation Privacy Notice is at `https://agenticprocess.org/privacy`.
- **Code of Conduct violations** go to `conduct@agenticprocess.org`. See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

---

## Accompanying artefacts (informative, outside the Specification)

The following live in this repository but are **not** part of the coordinated Specification. They are versioned independently and never copied into `/releases/<baseline-id>/spec/`.

- `/schemas/` — JSON Schema definitions (e.g., Process Frame schema).
- `/reference/` — reference designs (e.g., APP-RD-01 MCP Binding Reference Design).
- `/tools/` — validation harnesses and test tooling.

Each release manifest lists these in a separate "Accompanying artefacts" section with path, version and SHA-256.

---

## About

- Website: <https://agenticprocess.org>
- Discussion: GitHub Discussions on this repository
- Mail: contact details in the policy files above

*This README is maintained by the Release Approver. Changes to this file follow the pull-request process in `CONTRIBUTING.md`.*
