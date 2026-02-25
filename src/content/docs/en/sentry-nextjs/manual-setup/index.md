---
title: 'Manual Setup | Sentry for Next.js'
description: 'For the fastest setup, we recommend using the wizard installer.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup

# Manual Setup | Sentry for Next.js

For the fastest setup, we recommend using the [wizard installer](https://docs.sentry.io/platforms/javascript/guides/nextjs.md).

This guide covers manual setup for **Next.js 15+ with Turbopack and App Router**. For other setups, see:

* [Pages Router Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md) - For applications using the Pages Router
* [Webpack Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md) - For applications not using Turbopack

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#prerequisites)

You need:

* A Next.js application
* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)

Choose the features you want to configure:

Error Monitoring\[x]Logs\[ ]Session Replay\[x]Tracing\[ ]User Feedback

**How this guide works:**

1. **Install** - Add the Sentry SDK to your project
2. **Configure** - Set up SDK initialization files and Next.js configuration
3. **Verify** - Test error monitoring and any additional features you enabled

## [Install](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#install)

- [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add the Sentry SDK to your application.

```bash
npm install @sentry/nextjs --save
```

## [Configure](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#configure)

- [Apply Instrumentation to Your App](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#apply-instrumentation-to-your-app)

Extend your app's default Next.js options by adding `withSentryConfig` into your `next.config.ts` file.

`next.config.ts`

```typescript
import type { NextConfig } from "next";
import { withSentryConfig } from "@sentry/nextjs";

const nextConfig: NextConfig = {
  // Your existing Next.js configuration
};

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",

  // Only print logs for uploading source maps in CI
  silent: !process.env.CI,
});
```

- [Initialize Sentry SDKs](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#initialize-sentry-sdks)

Create the following files in your application's root directory (or `src` folder if you have one):

* `instrumentation-client.ts` - Client-side SDK initialization
* `sentry.server.config.ts` - Server-side SDK initialization
* `sentry.edge.config.ts` - Edge runtime SDK initialization

##### Tip

Include your DSN directly in these files, or use a *public* environment variable like `NEXT_PUBLIC_SENTRY_DSN`.

`instrumentation-client.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance

  // Capture 100% in dev, 10% in production
  // Adjust based on your traffic volume
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
  integrations: [
    // ___PRODUCT_OPTION_START___ session-replay
    Sentry.replayIntegration(),
    // ___PRODUCT_OPTION_END___ session-replay
    // ___PRODUCT_OPTION_START___ user-feedback
    Sentry.feedbackIntegration({
      colorScheme: "system",
    }),
    // ___PRODUCT_OPTION_END___ user-feedback
  ],
  // ___PRODUCT_OPTION_START___ session-replay

  // Capture Replay for 10% of all sessions,
  // plus for 100% of sessions with an error
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ session-replay
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});

// ___PRODUCT_OPTION_START___ performance
// This export will instrument router navigations
export const onRouterTransitionStart = Sentry.captureRouterTransitionStart;
// ___PRODUCT_OPTION_END___ performance
```

##### Adjust sample rates for production

The example above samples 100% of traces in development and 10% in production. Monitor your [usage stats](https://sentry.io/orgredirect/organizations/:orgslug/settings/stats/?dataCategory=spans) and adjust `tracesSampleRate` based on your traffic volume. Learn more about [sampling configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/sampling.md).

- [Register Server-Side SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#register-server-side-sdk)

Create a [Next.js Instrumentation file](https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation) named `instrumentation.ts` in your project root (or `src` folder). This file imports your server and edge configurations and exports `onRequestError` to capture server-side errors.

The `onRequestError` hook requires `@sentry/nextjs` version `8.28.0` or higher and Next.js 15.

`instrumentation.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await import("./sentry.server.config");
  }

  if (process.env.NEXT_RUNTIME === "edge") {
    await import("./sentry.edge.config");
  }
}

// Capture errors from Server Components, middleware, and proxies
export const onRequestError = Sentry.captureRequestError;
```

- [Capture React Render Errors](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#capture-react-render-errors)

Create `app/global-error.tsx` to capture errors that occur anywhere in your App Router application.

`global-error.tsx`

```tsx
"use client";

import * as Sentry from "@sentry/nextjs";
import NextError from "next/error";
import { useEffect } from "react";

export default function GlobalError({
  error,
}: {
  error: Error & { digest?: string };
}) {
  useEffect(() => {
    Sentry.captureException(error);
  }, [error]);

  return (
    <html>
      <body>
        {/* `NextError` is the default Next.js error page component. Its type
        definition requires a `statusCode` prop. However, since the App Router
        does not expose status codes for errors, we simply pass 0 to render a
        generic error message. */}
        <NextError statusCode={0} />
      </body>
    </html>
  );
}
```

- [Server Actions](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#server-actions)

Wrap your Server Actions with `Sentry.withServerActionInstrumentation()`.

`app/actions.ts`

```typescript
"use server";
import * as Sentry from "@sentry/nextjs";
import { headers } from "next/headers";

export async function submitForm(formData: FormData) {
  return Sentry.withServerActionInstrumentation(
    "submitForm", // Action name for Sentry
    {
      headers: await headers(), // Connect client and server traces
      formData, // Attach form data to events
      recordResponse: true, // Include response data
    },
    async () => {
      // Your server action logic
      const result = await processForm(formData);
      return { success: true, data: result };
    },
  );
}
```

- [Source Maps (Optional)](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#source-maps-optional)

Add the `authToken` option to your `next.config.ts` to enable readable stack traces. Set the `SENTRY_AUTH_TOKEN` environment variable in your CI/CD.

##### Important

Keep your auth token secret and out of version control.

`next.config.ts`

```typescript
export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",

  // Pass the auth token
  authToken: process.env.SENTRY_AUTH_TOKEN,

  // Upload a larger set of source maps for prettier stack traces
  widenClientFileUpload: true,
});
```

- [Tunneling (Optional)](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#tunneling-optional)

Prevent ad blockers from blocking Sentry events by routing them through your Next.js server.

This increases server load. Consider the trade-off for your application.

Using Next.js middleware with tunneling

If you're using Next.js middleware (`middleware.ts`) that intercepts requests, exclude the tunnel route:

`middleware.ts`

```typescript
export const config = {
  matcher: ["/((?!monitoring|_next/static|_next/image|favicon.ico).*)"],
};
```

`next.config.ts`

```typescript
export default withSentryConfig(nextConfig, {
  // Use a fixed route (recommended)
  tunnelRoute: "/monitoring",
});
```

## [Error Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#error-monitoring)

Test your error monitoring setup by throwing an error and viewing it in Sentry.

- [Throw a Test Error](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#throw-a-test-error)

Add this button to any page and click it to trigger a test error.

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

```jsx
<button
  type="button"
  onClick={() => {
    throw new Error("Sentry Test Error");
  }}
>
  Break the world
</button>;
```

- [Verify](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#verify)

Open [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) in Sentry to see your test error. [Learn more about capturing errors](https://docs.sentry.io/platforms/javascript/guides/nextjs/usage.md).

## [Verify Additional Features](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#verify-additional-features)

Based on the features you selected above, verify each one is working correctly.

- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#session-replay)

Session Replay captures video-like reproductions of user sessions. It's configured with `replayIntegration()` in your client config.

By default, Sentry masks all text, inputs, and media. You can customize this in [Privacy Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md).

**Verify:** Trigger an error or navigate your app, then check [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) in Sentry.

`instrumentation-client.ts`

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.replayIntegration({
      maskAllText: true,
      maskAllInputs: true,
      blockAllMedia: true,
    }),
  ],

  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

- [Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#tracing)

Tracing is configured with `tracesSampleRate` in your SDK init files. Next.js routes and API calls are automatically instrumented.

Add [custom spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/custom-instrumentation.md) to trace specific operations in your code.

**Verify:** Navigate to any page, then check [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) in Sentry.

```typescript
import * as Sentry from "@sentry/nextjs";

// Wrap operations with spans
const result = await Sentry.startSpan(
  { name: "expensive-operation", op: "function" },
  async () => {
    return await fetchDataFromAPI();
  },
);
```

- [Logs NEW](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#logs-)

Logs are enabled with `enableLogs: true` in your SDK config. Use the Sentry logger to send structured logs from anywhere in your application.

Connect popular logging libraries via [Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations).

**Verify:** Add a log statement, trigger it, then check [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) in Sentry.

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.logger.info("User clicked checkout button");

Sentry.logger.info("Order completed", {
  orderId: "12345",
  total: 99.99,
});

Sentry.logger.warn("Warning message");
Sentry.logger.error("Error occurred");
```

- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#user-feedback)

User Feedback adds an embeddable widget via `feedbackIntegration()` that lets users report bugs directly from your app.

**Verify:** Look for the feedback button (bottom-right corner), submit test feedback, then check [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) in Sentry.

[Learn more about User Feedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md)

`instrumentation-client.ts`

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.feedbackIntegration({
      colorScheme: "system",
    }),
  ],
});
```

## Hybrid Apps (App Router + Pages Router)

If your application uses both the App Router and Pages Router:

1. Follow this guide for App Router components
2. Add a `pages/_error.tsx` file for Pages Router error handling (see [Pages Router Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md))
3. Both routers share the same Sentry configuration files

The Sentry SDK automatically detects which router is being used and applies the appropriate instrumentation.

## Next Steps

You've successfully integrated Sentry into your Next.js application! Here's what to explore next:

* [Logs Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations) - Connect popular logging libraries like Pino, Winston, and Bunyan
* [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md) - Trace requests across services and microservices
* [AI Agent Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md) - Monitor AI agents built with Vercel AI SDK, LangChain, and more
* [Connect GitHub + Seer](https://docs.sentry.io/organization/integrations/source-code-mgmt/github.md#installing-github) - Enable AI-powered [root cause analysis](https://docs.sentry.io/product/ai-in-sentry/seer.md) by connecting your GitHub repository
* [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration.md) - Explore extended SDK configuration options

Are you having problems setting up the SDK?

* Try the [installation wizard](https://docs.sentry.io/platforms/javascript/guides/nextjs.md) for automatic setup
* [Get support](https://sentry.zendesk.com/hc/en-us/)

## Pages in this section

- [Pages Router Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md)
- [Webpack Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md)

