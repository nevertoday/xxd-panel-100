# XXD Panel soldier runtime

This is the family runtime contract for every numbered `xxd-panel-NNN` Soldier. Copy it verbatim into each Soldier as `references/soldier-runtime.md`. It is not an aesthetic prompt and never replaces `references/original-prompt/zh-CN.md`.

Read this file completely immediately before building every generation request. The numbered `SKILL.md` may add a panel-specific overlay; overlays add constraints and never rewrite this contract or the source brief.

## Authority boundary

1. Read `references/original-prompt/zh-CN.md` completely immediately before building every generation request. That Chinese source brief is the sole creative and aesthetic authority.
2. If its first Markdown heading is only an administrative document label (for example `# Original XXD Panel NNN style brief`), omit that heading from the image-generation request and copy the entire remaining body verbatim. If there is no such heading, use the entire file. Do not summarize, translate, polish, expand, reinterpret, or replace that body with `SKILL.md`, a README, a sample, a runtime adapter, this file, or any reading translation in `references/original-prompt/`. Those translations exist for international readers and sharing; they are never runtime prompt alternatives.
3. The source brief owns subject transformation, composition inside the design region, colour, palette derivation or fixed colour choices, materials, texture, whitespace, text amount, wording logic, typographic character, and prohibitions.
4. Runtime instructions may change only: selected output mode, final canvas ratio or pixels, placement or visibility of the reality source, device profile, wallpaper relationship, target text language, and user-exact text.
5. Append all runtime instructions **after** the complete source-brief body. Never insert them into, or rewrite, its aesthetic paragraphs.
6. When a source brief describes a 3:4 top-bottom container, treat that as the original presentation container. The selected mode-specific block replaces that container's **canvas ratio and orientation**. Comparison modes still keep exact 50:50 halves. Every remaining aesthetic and transformation instruction stays active.
7. Never create a generic palette, extract extra colours, lock a swatch set, invent an “aesthetic motive,” pre-compose a title, generate a copy package, or run an external semantic-reading framework. If the source brief itself asks for any of those things, let the image model perform them exactly there.
8. Samples show outcomes only. Do not copy their subject matter, colours, text, layout accidents, or aspect ratio.

Use these roles when the container changes:

```text
REALITY SOURCE = the uploaded photograph or other user-supplied source image
TRANSFORMED DESIGN = the source brief's designed reinterpretation of that reality view
```

The mode name is not a loose hint. For every requested asset, append exactly one of the four mode-specific delivery blocks below. Never send unused mode alternatives to the image model.

`top-bottom` and `left-right` always use exactly two equal 50:50 regions. That geometry is a family delivery rule and does not require a separate user request. Within each region, let the image model decide scale, crop or environmental extension, whitespace, overlap and internal layout unless the user explicitly requests more exact geometry.

Do not add extra outer canvas regions: no header, footer, centre strip, title band, inset panel, collage, or third band. Source-required internal grids, frames, image containers and sidebars belong entirely inside the TRANSFORMED DESIGN region and must be preserved.

Every ordinary asset is a single direct transformation from the current original source. Never feed an intermediate stylisation, an earlier generated result, another Panel's output, or a sample image back into the model as a second transformation pass. The only permitted multi-reference exception is an explicitly selected `linked` wallpaper pack.

## Resolve only runtime variables

Every invocation is a new job unless the user explicitly asks to inspect, edit, continue, or reuse a named result. Repeating the same request requires fresh generation and a new task folder; an old matching file never completes a new request. Remembered delivery preferences may reduce repeated questions, but never authorize reuse of an old source, result, prompt, or task directory.

### Inline fast path

Parse parameters anywhere after the invocation and input:

```text
/xxd-panel-NNN <source-or-directory> --mode top-bottom,design-only \
  --size auto,3:4,9:16,2160x3840 \
  --text prompt --locale ja-JP
```

