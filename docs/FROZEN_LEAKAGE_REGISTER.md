# Leakage Register

| rule_id | field_or_practice | status | rationale |
|---|---|---|---|
| L001 | regional_response_class / regional percentile / above-95th fields | PROHIBITED | Derived directly from assay features; using them as predictors would create circularity. |
| L002 | primary_lithology, raw lithology text, lithology confidence/assignment fields | PROHIBITED_AS_FEATURE | These define or directly encode the supervised lithology/skarn labels. |
| L003 | hole_id, sample_id, source_id | PROHIBITED_AS_FEATURE | Identifiers can memorize hole/source and create non-geological performance. |
| L004 | from_m, to_m, midpoint_m, coordinates | PROHIBITED_PRIMARY | Depth/location can encode stratigraphic position or hole identity; reserved for diagnostics only. |
| L005 | analytical method | PROHIBITED_PRIMARY | Method is provenance, not geology. In T2 it is confounded with hole. Keep for auditing, never as predictor. |
| L006 | PGE_total, Cu/Ni, Cu/Pd, Pt/Pd | NOT_IN_PRIMARY_PANEL | Not target leakage, but excluded from the first benchmark to reduce small-n feature engineering and double-counting. |
| L007 | Au/Pd/Pt | NOT_IN_PRIMARY_PANEL | Incomplete/censored support differs by hole. May be tested only in a separately locked secondary benchmark. |
| L008 | adjacent intervals split randomly | PROHIBITED_SPLIT | Neighbouring samples from the same hole are correlated; validation is grouped by drill hole. |

## Principle

The benchmark is designed so that geological labels, source identifiers, spatial position, derived assay-response summaries and method labels cannot leak into the primary predictor panel. Any future benchmark expansion should update this register before model fitting.
