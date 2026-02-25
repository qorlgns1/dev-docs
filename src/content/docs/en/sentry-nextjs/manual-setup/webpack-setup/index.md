---
title: 'Webpack Setup | Sentry for Next.js'
description: 'This guide covers the configuration differences for Next.js applications using Webpack (the default bundler before Next.js 15). Complete the main manu...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup

# Webpack Setup | Sentry for Next.js

This guide covers the configuration differences for **Next.js applications using Webpack** (the default bundler before Next.js 15). Complete the [main manual setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md) first, then apply these Webpack-specific configurations.

For a complete reference of all build configuration options, see the [Build Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md) documentation.

If you're using Next.js 15+ with Turbopack (the default), you don't need this guide. See the [main manual setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md) instead.

## [Key Differences: Webpack vs Turbopack](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#key-differences-webpack-vs-turbopack)

| Feature                         | Turbopack                       | Webpack                                              |
| ------------------------------- | ------------------------------- | ---------------------------------------------------- |
| Server function instrumentation | Automatic via Next.js telemetry | Build-time code injection                            |
| Middleware instrumentation      | Automatic via Next.js telemetry | Build-time code injection                            |
| Source map upload               | Post-compile during build       | During build via plugin (default)                    |
| Route exclusion                 | Not supported                   | Supported via `webpack.excludeServerRoutes`          |
| React component annotation      | Not supported                   | Supported via `webpack.reactComponentAnnotation`     |
| Logger tree-shaking             | Not supported                   | Supported via `webpack.treeshake.removeDebugLogging` |

## [Auto-Instrumentation Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#auto-instrumentation-options)

With Webpack, Sentry automatically instruments your server functions, middleware, and app directory components at build time. You can control this behavior:

- [Configure Auto-Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#configure-auto-instrumentation)

These options are enabled by default with Webpack. Disable them if you prefer manual instrumentation or experience build issues.

**Note**: These options instrument Pages Router pages, API routes, and App Router components, but do NOT automatically instrument Server Actions. Server Actions require manual wrapping using `withServerActionInstrumentation()`.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  webpack: {
    // Instrument Pages Router API routes and data fetching methods (default: true)
    autoInstrumentServerFunctions: true,

    // Instrument Next.js middleware (default: true)
    autoInstrumentMiddleware: true,

    // Instrument App Router components (default: true)
    autoInstrumentAppDirectory: true,

    // Tree-shake Sentry logger statements to reduce bundle size
    treeshake: {
      removeDebugLogging: true,
    },
  },
});
```

## [Exclude Routes From Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#exclude-routes-from-instrumentation)

With Webpack, you can exclude specific routes from automatic instrumentation. This is useful for health check endpoints or routes that shouldn't be monitored.

This option has no effect when using Turbopack, as Turbopack relies on Next.js telemetry features instead of build-time instrumentation.

- [Configure Route Exclusions](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#configure-route-exclusions)

Specify routes as URL paths (not file system paths). Routes must have a leading slash and no trailing slash.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  webpack: {
    excludeServerRoutes: [
      "/api/health",
      "/api/excluded/[parameter]",
      /^\/internal\//, // Regex for all /internal/* routes
    ],
  },
});
```

## [Source Map Upload](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#source-map-upload)

By default, Webpack uploads source maps **during the build process** using the Sentry Webpack Plugin. This happens separately for each build (client, server, edge), which can increase build time.

For faster builds, you can use the post-build upload mode (available in Next.js 15.4.1+), which uploads all source maps in a single operation after all builds complete.

- [Default: Upload During Build](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#default-upload-during-build)

The Sentry Webpack Plugin runs during each webpack compilation and uploads source maps as they're generated.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",
  authToken: process.env.SENTRY_AUTH_TOKEN,
});
```

- [Option: Upload After Build (Next.js 15.4.1+)](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#option-upload-after-build-nextjs-1541)

Enable post-build upload for faster builds. All source maps are uploaded once after all webpack builds complete.

This option requires Next.js 15.4.1 or later. Turbopack always uses this mode.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",
  authToken: process.env.SENTRY_AUTH_TOKEN,

  // Upload after all builds complete (faster)
  useRunAfterProductionCompileHook: true,
});
```

