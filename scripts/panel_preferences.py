#!/usr/bin/env python3
"""Store and retrieve the safe, family-wide XXD Panel delivery preference."""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1
MODES = {"top-bottom", "left-right", "design-only", "wallpaper-pack"}
TEXT_MODES = {"prompt", "exact", "none"}
WALLPAPER_RELATIONSHIPS = {"linked", "independent"}
DEVICES = {"phone", "ipad", "desktop", "watch"}
ORDINARY_MODES = {"top-bottom", "left-right", "design-only"}
SIZE_RE = re.compile(r"^(?:auto|source|[1-9][0-9]*:[1-9][0-9]*|[1-9][0-9]*x[1-9][0-9]*)$")


class PreferenceError(ValueError):
    pass


def _config_dir() -> Path:
    override = os.environ.get("XXD_PANEL_PREFS_DIR")
    if override:
        return Path(override).expanduser()
    if os.name == "nt" and os.environ.get("APPDATA"):
        return Path(os.environ["APPDATA"]) / "xxd-panel" / "preferences"
    xdg = os.environ.get("XDG_CONFIG_HOME")
    base = Path(xdg).expanduser() if xdg else Path.home() / ".config"
    return base / "xxd-panel" / "preferences"


def _preference_path() -> Path:
    return _config_dir() / "last-delivery.json"


def _split_values(values: list[str] | None) -> list[str]:
    result: list[str] = []
    for value in values or []:
        for item in value.replace("，", ",").split(","):
            item = item.strip()
            if item and item not in result:
                result.append(item)
    return result


def _clean_text(value: str | None, field: str, limit: int = 1024) -> str | None:
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    if len(value) > limit or any(ord(char) < 32 for char in value):
        raise PreferenceError(f"invalid {field}")
    return value


def _normalise_size(value: str) -> str:
    return value.strip().lower().replace("×", "x")


def _parse_wallpaper_sizes(values: list[str] | None) -> dict[str, str]:
    result: dict[str, str] = {}
    for value in _split_values(values):
        if "=" not in value:
            raise PreferenceError("wallpaper sizes must use device=WIDTHxHEIGHT")
        device, size = value.split("=", 1)
        device = device.strip().lower()
        size = _normalise_size(size)
        if device not in DEVICES or not re.fullmatch(r"[1-9][0-9]*x[1-9][0-9]*", size):
            raise PreferenceError("invalid wallpaper device or size")
        result[device] = size
    return result


def _validate_profile(profile: dict[str, Any]) -> dict[str, Any]:
    allowed = {
        "modes",
        "sizes",
        "text_mode",
        "locale",
        "wallpaper_relationship",
        "wallpaper_sizes",
        "output_root",
    }
    if set(profile) - allowed:
        raise PreferenceError("unsupported preference field")

    modes = profile.get("modes")
    if not isinstance(modes, list) or not modes or len(modes) > len(MODES):
        raise PreferenceError("modes are required")
    clean_modes: list[str] = []
    for mode in modes:
        if mode not in MODES:
            raise PreferenceError("invalid mode")
        if mode not in clean_modes:
            clean_modes.append(mode)

    sizes = profile.get("sizes", [])
    if not isinstance(sizes, list) or len(sizes) > 32:
        raise PreferenceError("invalid sizes")
    clean_sizes: list[str] = []
    for size in sizes:
        if not isinstance(size, str):
            raise PreferenceError("invalid size")
        clean_size = _normalise_size(size)
        if not SIZE_RE.fullmatch(clean_size):
            raise PreferenceError("invalid size")
        if clean_size not in clean_sizes:
            clean_sizes.append(clean_size)
    if ORDINARY_MODES.intersection(clean_modes) and not clean_sizes:
        raise PreferenceError("ordinary modes require a size policy")

    text_mode = profile.get("text_mode")
    if text_mode not in TEXT_MODES:
        raise PreferenceError("text mode is required")
    locale = _clean_text(profile.get("locale"), "locale", 64)
    if text_mode in {"prompt", "exact"} and not locale:
        raise PreferenceError("text modes require a locale")
    if text_mode == "none":
        locale = None

    wallpaper_relationship = profile.get("wallpaper_relationship")
    wallpaper_sizes = profile.get("wallpaper_sizes", {})
    if "wallpaper-pack" in clean_modes:
        if wallpaper_relationship not in WALLPAPER_RELATIONSHIPS:
            raise PreferenceError("wallpaper mode requires a relationship")
        if not isinstance(wallpaper_sizes, dict) or set(wallpaper_sizes) - DEVICES:
            raise PreferenceError("invalid wallpaper sizes")
        clean_wallpaper_sizes: dict[str, str] = {}
        for device, size in wallpaper_sizes.items():
            if not isinstance(size, str):
                raise PreferenceError("invalid wallpaper size")
            clean_size = _normalise_size(size)
            if not re.fullmatch(r"[1-9][0-9]*x[1-9][0-9]*", clean_size):
                raise PreferenceError("invalid wallpaper size")
            clean_wallpaper_sizes[device] = clean_size
    else:
        wallpaper_relationship = None
        clean_wallpaper_sizes = {}

    output_root = _clean_text(profile.get("output_root"), "output root")

    result: dict[str, Any] = {
        "modes": clean_modes,
        "sizes": clean_sizes,
        "text_mode": text_mode,
    }
    if locale:
        result["locale"] = locale
    if wallpaper_relationship:
        result["wallpaper_relationship"] = wallpaper_relationship
    if clean_wallpaper_sizes:
        result["wallpaper_sizes"] = clean_wallpaper_sizes
    if output_root:
        result["output_root"] = output_root
    return result


