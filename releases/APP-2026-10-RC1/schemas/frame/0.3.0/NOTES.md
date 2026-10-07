# APP Process Frame Schema — v0.3.0 Notes (APP-R1 Illustrative Reference)

**Designation:** APP-R1 Illustrative Reference. Non-normative.
**Status:** Reference realisation of the CORE-A1-05 published Frame schema requirement; implementations may deliver equivalent conformance via other schema realisations. Supersedes v0.2.0 Draft.
**Derived from:** APP-2026-10-RC1 coordinated baseline — APP-2 §3.1–3.3, §3.5–3.6, §3.9–3.10, §6; APP-3 §4.1, SEC-S6-01, App. B; APP-4 §3.1.
**Files:** `frame.schema.json` (JSON Schema 2020-12) · `examples/frame.example.json` · `examples/invalid/` (20 cases) · `validate_harness.py`.
**Test evidence:** harness evidence only (structural subset plus semantic checks): the example passes and all 20 invalid cases fail for the intended reason. Re-run with a standard validator (ajv or python-jsonschema, format assertion enabled) before external reliance. Not evidence of APP conformance.

## 1. Changes from 0.2.0

| Change | Reason |
|---|---|
| APP-R1 Illustrative Reference designation adopted; T3-Internal label retired | Aligns with the three-tier APP corpus taxonomy (normative APP-0..5 / informative APP-IG-01..05 / illustrative-reference APP-R*); clarifies non-normative status so implementations may deliver equivalent conformance via other schema realisations |
| `schema_version` bumped 0.2.0 → 0.3.0; `$id` URL and top-level `description` updated to match | Reflects designation change |
| No field, enum, allOf, or structural edits | Round 3 IP review (2026-10-07) confirmed the schema as drafted is correctly attributed to its APP-2 anchors and discloses no Z2 claim-scope content from 148514-0103/0104/0105 or TS-D-31B/32B/36B/55B retained TS content. Semantic distinctions flagged in parallel review (run vs step identity; governance_classification vs mutation-impact; compliance joint-state legality) are resolved without schema change — APP-2 §3.5/§3.6 and CORE-A1-02 anchors already provide correct scope |
| Derivation pinned to coordinated baseline APP-2026-10-RC1; prior per-document version refs (APP-2 v5.11, APP-3 v3.13, APP-4 v2.3) retired from the pin line | Follows the APP site's coordinated-baseline discipline: cross-document references cite the baseline, not individual document versions, to eliminate stale-pointer defects across updates |

## 2. Changes from 0.1.0 (historical)

| Change | Reason |
|---|---|
| Added required `lifecycle_state` (seed · observed · validated · mature) | CORE-A9-01 is a Frame lifecycle RO; 0.1.0 omitted it |
| `app_baseline` required, pattern-checked | Consumers must know which APP semantics apply |
| Provenance: `recorded_at` required; `prior_link_digest` required after `create`, forbidden on `create`; `create` must be sequence 1; sequence contiguous | SEC-S1-02 "every mutation is a verifiable link" was not structurally represented |
| Signature `canonicalization` required, pinned to RFC 8785 (JCS); signature scope and link target defined | Signatures were unverifiable across validators |
| `trustBoundaryType` on the Frame renamed `expected_trust_boundary_type` | The PxER field records observed context; the Frame may only declare an expectation |
| A step with any compliance constraint cannot set `compliance_scoped: false`; example corrected | 0.1.0 example was internally contradictory |
| `source_provenance[].registered_at` required | SEC-S1-04 hash registration |
| `principal_ref.display_name` removed | Non-authoritative text inside a signed identity object |
| Descriptions: `hitl` is configuration, not A6 evidence; `orchestration.mode` grounded in CORE-A4-04 with step semantics; EC-01a and EC-39 noted on `entity_extract` | Prevents overclaiming |
| Harness checks `date-time`/`date` format | JSON Schema 2020-12 treats `format` as annotation by default |

## 3. Review items not adopted

