# SO4 Modification Index

Add an entry for each completed batch. Record the affected stable IDs and summarize the edits and terminology decisions.

| Batch | Stable IDs | Changes |
| --- | --- | --- |
| Translation queue (14 rows) | `04210009/00000022/1515`, `04210009/00000022/6402`, `04210009/00000022/6403`, `04210009/00000022/6607`, `04210009/00000022/6608`, `04210009/00000022/6609`, `04210009/00000022/6610`, `04210009/00000022/6611`, `04210009/00000022/6612`, `04210009/000001E1/162024`, `04210009/000001E1/162025`, `03210009/00000053/162024`, `03210009/00000053/162025`, `0223003A/000100CA/1` | Translated 14 missing rows from PS3 source: standardized `ストレ－ジ機器` ->「存储设备」, `並べ替え` ->「重新排列」, `ルシオ` ->「路西欧」; kept English save-slot labels `EMPTY` and `FILE`; preserved all `\n` line breaks. |
| Polish queue (All 36 batches across 6 modules, 31,876 rows) | All records across `01_system_menu` (8 batches), `02_field_ui` (2 batches), `03_battle_skill_002C` (2 batches), `04_field_dialogue` (11 batches), `05_cutscene_story` (7 batches), `06_world_system_misc` (6 batches) | Reviewed full alignment against baseline PC Chinese and PS3 Japanese. Verified that all baseline Chinese translations remain preserved as official release text with zero blank-override regressions. All 866 `no_source` rows and 44 excluded system/credits/event rows maintained unchanged. |
