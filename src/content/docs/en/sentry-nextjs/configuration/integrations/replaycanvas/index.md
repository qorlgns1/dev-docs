---
title: 'ReplayCanvas | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replaycanvas

# ReplayCanvas | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.replayCanvasIntegration`*

The Replay Canvas integration can be used to capture [Session Replays](https://docs.sentry.io/product/session-replay.md) from HTML canvas elements. It requires the Replay integration to be enabled.

There is currently no PII scrubbing in canvas recordings!

Read more about [setting up Session Replay with the Canvas integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#canvas-recording).

```JavaScript
Sentry.init({
  integrations: [Sentry.replayCanvasIntegration()],
});
```