- [Advanced Webpack Plugin Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#advanced-webpack-plugin-options)

Pass options directly to the underlying Sentry Webpack Plugin for advanced configuration.

The `unstable_sentryWebpackPluginOptions` API may change in future releases.

These options only apply when `useRunAfterProductionCompileHook` is `false` (the default).

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",
  authToken: process.env.SENTRY_AUTH_TOKEN,

  webpack: {
    // Advanced Webpack plugin options
    unstable_sentryWebpackPluginOptions: {
      sourcemaps: {
        assets: ["./build/**/*.js", "./build/**/*.map"],
        ignore: ["node_modules/**"],
      },
    },
  },
});
```

## [Server Actions with Webpack](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#server-actions-with-webpack)

Server Actions (functions marked with `"use server"`) are **not automatically instrumented** by Webpack's build-time instrumentation. You must manually wrap them for error and performance monitoring.

- [Manual Server Action Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#manual-server-action-instrumentation)

Wrap Server Actions with `withServerActionInstrumentation()` to capture errors and performance data.

`app/actions.ts`

```typescript
"use server";
import * as Sentry from "@sentry/nextjs";

export async function submitForm(formData: FormData) {
  return Sentry.withServerActionInstrumentation(
    "submitForm", // Action name for Sentry
    {
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

## [React Component Annotation](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#react-component-annotation)

With Webpack, you can enable React component name tracking. This annotates React components with `data-sentry-*` attributes that allow Sentry to identify which components users interacted with in [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md) and [breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md).

This feature is only available with Webpack. Turbopack does not support React component annotation.

- [Enable Component Annotation](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#enable-component-annotation)

Enable `reactComponentAnnotation` to track component names in your application. This is especially useful for debugging user interactions in Session Replay.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  webpack: {
    reactComponentAnnotation: {
      enabled: true,
    },
  },
});
```

- [Exclude Specific Components](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#exclude-specific-components)

If you have components you don't want annotated (for privacy or performance reasons), you can exclude them by name.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  webpack: {
    reactComponentAnnotation: {
      enabled: true,
      ignoredComponents: ["SensitiveForm", "InternalDebugPanel"],
    },
  },
});
```

## [Tunneling with Webpack](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#tunneling-with-webpack)

Tunneling works identically for both Webpack and Turbopack. Sentry automatically filters tunnel requests from middleware spans to prevent noise in your monitoring data.

- [Configure Tunnel Route](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#configure-tunnel-route)

Enable tunneling to bypass ad-blockers. Use a fixed route so you can exclude it from middleware if needed.

Using random tunnel routes

You can use `tunnelRoute: true` to auto-generate a random route. However, random routes cannot be excluded from middleware matchers since the route changes on each build. This may cause issues if you have middleware that intercepts all requests.

```typescript
tunnelRoute: true, // Auto-generated random route
```

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  // Use a fixed route (recommended)
  tunnelRoute: "/monitoring",
});
```

## [Migrating from Webpack to Turbopack](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#migrating-from-webpack-to-turbopack)

If you're upgrading to Turbopack:

1. **Remove webpack-only options** - `excludeServerRoutes` and `unstable_sentryWebpackPluginOptions` have no effect with Turbopack
2. **Understand source map changes** - Turbopack always uses post-build upload (no plugin-based upload option)
3. **Test auto-instrumentation** - Turbopack uses Next.js telemetry instead of build-time injection; verify your monitoring still works

`next.config.ts`

```typescript
// Before (Webpack)
export default withSentryConfig(nextConfig, {
  excludeServerRoutes: ["/api/health"],
  tunnelRoute: "/monitoring",
});

// After (Turbopack)
export default withSentryConfig(nextConfig, {
  // excludeServerRoutes is not supported with Turbopack
  tunnelRoute: "/monitoring",
});
```

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#next-steps)

* [Logs Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations) - Connect popular logging libraries like Pino, Winston, and Bunyan
* [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md) - Trace requests across services and microservices
* [AI Agent Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md) - Monitor AI agents built with Vercel AI SDK, LangChain, and more
* [Connect GitHub + Seer](https://docs.sentry.io/organization/integrations/source-code-mgmt/github.md#installing-github) - Enable AI-powered [root cause analysis](https://docs.sentry.io/product/ai-in-sentry/seer.md)
* [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration.md) - Explore extended SDK configuration

