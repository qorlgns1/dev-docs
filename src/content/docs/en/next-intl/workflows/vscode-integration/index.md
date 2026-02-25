---
title: 'VSCode integration'
description: 'Prefer to watch a video?'
---

Source URL: https://next-intl.dev/docs/workflows/vscode-integration

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Workflows & integrations](https://next-intl.dev/docs/workflows "Workflows & integrations")VSCode integration

# VSCode integration

Prefer to watch a video?

[Editor tools](https://learn.next-intl.dev/chapters/03-translations/05-tooling)

To improve the workflow for managing messages right from your code editor, you can use an extension for VSCode that includes support for `next-intl`.

These extensions are known to support `next-intl`:

  1. [i18n Ally](https://next-intl.dev/docs/workflows/vscode-integration#i18n-ally)
  2. [Loccy](https://next-intl.dev/docs/workflows/vscode-integration#loccy)
  3. [Sherlock](https://next-intl.dev/docs/workflows/vscode-integration#sherlock)

## i18n Ally[](https://next-intl.dev/docs/workflows/vscode-integration#i18n-ally)

**Highlights:**

  * Message extraction
  * Inline annotations
  * Inline message editing
  * Machine translations

**Setup:**

  1. Install [i18n Ally](https://marketplace.visualstudio.com/items?itemName=lokalise.i18n-ally)
  2. Configure the extension in your project via [workspace settings](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings)

.vscode/settings.json
```
    "i18n-ally.localesPaths": ["./path/to/your/messages"], // E.g. "./messages"
    "i18n-ally.keystyle": "nested"
```

Learn more in the [i18n Ally docs](https://github.com/lokalise/i18n-ally/wiki).

## Loccy[](https://next-intl.dev/docs/workflows/vscode-integration#loccy)

**Highlights:**

  * Message extraction
  * Inline annotations
  * Inline message editing
  * AI-enhanced features for message creation, machine translations and more (paid)

**Setup:**

  1. Install [Loccy](https://loccy.dev) and it will auto-detect your i18n setup
  2. For advanced configuration, run `Loccy: Create Config File` from the command palette

Learn more on the [Loccy website](https://loccy.dev).

## Sherlock[](https://next-intl.dev/docs/workflows/vscode-integration#sherlock)

**Highlights:**

  * Message extraction
  * Inline annotations
  * Inline message editing

**Setup:**

  1. Install the [Sherlock VS Code extension](https://marketplace.visualstudio.com/items?itemName=inlang.vs-code-extension)
  2. Configure the extension in your project via `project.inlang/settings.json`:

project.inlang/settings.json
```
    {
      "$schema": "https://inlang.com/schema/project-settings",
      "sourceLanguageTag": "en",
      "languageTags": ["en", "de"],
      "modules": [
        "https://cdn.jsdelivr.net/npm/@inlang/plugin-next-intl@latest/dist/index.js"
      ],
      "plugin.inlang.nextIntl": {
        "pathPattern": "./messages/{languageTag}.json"
      }
    }
```

Learn more in the [inlang docs](https://inlang.com/m/193hsyds/plugin-inlang-nextIntl).

