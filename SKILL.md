---
name: xxd-panel-100
description: "XXD Panel 100｜Folk-Craft Narrative Painting: retells the subject and story of a photo as a naive, folk-inspired flat narrative illustration — simplified silhouettes and large primitive forms with gently exaggerated features, flattened perspective built from height, overlap and size, supporting objects scattered like symbols, dark areas in crayon, oil pastel or soft pencil grain that is rubbed, layered and broken so paper shows through, warm white paper, a limited palette of a few lively spot colours taken from the photo, generous whitespace and a few words in a plain folk-editorial typeface with some handwriting, placed like a sign, menu or note in the scene. Outputs PNG top-bottom or left-right comparisons, design-only images, or phone/tablet/desktop/watch wallpapers, from one photo or a folder. Use when the user invokes xxd-panel-100 or asks for folk art, naive silhouette, crayon or oil-pastel narrative illustration from a photo."
---

# XXD Panel 100

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.

Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-100/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-100-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
