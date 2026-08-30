<p align="center"><img src="./assets/banner.svg" alt="XXD Panel 100 project banner" width="1200"></p>

<div align="center">

# 🦁 XXD Panel 100

### Turn a photograph into tactile, naïve folk narrative art

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-000000?style=flat-square)](./SKILL.md)
[![Modes](https://img.shields.io/badge/Modes-4-EF805E?style=flat-square)](#)
[![Output](https://img.shields.io/badge/Output-PNG-4AA1AE?style=flat-square)](#)

<a href="README.md">简体中文</a> · <strong>English</strong> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

## Samples

The sample area is reserved in two verified sets: `sample-05`–`sample-08` are four independent 16:9 horizontal left-right compositions (`1536×864`), and `sample-09`–`sample-12` are four independent 3:4 vertical top-bottom compositions (`1536×2048`). Each must be generated directly from the Panel 100 source brief; actual raster samples are not bundled yet, and no other Panel or SVG placeholder will be substituted.

<!-- xxd-human-intro:start -->
## What it solves

**Panel 100** distils the source's most memorable subject, action, and relationship into naïve silhouettes, primitive forms, and a few folk symbols. Crayon, oil-pastel, and coarse-pencil grain keep the surface tactile while the photograph's liveliest colours become a concise, bright palette.

### Best for

- simplifying a photograph without losing its emotional and narrative core;
- lively source-derived colour, imperfect hand-made marks, and clear paper breathing space;
- whimsical subjects, everyday memories, cultural stories, and gentle visual humour;
- top-bottom, left-right, design-only, multi-ratio, wallpaper, and directory-batch delivery.

### Quick start

> Use XXD Panel 100 on this image and recommend the most suitable composition and size first.

<!-- xxd-human-intro:end -->

## Original prompt · Five languages

[简体中文](references/original-prompt/zh-CN.md) · [English](references/original-prompt/en.md) · [日本語](references/original-prompt/ja.md) · [한국어](references/original-prompt/ko.md) · [العربية](references/original-prompt/ar.md)

The Chinese file preserves the user's wording verbatim and is the sole runtime creative authority. The other four files are faithful reading translations and never rewrite the generation prompt.

**Signature:** Naïve folk narrative · primitive forms · flattened perspective · crayon grain · limited colour · folk editorial type

<!-- xxd-panel-benefit:start -->
## Quick fit check

| What you need to know | What this style gives you |
|---|---|
| **What you get** | A folk-editorial poster where rough silhouettes, hand-made grain, and everyday narrative work as one |
| **Recognisable signature** | primitive forms, flat space, crayon grain, warm paper, sparse colour accents, and folk lettering |
| **How it respects the source** | Subject, pose, and story relationship remain recognisable while redundant detail is removed |
| **Where it works** | Art posters, covers, social content, design-only art, multiple ratios, and four-device wallpaper sets |
<!-- xxd-panel-benefit:end -->

## Transformation logic

```text
read subject and relationship → remove complex background → compress into naïve silhouettes and primitive forms → retell through flattened perspective → derive a few vivid source colours → finish with dry-media grain and folk-editorial lettering
```

## Recognisable finished traits

- Simplified silhouettes and large primitive forms preserve identity while allowing compressed proportions and witty exaggeration.
- Dark areas retain rubbing, layering, breaks, and paper show-through rather than smooth uniform fills.
- Warm paper and dark silhouettes anchor a few vivid source-derived accents.
- Text enters like a sign, menu, note, or publication annotation rather than a commercial title bar.
- Avoid children's cartoons, cute stickers, realism, smooth vectors, complex perspective, 3D, and template effects.

All aesthetic constraints live only in the [canonical prompt](references/original-prompt/zh-CN.md). The Skill and runtime adapters resolve delivery variables. [Skill workflow](SKILL.md) · [English runtime adapter](references/xxd-panel-100-prompt.en.md)

<details>
<summary><strong>Full capabilities and parameters (open when needed)</strong></summary>

## The original brief is authoritative

`references/original-prompt/zh-CN.md` is this project's sole creative and aesthetic authority. The Skill no longer summarizes or expands it, and it does not impose a shared palette, colour plan, aesthetic motive, title, or microcopy package. GPT Image 2 follows that brief's own rules for colour, material, composition, whitespace, wording, and typography.

Mode and size completely replace the legacy 3:4 top-bottom delivery container without rewriting the transformation aesthetic. Each asset sends GPT Image 2 one selected mode's final contract instead of asking it to interpret four alternatives inside a generic template.

## Four combinable output modes

Select one or more of `top-bottom`, `left-right`, `design-only`, and `wallpaper-pack`. When several are selected, each is generated independently with its own prompt.

- `top-bottom`: one complete canvas with the reality view above and transformed design below.
- `left-right`: one complete canvas whose left-right structure runs from top edge to bottom edge, source left and design right. Typography stays inside that structure rather than creating a shared third footer; widths may be asymmetric.
- `design-only`: the source is a non-visible reference for identity, structure, colour logic, and facts; every visible element follows this Panel's transformation language.
- `wallpaper-pack`: each device receives an independently composed full-canvas transformed wallpaper, with no source-photo region.

There is no seam, midpoint-percentage, or pixel-coordinate test. Deterministic assembly is used only when the user explicitly requests exact panel geometry or pixel-identical source preservation.

Ordinary sizes are also multi-select: auto-fit, source aspect, 1:1, 3:4, 4:3, 4:5, 5:4, 2:3, 3:2, 9:16, 16:9, 21:9, 5:7, 7:5, or custom ratios/exact pixels. There is no silent default. Every distinct aspect is independently recomposed from the same verbatim source brief.

Wallpaper packs may be linked or independent. A linked pack creates one anchor image, then recomposes each remaining device from the original source plus that anchor; it never crops one image into four sizes.

Each invocation creates one task directory and writes every final PNG directly into it, with no source, mode, size, or device subfolders. Filenames include source order and a sanitized source name, for example `source-001-street-left-right-3x2-2160x1440.png` and `source-001-street-wallpaper-linked-phone-1440x3200.png`.

Pass an image directory directly to batch-process it with this same Soldier. Every discovered image keeps Panel 100's one original aesthetic. The Skill recursively inventories common raster formats, reports the count, resolves shared mode/size/text/locale settings once, and then generates each source independently without content or copy leaking between items. The whole batch still uses one flat task directory; an individual failure is recorded without silently dropping later images.

## Text modes

Before generation, resolve one of three choices:

1. **Model generates text from the original prompt**: the user supplies only the language or locale; GPT Image 2 follows the source brief's wording, amount, tone, and typography logic. Every word arises from the current image's content, atmosphere, or implied meaning, and anything presented as factual or documentary information must be grounded in supplied, visible, or verified facts.
2. **Use my exact text**: pass it verbatim, without rewriting, translating, or adding a title; typography still follows the source brief.
3. **No text**: prohibit visible text and pseudo-text.

The outer Skill no longer pre-writes titles, microcopy, or copy packages. Output language is resolved separately from the interface language and is never guessed from a person, scene, or filename.

## Complete-canvas first, raster-only delivery

The image model owns the aesthetics of the entire finished composition; paired layouts also default to one complete-canvas generation. `scripts/compose_panel.py` remains only for condition-based recovery, lossless pixel calibration, and read-only audit. It is not run pre-emptively and does not judge aesthetic success.

Every deliverable is a raster PNG and every invocation creates a fresh task under `~/Desktop/xxd/`. The configured image route exposes sanitised status only—never providers, endpoints, credentials, headers, prompts, responses, or account details. SVG, HTML, Canvas, diagrams, and programmatic drawing are not substitutes for the final artwork.

## Capability-adaptive questions and inline parameters

The same Skill adapts to the host's real interaction capabilities and never presents decorative symbols as clickable controls:

- **When Claude Code exposes `AskUserQuestion + multiSelect: true`**: modes and sizes use genuine checkboxes; text mode and wallpaper relationship use single-select. Common sizes are grouped into square, portrait, and landscape checkbox questions, selections accumulate across groups, and custom sizes use free input.
- **When Codex exposes only `request_user_input`**: use it only for mutually exclusive fields such as text mode and wallpaper relationship. Do not misrepresent modes or sizes as single-choice; collect them through clear combination input.
- **With no interactive question tool**: use two typed rounds—modes first, then sizes plus text. Never draw fake `- [ ]` boxes or ask the user to switch to Plan mode merely to obtain a form.

The second round initially shows only Smart recommendation, Source aspect, Common ratios, and Custom. Expand the full library only when requested: square `1:1`; portrait `3:4, 4:5, 2:3, 9:16, 5:7`; landscape `4:3, 5:4, 3:2, 16:9, 21:9, 7:5`. Any ratios may be combined, and exact pixels are always accepted.

All settings can also be passed inline:

```text
/xxd-panel-100 photo.jpg --mode top-bottom,design-only --size auto,3:4,9:16 --text prompt --locale ja-JP
```

Supported parameters are `--mode`, repeatable or comma-separated `--size`, `--text prompt|exact|none`, `--locale`, `--copy`, `--wallpaper linked|independent`, `--wallpaper-size`, `--out`, and `--prefs`. Complete parameters skip preflight; partial parameters trigger only missing questions.

### Reuse the last preference or start fresh

When a valid preference exists and this invocation still has unresolved delivery settings, the Skill summarises the previous modes, sizes, text and locale, wallpaper relationship, and output location, then offers three mutually exclusive choices: **Reuse**, **Reuse and edit**, or **Fresh configuration**. Explicit current requirements always win, and complete parameters still run without redundant questions.

Use `--prefs last|edit|new|off|clear` to choose the route inline:

```text
/xxd-panel-100 photo.jpg --prefs last
/xxd-panel-100 photo.jpg --prefs edit
/xxd-panel-100 photo.jpg --prefs new
```

The record stores delivery settings only. It never stores source images, exact copy, generated results, Panel choices, model routes, API credentials, or other sensitive information.

Replace `photo.jpg` with an image-directory path to enter batch processing automatically; no separate `--batch` switch is required.

### Parameter quick reference

| Parameter | Purpose | Common values or format |
|---|---|---|
| `--mode` | Select one or more deliverable types | `top-bottom`, `left-right`, `design-only`, `wallpaper-pack` |
| `--size` | Select ordinary-output ratios or exact pixels; accepts several | `auto`, `source`, `3:4`, `9:16`, `2160x3840` |
| `--text` | Choose the source of visible text | `prompt`, `exact`, `none` |
| `--locale` | Set the language or locale of visible text | `zh-CN`, `en-GB`, `ja-JP`, `ko-KR`, `ar-SA` |
| `--copy` | Pass user wording verbatim and imply `--text exact` | `--copy "Exact wording"` |
| `--wallpaper` | Set the relationship among four wallpapers | `linked`, `independent` |
| `--wallpaper-size` | Override pixel sizes by device | `phone=...`, `ipad=...`, `desktop=...`, `watch=...` |
| `--out` | Set an output root; a fresh task folder is still created | folder path |
| `--prefs` | Reuse, edit, replace, disable, or clear the last preference | `last`, `edit`, `new`, `off`, `clear` |

Replace `photo.jpg` with a local path, uploaded image, image directory, or another source explicitly supplied by the user. A directory enters batch processing automatically.

### Copyable commands by use case

```text
# Top-bottom comparison, auto canvas, prompt-generated British English
/xxd-panel-100 photo.jpg --mode top-bottom --size auto --text prompt --locale en-GB

# Left-right comparison, 3:2 landscape, no text
/xxd-panel-100 photo.jpg --mode left-right --size 3:2 --text none

# Design-only, 9:16 phone portrait, Japanese text
/xxd-panel-100 photo.jpg --mode design-only --size 9:16 --text prompt --locale ja-JP

# Linked wallpaper pack: establish one anchor, then recompose every device
/xxd-panel-100 photo.jpg --mode wallpaper-pack --wallpaper linked --text none

# Independent wallpapers with exact device resolutions
/xxd-panel-100 photo.jpg --mode wallpaper-pack --wallpaper independent --wallpaper-size phone=1440x3200,ipad=2048x2732,desktop=3840x2160,watch=1024x1024 --text none

# Follow the source image's aspect ratio
/xxd-panel-100 photo.jpg --mode design-only --size source --text none

# Create square, portrait, and landscape compositions
/xxd-panel-100 photo.jpg --mode design-only --size 1:1,3:4,16:9 --text none

# Combine a custom ratio with exact pixel targets
/xxd-panel-100 photo.jpg --mode design-only --size 11:14,2160x3840,3840x2160 --text none

# Let the original prompt generate wording; constrain only the locale
/xxd-panel-100 photo.jpg --mode design-only --size 3:4 --text prompt --locale en-GB

# Use exact copy without rewriting, translating, or adding a title
/xxd-panel-100 photo.jpg --mode design-only --size 3:4 --copy "Let the light stay" --locale en-GB

# Two modes × three sizes produce six independently composed assets
/xxd-panel-100 photo.jpg --mode top-bottom,design-only --size 1:1,3:4,9:16 --text prompt --locale en-GB

# Apply Panel 100 to a whole directory; shared settings resolve once
/xxd-panel-100 "/path/to/photos" --mode design-only --size auto,9:16 --text prompt --locale en-GB

# Repeated parameters accumulate; place the task under a chosen root
/xxd-panel-100 photo.jpg --mode top-bottom --mode left-right --size 3:4 --size 16:9 --text none --out ./deliveries
```

## Image-model priority

GPT Image 2 is the default first choice. It keeps this project's established workflow: high-fidelity source reference, explicit whole-canvas selection before generation, one complete-canvas generation for paired modes, and scripted composition only as a conditional fallback.

Seedance 5.0 Pro, Nano Banana Pro (Gemini Image Pro), Nano Banana 2 (Gemini Image Flash), or another compatible bitmap model may also be used when it is actually available through the current tools or configured routes and can satisfy source fidelity, whole-canvas ratio, target-language text, and linked-wallpaper multi-reference requirements. An alternative changes only the generation route; it must not change modes, canvas, copy, locale, wallpaper relationship, or the complete-canvas-first strategy.

If no suitable route is available, the Skill asks the user to enable an image-generation tool or provide an API key. User-provided credentials may be used for the current task without being echoed, displayed, logged, or exposed. They are not persisted, and provider, account, billing, or global route configuration is not modified, unless the user explicitly requests that configuration change.

</details>

## Get started

```bash
git clone https://github.com/nevertoday/xxd-panel-100.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-100" ~/.codex/skills/xxd-panel-100
```

Claude Code users may link the same folder under `~/.claude/skills/xxd-panel-100`. Restart the agent session after installation.

```text
$xxd-panel-100
Use this photograph, ask me for the modes and copy setting, then generate fresh raster outputs.
```

Full specifications: [Skill workflow](SKILL.md) · [source archive](references/original-prompt/zh-CN.md) · [English runtime adapter](references/xxd-panel-100-prompt.en.md) · [Chinese runtime adapter](references/xxd-panel-100-prompt.zh-CN.md)

<!-- xxd-panel-catalog:start -->
## Complete XXD Panel catalog

Each of the 60 Panels preserves its own original brief and aesthetic logic. The table lists every project address and its defining style characteristics; the current project is bold.

| Project | Style characteristics |
|---|---|
| [xxd-panel-001](https://github.com/nevertoday/xxd-panel-001) | NAÏVE LINE · RETRO PAPER · MIXED MEDIA · WITTY METAPHOR · WARM SPACE |
| [xxd-panel-002](https://github.com/nevertoday/xxd-panel-002) | NARRATIVE CONTOUR · HESITANT LINE · ANALOGOUS COLOUR · SELECTIVE ENLARGEMENT · MISREGISTERED TYPE |
| [xxd-panel-003](https://github.com/nevertoday/xxd-panel-003) | CONTINUOUS BLACK LINE · PUBLIC ISSUE · FORCE POINTS · SILENT SPACE · RELEASE |
| [xxd-panel-004](https://github.com/nevertoday/xxd-panel-004) | LOCAL REALITY · PRECISE SINGLE LINE · GEOMETRIC PERSPECTIVE · THEME COLOUR · CITY-BRAND TYPE |
| [xxd-panel-005](https://github.com/nevertoday/xxd-panel-005) | BLUNT MASSES · DARK STRUCTURAL FIELD · PARTIAL REVEAL · THREE-LAYER COLOUR · SCREENPRINT × PASTEL |
| [xxd-panel-006](https://github.com/nevertoday/xxd-panel-006) | 10–20% SUBJECT · 80–90% PAPER · FINE HAND LINE · FOUR COLOURS MAX · FLAT ACRYLIC |
| [xxd-panel-007](https://github.com/nevertoday/xxd-panel-007) | OBJECT-LIKE MINIATURES · CLOSE-UP / SECTION / REPEAT · STAGGERED PAPER · THIN BLACK NOTES |
| [xxd-panel-008](https://github.com/nevertoday/xxd-panel-008) | ORTHOGRAPHIC ISOMETRIC · PLATFORMS / STAIRS / DOORS · SPATIAL PARADOX · DYNAMIC PASTELS · MATTE 3D |
| [xxd-panel-009](https://github.com/nevertoday/xxd-panel-009) | TINY ANCHOR · VAST NEGATIVE SPACE · ONE SPATIAL RELATION · SPOT COLOUR · HALFTONE SCREENPRINT |
| [xxd-panel-010](https://github.com/nevertoday/xxd-panel-010) | ROUGH BLACK SILHOUETTE · WHITE FEATURE CUTOUT · DRY-MEDIA PAPER · SPARSE SETTING MARKS · PICTURE-BOOK TYPE |
| [xxd-panel-011](https://github.com/nevertoday/xxd-panel-011) | ONE CORE IMAGE · ONE RELATION · CONTINUOUS BLACK LINE · ACTIVE SILENCE · ONE MEMORY COLOUR |
| [xxd-panel-012](https://github.com/nevertoday/xxd-panel-012) | DENSE EMERGENCE · SPARSE DIFFUSION · GEOMETRIC RESTRAINT · ONE VITAL COLOUR · BLACK-GREY MICROTYPE |
| [xxd-panel-013](https://github.com/nevertoday/xxd-panel-013) | ONE HORIZONTAL TICKET · 74/26 SPLIT · HEALING WATERCOLOUR · IVORY SPACE · LOCALISED INFORMATION STUB |
| [xxd-panel-014](https://github.com/nevertoday/xxd-panel-014) | FOLD AND FACET · LAYER AND NEST · SOURCE-LED WEIGHT · REAL PAPER FIBRE · READABLE PAPER TYPE |
| [xxd-panel-015](https://github.com/nevertoday/xxd-panel-015) | DECONSTRUCT–SELECT–DISTIL–RECONSTRUCT · FEW FORMS · STRICT COLOUR ROLES · IVORY SPACE · ART-BOOK MICROTYPE |
| [xxd-panel-016](https://github.com/nevertoday/xxd-panel-016) | ONE SUBJECT · ONE MOTION · A LARGE FIELD OF AIR |
| [xxd-panel-017](https://github.com/nevertoday/xxd-panel-017) | ROUNDED FORM · ROUGH BROKEN LINE · PURE FLAT FILL · BRIGHT FIELDS · LIVELY ASYMMETRY |
| [xxd-panel-018](https://github.com/nevertoday/xxd-panel-018) | ONE VISUAL ANCHOR · FEW DEPTH LAYERS · WARM-IVORY SPACE · MATTE PAPER · COMPLETE MICROTYPE |
| [xxd-panel-019](https://github.com/nevertoday/xxd-panel-019) | RECOGNISE FIRST · REDUCE WITH INTENT · COMPOSE WITH TYPE |
| [xxd-panel-020](https://github.com/nevertoday/xxd-panel-020) | IMPASTO ISLAND · DIMENSIONAL MINIATURE · REAL KNIFE MARKS · GENEROUS PAPER SPACE · RESTRAINED EDITORIAL TYPE |
| [xxd-panel-021](https://github.com/nevertoday/xxd-panel-021) | PURE-BLACK RECTANGLE · SUBJECT MOSTLY INSIDE · ONE FEATURE BREAKS OUT · JITTERY PHOTOCOPY LINE · WHITE NEGATIVE FORM |
| [xxd-panel-022](https://github.com/nevertoday/xxd-panel-022) | PURE-BLACK RECTANGLE · SUBJECT MOSTLY INSIDE · ONE FEATURE BREAKS OUT · CLEAN ELASTIC LINE · ONE COLOUR SIGNAL |
| [xxd-panel-023](https://github.com/nevertoday/xxd-panel-023) | SOURCE-CHOSEN WINDOW · PALE BREATHING GROUND · LIVING COLOURED LIGHT · SPRAY GRAIN · DIFFUSE PROJECTION |
| [xxd-panel-024](https://github.com/nevertoday/xxd-panel-024) | PHOTOGRAPHIC SUBJECT · NARROW PALE WINDOW · SOURCE-ADAPTIVE DIRECTION · EASTERN WHITESPACE · PREMIUM EDITORIAL TYPE |
| [xxd-panel-025](https://github.com/nevertoday/xxd-panel-025) | FIRST-GLANCE SUBJECT · SECOND-GLANCE IMAGE · FIGURE–GROUND REVERSAL · 2–4 MORANDI COLOURS · PHYSICAL SCREENPRINT |
| [xxd-panel-026](https://github.com/nevertoday/xxd-panel-026) | RECOGNISE QUIETLY · REDUCE GENTLY · LET THE PAPER BREATHE |
| [xxd-panel-027](https://github.com/nevertoday/xxd-panel-027) | HEAVY IVORY PAPER · EMBOSS AND DEBOSS · FINE INCISION · MATTE-GOLD FOCUS · MUSEUM ORDER |
| [xxd-panel-028](https://github.com/nevertoday/xxd-panel-028) | ORTHOGRAPHIC ISOMETRIC · SMALL PAPER BASE · SOURCE-DERIVED PALETTE · FINE INK · EDITORIAL MODEL |
| [xxd-panel-029](https://github.com/nevertoday/xxd-panel-029) | HORIZONTAL FIELD · LIGHT WAX PASTEL · ROUGH HANDMADE PAPER · RISOGRAPH GRAIN · RELAXED HANDWRITING |
| [xxd-panel-030](https://github.com/nevertoday/xxd-panel-030) | REAL BOTANICAL MATERIAL · RECTANGULAR FIELD · NATURAL CROSSING · MINIMAL BLACK LINE · EDITORIAL WHITESPACE |
| [xxd-panel-031](https://github.com/nevertoday/xxd-panel-031) | ONE CORE MOTIF · SOURCE-DERIVED GEOMETRY · FOLK CATALOGUE · ROUGH INTERNAL INK · CRISP ORDER |
| [xxd-panel-032](https://github.com/nevertoday/xxd-panel-032) | TEXT–IMAGE UNITY · NATIVE LETTERING · SOURCE FEATURE · OPTICAL SPACING · GENEROUS WHITESPACE |
| [xxd-panel-033](https://github.com/nevertoday/xxd-panel-033) | RECOGNISABLE MOTIF · LAYERED COLLAGE · SCALE CONTRAST · VIVID SOURCE COLOUR · COVER TYPE |
| [xxd-panel-034](https://github.com/nevertoday/xxd-panel-034) | SMALL STAMP · 2–4 SPOT INKS · HAND-CARVED LINE · WARM PAPER · FIELD ANNOTATION |
| [xxd-panel-035](https://github.com/nevertoday/xxd-panel-035) | ONE BLOCK SUBJECT · VIVID SOURCE COLOUR · MATTE ABS · QUIET FIELD · MODULAR TYPE |
| [xxd-panel-036](https://github.com/nevertoday/xxd-panel-036) | ONE RELATION · FINE LINE · 2–4 COLOUR FIELDS · WATERCOLOUR EDGE · BREATHING SPACE |
| [xxd-panel-037](https://github.com/nevertoday/xxd-panel-037) | ONE BADGE · SOURCE ENAMEL · WHITE-METAL RIM · GILDED DETAIL · REAL SHADOW |
| [xxd-panel-038](https://github.com/nevertoday/xxd-panel-038) | SOURCE FABRIC · FRAYED EDGE · HAND STITCH · ACTIVE WHITESPACE · HIDDEN FEELING |
| [xxd-panel-039](https://github.com/nevertoday/xxd-panel-039) | ONE IMAGE · ONE ESSENCE · SILK DIRECTION · CLEAN GROUND · EASTERN SILENCE |
| [xxd-panel-040](https://github.com/nevertoday/xxd-panel-040) | TRUTHFUL ANCHOR · BLACK-LINE FIGURES · MICRO-NARRATIVE · ACTIVE WHITESPACE |
| [xxd-panel-041](https://github.com/nevertoday/xxd-panel-041) | THEME METAPHOR · ISOMETRIC ORDER · PALE MANUSCRIPT · JAPANESE COLOUR · EASTERN SPACE |
| [xxd-panel-042](https://github.com/nevertoday/xxd-panel-042) | ORIGINAL VIEW · 2–5 TRUE LAYERS · STABLE ANCHOR · TRANSLUCENT WATERCOLOUR · EDITORIAL NOTE |
| [xxd-panel-043](https://github.com/nevertoday/xxd-panel-043) | REAL LATHER · FRONTAL FLAT-LAY · SOURCE-DARK GROUND · MICRO-BUBBLE EDGE · QUIET SPACE |
| [xxd-panel-044](https://github.com/nevertoday/xxd-panel-044) | THIN GOLD · FRONTAL PLANE · SOURCE-DARK GROUND · HAMMERED TRACE · QUIET ORDER |
| [xxd-panel-045](https://github.com/nevertoday/xxd-panel-045) | ROUNDED MODULE · SOURCE COLOUR · ISOMETRIC DEPTH · MATTE TOUCH · EDITORIAL MICROTYPE |
| [xxd-panel-046](https://github.com/nevertoday/xxd-panel-046) | BRIGHT GROUND · VIVID IMPASTO · MINIATURE VOLUME · DIAGONAL FIELD · WARM LIGHT |
| [xxd-panel-047](https://github.com/nevertoday/xxd-panel-047) | ISOMETRIC MINIATURE · THEMATIC IMPASTO · REAL CONTACT · WARM-WHITE PAPER · LUMINOUS COLOUR |
| [xxd-panel-048](https://github.com/nevertoday/xxd-panel-048) | TRANSPARENT STRUCTURE · SCIENTIFIC ILLUSTRATION · LUCID MONOCHROME · PRECISE ANNOTATION · EDITORIAL SPACE |
| [xxd-panel-049](https://github.com/nevertoday/xxd-panel-049) | LIMITED-COLOUR WOODCUT · HAND-CARVED MARKS · MATTE INK · WARM PAPER · BROKEN EDGES |
| [xxd-panel-050](https://github.com/nevertoday/xxd-panel-050) | BESPOKE TRAVEL SCENE · AIRY BLUE · MINIMAL FLAT VECTOR · EDITORIAL WHITESPACE · ONE IMAGE, ONE IDENTITY |
| [xxd-panel-051](https://github.com/nevertoday/xxd-panel-051) | MINIATURE PAPER CRAFT · HORIZONTAL FLOATING LANDSCAPE · HANDMADE EVIDENCE · AIRY BLUE · VAST WHITESPACE |
| [xxd-panel-052](https://github.com/nevertoday/xxd-panel-052) | PAPER-CRAFT MINIATURE · HORIZONTAL FLOATING STRIP · HANDMADE MATERIAL · AIRY COOL BLUE · GENEROUS SPACE |
| [xxd-panel-053](https://github.com/nevertoday/xxd-panel-053) | OBSERVATIONAL PEN · TRANSPARENT WASH · MUSICAL RHYTHM · NEAR-WHITE PAPER · ACTIVE WHITESPACE |
| [xxd-panel-054](https://github.com/nevertoday/xxd-panel-054) | SELECTIVE MEMORY · MAIN VISUAL · SIX STICKERS · MATTE PRINT · AIRY BLUE |
| [xxd-panel-055](https://github.com/nevertoday/xxd-panel-055) | SUBJECT NARRATIVE · HEALING PASTELS · LIGHT OIL TEXTURE · AIRY BLUE · EDITORIAL SPACE |
| [xxd-panel-056](https://github.com/nevertoday/xxd-panel-056) | CORE IMAGE · VAST WHITESPACE · WARM–COOL JUMPS · NAIVE HAND · VISUAL METAPHOR |
| [xxd-panel-057](https://github.com/nevertoday/xxd-panel-057) | GEOMETRIC COMPOSITION · INTELLIGENT MOSAIC · ARCHITECTURAL DIAGRAM · ART MAP · WARM–COOL FIELDS |
| [xxd-panel-058](https://github.com/nevertoday/xxd-panel-058) | SUBTEXT READING · GEOMETRIC MINIMALISM · CONCEPTUAL LANDSCAPE · SOFT HANDMADE TEXTURE · PALE SPACE |
| [xxd-panel-059](https://github.com/nevertoday/xxd-panel-059) | HAND-DRAWN STORYTELLING · CHILDLIKE METAPHOR · WARM PAPER · GENTLE HUMOUR · POETIC ASIDE |
| [xxd-panel-060](https://github.com/nevertoday/xxd-panel-060) | BLACK PRIMARY FORM · IMMENSE NEGATIVE SPACE · HALFTONE DISSOLUTION · ZEN REFLECTION · FRAGMENTS OF THOUGHT |
| [xxd-panel-061](https://github.com/nevertoday/xxd-panel-061) | SELECTIVE MEMORY · 3–6 FRAGMENTS · CUT-PAPER COLOUR · RISOGRAPH · IMPROVISED EDITORIAL LAYOUT |
| [xxd-panel-062](https://github.com/nevertoday/xxd-panel-062) | MINIMAL BLACK LINE · ONE ACCENT COLOUR · CLEVER AWKWARDNESS · PALE PAPER · PROFESSIONAL WHITESPACE |
| [xxd-panel-063](https://github.com/nevertoday/xxd-panel-063) | CORE MASK · PIXEL FORMS · NESTED NEGATIVE SPACE · SUBTLE GLITCH · LIMITED PALETTE |
| [xxd-panel-064](https://github.com/nevertoday/xxd-panel-064) | TORN PAPER · AGED COLLAGE · PENCIL AND INK · TYPEWRITER MICROCOPY · POETIC ARCHIVE |
| [xxd-panel-065](https://github.com/nevertoday/xxd-panel-065) | BLACK STRUCTURE · TWO SOURCE-COLOUR LINES · MISREGISTRATION · VINTAGE PRINT RHYTHM · MICROTYPE |
| [xxd-panel-066](https://github.com/nevertoday/xxd-panel-066) | CHILDLIKE NARRATIVE · AWKWARD BLACK LINE · 3–6 FLAT COLOURS · HEALING PALETTE · HANDWRITTEN OBSERVATION |
| [xxd-panel-067](https://github.com/nevertoday/xxd-panel-067) | FIXED RED–BLUE INK · HAND-DRAWN DUAL INK · CHILDLIKE HUMOUR · EVERYDAY OBSERVATION · PALE PAPER |
| [xxd-panel-068](https://github.com/nevertoday/xxd-panel-068) | CHINESE XIEYI PLACEMENT · WHITE AS INK · INK LINE AND PALE COLOUR · INSCRIPTION TYPE · MODERN EDITORIAL |
| [xxd-panel-069](https://github.com/nevertoday/xxd-panel-069) | BROAD-BRUSH WINDOW · VITAL SOURCE COLOUR · FINE CONTOURS · BOUNDARY CROSSINGS · WARM-WHITE SPACE |
| [xxd-panel-070](https://github.com/nevertoday/xxd-panel-070) | HAND-DRAWN CONTOURS · BRIGHT IMPASTO／TRANSLUCENT COLOUR · MINIATURE SUBJECT · WARM-WHITE SPACE · TYPEWRITER EDITORIAL TYPE |
| [xxd-panel-071](https://github.com/nevertoday/xxd-panel-071) | SOFT PASTEL · PASTEL CRAYON · SOLUBLE PENCIL · NEAR-WHITE PAPER · FLOATING MEMORIES · POETIC HANDWRITING |
| [xxd-panel-072](https://github.com/nevertoday/xxd-panel-072) | TRANSLUCENT FROSTED WINDOWS · REGIONAL SOFT FOCUS · MINIMAL GEOMETRY · RECOGNISABLE SILHOUETTE · MODERN TYPE |
| [xxd-panel-073](https://github.com/nevertoday/xxd-panel-073) | ISOMETRIC MINIATURE ARCHITECTURE · CUT CUBE · CONTINENTAL-SHELF SECTION · RATIONAL SCAFFOLDING · TEXTURED PAPER |
| **[xxd-panel-074](https://github.com/nevertoday/xxd-panel-074)** | STANDARD ROUNDED SQUARE · FRONT PSEUDO-3D／2.5D · SOURCE-SOUL EXTRACTION · MATTE SCULPTURE · BRAND ICON |
| **[xxd-panel-075](https://github.com/nevertoday/xxd-panel-075)** | DARK CRAYON · IVORY HANDMADE PAPER · SOFT IRREGULAR FIELD · RISOGRAPH GRAIN · WHITESPACE · PRIVATE TYPEWRITER NOTE |
| **[xxd-panel-076](https://github.com/nevertoday/xxd-panel-076)** | ROUGH DARK CRAYON · CHARCOAL · BRIGHT MACARON BLOCKS · 45% CONTINUOUS WHITESPACE · NATURAL PAPER · OBSERVATION NOTES |
| **[xxd-panel-077](https://github.com/nevertoday/xxd-panel-077)** | MINIMAL PAPER SCULPTURE · CLEAR CUT-PAPER CONTOUR · LAYERED PLANES · SOFT SHADOW · HUMANIST MACARON · TRAVEL EDITORIAL |
| **[xxd-panel-078](https://github.com/nevertoday/xxd-panel-078)** | IVORY COTTON PAPER · DEEP DEBOSS · RECESSED CHAMPAGNE FOIL · FINE-LINE MARK · BLIND PRESSURE · UNDERSTATED LUXURY |
| **[xxd-panel-079](https://github.com/nevertoday/xxd-panel-079)** | GEOMETRIC STRAIGHTS · FREE ORGANIC CURVES · PEN AND WASH · UNFINISHED QUALITY · BROAD PAPER WHITE · EDITORIAL TYPE |
| **[xxd-panel-080](https://github.com/nevertoday/xxd-panel-080)** | SOFT ORGANIC GEOMETRY · DIGITAL GOUACHE · CRAYON GRAIN · BOTANICAL COLOUR · SOURCE-BORN METAPHOR · EMOTIONAL SPACE |
| **[xxd-panel-081](https://github.com/nevertoday/xxd-panel-081)** | EVEN-WEIGHT COLOURED MONOLINE · OPEN CONTOUR · DENSITY HIERARCHY · 2–4 SPOT INKS · RISOGRAPH GRAIN · KEEPSAKE NARRATIVE |
| **[xxd-panel-082](https://github.com/nevertoday/xxd-panel-082)** | IRREGULAR WATERCOLOUR FIELD · NAÏVE + WONKY · ISOMETRIC／2.5D · CHILDLIKE CONTOUR · VIVID COLOUR · SPATIAL PROTAGONIST |
| **[xxd-panel-083](https://github.com/nevertoday/xxd-panel-083)** | UGLY-CUTE DOODLE · WONKY TREMBLING CONTOUR · CONTROLLED WRONGNESS · ONE COMIC PROTAGONIST · ROUGH CRAYON · SPARSE-STRANGE-CLUMSY-ACCURATE |
| **[xxd-panel-084](https://github.com/nevertoday/xxd-panel-084)** | MINIMAL URBAN LINEWORK · GEOMETRIC SCAFFOLD · DENSITY-BASED STIPPLING · LEADING LINES · RESTRAINED COLOUR · POETIC WHITESPACE |
| **[xxd-panel-085](https://github.com/nevertoday/xxd-panel-085)** | HANDMADE MINIATURE STAGE · COLLECTIBLE DIMENSIONAL COVER · CLAY AND FELT · CUT PAPER AND STRING · MATTE TACTILITY · ARTFUL WHITESPACE |
| **[xxd-panel-092](https://github.com/nevertoday/xxd-panel-092)** | Expressive pen · loose contours · geometric and scribble hatching · negative-space composition |
| **[xxd-panel-093](https://github.com/nevertoday/xxd-panel-093)** | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| **[xxd-panel-094](https://github.com/nevertoday/xxd-panel-094)** | Fine pen-and-ink · selective solid black · source-derived spot colour · vast negative space · vintage book illustration |
| **[xxd-panel-095](https://github.com/nevertoday/xxd-panel-095)** | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| **[xxd-panel-096](https://github.com/nevertoday/xxd-panel-096)** | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| **[xxd-panel-097](https://github.com/nevertoday/xxd-panel-097)** | Mid-century vernacular commercial graphic · schematic line drawing · two-colour spot printing · functional humour |
| **[xxd-panel-100](https://github.com/nevertoday/xxd-panel-100)** | naïve folk narrative · primitive forms · flat space · crayon grain · warm paper · vivid limited colour · folk editorial type |
<!-- xxd-panel-catalog:end -->

## About XXD

XXD is Xiaoxiaodong's abbreviated brand name. Created and maintained by [@xiaoxiaodong01](https://x.com/xiaoxiaodong01).

## Support and membership

### Xiaoxiaodong Commander · General Command Skill · CNY 100

A one-time CNY 100 purchase unlocks this suite's General Command Skill (`xxd-panel-all`) for roster control, recommendations, Soldier dispatch, and batch coordination. Include “General Command Skill” in your WeChat message.

<!-- xxd-panel-command-system:start -->
**Your purchase unlocks the General Skill that commands the whole roster**

| Level | Skill | Responsibility |
|---|---|---|
| **General** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | Detect available numbered Skills; recommend by image, theme, or use; dispatch a chosen number; organize multi-style trials; and assign folders of images to individual jobs. |
| **Soldiers** | `xxd-panel-NNN` (currently 001–100) | Each numbered Skill executes only its own original brief and aesthetic, completing the individual job assigned by the General. |

The General Skill is the command center for the entire numbered-Skill roster. Your purchase unlocks it together with help for installation, updates, roster setup, and dispatch workflows. The General organizes and routes; it never rewrites, blends, or overrides a Soldier's original aesthetic. Every finished asset is still created independently by the selected Soldier Skill.
<!-- xxd-panel-command-system:end -->

### Knowledge Planet + Member Prompt Library + All General Skills Membership · CNY 699/year

[Knowledge Planet](https://wx.zsxq.com/group/15554814142882), the [XXD Member Prompt Library](https://vip.xiaoxiaodong.ai/), and membership for all General Skills are one membership: **one annual payment unlocks all three benefits, with no second purchase required.**

[Knowledge Planet](https://wx.zsxq.com/group/15554814142882) · [Member Prompt Library](https://vip.xiaoxiaodong.ai/)

<p align="center"><a href="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png"><img src="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png" alt="XXD WeChat" width="280"></a></p>

<div align="center"><strong>Let the mark pause, let the colour shift, and let the feeling remain.</strong></div>

---

<div align="center">

## Support this open-source project

If this project helps you, you’re welcome to support it through Buy Me a Coffee—entirely optional.


<p align="center"><a href="https://github.com/nevertoday/zhongguo-traditional-colors/blob/main/docs/images/buy-me-a-coffee-qr.png?raw=true"><img src="https://github.com/nevertoday/zhongguo-traditional-colors/blob/main/docs/images/buy-me-a-coffee-qr.png?raw=true" alt="Buy Me a Coffee" width="180"></a></p>

</div>
