# v0.3 Scientific Synthesis — Regional, Geochemical and Downhole Integration

## 1. Purpose

Version 0.3 converts the PDF-derived drill-hole foundation into a geological/geochemical integration framework. The objective is not to generate exploration probabilities, but to establish a traceable analytical layer in which drill-core intervals can be compared with their regional geochemical context without losing source provenance, censoring semantics, analytical-method information, or interval confidence.

The final v0.3 state is frozen before supervised modelling.

## 2. v0.3.1 — Regional integration

Benchmark holes were linked to the Disraeli (DIS) and Seagull (SEA) intrusion-system contexts using assessment-property identity and regional spatial context. The regional layer includes whole-rock chemistry, isotope context, and nearby mineral-inventory/deposit information.

### Regional whole-rock state

- 138 raw regional whole-rock rows were reviewed.
- 121 canonical unique samples were retained after source-aware normalization.
- DIS: 55 canonical samples.
- SEA: 66 canonical samples.
- 8,486 long-format regional geochemical results were retained.

Regional medians and derived system metrics were independently recalculated as a reproducibility check. Sixteen system × metric checks reproduced the expected values.

The regional layer is contextual. It is not treated as a perfectly representative population of either intrusion system.

## 3. v0.3.2 — Geochemical harmonization

A shared analytical feature layer was built across regional and drill-core datasets. The common analyte panel includes Ni, Cu, Co, Au, Pd and Pt.

### Harmonization rules

- Ni, Cu and Co are standardized to ppm in the common layer.
- Au, Pd and Pt are standardized to ppb.
- Original values and original units remain preserved.
- Analytical-method metadata remain attached to the observations.
- Unit compatibility is not treated as analytical-method equivalence.
- Censored values retain qualifier and detection-limit meaning.
- No half-detection-limit substitution is used in the primary harmonized layer.

### Harmonized state

- 10,013 harmonized analytical records.
- 574 rows in the common regional + core analysis matrix.
- 493 censored analytical observations retained explicitly.
- 413 core chemistry-eligible records.
- 338 chemistry records in the exact-depth eligibility subset at this stage.

Derived features such as Cu/Ni, Pt/Pd and Cu/Pd are only calculated where the required underlying observations are valid and uncensored.

## 4. v0.3.3 — Interval, lithology and chemistry integration

Exact assay-sample intervals were joined to exact primary lithology intervals rather than assigning geology only at hole level.

### Exact sample/lithology assignments

- 345 exact core samples were assigned quantitative primary-lithology coverage.
- 336 samples lie within one primary lithology.
- 9 samples cross a primary-lithology boundary.
- 6 samples also overlap secondary/subinterval features.

Boundary-crossing intervals are preserved explicitly rather than forced into a single geological class without a confidence rule.

The strongest integrated population contains **167 samples** satisfying all three conditions:

1. exact sample depth interval;
2. exact primary lithology assignment;
3. populated shared geochemical feature information.

Another 178 exact lithology-linked samples lack a populated common chemistry panel, while 75 chemistry-bearing records remain depth-unresolved and therefore are retained only for broader system-level context.

## 5. Regional-position calculations

For integrated core samples, same-system regional position was calculated using empirical distributions from the corresponding regional context.

The comparison layer includes:

- empirical percentile;
- regional median and interquartile range;
- robust IQR position;
- relation to supplied regional minimum/maximum;
- a minimum same-system reference count of 10.

This produced:

- 1,779 core-feature regional-position calculations;
- 1,681 comparisons retained after the regional n ≥ 10 rule;
- 242 samples with at least two regionally comparable features;
- 98 system × lithology × feature summary combinations.

These are descriptive context measures, not probabilities of mineralization.

## 6. v0.3.4 — Measured-depth downhole context

The strongest exact integrated subset contains 167 samples across five holes:

- DL-21-004: 34 samples;
- SN12-01: 45;
- SN12-02: 38;
- U-17-01: 16;
- U-17-02: 34.

Because complete station-by-station trajectory information is not available for every hole, interpretation is restricted to measured depth. No unsupported full 3-D borehole trajectory is reconstructed.

### Descriptive regional-response classes

Using raw analyte relationships to the supplied same-system regional distributions:

- 95 samples remain within the regional envelope;
- 23 have one feature at or above the 95th percentile;
- 22 have multiple features at or above the 95th percentile;
- 27 have at least one feature above the supplied regional maximum.

These classes are descriptive summaries only. They are not ore labels and are not used as hidden supervised targets.

### Downhole clustering

Only touching or overlapping sample intervals are grouped into downhole response clusters. A 0.01 m tolerance is used only to absorb numerical rounding.

- 23 conservative response clusters were identified.
- 48 source-defined primary-lithology packages were summarized geochemically.

## 7. v0.3.5 — Cross-hole synthesis

Cross-hole comparison is governed by explicit comparability rules. Concentrations are not assumed directly comparable merely because units were harmonized.

Across same-system hole-pair × feature comparisons:

- 24 comparisons were evaluated;
- 7 were Tier A;
- 1 was Tier B;
- 12 were Tier C;
- 4 were Tier D;
- 8 support direct same-method concentration comparison.

### Descriptive observations

- SN12-01 and SN12-02 provide the cleanest same-method cross-hole comparison.
- The exact DL-21-004 gabbro subset shows upper-tail Cu/Pd behavior relative to the supplied DIS regional context while Ni remains comparatively low.
- U-17-01 and U-17-02 show repeated upper-tail Cu/Co behavior and locally elevated Pt relative to the supplied regional context.
- In the sampled exact magnetite-skarn subset across the U17 holes, 24 of 27 samples fall in one of the descriptive response classes.
- Repeated SEA gabbro and mafic-intrusive subsets generally do not show the same response-class frequency.

These observations describe the sampled subsets only. Cross-system response fractions are not interpreted as intrusion fertility, prospectivity or deposit ranking.

## 8. Frozen v0.3 state

The final v0.3 integration foundation contains:

- 10 benchmark holes;
- 403 lithology intervals;
- 453 assay samples;
- 1,527 assay results;
- 121 canonical regional samples;
- 8,486 regional geochemical results;
- 10,013 harmonized analytical records;
- 345 exact sample/lithology assignments;
- 167 exact integrated downhole samples across five holes.

No hole is treated as validated for complete 3-D trajectory work.

## 9. Scientific interpretation

The primary contribution of v0.3 is the integration architecture: provenance-preserving source reconstruction, analytical harmonization, interval-aware geological joining, measured-depth context, regional normalization and explicit comparability rules. The result is a defensible pre-modelling foundation that can be extended with additional independent drill-core data and future analytical modalities without changing the underlying QC principles.
