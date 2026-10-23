<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
NEURO-EVIDENCE-BENCH — repository governance and provenance
-->

# Validation tooling API

The metadata command accepts `--root` and `--json`. The inventory command additionally accepts `--mode generate|verify` and requires `--output` only for generation. All commands emit safe structured JSON. Exits are 0 for the requested scope, 2 for refusal, 3 for unavailable required inputs or tools, and 4 for invalid invocation or configuration.

Metadata validation accepts no generated inventory dependency. Inventory generation publishes deterministic new bytes; verification requires the canonical inventory and complete initial paths. A successful operation does not qualify metric correctness, measured origin or benchmark comparability or establish release readiness.

## Metadata acceptance

::: bench_validation.metadata.validate_metadata

## Finite input

::: bench_validation.inputs.read_file

::: bench_validation.inputs.read_json

## Capability inventory

::: bench_validation.capabilities.inventory_bytes

::: bench_validation.capabilities.create_inventory

::: bench_validation.capabilities.validate_capabilities

## Diagnostics

::: bench_validation.report.Finding

::: bench_validation.report.Report

## Command interfaces

::: bench_validation.cli.metadata_main

::: bench_validation.cli.inventory_main

## Source ownership and maintained tree

::: bench_validation.provenance.validate_notice

::: bench_validation.provenance.validate_provenance

::: bench_validation.structure.maintained_paths

::: bench_validation.structure.validate_structure

## YAML and workflow policy

::: bench_validation.yaml_input.read_yaml

::: bench_validation.workflows.validate_workflows

## Complete dependency observations

Release candidates and observed installed metadata are separate records. The hash lock covers the entire selected development graph. Exact source-builder constraints also use that lock. Recorded installation RECORD hashes are observations; relocated entry-script paths prevent treating them as universal build identities. Custom licence references retain exact source terms and do not infer permissions.

::: bench_validation.dependency_lock.parse_direct

::: bench_validation.dependency_lock.parse_lock

::: bench_validation.dependency_records.Artifact

::: bench_validation.dependency_records.LicenseEvidence

::: bench_validation.dependency_records.LicenseSource

::: bench_validation.dependency_records.PackageRecord

::: bench_validation.dependency_records.read_provenance

::: bench_validation.dependencies.verify_records

::: bench_validation.dependencies.verify_installed

::: bench_validation.dependencies.verify_configuration

::: bench_validation.dependencies.validate_dependencies

::: bench_validation.native_tools.verify_native_tools

## Actual documentation rendering

::: bench_validation.documentation.References

::: bench_validation.documentation.render_markdown

::: bench_validation.documentation.inspect_markdown

::: bench_validation.documentation.build_site

::: bench_validation.documentation.inspect_projection

::: bench_validation.documentation.validate_documentation

## Tool completion and scoped preflight

Every tool uses a fixed absolute executable, literal arguments and a finite deadline. Actual exits survive communication errors where observed. Output limits apply to accepted completed output; the caller reserves process memory separately. A named preflight subset reports its narrower scope. The complete operation requires the entire compiled profile. Missing tools, invalid protocol and native failures retain their real states.

::: bench_validation.execution.ToolResult

::: bench_validation.execution.run_tool

::: bench_validation.preflight.Check

::: bench_validation.preflight.Outcome

::: bench_validation.preflight.PreflightReport

::: bench_validation.preflight.validate_checker_report

::: bench_validation.preflight.run_check

::: bench_validation.preflight.run_checks

::: bench_validation.preflight.source_payload

::: bench_validation.validation_profile.scaffold_checks

::: bench_validation.preflight_cli.preflight_main

## Shared command and protocol interfaces

::: bench_validation.inputs.parse_json

::: bench_validation.report.Refusal

::: bench_validation.cli.Parser

::: bench_validation.cli.check_main

::: bench_validation.cli.emit_report

::: bench_validation.ci_dependencies.verify_ci_dependencies

## Native workflow composition

The coordinator executes the eight complete native jobs from the maintained workflow sources. Each of four category gates requires every actual descendant result, and the stable required gate checks all four category results. The workflow policy verifies exact job equality with each source and rejects missing descendants, masked outcomes, altered commands and workflow calls. This preserves all category checks without depending on an unsupported reusable-workflow syntax. Both native syntax and unchanged pedantic workflow checks inspect the actual executable configuration; no projected input or suppressed finding is used.
