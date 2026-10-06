# Repository Security Automation Policy

This file documents how automated workflows and third-party integrations are permitted to operate in this repository. It is a public, auditable statement of policy, aimed at reviewers, security researchers, and future custodians (including the Successor Foundation).

For reporting vulnerabilities in the Specification, see [`SECURITY.md`](SECURITY.md).

---

## 1. GitHub Actions baseline

Every workflow in `.github/workflows/` MUST comply with the following:

### 1.1 Permissions

- `permissions: contents: read` is declared at workflow level by default.
- Any job that requires elevated permissions declares them scoped to that job only.
- A workflow that writes to the repository, posts comments, or modifies metadata declares each needed permission explicitly and no more.

### 1.2 Secrets

- **Repository secrets are not used in pull-request-triggered workflows.** This prevents a hostile PR from exfiltrating a secret via a build step.
- Secrets, if introduced, are scoped to the smallest workflow that needs them, logged in [`OPERATIONS-REGISTRY.md`](OPERATIONS-REGISTRY.md) at introduction, and rotated or removed on a named timeline.

### 1.3 Runners

- Workflows use **GitHub-hosted runners only**. Self-hosted runners are not permitted; they expose the project to repository-code execution on infrastructure the project does not control.

### 1.4 Triggers

- **`pull_request_target` is avoided** unless strictly necessary. Where unavoidable:
  - No checkout of the PR-head code.
  - PR titles, branch names, issue bodies, labels, and commit messages are treated as **untrusted input** and are not interpolated into shell commands or other interpreters without sanitisation.
- Workflows triggered by `issue_comment`, `discussion_comment`, or similar are treated with the same discipline.
- First-time contributors' workflow runs **require maintainer approval** (GitHub repository setting, enforced in the GitHub web UI).

### 1.5 Third-party action pinning

- **Every third-party action is pinned to a full commit SHA** with a version comment. Tag references (`@v4`) are forbidden because they can be moved by the action's publisher.
- Example of a correct reference:
  ```yaml
  - uses: actions/checkout@abc123def7890123456789abcdef0123456789ab # v4.0.0
  ```
- Tag-only references (`uses: actions/checkout@v4`) fail code review.

### 1.6 Workflow file ownership

- All files under `.github/workflows/` are owned by `@agenticprocessprotocol/custodians` in [`.github/CODEOWNERS`](.github/CODEOWNERS). A code-owner review is required before any workflow change can be merged.

---

## 2. Third-party GitHub Apps — admission checklist

Before installing any third-party GitHub App, the Release Approver completes the following admission checklist, with values **verified at the moment of installation**. The Custodian prepares the checklist; the Release Approver captures the values GitHub displays.

| Field | Source of truth (verify at installation) |
|---|---|
| App name displayed by GitHub | GitHub App installation screen |
| Publisher identity displayed by GitHub | GitHub App installation screen |
| Exact repository permissions requested | GitHub App installation permissions list |
| Exact organisation permissions requested | GitHub App installation permissions list |
| Public data-retention or privacy statement | App landing page and linked publisher documentation |
| Installation scope | Verify "Only select repositories" is chosen; capture the repository list |
| Alternative considered (e.g., repo-local workflow) | Note whether a self-hosted alternative exists and why it was not preferred |
| Named human approving | Release Approver signature at installation moment |
| Verification timestamp | Date and time of installation |

Verified values are recorded in [`OPERATIONS-REGISTRY.md`](OPERATIONS-REGISTRY.md). If any observed value materially differs from the public claims about the App, the Release Approver decides whether to proceed or fall back to a repo-local workflow.

**No App is installed unilaterally by the Custodian.**

---

## 3. Dependabot

Dependabot is configured at [`.github/dependabot.yml`](.github/dependabot.yml) to monitor:

- `github-actions` — weekly updates for pinned actions (keeps SHA pins current without changing policy).
- `pip` — weekly updates for Python dependencies used by validator scripts.

Dependabot PRs follow the same review process as any other PR, including the DCO requirement (Dependabot sign-off is configured).

---

## 4. Operational discipline

- The Operations Registry [`OPERATIONS-REGISTRY.md`](OPERATIONS-REGISTRY.md) records every installed App, external Action, mail alias, DNS record, and permission grant with a named human approver and installation timestamp.
- Workflows that **create or modify files, open PRs, or post to Discussions** are reviewed with particular care because they are the mechanism by which an exploited supply-chain attack would most likely manifest.
- Workflow failures on `main` are treated as incidents, not noise. A failed `validate-spec` run on `main` indicates either (a) a bypass has been taken on a prior PR, or (b) the validator has broken; both require investigation.

---

## 5. Changes to this policy

Material changes to `SECURITY-AUTOMATION.md` require Release Approver sign-off per [`GOVERNANCE.md`](GOVERNANCE.md) §2.2 (classified as a legal/governance change path). Clerical corrections may be submitted directly.
