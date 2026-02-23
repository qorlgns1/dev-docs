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
import json
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
REFS_DIR = REPO_ROOT / "skills/add-doc/references"
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

FEEDBACK_NOISE_LINES = {
    "copy page",
    "페이지 복사",
    "was this helpful?",
    "도움이 되었나요?",
    "send",
    "전송",
    "supported.",
    "지원됨.",
}
META_NOISE_PREFIXES = (
    "@doc-version:",
    "@last-updated:",
)

CARD_HEADING_RE = re.compile(r"^(#{3,6})\s+\[([^\]]+)\]\((https?://[^)\s]+)\)\s*$")
BREADCRUMB_RE = re.compile(r"^\[[^\]]+\]\([^)]+\)\[[^\]]+\]\([^)]+\)\S*$")
MD_LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
LEGACY_CODE_OPEN_RE = re.compile(r"^(?P<prefix>\s*(?:>\s*)*)\[code\](?P<rest>.*)$", re.IGNORECASE)
LEGACY_CODE_CLOSE_RE = re.compile(r"^(?P<prefix>\s*(?:>\s*)*)\[/code\]\s*$", re.IGNORECASE)


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


def markdown_candidate(url: str) -> str:
    p = urlparse(url)
    path = p.path.rstrip("/")
    if not path:
        path = "/index"
    if not path.endswith(".md"):
        path = f"{path}.md"
    return urlunparse((p.scheme, p.netloc, path, "", "", ""))


def looks_like_markdown(text: str) -> bool:
    sample = text.lstrip()[:800].lower()
    if sample.startswith("<!doctype html") or sample.startswith("<html"):
        return False
    return bool(re.search(r"(?m)^#\s+\S", text) or re.search(r"(?m)^[-*]\s+\[", text))


def absolutize_markdown_links(text: str, page_url: str) -> str:
    def repl(m: re.Match[str]) -> str:
        href = m.group(2).strip()
        if not href:
            return m.group(0)
        if href.startswith("#") or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", href):
            return m.group(0)
        return f"{m.group(1)}{urljoin(page_url, href)}{m.group(3)}"

    return MD_LINK_RE.sub(repl, text)


def fetch_markdown_source(page_url: str) -> str | None:
    md_url = markdown_candidate(page_url)
    if md_url == page_url:
        return None

    try:
        r = httpx.get(
            md_url,
            timeout=30,
            follow_redirects=True,
            headers={"User-Agent": USER_AGENT},
        )
        if r.status_code == 200 and looks_like_markdown(r.text):
            return absolutize_markdown_links(r.text, page_url)
    except Exception:
        return None
    return None


