---
title: 'Replay | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replay

# Replay | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.replayIntegration`*

[Session Replay](https://docs.sentry.io/product/explore/session-replay.md) helps you get to the root cause of an error or latency issue faster by providing you with a video-like reproduction of what was happening in the user's browser before, during, and after the issue. You can rewind and replay your application's DOM state and see key user interactions, like mouse clicks, scrolls, network requests, and console entries, in a single combined UI inspired by your browser's DevTools.

Read more about [setting up Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md).

```JavaScript
Sentry.init({
  integrations: [Sentry.replayIntegration()],
});
```

