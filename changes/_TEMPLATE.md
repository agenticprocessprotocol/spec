# Change-Impact Manifest — APP-XXXX

<!--
This template is for NORMATIVE pull requests. Copy to
/changes/APP-<nnnn>.md, where nnnn is the originating normative-proposal
Issue number (or a monotonically-increasing counter if no originating
Issue exists).

The nine fields below correspond to APP-1 §4. The normative-keyword
validator will pass once any file matching /changes/APP-*.md exists; the
cross-reference and release-integrity validators do not inspect the
content of this file. The quality of the content is a human review
concern — your reviewers will read it carefully.

Delete this comment block before committing.
-->

**Originating issue:** #<issue number>
**Originating proposer:** <name or role; "editorial" is acceptable where no outside proposer exists>
**Target baseline (if known):** APP-YYYY-MM-RCn
**Change class:** <Modify / Add / Remove / Clarify (normative) / Replace>
**AI-authorship disclosure:** <per CONTRIBUTING.md §4>

---

## 1. Changed requirement IDs (with semantic delta)

For each requirement ID whose semantics change, state the delta.

- `<REQ-ID>` — current semantics: <summary of what is required today>. Proposed semantics: <what is required after this change>. Delta: <in one line, "strengthens from SHOULD to MUST" / "narrows applicability from X to X-under-Y" / "widens accepted mechanism from only-A to A-or-B" / etc.>

## 2. Affected normative documents

List every normative document (APP-0, APP-1, APP-2, APP-3, APP-4, APP-5) that this PR touches, with section numbers.

- APP-<n>: §<section>, …

## 3. Affected informative documents

List every informative document (APP-IG-01 through APP-IG-05) that must be updated to remain consistent.

- APP-IG-<nn>: §<section>, …

## 4. Cross-reference updates

List every forward and reciprocal cross-reference that must change. State both ends of each pair.

- APP-<n> §<x> now cites APP-<m> §<y>; reciprocal update required at APP-<m> §<y> to cite APP-<n> §<x>.

## 5. APP-5 applicability impact

For every changed requirement, state how APP-5 applicability changes (conformance profiles, maturity levels).

- `<REQ-ID>`: applicability change (if any), new/modified test criteria, new/modified test procedure.

## 6. Traceability impact (APP-IG-02 §7)

State how the Cross-Reference Matrix must be updated.

- Objective → Requirement updates: …
- Requirement → Test updates: …
- Section → Requirement updates: …

## 7. Test impact (new/amended APP-5 T-* IDs)

List each new or amended APP-5 test identifier.

- `T-<objective>-<nn>` — new / modified: <summary of test change>.

## 8. Migration impact

How should existing conformant implementations respond?

- Prior-baseline conformant implementations: <no change required | upgrade path described below>.
- Version-negotiation impact: <does this PR require a baseline bump? Does it introduce a feature flag?>.

## 9. Suite baseline regeneration

If this PR is baseline-bound, list the regeneration steps.

- Manifest file updates: `MANIFEST.md`, `manifest.json`.
- Release notes updates: `/releases/<baseline>/RELEASE-NOTES.md`.
- Changelog entry addition: `CHANGELOG.md`.
- Decision record: `/decisions/APP-DEC-XXXX.md`.

---

*Reviewers: see `/GOVERNANCE.md` §2.3 for the Normative Suite Control gate.*
