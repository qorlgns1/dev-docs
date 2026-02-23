---
name: translate-docs-ko
description: Translate technical documentation into Korean Markdown while preserving structure, links, and code blocks. Use when asked to localize docs from a URL, a URL list, a sitemap subtree (for example `/codex/*`), or existing Markdown/HTML documentation files into publishable Korean docs.
---

# Translate Docs Ko

## Overview

Produce Korean translations for documentation with deterministic file outputs.
Use the bundled script for full-site sections and repeatable localization tasks.

## Workflow

1. Define source scope.
- Prefer `--base-url` + sitemap filtering for docs sites.
- Use `--urls-file` for mixed sources or curated lists.
2. Run the script and write English/Korean Markdown trees.
- Export English Markdown first:
  - `python3 scripts/translate_docs.py --base-url {base_url} --output-dir {output_dir} --no-translate`
- Translate Markdown tree with Codex CLI (no API key):
  - `python3 scripts/translate_markdown_tree_codex.py --source-root {source_root} --dest-root {dest_root} --style natural`
3. Review quality and terminology.
- Load `references/style-guide.md` and apply wording consistency.
- Check headings, lists, tables, links, and fenced code blocks for formatting regressions.
4. Iterate with focused reruns.
- Use `--limit` for quick validation.
- Use `--force` for full regeneration after prompt or model changes.

## Commands

```bash
# Export /codex/* from sitemap (English source tree)
python3 scripts/translate_docs.py \
  --base-url {base_url} \
  --output-dir {output_dir} \
  --no-translate

# Translate to Korean with Codex CLI and write ko tree
python3 scripts/translate_markdown_tree_codex.py \
  --source-root {source_root} \
  --dest-root {dest_root} \
  --style natural
```

## Guardrails

- Preserve Markdown structure exactly where possible.
- Keep code snippets, command flags, API paths, and URLs unchanged.
- Keep product names and proper nouns in original form unless Korean usage is established.
- Save per-page outputs in deterministic paths to make diffs reviewable.
- Prefer Codex CLI translation workflow when API keys are unavailable.
