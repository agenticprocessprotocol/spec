# CSL 1.0 Notices

**Purpose:** This file is the `Notices.md` companion referenced by the **Community Specification License 1.0** at §§2.1.3.3, 2.3, and 3. It is the mechanism by which:

- **Implementers** indicate acceptance of the Licence under CSL 1.0 §2.1.3.3.
- **Contributors** issue **Exclusion Notices** under CSL 1.0 §3.
- **Contributors** provide notice of **withdrawal** under CSL 1.0 §2.3.

Each notice is a pull request adding an entry below under the appropriate section. This file is **append-only** — existing entries are never edited or removed; a superseding notice adds a new entry.

**Status:** this file is effective once published in a tagged coordinated APP baseline. Prior to that, this file is a drafting template.

**How to submit a notice:** open a pull request that adds a new entry to the appropriate section. The PR triggers code-owner review by `@agenticprocessprotocol/release-approvers`. The entry is published when the PR is merged.

---

## 1. Implementer acceptance notices (CSL 1.0 §2.1.3.3)

For an Implementer whose implementation is distributed in a form other than source code, acceptance of the Licence is indicated by a pull request to this section. CSL 1.0 §2.1.3.1 and §2.1.3.2 (source code and in-distribution notices) are alternative acceptance paths and do not require an entry here.

**Entry format:**

```markdown
### <Implementer name>
- **Specification version implemented:** <baseline-id, e.g. APP-2026-10-RC1>
- **Authorised individual:** <Name, role at the Implementer>
- **System identifier:** <implementation name/identifier, as the Implementer uses it>
- **Contact for licensing matters:** <email or address>
- **Date of acceptance:** <YYYY-MM-DD>
- **PR link:** <GitHub PR URL>
```

**Entries:**

*(None at the current baseline. Add new entries below this line.)*

---

## 2. Contributor Exclusion Notices (CSL 1.0 §3)

A Contributor may exclude specified patent claims from the licensing commitments under CSL 1.0 §2.1.1 by filing an Exclusion Notice. CSL 1.0 §3.1 provides a 45-day window from the date of Contribution; CSL 1.0 §3.2 provides a window prior to a Draft Specification becoming Approved for claims eligible under §3.1 constraints.

**Entry format:**

```markdown
### <Contributor name> — Exclusion Notice <sequence number>
- **Type:** <§3.1 Contribution-based | §3.2 Approval-based>
- **Patents or patent applications excluded:** <specific identifiers; or a specific claim scope statement>
- **Scope of exclusion:** <description, with reference to the specific Contribution(s) or Draft Specification sections>
- **Effective date of underlying Contribution(s) (for §3.1):** <YYYY-MM-DD>
- **Notice filed:** <YYYY-MM-DD>
- **PR link:** <GitHub PR URL>
```

**Entries:**

*(None at the current baseline. Add new entries below this line.)*

---

## 3. Contributor Withdrawal Notices (CSL 1.0 §2.3)

A Contributor may withdraw from the Working Group by filing a Withdrawal Notice. Per CSL 1.0 §2.3, existing commitments and obligations up to the date of withdrawal remain in effect; no new obligations are incurred after that date.

**Entry format:**

```markdown
### <Contributor name> — Withdrawal Notice
- **Date of withdrawal:** <YYYY-MM-DD>
- **Scope of prior Contributions (for reference):** <summary; detailed record is in commit history>
- **PR link:** <GitHub PR URL>
```

**Entries:**

*(None at the current baseline. Add new entries below this line.)*

---

## 4. Specification status entries

Status changes (e.g., a Draft Specification being designated an Approved Specification per `csl/Governance.md` §3) are recorded here as a durable notice, in addition to the manifest, release notes, and this file's audit trail elsewhere.

**Entry format:**

```markdown
### <Baseline-id> — <status designation>
- **Baseline tag:** <APP-YYYY-MM-RCn>
- **Status:** <Draft Specification | Approved Specification>
- **Effective date:** <YYYY-MM-DD>
- **Approving procedure:** <reference to csl/Governance.md section; decision record under /decisions/>
- **PR link:** <GitHub PR URL>
```

**Entries:**

*(None at the current baseline. Add new entries below this line.)*

---

## 5. File discipline

- **Append-only.** Existing entries are not edited or removed. Superseding information is added as a new entry.
- Changes to the **structure** of this file (not entries) are governed by `GOVERNANCE.md` §2.2 and require Release Approver sign-off.
- Entries added via PR are reviewed by `@agenticprocessprotocol/release-approvers` per `.github/CODEOWNERS`.

---

*This file satisfies CSL 1.0's structural requirement for a Notices.md companion. For the Draft → Approved transition process, see `csl/Governance.md`. For the technical scope that bounds patent commitments, see `csl/Scope.md`. For the licence itself, see `/LICENSE`.*
