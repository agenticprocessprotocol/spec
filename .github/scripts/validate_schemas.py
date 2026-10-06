#!/usr/bin/env python3
"""validate_schemas.py — schema integrity under /schemas/.

Checks:
  * Every schema file (schemas/**/*.json except files under examples/)
    is valid JSON and declares `"$schema": "https://json-schema.org/draft/2020-12/schema"`.
  * The schema itself passes 2020-12 meta-schema validation.
  * Every file under examples/ (siblings of the schema) VALIDATES against
    the schema.
  * Every file under examples/invalid/ FAILS validation against the schema.
  * Published version directories (schemas/<name>/<version>/) are
    immutable: on a pull_request, no file inside such a directory may
    have changed vs the base commit (except in a PR that creates the
    directory).
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import ROOT, Reporter, iter_schema_files, main_guard

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover - CI should install deps
    print(f"::error title=schemas::jsonschema package not installed: {exc}", file=sys.stderr)
    sys.exit(2)


EXPECTED_SCHEMA_URI = "https://json-schema.org/draft/2020-12/schema"


def _validate_meta(schema_doc: dict) -> list[str]:
    try:
        Draft202012Validator.check_schema(schema_doc)
        return []
    except Exception as exc:  # jsonschema raises SchemaError
        return [f"meta-schema check failed: {exc}"]


def _validate_examples(schema_path: pathlib.Path, schema_doc: dict, r: Reporter) -> None:
    schema_dir = schema_path.parent
    valid_dir = schema_dir / "examples"
    invalid_dir = schema_dir / "examples" / "invalid"
    validator = Draft202012Validator(schema_doc)

    if valid_dir.is_dir():
        for ex in sorted(valid_dir.glob("*.json")):
            # Skip files under examples/invalid/.
            if invalid_dir in ex.parents:
                continue
            try:
                data = json.loads(ex.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                r.error(f"example is not valid JSON: {exc}", file=ex)
                continue
            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if errors:
                summary = "; ".join(f"{list(e.path)}: {e.message}" for e in errors[:3])
                r.error(f"valid-example failed validation: {summary}", file=ex)

    if invalid_dir.is_dir():
        for ex in sorted(invalid_dir.glob("*.json")):
            try:
                data = json.loads(ex.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                # Invalid JSON is fine for an "invalid" example — it's trivially non-conformant.
                continue
            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if not errors:
                r.error("invalid-example PASSED validation (should fail)", file=ex)


def _check_immutable_published_versions(r: Reporter) -> None:
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    base = os.environ.get("BASE_SHA", "")
    if event != "pull_request" or not base:
        return

    try:
        changed = subprocess.check_output(
            ["git", "diff", "--name-only", base, "HEAD", "--", "schemas/"],
            cwd=ROOT, text=True,
        ).splitlines()
    except subprocess.CalledProcessError:
        return

    for rel in changed:
        if not rel.strip():
            continue
        # schemas/<schema_name>/<version>/...  — a version dir is immutable
        # once it exists on main. Detect by checking that the directory
        # existed in the base ref.
        parts = pathlib.PurePosixPath(rel).parts
        if len(parts) < 3:
            continue
        _, _, version = parts[0], parts[1], parts[2]
        version_dir = pathlib.PurePosixPath(parts[0], parts[1], version)
        # Was this version dir present in base?
        try:
            subprocess.check_output(
                ["git", "cat-file", "-e", f"{base}:{version_dir}"],
                cwd=ROOT, stderr=subprocess.DEVNULL,
            )
            existed = True
        except subprocess.CalledProcessError:
            existed = False
        if existed:
            r.error(
                f"schemas/{parts[1]}/{version}/ is published and must not be modified; create a new version directory instead",
                file=ROOT / rel,
            )


def _run() -> int:
    r = Reporter("schemas")
    schemas = iter_schema_files()
    if not schemas:
        print("schemas: no schema files found; nothing to validate")
        return r.finish()

    for sp in schemas:
        try:
            schema_doc = json.loads(sp.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            r.error(f"schema is not valid JSON: {exc}", file=sp)
            continue
        if not isinstance(schema_doc, dict):
            r.error("schema top level must be an object", file=sp)
            continue
        if schema_doc.get("$schema") != EXPECTED_SCHEMA_URI:
            r.error(f"schema must declare \"$schema\": \"{EXPECTED_SCHEMA_URI}\"", file=sp)
            continue
        for err in _validate_meta(schema_doc):
            r.error(err, file=sp)
            continue
        _validate_examples(sp, schema_doc, r)

    _check_immutable_published_versions(r)
    return r.finish()


if __name__ == "__main__":
    sys.exit(main_guard(_run))