def _load() -> dict[str, Any]:
    path = _preference_path()
    if not path.is_file():
        return {"status": "missing"}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("schema_version") != SCHEMA_VERSION:
            raise PreferenceError("unsupported preference schema")
        preferences = data.get("preferences")
        if not isinstance(preferences, dict):
            raise PreferenceError("invalid preference payload")
        clean = _validate_profile(preferences)
        return {
            "status": "found",
            "updated_at": data.get("updated_at"),
            "preferences": clean,
        }
    except (OSError, json.JSONDecodeError, PreferenceError):
        return {"status": "invalid"}


def _save(args: argparse.Namespace) -> dict[str, Any]:
    modes = _split_values(args.modes)
    sizes = [_normalise_size(item) for item in _split_values(args.sizes)]
    profile: dict[str, Any] = {
        "modes": modes,
        "sizes": sizes,
        "text_mode": args.text_mode,
        "locale": args.locale,
        "wallpaper_relationship": args.wallpaper,
        "wallpaper_sizes": _parse_wallpaper_sizes(args.wallpaper_sizes),
        "output_root": args.output_root,
    }
    clean = _validate_profile(profile)
    payload = {
        "schema_version": SCHEMA_VERSION,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "preferences": clean,
    }
    directory = _config_dir()
    directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    try:
        os.chmod(directory, stat.S_IRWXU)
    except OSError:
        pass
    fd, temporary_name = tempfile.mkstemp(prefix=".last-delivery-", suffix=".json", dir=directory)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.chmod(temporary_name, stat.S_IRUSR | stat.S_IWUSR)
        os.replace(temporary_name, _preference_path())
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)
    return {"status": "saved", "preferences": clean}


def _clear() -> dict[str, str]:
    path = _preference_path()
    try:
        path.unlink()
        return {"status": "cleared"}
    except FileNotFoundError:
        return {"status": "missing"}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("load", help="load the last safe delivery preference")
    subparsers.add_parser("clear", help="remove the remembered delivery preference")

    save = subparsers.add_parser("save", help="replace the remembered delivery preference")
    save.add_argument("--modes", action="append", required=True)
    save.add_argument("--sizes", action="append", default=[])
    save.add_argument("--text-mode", choices=sorted(TEXT_MODES), required=True)
    save.add_argument("--locale")
    save.add_argument("--wallpaper", choices=sorted(WALLPAPER_RELATIONSHIPS))
    save.add_argument("--wallpaper-sizes", action="append", default=[])
    save.add_argument("--output-root")
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        if args.command == "load":
            result = _load()
        elif args.command == "save":
            result = _save(args)
        else:
            result = _clear()
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
        return 0
    except (OSError, PreferenceError) as error:
        print(json.dumps({"status": "error", "message": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
