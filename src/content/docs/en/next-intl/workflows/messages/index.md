---
title: 'Validating messages'
description: 'To ensure quality and completeness of your messages, you can use i18n-check.'
---

Source URL: https://next-intl.dev/docs/workflows/messages

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Workflows & integrations](https://next-intl.dev/docs/workflows "Workflows & integrations")Validating messages

# Validating messages

To ensure quality and completeness of your messages, you can use [i18n-check](https://github.com/lingualdev/i18n-check).

This CLI helps you validate against issues like:

  1. Missing translations in target locales
  2. Inconsistent usage of ICU arguments across translations

**Usage:**
```
    npx @lingual/i18n-check@latest --source en --locales messages
```

**Output:**
```
    Found missing keys!
    ┌────────────────────┬───────────────────────────────┐
    │ file               │ key                           │
    ├────────────────────┼───────────────────────────────┤
    │  messages/de.json  │  NewsArticle.title            │
    └────────────────────┴───────────────────────────────┘
```

💡

You can also use the [`--unused`](https://github.com/lingualdev/i18n-check#--unused--u) flag to detect keys that are defined in your messages, but are not referenced anywhere in your codebase (currently experimental).

