# Methods and version history

This repository exposes the public research-software layer of a staged Canadian drill-core workflow. The frozen scientific lineage is intentionally preserved rather than silently overwritten as source quality improves.

## v0.1.1 FINAL — source readiness and provenance

Purpose: establish a traceable source foundation before interpretation or modelling.

Key steps:
- inventory assessment reports and regional datasets;
- retain original source identifiers, document/page provenance, units and qualifiers;
- define relational tables, vocabularies and QC rules;
- establish a 10-hole benchmark set;
- incorporate U-17-02 so all benchmark holes have local primary-source evidence.

## v0.2 RC2 — PDF-derived interval reconstruction and QC

Purpose: reconstruct the defensible drill-hole information available from supplied public reports without inventing missing precision.

Outputs:
- 403 lithology/geological intervals;
- 453 assay-sample records;
- 1,527 assay-result rows;
- 11 downhole survey records;
- 84 repeat/QC groups.

Important rules:
- visible source truncation is retained as truncation;
- censored results such as `<5` retain qualifier and detection-limit semantics;
- assay repeats and QA/QC rows are not collapsed silently;
- image-only DL14 analytical certificates are not populated by unverified bulk OCR.

## v0.3.1 — regional integration

The drill-core benchmark was linked to Disraeli and Seagull regional intrusion-system context. MRD308 whole-rock geochemistry, isotope context and nearby mineral-inventory/deposit information were integrated in a provenance-aware regional layer.

Headline state: 121 canonical regional whole-rock samples and 8,486 regional geochemical results. Existing system-level summary metrics were independently reproduced as a QC check.

## v0.3.2 — geochemical harmonization

A common analytical layer was built across regional and drill-core datasets. Shared analytes include Ni, Cu, Co, Au, Pd and Pt. Au/Pd/Pt are standardized to ppb in the common layer while raw values and raw units remain preserved.

Censored observations are retained explicitly and no half-detection-limit substitution is used in the primary harmonization. Unit compatibility is not treated as proof of analytical-method equivalence.

Headline state: 10,013 harmonized analytical records, including 493 censored results.

## v0.3.3 — interval-geochemistry integration

Exact sample intervals were linked to lithology intervals. The workflow distinguishes complete single-lithology coverage from boundary-crossing samples rather than forcing all samples into one geological unit.

Headline state:
- 345 exact sample-lithology assignments;
- 336 within one primary lithology;
- 9 crossing a primary lithology boundary;
- 167 samples meeting the strongest exact-depth + exact-lithology + common-geochemistry integration state.

## v0.3.4 — measured-depth downhole context

The strongest integrated subset was examined downhole using measured depth only. Regional empirical percentiles, response classes, touching/overlapping response clusters and lithology-package summaries were generated.

This stage deliberately avoids unsupported 3-D trajectory interpretation where station-by-station survey data are incomplete.

Headline state: 167 exact integrated samples across DL-21-004, SN12-01, SN12-02, U-17-01 and U-17-02.

## v0.3.5 — cross-hole synthesis

Cross-hole comparison rules separate same-method concentration comparison from broader unit-harmonized contextual comparison. A tiered comparability framework prevents apparent numerical similarity from being treated automatically as analytical equivalence.

Observed patterns are descriptive sampled-subset findings, not deposit-fertility probabilities.

## v0.3 FINAL

Frozen integration release:
- 10 benchmark holes;
- 403 lithology intervals;
- 453 assay samples;
- 1,527 assay results;
- 121 regional samples;
- 8,486 regional geochemical results;
- 10,013 harmonized records;
- 345 exact sample-lithology assignments;
- 167 exact integrated downhole samples across 5 holes.

No hole is treated as fully validated for complete 3-D trajectory work.

## v0.4.1 — benchmark design frozen before model fitting

Two classification tasks were declared in advance.

### T1 — Seagull lithology
- holes: SN12-01 and SN12-02;
- labels: gabbroic, diabase, mafic intrusive;
- primary predictors: log10 Ni, Cu and Co;
- whole-hole transfer only.

### T2 — Disraeli/Caro Lake magnetite-skarn
- holes: U-17-01 and U-17-02;
- labels: magnetite skarn vs non-skarn;
- primary predictors: log10 Ni, Cu and Co;
- whole-hole transfer only.

Hole/source IDs, depth/location, lithology text, analytical-method labels and assay-derived response fields are excluded from the primary predictor panel.

## v0.4.2 — fixed baseline models

Models were fixed without tuning against held-out holes:
- prior dummy classifier;
- standardized balanced logistic regression;
- balanced random forest.

The drill hole is the independent validation unit. Headline performance therefore uses the equal-hole mean of fold metrics rather than allowing the longer/more densely sampled hole to dominate the summary.

Primary equal-hole mean balanced accuracy:
- T1: dummy 0.333; logistic 0.574; random forest 0.510;
- T2: dummy 0.500; logistic 0.689; random forest 0.814.

The strict T2 single-lithology sensitivity subset yields approximately 0.897 for the random forest, but only three Tier-B samples are removed. This is treated as small-n sensitivity rather than a general performance claim.

## v0.4 FINAL — interpretation

T1 is a preliminary, fold-sensitive lithogeochemical signal rather than a robust lithology classifier. T2 is a more consistent baseline result in this limited dataset, but analytical method changes with hole, so it represents combined geological + analytical domain transfer.

No v0.4 model is validated for ore targeting, deposit ranking, prospectivity ranking, probability of mineralization, generalized 3-D prediction or causal interpretation of feature importance.