Replace `NNN` with the current Soldier number. Accepted flags:

- `--mode`: one or more of `top-bottom`, `left-right`, `design-only`, `wallpaper-pack`. Repeated flags and comma-separated values accumulate; accept natural-language equivalents and `all` / `全部`.
- `--size`: one or more of `auto`, `source`, `1:1`, `3:4`, `4:3`, `4:5`, `5:4`, `2:3`, `3:2`, `9:16`, `16:9`, `21:9`, `5:7`, `7:5`, any custom ratio, or exact `WIDTHxHEIGHT`. Repeated flags accumulate; accept `×`.
- `--text`: `prompt`, `exact`, or `none`. Accept legacy aliases `auto` → `prompt` and `custom` → `exact` without presenting the old labels to users.
- `--copy "..."`: exact user text; implies `--text exact`. Do not rewrite or translate it.
- `--locale`: target language, market, or locale for visible text.
- `--wallpaper`: `linked` or `independent`.
- `--wallpaper-size`: labelled device sizes, for example `phone=1440x3200,ipad=2048x2732,desktop=3840x2160,watch=1024x1024`.
- `--out`: explicit output root.
- `--prefs`: `last`, `edit`, `new`, `off`, or `clear`; controls whether this invocation reuses, edits, ignores, suppresses, or clears the family-wide remembered delivery preference.

Explicit parameters override ambiguous prose. Multi-value parameters accumulate and deduplicate in user order; single-value parameters use the last explicit value. If every required variable is resolved, skip preflight and generate. If values are partial, ask only for unresolved variables. Ask about a direct contradiction such as `--text none` with `--copy`.

### Remembered preference gate

After parsing current prose and inline parameters, read [runtime-preferences.md](runtime-preferences.md) completely and follow it before the ordinary preflight. When unresolved settings remain and a valid previous record exists, offer exactly three clear routes: reuse, reuse and edit, or fresh configuration. A fully specified current invocation remains a true fast path and skips this question.

The remembered record is shared across the XXD Panel family because these are common delivery variables, not Soldier aesthetics. Current explicit requirements always win. Never remember exact copy, source paths, Panel selection, generated content, model routes, credentials, or secrets. Once the current settings are fully resolved, save only the safe delivery fields through `scripts/panel_preferences.py`, unless the user selected `--prefs off` or asked not to remember the invocation.

### Directory batch intake

A readable directory supplied as the source is explicit batch intent. Enter batch processing immediately; do not ask whether the user wants a batch and do not show an unrelated mode menu before inventory.

1. Recursively inventory supported raster files (`.png`, `.jpg`, `.jpeg`, `.webp`, `.heic`, `.heif`, `.avif`, `.tif`, `.tiff`, `.bmp`) case-insensitively. Respect an explicit top-level-only request or user exclusions.
2. Ignore hidden files and hidden directories, non-images, this Skill's generated task folders, and output roots inside the supplied tree. Do not follow a symbolic link whose resolved target escapes the supplied directory.
3. Use stable natural ordering by relative path. Report the discovered count and recursive scope before generation. Identify unreadable or undecodable candidates; never silently skip them. If no supported images exist, stop without creating an empty task directory.
4. Build one queue item per discovered source. All queue items use this same numbered Panel and its unchanged source brief; a Soldier never selects, blends, or switches to another Panel during a batch.
5. Resolve shared mode, size, text, locale, wallpaper, and output settings once for the whole batch. Parameters and clear prose still skip questions. Resolve `auto` and `source` per image because orientations may differ. Before execution, state the input count, shared settings, per-image exceptions, and total expected output count.
6. Treat every source as a logically isolated generation job: read the source brief afresh, construct its prompt independently, and never carry another image's content, inferred meaning, wording, prompt, anchor, or result into it. Wallpaper anchors belong only to their own source.
7. `--text prompt` generates source-grounded wording independently for each image. `--text none` applies to all images. A single `--copy` deliberately applies the same exact text to every image; when exact text differs, accept an explicit relative-path-or-filename → exact-text mapping and verify every intended source before generation. Never reuse one mapped caption for another source.
8. A failed source or asset must be named and reported without silently dropping later queue items. Apply the normal single-asset retry rule only to the failed output, continue with the remaining queue, and finish with succeeded/failed counts and paths.

