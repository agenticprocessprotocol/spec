# APP-DEC-0004 — `main` ruleset activation (Phase 2b/2c)

| Field | Value |
|:---|:---|
| Decision number | APP-DEC-0004 |
| Date | 2026-10-24 |
| Status | Accepted |
| Decided by | Vaidhya, Release Approver (Interim Custodian) |
| Instruments affected | Ruleset `main-protection` on `agenticprocessprotocol/spec`; repository access of teams `custodians`, `editors`, `release-approvers`; `GOVERNANCE.md` §2.2 and §4; `OPERATIONS-REGISTRY.md` §2, §3, §9 |
| Related | APP-DEC-0003 (KI-09 tracking); Issue #16 (KI-09); PR #24 (CODEOWNERS pattern fix); test PRs #22 and #23 |

## Decision

1. **Phase 2b and 2c are brought forward**, ahead of Phase 2.5 and Phase 2a. The `main` ruleset is activated now; the DCO App installation stays pending.
2. **Ruleset `main-protection` is active on the default branch** from 2026-10-24, with the settings in §2.
3. **Required status checks are limited to five:** the four `validate-spec` jobs and `release-integrity` (§3).
4. **Teams `custodians`, `editors` and `release-approvers` have Write access to `spec`** from 2026-10-24. GitHub accepts a team as a code owner only if the team is visible and has explicit Write access to the repository. This grant cleared the "unknown owner" errors GitHub reported for every line of `.github/CODEOWNERS`.
5. **Code-owner review is off at activation.** It is to be switched on after the CODEOWNERS pattern fix (PR #24) merges. §4 records a consequence to confirm before that switch is made.

## 1. Context

`GOVERNANCE.md` §4 and Custodian Instructions §8 set the target `main` ruleset. Activation was scheduled for Phase 2c, after a decision record in Phase 2b. Until now, `main` was protected only by Custodian discipline. Direct commits to `main` on 2026-10-07, 2026-10-08 and 2026-10-09 are recorded in `OPERATIONS-REGISTRY.md` §9 as the events KI-09 tracks. Issue #16 (KI-09) closes "when Package 4 activation decision is recorded"; this record is that decision.

## 2. Settings in force

Read from the GitHub rulesets API on 2026-10-24. The ruleset was created at 08:41 UTC and last edited at 08:50 UTC. Ruleset ID `25775829`.

| Setting | In force |
|:---|:---|
| Target | Default branch (`~DEFAULT_BRANCH`, currently `main`) |
| Enforcement | Active |
| Bypass list | `release-approvers` team, for pull requests only |
| Restrict deletions | On |
| Block force pushes | On |
| Require a pull request before merging | On |
| Required approvals | 1 |
| Dismiss stale approvals when new commits are pushed | On |
| Require approval of the most recent reviewable push (approver other than the last pusher) | On |
| Require conversation resolution | On |
| Require review from Code Owners | **Off** (see §4) |
| Allowed merge methods | Squash only |
| Require linear history | On |
| Required status checks | `Manifest validator`, `Legacy-name validator`, `Normative-keyword validator`, `Cross-reference validator`, `Release integrity + sign-off verification` (source: GitHub Actions) |
| Require branches to be up to date before merging | Off |
| Signed commits | Not required |
| Further API parameter | `require_extra_approval_for_unattributed_changes: true`, recorded as the API reports it |

The full API export is reproduced in the appendix.

## 3. Required checks: what is excluded, and when it is added

| Check | Why it is not required yet | Added when |
|:---|:---|:---|
| `links` (Lychee link check) | Runs only when Markdown or HTML changes. A required check that does not run leaves a PR waiting indefinitely | The workflow reports on every pull request |
| `validate-schemas` | Runs only when `schemas/**` changes; same reason | The workflow reports on every pull request |
| DCO | **No DCO check exists today.** The DCO App is not installed, and no repository workflow checks `Signed-off-by` trailers | The DCO App is installed, or a repository-local DCO job is added |
| Reference-hygiene validator | Proposed in draft PR #21; not on `main` | PR #21 merges and the Release Approver adds it |

Until a DCO check exists, the Custodian checks the `Signed-off-by` trailer on every commit of every pull request as part of review.

## 4. Code-owner review

**Planned:** switch on "Require review from Code Owners" after PR #24 merges.

**Consequence to confirm before switching it on.** GitHub's rules, both from its documentation:

- When code-owner review is required, an approval from any one listed owner satisfies it.
- A pull-request author cannot approve their own pull request.

At the time of this decision, `custodians` and `release-approvers` each have one member, the Release Approver, whose account also opens the pull requests the Custodian prepares. With code-owner review on, such a pull request cannot obtain a code-owner approval for any path owned only by those two teams. Those paths include:

- root files and `sessions/`;
- `decisions/`, `legal/`, `csl/`, `releases/`, `OPERATIONS-REGISTRY.md`;
- `.github/` workflows and scripts, and `tools/`;
- APP-1 and the APP-IG guides under `drafts/spec/`.

Such a pull request could then merge only through the `release-approvers` bypass, and every bypass is logged as a governance event. Paths owned by `editors`, or by `editors` with `release-approvers`, are unaffected, because the co-maintainer can approve them.

The Release Approver decides before the switch is made whether to proceed, keep code-owner review off until each owning team has a member who does not author the pull requests it reviews, or change team membership or pull-request authorship.

## 5. Other departures from the `GOVERNANCE.md` §4 target

| Item | Target | In force | Note |
|:---|:---|:---|:---|
| Branch up to date | Yes for release PRs | Off for all PRs | Rulesets cannot scope this by path. The Custodian brings a release PR up to date with `main` before preparing its merge |
| Restrict workflow changes | Via CODEOWNERS ownership of `.github/workflows/**` | Not enforced while code-owner review is off | Workflow changes still need one approval from someone other than the last pusher |

## 6. Verification

| Test | PR | Result |
|:---|:---|:---|
| A — RFC 2119 keyword added under `/drafts/spec/` with no change-impact manifest and no sign-off | #22 | `Normative-keyword validator` failed; `Release integrity + sign-off verification` failed; merge blocked |
| B — informative file under `/drafts/guides/`, no keyword | #23 | All five required checks passed; merge blocked only by the review requirement |

Tranche 2 acceptance also lists a DCO App check on pull requests with and without sign-off. That item stays open until the DCO App is installed.

## 7. Known Issue disposition

KI-09 (Issue #16) is resolved by this record: the `main` ruleset is active, and the differential sign-off check has been exercised on live pull requests (#20, #22, #23). The DCO App installation continues as a Phase 2c item outside KI-09.

## Appendix — API export (2026-10-24)

```json
{
  "id": 25775829,
  "name": "main-protection",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "bypass_actors": [ { "actor_type": "Team", "actor_id": 19697337, "bypass_mode": "pull_request" } ],
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "pull_request", "parameters": {
        "required_approving_review_count": 1,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "require_last_push_approval": true,
        "required_review_thread_resolution": true,
        "require_extra_approval_for_unattributed_changes": true,
        "allowed_merge_methods": ["squash"] } },
    { "type": "required_linear_history" },
    { "type": "required_status_checks", "parameters": {
        "strict_required_status_checks_policy": false,
        "do_not_enforce_on_create": false,
        "required_status_checks": [
          { "context": "Manifest validator", "integration_id": 15368 },
          { "context": "Legacy-name validator", "integration_id": 15368 },
          { "context": "Normative-keyword validator", "integration_id": 15368 },
          { "context": "Cross-reference validator", "integration_id": 15368 },
          { "context": "Release integrity + sign-off verification", "integration_id": 15368 } ] } }
  ]
}
```

Team `19697337` is `release-approvers`. Integration `15368` is GitHub Actions.
