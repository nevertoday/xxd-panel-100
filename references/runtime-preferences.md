# XXD Panel remembered delivery preferences

Use this contract whenever an XXD Panel invocation still has unresolved delivery settings after parsing the user's current words and inline parameters. The purpose is to reduce repeated setup without allowing an earlier task to contaminate the current source or aesthetic.

## What is remembered

The whole XXD Panel family shares one last-delivery record. It may contain only:

- selected output modes;
- size policies, ratios, or exact pixels;
- text mode and target locale;
- wallpaper relationship and labelled device sizes;
- an explicitly chosen output root.

Never remember a source path, uploaded image, exact user copy, filename-to-copy mapping, selected Panel number, routing strategy, visual interpretation, generated prompt, result path, task name, model/provider/endpoint, credential, account detail, or secret. `text_mode=exact` may be remembered, but the exact copy is deliberately absent and must be requested again.

Remembering delivery preferences never means reusing an old result. Every invocation still creates a fresh task and fresh images, and every numbered Soldier still uses only its own canonical original prompt as aesthetic authority.

## Priority and opening behaviour

1. Parse the current invocation first. Explicit parameters and clear current prose always override remembered values.
2. When all required delivery variables are already resolved, skip the preference question and continue directly. Save the newly resolved safe preference before generation unless the user selected `--prefs off` or explicitly asked not to remember it.
3. When variables remain unresolved, run `python3 scripts/panel_preferences.py load`, resolving the script path relative to the active Skill directory rather than assuming the process working directory.
4. If the result is `missing` or `invalid`, do not expose file contents or treat it as a task failure. Continue with the ordinary preflight.
5. If a valid record exists, show a compact human-readable summary and ask one genuine single-choice question:

```text
检测到上次的 XXD Panel 交付偏好：
成品：<modes>
尺寸：<size policies / ratios / pixels>
文字：<mode and locale; say “准确文字需本次重新输入” when exact>
壁纸：<relationship and device sizes, only when relevant>
输出：<custom root or default>

这次怎么开始？
1. 直接沿用——沿用上次设置，本次已经说出的要求优先
2. 沿用并修改——先带入上次设置，只修改我指定的项目
3. 全新配置——忽略上次设置，从头选择
```

Use the host's single-choice question tool when available; these three options are mutually exclusive. Without such a tool, use the numbered text question exactly as a typed choice, not fake checkboxes.

## Meaning of the three choices

- **Reuse:** fill unresolved fields from the record. Current explicit requirements win. Ask only for values that cannot safely carry over, such as the new exact copy, or for requirements newly introduced by the current mode.
- **Reuse and edit:** load the record, then ask which fields to change: modes, sizes, text/language, wallpaper settings, or output root. Use real multi-select when available; otherwise accept a typed combination. Keep every unselected field and ask only the chosen fields.
- **Fresh configuration:** ignore the record for this invocation and run the normal preflight. Do not delete the old record immediately; replace it only after the new settings are fully resolved, so cancellation does not destroy a useful preference.

Partial inline parameters do not suppress this choice. They override the matching remembered fields, while the selected preference route determines how the remaining fields are resolved.

## Inline preference controls

Accept `--prefs` anywhere after the invocation:

- `--prefs last`: reuse the record without asking the three-way preference question;
- `--prefs edit`: load it and ask only what to change;
- `--prefs new`: ignore it and run a fresh configuration;
- `--prefs off`: ignore it for this invocation and do not save this invocation;
- `--prefs clear`: clear the record, then run a fresh configuration and save the new resolved preference unless the user also says not to remember it.

If `last` or `edit` is requested but no valid record exists, say so briefly and use fresh configuration. Natural-language equivalents such as “沿用上次设置”, “在上次基础上改”, “这次重新选”, and “不要记住这次” have the same meaning.

## Saving the resolved preference

After the current delivery settings are complete and consistent, save only the safe fields with `python3 scripts/panel_preferences.py save ...`, again resolving the helper relative to the active Skill directory. Pass modes and sizes as repeatable or comma-separated values. Pass wallpaper fields only when wallpaper mode is active. Never pass exact copy or any forbidden field to the helper.

`auto` is remembered as the policy `auto`, not as the source-dependent ratio calculated for the previous image. `source` is remembered as `source`, not as the previous source's dimensions. A custom output root may be reused only while it remains usable; if it is unavailable, treat only that field as unresolved.

For a directory batch, save the shared delivery settings only. Never save per-image exceptions or filename-to-copy mappings. For the General Skill, never save recommendation mode, selected Soldier numbers, comparison sets, or batch assignment strategy; only the delivery settings ultimately passed to Soldiers are eligible.
