#!/usr/bin/env python3
"""Compose or finalize XXD panel artwork at deterministic dimensions.

Supported layouts:

    top-bottom   source photo above, designed image below, exact 50/50
    left-right   source photo left, designed image right, exact 50/50
    design-only  designed image fills the entire output; source is not shown

Examples:

    compose_panel.py --plan --layout top-bottom --source photo.jpg
    compose_panel.py --plan --layout left-right --size 2560x1440
    compose_panel.py --source photo.jpg --design panel.png --out poster.png \
        --layout left-right --size 2560x1440 --anchor center
    compose_panel.py --design panel.png --out artwork.png \
        --layout design-only --size 2048x2048
    compose_panel.py --audit poster.png --layout left-right

The legacy --top and --bottom names remain aliases for --source and --design.
Needs Pillow. If the default interpreter lacks it, run explicitly, e.g.
    /opt/homebrew/bin/python3 compose_panel.py ...
"""

from __future__ import annotations

import argparse
import sys
from math import gcd
from pathlib import Path

try:
    from PIL import Image
except ModuleNotFoundError:
    sys.exit(
        "Pillow is required.\n"
        "  Try:  /opt/homebrew/bin/python3 compose_panel.py ...\n"
        "  Or:   python3 -m pip install Pillow"
    )


def parse_ratio(text: str) -> tuple[float, float]:
    sep = ":" if ":" in text else "x" if "x" in text.lower() else None
    if sep is None:
        raise argparse.ArgumentTypeError(f"ratio must look like 3:4, got {text!r}")
    normalized = text.lower()
    w, _, h = normalized.partition(sep)
    try:
        wv, hv = float(w), float(h)
    except ValueError:
        raise argparse.ArgumentTypeError(f"ratio must be numeric, got {text!r}") from None
    if wv <= 0 or hv <= 0:
        raise argparse.ArgumentTypeError(f"ratio must be positive, got {text!r}")
    return wv, hv


def parse_size(text: str) -> tuple[int, int]:
    normalized = text.lower().replace("×", "x")
    if "x" not in normalized:
        raise argparse.ArgumentTypeError(f"size must look like 2048x2048, got {text!r}")
    w, _, h = normalized.partition("x")
    try:
        width, height = int(w), int(h)
    except ValueError:
        raise argparse.ArgumentTypeError(f"size must use whole pixels, got {text!r}") from None
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError(f"size must be positive, got {text!r}")
    return width, height


def canvas_size(
    layout: str,
    ratio: tuple[float, float] | None,
    width: int | None,
    exact_size: tuple[int, int] | None,
    source_size: tuple[int, int] | None,
) -> tuple[int, int]:
    """Resolve an explicit canvas or adapt it losslessly to the source."""
    if exact_size is not None:
        cw, ch = exact_size
    elif ratio is not None:
        if width is None:
            raise ValueError("a width or readable --source is required with --canvas")
        wr, hr = ratio
        cw = width
        ch = round(width * hr / wr)
    elif source_size is not None:
        sw, sh = source_size
        if layout == "top-bottom":
            cw, ch = sw, sh * 2
        elif layout == "left-right":
            cw, ch = sw * 2, sh
        else:
            cw, ch = sw, sh
    else:
        raise ValueError(
            "no default ratio is imposed; provide --source for source-adaptive sizing, "
            "or specify --size/--canvas"
        )

    if layout == "top-bottom" and ch % 2:
        if exact_size is not None:
            raise ValueError(
                f"top-bottom requires an even output height for exact 50/50, got {cw}x{ch}"
            )
        ch += 1
    elif layout == "left-right" and cw % 2:
        if exact_size is not None:
            raise ValueError(
                f"left-right requires an even output width for exact 50/50, got {cw}x{ch}"
            )
        cw += 1
        if ratio is not None:
            ch = round(cw * ratio[1] / ratio[0])

    return cw, ch


def panel_size(layout: str, canvas: tuple[int, int]) -> tuple[int, int]:
    cw, ch = canvas
    if layout == "top-bottom":
        return cw, ch // 2
    if layout == "left-right":
        return cw // 2, ch
    return cw, ch


def cover(img: Image.Image, size: tuple[int, int], anchor: str) -> Image.Image:
    """Scale to fill ``size`` and crop overflow without distortion."""
    tw, th = size
    sw, sh = img.size
    scale = max(tw / sw, th / sh)
    nw, nh = max(tw, round(sw * scale)), max(th, round(sh * scale))
    img = img.resize((nw, nh), Image.LANCZOS)

    if anchor == "left":
        left = 0
    elif anchor == "right":
        left = nw - tw
    else:
        left = (nw - tw) // 2

    if anchor == "top":
        top = 0
    elif anchor == "bottom":
        top = nh - th
    else:
        top = (nh - th) // 2

    return img.crop((left, top, left + tw, top + th))


def load(path: Path) -> Image.Image:
    try:
        img = Image.open(path)
    except FileNotFoundError:
        sys.exit(f"not found: {path}")
    except OSError as exc:
        sys.exit(f"cannot read {path}: {exc}")
    return img.convert("RGB")


