#!/usr/bin/env python3
"""
Step 2: English Markdown → Korean Markdown (Codex CLI)

Translates all .md files under --source-root to --dest-root
using `codex exec`. No API key required.

Usage:
  python3 translate.py --source-root src/content/docs/en/codex \
                       --dest-root   src/content/docs/codex
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent.parent.parent
LEGACY_CODE_OPEN_RE = re.compile(r"^(?:>\s*)?\[code\].*$", re.IGNORECASE)
LEGACY_CODE_CLOSE_RE = re.compile(r"^(?:>\s*)?\[/code\]\s*$", re.IGNORECASE)


# ── Chunking ─────────────────────────────────────────────────────────────────

def split_chunks(text: str, max_chars: int) -> list[str]:
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
        elif not in_code and LEGACY_CODE_OPEN_RE.match(stripped):
            in_code = True
        elif in_code and LEGACY_CODE_CLOSE_RE.match(stripped):
            in_code = False

        line_size = len(line) + 1
        if buf and size + line_size > max_chars and not in_code:
            chunks.append("\n".join(buf).strip())
            buf, size = [line], line_size
        else:
            buf.append(line)
            size += line_size

    if buf:
        chunks.append("\n".join(buf).strip())
    return [c for c in chunks if c]


def unwrap_fence(text: str) -> str:
    s = text.strip()
    if not s.startswith("```"):
        return text
    lines = s.splitlines()
    if len(lines) < 3 or lines[-1].strip() != "```":
        return text
    if lines[0].strip().lower() in {"```", "```md", "```markdown"}:
        return "\n".join(lines[1:-1]).rstrip() + "\n"
    return text


# ── Codex exec ───────────────────────────────────────────────────────────────

PROMPT_TMPL = """\
Translate the following English technical Markdown into Korean.
Return only translated Markdown.
Preserve Markdown structure, heading hierarchy, bullet/numbered lists, and tables.
Do not change URLs.
Do not translate code blocks, inline code, CLI flags, file paths, env vars, API endpoints, or model IDs.
Prefer natural, fluent Korean wording while keeping technical precision.

<SOURCE_MARKDOWN>
{text}
</SOURCE_MARKDOWN>
"""


def run_codex(prompt: str, out_file: Path, model: str, effort: str, timeout: int) -> tuple[int, str]:
    cmd = [
        "codex", "exec",
        "--skip-git-repo-check",
        "--model", model,
        "-c", f"model_reasoning_effort={effort}",
        "--output-last-message", str(out_file),
        "-",
    ]
    try:
        proc = subprocess.run(
            cmd, input=prompt, text=True,
            cwd=str(REPO_ROOT), capture_output=True, timeout=timeout,
        )
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")
    except subprocess.TimeoutExpired as e:
        logs = (e.stdout or b"").decode("utf-8", errors="replace")
        return 124, logs + f"\n[TIMEOUT] {timeout}s exceeded"


def translate_file(src: Path, dst: Path, model: str, effort: str,
                   max_chars: int, retries: int, timeout: int) -> bool:
    text = src.read_text(encoding="utf-8")
    chunks = split_chunks(text, max_chars)
    results: list[str] = []

    for ci, chunk in enumerate(chunks, 1):
        prompt = PROMPT_TMPL.format(text=chunk)
        ok = False
        for attempt in range(1, retries + 1):
            with tempfile.NamedTemporaryFile(mode="w+", suffix=".md", delete=False, encoding="utf-8") as f:
                tmp = Path(f.name)
            code, _ = run_codex(prompt, tmp, model, effort, timeout)
            if code == 0 and tmp.exists():
                translated = unwrap_fence(tmp.read_text(encoding="utf-8"))
                results.append(translated.strip())
                tmp.unlink(missing_ok=True)
                ok = True
                break
            tmp.unlink(missing_ok=True)
            if len(chunks) > 1:
                print(f"  [retry {attempt}/{retries}] chunk {ci}/{len(chunks)}", flush=True)
            time.sleep(min(2.0, 0.5 * attempt))

        if not ok:
            return False

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("\n\n".join(results).rstrip() + "\n", encoding="utf-8")
    return True


# ── Main ─────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Translate Markdown tree to Korean via Codex CLI")
    p.add_argument("--source-root", type=Path, required=True)
    p.add_argument("--dest-root", type=Path, required=True)
    p.add_argument("--model", default="gpt-5.1-codex-mini")
    p.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh"])
    p.add_argument("--max-chars", type=int, default=12000)
    p.add_argument("--retries", type=int, default=3)
    p.add_argument("--timeout", type=int, default=240)
    p.add_argument("--interval", type=float, default=0.1)
    p.add_argument("--force", action="store_true", help="Re-translate existing files")
    p.add_argument("--limit", type=int, default=None)
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if not args.source_root.exists():
        print(f"[ERROR] source-root not found: {args.source_root}", file=sys.stderr)
        return 2

    files = sorted(args.source_root.rglob("*.md"))
    if args.limit:
        files = files[:args.limit]
    total = len(files)
    print(f"[translate] {total} file(s)  {args.source_root} → {args.dest_root}", flush=True)

    failures = 0
    for i, src in enumerate(files, 1):
        rel = src.relative_to(args.source_root)
        dst = args.dest_root / rel

        if dst.exists() and not args.force:
            print(f"[{i}/{total}] SKIP {rel}", flush=True)
            continue

        chunks_note = ""
        text = src.read_text(encoding="utf-8")
        n_chunks = len(split_chunks(text, args.max_chars))
        if n_chunks > 1:
            chunks_note = f" ({n_chunks} chunks)"

        print(f"[{i}/{total}] TRANSLATE {rel}{chunks_note}", flush=True)
        ok = translate_file(src, dst, args.model, args.effort,
                            args.max_chars, args.retries, args.timeout)
        if not ok:
            print(f"[ERROR] failed: {rel}", file=sys.stderr)
            failures += 1

        time.sleep(args.interval)

    print(f"[translate] Done. Failures: {failures}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