One batch invocation is one physical task directory even though its queue items are logically isolated. Do not create a task directory per source.

### Capability-adaptive preflight

Do not switch the user's session into Plan mode merely to obtain a question UI. A Skill describes behaviour but cannot create UI capabilities that the host has not exposed. Detect the actual question-tool schema and follow this order:

1. **Real multi-select tool available — for example Claude Code `AskUserQuestion` with `multiSelect: true`:** use genuine checkbox questions for modes and sizes. Use single-select questions for text mode and wallpaper relationship. Do not print a redundant numbered menu after showing the form.
   - First form: modes (`top-bottom`, `left-right`, `design-only`, `wallpaper-pack`) with `multiSelect: true`; size route (`自动适配`, `跟随原图`, `常用比例`, `自定义`) with multi-select enabled when the host permits combined size sources; text mode as single-select.
   - When `常用比例` is selected, show real checkbox groups for all concrete ratios, split only as required by host option limits: square `1:1`; portrait `3:4`, `4:5`, `2:3`, `9:16`, `5:7`; landscape `4:3`, `5:4`, `3:2`, `16:9`, `21:9`, `7:5`. Accumulate selections across groups. When `自定义` is selected, collect one or more ratios or exact pixel targets through the host's free-input/Other path.
   - If wallpaper is selected, ask `linked` versus `independent` as a genuine single-select. Ask only unresolved questions and respect answers already present in prose or parameters.
2. **Only a mutually exclusive question tool is available — for example Codex `request_user_input`:** use it only for genuinely single-choice fields such as text mode, wallpaper relationship, or the size-entry route. Never represent modes or concrete sizes as a single-select when the user may choose several. Collect those multi-value fields with the two-round combination input below. Do not claim that a single-choice card is a checkbox.
3. **No interactive question tool is available:** use the same two-round combination input below. It is typed multi-value input, not a clickable form. Never draw Markdown `- [ ]` boxes or other fake controls.

Inline parameters and clear natural language always take priority. Skip every field already resolved. When all required values are present, skip every question and generate immediately.

#### Two-round combination-input fallback

First round — modes. This is a typed combination question, so label it honestly instead of calling it a checkbox:

```text
请选择一个或多个成品类型：

1. 上下对照（原图在上，本编号设计在下，严格各占 50%）
2. 左右对照（原图在左，本编号设计在右，严格各占 50%）
3. 只要设计图（原图仅作参考，不出现在成品中）
4. 四端壁纸（手机、iPad、电脑、儿童手表）

可回复：1｜1+3｜2、4｜全部
```

Second round — when at least one ordinary mode is selected, ask size route and text mode together. If the selection contains only `wallpaper-pack`, skip the ordinary-size part and resolve text plus device sizes and wallpaper relationship.

```text
请选择尺寸，可多选：

1. 智能推荐（显示本次计算出的比例与像素）
2. 跟随原图
3. 常用比例（可直接写 3:4、9:16 等一个或多个比例）
4. 自定义（输入一个或多个比例／准确像素）

请选择文字方式：

A. 模型根据原始提示词生成文字（注明语言或地区）
B. 使用我的准确文字（发送原文并注明语言或地区）
C. 不要文字

可回复：尺寸 1＋9:16；文字 A，日语
可回复：尺寸 3:4、16:9；文字 B，准确文字「……」，简体中文
```

If the user answers only `常用比例`, show the grouped library once and accept any combination:

