# Operations Registry

This file records every operational element of the Agentic Process Protocol repository that has governance significance — GitHub Apps, external Actions, mail aliases, DNS records, permission grants, and the human who approved each.

**Why this file exists:** matriculation to a Successor Foundation should be a file transfer, not an archaeology exercise. Every item here has a named approver and a timestamp, so custody transfer is mechanical.

**Format discipline:** append-only within each section. If an item is removed, add a removal entry; do not delete the installation entry.

---

## 1. GitHub organisation

| Element | Value | Approver | Date | Notes |
|---|---|---|---|---|
| Organisation | `agenticprocessprotocol` | Vaidhya (Vach AI Limited) | 2026-10-06 | Established in Work Package 1 |
| 2FA enforcement | On | Vaidhya | 2026-10-06 | Org-wide |
| Default Actions permissions | Read-only | Vaidhya | 2026-10-06 | Org-level default |

## 2. Repository

| Element | Value | Approver | Date | Notes |
|---|---|---|---|---|
| Repository | `agenticprocessprotocol/spec` | Vaidhya | 2026-09-XX | Public, empty at creation |
| Default branch | `main` | Vaidhya | 2026-10-XX | Set during Package 2 PR merge |
| Branch protection — `main` | Enabled, interim ruleset | Vaidhya | 2026-10-06 | Activated at Package 4 |
| Tag protection — `APP-*` | Enabled | Vaidhya | 2026-10-06 | Activated at Package 4 |
| Private vulnerability reporting | Enabled | Vaidhya | 2026-10-06 | Activated at Package 4 |
| Secret scanning + push protection | Enabled | Vaidhya | 2026-10-06 | Activated at Package 4 |
| First-time contributor workflow approval | Required | Vaidhya | 2026-10-06 | Activated at Package 4 |

## 3. Teams and access

| Team | Members | Approver | Date | Notes |
|---|---|---|---|---|
| `@agenticprocessprotocol/custodians` | APP Custodian, Vaidhya | Vaidhya | 2026-09-28 | Created in Package 1 |
| `@agenticprocessprotocol/editors` | Vaidhya | Vaidhya | 2026-10-06 | Co-maintainer per §4 Option A |
| `@agenticprocessprotocol/release-approvers` | Bhavna | Bhavna | 2026-10-06 | Named individual, not a shared mailbox |
| `@agenticprocessprotocol/working-group` | *(empty)* | Vaidhya | 2026-10-XX | Reserved for WG formation |

## 4. GitHub Apps installed

| App | Publisher | Scope | Permissions | Approver | Installation date | Verification notes |
|---|---|---|---|---|---|---|
| *(none yet)* | | | | | | DCO App to be installed at Package 4 per admission checklist in `SECURITY-AUTOMATION.md` §2 |
| Claude GitHub App | Anthropic | User account `APPcustodian` (Personal) — All repositories | *(to be captured)* | Vaidhya (Release Approver) | 2026-10-XX | Recorded 2026-10-08 (see §9). Admission checklist values not yet captured |
| Claude GitHub App | Anthropic | Organisation `agenticprocessprotocol` — All repositories | *(to be captured)* | Vaidhya (Release Approver) | 2026-10-XX | Recorded 2026-10-08 (see §9). Admission checklist values not yet captured |

### DCO App installation — admission checklist values (populated at Package 4)

| Field | Verified value |
|---|---|
| App name displayed by GitHub | *(to be captured)* |
| Publisher identity displayed by GitHub | *(to be captured)* |
| Repository permissions requested | *(to be captured)* |
| Organisation permissions requested | *(to be captured)* |
| Public data-retention or privacy statement | *(to be captured — reference URL)* |
| Installation scope | *(Only select repositories = `agenticprocessprotocol/spec`)* |
| Alternative considered | Repo-local DCO workflow — considered as fallback if App permissions materially exceed need |
| Named human approving | Vaidhya (Release Approver) |
| Verification timestamp | *(to be captured)* |

