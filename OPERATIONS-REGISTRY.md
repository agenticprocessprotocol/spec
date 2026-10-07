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

*(Append-only. If any element above is removed, add an entry here with: element, removal date, approver, reason, and replacement if any. Do not delete the installation entry above.)*

---

**Governance of this file:** `OPERATIONS-REGISTRY.md` is co-owned by `@agenticprocessprotocol/custodians` and `@agenticprocessprotocol/release-approvers` in `.github/CODEOWNERS`. Changes require Release Approver sign-off per `GOVERNANCE.md` §2.2.
