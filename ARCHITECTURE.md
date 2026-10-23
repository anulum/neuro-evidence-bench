<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
NEURO-EVIDENCE-BENCH — repository governance and provenance
-->

# Architecture

The current executable surface validates this repository's metadata, source, workflow policy, development dependencies, rendered documentation and inventory. Fixed Python entry points under tools/bench_validation produce scoped infrastructure reports; received files cannot select an executable or weaker policy. Inventory generation follows accepted metadata and writes a new exclusive output. Read-only verification never repairs input.

Planned benchmark work owns a prior run plan, metric and provenance definitions, executor integration, result assembly, comparison and an independently followable rerun procedure. A prior plan identifies existing model, data and configuration inputs; it cannot name future output. Every required metric remains visible, including failures and unavailable observations.

~~~mermaid
flowchart LR
  S[Existing workload and metric policy] --> P[Prior plan]
  P --> E[Accepted execution provider]
  E --> O[Owning observation artefacts]
  O --> R[Complete immutable result]
  P --> R
  R --> V[Verification comparison and new rerun]
~~~

That benchmark graph is planned, not implemented by the current repository validators. EVIDENCE-MANIFEST-TOOLKIT owns common sealing and trust; instruments own actual observations; EXPERIMENT-LEDGER owns record storage. This repository owns no second signing root, instrument implementation or authoritative result database.

Read the [component guide](docs/ARCHITECTURE.md), [trust boundaries](docs/THREAT_MODEL.md) and [validation commands](VALIDATION.md).