def parse_locs(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [n.text.strip() for n in root.findall(".//sm:loc", ns) if n.text]


def parse_sitemap(xml_text: str) -> tuple[str, list[str]]:
    """
    Parse sitemap XML and return (kind, locs)
    kind: "sitemapindex" | "urlset" | "unknown"
    """
    root = ET.fromstring(xml_text)
    tag = root.tag.split("}")[-1].lower()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [n.text.strip() for n in root.findall(".//sm:loc", ns) if n.text]
    if tag == "sitemapindex":
        return "sitemapindex", locs
    if tag == "urlset":
        return "urlset", locs
    return "unknown", locs


def collect_urls(base_url: str) -> list[str]:
    p = urlparse(base_url)
    scope = p.path.rstrip("/") or "/"
    origin = f"{p.scheme}://{p.netloc}"

    urls: list[str] = []
    sitemap_entries: list[str] = []

    for sitemap_url in (f"{origin}/sitemap-index.xml", f"{origin}/sitemap.xml"):
        try:
            xml = fetch(sitemap_url)
        except Exception:
            continue
        kind, locs = parse_sitemap(xml)
        if kind == "sitemapindex":
            sitemap_entries.extend(locs)
            break
        if kind == "urlset":
            for loc in locs:
                norm = canonicalize(loc)
                if in_scope(norm, scope):
                    urls.append(norm)
            break

    for sm in sitemap_entries:
        try:
            sm_xml = fetch(sm)
        except Exception:
            continue
        kind, locs = parse_sitemap(sm_xml)
        if kind == "urlset":
            for loc in locs:
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

    # html2text가 본문 H1을 놓치는 경우에만 fallback 제목을 앞에 붙인다.
    if not re.search(r"(?m)^#\s+\S", body):
        body = f"# {title}\n\n{body}"

    md = f"Source URL: {page_url}\n\n{body}\n"
    return normalize_markdown(md)


def page_to_markdown(page_url: str) -> str:
    md_src = fetch_markdown_source(page_url)
    if md_src is not None:
        return normalize_markdown(f"Source URL: {page_url}\n\n{md_src}\n")

    html = fetch(page_url)
    return html_to_markdown(html, page_url)


def normalize_markdown(md: str) -> str:
    """
    Post-process markdown generated by html2text.
    - Split compacted card headings: `... )### [ ... ]`
    - Convert heading-style cards (`### [..](..)` ) to bullet links
    - Remove common feedback/breadcrumb noise lines
    - Convert legacy [code]...[/code] blocks to fenced code blocks
    """
    md = normalize_legacy_code_blocks(md)

    # 카드 링크가 한 줄에 이어붙는 패턴 분리
    md = re.sub(r"\)(?=#{3,6}\s+\[)", ")\n\n", md)
    md = re.sub(r"(?<!\n)(#{3,6}\s+\[)", r"\n\1", md)

    out: list[str] = []
    in_code = False

    for raw in md.splitlines():
        line = raw.rstrip()
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue

        if in_code:
            out.append(line)
            continue

        if stripped and stripped.lower() in FEEDBACK_NOISE_LINES:
            continue

        if stripped and stripped.lower().startswith(META_NOISE_PREFIXES):
            continue

        if stripped and BREADCRUMB_RE.match(stripped):
            continue

        if "docs/llms.txt" in stripped and "overview" in stripped.lower():
            continue

        m = CARD_HEADING_RE.match(stripped)
        if m:
            label = m.group(2).strip()
            href = m.group(3).strip()
            out.append(f"- [{label}]({href})")
            continue

        out.append(line)

    normalized = "\n".join(out)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized).strip() + "\n"
    return normalized


def normalize_legacy_code_blocks(md: str) -> str:
    """
    Convert legacy markdown code tags into fenced code blocks.
    Supports plain (`[code]`) and blockquote-prefixed (`> [code]`) forms.
    """
    out: list[str] = []
    in_legacy_code = False
    fence_prefix = ""
    code_lines: list[str] = []

    def flush_legacy_block() -> None:
        # Pick a fence length that will not conflict with backticks
        # inside the captured code lines.
        max_backticks = 0
        for code_line in code_lines:
            for m in re.finditer(r"`+", code_line):
                max_backticks = max(max_backticks, len(m.group(0)))
        fence = "`" * max(3, max_backticks + 1)

        out.append(f"{fence_prefix}{fence}")
        out.extend(code_lines)
        out.append(f"{fence_prefix}{fence}")

    for raw in md.splitlines():
        line = raw.rstrip()

        if not in_legacy_code:
            m_open = LEGACY_CODE_OPEN_RE.match(line)
            if not m_open:
                # Some sources include stray closing tags without a matching opener.
                # Drop them to avoid leaking raw [/code] markers into rendered docs.
                if LEGACY_CODE_CLOSE_RE.match(line):
                    continue
                out.append(line)
                continue

            fence_prefix = m_open.group("prefix") or ""
            code_lines = []

            first_code_line = (m_open.group("rest") or "").lstrip()
            if first_code_line:
                code_lines.append(f"{fence_prefix}{first_code_line}")

            in_legacy_code = True
            continue

        m_close = LEGACY_CODE_CLOSE_RE.match(line)
        if m_close and (m_close.group("prefix") or "") == fence_prefix:
            flush_legacy_block()
            in_legacy_code = False
            fence_prefix = ""
            code_lines = []
            continue

        code_lines.append(line)

    if in_legacy_code:
        flush_legacy_block()

    return "\n".join(out)