## 5. External GitHub Actions used

Every third-party action pinned to a full commit SHA. Dependabot keeps SHAs current.

| Action | Pin | First used | Approver | Notes |
|---|---|---|---|---|
| `actions/checkout` | *(SHA pin recorded in workflows)* | 2026-10-XX | Vaidhya | Standard checkout |
| `actions/setup-python` | *(SHA pin)* | 2026-10-XX | Vaidhya | Python 3.12 for validators |
| `lycheeverse/lychee-action` | *(SHA pin)* | 2026-10-XX | Vaidhya | Link checker |

*(Entries added as workflows evolve. SHAs are in the workflow files; this table is a human-readable summary.)*

## 6. Mail infrastructure

| Alias | Mailbox / forward | Approver | Date | Notes |
|---|---|---|---|---|
| `security@agenticprocess.org` | Shared mailbox, Vach M365 tenant | Vaidhya | 2026-09-XX | Monitored by Release Approver + deputy |
| `privacy@agenticprocess.org` | Shared mailbox, Vach M365 tenant | Vaidhya | 2026-09-XX | **Live compliance obligation** per Privacy Notice v0.3 |
| `conduct@agenticprocess.org` | Shared mailbox, Vach M365 tenant | Vaidhya | 2026-09-XX | Code of Conduct reports |
| `custodian@agenticprocess.org` | Shared mailbox, Vach M365 tenant | Vaidhya | 2026-09-XX | General custodian correspondence |
| `webmaster@agenticprocess.org` | Shared mailbox, Vach M365 tenant | Vaidhya | 2026-09-XX | Site operational contact |
| `contribute@agenticprocess.org` | *(deferred)* | — | — | Create when named in published contribution guidance |
| `wg@agenticprocess.org` | *(deferred)* | — | — | Create when named in WG communications |

Mail is on the Vach AI Limited M365 tenant with `agenticprocess.org` as an additional accepted domain. Transfers to Successor Foundation infrastructure at matriculation per Charter §2.

## 7. DNS records

| Type | Name | Purpose | Approver | Date |
|---|---|---|---|---|
| TXT | GitHub org verification | Prove org ownership | Vaidhya | 2026-09-XX |
| MX | `agenticprocess.org` | Mail routing to Vach M365 tenant | Vaidhya | 2026-09-XX |
| TXT | `agenticprocess.org` SPF | Mail sender policy | Vaidhya | 2026-09-XX |
| TXT | DKIM selector | Mail signing | Vaidhya | 2026-09-XX |
| TXT | DMARC | Mail receiver policy | Vaidhya | 2026-09-XX |
| TXT | `agenticprocessprotocol.org` defensive | Defensive redirect only | Vaidhya | 2026-09-XX |

## 8. Secrets

| Secret | Scope | Purpose | Approver | Rotation policy |
|---|---|---|---|---|
| *(none)* | | | | |

Repository secrets are introduced only where strictly required, by Release Approver approval, with a named rotation policy.

## 9. Removals and transitions

2026-10-07 — APP-2026-10-RC1 tag created and GitHub Release published. Approver: @APPcustodian (Vaidhya). Reviewer on PR #7: @bhavna-vach.

# 2026-10-07 — Legal instrument activation

- `legal/APP_Contribution_Terms_v0_3.md` — Effective 2026-10-07
- `legal/APP_Consultation_Privacy_Notice_v0_4.md` — Effective 2026-10-07
- `legal/REVIEW-STATUS.md` — Successor Foundation review items disclosed

Committed directly to main by Release Approver (APPcustodian / Vaidhya).
Direct-commit path used; Package 4 `main` ruleset not yet active.
Validators (validate-spec, links) ran and passed on push.
Release-integrity and DCO checks did not fire (pull_request-triggered only);
sign-off is in the Release Approver's committer identity on the commits.

Approved content per prior session planning; no retrospective PR needed.

