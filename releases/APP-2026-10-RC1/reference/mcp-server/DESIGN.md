# APP A1 Integration Surface — MCP Binding Reference Design

**Designation:** APP-R2 Illustrative Reference. Non-normative.
**Version:** 0.3 Draft (supersedes 0.2 Draft) · **Status:** Informative. Not part of the APP Specification. Creates no conformance obligation and makes no conformance claim.
**Repository path:** `/reference/mcp-server/DESIGN.md` · **Licence:** Apache-2.0, per `agenticprocess.org/#governance`.
**APP sources:** APP-2026-10-RC1 coordinated baseline.
**MCP sources checked:** specification revision 2026-07-28 and its changelog (`modelcontextprotocol.io/specification/2026-07-28/changelog`); extensions overview (`modelcontextprotocol.io/extensions/overview`).

## 0. Changes from 0.2 Draft

| Change | Reason |
|---|---|
| APP-R2 Illustrative Reference designation adopted; T3-Internal tier retired; internal pre-publication release note removed | Aligns with the three-tier APP corpus taxonomy (normative APP-0..5 / informative APP-IG-01..05 / illustrative-reference APP-R*); the pre-publication IP screen that the removed note cued was completed before release |
| Extension identifier `org.agenticprocess/app` placeholder language removed; current interim custodial status referenced via `agenticprocess.org/#governance` | agenticprocess.org publishes Vach AI Limited (DIFC) as interim custodian pending AAIF handover; the identifier is backed by a real domain, not a placeholder |
| §5.4 wording clarified: "session-scoped identity token reference" → "run-scoped session identity reference per SEC-S13-01"; bullet reworded to match | Removes a drafting ambiguity between run-level and step-level identity scope while adding no new signposting; step-level admission mechanics remain governed by APP-2 §3.5 as published |
| Licence line simplified: now cites `agenticprocess.org/#governance` directly | Apache-2.0 for code and schemas is published at the site; no need to replicate internally |
| APP sources pinned to coordinated baseline APP-2026-10-RC1; prior per-document version refs (APP-2 v5.11, APP-3 v3.13, APP-5 v1.8) retired from the pin line | Follows the APP site's coordinated-baseline discipline: cross-document references cite the baseline, not individual document versions, to eliminate stale-pointer defects across updates. Register D-03 retarget action closed. |

---

## 1. Purpose and claim boundary

APP-2 names MCP as a Recommended Pattern transport for the A1 integration surface (CORE-A1-04) but does not define how APP concepts map onto MCP primitives. This document proposes that mapping for one reference component.

**Claim boundary.** This is the intended design. Coverage statements below are *intended coverage of the declared scope, subject to implementation and test results*. No conformance is claimed until the APP-5 tests in §8 pass against a running implementation (APP-5 CONF-T-02), and no interoperability is claimed before a second independent implementation passes the same vectors (APP-1 Art. 5).

## 2. Binding status: what is APP and what is a reference choice

Every element below carries one of three statuses:

| Status | Meaning |
|---|---|
| **APP-RO** | Implements an APP Required Outcome as written. Not optional. |
| **APP-RP** | Implements an APP Recommended Pattern. |
| **Choice** | A reference-design choice. Another implementation may choose differently. |

Test for "Choice": if two implementations could choose differently and still interoperate, the element stays a Choice and is not proposed for standardisation. Elements that implementations *must* share to interoperate (extension identifier, wire fields, error meanings) are Choices today and are proposed for standardisation through the APP change route (register M-10). An informative design cannot make them binding.

## 3. Component position

This design is an **A1-facing component within a Governance Orchestrator (GO)**, not a GO. It does not claim GO conformance. A conformant GO also needs the components below; this component interfaces with them but does not specify them.