| Proposal | Why not |
|---|---|
| Split `C3C4` into C3 and C4 | APP-2 §6 defines a four-point ordinal whose fourth point is **C3C4**; C0–C4 is the informative IG-03 authorship model |
| Richer degradation enum | CORE-XX-01 specifies exactly "fail-closed or fail-open" for C2 steps |
| Different `completion_gate` vocabulary | `none` · `review` · `attestation` is verbatim CORE-A4-05 |
| Typed DAG edges | CORE-A0-01 requires a dependency chain only; DAG-JSON (A0-03) is a Reference Mechanism |
| Extra recovery-authorisation field | CORE-A4-06 intent layer is Frame version plus recovery-policy reference; both present |
| Extension envelope with critical flag; open objects | Adds an interoperability contract with no current second implementer. Closed core with reversed-domain `extensions` retained; evolution rule in §4 |
| Tenant namespace for entity types | EC-03 is a Recommended Pattern; deferred |
| Five-module schema split; formal S1/S2/S3 validation documents; diagnostic code registry | Standards-engineering work for the WG, not needed for a draft artefact |
| Typed references for constraints, principals, promotion evidence | Choices without a current interoperability need; deferred |

## 4. Traceability

"Outcome" names the APP requirement; "Name" says whether the field name comes from the corpus or is a schema Choice.

| Field | Outcome | Name |
|---|---|---|
| `frame_id`, `frame_version` (integer) | CORE-A1-05; SEC-S1-03 monotonic versioning | Choice |
| `lifecycle_state` | CORE-A9-01 | Values: corpus |
| `intent.authored_by`, `intent.approval` | CORE-A4-01 intent layer | Choice |
| `orchestration.mode`, `orchestration.completion_gate` | CORE-A4-04; CORE-A4-05 (RP) | Choice; values corpus |
| `compliance_scoped` (Frame, step) | SEC-S6-01 absence check | Choice |
| `source_provenance[]` | SEC-S1-04 | Choice |
| `provenance[]` | SEC-S1-02, S1-03; CORE-A1-02 | Choice; classification values corpus |
| `signature` | SEC-S1-01; APP-3 App. B | Choice (JCS pinned here) |
| `steps[].step_id`, `executing_system`, `depends_on`, `accountability_owner` | CORE-A0-01 | Choice |
| `steps[].dp_classification_intended` | CORE-A0-01, A3-01 | Corpus |
| `steps[].p_level` | CORE-A3-04 | Choice |
| `steps[].classification_provenance` | CORE-A8-01/02, applied to D steps and `permanent_P` (KI-05) | Values corpus |
| `steps[].compliance[]` | CORE-A5-01/02/03; APP-2 §6 | Values corpus |
| `steps[].degradation_behaviour` | CORE-XX-01 | Choice; values corpus |
| `steps[].hitl` | CORE-A0-02, A6-04 (RP configuration) | Choice |
| `steps[].entity_extract[]` | APP-4 EC-01/02 | Corpus |
| `executing_system.expected_trust_boundary_type` | CORE-A2-03 vocabulary | Choice |
| `autonomy_mode`, `recovery_policy_ref`, `d_potential`, `promotion_target`, `sla`, `integration_level` | SEC-S6-03; CORE-A4-06; A0-02; APP-2 §4 | Choice |

## 5. Validation layers and evolution

1. **Structural** (`frame.schema.json`): shapes, enums, conditional rules. Validators MUST enable format assertion.
2. **Semantic** (harness ✓ where implemented): ✓ unique step IDs, resolvable and acyclic `depends_on`; ✓ contiguous provenance from `create`, last entry matches `frame_version`, backward version only via rollback; ✓ compliance-scoped steps carry a constraint; A5-03 no silent weakening; EC-01a `entity_extract` changes increment the version (cross-version check).
3. **Runtime** (outside the schema): signature and `prior_link_digest` verification, key resolution; consumer rejects versions below last-applied (SEC-S1-03); EC-39 field-path minimisation review.

Evolution rule for drafts: minor versions add optional fields only; any new required field or changed enum is a major version. Consumers validate against the `schema_version` the Frame declares.

## 6. Next test against Vach architecture

The architecture review found one Vach-side naming drift (`earned_design` vs APP `extracted_design`) to correct on the Vach side. No other architecture field maps to an APP Required Outcome missing from 0.2.0.