```text
方形：1:1
竖版：3:4、4:5、2:3、9:16、5:7
横版：4:3、5:4、3:2、16:9、21:9、7:5
也可以直接输入准确像素。
```

Do not decide wording outside the source brief. For option A, provide only the target language to the image model; the image model follows the source brief's existing text logic. For option B, pass the user's characters verbatim and add no other copy. For option C, prohibit all visible text and pseudo-text.

Do not infer language or market from a person's appearance, name, clothing, scene, filename, metadata, signage, or the language used to operate the Skill. Resolve it explicitly whenever text is requested. Use natural target-language shaping, direction, punctuation, spacing, and line breaking. For Arabic, preserve connected forms and right-to-left text flow without indiscriminately mirroring the artwork.

A source-required oversized title must not be reduced to a tiny caption. Exact and text-free requests override wording or presence only; preserve the remaining aesthetic instructions, including hierarchy, scale, material and placement. If text-free delivery would destroy a source-required character-built image language, explain the conflict and resolve it before spending an image call; never silently replace that language.

If `wallpaper-pack` is selected, ask one additional single-choice question unless resolved:

```text
四端壁纸采用哪种关系？

1. 连贯套装：先生成并确认一张定调图，其余三张参考原图＋定调图独立重构
2. 四张独立：四张都只参考原图，各自构图
```

Neither option crops or mechanically resizes one wallpaper into the other devices. Default device sizes unless the user supplies labelled sizes:

```text
phone=1440x3200
ipad=2048x2732
desktop=3840x2160
watch=1024x1024
```

Ordinary-size choices do not multiply wallpaper outputs.

### Size resolution

- No silent default ratio exists.
- For `auto`, recommend a whole-canvas ratio from the source orientation, selected mode, source brief and intended use, then show the resolved ratio and pixels. Do not derive panel boxes or crop coordinates; the image model composes the selected relationship inside that canvas.
- `source` means the source photograph's aspect for the whole requested ordinary output.
- Exact pixels override a ratio.
- Every distinct aspect ratio is a separate complete-canvas composition from the same source and the same verbatim style brief. Never crop one ratio from another. Multiple resolutions sharing one aspect may be exported from the highest-quality approved composition.
- A size set applies to every selected ordinary mode unless the user maps sizes per mode.
- Before generation, state the resolved modes, concrete sizes, text mode and locale, wallpaper relationship if relevant, and total output count. Do not ask for another confirmation when they are complete and consistent.

## Build the generation prompt

For each distinct asset, concatenate exactly:

```text
[VERBATIM SOURCE-BRIEF BODY FROM references/original-prompt/zh-CN.md,
OMITTING ONLY AN ADMINISTRATIVE FIRST MARKDOWN HEADING IF PRESENT]

[COMMON DELIVERY PREAMBLE]
[EXACTLY ONE SELECTED MODE BLOCK]
[EXACTLY ONE TEXT BLOCK]
[USER'S OTHER EXPLICIT REQUIREMENTS, IF ANY]
```

Use this common preamble:

```text
MODE-SPECIFIC DELIVERY OVERRIDE — CURRENT ASSET

This block is the final authority only for the current presentation mode,
reality-source visibility, final canvas and device delivery. It completely
replaces the source brief's legacy statements about 3:4, upper/lower placement,
equal sections and the old top-bottom container.

Every source-brief instruction about the transformation's visual language,
subject identity, colour, material, texture, internal composition, whitespace,
text character and typography remains authoritative.

REALITY VIEW means the faithful photograph or factual scene defined by the source brief.
TRANSFORMED DESIGN means the source brief's designed reinterpretation of that reality view.

FINAL CANVAS: <resolved ratio and/or exact WIDTHxHEIGHT>
COMPOSITION METHOD: ONE COHERENT COMPLETE-CANVAS GENERATION
COMPARISON GEOMETRY: EXACT 50:50 WHEN TOP_BOTTOM OR LEFT_RIGHT IS SELECTED
NO EXTRA OUTER REGION: no header band, footer band, centre strip, inset panel, collage or third band
SOURCE-REQUIRED INTERNAL STRUCTURE: grids, frames, image containers and sidebars required by the source brief stay inside the TRANSFORMED DESIGN
TRANSFORMATION PASSES: ONE DIRECT PASS FROM THE CURRENT ORIGINAL SOURCE

Colour follows the original brief's existing colour instructions exactly.
Unless the user explicitly requests a colour change, do not add, replace,
summarize, or re-plan any palette.
```