| Dependent GO component | APP requirements | Interface from this component |
|---|---|---|
| PxER assembly and query | CORE-A2-01, A2-03, A2-08a | Receives step contributions (§5.4); exposes read-only query (§5.4) |
| D/P classification | CORE-A3-*, SEC-S3 | Frame carries intended classification; this component does not classify |
| Accountability chain | CORE-A4-01 | Frame carries accountability owner; step records reference it |
| Compliance evaluation | CORE-A5-* | Frame carries compliance references; not evaluated here |
| HITL approval surface | CORE-A6-01–03, SEC-S5-01 | Checkpoint handle and evidence reference (§5.6) |
| Evidence verification and write-path audit | SEC-S4-01, S4-05 | Carries signed service provenance on writes; verification is GO-side |
| Independent signed trace | SEC-S7-01 | None; the trace must be independent of this component |
| Entity correlation | APP-4 | Passes `entity_refs` through (§5.4); no inference |
| Severe-event detection | SEC-XX-05 | Receives safe-state instructions and enforces them at the surface (§5.8) |

## 4. Extension declaration and discovery

| Element | Value | Status |
|---|---|---|
| Binding mechanism | Unofficial MCP extension; third-party extensions use a reversed domain owned by the author | Choice |
| Identifier | `org.agenticprocess/app` (prefix owned by the `agenticprocess.org` domain; current interim custodian published at `agenticprocess.org/#governance`) | Choice |
| Advertised in | `ServerCapabilities.extensions`, returned by `server/discover` | Choice (MCP-mandated RPC) |

Settings object (Choice):

```json
{
  "org.agenticprocess/app": {
    "appBaseline": "<tagged baseline>",
    "roles": ["governance-orchestrator"],
    "components": ["a1-mcp-binding"],
    "conformanceDeclarations": [{ "scope": "<scope-id>", "profile": "<APP-5 profile>", "lLevel": "L2" }],
    "partialConformance": ["<requirement IDs not implemented>"],
    "frameSchema": "app://schemas/frame/<version>",
    "contributionSchema": "app://schemas/contribution/<version>",
    "agentCardStandard": "<declared per CORE-A1-06>"
  }
}
```

The settings **support** the declarations CORE-CP-01 and CORE-CP-04 require (APP-RO) by making them discoverable. Discovery alone does not demonstrate that declarations are honoured; T-GOV-13 does.

## 5. Primitive mapping

### 5.1 Outbound: consume the Frame

| APP artefact | MCP primitive | URI | Status | Source |
|---|---|---|---|---|
| Process Frame, versioned | Resource | `app://frames/{processId}/versions/{version}` | APP-RO (content); Choice (URI) | CORE-A1-01, A1-05, A0-01 |
| Step view | Resource template | `…/versions/{version}/steps/{stepId}` | Choice | CORE-A0-01 |
| Frame schema | Resource | `app://schemas/frame/{schemaVersion}` | APP-RO (must exist, discoverable) | CORE-A1-05 |
| Mutation provenance chain | Resource | `app://frames/{processId}/provenance` | APP-RO (content); Choice (URI) | SEC-S1-02 |

Rules:
- `cacheScope` is always `private` (tenant-scoped governance data). Choice.
- **Consumer obligation (APP-RO, SEC-S1-03):** a consumer rejects any Frame version lower than its last-applied version. The server's resources expose version and provenance so consumers can enforce this; the server cannot enforce it on their behalf.
- **Schema dependency:** CORE-A1-05 requires the schema to cover A0-01 fields plus A3, A4, A5 and SEC-S1-02 provenance attributes. Until published (register M-07), §5.1 is not testable.

### 5.2 Inbound: changes through the governance gate

**Method:** `org.agenticprocess/app/frame.submitChange` (Choice)

