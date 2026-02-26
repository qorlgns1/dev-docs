---
title: 'Tree Shaking | Sentry for Next.js'
description: 'The Sentry Next.js SDK supports tree shaking for webpack builds with some additional configurations.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking

# Tree Shaking | Sentry for Next.js

The Sentry Next.js SDK supports [tree shaking](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking) for webpack builds with some additional configurations.

If you want to minimize the bundle size of the Sentry SDK, we recommend reading through this page and applying the tree-shaking configurations shown.

This guide is only relevant if you're using webpack to build your Next.js application. Tree-shaking options are not supported for Turbopack builds at the moment.

## [Tree-Shaking Optional Code](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#tree-shaking-optional-code)

The Sentry Next.js SDK includes code that isn't strictly required for basic error collection, such as debug logging and tracing functionality. While debug code is useful during development, it adds unnecessary weight to your production bundles. The Next.js SDK provides tree shaking options through the `withSentryConfig` function, allowing you to remove this optional code during the webpack build process.

Anything you don't import or use can be tree shaken by webpack. This means that optional integrations like Session Replay, Browser Tracing, Browser Profiling, and any unused utility methods won't be included in your bundle unless you import and use them. The rest of this page covers ways to tree shake internal SDK code, which you only need if you're using certain Sentry features.

## [Tree-Shaking Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#tree-shaking-options)

To tree shake Sentry debug code in Next.js projects, use `webpack.treeshake` options in your build configuration, like in this example:

`next.config.(js|mjs)`

```javascript
const nextConfig = {
  // your next.js config
};

withSentryConfig(nextConfig, {
  webpack: {
    treeshake: {
      // Tree shaking options...
      removeDebugLogging: false,
      removeTracing: false,
      excludeReplayIframe: false,
      excludeReplayShadowDOM: false,
      excludeReplayCompressionWorker: false,
    },
  },
});
```

For more information on custom webpack configurations in Next.js, see [Custom Webpack Config](https://nextjs.org/docs/api-reference/next.config.js/custom-webpack-config) in the Next.js docs.

The following sections cover each available tree-shaking option and how to configure them.

- [webpack.treeshake.removeDebugLogging](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.removeDebugLogging)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Setting this option to true will remove all Sentry SDK debug logging code (the console logs that appear when you set `debug: true` in your SDK configuration). This doesn't affect Sentry's Logs product (controlled by the `enableLogs` option) or your app's logging.

- [webpack.treeshake.removeTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.removeTracing)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Setting this option to `true` will remove all code related to tracing and performance monitoring.

You should not use any tracing-related SDK features (for example, `Sentry.startSpan()`) when this option is enabled. Also, this option has no effect if you did not add `browserTracingIntegration`.

- [webpack.treeshake.excludeReplayIframe](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.excludeReplayIframe)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Setting this option to `true` will remove any SDK code related to capturing iframe content during [Session Replays](https://docs.sentry.io/platforms/javascript/session-replay.md). This only applies when you've enabled `replayIntegration`.

- [webpack.treeshake.excludeReplayShadowDOM](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.excludeReplayShadowDOM)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Setting this option to `true` will remove any SDK code related to capturing shadow DOM elements during [Session Replays](https://docs.sentry.io/platforms/javascript/session-replay.md). This only applies when you've enabled `replayIntegration`.

- [webpack.treeshake.excludeReplayCompressionWorker](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.excludeReplayCompressionWorker)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Setting this option to `true` will remove any SDK code related to the included compression web worker for [Session Replay](https://docs.sentry.io/platforms/javascript/session-replay.md). Enable this option if you want to host a compression worker yourself. See [Using a Custom Compression Worker](https://docs.sentry.io/platforms/javascript/session-replay/configuration.md#using-a-custom-compression-worker) for details. This only applies when you've enabled `replayIntegration`.

**We don't recommend enabling this option unless you provide a custom worker URL**.

If you want to learn more about the available tree-shaking options and how to set them manually with different bundlers, see the [tree shaking documentation](https://docs.sentry.io/platforms/javascript/guides/react/configuration/tree-shaking.md#tree-shaking-with-webpack) for the JavaScript SDK.

