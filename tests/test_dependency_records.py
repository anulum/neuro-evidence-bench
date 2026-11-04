# SPDX-License-Identifier: AGPL-3.0-or-later
# Commercial license available
# © Concepts 1996–2026 Miroslav Šotek. All rights reserved.
# © Code 2020–2026 Miroslav Šotek. All rights reserved.
# ORCID: 0009-0009-3560-0851
# Contact: www.anulum.li | protoscience@anulum.li
# NEURO-EVIDENCE-BENCH — actual closed dependency provenance input tests

"""Read real package observations and refuse malformed or unbound declarations."""

import json
from pathlib import Path

import pytest

from bench_validation.dependency_records import read_provenance
from bench_validation.report import Refusal
from tests.native_process import run_isolated_program

REPOSITORY = Path(__file__).resolve().parents[1]


def test_actual_record_shapes_and_custom_source_bindings() -> None:
    """Read actual observations, retaining the upstream-only licence source."""
    source, records = read_provenance(REPOSITORY)
    assert source["python_version"] == "3.15.2"
    assert {row["name"] for row in records} >= {"ruff", "uv", "mypy", "jsonschema"}
    upstream = [row for row in records if row.get("license_source")]
    assert {row["name"] for row in upstream} == {"packageurl-python"}
    assert all(
        row["license_expression"] == row["license_source"]["detected_spdx"] for row in upstream
    )


def test_custom_licence_retains_actual_installed_text(tmp_path: Path) -> None:
    """Accept a custom identity bound to the actual installed licence record."""
    source = json.loads((REPOSITORY / "dependency-provenance.json").read_text())
    row = next(row for row in source["packages"] if row["license_evidence"])
    expected = row["license_evidence"]
    row["license_expression"] = "LicenseRef-installed-" + row["name"]
    (tmp_path / "dependency-provenance.json").write_text(json.dumps(source))
    _, records = read_provenance(tmp_path)
    actual = next(record for record in records if record["name"] == row["name"])
    assert actual["license_expression"] == row["license_expression"]
    assert actual["license_evidence"] == expected


@pytest.mark.parametrize("fault", ["shape", "duplicate", "canonical", "licence", "licence_source"])
def test_actual_record_refusals(tmp_path: Path, fault: str) -> None:
    """Refuse altered real observations without exposing declaration contents."""
    source = json.loads((REPOSITORY / "dependency-provenance.json").read_text())
    if fault == "shape":
        source["unknown"] = "CONFIDENTIAL_PAYLOAD"
        expected = "dependency.records"
    elif fault == "duplicate":
        source["packages"].append(source["packages"][0])
        expected = "dependency.names"
    elif fault == "canonical":
        source["packages"][0]["name"] = source["packages"][0]["name"].upper()
        expected = "dependency.names"
    elif fault == "licence":
        source["packages"][0]["license_expression"] = "MIT AND ???"
        expected = "dependency.licence"
    else:
        row = source["packages"][0]
        row["license_expression"] = "LicenseRef-installed-" + row["name"]
        row["license_evidence"] = []
        row.pop("license_source", None)
        expected = "dependency.licence_source"
    (tmp_path / "dependency-provenance.json").write_text(json.dumps(source))
    with pytest.raises(Refusal) as caught:
        read_provenance(tmp_path)
    assert caught.value.finding.code == expected
    assert "CONFIDENTIAL_PAYLOAD" not in caught.value.finding.message


def test_real_missing_provenance_libraries() -> None:
    """Invoke the public reader in an actual interpreter without site packages."""
    program = """
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from bench_validation.dependency_records import read_provenance
from bench_validation.report import Refusal
try:
    read_provenance(Path(sys.argv[2]))
except Refusal as error:
    print(error.finding.code)
    sys.exit(error.finding.exit_code)
"""
    result = run_isolated_program(program, str(REPOSITORY / "tools"), str(REPOSITORY))
    assert result.returncode == 3
    assert result.stdout.strip() == "dependency.tool"
    assert result.stderr == ""