| Input | Purpose | Status / source |
|---|---|---|
| `processId` | Target Frame | Choice |
| `baseVersion` | Concurrency base for the proposed change | Choice (reference concurrency mechanism) |
| `changeType` | `forward` or `rollback` | Choice; `rollback` realises SEC-S1-03 |
| `change` | Proposed step changes with governance attributes | APP-RO (CORE-A1-02) |
| `scope` | `intra-system` · `cross-system` | APP-RO (CORE-A1-03) |
| `signature` | Detached signature over the canonical change | APP-RO (SEC-S1-01); canonicalisation open (register T-01) |

| Result | Values | Status / source |
|---|---|---|
| `classification` | `governance-complete` · `partial` · `absent` | APP-RO (CORE-A1-02) |
| `outcome` | `merged` · `routed-to-enrichment` · `flagged-for-review` · `requires-frame-mediation` · `requires-rollback-approval` | APP-RO (A1-02, A1-03, SEC-S1-03) |
| `newVersion` | Present when merged | Choice |

Rules:
- Unsigned or invalid submissions are rejected before classification (SEC-S1-01).
- `cross-system` changes never merge directly (CORE-A1-03).
- A `rollback` merges only with explicit governance approval; any backward transition without it is blocked (SEC-S1-03).
- Every merged change appends to the provenance chain with signer, authoriser and governance classification (SEC-S1-02).

### 5.3 Notification

MCP 2026-07-28 replaced `resources/subscribe` with `subscriptions/listen`. The component accepts `resourceSubscriptions` on Frame URIs and emits tagged change notifications on publication of a new version. Notifications carry no Frame content; consumers re-read, re-validate (CORE-A1-05) and apply the monotonic rule (SEC-S1-03). Status: APP-RO (pattern exists, CORE-A1-01); Choice (mechanism).

### 5.4 Governed runs and evidence contribution

MCP 2026-07-28 removed protocol-level sessions; cross-call state uses server-minted handles passed as arguments.

| Method | Purpose | Status / source |
|---|---|---|
| `…/run.open` | Opens a governed process instance against a Frame version; returns `runHandle` and a run-scoped session identity reference per SEC-S13-01 | Choice (handle); APP-RO (token content, SEC-S13-01) |
| `…/run.recordStep` | Contributes a step: CORE-A2-02 minimum fields, CORE-A2-03 conformance fields, and any PxER extension-point blocks | APP-RO (fields) |
| `…/run.contributeTelemetry` *(L3, optional)* | Contributor telemetry; recorded with `verification_status: pending` | APP-RO (SEC-S4-01, S4-03) |
| `…/run.close` | Marks the instance ended | Choice |
| Resource `app://runs/{runHandle}/steps` | Read-only query of recorded steps during and after the run | APP-RO (queryable, CORE-A2-01) |

Evidence rules:
- **Immutable on write.** Each contributed record is append-only and immutable when accepted, and queryable during execution. `run.close` changes instance status only; it is not the point at which evidence becomes immutable (CORE-A2-01).
- **Assembly boundary.** This component is the intake to the GO's PxER assembly (§3). It does not define assembly.
- **Write-path provenance.** Every write carries signed service provenance; verification against an independent audit log is GO-side (SEC-S4-05).
- **Extension points** (APP-2 §3.4.0), accepted as opaque blocks and attached to the step:

| Block | Populated by | When |
|---|---|---|
| `entity_refs` | Contributing system or GO correlation component | When `entity_extract` is declared on the Frame step (APP-4 EC-07/08/11) |
| `governance_events` | GO severe-event component | On a safe-state transition (SEC-XX-05) |
| `recovery_evidence` | Contributing system | When the step invoked a recovery path (CORE-A2-13/14) |

- The session identity reference is attached to records produced during the run (SEC-S13-01/02).
- OpenTelemetry trace context in `_meta` MAY be copied as a telemetry cross-reference; it is telemetry, not evidence (CORE-A2-06). Choice.

**Open translation:** mapping APP's "session" (SEC-S2-03, SEC-S13) onto a run handle is a proposed translation, not an established equivalence (register M-03).

### 5.5 Tool facade for generic MCP clients

