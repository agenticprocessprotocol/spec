# APP Governance

This file describes **how decisions are made** in the Agentic Process Protocol repository during the **interim custody** period. It is a public, community-facing document — not a legal instrument. The binding legal instruments are the [Contribution Terms](https://agenticprocess.org/contribute) (adopting CSL 1.0 verbatim) and the [Working Group Data Handling Charter](https://agenticprocess.org/charter).

For the CSL 1.0 §9.2 *Draft Specification → Approved Specification* process, see [`csl/Governance.md`](csl/Governance.md). That file is kept separately because CSL 1.0 refers to it by name.

---

## 1. Roles

### Release Approver

A **named individual** who is accountable for decisions on normative changes, releases, and governance records. During interim custody the Release Approver is **Vaidhya** (Vach AI Limited). The Release Approver may not be anonymous and may not be a shared account.

The Release Approver:

- Signs off on normative, release, scope, and legal pull requests via the sign-off template in the PR body.
- Approves the publication clearance of accompanying artefacts (schemas, reference designs).
- Owns tag creation, release publication, and ruleset configuration.
- Decides escalations arising from the Custodian's escalation matrix.
- Does not interpret legal questions unilaterally; those go to counsel.

### Co-maintainer

At least **one additional named maintainer with write access and reviewer capability** in the `@agenticprocessprotocol/editors` team. The co-maintainer's role is to provide the second accountable review on PRs, satisfying GitHub's rule that an approval be from someone other than the last pusher. The co-maintainer during interim custody is **Bhavna Krishnan** (Vach AI Limited).

### Editors

Members of `@agenticprocessprotocol/editors` who edit specification drafts and informative guides. The Release Approver and the co-maintainer are editors by default.

### Custodian

The operational role responsible for repository mechanics — command preparation, PR drafting, validator and workflow upkeep, dashboards. The Custodian **prepares and explains** but does not approve. Custodian operations may be delegated to a technical team member or to a scoped Claude Code session.

### Working Group members (future)

At Working Group formation, decision authority transfers from the Release Approver to the Working Group. The transition conditions are listed in §5.

---

## 2. How decisions are made

### 2.1 Discussions → Issues → Pull Requests

The flow for any proposed change:

1. **Open a Discussion** if you have a question or want to explore an idea. Discussions are the natural home for exploratory thinking.
2. **Open an Issue** using the appropriate [Issue Form](.github/ISSUE_TEMPLATE/) once you have a specific defect to report or a specific change to propose.
3. **An editor opens a Pull Request** when a proposal has been discussed sufficiently to be worth implementing. Normative proposals do **not** begin as pull requests.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full decision tree.

### 2.2 Approval thresholds (interim)

Every pull request to `main` requires:

- **One approving review from a person other than the last pusher** (enforced by GitHub ruleset).
- **CODEOWNER review** for the paths the PR touches (enforced by [`.github/CODEOWNERS`](.github/CODEOWNERS) and the ruleset).

**Additionally**, PRs of the following classes require **explicit Release Approver sign-off** recorded in the PR body (sign-off template provided in the PR template, verified by the `release-integrity` check):

- **Release PRs** — any change under `/releases/APP-YYYY-MM-RCn/`.
- **Scope changes** — any change to `csl/Scope.md`, `csl/Governance.md`, `csl/Notices.md`.
- **Legal changes** — any change under `/legal/**`.
- **Schema or reference-design changes** — any change under `/schemas/**` or `/reference/**`.
- **Normative changes** — any change that modifies a requirement, an RFC 2119/8174 keyword, a conformance obligation, a schema identified as part of the Specification, a protocol invariant, a security outcome, or an interpretation affecting implementation or conformance.

Where the Release Approver is also an editor (which is normal at interim), the Release Approver's **Editor approval** (a GitHub review approval) and the **Release Approver sign-off** (a completed template field) are **two distinct governance acts** and are recorded separately in the PR. Both are required.

### 2.3 Normative Suite Control gate

Normative changes must pass through the Normative Suite Control gate before merge:

1. A completed **change-impact manifest** is present at `/changes/APP-XXXX.md`, covering all nine fields required by APP-1 §4 (requirement ID deltas, affected documents, cross-reference updates, APP-5 applicability impact, traceability impact, test impact, migration impact, suite baseline regeneration).
2. All automated checks pass: `validate-spec` (manifest, legacy-name, keyword, cross-reference), `links`, `release-integrity`, DCO.
3. The approval threshold in §2.2 is met: Editor approval + CODEOWNER review + Release Approver sign-off.

Only then will the Custodian prepare the merge. The Release Approver clicks Merge.

### 2.4 Schema-change path

Pull requests modifying `/schemas/**` are labelled `schema-change`. Each such PR must:

- Create a **new version directory** (published version directories are immutable).
- Follow the evolution rule — minor version adds optional fields only; any new required field or changed enum requires a major version bump.
- Update `examples/` (valid) and `examples/invalid/` (must fail validation) in the same PR.
- Pass `validate-schemas`.
- Carry Release Approver sign-off and a publication-clearance record in `/decisions/`.

If the Working Group adopts a schema into the Specification, it migrates to the normative path above.

---

## 3. What the Custodian does and does not do

The Custodian **prepares, validates, and explains**:

- Writes PR descriptions and review comments for the Release Approver to post.
- Runs validators and reports results.
- Maintains the Operations Registry and the Decisions log.
- Produces the Custodian Dashboard at each session open.
- Flags escalations.

The Custodian **does not**:

- Merge pull requests.
- Close discussions, issues, or PRs.
- Delete branches, tags, releases, or files.
- Publish releases or tag baselines.
- Change branch-protection rules or rulesets.
- Invite, remove, or change permissions of collaborators or teams.
- Install, remove, or reconfigure GitHub Apps.
- Interpret legal questions.

Every irreversible action is performed by the Release Approver, with their own GitHub session.

---

## 4. Branch protection and ruleset posture (interim)

The `main` branch is protected by a GitHub ruleset:

| Rule | Interim setting |
|---|---|
| Require pull request | Yes |
| Required approvals | 1 (uniform; dual sign-off for the classes in §2.2 is enforced by the `release-integrity` check) |
| Require approval other than last pusher | Yes |
| Dismiss stale approvals on push | Yes |
| Require conversation resolution | Yes |
| Require code-owner review | Yes |
| Required status checks | `validate-spec`, `validate-schemas`, `links`, `release-integrity`, `DCO` |
| Require linear history | Yes |
| Squash merge only | Yes |
| Block force pushes | Yes |
| Block deletions | Yes |
| Signed commits | No (deferred — see §4.1) |
| Bypass list | `release-approvers` only; never "all admins" |
| Restrict workflow changes | Yes (via `.github/CODEOWNERS` ownership of `.github/workflows/**`) |
| Protect release tags | Yes — tag ruleset for `APP-*` prevents creation, update, or deletion outside `release-approvers` |

**Ruleset activation is blocked until the co-maintainer is confirmed in the editors team with 2FA.** This is because GitHub does not allow self-approval, and the "approval other than last pusher" rule requires a second reviewer with write access.

### 4.1 Signed commits posture

Signed commits are **not required at launch**. Requiring signatures on first contributions forces unsigned-commit remediation via rebase and force push, which is a poor experience for non-technical contributors. Signed commits will be required on release branches first, after a documented contributor-readiness check.

---

## 5. Working Group formation — the matriculation trigger

The interim governance in this file steps up to full Working Group governance when **all** of the following are true (Release Approver confirms):

1. **Charter v0.4 or later** is ratified with clear membership rules.
2. **Minimum three organisationally-independent maintainers** with write access.
3. **AAIF or equivalent neutral custodian** formally designated.
4. **Contribution Terms v0.3 or later** published with a CLA option available.
5. **First public consultation window** has closed and a decision record exists for material comments.

Until all five are true, the interim rules in this file apply.

At the trigger, approval thresholds become uniform at **2 approvals + CODEOWNER + status checks** for all PRs to `main`, and the Release Approver's unilateral sign-off is replaced by the Working Group's decision procedure in a revised `csl/Governance.md`.

---

## 6. Decision records

Every accepted or rejected normative proposal, every ruleset change, every GitHub App installation, and every publication-clearance decision is recorded in `/decisions/APP-DEC-XXXX.md`. This exists so matriculation to the Successor Foundation is a file transfer, not an archaeology exercise.

The Operations Registry at [`OPERATIONS-REGISTRY.md`](OPERATIONS-REGISTRY.md) records every installed GitHub App, external Action, mail alias, DNS record, and permission grant with a named human approver and installation timestamp.

---

## 7. Escalation

The following, if encountered, are escalated immediately to the Release Approver and handled per the Charter and Privacy Notice (not inside the PR or Issue thread):

- Personal data of a third party or sensitive personal data in a public comment, Issue, PR, or Discussion.
- A suspected security defect posted publicly.
- Any accusation of licence, IP, or antitrust violation directed at APP, the Interim Custodian, or a Contributor.
- Any contact from a public official, regulator, or opposing legal counsel.
- Any request to change branch protection, add secrets, install a GitHub App, or grant admin access.

The Custodian's first action in these cases is restrictive visibility (hide, mark off-topic, lock, or similar) and private notification of the Release Approver — not a public reply.

---

## 8. Changes to this file

`GOVERNANCE.md` is a repository file; changes follow the pull-request process in [`CONTRIBUTING.md`](CONTRIBUTING.md). Material changes to this file require Release Approver sign-off per §2.2.

---

*This file is the public, community-facing governance description. The binding legal instruments are the Contribution Terms (CSL 1.0 verbatim) and the WG Data Handling Charter.*
