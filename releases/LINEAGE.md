# Release lineage

This repository preserves a staged scientific lineage rather than silently replacing earlier states.

```text
v0.1.1 FINAL
Source readiness, provenance, relational schema, QC foundation
        ↓
v0.2 RC2
PDF-derived interval reconstruction, assay ingestion and source-aware QC
        ↓
v0.3 FINAL
Regional integration, geochemical harmonization, interval/lithology joins,
downhole context and cross-hole synthesis
        ↓
v0.4 FINAL
Frozen label/feature policies, leakage register, whole-hole validation,
and fixed baseline classification models
```

## Maintenance principle

If improved source files become available, they should enter through an explicit maintenance branch such as `v0.2.x`, with downstream integration regenerated transparently. Frozen releases should not be overwritten in place.

## Public repository role

The GitHub repository is a curated research-software layer. Large third-party source packages and private archival build artifacts are intentionally excluded. Public demonstrations use synthetic rows and compact derived summary products while preserving the scientific rules used by the full workflow.
