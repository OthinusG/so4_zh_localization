# SO4 Localization Project Memory

## Initialization on 2026-11-26

- The GitHub repository is [OthinusG/so4_zh_localization](https://github.com/OthinusG/so4_zh_localization). The default branch is `main`.
- The local workspace uses the directory and tracking conventions of [Grisaia Localization](https://github.com/OthinusG/grisaia_zh_localization).
- The PS3/PC extract has six modules and 32,819 unique `stable_id` values. The JSON and TSV exports agree on all fields and row order.
- PC Chinese seeds the polishing workflow. There are 31,312 rows for polishing, 641 for translation followed by polishing, and 866 blank or whitespace-only placeholders.
- Among the 31,312 rows with PC Chinese, 4,556 have a false `jp_same` flag and 2,282 have a false `ctrl_same` flag. Compare platform context before reusing PC Chinese for PS3.
- A blank working override preserves the baseline Chinese on a polishing row. Platform-specific packaging is pending.

## Data Quality and Alignment Findings (2026-11-26)

- Discovered corrupted Japanese source text and font decoding artifacts in `05_cutscene_story` (579 rows out of 641 `translate_then_polish` entries), concentrated in packs like `0x0223003A/0x100E8`.
- Discovered index drift and message sequence misalignment between PS3 and PC cutscene packs under naive `(f0, f1, msg_id)` matching.
- Documented findings, root causes, and technical remediation paths in `README.md`.
