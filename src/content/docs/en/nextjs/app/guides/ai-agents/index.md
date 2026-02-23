---
title: 'Guides: AI Coding Agents'
description: 'Next.js ships version-matched documentation inside the  package, allowing AI coding agents to reference accurate, up-to-date APIs and patterns. An  fi...'
---

# Guides: AI Coding Agents | Next.js

Source URL: https://nextjs.org/docs/app/guides/ai-agents

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)AI Coding Agents

Copy page

# How to set up your Next.js project for AI coding agents

Last updated February 20, 2026

Next.js ships version-matched documentation inside the `next` package, allowing AI coding agents to reference accurate, up-to-date APIs and patterns. An `AGENTS.md` file at the root of your project directs agents to these bundled docs instead of their training data.

## How it works[](https://nextjs.org/docs/app/guides/ai-agents#how-it-works)

When you install `next`, the Next.js documentation is bundled at `node_modules/next/dist/docs/`. The bundled docs mirror the structure of the [Next.js documentation site](https://nextjs.org/docs):
[code] 
    node_modules/next/dist/docs/
    ├── 01-app/
    │   ├── 01-getting-started/
    │   ├── 02-guides/
    │   └── 03-api-reference/
    ├── 02-pages/
    ├── 03-architecture/
    └── index.mdx
[/code]

This means agents always have access to docs that match your installed version — no network request or external lookup required.

The `AGENTS.md` file at the root of your project tells agents to read these bundled docs before writing any code. Most AI coding agents — including Claude Code, Cursor, GitHub Copilot, and others — automatically read `AGENTS.md` when they start a session.

## Getting started[](https://nextjs.org/docs/app/guides/ai-agents#getting-started)

### New projects[](https://nextjs.org/docs/app/guides/ai-agents#new-projects)

[`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app) generates `AGENTS.md` and `CLAUDE.md` automatically. No additional setup is needed:

pnpmnpmyarnbun

Terminal
[code]
    pnpm create next-app@canary
[/code]

If you don't want the agent files, pass `--no-agents-md`:
[code] 
    npx create-next-app@canary --no-agents-md
[/code]

### Existing projects[](https://nextjs.org/docs/app/guides/ai-agents#existing-projects)

Ensure you are on Next.js `v16.2.0-canary.37` or later, then add the following files to the root of your project.

`AGENTS.md` contains the instructions that agents will read:

AGENTS.md
[code]
    <!-- BEGIN:nextjs-agent-rules -->
     
    # Next.js: ALWAYS read docs before coding
     
    Before any Next.js work, find and read the relevant doc in `node_modules/next/dist/docs/`. Your training data is outdated — the docs are the source of truth.
     
    <!-- END:nextjs-agent-rules -->
[/code]

`CLAUDE.md` uses the `@` import syntax to include `AGENTS.md`, so [Claude Code](https://docs.anthropic.com/en/docs/claude-code) users get the same instructions without duplicating content:

CLAUDE.md
[code]
    @AGENTS.md
[/code]

## Understanding AGENTS.md[](https://nextjs.org/docs/app/guides/ai-agents#understanding-agentsmd)

The default `AGENTS.md` contains a single, focused instruction: **read the bundled docs before writing code**. This is intentionally minimal — the goal is to redirect agents from stale training data to the accurate, version-matched documentation in `node_modules/next/dist/docs/`.

The `<!-- BEGIN:nextjs-agent-rules -->` and `<!-- END:nextjs-agent-rules -->` comment markers delimit the Next.js-managed section. You can add your own project-specific instructions outside these markers without worrying about them being overwritten by future updates.

The bundled docs include guides, API references, and file conventions for the App Router and Pages Router. When an agent encounters a task involving routing, data fetching, or any other Next.js feature, it can look up the correct API in the bundled docs rather than relying on potentially outdated training data.

> **Good to know:** To see how bundled docs and `AGENTS.md` improve agent performance on real-world Next.js tasks, visit the [benchmark results](https://nextjs.org/evals).

## Next Steps

### [Next.js MCP ServerLearn how to use Next.js MCP support to allow coding agents access to your application state](https://nextjs.org/docs/app/guides/mcp)

Was this helpful?

supported.

Send
