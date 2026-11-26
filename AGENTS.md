# SO4 Localization Project Guidelines

- Read `README.md`, `MEMORY.md`, and `so4_localization_project_plan.md` before changing the project.
- Use `stable_id` to match records across files. Preserve the original row order, identifiers, pack metadata, and extracted text in both baselines.
- Edit only `zh_edit` in `tsv/so4_working.tsv`. Use the existing PC Chinese for `polish` and the available Japanese for `translate_then_polish`. Leave `no_source` rows untouched.
- Check the Japanese variants and control strings before editing. Maintain the selected output platform's required tokens and verify platform-specific differences before packaging.
- Keep work batches at 1,000 records or fewer. Record completed changes by stable ID in `so4_modification_index.md` and run `python3 scripts/verify_alignment.py` before checking off a batch.
- Store TSV files in `tsv/`, terminology in `analysis/`, and scratch files in `tmp/`.
