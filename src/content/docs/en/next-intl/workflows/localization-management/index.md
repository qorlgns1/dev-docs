---
title: 'Localization management with Crowdin'
description: 'Prefer to use a fully AI-driven workflow?'
---

Source URL: https://next-intl.dev/docs/workflows/localization-management

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Workflows & integrations](https://next-intl.dev/docs/workflows "Workflows & integrations")Localization management with Crowdin

# Localization management with Crowdin

Prefer to use a fully AI-driven workflow?

[AI translations with Crowdin](https://learn.next-intl.dev/chapters/10-continuous-localization/01-local-workflow)

Once you’ve set up your app with `next-intl`, you’ll have multiple translation bundles that contain your messages (e.g. `en.json`). To streamline the workflow of managing these and to allow other team members to contribute translations, it’s a good idea to use a localization management platform.

While `next-intl` works with all localization management platforms that support translating JSON files, `next-intl` recommends [Crowdin](https://crowdin.com) for managing your translations.

## Collaborate with translators[](https://next-intl.dev/docs/workflows/localization-management#collaborate-with-translators)

The Crowdin Editor provides an easy-to-use environment for translating messages. Apart from guiding translators through your messages, the workflow is improved with advanced features like machine translation suggestions, glossaries and contextual screenshots.

[![Crowdin Editor](https://next-intl.dev/_next/image?url=%2Fcrowdin-editor-schematic.png&w=1920&q=75)](https://crowdin.com/page/freelance-translators)

The Crowdin Editor enables translators to work with JSON files from `next-intl` (illustration).

## Decouple localization from development[](https://next-intl.dev/docs/workflows/localization-management#decouple-localization-from-development)

As a developer-focused localization service, Crowdin helps you to decouple the localization process from development and integrates with your existing workflows.

**Integration options:**

  1. Command-line integration with the [Crowdin CLI](https://developer.crowdin.com/cli-tool/)
  2. Git integration e.g. via the [GitHub app](https://support.crowdin.com/github-integration/)
  3. Automatic workflows triggered from [webhooks](https://developer.crowdin.com/api/v2/#tag/Webhooks)
  4. Over-the-air delivery via the [JS SDK](https://developer.crowdin.com/sdk-ota-web/)
  5. Manual up- and download of messages

[![Crowdin workflow](https://next-intl.dev/_next/image?url=%2Fcrowdin-workflow.png&w=1920&q=75)](https://crowdin.com/teams/engineering)

The [Crowdin GitHub integration](https://support.crowdin.com/github-integration/) automatically creates pull requests when translations are updated.

## Example workflow with the GitHub integration[](https://next-intl.dev/docs/workflows/localization-management#example-workflow-with-the-github-integration)

For this example, we’re going to use an example that is publicly available on GitHub: [Street Photography Viewer](https://github.com/amannn/street-photography-viewer). It’s a Next.js app that displays street photography pictures from Unsplash and uses `next-intl` for all internationalization needs.

Once you have a GitHub repository with your app, you can follow these steps:

  1. Install [the GitHub app from the Crowdin store](https://store.crowdin.com/github)
  2. Follow [the setup guide for the GitHub integration](https://support.crowdin.com/github-integration/)

After this procedure, Crowdin will commit a configuration file to your repository based on your settings.

crowdin.yml
```
    files:
      - source: /messages/en.json
        translation: /messages/%locale%.json
```

This file provides the local translations in your repository to Crowdin.

![Crowdin repository mapping](https://next-intl.dev/_next/image?url=%2Fcrowdin-repo-mapping.png&w=1920&q=75)

With the configuration file in place, Crowdin knows about the translation files in your repository.

Now, as soon as a translation gets updated in Crowdin, the next sync will create a pull request in your repository with the updates.

![Crowdin repository sync](https://next-intl.dev/_next/image?url=%2Fcrowdin-repo-sync.png&w=1920&q=75)

Automatic translation sync from Crowdin ([example pull request](https://github.com/amannn/street-photography-viewer/pull/3))

→ Head over to [Crowdin](https://support.crowdin.com/introduction/) to learn more.

