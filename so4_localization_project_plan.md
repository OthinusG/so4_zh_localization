# SO4 Localization Project Plan

## 1. Completed and excluded work

- ~~Initialize the workspace from the PS3 and PC extracts.~~ Done 2026-11-26.
- ~~Document corrupted `05_cutscene_story` source text and `msg_id` drift.~~ Done.
- ~~Replace the baseline with the corrected extract (`pc_source_id` realignment) and rebuild the work queue.~~ Done in commit `14ca740`; `python3 scripts/verify_alignment.py` passes on the current tables.
- ~~Translate the 866 blank or whitespace-only placeholders.~~ Not applicable; they stay in the alignment as `no_source` rows and are not edited.
- ~~Translate 35 PS3-only credits rows (`0221001E/00000001/190000`–`190034`).~~ Not needed; keep the original PS3 text.
- ~~Translate 9 event/filename keys in `04_field_dialogue` (`0223001E/000000A7/55`–`65`).~~ Not needed; these are internal resource names such as `vm008_W00E01a` and stay unchanged.

## 2. Translation queue (14 rows, 12 need Chinese)

All rows below have an empty `pc_zh` and no usable PC Japanese source. Translate from `ps3_jp`, write the result to `zh_edit`, and keep the control tokens shown in the source (`\n`).

### `01_system_menu` (11 rows)

| stable_id | PS3 source | Suggested Chinese | Notes |
| --- | --- | --- | --- |
| `04210009/00000022/1515` | ストレ－ジ機器が接続されていないか容量が不足しています。\nこのまま開始しますか？ | 存储设备未连接或容量不足。\n是否仍要开始？ | Keep one `\n` |
| `04210009/00000022/6402` | EMPTY | EMPTY | Save-slot label; may stay English, confirm glyph width in game |
| `04210009/00000022/6403` | FlLE | FILE | Save-slot label; may stay English |
| `04210009/00000022/6607` | ストレ－ジ機器の読み込みに失敗しました。 | 存储设备读取失败。 | |
| `04210009/00000022/6608` | 容量が不足しています。\nもうー度ストレ－ジ機器を選択してください。 | 容量不足。\n请重新选择存储设备。 | Keep one `\n` |
| `04210009/00000022/6609` | チェックしています。\n本体の電源を切らないでください。\n処理中のストレ－ジ機器に触れないでください。 | 正在检查。\n请勿关闭主机电源。\n请勿触碰正在处理的存储设备。 | Keep two `\n` |
| `04210009/00000022/6610` | 使用中のストレ－ジ機器が見つかりません。\nもうー度ストレ－ジ機器を選択してください。 | 未找到使用中的存储设备。\n请重新选择存储设备。 | Keep one `\n` |
| `04210009/00000022/6611` | サインインしたゲ－マ－ プロフィ－ルの入ったストレ－ジ機器が取り外されました。\nストレ－ジ機器を接続しなおしてから、\nもうー度ストレ－ジ機器を選択してください。 | 已移除存有已登录玩家资料的存储设备。\n请重新连接存储设备，\n然后重新选择存储设备。 | Keep two `\n` |
| `04210009/00000022/6612` | ゲ－ムを再開しますか？\nサインインしたゲ－マ－ プロフィ－ルが入っている\nストレ－ジ機器が接続されていない場合は実績の解除は行われません。 | 是否继续游戏？\n若未连接存有已登录玩家资料的\n存储设备，将不会解除成就。 | Keep two `\n` |
| `04210009/000001E1/162024` | 並べ替え | 重新排列 | Matches existing PC translation |
| `04210009/000001E1/162025` | ストレ－ジ機器切替 | 存储设备切换 | Same text as `02_field_ui` row below |

### `02_field_ui` (2 rows)

