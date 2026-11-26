# SO4 Localization Project Memory

## Initialization on 2026-11-26

- The GitHub repository is [OthinusG/so4_zh_localization](https://github.com/OthinusG/so4_zh_localization). The default branch is `main`.
- The local workspace uses the directory and tracking conventions of [Grisaia Localization](https://github.com/OthinusG/grisaia_zh_localization).
- The PS3/PC extract has six modules and 32,819 unique `stable_id` values. The JSON and TSV exports agree on all fields and row order.
- PC Chinese seeds the polishing workflow. There are 31,312 rows for polishing, 641 for translation followed by polishing, and 866 blank or whitespace-only placeholders.
- Among the 31,312 rows with PC Chinese, 4,556 have a false `jp_same` flag and 2,282 have a false `ctrl_same` flag. Compare platform context before reusing PC Chinese for PS3.
- A blank working override preserves the baseline Chinese on a polishing row. Platform-specific packaging is pending.
