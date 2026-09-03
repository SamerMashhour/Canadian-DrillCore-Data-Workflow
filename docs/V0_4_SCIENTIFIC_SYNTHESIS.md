# v0.4 Scientific Synthesis — Frozen Classification Benchmark

## 1. Objective

Version 0.4 tests whether a small, leakage-resistant geological classification benchmark can be built from the frozen v0.3 foundation without relaxing the source, interval and analytical constraints established earlier.

The benchmark is intentionally conservative. Its purpose is to test workflow discipline and whole-hole transfer, not to claim deployable ore targeting or generalized geological prediction.

## 2. Benchmark design frozen before fitting

Two tasks were declared before model execution.

### T1 — Seagull three-class lithology

Holes:
- SN12-01;
- SN12-02.

Classes:
- `gabbroic` — gabbro + melanocratic gabbro;
- `diabase`;
- `mafic_intrusive` — mafic intrusive, undifferentiated.

Other or sedimentary units are excluded rather than forced into a catch-all class.

Population:
- primary cohort: n = 59;
- strict Tier-A-only cohort: n = 57.

### T2 — Disraeli/Caro Lake magnetite-skarn

Holes:
- U-17-01;
- U-17-02.

Classes:
- magnetite skarn;
- non-skarn.

Population:
- primary cohort: n = 49;
- strict Tier-A-only cohort: n = 46.

## 3. Label confidence

The geological label-confidence rule is frozen before model fitting.

- **Tier A:** the sample lies completely within one exact primary lithology interval.
- **Tier B:** the sample overlaps multiple exact primary intervals, but one lithology covers at least 80% of the sample length.
- **Tier X:** lower-confidence assignments excluded from the primary benchmark.

Primary reporting uses Tier A + Tier B. Strict sensitivity reporting uses Tier A only.

## 4. Predictor panel

The primary predictor panel is deliberately small:

- log10 Ni ppm;
- log10 Cu ppm;
- log10 Co ppm.

Only positive, complete and uncensored values enter the primary panel. No primary imputation is used.

Excluded from the predictor panel:

- hole or source identifier;
- measured depth;
- coordinates or location fields;
- lithology text;
- analytical-method label;
- regional-response classes or percentile fields;
- any assay-derived response variable that would encode the target;
- Au, Pd and Pt in the primary benchmark;
- derived ratios in the primary benchmark.

## 5. Validation strategy

The drill hole is treated as the independent validation unit.

No random neighboring-interval split is permitted.

Each task uses leave-one-whole-hole-out transfer:

- T1 trains on one SN12 hole and tests on the other, then reverses.
- T2 trains on one U17 hole and tests on the other, then reverses.

Because the number of independent holes is small, headline performance uses the **equal-hole mean of held-out fold metrics**. Pooled out-of-hole predictions are retained as secondary diagnostics.

## 6. Fixed baseline models

Three baseline models are fixed before evaluation:

1. prior-probability dummy classifier;
2. StandardScaler + class-balanced logistic regression;
3. class-balanced random forest.

No hyperparameter tuning or model selection is performed against the held-out benchmark holes.

## 7. Primary results

### T1 — Seagull lithology

Equal-hole mean balanced accuracy:

| Model | Mean balanced accuracy |
|---|---:|
| Dummy | 0.333 |
| Logistic regression | **0.574** |
| Random forest | 0.510 |

Logistic fold range: approximately 0.497–0.650.

Interpretation: T1 contains a preliminary lithogeochemical signal, but the result is fold-sensitive and does not support a claim of a robust generalized lithology classifier.

### T2 — magnetite-skarn vs non-skarn

Equal-hole mean balanced accuracy:

| Model | Mean balanced accuracy |
|---|---:|
| Dummy | 0.500 |
| Logistic regression | 0.689 |
| Random forest | **0.814** |

Random-forest fold range: approximately 0.794–0.833.

The strict Tier-A-only sensitivity cohort yields an approximately 0.897 equal-hole mean balanced accuracy for the fixed random forest. Only three Tier-B samples are removed, so the improvement is treated as small-n label-boundary sensitivity rather than a general performance claim.

## 8. Important T2 domain-shift limitation

The listed base-metal analytical-method families differ between U-17-01 and U-17-02. As a result, the T2 held-out-hole test combines:

- geological transfer;
- drill-hole transfer;
- analytical-method domain transfer.

The result therefore cannot be interpreted as pure lithological separability.

## 9. What the benchmark does not establish

Version 0.4 does not validate:

- ore targeting;
- probability of mineralization;
- deposit ranking;
- intrusion fertility ranking;
- prospectivity ranking;
- generalized 3-D prediction;
- transfer to new districts;
- causal interpretation of model coefficients or feature importance.

Feature importance and logistic coefficients are retained as diagnostics only. Some coefficient directions vary between folds, reinforcing the need for caution.

## 10. Why repeated tuning is not the next step

The same four supervised holes should not be repeatedly used for tuning and then treated as independent validation.

The strongest next improvement is **new independent data**:

- additional holes with exact interval and assay information;
- improved survey information;
- verified missing analytical tables;
- genuinely new analytical modalities.

Any later expansion should freeze revised labels, eligibility and features before refitting.

## 11. Frozen v0.4 interpretation

Version 0.4 demonstrates that a provenance-aware drill-core workflow can be carried forward into a leakage-controlled whole-hole classification benchmark. T1 is preliminary and fold-sensitive. T2 is comparatively promising in this limited sample but remains domain-shift-limited and based on only two independent holes.

The main contribution is therefore the benchmark design and validation discipline as much as the numerical model score.
