#!/usr/bin/env python3
"""Private bitmap bridge for an already configured Codex provider.

The bridge intentionally prints only sanitized capability/result records. It
never prints provider names, endpoint URLs, request headers, credentials,
prompts, or response bodies.
"""

from __future__ import annotations

import argparse
import base64
import io
import json
import math
import mimetypes
import os
from pathlib import Path
import sys
import tomllib
import urllib.error
import urllib.parse
import urllib.request
import uuid


DEFAULT_MODEL = "gpt-image-2"
MAX_RESPONSE_BYTES = 100 * 1024 * 1024
GPT_IMAGE_2_MIN_PIXELS = 655_360
GPT_IMAGE_2_MAX_PIXELS = 8_294_400
GPT_IMAGE_2_MAX_EDGE = 3840
GPT_IMAGE_2_MAX_RATIO = 3.0


class BridgeError(Exception):
    def __init__(self, reason: str, phase: str, status: int | None = None):
        super().__init__(reason)
        self.reason = reason
        self.phase = phase
        self.status = status


class NoCredentialRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


def emit(payload: dict, *, error: bool = False) -> None:
    stream = sys.stderr if error else sys.stdout
    print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), file=stream)


def codex_dir() -> Path:
    override = os.environ.get("XXD_IMAGEGEN_CODEX_DIR")
    if override:
        return Path(override).expanduser()
    configured = os.environ.get("CODEX_HOME")
    if configured:
        return Path(configured).expanduser()
    return Path.home() / ".codex"


def load_json_object(path: Path, phase: str) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BridgeError("credential_store_unavailable", phase) from exc
    except Exception as exc:
        raise BridgeError("credential_store_unreadable", phase) from exc
    if not isinstance(data, dict):
        raise BridgeError("credential_store_unreadable", phase)
    return data


def load_route() -> tuple[str, dict[str, str]]:
    root = codex_dir()
    config_path = root / "config.toml"
    try:
        config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BridgeError("route_not_configured", "route") from exc
    except Exception as exc:
        raise BridgeError("route_config_unreadable", "route") from exc

    active = config.get("model_provider")
    providers = config.get("model_providers")
    if not isinstance(active, str) or not isinstance(providers, dict):
        raise BridgeError("route_not_configured", "route")
    provider = providers.get(active)
    if not isinstance(provider, dict):
        raise BridgeError("route_not_configured", "route")

    base_url = provider.get("base_url")
    if not isinstance(base_url, str) or not base_url.strip():
        raise BridgeError("route_not_configured", "route")
    parsed = urllib.parse.urlsplit(base_url.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise BridgeError("route_config_invalid", "route")

    headers: dict[str, str] = {"Accept": "application/json"}
    fixed_headers = provider.get("http_headers")
    if isinstance(fixed_headers, dict):
        for name, value in fixed_headers.items():
            if isinstance(name, str) and isinstance(value, str):
                headers[name] = value

    env_headers = provider.get("env_http_headers")
    if isinstance(env_headers, dict):
        for name, env_name in env_headers.items():
            if not isinstance(name, str) or not isinstance(env_name, str):
                continue
            value = os.environ.get(env_name)
            if value:
                headers[name] = value

    has_authorization = any(name.lower() == "authorization" for name in headers)
    if not has_authorization:
        token: str | None = None
        env_key = provider.get("env_key")
        if isinstance(env_key, str) and env_key:
            token = os.environ.get(env_key)
        direct_token = provider.get("experimental_bearer_token")
        if not token and isinstance(direct_token, str) and direct_token:
            token = direct_token
        if not token and provider.get("requires_openai_auth") is True:
            auth = load_json_object(root / "auth.json", "auth")
            stored = auth.get("OPENAI_API_KEY")
            if isinstance(stored, str) and stored:
                token = stored
        if not token:
            fallback = os.environ.get("OPENAI_API_KEY")
            if fallback:
                token = fallback
        if token:
            headers["Authorization"] = f"Bearer {token}"

    headers.setdefault("User-Agent", "xxd-configured-imagegen/1")
    return base_url.strip(), headers


def endpoint(base_url: str, suffix: str) -> str:
    parsed = urllib.parse.urlsplit(base_url)
    path = parsed.path.rstrip("/")
    for terminal in ("/responses", "/chat/completions", "/images/generations", "/images/edits"):
        if path.endswith(terminal):
            path = path[: -len(terminal)]
            break
    path = path.rstrip("/") + suffix
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, parsed.query, ""))


def read_limited(response) -> bytes:  # noqa: ANN001
    length = response.headers.get("Content-Length")
    if length:
        try:
            if int(length) > MAX_RESPONSE_BYTES:
                raise BridgeError("response_too_large", "response")
        except ValueError:
            pass
    raw = response.read(MAX_RESPONSE_BYTES + 1)
    if len(raw) > MAX_RESPONSE_BYTES:
        raise BridgeError("response_too_large", "response")
    return raw


