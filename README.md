<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
NEURO-EVIDENCE-BENCH — repository governance and provenance
-->

# NEURO-EVIDENCE-BENCH

NEURO-EVIDENCE-BENCH defines a boundary for auditable benchmark plans, evidence-backed results and independent reruns. The current implementation provides repository validation tooling. Benchmark execution, metric collection, result assembly and comparison remain planned; no benchmark runtime or measured capability is installed.

The local metadata explicitly records `local_scaffold`, `architecture_only`, empty capabilities, claims and qualified schemas. The planned identifiers `neuro_evidence_bench.plan.v1` and `neuro_evidence_bench.result.v1` are declarations. Neither format is registered or accepted by this tooling.

## Validate repository metadata

Use Python 3.15.2 with the hash-locked development dependencies:

```sh
uv venv --python 3.15.2 .venv
uv pip install --python .venv/bin/python --require-hashes --build-constraints requirements-dev.txt --default-index https://pypi.org/simple -r requirements-dev.txt
make native-tools
.venv/bin/python tools/check_repository_metadata.py --root . --json
```

The metadata checker binds the exact reviewed schema, expected repository identity, governing profile, running interpreter and raw development lock. A metadata pass covers that operation only. Repository inventory verification additionally requires the complete initial path contract.

Read [validation](VALIDATION.md), [architecture](ARCHITECTURE.md), [contribution instructions](CONTRIBUTING.md) and [support](SUPPORT.md). The [roadmap](ROADMAP.md) distinguishes planned domain work from implemented tooling.

## Planned metric alignment

The design acknowledges [NeuroBench](https://github.com/NeuroBench/neurobench) as a reference for benchmark methodology. Its [model footprint](https://neurobench.readthedocs.io/en/latest/metrics/static_metrics/model_footprint.html), [connection sparsity](https://neurobench.readthedocs.io/en/latest/metrics/static_metrics/connection_sparsity.html) and [activation sparsity](https://neurobench.readthedocs.io/en/latest/metrics/workload_metrics/activation_sparsity.html) have distinct definitions and populations. No implementation or dataset is copied. Alignment and any deviations require explicit source-bound verification before a compatibility claim.

## Licence and contact

AGPL-3.0-or-later applies; see [LICENSE](LICENSE) and [NOTICE](NOTICE.md). Commercial licensing is available through [ANULUM](https://www.anulum.li), protoscience@anulum.li. No hosted repository, deployment, release, badge, DOI or certification is asserted by this local source tree.

![ANULUM](docs/assets/anulum_logo_company.jpg)

![Fortis Studio](docs/assets/fortis_studio_logo.jpg)

The reservation below was issued on 2026-10-19 and added to this repository on 2026-10-23.

## Text and data mining reservation

The rightsholder, Miroslav Šotek (ANULUM), expressly reserves the use of the
works in this repository for text and data mining, including the collection of
this content for, and its use in, training, fine-tuning or evaluating machine
learning and artificial intelligence models, in accordance with Article 4(3) of
Directive (EU) 2019/790 and the national provisions transposing it.

No permission for such use has been granted beyond what the licence in
`LICENSE` grants. This reservation does not change that licence: uses the
licence permits remain permitted on its terms, including its attribution and
share-alike conditions.

Reservation made on 2026-10-19. Requests for permission: contact the
rightsholder through the contact listed in this repository.
