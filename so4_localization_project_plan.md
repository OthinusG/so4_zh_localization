# SO4 Localization Project Plan

## Scope and acceptance

- Initialize the workspace from the supplied PS3 and PC extracts. The baseline files must retain their original contents and row order.
- Assign one work row to every baseline stable ID. Route nonblank `pc_zh` to `polish`, remaining rows with Japanese text to `translate_then_polish`, and blank or whitespace-only rows to `no_source`.
- Leave the Chinese override column empty at initialization. Verify full JSON/TSV equivalence, unique IDs, work row alignment, and workflow counts.

## Editorial workflow

Use the Japanese text for the relevant platform. Compare both source columns when `jp_same` is false and inspect the control fields when `ctrl_same` is false. Check embedded names and placeholders in context. Record terminology and edits, run the alignment check, and then mark the batch complete. Packaging and in-game verification require a target-platform decision.

## Batch checklist

Ranges are 1-based record positions within each module after filtering the baseline in its original order. Each batch contains at most 1,000 records and may contain both workflows. The counts show how many records follow each path.

### `01_system_menu`

- [ ] Records 1–1000 (991 polish, 9 translate then polish, 0 placeholders)
- [ ] Records 1001–2000 (997 polish, 2 translate then polish, 1 placeholders)
- [ ] Records 2001–3000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 3001–4000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 4001–5000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 5001–6000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 6001–7000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 7001–7650 (650 polish, 0 translate then polish, 0 placeholders)

### `02_field_ui`

- [ ] Records 1–1000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 1001–1691 (689 polish, 2 translate then polish, 0 placeholders)

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
- [ ] Records 7001–8000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 8001–9000 (986 polish, 14 translate then polish, 0 placeholders)
- [ ] Records 9001–10000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 10001–10286 (286 polish, 0 translate then polish, 0 placeholders)

### `05_cutscene_story`

- [ ] Records 1–1000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 1001–2000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 2001–3000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 3001–4000 (490 polish, 510 translate then polish, 0 placeholders)
- [ ] Records 4001–5000 (928 polish, 69 translate then polish, 3 placeholders)
- [ ] Records 5001–6000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 6001–6488 (488 polish, 0 translate then polish, 0 placeholders)

### `06_world_system_misc`

- [ ] Records 1–1000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 1001–2000 (965 polish, 35 translate then polish, 0 placeholders)
- [ ] Records 2001–3000 (1000 polish, 0 translate then polish, 0 placeholders)
- [ ] Records 3001–4000 (692 polish, 0 translate then polish, 308 placeholders)
- [ ] Records 4001–5000 (975 polish, 0 translate then polish, 25 placeholders)
- [ ] Records 5001–5537 (9 polish, 0 translate then polish, 528 placeholders)
