# SO4 Localization Project Memory

## Initialization on 2026-11-26

- The GitHub repository is [OthinusG/so4_zh_localization](https://github.com/OthinusG/so4_zh_localization). The default branch is `main`.
- The local workspace uses the directory and tracking conventions of [Grisaia Localization](https://github.com/OthinusG/grisaia_zh_localization).
- The PS3/PC extract has six modules and 32,800 unique `stable_id` values. The JSON and TSV exports agree on all fields and row order.
- PC Chinese seeds the polishing workflow. There are 31,876 rows for polishing, 58 for translation followed by polishing, and 866 blank or whitespace-only placeholders.
- Among the 31,876 rows with PC Chinese, 4,686 have a false `jp_same` flag and 2,950 have a false `ctrl_same` flag. Compare platform context before reusing PC Chinese for PS3.
- The baseline carries a `pc_source_id` column for cross-scene realignment; 1,111 rows point to a different PC source ID than their `stable_id`.
- A blank working override preserves the baseline Chinese on a polishing row. Platform-specific packaging is pending.

## Data Quality and Alignment Findings (2026-11-26)

- The initial baseline had corrupted Japanese source text and font decoding artifacts in `05_cutscene_story` (579 rows), plus index drift in six cutscene packs (`0x100CE/E8/E9/EA/F3/F6`).
- The baseline was replaced with the corrected extract from `/Users/wqin/Downloads/outputs`: 32,800 rows, `pc_source_id` realignment, zero `<G:>`/`<LG:>` glyphs, and 58 `translate_then_polish` rows.
- `analysis/extraction_summary.json` records the extraction statistics; `README.md` documents the remediated root causes.
- Completed translation queue of 14 rows across `01_system_menu` (11 rows), `02_field_ui` (2 rows), and `05_cutscene_story` (1 row) into `tsv/so4_working.tsv`. Standardized glossary entries recorded in `analysis/so4_glossary.json` and change record logged in `so4_modification_index.md`.