def request_bytes(
    url: str,
    headers: dict[str, str],
    *,
    body: bytes,
    content_type: str,
    timeout: int,
    phase: str,
) -> tuple[int, bytes]:
    request_headers = dict(headers)
    request_headers["Content-Type"] = content_type
    request = urllib.request.Request(url, data=body, method="POST", headers=request_headers)
    opener = urllib.request.build_opener(NoCredentialRedirects())
    try:
        with opener.open(request, timeout=timeout) as response:
            return response.status, read_limited(response)
    except urllib.error.HTTPError as exc:
        try:
            raw = exc.read(MAX_RESPONSE_BYTES + 1)
        except Exception:
            raw = b""
        return exc.code, raw
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise BridgeError("route_unreachable", phase) from exc


def json_request(
    base_url: str,
    headers: dict[str, str],
    suffix: str,
    payload: dict,
    timeout: int,
    phase: str,
) -> tuple[int, bytes]:
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return request_bytes(
        endpoint(base_url, suffix),
        headers,
        body=body,
        content_type="application/json",
        timeout=timeout,
        phase=phase,
    )


def parse_size(value: str) -> tuple[int, int] | None:
    if value == "auto":
        return None
    parts = value.lower().split("x", 1)
    if len(parts) != 2:
        raise BridgeError("invalid_size", "input")
    try:
        width, height = int(parts[0]), int(parts[1])
    except ValueError as exc:
        raise BridgeError("invalid_size", "input") from exc
    if width < 1 or height < 1:
        raise BridgeError("invalid_size", "input")
    return width, height


def normalize_gpt_image_2_size(target: tuple[int, int] | None) -> str:
    if target is None:
        return "auto"
    width, height = target
    ratio = max(width, height) / min(width, height)
    if ratio > GPT_IMAGE_2_MAX_RATIO:
        raise BridgeError("unsupported_aspect_ratio", "input")

    pixels = width * height
    lower_scale = math.sqrt(GPT_IMAGE_2_MIN_PIXELS / pixels)
    upper_scale = min(
        math.sqrt(GPT_IMAGE_2_MAX_PIXELS / pixels),
        GPT_IMAGE_2_MAX_EDGE / max(width, height),
    )
    if lower_scale > upper_scale:
        raise BridgeError("unsupported_size", "input")
    scale = min(max(1.0, lower_scale), upper_scale)

    for _ in range(200):
        out_w = max(16, int(round(width * scale / 16.0)) * 16)
        out_h = max(16, int(round(height * scale / 16.0)) * 16)
        out_pixels = out_w * out_h
        if (
            max(out_w, out_h) <= GPT_IMAGE_2_MAX_EDGE
            and GPT_IMAGE_2_MIN_PIXELS <= out_pixels <= GPT_IMAGE_2_MAX_PIXELS
            and max(out_w, out_h) / min(out_w, out_h) <= GPT_IMAGE_2_MAX_RATIO
        ):
            return f"{out_w}x{out_h}"
        if out_pixels < GPT_IMAGE_2_MIN_PIXELS:
            scale *= 1.005
        else:
            scale *= 0.995
    raise BridgeError("unsupported_size", "input")


def prompt_text(path: Path) -> str:
    try:
        value = path.read_text(encoding="utf-8").strip()
    except Exception as exc:
        raise BridgeError("prompt_unreadable", "input") from exc
    if not value:
        raise BridgeError("prompt_empty", "input")
    return value


