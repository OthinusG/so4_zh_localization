# STAR OCEAN 4 Chinese Localization

This workspace prepares the aligned PS3 and PC extracts for Chinese localization. Existing PC Chinese goes through Japanese-source review and polishing. Records with only Japanese go through translation and then polishing. Records with no source text stay in the alignment as placeholders.

| Path | Purpose |
| --- | --- |
| `so4_bilingual_full_ps3_pc_jp_zh.json` | Original aligned PS3 and PC data, used as the validation baseline |
| `tsv/so4_bilingual_full_ps3_pc_jp_zh.tsv` | Original TSV view of the same data |
| `tsv/so4_working.tsv` | Work queue and editable Chinese overrides, keyed by `stable_id` |
| `so4_localization_project_plan.md` | Workflow, acceptance criteria, and module batch checklist |
| `so4_modification_index.md` | Record of completed edits |
| `analysis/so4_glossary.json` | Shared glossary for future editorial work |
| `scripts/verify_alignment.py` | Baseline and work queue validator |

Join the work queue to either baseline by `stable_id`. Only `zh_edit` is editable. A blank edit leaves the original `pc_zh` in use on a `polish` row and leaves a `translate_then_polish` row untranslated. Track reviewed translations in the batch checklist, including reviews that kept the original wording.

Run `python3 scripts/verify_alignment.py` with Python 3.10 or newer. A future packaging step needs a selected target platform and in-game testing.
