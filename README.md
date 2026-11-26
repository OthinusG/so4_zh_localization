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

## Known Issues and Solutions (已知问题与解决方案)

### 1. `05_cutscene_story` 剧情文本乱码与字符编码损坏
- **现象 (Issue)**: 
  在 641 条待翻译（`translate_then_polish`）的记录中，有 579 条集中在 `05_cutscene_story`（例如 `0x0223003A/0x100E8` 等数据包）。其 PS3 日文源文本存在大范围的文字乱码与错字（例如：`彼らはパロメタダータ攻格作戦は\n奮加する戦士たぢです`、`グりユりを撃釀1た奮マんは敬意を表1Tいます`、`な なん飽1？`）。
- **根因 (Root Cause)**:
  PS3 提取端所使用的字符映射表（Custom Font Charset / Shift-JIS 映射表）与游戏实际打包字体存在偏差，导致特定汉字和假名被错误解析为混淆字符。
- **解决办法 (Solution)**:
  1. 重新核验与修正 PS3 端的字库映射提取工具（特别是针对 `0x0223003A` 系列封包），使用正确的码表重新导出文本。
  2. 针对已知乱码模式（如 `飽1` -> `の` / `か` 等）建立系统性映射补丁表，在提取阶段消除乱码，禁止在此类损坏文本上直接人工或机器盲翻。

### 2. PS3 与 PC 剧情消息索引（`msg_id`）错位与对齐偏差
- **现象 (Issue)**:
  在剧情文本提取中，同一场景内的 PS3 `msg_id` 与 PC `msg_id` 出现明显的行号漂移与不对齐。例如在 `0x0223003A/0x100E8` 中，PC 的 `msg_id` 与 PS3 对应的台词处于不同序列，导致大量行在另一端匹配为空，被错误归类为仅 PS3 独占的待翻译条目。
- **根因 (Root Cause)**:
  PS3 与 PC 版本的封包结构存在差异（PC 端部分字幕或事件文本经过合并、分段重排或 pack 拆分），当前基于静态 `(f0, f1, msg_id)` 简单对齐的算法无法适应版本间的索引重排。
- **解决办法 (Solution)**:
  1. 升级对齐算法：引入模糊匹配（Fuzzy String Matching / LCS 最长公共子序列）及控制符特征匹配，对跨版本的同一剧情对话进行序列重对齐。
  2. 重新生成双语基线 `so4_bilingual_full_ps3_pc_jp_zh.json`，消除因行号漂移虚增的待翻译行。

### 3. 系统/菜单跨平台控制码与平台专用术语差异
- **现象 (Issue)**:
  全库 32,819 行中，有 4,556 行 `jp_same = false`，2,282 行 `ctrl_same = false`。特别是 `01_system_menu` 和 `02_field_ui` 中，PS3 端含有专用储存设备（如“ストレ－ジ機器”）、按键控制符等，而 PC 端使用键鼠/通用手柄提示。
- **根因 (Root Cause)**:
  主机版（PS3/Xbox 360）与 PC 移植版的系统机制与按键架构不同。
- **解决办法 (Solution)**:
  1. 维持分平台控制符校验：翻译与润色时保留各平台原生控制标签（如 `<NAME:xxxx>`、按键图标等）。
  2. 确定最终封包目标（PS3 移植或 PC 增强）：针对目标平台分别处理对应的控制符与术语映射，打包前执行平台合法性校验。
