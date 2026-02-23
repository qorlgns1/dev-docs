#!/usr/bin/env python3
"""
Step 1: URL → English Markdown

Crawls a documentation site via sitemap and saves English Markdown
to src/content/docs/en/<section>/.

Usage:
  python3 fetch.py --url https://developers.openai.com/codex/
  python3 fetch.py --url https://nextjs.org/docs --section nextjs
"""

from __future__ import annotations

import argparse
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
import re
from urllib.parse import urljoin, urlparse, urlunparse


def require(name: str, import_name: str | None = None):
    try:
        return __import__(import_name or name)
    except ImportError:
        print(f"[ERROR] Missing: {import_name or name}. Run: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(2)


bs4 = require("beautifulsoup4", "bs4")
html2text = require("html2text")
httpx = require("httpx")

REPO_ROOT = Path(__file__).parent.parent.parent.parent
EN_DOCS = REPO_ROOT / "src/content/docs/en"
USER_AGENT = "add-doc/1.0"
GENERIC_SEGMENTS = {
    "docs",
    "doc",
    "documentation",
    "guide",
    "guides",
    "learn",
    "manual",
    "reference",
    "references",
    "api",
    "apis",
    "developer",
    "developers",
}


# ── URL helpers ──────────────────────────────────────────────────────────────

def canonicalize(url: str) -> str:
    p = urlparse(url)
    path = p.path.rstrip("/") or "/"
    return urlunparse((p.scheme or "https", p.netloc, path, "", "", ""))


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "docs"


def infer_section(base_url: str) -> tuple[str, str]:
    p = urlparse(base_url)
    path_segments = [seg for seg in p.path.split("/") if seg]
    non_generic = [seg for seg in path_segments if seg.lower() not in GENERIC_SEGMENTS]

    # path에서 의미 있는 세그먼트가 있으면 우선 사용 (예: /codex, /docs/react)
    if non_generic:
        return slugify(non_generic[-1]), "path"

    # path가 전부 generic이면 도메인에서 후보 추출 (예: nextjs.org -> nextjs)
    host_parts = [h for h in p.netloc.lower().split(".") if h and h != "www"]
    if host_parts:
        return slugify(host_parts[0]), "domain"

    return "docs", "fallback"


def in_scope(url: str, scope: str) -> bool:
    path = urlparse(url).path.rstrip("/")
    scope = scope.rstrip("/")
    return path == scope or path.startswith(scope + "/")


def fetch(url: str) -> str:
    r = httpx.get(url, timeout=30, follow_redirects=True, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    return r.text


def parse_locs(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [n.text.strip() for n in root.findall(".//sm:loc", ns) if n.text]


def collect_urls(base_url: str) -> list[str]:
    p = urlparse(base_url)
    scope = p.path.rstrip("/") or "/"
    origin = f"{p.scheme}://{p.netloc}"

    index_xml = fetch(f"{origin}/sitemap-index.xml")
    sitemaps = parse_locs(index_xml)

    urls: list[str] = []
    for sm in sitemaps:
        for loc in parse_locs(fetch(sm)):
            norm = canonicalize(loc)
            if in_scope(norm, scope):
                urls.append(norm)

    urls.append(canonicalize(base_url))
    return sorted(set(urls))


def url_to_relpath(url: str, base_path: str) -> Path:
    """URL → relative path under the section directory."""
    path = urlparse(url).path.rstrip("/")
    base = base_path.rstrip("/")
    if path == base:
        return Path("index.md")
    rel = path[len(base):].lstrip("/")
    return Path(rel) / "index.md"


# ── HTML → Markdown ──────────────────────────────────────────────────────────

def choose_main(soup):
    for sel in ["article", "main article", "main", "[data-pagefind-body]", "[data-content]", "body"]:
        node = soup.select_one(sel)
        if node and len(node.get_text(" ", strip=True)) > 200:
            return node
    return soup.body or soup


def clean_node(node, page_url: str):
    for sel in [
        "script", "style", "noscript", "template", "svg", "canvas",
        "header", "footer", "nav", "aside",
        "[aria-hidden='true']", "[class*='sidebar']", "[class*='toc']", "[data-pagefind-ignore]",
    ]:
        for el in node.select(sel):
            el.decompose()

    for a in node.select("a[href]"):
        a["href"] = urljoin(page_url, a["href"])
    for img in node.select("img[src]"):
        img["src"] = urljoin(page_url, img["src"])


def html_to_markdown(html: str, page_url: str) -> str:
    soup = bs4.BeautifulSoup(html, "html.parser")

    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    if not title:
        h1 = soup.find("h1")
        title = h1.get_text(strip=True) if h1 else page_url

    main = choose_main(soup)
    clean_node(main, page_url)

    conv = html2text.HTML2Text()
    conv.body_width = 0
    conv.ignore_images = True
    conv.ignore_links = False
    conv.mark_code = True
    conv.single_line_break = False

    body = conv.handle(str(main)).strip()
    return f"# {title}\n\nSource URL: {page_url}\n\n{body}\n"


# ── Main ─────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Fetch documentation → English Markdown")
    p.add_argument("--url", required=True, help="Base URL (e.g. https://developers.openai.com/codex/)")
    p.add_argument("--section", default=None, help="Section name (auto-derived from URL if omitted)")
    p.add_argument("--force", action="store_true", help="Overwrite existing files")
    p.add_argument("--limit", type=int, default=None, help="Max pages to fetch")
    p.add_argument("--interval", type=float, default=0.2, help="Delay between requests (s)")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    base_url = canonicalize(args.url)
    base_path = urlparse(base_url).path.rstrip("/") or "/"

    if args.section:
        section = slugify(args.section)
        section_source = "manual"
    else:
        section, inferred_by = infer_section(base_url)
        section_source = f"auto:{inferred_by}"
    out_root = EN_DOCS / section

    print(f"[fetch] URL   : {base_url}", flush=True)
    print(f"[fetch] Section: {section} ({section_source})", flush=True)
    print(f"[fetch] Output : {out_root}", flush=True)

    urls = collect_urls(base_url)
    if args.limit:
        urls = urls[:args.limit]
    total = len(urls)
    print(f"[fetch] Found {total} URL(s)", flush=True)

    failures = 0
    for i, url in enumerate(urls, 1):
        rel = url_to_relpath(url, base_path)
        dst = out_root / rel

        if dst.exists() and not args.force:
            print(f"[{i}/{total}] SKIP {rel}", flush=True)
            continue

        print(f"[{i}/{total}] FETCH {url}", flush=True)
        try:
            html = fetch(url)
            md = html_to_markdown(html, url)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(md, encoding="utf-8")
        except Exception as e:
            print(f"[ERROR] {url}: {e}", file=sys.stderr)
            failures += 1

        time.sleep(args.interval)

    print(f"[fetch] Done. Failures: {failures}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
