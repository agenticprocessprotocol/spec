# Security Policy

Thank you for helping keep the Agentic Process Protocol safe.

This file covers:

- how to report a security vulnerability,
- what the project will not accept into the public repository,
- the scope of "security" for APP (which is a specification, not a product).

---

## 1. Reporting a vulnerability

### 1.1 Preferred: GitHub private vulnerability reporting

Please report suspected security defects via the repository's **Security** tab → **Report a vulnerability**. This creates a private channel visible only to repository maintainers.

Direct link: `https://github.com/agenticprocessprotocol/spec/security/advisories/new`

### 1.2 Backup channel

If GitHub's private reporting is unavailable to you, email **security@agenticprocess.org**. This mailbox is monitored by the Release Approver and a trusted deputy.

If you need to encrypt your report, request an OpenPGP key from `security@agenticprocess.org` and we will provide one before you send the detail.

### 1.3 What **not** to do

**Please do not open a public GitHub Issue** for a suspected security defect. A public report risks exposure to anyone watching the repository before a fix can be prepared. If you have already opened such an Issue by accident, email `security@agenticprocess.org` immediately so we can take restrictive-visibility action.

### 1.4 What to include

Where you can, your report should state:

- Which document, requirement ID, schema, or reference design is affected.
- The nature of the defect (what the Specification says, what you believe it should say).
- Whether an implementation that follows the Specification literally would be exploitable, and under what conditions.
- Any proof-of-concept, test vector, or implementation evidence.
- Your preferred credit (name, affiliation, or anonymous).

You do not need all of this to report. A clear description of the concern is enough.

---

## 2. What APP is, for security purposes

APP is a **specification**, not a running service. "Security defects" in APP are typically one of:

- a **normative defect** in a security requirement (APP-3, or a security-relevant requirement in APP-2 or APP-4),
- an **ambiguity** that allows a conforming implementation to be exploitable,
- a **schema defect** that permits an unsafe construct in `/schemas/**` or a reference design in `/reference/**`,
- a **validator defect** in `/tools/**` that permits an invalid artefact to pass.

Vulnerabilities in a **third-party implementation** of APP are the responsibility of that implementation's vendor; please report them to the vendor. We can help you locate the vendor if the implementation claims APP conformance.

---

## 3. Response posture

- We acknowledge receipt within **three working days**.
- We assess scope and classify the report within **ten working days** of acknowledgement.
- Where remediation is needed, we discuss a disclosure window with the reporter. The project does not operate a fixed embargo policy; we calibrate to the risk and the complexity of coordination.
- Credit is at the reporter's option.

We do not operate a paid bug bounty.

---

## 4. Never-in-repo

Please do **not** paste the following into any public comment, Issue, PR, Discussion, or commit:

- **Credentials of any kind** — API keys, tokens, passwords, session cookies, private keys, service-account secrets.
- **Off-platform-collected personal data** — mailing-list membership, sign-up sheets, event attendance, reviewer contacts, employer/affiliation fields collected outside GitHub, private correspondence copied in.
  - *This rule does not restrict* ordinary GitHub identity (your username, display name, DCO sign-off email, commit metadata) — those are inherent to using GitHub and are disclosed in the Privacy Notice.
- **Sensitive personal data** — health, sexual orientation, religion, race, political opinions, national ID numbers, dates of birth.
- **Third-party content without a licence check** — copyrighted material, unlicensed code, paywalled standards text.
- **Interim Custodian internal material** — commercial strategy, competitor analysis, unreleased implementation IP, pricing, uncleared customer references.
- **Undisclosed, materially-AI-generated substantive normative content** — see `CONTRIBUTING.md` §4 for the disclosure rule.

If any of this appears in a public comment or Issue, the Custodian will apply the most restrictive GitHub visibility control available (hide, mark off-topic, lock, redact as the surface allows) and notify the Release Approver. The material is **not** reproduced in replies, titles, or commit messages.

**Note on GitHub visibility controls.** Visibility actions do not erase notifications already sent, forks or clones already made, cached copies, or prior third-party access. If sensitive material was briefly exposed, we treat that as an incident and follow the Privacy Notice and Charter — not as a situation that visibility controls alone can undo.

---

## 5. Related documents

- Privacy inquiries → `privacy@agenticprocess.org`, [Consultation Privacy Notice](https://agenticprocess.org/privacy).
- Code of Conduct → [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), reports to `conduct@agenticprocess.org`.
- Operational security of the repository (Actions, Apps, workflows) → [`SECURITY-AUTOMATION.md`](SECURITY-AUTOMATION.md).

---

*This policy applies to the repository `github.com/agenticprocessprotocol/spec` and the Specification documents it contains. It does not apply to vendor implementations.*