**KI-09 relevance:** this is the kind of event Package 4 activation prevents.
Tracked.

## 2026-10-08 — APP operational infrastructure

Cloud environment:
- Platform: Claude Code cloud environment (Anthropic-hosted)
- Name: APP
- Network policy: Trusted
- Repository scope: agenticprocessprotocol/spec
- Authorized by: Vaidhya, Release Approver

GitHub Apps installed:
- Claude GitHub App on APPcustodian (user, Personal, All repositories)
- Claude GitHub App on agenticprocessprotocol (org, All repositories)
- Authorized by: Vaidhya, Release Approver

Fallback:
- Manual GitHub web UI per Runbook §5 if cloud environment unavailable
- Local git clone + manual push if required

## 2026-10-08 — Governance corrections (same-day)

Two corrections to the 2026-10-08 entry above:

1. Claude GitHub App scope on agenticprocessprotocol narrowed
   from "All repositories" to "Only `spec`" on 2026-10-08. Matches
   Runbook §8 / `SECURITY-AUTOMATION.md` §2 admission checklist
   discipline. APPcustodian user-level scope retained at "All
   repositories" (user account has single-purpose scope;
   functionally equivalent to spec-only).

2. Procedural note on the 2026-10-08 section above: direct
   commit by Release Approver; CODEOWNERS review not exercised;
   Package 4 ruleset not yet active. KI-09 tracks activation.

Approved by Vaidhya, Release Approver.

## 2026-10-08 — Parallel Claude Code session note

Two Claude Code sessions committed to main on 2026-10-08:
- Session A (desktop Code tab, Vaidhya): governance commits with
  explicit Release Approver approval
- Session B (web-chat-triggered, Claude): commit 1395f93 to
  APP-DEC-0003 adding Issue number column

Session B commit content was correct and intended. Attribution
and approval line were not applied because the session was
triggered via web chat without passing through the Code tab
approval pattern.

Going forward: APP operations route through the Code tab
session (Session A) only. Web chat prepares instructions as
text; execution happens in Code tab with explicit Release
Approver approval.

KI-09 relevance: this is another instance Package 4 ruleset
activation would prevent.

Approved by Vaidhya, Release Approver.

## 2026-10-09 — WP3 (APP-2026-10-RC1 Baseline) — Formal closure

**Tag date:** 2026-10-07
**Entry recorded:** 2026-10-09
**Approver:** Vaidhya (APPcustodian)
**Tag:** APP-2026-10-RC1 at commit 59b296a
**Release:** published Latest on github.com/agenticprocessprotocol/spec/releases

**WP3 artefacts produced at tag time:**

- `/releases/APP-2026-10-RC1/spec/` — eleven coordinated specification documents at tag versions
- `/releases/APP-2026-10-RC1/guides/` — plain-language guides at tag versions
- `/releases/APP-2026-10-RC1/legal/` — Contribution Terms v0.2, WG Data Handling Charter v0.3, Consultation Privacy Notice v0.3 (RC1 baseline versions)
- `/releases/APP-2026-10-RC1/MANIFEST.md` and `/releases/APP-2026-10-RC1/manifest.json`
- `/releases/APP-2026-10-RC1/RELEASE-NOTES.md`
- `/releases/APP-2026-10-RC1/KNOWN_ISSUES.md`
- Lightweight Git tag `APP-2026-10-RC1`
- GitHub Release published Latest
- APP-DEC-0002 (RC1 publication decision record)

