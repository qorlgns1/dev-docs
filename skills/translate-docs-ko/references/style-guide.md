# Korean Translation Style Guide

## Goals

- Keep technical accuracy first.
- Preserve markdown fidelity: headings, links, tables, and code blocks.
- Optimize for Korean readability without dropping technical nuance.

## Terminology Rules

- Keep product and API names in English:
  - OpenAI, Codex, ChatGPT, Agents SDK, MCP
- Keep code artifacts unchanged:
  - File paths, CLI flags, env vars, endpoint paths, model IDs
- Translate descriptive nouns when natural:
  - workflow -> 워크플로
  - troubleshooting -> 문제 해결
  - permissions -> 권한

## Formatting Rules

- Never alter URL targets inside markdown links.
- Keep fenced code blocks and inline code text unchanged.
- Keep list nesting and numbering semantics unchanged.
- Preserve heading hierarchy (`#`, `##`, `###`).

## Tone

- Use concise technical Korean.
- Avoid colloquial or promotional tone.
- Prefer direct imperative phrasing in procedural sections.
