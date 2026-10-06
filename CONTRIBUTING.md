# Contributing to APP

Thank you for your interest in the Agentic Process Protocol. This file explains **where to send what**, how contributions are licensed, and how we track authorship.

If anything here is unclear, open a **Discussion** rather than guessing.

---

## 1. Where to send what — decision tree

| What you have | Where it goes |
|---|---|
| A **question** about how something works | **GitHub Discussions** → *Getting Started & Questions* |
| A **suspected documentation defect** (ambiguity, inconsistency, factual error) | **GitHub Issue** → *Documentation defect* form |
| A **clarification request** (the text may be correct but is hard to read) | **GitHub Issue** → *Clarification* form |
| A **substantive change proposal** (new requirement, changed obligation, new conformance criterion) | **GitHub Issue** → *Normative proposal* form (not a PR) |
| An **implementation report** (what worked, what didn't, where the spec was unclear) | **GitHub Issue** → *Implementation experience* form |
| A **suspected security defect** | **Private vulnerability report** via the Security tab, **not** a public Issue — see [`SECURITY.md`](SECURITY.md) |
| A **personal-data concern** or a request about data we hold | `privacy@agenticprocess.org` — see the [Consultation Privacy Notice](https://agenticprocess.org/privacy) |
| A **Code of Conduct report** | `conduct@agenticprocess.org` — see [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) |

**Normative changes do not begin as pull requests.** They begin as a *Normative proposal* issue. The editors convert accepted proposals into pull requests after discussion. This exists so the discussion of *what* to change is separate from the discussion of *how* to word the change.

**Editorial changes** (typos, formatting, cross-reference target fixes that do not change meaning) may be submitted directly as a pull request. The PR template asks you to classify the change; if you are unsure, use the issue path first.

---

## 2. Licensing of contributions

By making a contribution to this repository, you accept the **APP Contribution Terms**, which adopt the **Community Specification License 1.0** (SPDX: `Community-Spec-1.0`) verbatim as the operative Working Group licence. See [`LICENSE`](LICENSE) for the full text.

Key points, in plain language:

- Your contribution grants a copyright licence allowing the Working Group to publish and distribute the Specification, and allowing anyone to implement it.
- Where your contribution brings in patent claims that are *necessary to implement* the Specification within the scope defined by `csl/Scope.md`, you grant a royalty-free patent licence to Licensees who have accepted the licence per CSL 1.0 §2.1.3.
- You may exclude specific patent claims by filing an **Exclusion Notice** per CSL 1.0 §3, within 45 days of your contribution. See `csl/Notices.md`.
- Accompanying source code, schemas, and tooling under `/schemas/`, `/reference/`, and `/tools/` are licensed under **Apache License 2.0** — not CSL 1.0.

If you contribute on behalf of an organisation, you confirm you are authorised to bind that organisation.

---

## 3. Developer Certificate of Origin (DCO) sign-off

**Every commit must carry a `Signed-off-by:` trailer.** This is how you confirm you have the right to submit the contribution under the applicable licence, per the Developer Certificate of Origin 1.1 ([text here](https://developercertificate.org/)).

### 3.1 Preferred (command line)

```bash
git commit --signoff -m "Your commit message"
# or on an existing commit:
git commit --amend --signoff
```

This adds a line like:

```
Signed-off-by: Your Name <your.email@example.com>
```

Use a name you are prepared to be publicly associated with. The email must be real.

### 3.2 Alternative (GitHub web UI)

If you are editing a file through the GitHub web UI:

1. Make your edit and scroll to the **Commit changes** panel.
2. In the extended description field (below the commit message), add on its own line:
   ```
   Signed-off-by: Your Name <your.email@example.com>
   ```
3. Commit.

### 3.3 If you can't sign off

If you cannot complete DCO sign-off for a reason specific to your situation, your idea is still welcome. Open a **Discussion** or an **Issue** describing what you'd like to see changed and why. An editor may author an independent implementation of your idea. In that case:

- The editor's DCO sign-off applies to the editor's own contribution. It does not substitute for your sign-off; the editor is not representing that you signed off.
- You are credited by name in the PR description and in `CHANGELOG.md` for raising the idea.
- This preserves both your contribution to the discussion and the legal integrity of the DCO chain.

This path is for situations where sign-off is impractical; it is not a general route to avoid DCO.

---

## 4. AI-authorship disclosure

APP contributions may be developed with AI assistance. The project cares about accuracy, licensing, and attribution — not about writing style.

**You must disclose material AI assistance** where an AI system generated substantive proposed normative wording, rationale, technical analysis, or test content that you have not independently reviewed and validated.

You do **not** need to disclose:

- Ordinary use of grammar checkers, code-completion tools, or translation software.
- AI assistance limited to style, structure, or formatting of your own analysis.
- Use of an AI as a research tool to find or summarise material you then independently verify.

The project does not attempt to infer AI use from writing style, tone, grammar, or completeness of prose. The test is whether substantive content was generated by an AI and whether you have reviewed it.

**You remain responsible** for the accuracy, originality, licensing status, and authority of every submission you make, regardless of how it was produced. Unverified, unlicensed, inaccurate, or non-attributable content is a defect regardless of authorship source.

The disclosure field is in every Issue Form and PR template.

---

## 5. Pull request process

### 5.1 What the PR template asks for

- **Change classification:** editorial, normative, schema, release, scope-change, or other.
- **Linked issue:** for normative, scope, or schema changes, the originating issue (and, for normative changes, the change-impact manifest at `/changes/APP-XXXX.md`).
- **Change-impact manifest link:** for normative changes, a path to the completed manifest.
- **DCO:** confirmation that all commits are signed off.
- **AI-authorship disclosure:** as described in §4.
- **Personal-data acknowledgement:** that your contribution does not include personal data of third parties, sensitive personal data, off-platform-collected personal data, or anything else listed under *Never-in-repo* in [`SECURITY.md`](SECURITY.md).
- **Release Approver sign-off** (for release / scope / legal / normative PRs only): completed by the Release Approver before merge.

### 5.2 Required checks

Every PR must pass:

- **DCO check** — all commits signed off.
- **`validate-spec`** — manifest, legacy-name, keyword, and cross-reference validators.
- **`validate-schemas`** (for schema-touching PRs) — schema validation against the published meta-schema plus `examples/` and `examples/invalid/`.
- **`links`** — all internal and external links resolve.
- **`release-integrity`** (for release PRs) — manifest and release-notes integrity, including the Release Approver sign-off template field.

Failing checks block merge. The Custodian helps you diagnose, but does not merge.

### 5.3 Reviewers

GitHub automatically requests review from the owners of the paths your PR touches, per [`.github/CODEOWNERS`](.github/CODEOWNERS). The code-owner review is required by branch protection.

### 5.4 Normative changes — the extra discipline

If your change is normative (modifies a requirement, an RFC 2119/8174 keyword, a conformance obligation, a schema identified as part of the Specification, a protocol invariant, or an interpretation that affects implementation or conformance), the PR must include a completed **change-impact manifest** at `/changes/APP-XXXX.md`. The manifest format is defined in APP-1 §4 and templated at `/changes/_TEMPLATE.md`. It covers:

- Changed requirement IDs with a semantic delta statement for each.
- Affected normative and informative documents.
- Cross-reference updates (reciprocal citations).
- APP-5 applicability and test impact.
- Traceability impact (APP-IG-02 §7).
- Migration and version-negotiation impact.
- Updated suite manifest and release notes where the PR is baseline-bound.

The Custodian will not prepare the merge until (i) the manifest is present and complete, (ii) all automated checks pass, and (iii) the applicable approval threshold is met.

---

## 6. Governance and matriculation posture

- Decision authority currently rests with the **Release Approver**. See [`GOVERNANCE.md`](GOVERNANCE.md).
- The Working Group formation trigger — the conditions under which decision authority transfers from the Release Approver to a quorum of maintainers — is listed in `GOVERNANCE.md` §5.
- The interim custodian is **Vach AI Limited**. The intended beneficiary is a to-be-designated Successor Foundation. See the [Working Group Data Handling Charter](https://agenticprocess.org/charter).

---

## 7. Changes to this file

Material changes to `CONTRIBUTING.md` require a PR. Clerical corrections (typos, broken-link fixes) may be submitted directly; substantive policy changes should first be opened as a Discussion to invite input.

---

*Questions? Open a Discussion in **Getting Started & Questions**. Thank you for contributing.*
