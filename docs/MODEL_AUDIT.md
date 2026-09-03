# Model Audit Findings

| finding_id | scope | finding | evidence | limitation |
|---|---|---|---|---|
| V04-F01 | Protocol | The classification design was frozen before model fitting and no hyperparameter tuning was performed against held-out holes. | Frozen design and fixed-model definitions. | Verifies process integrity, not geological generalization. |
| V04-F02 | T1 SEA lithology | The fixed logistic baseline shows a modest transferable lithology signal, but it is fold-sensitive: equal-hole mean balanced accuracy 0.574, folds 0.497–0.650. | SN12-01 and SN12-02 are each held out once; all three target classes occur in both holes. | Only two independent holes are available; class proportions and downhole sampling differ. |
| V04-F03 | T1 class stability | Errors are class- and hole-dependent rather than uniformly distributed, and some coefficient directions vary across folds. | Fold-level class recall and coefficient diagnostics. | Coefficients should not be interpreted as stable lithogeochemical controls. |
| V04-F04 | T2 magnetite-skarn | The fixed random-forest baseline is comparatively consistent: equal-hole mean balanced accuracy 0.814, fold range 0.794–0.833. | Both U-17 holes contain magnetite-skarn and non-skarn labels, and each is held out once. | Analytical-method label changes with hole, so this is combined geological + analytical domain transfer. |
| V04-F05 | Boundary sensitivity | Removing Tier-B labels changes T2 random-forest equal-hole mean balanced accuracy from 0.814 to about 0.897. | Primary versus strict Tier-A-only sensitivity cohort. | Only three T2 Tier-B samples are removed; this is small-n sensitivity, not proof of a general boundary effect. |
| V04-F06 | Independent-hole scope | The supervised v0.4 benchmark uses four holes: SN12-01, SN12-02, U-17-01 and U-17-02. | Frozen benchmark manifests and cohort counts. | DL-21-004 remains context-only; other benchmark holes remain blocked by upstream source limitations. |
| V04-F07 | Model interpretation | No v0.4 model is validated for ore targeting, deposit ranking or probability-of-mineralization claims. | Labels are lithology/skarn classes, predictors are only Ni-Cu-Co, and validation spans only two holes per task. | Additional independent holes and/or genuinely new analytical modalities are required before extending the claim. |

## Aggregation note

Because the held-out unit is the drill hole, equal-hole mean fold metrics are emphasized. Pooled out-of-hole metrics are preserved as a secondary sample-weighted view.

## Audit conclusion

The strongest result in v0.4 is not the numerical score alone; it is the preservation of an auditable benchmark boundary. Labels, predictors, leakage rules, whole-hole splits and model settings are fixed before evaluation. The next scientifically meaningful gain should come from new independent evidence rather than repeated tuning against the same four holes.
