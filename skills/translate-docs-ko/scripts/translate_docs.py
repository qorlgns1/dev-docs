#!/usr/bin/env python3
"""
Translate documentation pages into Korean Markdown.

Features:
- Collect URLs from sitemap and keep only pages under the base path.
- Extract main page content and convert HTML to Markdown.
- Optionally translate Markdown with the OpenAI Responses API.
- Save deterministic output trees: <output>/en/... and <output>/ko/...
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse


def require_module(name: str, import_name: str | None = None):
    module_name = import_name or name
    try:
        return __import__(module_name)
    except ImportError:
        print(
            f"[ERROR] Missing dependency: {module_name}. "
            "Install with: python3 -m pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(2)


bs4 = require_module("beautifulsoup4", "bs4")
html2text = require_module("html2text")
httpx = require_module("httpx")


USER_AGENT = "translate-docs-ko/1.0"


@dataclass
class Config:
    base_url: str
    output_dir: Path
    model: str
    target_language: str
    no_translate: bool
    force: bool
    limit: int | None
    max_chars: int
    request_interval: float
    retries: int
    urls_file: Path | None


def canonicalize_url(url: str) -> str:
    parsed = urlparse(url)
    scheme = parsed.scheme or "https"
    netloc = parsed.netloc
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return urlunparse((scheme, netloc, path, "", "", ""))


def fetch_text(url: str, timeout: int = 30) -> str:
    response = httpx.get(
        url,
        timeout=timeout,
        follow_redirects=True,
        headers={"User-Agent": USER_AGENT},
    )
    response.raise_for_status()
    return response.text


def parse_xml_locs(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [node.text.strip() for node in root.findall(".//sm:loc", ns) if node.text]


def in_scope(url: str, scope_path: str) -> bool:
    path = urlparse(url).path.rstrip("/")
    scope = scope_path.rstrip("/")
    return path == scope or path.startswith(scope + "/")


def collect_urls_from_sitemap(base_url: str) -> list[str]:
    parsed = urlparse(base_url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Invalid base URL: {base_url}")

    scope_path = parsed.path.rstrip("/") or "/"
    origin = f"{parsed.scheme}://{parsed.netloc}"
    sitemap_index_url = f"{origin}/sitemap-index.xml"

    sitemap_index = fetch_text(sitemap_index_url)
    sitemap_urls = parse_xml_locs(sitemap_index)
    if not sitemap_urls:
        raise RuntimeError(f"No sitemap entries found in {sitemap_index_url}")

    urls: list[str] = []
    for sitemap_url in sitemap_urls:
        sitemap_xml = fetch_text(sitemap_url)
        for loc in parse_xml_locs(sitemap_xml):
            normalized = canonicalize_url(loc)
            if in_scope(normalized, scope_path):
                urls.append(normalized)

    # Ensure the base URL is included.
    urls.append(canonicalize_url(base_url))

    deduped = sorted(set(urls))
    return deduped


def load_urls_from_file(path: Path) -> list[str]:
    urls: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        urls.append(canonicalize_url(line))
    return sorted(set(urls))


def choose_main_node(soup):
    selectors = [
        "article",
        "main article",
        "main",
        "[data-pagefind-body]",
        "[data-content]",
        "body",
    ]
    for selector in selectors:
        node = soup.select_one(selector)
        if node and len(node.get_text(" ", strip=True)) > 200:
            return node
    return soup.body or soup


def clean_main_node(main_node, page_url: str):
    for selector in [
        "script",
        "style",
        "noscript",
        "template",
        "svg",
        "canvas",
        "header",
        "footer",
        "nav",
        "aside",
        "[aria-hidden='true']",
        "[class*='sidebar']",
        "[class*='toc']",
        "[data-pagefind-ignore]",
    ]:
        for node in main_node.select(selector):
            node.decompose()

    for tag in main_node.select("a[href]"):
        tag["href"] = urljoin(page_url, tag["href"])
    for tag in main_node.select("img[src]"):
        tag["src"] = urljoin(page_url, tag["src"])


def html_to_markdown(html: str, page_url: str) -> str:
    soup = bs4.BeautifulSoup(html, "html.parser")
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    if not title:
        h1 = soup.find("h1")
        title = h1.get_text(strip=True) if h1 else page_url

    main_node = choose_main_node(soup)
    clean_main_node(main_node, page_url)

    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_images = True
    converter.ignore_emphasis = False
    converter.ignore_links = False
    converter.mark_code = True
    converter.single_line_break = False

    body_md = converter.handle(str(main_node)).strip()
    lines = [
        f"# {title}",
        "",
        f"Source URL: {page_url}",
        "",
        body_md,
    ]
    return "\n".join(lines).strip() + "\n"


def split_markdown(markdown_text: str, max_chars: int) -> list[str]:
    chunks: list[str] = []
    buffer: list[str] = []
    length = 0
    in_code = False

    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code

        line_len = len(line) + 1
        if buffer and (length + line_len) > max_chars and not in_code:
            chunks.append("\n".join(buffer).strip())
            buffer = [line]
            length = line_len
            continue

        buffer.append(line)
        length += line_len

    if buffer:
        chunks.append("\n".join(buffer).strip())
    return [chunk for chunk in chunks if chunk]


def extract_response_text(response) -> str:
    output_text = getattr(response, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    parts: list[str] = []
    for output in getattr(response, "output", []) or []:
        for content in getattr(output, "content", []) or []:
            text_value = getattr(content, "text", None)
            if isinstance(text_value, str):
                parts.append(text_value)
                continue
            if hasattr(text_value, "value") and isinstance(text_value.value, str):
                parts.append(text_value.value)
    return "\n".join(parts).strip()


def translate_chunk(client, model: str, text: str, target_language: str) -> str:
    system_prompt = (
        f"Translate English technical Markdown into {target_language}. "
        "Preserve Markdown structure, links, tables, and code fences. "
        "Do not translate source code, paths, command flags, URLs, or environment variable names. "
        "Return only translated Markdown."
    )
    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
    )
    translated = extract_response_text(response)
    if not translated:
        raise RuntimeError("Translation API returned empty output.")
    return translated


def translate_markdown(client, model: str, markdown_text: str, target_language: str, max_chars: int, retries: int) -> str:
    chunks = split_markdown(markdown_text, max_chars=max_chars)
    translated_chunks: list[str] = []
    total = len(chunks)
    for index, chunk in enumerate(chunks, start=1):
        last_error: Exception | None = None
        for attempt in range(1, retries + 1):
            try:
                print(f"  - Translating chunk {index}/{total} (attempt {attempt})")
                translated_chunks.append(
                    translate_chunk(client, model=model, text=chunk, target_language=target_language)
                )
                last_error = None
                break
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                sleep_seconds = min(4.0, 0.6 * attempt)
                time.sleep(sleep_seconds)
        if last_error:
            raise RuntimeError(f"Chunk translation failed: {last_error}") from last_error
    return "\n\n".join(translated_chunks).strip() + "\n"


def url_to_output_relpath(url: str) -> Path:
    path = urlparse(url).path.rstrip("/")
    if not path:
        return Path("index.md")
    return Path(path.lstrip("/")) / "index.md"


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description="Translate documentation to Korean Markdown.")
    parser.add_argument(
        "--base-url",
        default="https://developers.openai.com/codex/",
        help="Base URL whose sitemap subtree should be translated.",
    )
    parser.add_argument(
        "--output-dir",
        default="docs/codex",
        help="Output directory for generated Markdown files.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5-mini",
        help="OpenAI model name for translation.",
    )
    parser.add_argument(
        "--target-language",
        default="Korean",
        help="Target translation language.",
    )
    parser.add_argument("--no-translate", action="store_true", help="Only export English Markdown.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output files.")
    parser.add_argument("--limit", type=int, default=None, help="Process only the first N URLs.")
    parser.add_argument(
        "--max-chars",
        type=int,
        default=6000,
        help="Max characters per translation chunk.",
    )
    parser.add_argument(
        "--request-interval",
        type=float,
        default=0.2,
        help="Delay in seconds between page requests.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Retry count for translation API calls.",
    )
    parser.add_argument(
        "--urls-file",
        type=Path,
        default=None,
        help="Optional file with explicit URLs (one per line). If provided, skip sitemap discovery.",
    )
    args = parser.parse_args()

    return Config(
        base_url=args.base_url,
        output_dir=Path(args.output_dir),
        model=args.model,
        target_language=args.target_language,
        no_translate=args.no_translate,
        force=args.force,
        limit=args.limit,
        max_chars=args.max_chars,
        request_interval=args.request_interval,
        retries=args.retries,
        urls_file=args.urls_file,
    )


def main() -> int:
    config = parse_args()
    config.output_dir.mkdir(parents=True, exist_ok=True)

    if config.urls_file:
        if not config.urls_file.exists():
            print(f"[ERROR] URLs file not found: {config.urls_file}", file=sys.stderr)
            return 2
        urls = load_urls_from_file(config.urls_file)
    else:
        urls = collect_urls_from_sitemap(config.base_url)

    if config.limit is not None:
        urls = urls[: max(config.limit, 0)]

    if not urls:
        print("[ERROR] No URLs found to process.", file=sys.stderr)
        return 2

    do_translate = not config.no_translate
    client = None
    if do_translate:
        openai_module = require_module("openai")
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("[ERROR] OPENAI_API_KEY is not set. Use --no-translate or set the API key.", file=sys.stderr)
            return 2
        client = openai_module.OpenAI(api_key=api_key)

    records: list[dict] = []
    en_root = config.output_dir / "en"
    ko_root = config.output_dir / "ko"
    failures = 0

    print(f"[INFO] Processing {len(urls)} page(s)")
    for idx, url in enumerate(urls, start=1):
        rel = url_to_output_relpath(url)
        en_path = en_root / rel
        ko_path = ko_root / rel

        if (
            not config.force
            and en_path.exists()
            and (config.no_translate or ko_path.exists())
        ):
            print(f"[{idx}/{len(urls)}] SKIP {url}")
            records.append(
                {
                    "url": url,
                    "en_path": str(en_path),
                    "ko_path": str(ko_path),
                    "status": "skipped_existing",
                }
            )
            continue

        print(f"[{idx}/{len(urls)}] FETCH {url}")
        try:
            html = fetch_text(url)
            english_markdown = html_to_markdown(html, page_url=url)
            write_text(en_path, english_markdown)

            status = "exported_en"
            if do_translate:
                translated = translate_markdown(
                    client=client,
                    model=config.model,
                    markdown_text=english_markdown,
                    target_language=config.target_language,
                    max_chars=config.max_chars,
                    retries=config.retries,
                )
                write_text(ko_path, translated)
                status = "exported_en_ko"

            records.append(
                {
                    "url": url,
                    "en_path": str(en_path),
                    "ko_path": str(ko_path),
                    "status": status,
                }
            )
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"[ERROR] {url}: {exc}", file=sys.stderr)
            records.append(
                {
                    "url": url,
                    "en_path": str(en_path),
                    "ko_path": str(ko_path),
                    "status": "error",
                    "error": str(exc),
                }
            )

        time.sleep(config.request_interval)

    manifest_path = config.output_dir / "manifest.json"
    write_text(manifest_path, json.dumps(records, ensure_ascii=False, indent=2) + "\n")
    print(f"[INFO] Wrote manifest: {manifest_path}")
    print(f"[INFO] Failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