| stable_id | PS3 source | Suggested Chinese | Notes |
| --- | --- | --- | --- |
| `03210009/00000053/162024` | 並べ替え | 重新排列 | Reuse the `01_system_menu` wording |
| `03210009/00000053/162025` | ストレ－ジ機器切替 | 存储设备切换 | Reuse the `01_system_menu` wording |

### `05_cutscene_story` (1 row)

| stable_id | PS3 source | Suggested Chinese | Notes |
| --- | --- | --- | --- |
| `0223003A/000100CA/1` | ルシオ…… | 卢西奥…… | Character name; confirm the accepted rendering before editing |

### Terminology notes

- `並べ替え` already appears as「重新排列」in the PC Chinese; keep that wording.
- Existing PC Chinese mixes「存储器」「储存机器」「存储」for `ストレ－ジ機器`. Use「存储设备」for these 12 new rows and record it in `analysis/so4_glossary.json`; unify older rows during polishing if practical.
- `実績` here means achievement progress; PS3 system text elsewhere may use「奖杯」. Confirm on the target platform before packaging.

### Completion criteria for this queue

1. Fill `zh_edit` for the 12 Chinese rows (leave `EMPTY`/`FILE` blank only if the English labels are confirmed in game).
2. Check control tokens and line breaks against `ps3_jp`.
3. Run `python3 scripts/verify_alignment.py`.
4. Record the edited stable IDs in `so4_modification_index.md`.

## 3. Polish queue (31,876 rows, 0 batches completed)

Use the PC Chinese as the base, compare `ps3_jp` when `jp_same` is false and `controls_ps3` when `ctrl_same` is false. Ranges are 1-based record positions within each module after filtering the baseline in its original order. Each batch contains at most 1,000 records. Batches that still contain translation rows are marked.

### `01_system_menu`

- [ ] Records 1–1000 (991 polish, 9 translate then polish, 0 placeholders) — includes translation rows above
- [ ] Records 1001–2000 (997 polish, 2 translate then polish, 1 placeholders) — includes translation rows above
- [ ] Records 2001–3000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 3001–4000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 4001–5000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 5001–6000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 6001–7000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 7001–7650 (650 polish, 0 translate then polish, 0 placeholders)

### `02_field_ui`

- [ ] Records 1–1000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 1001–1691 (689 polish, 2 translate then polish, 0 placeholders) — includes translation rows above

### `03_battle_skill_002C`

- [ ] Records 1–1000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 1001–1167 (167 polish, 0 translate then polish, 0 placeholders)

### `04_field_dialogue`

- [ ] Records 1–1000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 1001–2000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 2001–3000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 3001–4000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 4001–5000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 5001–6000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 6001–7000 (999 polish, 0 translate then polish, 1 placeholders)
- [ ] Records 7001–8000 (991 polish, 9 translate then polish, 0 placeholders) — 9 rows are filename keys, excluded from translation
- [ ] Records 8001–9000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 9001–10000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 10001–10286 (286 polish, 0 translate then polish, 0 placeholders)

### `05_cutscene_story`

- [ ] Records 1–1000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 1001–2000 (999 polish, 1 translate then polish, 0 placeholders) — includes the `ルシオ……` row
- [ ] Records 2001–3000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 3001–4000 (999 polish, 0 translate then polish, 1 placeholders)
- [ ] Records 4001–5000 (998 polish, 0 translate then polish, 2 placeholders)
- [ ] Records 5001–6000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 6001–6469 (469 polish, 0 translate then polish, 0 placeholders)

### `06_world_system_misc`

- [ ] Records 1–1000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 1001–2000 (965 polish, 35 translate then polish, 0 placeholders) — 35 credits rows, excluded from translation
- [ ] Records 2001–3000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 3001–4000 (692 polish, 0 translate then polish, 308 placeholders)
- [ ] Records 4001–5000 (975 polish, 0 translate then polish, 25 placeholders)
- [ ] Records 5001–5537 (9 polish, 0 translate then polish, 528 placeholders)