Clients that do not declare the extension participate through tools calling the same handlers, so governance treatment is identical across invocation modes (CORE-A7-01, APP-RO). Tool names and annotations are Choices.

| Tool | Handler | Annotations |
|---|---|---|
| `app_get_step` | §5.1 step view | `readOnlyHint: true` |
| `app_submit_frame_change` | §5.2 | `readOnlyHint: false` |
| `app_open_run` / `app_record_step` / `app_close_run` | §5.4 | `readOnlyHint: false` |

No tool can approve, promote or elevate authority. A model-invoked proposal of an authority change is recorded as a proposal, never as an authorisation source (SEC-S13-03, APP-RO).

### 5.6 HITL checkpoints

When a Frame step requires human review:
1. `run.recordStep` for that step returns a task handle (MCP Tasks extension). Choice.
2. **Blocking (APP-RO, CORE-A6-01):** until the checkpoint resolves, the component rejects completion of the step and any `recordStep` for steps that depend on it.
3. **Evidence binding (APP-RO, CORE-A6-02/03):** on resolution, the step record references the HITL engagement record produced by the GO's approval surface, which carries decision, duration, evidence reviewed and the engagement-fidelity marker. This component carries the reference; it does not measure engagement.
4. Approvals happen on the GO's approval surface, not through the agent's MCP channel. MCP's Multi Round-Trip Requests pattern is not used, because an elicitation relayed through the agent's client does not meet SEC-S5-01 (approval surfaces generated from independently verified data).

### 5.7 Governance unavailable (CORE-XX-01)

When the governance layer is unavailable: C0/C1 steps fail closed; C2 steps follow the Frame-declared behaviour; C3/C4 steps may proceed with a governance-unavailable flag in the evidence record. Status: APP-RO.

### 5.8 Severe-event safe state (SEC-XX-05)

When the GO's severe-event component signals a severe governance-critical event for a run, delegation chain or agent:
- the component refuses every privileged method (`frame.submitChange`, `run.recordStep` for action steps, and tool equivalents) for the affected scope **before** the next privileged action is attempted;
- refusal persists until the GO signals a release condition defined by SEC-XX-05;
- the GO records the `governance_events` block; this component attaches it (§5.4).

Status: APP-RO. The signalling interface between GO and component is a Choice.

### 5.9 Errors (Choice)

MCP reserves `-32020` to `-32099` and leaves `-32000` to `-32019` implementation-defined.

| Code | Name | Trigger |
|---|---|---|
| -32010 | `AppSignatureInvalid` | SEC-S1-01, SEC-S2-01 |
| -32011 | `AppSequenceViolation` | SEC-S2-01 out-of-sequence |
| -32012 | `AppSchemaInvalid` | CORE-A1-05 |
| -32013 | `AppGovernanceUnavailable` | CORE-XX-01 fail-closed |
| -32014 | `AppAuthorityRejected` | SEC-S2-06, SEC-S13-03 |
| -32015 | `AppSafeStateActive` | SEC-XX-05 |
| -32016 | `AppCheckpointUnresolved` | CORE-A6-01 blocking |
| -32017 | `AppStaleVersion` | SEC-S1-03 |

Codes in the implementation-defined range can collide across implementations; standardising them is part of M-10.

## 6. Security binding