# ── Nav extraction ───────────────────────────────────────────────────────────

def _find_nav_node(soup):
    """사이드바 내비게이션 노드를 찾아 반환."""
    for sel in [
        "nav[aria-label*='sidebar' i]",
        "nav[aria-label*='documentation' i]",
        "[data-testid*='sidebar']",
        "[class*='sidebar'] > nav",
        "[class*='sidebar'] > ul",
        "aside > nav",
        "nav",
    ]:
        for node in soup.select(sel):
            if len(node.find_all("a")) >= 4:
                return node
    return None


def _parse_ul(ul, base_url: str, base_path: str) -> list[dict]:
    items = []
    for li in ul.find_all("li", recursive=False):
        item = _parse_li(li, base_url, base_path)
        if item:
            items.append(item)
    return items


def _parse_li(li, base_url: str, base_path: str) -> dict | None:
    a = li.find("a", recursive=False)
    sub_ul = li.find("ul")

    label, url = "", None

    if a:
        label = a.get_text(strip=True)
        href = a.get("href", "")
        if href:
            abs_url = canonicalize(urljoin(base_url, href))
            if in_scope(abs_url, base_path):
                url = abs_url

    if not label:
        for child in li.children:
            if hasattr(child, "name") and child.name not in ("ul", "li", "a"):
                t = child.get_text(strip=True)
                if t:
                    label = t
                    break

    if not label:
        return None

    if sub_ul:
        children = _parse_ul(sub_ul, base_url, base_path)
        if not children and url is None:
            return None
        item: dict = {"label": label, "items": children}
        if url:
            item["url"] = url
        return item
    elif url:
        return {"label": label, "url": url}
    return None


def _item_count(items: list) -> int:
    total = len(items)
    for item in items:
        if "items" in item:
            total += _item_count(item["items"])
    return total


def extract_nav(base_url: str, base_path: str, section: str) -> bool:
    """메인 페이지에서 내비게이션 구조를 추출해 references/<section>-nav.json 으로 저장."""
    print(f"[nav] Extracting navigation from {base_url}", flush=True)
    try:
        html = fetch(base_url)
    except Exception as e:
        print(f"[nav] Warning: could not fetch page: {e}", file=sys.stderr)
        return False

    soup = bs4.BeautifulSoup(html, "html.parser")
    nav_node = _find_nav_node(soup)
    if not nav_node:
        print("[nav] No navigation element found", file=sys.stderr)
        return False

    top_ul = nav_node if nav_node.name == "ul" else nav_node.find("ul")
    if not top_ul:
        print("[nav] No <ul> inside nav element", file=sys.stderr)
        return False

    items = _parse_ul(top_ul, base_url, base_path)
    if not items:
        print("[nav] Empty navigation (no in-scope links found)", file=sys.stderr)
        return False

    REFS_DIR.mkdir(parents=True, exist_ok=True)
    out_file = REFS_DIR / f"{section}-nav.json"
    out_file.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"[nav] Saved: {out_file.relative_to(REPO_ROOT)} "
        f"({_item_count(items)} items, {len(items)} top-level groups)",
        flush=True,
    )
    return True


# ── Main ─────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Fetch documentation → English Markdown")
    p.add_argument("--url", required=True, help="Base URL (e.g. https://developers.openai.com/codex/)")
    p.add_argument("--section", default=None, help="Section name (auto-derived from URL if omitted)")
    p.add_argument("--force", action="store_true", help="Overwrite existing files")
    p.add_argument("--limit", type=int, default=None, help="Max pages to fetch")
    p.add_argument("--interval", type=float, default=0.2, help="Delay between requests (s)")
    p.add_argument("--no-nav", action="store_true", help="Skip nav structure extraction")
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
            md = page_to_markdown(url)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(md, encoding="utf-8")
        except Exception as e:
            print(f"[ERROR] {url}: {e}", file=sys.stderr)
            failures += 1

        time.sleep(args.interval)

    print(f"[fetch] Done. Failures: {failures}", flush=True)

    if not args.no_nav:
        extract_nav(base_url, base_path, section)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
