#!/usr/bin/env python3
"""
Batch-translate a Markdown tree into Korean using Codex CLI.

This script does not require OPENAI_API_KEY.
It uses the logged-in Codex CLI session.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate Markdown files to Korean with codex exec."
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        required=True,
        help="Root directory containing source Markdown files.",
    )
    parser.add_argument(
        "--dest-root",
        type=Path,
        required=True,
        help="Root directory where translated Markdown files are saved.",
    )
    parser.add_argument(
        "--style",
        choices=["natural", "literal"],
        default="natural",
        help="Translation style.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5-codex",
        help="Model passed to codex exec.",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=["low", "medium", "high", "xhigh"],
        default="high",
        help="Reasoning effort passed to codex CLI config.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Translate only first N files (sorted).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing destination files.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Retry count per file when codex exec fails.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=240,
        help="Per-file timeout for each codex exec invocation.",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=0.1,
        help="Sleep seconds between files.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="Optional manifest path. Defaults to <dest-root>/manifest-ko.json.",
    )
    parser.add_argument(
        "--workdir",
        type=Path,
        default=Path.cwd(),
        help="Working directory for codex exec.",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=12000,
        help="Maximum characters per translation chunk.",
    )
    return parser.parse_args()


def find_markdown_files(source_root: Path) -> list[Path]:
    return sorted(path for path in source_root.rglob("*.md") if path.is_file())


def maybe_unwrap_markdown_fence(text: str) -> str:
    stripped = text.strip()
    if not stripped.startswith("```"):
        return text
    lines = stripped.splitlines()
    if len(lines) < 3:
        return text
    if not lines[-1].strip() == "```":
        return text
    first = lines[0].strip().lower()
    if first in {"```", "```md", "```markdown"}:
        body = "\n".join(lines[1:-1]).rstrip() + "\n"
        return body
    return text


def split_markdown_chunks(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    buf: list[str] = []
    size = 0
    in_code = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code

        line_size = len(line) + 1
        if buf and (size + line_size > max_chars) and not in_code:
            chunks.append("\n".join(buf).strip())
            buf = [line]
            size = line_size
            continue

        buf.append(line)
        size += line_size

    if buf:
        chunks.append("\n".join(buf).strip())

    return [chunk for chunk in chunks if chunk]


def build_prompt(markdown_text: str, style: str) -> str:
    style_line = (
        "Prefer natural, fluent Korean wording while keeping technical precision."
        if style == "natural"
        else "Prefer literal Korean wording while keeping technical precision."
    )
    return (
        "Translate the following English technical Markdown into Korean.\n"
        "Return only translated Markdown.\n"
        "Preserve Markdown structure, heading hierarchy, bullet/numbered lists, and tables.\n"
        "Do not change URLs.\n"
        "Do not translate code blocks, inline code, CLI flags, file paths, env vars, API endpoints, or model IDs.\n"
        f"{style_line}\n\n"
        "<SOURCE_MARKDOWN>\n"
        f"{markdown_text}\n"
        "</SOURCE_MARKDOWN>\n"
    )


def run_codex_translate(
    prompt: str,
    output_file: Path,
    model: str,
    reasoning_effort: str,
    workdir: Path,
    timeout_seconds: int,
) -> tuple[int, str]:
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "--model",
        model,
        "-c",
        f"model_reasoning_effort={reasoning_effort}",
        "--output-last-message",
        str(output_file),
        "-",
    ]
    try:
        proc = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            cwd=str(workdir),
            capture_output=True,
            timeout=timeout_seconds,
        )
        logs = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode, logs
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        logs = stdout + stderr
        return 124, logs + f"\n[TIMEOUT] exceeded {timeout_seconds}s\n"


def main() -> int:
    args = parse_args()
    if not args.source_root.exists():
        print(f"[ERROR] source root does not exist: {args.source_root}", file=sys.stderr)
        return 2

    files = find_markdown_files(args.source_root)
    if args.limit is not None:
        files = files[: max(args.limit, 0)]
    if not files:
        print("[ERROR] no markdown files found", file=sys.stderr)
        return 2

    args.dest_root.mkdir(parents=True, exist_ok=True)
    manifest_path = args.manifest or (args.dest_root / "manifest-ko.json")

    results: list[dict] = []
    failures = 0
    total = len(files)

    for idx, src_path in enumerate(files, start=1):
        rel = src_path.relative_to(args.source_root)
        dst_path = args.dest_root / rel

        if dst_path.exists() and not args.force:
            print(f"[{idx}/{total}] SKIP {rel}", flush=True)
            results.append(
                {
                    "source": str(src_path),
                    "dest": str(dst_path),
                    "status": "skipped_existing",
                }
            )
            continue

        markdown_text = src_path.read_text(encoding="utf-8")
        chunks = split_markdown_chunks(markdown_text, max_chars=args.max_chars)
        dst_path.parent.mkdir(parents=True, exist_ok=True)

        chunk_note = f" ({len(chunks)} chunk(s))" if len(chunks) > 1 else ""
        print(f"[{idx}/{total}] TRANSLATE {rel}{chunk_note}", flush=True)
        ok = False
        last_error = ""
        translated_chunks: list[str] = []

        for chunk_index, chunk in enumerate(chunks, start=1):
            if len(chunks) > 1:
                print(
                    f"  [chunk {chunk_index}/{len(chunks)}] {rel}",
                    flush=True,
                )
            prompt = build_prompt(chunk, style=args.style)
            chunk_ok = False
            for attempt in range(1, args.retries + 1):
                with tempfile.NamedTemporaryFile(
                    mode="w+",
                    suffix=".md",
                    delete=False,
                    encoding="utf-8",
                ) as tmp:
                    tmp_path = Path(tmp.name)

                code, logs = run_codex_translate(
                    prompt=prompt,
                    output_file=tmp_path,
                    model=args.model,
                    reasoning_effort=args.reasoning_effort,
                    workdir=args.workdir,
                    timeout_seconds=args.timeout_seconds,
                )
                if code == 0 and tmp_path.exists():
                    translated = tmp_path.read_text(encoding="utf-8")
                    translated = maybe_unwrap_markdown_fence(translated)
                    translated_chunks.append(translated.strip())
                    tmp_path.unlink(missing_ok=True)
                    chunk_ok = True
                    break

                tmp_path.unlink(missing_ok=True)
                last_error = logs[-3000:]
                print(
                    "  "
                    f"[retry {attempt}/{args.retries}] "
                    f"chunk {chunk_index}/{len(chunks)} failed for {rel} (code={code})",
                    flush=True,
                )
                time.sleep(min(2.0, 0.5 * attempt))

            if not chunk_ok:
                ok = False
                break

        if translated_chunks and len(translated_chunks) == len(chunks):
            final_text = "\n\n".join(part for part in translated_chunks if part).rstrip() + "\n"
            dst_path.write_text(final_text, encoding="utf-8")
            ok = True
            results.append(
                {
                    "source": str(src_path),
                    "dest": str(dst_path),
                    "status": "translated",
                    "chunks": len(chunks),
                }
            )

        if not ok:
            failures += 1
            print(f"[ERROR] failed: {rel}", file=sys.stderr, flush=True)
            results.append(
                {
                    "source": str(src_path),
                    "dest": str(dst_path),
                    "status": "error",
                    "error_tail": last_error,
                }
            )

        time.sleep(args.interval)

    manifest_path.write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"[INFO] wrote manifest: {manifest_path}", flush=True)
    print(f"[INFO] failures: {failures}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
