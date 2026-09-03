# Benchmark Protocol

## Purpose
v0.4.1 converts the frozen v0.3 geological/geochemical foundation into two small, auditable classification benchmarks. The purpose is **methodological benchmarking**, not ore targeting.

## Label confidence tiers
- **Tier A:** sample lies within one exact primary lithology interval.
- **Tier B:** sample crosses exact primary boundaries but the dominant logged lithology covers at least **80%** of sample length.
- **Tier X:** below the locked dominance threshold or otherwise unsuitable; excluded.

The primary cohorts use A+B. A strict A-only cohort is frozen for sensitivity analysis.

## T1 — SEA lithology
Question: can Ni-Cu-Co chemistry distinguish three repeatedly logged mafic lithology families across SN12-01 and SN12-02?

Locked mapping:
- `gabbro` + `melanocratic_gabbro` → `gabbroic`
- `diabase` → `diabase`
- `mafic_intrusive_undifferentiated` → `mafic_intrusive`

Sedimentary units, null/unresolved lithologies, and other units are excluded rather than forced into a heterogeneous `other` class.

## T2 — DIS magnetite skarn
Question: can Ni-Cu-Co chemistry distinguish logged magnetite-skarn from non-skarn intervals when transferred between U-17-01 and U-17-02?

- Positive label: `magnetite_skarn`
- Negative label: any other eligible logged primary lithology within the two U-17 holes.

This benchmark has a known domain-shift complication: U-17-01 and U-17-02 have different listed base-metal method labels. Therefore leave-one-hole-out performance is interpreted as transportability under combined hole + method shift.

## Predictor panel
Only log10-transformed uncensored positive Ni, Cu and Co values are in the primary panel. Transformations are deterministic. Standardization, where used by a model, must be fitted on the training fold only.

Au, Pd and Pt are excluded from the primary panel because missingness/censoring is uneven. Ratios and regional-percentile features are excluded from the first benchmark.

## Splitting
Random interval splitting is prohibited. Each task has exactly two fixed folds, each holding out one entire drill hole.

## Models pre-declared for v0.4.2
1. Dummy prior baseline.
2. StandardScaler + class-balanced logistic regression with fixed settings and no hyperparameter tuning.
3. Class-balanced random forest with fixed conservative settings and no hyperparameter tuning.

With only two independent holes per task, the first benchmark will not optimize hyperparameters against the held-out holes.

## Metrics
T1 primary: balanced accuracy. Secondary: macro-F1, per-class recall, confusion matrix, multiclass log loss.

T2 primary: balanced accuracy. Secondary: macro-F1, sensitivity, specificity, ROC-AUC, PR-AUC, Brier score, confusion matrix.

Fold-specific results and pooled out-of-fold predictions are both mandatory. No inferential p-values or sample-wise confidence intervals are claimed because intervals within a hole are depth-clustered.
