# XXD Panel 100 | Runtime Adapter (English)

This is not a second aesthetic prompt. Read `references/original-prompt/zh-CN.md` in full before generation; it is the sole creative and aesthetic authority for Panel 100. The current archive has no Markdown heading, so use the entire source brief verbatim. If a future archive adds a purely administrative heading, omit only that heading. This file only appends the current user's runtime variables.

## Non-authoring boundary

- Do not summarize, translate, expand, polish, or “improve” the source brief.
- Do not add a palette plan, material plan, composition theory, whitespace rule, title, microcopy package, or aesthetic motive.
- Preserve the source brief's own colour behaviour exactly, whether it derives colour from the photograph or specifies a fixed family.
- Let the image model execute the source brief's existing text logic. The outer Skill does not pre-write copy.
- Current modes and sizes completely replace the legacy 3:4 top-bottom container, never the remaining aesthetic rules.
- Append only the selected mode's block to each asset; never send the unused modes as alternatives.

## Common delivery preamble

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

FINAL CANVAS: <ratio and/or exact WIDTHxHEIGHT>
COMPOSITION METHOD: ONE COHERENT COMPLETE-CANVAS GENERATION
EXACT PANEL GEOMETRY: ONLY WHEN THE USER EXPLICITLY REQUESTS IT

Colour follows the original brief's existing colour instructions exactly.
Unless the user explicitly requests a colour change, do not add, replace,
summarize, or re-plan any palette.
```

## Select exactly one mode block

```text
OUTPUT MODE: TOP_BOTTOM
Create one complete canvas whose dominant structure is two primary horizontal parts: the REALITY VIEW above and the TRANSFORMED DESIGN below. Together they organize the full width. Let the image model determine visual proportions, internal crop or extension, whitespace and typography from the source, source brief and final canvas.
```

```text
OUTPUT MODE: LEFT_RIGHT
Create one complete canvas whose dominant structure is two primary vertical parts: the REALITY VIEW left and the TRANSFORMED DESIGN right. Together they organize the canvas from top edge to bottom edge; all visible material and typography belongs within this left-right structure. Let the image model choose asymmetric widths, internal crop or extension and whitespace.
```

```text
OUTPUT MODE: DESIGN_ONLY
Create one full-canvas artwork entirely in the TRANSFORMED DESIGN language. Use the REALITY VIEW only as the non-visible source of identity, structure, relationships, colour logic and facts. Every visible element belongs to the source brief's designed reinterpretation rather than an untransformed presentation of the source photograph.
```

```text
OUTPUT MODE: WALLPAPER_PACK
DEVICE PROFILE: <resolved PHONE, IPAD, DESKTOP or WATCH>
WALLPAPER RELATIONSHIP: <resolved INDEPENDENT or LINKED>
Create one full-canvas wallpaper for this device entirely in the TRANSFORMED DESIGN language. Use the REALITY VIEW only as a non-visible reference. Recompose for the device canvas and usable screen space; every visible element belongs to the designed result.
```

Append exactly one text block after the selected mode block. If the user has other explicit requirements, append those verbatim after the text block at the very end.

### Text generated from the original prompt

```text
TEXT MODE: ORIGINAL_PROMPT_GENERATED
TEXT LANGUAGE: <user-confirmed language or locale>

The image model generates wording by following the original brief's existing
text-generation logic. Every visible word must arise naturally from the current
source image's content, atmosphere or implied meaning. Anything presented as
factual or documentary information must come from user-supplied, visibly readable
or otherwise verified source facts; when those facts are unavailable, use poetic
non-factual wording. The runtime shell is never a source of visible copy.
```

### User-exact text

```text
TEXT MODE: USER_EXACT
TEXT LANGUAGE: <user-confirmed language or locale>
TEXT: “<user's exact characters>”

Use the supplied text verbatim. Do not rewrite, translate, spell-correct, or add
any other wording. Typography and placement still follow the original brief.
```

### No text

```text
TEXT MODE: NONE
Render no letters, characters, numbers, titles, labels, logos, or pseudo-text anywhere.
```

See `SKILL.md` for preflight, multi-size, multi-mode, wallpaper, execution, and output rules. Every final generation request has this order:

```text
complete verbatim source-brief body from original-prompt/zh-CN.md (all current content)
+ common delivery preamble
+ exactly one selected mode block
+ exactly one text-mode block
+ any other explicit user requirement, verbatim, at the very end
```