Append exactly one of these mode blocks; do not include the other three.

Top-bottom:

```text
OUTPUT MODE: TOP_BOTTOM

Create one complete canvas containing exactly two full-width horizontal regions.
The REALITY VIEW occupies the upper 50% and the TRANSFORMED DESIGN occupies the
lower 50%, separated only at the exact vertical midpoint. Do not create a header,
footer, centre strip, title band, inset panel, grid, card row, collage, or third
region outside those two halves. Keep all typography inside the lower 50% without
turning it into another zone. Source-required internal grids, frames, containers
and sidebars belong inside the lower 50%. Determine only each region's internal
crop, extension, whitespace and typography from the source, source brief and
final canvas; never alter the 50:50 split.
```

Left-right:

```text
OUTPUT MODE: LEFT_RIGHT

Create one complete canvas containing exactly two full-height vertical regions.
The REALITY VIEW occupies the left 50% and the TRANSFORMED DESIGN occupies the
right 50%, separated only at the exact horizontal midpoint. Do not rotate this
into a top-bottom layout and do not create a header, footer, centre strip, title
band, inset panel, grid, card row, collage, or third region outside those two
halves. Keep all typography inside the right 50% without turning it into another
zone. Explicitly map the source brief's upper/lower positional terms to
left/right while preserving its aesthetic instructions and strict equal halves.
Source-required internal grids, frames, containers and sidebars belong inside
the right 50%. Determine only each region's internal crop, extension, whitespace
and typography from the source, source brief and final canvas; never alter the
50:50 split.
```

Design-only:

```text
OUTPUT MODE: DESIGN_ONLY

Create one full-canvas artwork entirely in the TRANSFORMED DESIGN language.
Use the REALITY VIEW only as the non-visible source of identity, structure,
relationships, colour logic and facts. Every visible visual element must be
part of the source brief's designed reinterpretation rather than an
untransformed presentation of the source photograph.
```

Wallpaper pack — one block per device asset:

```text
OUTPUT MODE: WALLPAPER_PACK
DEVICE PROFILE: <resolved PHONE, IPAD, DESKTOP or WATCH>
WALLPAPER RELATIONSHIP: <resolved INDEPENDENT or LINKED>

Create one full-canvas wallpaper for this device entirely in the TRANSFORMED
DESIGN language. Use the REALITY VIEW only as a non-visible reference. Recompose
the artwork for this device's canvas and usable screen space; every visible
element belongs to the designed result.
```

Append exactly one text block after the selected mode block. If the user has other explicit requirements, append those verbatim after the text block at the very end.

Prompt-generated text:

```text
TEXT MODE: ORIGINAL_PROMPT_GENERATED
TEXT LANGUAGE: <resolved language or locale>

The image model must generate any wording by following the original brief's
existing text-generation logic. Every visible word must arise naturally from
the current source image's content, atmosphere or implied meaning as interpreted
through that logic. Anything presented as factual or documentary information
must come from user-supplied, visibly readable or otherwise verified source
facts; when those facts are unavailable, use poetic non-factual wording. The
runtime shell is never a source of visible copy. Preserve the source brief's
typography, hierarchy, scale, material and placement. A source-required
oversized title must not be reduced to a tiny caption.
```

User-exact text:

```text
TEXT MODE: USER_EXACT
TEXT LANGUAGE: <resolved language or locale>
TEXT: 「<user's exact characters>」

Use the supplied text verbatim. Do not rewrite, translate, spell-correct, or add
any other wording. Typography and placement still follow the original brief.
```

Text-free:

```text
TEXT MODE: NONE
Render no letters, characters, numbers, logos, captions, labels, or pseudo-text anywhere.
```

If the user explicitly changes colour or another style variable, append that exact request at the very end, after the text block, and identify it as a user override. Do not elaborate it.

Immediately before generation, verify that the constructed prompt contains exactly one `OUTPUT MODE:` line and no instructions from an unselected mode.

## Bitmap execution

- Prefer GPT Image 2 whenever the host's built-in image capability or an already configured compatible route exposes it.
- Also support Seedance 5.0 Pro, Nano Banana Pro (Gemini Image Pro), Nano Banana 2 (Gemini Image Flash), or another compatible bitmap model only when it can preserve the reference, requested canvas, language, and multi-reference needs. Changing the model must not change this workflow or the prompt-authority boundary.
- Judge readiness by an actual image-capability check, not one missing tool or environment variable. Never name or expose a provider, endpoint, credential, header, account, route, or secret.
- If the built-in image tool is exposed, follow the installed `imagegen` Skill and make one generation/edit call per distinct asset. A wallpaper pack requires four outputs, not one contact sheet.
- If built-in generation is not exposed, run `python3 scripts/configured_imagegen.py probe`. Its sanitized result is the only allowed diagnostic surface. If ready, use `edit` with the source and a private prompt file; use `generate` only when no image reference genuinely exists.
- Do not echo a credential or full prompt in shell history or logs. Do not inspect configuration files manually. Do not modify provider, account, billing, credential, or global routing settings unless the user explicitly requests that separate change.
- If no compatible route is verified, ask the user to enable a suitable image tool or voluntarily provide an API key for the task. Never ask them to expose an existing secret, and never assert that a key is missing without a trusted sanitized result.
- Generate finished raster imagery. SVG, HTML, CSS, Canvas, diagrams, and programmatic vector drawing are not substitutes.

Use **one complete-canvas generation per output**. Give the image model the current original source, complete source-brief body, common preamble, one selected mode block, one text block and final canvas in one request; do not pre-crop the source, generate separate panels, or perform a second image-to-image style pass. Retry a failed complete canvas once from the original source by restating only a meaningful failed content or delivery constraint; never retry from the failed output.

Use `scripts/compose_panel.py` to audit the 50:50 comparison split when needed, and to assemble or preserve pixels only when generation cannot satisfy the contract or the user requires pixel-identical source preservation. The script may crop/paste/size/audit raster files; it must never invent the artwork or judge style, and its output must never become a new generation source.

For a linked wallpaper pack, generate one device image first as the visual anchor, then supply both the original source and that approved anchor to each remaining device generation. Recompose each canvas; never crop an earlier wallpaper or chain derivatives. For an independent pack, every device sees only the original source.

## Resource discipline

Generate only the outputs the current user requests. Repository samples are optional documentation, never a runtime prerequisite. See `references/sample-workflow.md` only when maintaining or creating requested sample artwork. Do not generate previews, alternative styles or automatic retries merely because this package has no sample artwork. Report a failed or uncertain acceptance check honestly and ask before extra generation beyond the agreed output count. Reuse the deterministic helpers instead of rewriting them.

## Source and output isolation

Use only sources attached to the current invocation, explicit image paths, an explicitly supplied input directory, or a prior source explicitly identified by the user as “the same image.” Scan a directory only under the directory-batch rules above; never scan Desktop, workspace roots, output folders, or unrelated directories for a substitute. Historical outputs and sample assets are not inputs unless explicitly named.

Write every selected final PNG directly inside one fresh task directory. The task directory is the only grouping layer. The numbered `SKILL.md` states the default root `~/Desktop/xxd/xxd-panel-NNN/<fresh-task>/`. Example names:

```text
source-001-photo-name-top-bottom-3x4-1536x2048.png
source-001-photo-name-left-right-3x2-2160x1440.png
source-001-photo-name-design-only-3x4-1536x2048.png
source-001-photo-name-wallpaper-linked-phone-1440x3200.png
source-001-photo-name-wallpaper-linked-ipad-2048x2732.png
source-001-photo-name-wallpaper-linked-desktop-3840x2160.png
source-001-photo-name-wallpaper-linked-watch-1024x1024.png
```

Use zero-padded source-order prefixes plus a sanitized source stem for multiple inputs, for example `source-001-street` and `source-002-flower`. Follow with the mode, then a collision-safe size label; include wallpaper relationship and device for wallpaper files. If different relative paths share a stem, retain enough path context or a short collision suffix to keep names unique. Normalize ratio separators to `x` in filenames and include exact output pixels whenever they help distinguish requested variants. Do not create source, mode, size, or device subdirectories, and do not create empty directories for unselected modes.

`--out` replaces the root but not fresh-task isolation. Reserve a collision-safe task name before generation. Do not create an automatic collage, overview, mockup, or combined preview. Return absolute PNG paths in source order, then mode order 1→4; wallpaper order is phone, iPad, desktop, watch.

## Acceptance gate

Inspect every final PNG at full size and thumbnail size. Accept only when:

- it is a fresh result from the correct current source or theme;
- mode, source visibility, whole-canvas ratio or exact pixels, count, and PNG format match the resolved runtime variables;
- the source remains recognisable and its important subject and context are not needlessly truncated, stretched or replaced;
- `top-bottom` has exactly two full-width regions split 50:50 at the vertical midpoint: faithful reality above and one unified transformed design below; there is no header, footer, centre strip, inset panel, collage, or third band outside those halves;
- `left-right` has exactly two full-height regions split 50:50 at the horizontal midpoint: faithful reality left and one unified transformed design right; it is never rotated into top-bottom, and typography never becomes a shared third band;
- `design-only` and every wallpaper contain a full-canvas transformed design: the reality source remains reference material, and no visible area presents it as an untransformed source photograph;
- the 50:50 comparison split is visibly correct; use the seam audit when needed to verify it, while using pixel-exact raster composition only when generation cannot satisfy the contract or the user requires pixel-identical source preservation;
- the transformed design comes directly from the current original source in one pass, not from an intermediate stylisation, another Panel output, an earlier result, or a sample; the sole exception is the explicitly selected linked-wallpaper anchor contract, which still includes the original source;
- source-required internal grids, frames, image containers and sidebars remain inside the designed region rather than being stripped as “extra bands”;
- the result follows `references/original-prompt/zh-CN.md`, especially its own colour, material, composition, whitespace, and typography requirements, without an outer Skill palette or added art direction;
- prompt-generated text uses the requested language, follows the source brief's own text logic and is meaningfully rooted in the current source image; anything that reads as factual or documentary information is traceable to supplied, visible or verified facts; user-exact text is verbatim with no additions; text-free output contains no text or pseudo-text; a source-required oversized title is not reduced to a tiny caption;
- linked and independent wallpaper rules are respected;
- for a directory batch, every discovered source appears exactly once in the queue, all requested outputs stay inside the one batch task directory, and the final report accounts for every success and failure;
- no SVG/code-rendered substitute, watermark, UI, route information, or secret appears.

When a result fails, retry only the failed source-brief or runtime requirement. Do not “improve” it by introducing a new aesthetic theory. A panel-specific overlay in `SKILL.md` may add further acceptance checks; it never relaxes this gate.

Before delivery or publication, clean the final images using the available `xxd-strip-ai-meta` workflow and verify the supported provenance metadata is removed. Preserve pixels and colour profiles during cleanup. This is metadata hygiene, not a claim that the artwork was not AI-generated.