**Validators passing on release PR (#7):** `validate-spec`, `links`, `release-integrity`. `validate-schemas` did not run (path filter `schemas/**` not matched by the PR). No DCO App check ran (DCO App not yet installed; Package 4); release-integrity performed sign-off verification.

**Documentation gaps at tag time, closed during this entry's drafting (2026-10-09):**

- `CHANGELOG.md` was not updated at tag time. Public CHANGELOG read "RC1 is in preparation and not citable", contradicting the published Release and tag. Closed by commit `9bd8e5b` adding the APP-2026-10-RC1 CHANGELOG entry with baseline-version legal instruments, plus an Unreleased section noting Contribution Terms v0.3 and Consultation Privacy Notice v0.4 activated 2026-10-07.
- `APP-DEC-0001` (WP2 scaffold adoption decision record) remained at Status: Proposed with a placeholder date despite the scaffold having been adopted at WP2 merge. This was a WP2 decision-record defect surfaced during WP3 retrospective, not a WP3 artefact. Closed by commit `c6df45d` setting Status: Accepted with the actual WP2 scaffold adoption date.

Both closure commits direct to main under Runbook §4 interim operating mode. release-integrity (including sign-off verification) is PR-triggered and did not run on these direct commits; DCO sign-off trailers are present and self-attested. Package 4 Tranche 2 will install the DCO App and activate the main branch ruleset, routing all future main-branch changes through PR validation (release-integrity + DCO App checks).

Gaps are documented here rather than being silently resolved, per the governance paper trail integrity principle (prior-session lesson 7).

**Known Issues at RC1 publication:** mapped to GitHub Issues #8–#17 under APP-DEC-0003 (Kit C).

## 2026-10-09 — WP4 Tranche 1 — Feedback and safeguards (partial)

**Date:** 2026-10-08
**Approver:** Vaidhya (APPcustodian)

Partial completion of WP4. Safeguards layer activated; DCO App installation and `main` branch ruleset deferred to Tranche 2 (pending APP-DEC-0004).

**Platform configuration completed:**

- **GitHub Discussions — six categories live** per Custodian Instructions §5 Package 4:
  - Announcements (moderator-only post, all-comment)
  - Getting Started & Questions
  - Document Feedback
  - Substantive Proposals
  - Implementation Experience
  - Working Group Administration

  Default Polls and Ideas categories deleted. General and Show-and-Tell retained; may be scoped or removed later based on observed use.

- **Tag ruleset — "APP release tag protection"** active at repository level, targeting `APP-*`. Restrict creations / updates / deletions. Bypass actors: `release-approvers` team only. Protects `APP-2026-10-RC1` and all future `APP-*` tags against unauthorised creation, modification, or deletion.

  Scope note: ruleset installed at repository level, not organisation level, because org-level rulesets are non-enforcing at the current GitHub plan tier. This is an infrastructure constraint, not a design preference.

- **First-time-contributor workflow approval:** verified active (GitHub default for public repositories).

- **Private vulnerability reporting + secret scanning + push protection:** confirmed active (enabled at an earlier stage; included here for Tranche 1 completeness).

**Deferred to WP4 Tranche 2 (planned via APP-DEC-0004):**

- DCO GitHub App admission checklist and installation (Instructions §8).
- `main` branch ruleset activation per §9 target state. Resolves KI-09 (Issue #16).

**Operational note — platform/content split:** three of four Tranche 1 items were executed via manual GitHub web UI rather than Claude Code. Two causes: (a) the Claude Code cloud session proxy refuses repository-settings and ruleset writes (HTTP 403), although the GitHub REST API itself supports enabling Discussions and creating rulesets; (b) Discussion categories have no REST API, and GraphQL is not reachable from Claude Code cloud sessions. Content work (files, Issues, commits) continues via Claude Code; platform configuration via manual UI. This split is a persistent operating boundary, documented here so future AAIF transfer sees the pattern.

*(Append-only. If any element above is removed, add an entry here with: element, removal date, approver, reason, and replacement if any. Do not delete the installation entry above.)*

---

**Governance of this file:** `OPERATIONS-REGISTRY.md` is co-owned by `@agenticprocessprotocol/custodians` and `@agenticprocessprotocol/release-approvers` in `.github/CODEOWNERS`. Changes require Release Approver sign-off per `GOVERNANCE.md` §2.2.
