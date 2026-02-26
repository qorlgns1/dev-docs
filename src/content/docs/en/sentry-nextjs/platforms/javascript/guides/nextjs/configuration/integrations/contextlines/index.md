---
title: 'ContextLines | Sentry for Next.js'
description: "This integration adds source code from inline JavaScript of the current page's HTML (e.g. JS in  tags) to stack traces of captured errors. It *can't* ..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines

# ContextLines | Sentry for Next.js

*Import name: `Sentry.contextLinesIntegration`*

This integration adds source code from inline JavaScript of the current page's HTML (e.g. JS in `<script>` tags) to stack traces of captured errors. It *can't* collect source code from assets referenced by your HTML (e.g. `<script src="..." />`).

The `ContextLines` integration is useful when you have inline JS code in HTML pages that can't be accessed by Sentry's backend, for example, due to a login-protected page.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.contextLinesIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md#options)

- [`frameContextLines`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md#framecontextlines)

*Type: `number`*

The number of lines to collect around each stack frame's line number. Defaults to 7.

