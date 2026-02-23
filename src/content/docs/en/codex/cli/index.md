---
title: 'Codex CLI'
description: "Codex CLI is OpenAI's coding agent that you can run locally from your terminal. It can read, change, and run code on your machine in the selected dire..."
---

Source URL: https://developers.openai.com/codex/cli

# Codex CLI

Codex CLI is OpenAI's coding agent that you can run locally from your terminal. It can read, change, and run code on your machine in the selected directory.
It's [open source](https://github.com/openai/codex) and built in Rust for speed and efficiency.

Codex is included with ChatGPT Plus, Pro, Business, Edu, and Enterprise plans. Learn more about [what's included](https://developers.openai.com/codex/pricing).

- [Codex CLI overview](https://www.youtube.com/watch?v=iqNzfK4_meQ)

## CLI setup

The Codex CLI is available on macOS and Linux. Windows support is
  experimental. For the best Windows experience, use Codex in a WSL workspace
  and follow our <a href="/codex/windows">Windows setup guide</a>.

---

## Work with the Codex CLI

- [Run Codex interactively](https://developers.openai.com/codex/cli/features#running-in-interactive-mode)

Run `codex` to start an interactive terminal UI (TUI) session.

- [Control model and reasoning](https://developers.openai.com/codex/cli/features#models-reasoning)

Use `/model` to switch between GPT-5.3-Codex and other available models, or adjust reasoning levels.

- [Image inputs](https://developers.openai.com/codex/cli/features#image-inputs)

Attach screenshots or design specs so Codex reads them alongside your prompt.

- [Run local code review](https://developers.openai.com/codex/cli/features#running-local-code-review)

Get your code reviewed by a separate Codex agent before you commit or push your changes.

- [Use multi-agent](https://developers.openai.com/codex/multi-agent)

Enable experimental multi-agent collaboration and parallelize complex tasks.

- [Web search](https://developers.openai.com/codex/cli/features#web-search)

Use Codex to search the web and get up-to-date information for your task.

- [Codex Cloud tasks](https://developers.openai.com/codex/cli/features#working-with-codex-cloud)

Launch a Codex Cloud task, choose environments, and apply the resulting diffs without leaving your terminal.

- [Scripting Codex](https://developers.openai.com/codex/sdk#using-codex-cli-programmatically)

Automate repeatable workflows by scripting Codex with the `exec` command.

- [Model Context Protocol](https://developers.openai.com/codex/mcp)

Give Codex access to additional third-party tools and context with Model Context Protocol (MCP).

- [Approval modes](https://developers.openai.com/codex/cli/features#approval-modes)

Choose the approval mode that matches your comfort level before Codex edits or runs commands.