def overflow_report(img: Image.Image, size: tuple[int, int], label: str) -> str:
    """Report how much source content a cover crop would discard."""
    tw, th = size
    src = img.width / img.height
    dst = tw / th
    if abs(src - dst) < 0.01:
        return f"  {label}: aspect {src:.3f} fits {dst:.3f} — no crop"
    if src > dst:
        kept = dst / src
        message = (
            f"  {label}: aspect {src:.3f} vs {dst:.3f} — source is wider, "
            f"keeping {kept:.0%} of its width"
        )
    else:
        kept = src / dst
        message = (
            f"  {label}: aspect {src:.3f} vs {dst:.3f} — source is taller, "
            f"keeping {kept:.0%} of its height"
        )
    if kept < 0.75:
        message += "  << extend the background instead of cropping this hard"
    return message


def plan(layout: str, canvas: tuple[int, int], ratio_label: str) -> None:
    cw, ch = canvas
    pw, ph = panel_size(layout, canvas)
    common = gcd(pw, ph)
    print(f"layout   {layout}")
    print(f"canvas   {cw}x{ch}  ({ratio_label})")

    if layout == "top-bottom":
        print(f"seam at  y = {ph}")
        print(
            f"generate source and design at {pw}x{ph}  "
            f"(aspect {pw / ph:.3f} = {pw // common}:{ph // common})"
        )
        print("source   upper half")
        print("design   lower half")
    elif layout == "left-right":
        print(f"seam at  x = {pw}")
        print(
            f"generate source and design at {pw}x{ph}  "
            f"(aspect {pw / ph:.3f} = {pw // common}:{ph // common})"
        )
        print("source   left half")
        print("design   right half")
    else:
        print("seam     none")
        print(
            f"generate the designed image at {pw}x{ph}  "
            f"(aspect {pw / ph:.3f} = {pw // common}:{ph // common})"
        )
        print("source   used as reference only; not visible in the output")


def axis_scores(img: Image.Image, layout: str) -> tuple[list[float], int]:
    gray = img.convert("L")
    w, h = gray.size
    if layout == "top-bottom":
        small = gray.resize((min(w, 256), h), Image.LANCZOS)
        px = small.load()
        scores = [
            sum(abs(px[x, y] - px[x, y - 1]) for x in range(small.width)) / small.width
            for y in range(1, h)
        ]
        return scores, h

    small = gray.resize((w, min(h, 256)), Image.LANCZOS)
    px = small.load()
    scores = [
        sum(abs(px[x, y] - px[x - 1, y]) for y in range(small.height)) / small.height
        for x in range(1, w)
    ]
    return scores, w


def audit(path: Path, layout: str, expected_size: tuple[int, int] | None) -> None:
    img = load(path)
    w, h = img.size
    print(f"image      {w}x{h}   aspect {w / h:.3f}")

    if expected_size is not None:
        if (w, h) == expected_size:
            print(f"size       OK — matches requested {w}x{h}")
        else:
            print(
                f"size       OFF — requested {expected_size[0]}x{expected_size[1]}, "
                f"got {w}x{h}"
            )

    if layout == "design-only":
        print("seam       N/A — design-only has no photographic panel or split.")
        print("verdict    OK" if expected_size in (None, (w, h)) else "verdict    OFF")
        return

    scores, axis_length = axis_scores(img, layout)
    best_index = max(range(len(scores)), key=scores.__getitem__)
    seam = best_index + 1
    strength = scores[best_index]
    mean = sum(scores) / len(scores)
    half = axis_length / 2
    offset = seam - half
    offset_pct = abs(offset) / axis_length * 100
    axis = "y" if layout == "top-bottom" else "x"

    print(f"exact half {axis} = {half:.1f}")
    print(
        f"seam found {axis} = {seam}   "
        f"(axis delta {strength:.1f}, page mean {mean:.1f})"
    )

    if strength < 6.0 or strength < mean * 3:
        print("verdict    NO CLEAR SEAM — no hard central division stands out.")
        print("           Compose from two panels instead of trusting one model call.")
        return

    print(f"offset     {offset:+.0f} px  =  {offset_pct:.2f}% of split axis")
    if offset_pct < 0.25:
        print("verdict    OK — the split is effectively exact.")
    else:
        first = seam / axis_length * 100
        print(f"verdict    OFF — panels are {first:.1f}% / {100 - first:.1f}%, not 50/50.")
        print("           Regenerate the panels separately and compose them here.")


