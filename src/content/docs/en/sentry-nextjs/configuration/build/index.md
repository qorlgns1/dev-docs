---
title: 'Build Options | Sentry for Next.js'
description: "The Sentry Next.js SDK supports automatic code injection and source map upload during your app's build process using the  wrapper in your Next.js conf..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build

# Build Options | Sentry for Next.js

The Sentry Next.js SDK supports automatic code injection and source map upload during your app's build process using the `withSentryConfig` wrapper in your Next.js configuration file (`next.config.js` or `next.config.mjs`). For information on updating the configuration, see the [Manual Setup guide](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#configure).

## [Available Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#available-options)

## [Core Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#core-options)

- [org](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#org)

| Type | `string` |
| ---- | -------- |

The slug of the Sentry organization associated with the app.

- [project](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#project)

| Type | `string` |
| ---- | -------- |

The slug of the Sentry project associated with the app.

- [authToken](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#authToken)

| Type | `string` |
| ---- | -------- |

The authentication token to use for all communication with Sentry. Can be obtained from <https://sentry.io/orgredirect/organizations/:orgslug/settings/auth-tokens/>.

- [sentryUrl](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sentryUrl)

| Type    | `string`             |
| ------- | -------------------- |
| Default | `https://sentry.io/` |

The base URL of your Sentry instance. Use this if you are using a self-hosted or Sentry instance other than sentry.io.

- [headers](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#headers)

| Type | `Record<string, string>` |
| ---- | ------------------------ |

Headers added to every outgoing network request.

- [telemetry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#telemetry)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

If set to true, internal plugin errors and performance data will be sent to Sentry.

At Sentry we like to use Sentry ourselves to deliver faster and more stable products. We're very careful of what we're sending. We won't collect anything other than error and high-level performance data. We will never collect your code or any details of the projects in which you're using this plugin.

- [silent](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#silent)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Suppresses all Sentry SDK build logs.

- [debug](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#debug)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Prints additional debug information about the SDK and uploading source maps when building the application.

- [errorHandler](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#errorHandler)

| Type | `(error: Error) => void` |
| ---- | ------------------------ |

A callback function that will be invoked when errors occur during the Sentry build process. This is particularly useful for gracefully handling CI/CD pipeline failures when there are connectivity issues. You can optionally re-throw the error to fail the build process.

```javascript
withSentryConfig(nextConfig, {
  // ... other options
  errorHandler: (error) => {
    console.warn("Sentry build error occurred:", error);
    // Optionally, you can still fail the build by re-throwing the error
    // throw error;
  },
});
```

## [Source Maps Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#source-maps-options)

- [sourcemaps.disable](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.disable)

| Type | `boolean` |
| ---- | --------- |

Disable any functionality related to source maps.

- [sourcemaps.assets](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.assets)

| Type | `string \| string[]` |
| ---- | -------------------- |

A glob or an array of globs that specifies the build artifacts that should be uploaded to Sentry. If not specified, the plugin will try to upload all JavaScript files and source map files created during build.

The globbing patterns follow the implementation of the `glob` package.

- [sourcemaps.ignore](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.ignore)

| Type    | `string \| string[]` |
| ------- | -------------------- |
| Default | `[]`                 |

A glob or an array of globs that specifies which build artifacts should not be uploaded to Sentry.

- [sourcemaps.deleteSourcemapsAfterUpload](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.deleteSourcemapsAfterUpload)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Toggle whether generated **client-side** source maps within your Next.js build folder will be automatically deleted after being uploaded to Sentry. When enabled, source maps in `.next/static/` are deleted but **server-side source maps** (in `.next/server/`) are intentionally kept because:

* They are required for server-side error reporting at runtime.
* They are not a security concern since they are not publicly accessible to users.

To customize which files are deleted after upload (for example, to include additional paths), use the `sourcemaps.filesToDeleteAfterUpload` option instead.

- [sourcemaps.filesToDeleteAfterUpload](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.filesToDeleteAfterUpload)

| Type | `string \| string[]` |
| ---- | -------------------- |

An array of glob patterns that specifies which source map files will be deleted after being uploaded to Sentry. When set, this overrides the default deletion behavior of `deleteSourcemapsAfterUpload`.

Use this option when you need fine-grained control over which source maps are deleted. Make sure to also enable [hidden source maps](https://webpack.js.org/configuration/devtool/) for any files you plan to delete, otherwise your build output will contain broken `sourceMappingURL` references.

```javascript
withSentryConfig(nextConfig, {
  sourcemaps: {
    filesToDeleteAfterUpload: [".next/static/**/*.map"],
  },
});
```

## [Release Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release-options)

- [release.name](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release.name)

| Type | `string` |
| ---- | -------- |

Unique identifier for the release you want to create. Defaults to automatically detecting a value for your environment.

- [release.create](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release.create)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Whether the plugin should create a release on Sentry during the build.

- [release.finalize](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release.finalize)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Whether the Sentry release should be automatically finalized after the build ends.

- [release.dist](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release.dist)

| Type | `string` |
| ---- | -------- |

Unique identifier for the distribution, used to further segment your release. Usually your build number.

## [Bundle Size Optimizations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#bundle-size-optimizations)

- [bundleSizeOptimizations.excludeDebugStatements](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#bundleSizeOptimizations.excludeDebugStatements)

| Type | `boolean` |
| ---- | --------- |

If set to `true`, the Sentry SDK will attempt to tree-shake any debugging code within itself during the build.

- [bundleSizeOptimizations.excludeTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#bundleSizeOptimizations.excludeTracing)

| Type | `boolean` |
| ---- | --------- |

If set to `true`, the Sentry SDK will attempt to tree-shake code related to tracing and performance monitoring.

**Notice:** Do not enable this when using any performance monitoring-related SDK features.

## [Next.js Specific Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#nextjs-specific-options)

- [widenClientFileUpload](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#widenClientFileUpload)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Include Next.js-internal code and code from dependencies when uploading source maps.

When and why to widen the upload scope.

If you find that there are some frames in your client-side stack traces that aren't getting source-mapped even when most others are, the issue might be that those frames are from files in `static/chunks/` rather than `static/chunks/pages/`. By default, such files aren't uploaded because the majority of the files in `static/chunks/` only contain Next.js or third-party code. To upload all of the files and source maps, including ones from third-party packages, set the `widenClientFileUpload` option to `true`.

Note: Enabling this option can lead to longer build times.

- [tunnelRoute](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#tunnelRoute)

| Type | `string \| boolean` |
| ---- | ------------------- |

This feature requires **Next.js version 11+** and doesn't currently work with self-hosted Sentry instances.

Tunnel Sentry requests through this route on your Next.js server to prevent ad-blockers from blocking Sentry events from being sent.

This option can be set to:

* `true` for auto-generated routes, which are unpredictable and change with each deployment.
* A custom static string path like `/error-monitoring`.

Learn more about tunneling in the [troubleshooting section](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting.md#dealing-with-ad-blockers).

Using Next.js middleware on Turbopack

If you're using Turbopack, client-side event recording will fail if your Next.js middleware intercepts the configured tunnel route. To fix this, set the route to a fixed string (like `/error-monitoring`) and add a negative matcher like `(?!error-monitoring)` in your middleware to exclude the tunnel route. If you're not using Turbopack, Sentry will automatically skip the tunnel route in your middleware.

- [useRunAfterProductionCompileHook](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#useRunAfterProductionCompileHook)

| Type    | `boolean`                         |
| ------- | --------------------------------- |
| Default | `false(webpack)\|true(turbopack)` |

##### Version support

You can use this option with Next.js version 15.4.1 and later.

Enables the use of the [`runAfterProductionCompile` hook from Next.js](https://nextjs.org/docs/architecture/nextjs-compiler#runafterproductioncompile) to upload sourcemaps after the build is completed.

* This option is set to `true` by default for Turbopack as there are no alternative ways to upload sourcemaps here.
* This option is set to `false` for Webpack as the default behavior is to upload sourcemaps during the build process using the [Sentry Webpack Plugin](https://github.com/getsentry/sentry-javascript-bundler-plugins).

**Important:** Enabling this option will mutate your Next.js build output by injecting [Debug IDs](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md) via the Sentry CLI. If you are relying on any sort of integrity hashes for your build artifacts, you will need to disable this option.

- [routeManifestInjection](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#routeManifestInjection)

| Type    | `boolean\|object` |
| ------- | ----------------- |
| Default | `true`            |

Available since: `v10.34.0`

##### App Router only

`routeManifestInjection` option is only supported in the App Router.

Controls injection and filtering of the route manifest in the client bundle.

The route manifest is a build-time generated mapping of your Next.js App Router routes that enables Sentry to group transactions by parameterized route names (for example, `/users/:id` instead of `/users/123` or `/users/456`).

You can set this option to `false` to disable the route manifest injection.

**Disable this option if:**

* You want to minimize client bundle size
* You're experiencing build issues related to route scanning
* You prefer raw URLs in transaction names

You can also pass in an object with an `exclude` property to control which routes should be excluded from the route manifest. The `exclude` property accepts an array of strings or regular expressions, or a function that returns `true` to exclude a route.

```javascript
withSentryConfig(nextConfig, {
  // Exclude specific routes using an array of strings or RegExps
  routeManifestInjection: {
    exclude: ["/api/health", "/api/excluded/[parameter]", /^\/internal\//],
  },
});
```

Excluded routes will appear as raw URLs in transaction names instead of parameterized routes.

**Use `exclude` if:**

* You want to hide internal or unreleased routes from appearing in the client bundle
* You want to reduce bundle size by excluding routes that don't benefit from parameterized grouping (for example, static routes with no dynamic segments)

## [Next.js Webpack Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#nextjs-webpack-options)

These options only take effect if you're using Webpack. If you're using Turbopack, these options will have no effect.

- [webpack.autoInstrumentServerFunctions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.autoInstrumentServerFunctions)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Automatically instrument Next.js data fetching methods and Next.js API routes with error and performance monitoring.

- [webpack.autoInstrumentMiddleware](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.autoInstrumentMiddleware)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Automatically instrument Next.js middleware with error and performance monitoring.

- [webpack.autoInstrumentAppDirectory](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.autoInstrumentAppDirectory)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Automatically instrument components in the `app` directory with error monitoring.

- [webpack.excludeServerRoutes](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.excludeServerRoutes)

| Type | `Array<RegExp \| string>` |
| ---- | ------------------------- |

Exclude specific server-side API routes or pages from automatic Sentry instrumentation during build time. This option takes an array of strings or regular expressions and affects pages in the `pages` and `app` directories.

When defining routes, note the following:

* Specify pages as routes and not as file system paths. For example, write `/animals` instead of `pages/animals/index.js`.
* Make sure that any provided string matches the route exactly, has a leading slash, and doesn't have a trailing slash.

```javascript
webpack.excludeServerRoutes: [
  "/some/excluded/route",
  "/excluded/route/with/[parameter]",
  /^\/route\/beginning\/with\/some\/prefix/,
  /\/routeContainingASpecificPathSegment\/?/,
];
```

- [webpack.automaticVercelMonitors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.automaticVercelMonitors)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Automatically create cron monitors in Sentry for your Vercel Cron Jobs if configured via `vercel.json`.

- [webpack.unstable\_sentryWebpackPluginOptions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.unstable_sentryWebpackPluginOptions)

| Type | `SentryWebpackPluginOptions` |
| ---- | ---------------------------- |

Pass configuration options directly to the [Sentry Webpack Plugin](https://www.npmjs.com/package/@sentry/webpack-plugin) that ships with the Sentry Next.js SDK. If `withSentryConfig` doesn't provide the option you need to modify, you may override the `sentryWebpackPluginOptions` using this option.

##### Important

This option is considered unstable, and its API may change in a breaking way in any release.

- [webpack.reactComponentAnnotation.enabled](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.reactComponentAnnotation.enabled)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Enables React component name tracking. When enabled, it annotates React components with data attributes that allow Sentry to track which components users interacted with in features like Session Replay and breadcrumbs.

- [webpack.reactComponentAnnotation.ignoredComponents](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.reactComponentAnnotation.ignoredComponents)

| Type | `string[] \| undefined` |
| ---- | ----------------------- |

A list of React component names to exclude from component annotation.

- [webpack.treeshake](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.treeshake)

| Type | `object` |
| ---- | -------- |

Configuration options for tree shaking. Refer to the [tree shaking documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md) for more details.

