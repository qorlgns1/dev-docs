---
title: 'Event Level | Sentry for Next.js'
description: 'The level - similar to logging levels - is generally added by default by the SDK. You can either provide a dedicated level directly in , or configure ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/level

# Event Level | Sentry for Next.js

The level - similar to logging levels - is generally added by default by the SDK. You can either provide a dedicated level directly in `captureMessage`, or configure a level on the scope in order to apply it to all events.

To set the level out of scope, you can call `captureMessage()` per event:

```javascript
Sentry.captureMessage("this is a debug message", "debug");
```

Available levels are `"fatal"`, `"error"`, `"warning"`, `"log"`, `"info"`, and `"debug"`.

To set the level within scope, you can call `setLevel()`:

```javascript
Sentry.getCurrentScope().setLevel("warning");
```

or per event:

```javascript
Sentry.withScope(function (scope) {
  scope.setLevel("info");

  // The exception has the event level set by the scope (info).
  Sentry.captureException(new Error("custom error"));
});

// Outside of withScope, the Event level will have their previous value restored.
// The exception has the event level set (error).
Sentry.captureException(new Error("custom error 2"));
```