def collision_safe_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suffix = path.stem, path.suffix or ".png"
    candidate = path
    number = 2
    while candidate.exists():
        candidate = path.with_name(f"{stem}-{number}{suffix}")
        number += 1
    print(f"note: {path.name} existed, writing {candidate.name}")
    return candidate


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Compose top-bottom, left-right, or design-only panel artwork.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--layout",
        choices=("top-bottom", "left-right", "design-only"),
        default="top-bottom",
        help="output mode (default top-bottom)",
    )
    p.add_argument("--source", "--top", dest="source", type=Path, help="source photograph")
    p.add_argument("--design", "--bottom", dest="design", type=Path, help="designed image")
    p.add_argument("--out", type=Path, help="output image")
    p.add_argument(
        "--canvas",
        help="explicit canvas ratio; when omitted, infer a lossless layout from --source",
    )
    p.add_argument("--size", type=parse_size, help="exact output pixels, e.g. 2560x1440")
    p.add_argument(
        "--width",
        type=int,
        help="width used with --canvas; defaults to source width when available",
    )
    p.add_argument(
        "--anchor",
        choices=("top", "center", "bottom", "left", "right"),
        default="center",
        help="which source-photo edge a residual crop keeps (default center)",
    )
    p.add_argument("--plan", action="store_true", help="print target dimensions, then exit")
    p.add_argument("--audit", type=Path, help="audit seam and optional requested size")
    args = p.parse_args(argv)

    if args.width is not None and args.width < 2:
        sys.exit("--width must be at least 2")

    if args.audit and args.size is None and args.canvas is None and args.source is None:
        audit(args.audit, args.layout, None)
        return 0

    source_for_sizing = load(args.source) if args.source is not None else None
    source_size = source_for_sizing.size if source_for_sizing is not None else None
    ratio_text = args.canvas
    ratio = parse_ratio(ratio_text) if ratio_text else None
    working_width = args.width
    if ratio is not None and working_width is None:
        working_width = source_size[0] if source_size is not None else None
    try:
        canvas = canvas_size(args.layout, ratio, working_width, args.size, source_size)
    except ValueError as exc:
        sys.exit(str(exc))
    if args.size:
        ratio_label = f"exact {canvas[0]}x{canvas[1]}"
    elif ratio_text:
        ratio_label = ratio_text
    else:
        ratio_label = f"source-adaptive from {source_size[0]}x{source_size[1]}"

    if args.audit:
        audit(args.audit, args.layout, canvas if args.size else None)
        return 0

    if args.plan:
        plan(args.layout, canvas, ratio_label)
        return 0

    required = ["design", "out"] if args.layout == "design-only" else ["source", "design", "out"]
    missing = [f"--{name}" for name in required if getattr(args, name) is None]
    if missing:
        sys.exit(f"missing required argument(s): {', '.join(missing)}  (or use --plan / --audit)")

    cw, ch = canvas
    pw, ph = panel_size(args.layout, canvas)
    design_src = load(args.design)
    adaptive = args.size is None and args.canvas is None

    if adaptive and design_src.size != (pw, ph):
        source_aspect = pw / ph
        design_aspect = design_src.width / design_src.height
        if abs(source_aspect - design_aspect) / source_aspect > 0.005:
            sys.exit(
                f"source-adaptive mode requires design aspect {pw}:{ph}, got "
                f"{design_src.width}:{design_src.height}; regenerate without stock-ratio cropping"
            )
        print(
            f"adaptive design resize {design_src.width}x{design_src.height} -> {pw}x{ph} "
            "(same aspect, no crop)"
        )

    adaptive_design = (
        design_src.copy()
        if design_src.size == (pw, ph)
        else design_src.resize((pw, ph), Image.LANCZOS)
    )

    if args.layout == "design-only":
        print(f"layout design-only, canvas {cw}x{ch}, no seam")
        print(overflow_report(design_src, (cw, ch), "design"))
        result = adaptive_design if adaptive else cover(design_src, (cw, ch), "center")
    else:
        source_src = source_for_sizing or load(args.source)
        axis = "y" if args.layout == "top-bottom" else "x"
        seam = ph if args.layout == "top-bottom" else pw
        print(
            f"layout {args.layout}, canvas {cw}x{ch}, each panel {pw}x{ph}, "
            f"seam at {axis}={seam}"
        )
        print(overflow_report(source_src, (pw, ph), "source"))
        print(overflow_report(design_src, (pw, ph), "design"))
        result = Image.new("RGB", (cw, ch))
        source_panel = source_src.copy() if adaptive else cover(source_src, (pw, ph), args.anchor)
        design_panel = adaptive_design if adaptive else cover(design_src, (pw, ph), "center")
        if args.layout == "top-bottom":
            result.paste(source_panel, (0, 0))
            result.paste(design_panel, (0, ph))
        else:
            result.paste(source_panel, (0, 0))
            result.paste(design_panel, (pw, 0))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    out = collision_safe_path(args.out)
    result.save(out)

    assert result.size == canvas, "output dimensions do not match the resolved canvas"
    if args.layout == "top-bottom":
        assert result.height == ph * 2, "top-bottom split is not exact"
        split_note = f", split exactly {ph}/{ph}"
    elif args.layout == "left-right":
        assert result.width == pw * 2, "left-right split is not exact"
        split_note = f", split exactly {pw}/{pw}"
    else:
        split_note = ", design-only"
    print(f"wrote {out.resolve()}  ({cw}x{ch}{split_note})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