def multipart_body(fields: dict[str, str], images: list[Path]) -> tuple[bytes, str]:
    boundary = "----xxd-" + uuid.uuid4().hex
    buffer = io.BytesIO()

    def write(value: bytes) -> None:
        buffer.write(value)

    for name, value in fields.items():
        write(f"--{boundary}\r\n".encode())
        write(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
        write(value.encode("utf-8"))
        write(b"\r\n")

    for image in images:
        try:
            data = image.read_bytes()
        except Exception as exc:
            raise BridgeError("source_unreadable", "input") from exc
        if not data:
            raise BridgeError("source_unreadable", "input")
        filename = image.name.replace('"', "")
        mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        write(f"--{boundary}\r\n".encode())
        write(
            f'Content-Disposition: form-data; name="image"; filename="{filename}"\r\n'.encode(
                "utf-8"
            )
        )
        write(f"Content-Type: {mime}\r\n\r\n".encode())
        write(data)
        write(b"\r\n")
    write(f"--{boundary}--\r\n".encode())
    return buffer.getvalue(), f"multipart/form-data; boundary={boundary}"


def response_image(raw: bytes, timeout: int) -> bytes:
    try:
        payload = json.loads(raw)
    except Exception as exc:
        raise BridgeError("invalid_image_response", "response") from exc
    if not isinstance(payload, dict):
        raise BridgeError("invalid_image_response", "response")
    data = payload.get("data")
    if not isinstance(data, list) or not data or not isinstance(data[0], dict):
        raise BridgeError("image_missing", "response")
    item = data[0]
    encoded = item.get("b64_json")
    if isinstance(encoded, str) and encoded:
        try:
            return base64.b64decode(encoded, validate=True)
        except Exception as exc:
            raise BridgeError("image_decode_failed", "response") from exc
    image_url = item.get("url")
    if not isinstance(image_url, str) or not image_url:
        raise BridgeError("image_missing", "response")
    if image_url.startswith("data:"):
        try:
            return base64.b64decode(image_url.split(",", 1)[1], validate=True)
        except Exception as exc:
            raise BridgeError("image_decode_failed", "response") from exc
    parsed = urllib.parse.urlsplit(image_url)
    if parsed.scheme not in {"http", "https"}:
        raise BridgeError("image_download_refused", "response")
    try:
        with urllib.request.urlopen(image_url, timeout=timeout) as response:
            return read_limited(response)
    except Exception as exc:
        raise BridgeError("image_download_failed", "response") from exc


def write_png(raw: bytes, out: Path, target: tuple[int, int] | None, force: bool) -> None:
    if out.suffix.lower() != ".png":
        raise BridgeError("output_must_be_png", "output")
    if out.exists() and not force:
        raise BridgeError("output_exists", "output")
    try:
        from PIL import Image, ImageOps
    except Exception as exc:
        raise BridgeError("pillow_unavailable", "output") from exc
    try:
        with Image.open(io.BytesIO(raw)) as image:
            image.load()
            if target is not None and image.size != target:
                image = ImageOps.fit(image, target, method=Image.Resampling.LANCZOS)
            if image.mode not in {"RGB", "RGBA"}:
                image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
            out.parent.mkdir(parents=True, exist_ok=True)
            image.save(out, format="PNG")
    except BridgeError:
        raise
    except Exception as exc:
        raise BridgeError("invalid_bitmap", "output") from exc


def probe(timeout: int) -> int:
    base_url, headers = load_route()
    status, _ = json_request(base_url, headers, "/images/generations", {}, timeout, "probe")
    ready = status in {200, 400, 409, 422}
    emit({"ok": ready, "bitmap_route": ready, "http_status": status})
    return 0 if ready else 2


def run_image(args: argparse.Namespace) -> int:
    base_url, headers = load_route()
    target = parse_size(args.size)
    request_size = normalize_gpt_image_2_size(target) if args.model == DEFAULT_MODEL else args.size
    prompt = prompt_text(args.prompt_file)
    common = {
        "model": args.model,
        "prompt": prompt,
        "n": "1",
        "size": request_size,
        "quality": args.quality,
        "output_format": "png",
        "stream": "false",
    }

    if args.command == "generate":
        payload: dict[str, object] = dict(common)
        payload["n"] = 1
        payload["stream"] = False
        status, raw = json_request(
            base_url, headers, "/images/generations", payload, args.timeout, "generate"
        )
    else:
        images = [Path(value).expanduser() for value in args.image]
        if not images:
            raise BridgeError("source_required", "input")
        body, content_type = multipart_body(common, images)
        status, raw = request_bytes(
            endpoint(base_url, "/images/edits"),
            headers,
            body=body,
            content_type=content_type,
            timeout=args.timeout,
            phase="edit",
        )

    if not 200 <= status < 300:
        raise BridgeError("image_request_rejected", args.command, status)
    image = response_image(raw, args.timeout)
    out = Path(args.out).expanduser()
    write_png(image, out, target, args.force)
    emit({"ok": True, "bitmap_written": True, "path": str(out.resolve())})
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Use the active configured bitmap route privately.")
    sub = root.add_subparsers(dest="command", required=True)

    check = sub.add_parser("probe", help="Return only a sanitized readiness result.")
    check.add_argument("--timeout", type=int, default=20)

    for name in ("generate", "edit"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--prompt-file", type=Path, required=True)
        cmd.add_argument("--out", required=True)
        cmd.add_argument("--size", default="auto")
        cmd.add_argument("--quality", choices=("low", "medium", "high", "auto"), default="high")
        cmd.add_argument("--model", default=DEFAULT_MODEL)
        cmd.add_argument("--timeout", type=int, default=600)
        cmd.add_argument("--force", action="store_true")
        if name == "edit":
            cmd.add_argument("--image", action="append", required=True)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command == "probe":
            return probe(args.timeout)
        return run_image(args)
    except BridgeError as exc:
        payload: dict[str, object] = {"ok": False, "phase": exc.phase, "reason": exc.reason}
        if exc.status is not None:
            payload["http_status"] = exc.status
        emit(payload, error=True)
        return 2
    except Exception:
        emit({"ok": False, "phase": "internal", "reason": "sanitized_internal_error"}, error=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
