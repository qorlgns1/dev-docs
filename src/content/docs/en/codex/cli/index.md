---
title: Codex CLI
description: Codex CLI is OpenAI’s coding agent that you can run locally from your terminal. It can read, change, and run code on your machine in the selected dire...
sidebar:
  order: 22
---

# Codex CLI

Source URL: https://developers.openai.com/codex/cli

Codex CLI is OpenAI’s coding agent that you can run locally from your terminal. It can read, change, and run code on your machine in the selected directory. It’s [open source](https://github.com/openai/codex) and built in Rust for speed and efficiency.

Codex is included with ChatGPT Plus, Pro, Business, Edu, and Enterprise plans. Learn more about [what’s included](https://developers.openai.com/codex/pricing).

  


## CLI setup

Choose your package manager

npmHomebrew

  1. 1

### Install

Install the Codex CLI with npm.

npm install command

npm i -g @openai/codexCopy

  2. 2

### Run

Run Codex in a terminal. It can inspect your repository, edit files, and run commands.

Run Codex command

codexCopy

The first time you run Codex, you'll be prompted to sign in. Authenticate with your ChatGPT account or an API key.

See the [pricing page](https://developers.openai.com/codex/pricing) if you're not sure which plans include Codex access.

  3. 3

### Upgrade

New versions of the Codex CLI are released regularly. See the [changelog](https://developers.openai.com/codex/changelog) for release notes. To upgrade with npm, run:

npm upgrade command

npm i -g @openai/codex@latestCopy




The Codex CLI is available on macOS and Linux. Windows support is experimental. For the best Windows experience, use Codex in a WSL workspace and follow our [Windows setup guide](https://developers.openai.com/codex/windows).

* * *

## Work with the Codex CLI

### [Run Codex interactivelyRun `codex` to start an interactive terminal UI (TUI) session.](https://developers.openai.com/codex/cli/features#running-in-interactive-mode)### [Control model and reasoningUse `/model` to switch between GPT-5.3-Codex and other available models, or adjust reasoning levels.](https://developers.openai.com/codex/cli/features#models-reasoning)### [Image inputsAttach screenshots or design specs so Codex reads them alongside your prompt.](https://developers.openai.com/codex/cli/features#image-inputs)### [Run local code reviewGet your code reviewed by a separate Codex agent before you commit or push your changes.](https://developers.openai.com/codex/cli/features#running-local-code-review)### [Use multi-agentEnable experimental multi-agent collaboration and parallelize complex tasks.](https://developers.openai.com/codex/multi-agent)### [Web searchUse Codex to search the web and get up-to-date information for your task.](https://developers.openai.com/codex/cli/features#web-search)### [Codex Cloud tasksLaunch a Codex Cloud task, choose environments, and apply the resulting diffs without leaving your terminal.](https://developers.openai.com/codex/cli/features#working-with-codex-cloud)### [Scripting CodexAutomate repeatable workflows by scripting Codex with the `exec` command.](https://developers.openai.com/codex/sdk#using-codex-cli-programmatically)### [Model Context ProtocolGive Codex access to additional third-party tools and context with Model Context Protocol (MCP).](https://developers.openai.com/codex/mcp)### [Approval modesChoose the approval mode that matches your comfort level before Codex edits or runs commands.](https://developers.openai.com/codex/cli/features#approval-modes)
