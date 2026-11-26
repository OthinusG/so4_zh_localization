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
| `analysis/extraction_summary.json` | Extraction and alignment statistics for the current baseline |
| `scripts/verify_alignment.py` | Baseline and work queue validator |

Join the work queue to either baseline by `stable_id`. Only `zh_edit` is editable. A blank edit leaves the original `pc_zh` in use on a `polish` row and leaves a `translate_then_polish` row untranslated. Track reviewed translations in the batch checklist, including reviews that kept the original wording.

Run `python3 scripts/verify_alignment.py` with Python 3.10 or newer. A future packaging step needs a selected target platform and in-game testing.

## Known Issues and Solutions (已知问题与解决方案)

### 1. `05_cutscene_story` 剧情文本乱码与字符编码损坏 — 已修复
- **现象 (Issue)**:
  旧基线中 641 条 `translate_then_polish` 记录有 579 条集中在 `05_cutscene_story`，其 PS3 日文源文本存在大范围乱码（如 `彼らはパロメタダータ攻格作戦は...`、`な なん飽1？`）。
- **根因 (Root Cause)**:
  PS3 端字符映射表与实际打包字体存在偏差，特定汉字和假名被错误解析。
- **修复 (Resolution)**:
  使用校正后的字库映射（`charmap_ps3_final.json`、`charmap_003a_jp_clusters.json`）与无损 DXT3 字库解码重新提取。当前基线未解析字形 `<G:>`/`<LG:>` 为 0，`05_cutscene_story` 仅剩 1 条待翻译记录。

### 2. PS3 与 PC 剧情消息索引（`msg_id`）错位与对齐偏差 — 已修复
- **现象 (Issue)**:
  `0x0223003A/0x100E8` 等场景中 PS3 与 PC 的 `msg_id` 序列漂移，大量行在另一端匹配为空，被误判为 PS3 独占待翻译条目。
- **根因 (Root Cause)**:
  6 个过场文件（`0x100CE/E8/E9/EA/F3/F6`）在 PC 端被拆分或重排，静态 `(f0, f1, msg_id)` 对齐无法跨越索引平移。
- **修复 (Resolution)**:
  对新基线执行内容级跨场景重对齐（1,040 条），并以新增的 `pc_source_id` 列记录 PC 端溯源 ID（1,111 行与 `stable_id` 不同）。待翻译总数由 641 降至 58，其中 35 条为 PS3 演职员表。

### 3. 系统/菜单跨平台控制码与平台专用术语差异
- **现象 (Issue)**:
  全库 32,800 行中，有 4,686 行 `jp_same = false`，2,950 行 `ctrl_same = false`。特别是 `01_system_menu` 和 `02_field_ui` 中，PS3 端含有专用储存设备（如“ストレ－ジ機器”）、按键控制符等，而 PC 端使用键鼠/通用手柄提示。
- **根因 (Root Cause)**:
  主机版（PS3/Xbox 360）与 PC 移植版的系统机制与按键架构不同。
- **解决办法 (Solution)**:
  1. 维持分平台控制符校验：翻译与润色时保留各平台原生控制标签（如 `<NAME:xxxx>`、按键图标等）。
  2. 确定最终封包目标（PS3 移植或 PC 增强）：针对目标平台分别处理对应的控制符与术语映射，打包前执行平台合法性校验。
