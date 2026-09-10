# Sample artwork workflow

This package currently has no generated sample artwork. Commands in the READMEs are usage examples, not visual evidence. Packaging and documentation checks never call an image model.

When the user requests sample artwork:

1. Use a user-supplied source photograph and this Panel's complete canonical source. If no source exists, request one; never borrow another Panel's output or invent an unavailable reference image.
2. Resolve the requested count, mode, dimensions and text settings once. Generate one complete canvas per requested result. Do not generate a default multi-image batch, automatic variants, contact sheets or retries.
3. Follow SKILL.md. The comparison canvas has exactly two equal regions; source-required grids, boxes, sidebars or frames belong inside the designed region. For design-only and wallpapers the design fills the canvas.
4. Visually inspect the result for identity, medium, palette, typography, composition and the correct midpoint. Dimension checks alone cannot establish visual acceptance. Clean supported provenance metadata without altering pixels; do not claim this makes the work non-AI.
5. Only after visual acceptance, store the real output in assets/examples. Record its relative path, SHA-256, width, height, mode, canonical source SHA-256 and visual_review: passed in samples.json. Use status: ready only when every listed image passes. Keep failed results out of the gallery.
6. Run python3 scripts/check_samples.py. Then update the sample section in all five READMEs to link to the actual files, remove the no-samples statement, and describe the true mode. Keep the advertising templates unchanged. Run the repository README advertising validator before publication.

Do not add nonexistent sample links, confuse a source photo with a generated example, or present another numbered Panel's artwork as this Panel's work. Samples are documentation evidence and never replace the canonical prompt during runtime generation.