| APP requirement | Binding | Status | MCP 2026-07-28 note |
|---|---|---|---|
| SEC-S2-01 mutual TLS | Required on the Streamable HTTP endpoint | APP-RO | MCP does not require mTLS (register M-02). |
| SEC-S2-01 OAuth 2.1 with dynamic client registration | **DCR supported, as APP requires.** Client ID Metadata Documents also supported for MCP clients that prefer them. | APP-RO + Choice | MCP deprecates DCR but retains it for backward compatibility; APP change proposed (register M-01). |
| SEC-S2-01 proof-of-possession | DPoP (RFC 9449) | APP-RO | MCP is finalising DPoP adoption. |
| SEC-S2-01 drop unsigned or out-of-sequence messages | APP signature and per-run sequence number in request `_meta` (`org.agenticprocess/app/sig`, `…/seq`) | APP-RO (outcome); Choice (mechanism) | MCP has no message signing or sessions. |
| SEC-S2-03 signing with sequence numbers for stateful sessions | Applied to runs as the proposed session equivalent | Proposed translation | See register M-03. |
| SEC-S1-01/02/03 Frame signing, provenance, monotonic versions | §5.1–5.2 | APP-RO | — |
| SEC-S2-02 signed Agent Cards | Verifies signatures on consumed Agent Cards per the declared standard (A2A) | APP-RO | MCP defines no Agent Card (register M-05). |
| SEC-S13-01/02 session identity token | Reference bound to `runHandle`, attached and retained with run records | APP-RO | — |
| SEC-XX-01 activation ordering | `server/discover` does not advertise the extension until mTLS, token validation and signature verification are active | APP-RO (outcome); Choice (gate) | — |

## 7. Out of scope

Evidence assembly internals; evidence verification pipelines; HITL engagement measurement and approval-surface design; D/P classification; entity correlation inference; severe-event detection; promotion, drift and process intelligence (A8–A11); persistence, scaling, multi-tenancy, UI; A2A binding.

## 8. Tests, reports and milestones

### 8.1 APP-5 tests targeted (per APP-2026-10-RC1 baseline)

| Milestone | Delivers | APP-5 tests |
|---|---|---|
| **M0** Schemas (prerequisite) | Frame and contribution schemas published | Enables T-SPEC-07 |
| **M1** Discovery, outbound, notification | §4, §5.1, §5.3 | T-SPEC-01, T-SPEC-02 (outbound, notification), T-SPEC-07, T-GOV-13 |
| **M2** Inbound gate and Frame security | §5.2 | T-SPEC-02 (inbound), T-SPEC-03, T-SPEC-04, T-SEC-02 |
| **M3** Transport security | §6 | T-SEC-06, T-SEC-07, T-SEC-08, T-SEC-31, T-SEC-32 |
| **M4** Runs, checkpoints, degradation, safe state, parity | §5.4–5.8 | T-EVID-01, T-EVID-02, T-EVID-03, T-GOV-11 (MCP modes), T-GOV-15, T-SEC-53, T-SEC-60 |
| **M5** Interoperability | Second independent implementation, shared vectors | Required before any interoperability claim |

T-EVID tests exercise the GO's PxER; they pass only with the dependent components in §3.

### 8.2 Negative cases (reference-design additions, to propose to APP-5)

Stale Frame version accepted by a consumer; backward transition without rollback approval; cross-system change merged directly; invalid or missing signature; replayed request; request on a wrong or closed `runHandle`; evidence write without service provenance; step completion while a checkpoint is unresolved; privileged action while safe state is active; governance outage per criticality tier; recovery after outage.

### 8.3 Two separate reports

1. **MCP binding report:** behaviour against the pinned MCP revision (2026-07-28).
2. **APP obligations report:** APP-5 results for the declared component, role and L-level, against the pinned APP baseline.

Dates are set once the build team is in place. Suggested stack (Choice): TypeScript MCP SDK, Streamable HTTP, stateless JSON responses.

## 9. Open items

Tracked in the **APP Improvement Opportunities Register**: M-01 (DCR), M-02 (mTLS), M-03 (session translation), M-05 (Agent Card), M-07 (schemas), M-10 (binding route), T-01 (canonicalisation). D-03 (baseline) closed in v0.3 Draft.

## 10. Future path

If a second implementation adopts this binding, the WG can choose the route for making it interoperable: a normative APP-2 annex, an APP-5 binding profile, or an MCP Extensions Track SEP (register M-10). MCP requires at least one reference implementation in an official SDK before accepting an extension SEP.
