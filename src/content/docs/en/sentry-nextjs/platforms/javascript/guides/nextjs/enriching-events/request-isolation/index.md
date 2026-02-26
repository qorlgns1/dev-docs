---
title: 'Request Isolation | Sentry for Next.js'
description: 'In server-side environments, the isolation scope automatically forks around request boundaries. This is done automatically by the SDK. As a result, ea...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/request-isolation

# Request Isolation | Sentry for Next.js

In server-side environments, the [isolation scope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md) automatically forks around request boundaries. This is done automatically by the SDK. As a result, each request has its own isolation scope, and data set on the isolation scope only applies to events captured during that request.

However, there are also other times when you may want to have isolation, for example, in background jobs or when you want to isolate a specific part of your code. In these cases, you can use `Sentry.withIsolationScope()` to create a new isolation scope that's valid inside of the callback you pass to it. Learn more about using [withIsolationScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#using-withisolationscope).

The following example shows how you can use `withIsolationScope` to attach data to a specific job run:

```javascript
async function job(jobId) {
  return Sentry.withIsolationScope(async () => {
    // Only valid for events in this callback
    Sentry.setTag("jobId", jobId);
    await doSomething();
  });
}
```

