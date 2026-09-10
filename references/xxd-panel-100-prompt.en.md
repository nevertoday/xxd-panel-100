# XXD Panel 100 | Runtime Adapter (English)

This is not a second aesthetic prompt. Read `references/original-prompt/zh-CN.md` in full before generation; it is the sole creative and aesthetic authority for Panel 100. If the first Markdown heading is only an internal archival label, omit it from the image request and use the remaining source-brief body verbatim. If there is no such heading, use the entire file. This file only appends the current user's runtime variables.

See `references/soldier-runtime.md` for preflight, multi-size, multi-mode, wallpaper, execution, and output rules. `SKILL.md` supplies only this Panel's identity and overlay.

## Non-authoring boundary

- Do not summarize, translate, expand, polish, or “improve” the source brief.
- Do not add a palette plan, material plan, composition theory, whitespace rule, title, microcopy package, or aesthetic motive.
- Preserve the source brief's own colour behaviour exactly, whether it derives colour from the photograph or specifies a fixed family.
- Let the image model execute the source brief's existing text logic. The outer Skill does not pre-write copy.
- Current modes and sizes completely replace the legacy 3:4 top-bottom container, never the remaining aesthetic rules. Comparison modes always keep exact 50:50 halves.
- Append only the selected mode's block to each asset; never send the unused modes as alternatives.
- Build every ordinary asset directly from the current original source in one generation pass. Never use an intermediate stylisation, prior result, sample, or another Panel output as a second reference pass. The sole exception is an explicitly selected linked wallpaper pack.

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
COMPARISON GEOMETRY: EXACT 50:50 WHEN TOP_BOTTOM OR LEFT_RIGHT IS SELECTED
NO EXTRA OUTER REGION: no header band, footer band, centre strip, collage or third band
SOURCE-REQUIRED INTERNAL STRUCTURE: grids, frames, image containers and sidebars stay inside the TRANSFORMED DESIGN
TRANSFORMATION PASSES: ONE DIRECT PASS FROM THE CURRENT ORIGINAL SOURCE

Colour follows the original brief's existing colour instructions exactly.
Unless the user explicitly requests a colour change, do not add, replace,
summarize, or re-plan any palette.
```

## Select exactly one mode block

```text
OUTPUT MODE: TOP_BOTTOM
Create one complete canvas with exactly two full-width horizontal regions. The REALITY VIEW occupies the upper 50% and the TRANSFORMED DESIGN occupies the lower 50%, separated only at the exact vertical midpoint. Do not create a header, footer, centre strip, title band, collage, or third region outside those two halves. Keep all typography inside the lower 50%. Source-required internal grids, frames, containers and sidebars belong inside the lower 50%. Decide only the internal crop or extension, whitespace and typography inside each region; never alter the 50:50 split.
```

```text
OUTPUT MODE: LEFT_RIGHT
Create one complete canvas with exactly two full-height vertical regions. The REALITY VIEW occupies the left 50% and the TRANSFORMED DESIGN occupies the right 50%, separated only at the exact horizontal midpoint. Never rotate this into top-bottom. Do not create a header, footer, centre strip, title band, collage, or third region outside those two halves. Keep all typography inside the right 50%. Map the source brief's upper/lower positional terms to left/right while preserving its aesthetic instructions and strict equal halves. Source-required internal grids, frames, containers and sidebars belong inside the right 50%. Decide only the internal crop or extension, whitespace and typography inside each region; never alter the 50:50 split.
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
Preserve the source brief's typography, hierarchy, scale, material and placement.
A source-required oversized title must not be reduced to a tiny caption.
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

Every final generation request has this order:

```text
complete verbatim source-brief body from original-prompt/zh-CN.md, excluding only an archival first heading if present
+ common delivery preamble
+ exactly one selected mode block
+ exactly one text-mode block
+ any other explicit user requirement, verbatim, at the very end
```
