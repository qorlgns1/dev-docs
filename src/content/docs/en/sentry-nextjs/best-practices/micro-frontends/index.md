---
title: 'Micro Frontends | Sentry for Next.js'
description: 'To ensure the Sentry JavaScript SDK works with your micro frontends, make sure all micro frontends that import from a  package are using the same vers...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends

# Micro Frontends | Sentry for Next.js

To ensure the Sentry JavaScript SDK works with your micro frontends, make sure all micro frontends that import from a `@sentry/*` package are [using the same version of the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#sdk-version-alignment).

If your app uses micro frontends, it's very useful to be able to track which one an error is coming from. To do this with Sentry, you can create either an automatic or a manual setup where you send events to separate Sentry projects representing each of your micro frontends. This makes it easier to see what's going wrong and where, helping you track issues and fix them faster, especially in complex frontend architectures.

Below you'll find setup instructions for both an automatic and a manual way to route errors to different Sentry projects.

## [Vercel Multi-Zone Micro Frontends](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#vercel-multi-zone-micro-frontends)

Vercel's multi-zone applications let you slice a large app into smaller, independently managed projects. Each project operates as its own application, with its own UI and tech stack. For example, you might use Next.js for one project, SvelteKit for another, and React for a third.

To set up Sentry in a multi-zone setup, configure Sentry separately within each project. Follow the installation steps for the framework each project uses. Here are a few examples:

* **[Next.js](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)**
* **[React](https://docs.sentry.io/platforms/javascript/guides/react.md)**
* **[SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)**

We recommend using a different DSN for each project. This makes it easier to identify which project errors are coming from, helping you track issues and fix them faster in complex frontend architectures.

With the exception of Vercel multi-zone micro frontends, you should call `Sentry.init()` only once in your application. Initializing Sentry multiple times can lead to unexpected behavior.

## [Automatically Route Errors to Different Projects](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#automatically-route-errors-to-different-projects)

`ModuleMetadata` and `makeMultiplexedTransport` can be used together to automatically route events to specific Sentry projects that represent your micro frontend services. Events will be routed once the service where the error occurred has been identified, ensuring errors are tracked in the correct project.

* Requires version `2.18.0` or higher of `@sentry/webpack-plugin`, `@sentry/rollup-plugin`, `@sentry/vite-plugin` or `@sentry/esbuild-plugin`.

* Requires SDK version `7.59.0` or higher.

To identify the source of an error, you must first inject metadata that helps identify which bundles were responsible for the error. You can do this with any of the Sentry bundler plugins by enabling the `moduleMetadata` option. The example below is for Webpack, but this is also supported in Vite, Rollup, and esbuild.

**Install the below code snippet in your micro frontend:**

```javascript
// webpack.config.js
const { sentryWebpackPlugin } = require("@sentry/webpack-plugin");

module.exports = {
  devtool: "hidden-source-map", // Source map generation must be turned on ("hidden-source-map", "source-map", etc.)
  plugins: [
    sentryWebpackPlugin({
      moduleMetadata: ({ release }) => ({
        dsn: "__MODULE_DSN__",
        release,
      }),
    }),
  ],
};
```

**Replace `__MODULE_DSN__` with your actual Sentry project DSN.** You can find your DSN in your Sentry project settings under Client Keys (DSN).

Once metadata has been injected into modules, the `moduleMetadataIntegration` can be used to look up that metadata and attach it to stack frames with matching file names. This metadata is then available in the `beforeSend` callback as the `module_metadata` property on each `StackFrame`. This can be used to identify which bundles may be responsible for an error. Once the destination is determined, you can store it as a list of DSN-release pairs in `event.extra[MULTIPLEXED_TRANSPORT_EXTRA_KEY]` for the multiplexed transport to reference for routing.

**Install the below code snippet in your host:**

```javascript
import {
  init,
  makeFetchTransport,
  moduleMetadataIntegration,
  makeMultiplexedTransport,
  MULTIPLEXED_TRANSPORT_EXTRA_KEY,
} from "@sentry/browser";

init({
  dsn: "__DEFAULT_DSN__",
  integrations: [moduleMetadataIntegration()],
  transport: makeMultiplexedTransport(makeFetchTransport),
  beforeSend: (event) => {
    if (event?.exception?.values?.[0].stacktrace.frames) {
      const frames = event.exception.values[0].stacktrace.frames;
      // Find the last frame with module metadata containing a DSN
      const routeTo = frames
        .filter(
          (frame) => frame.module_metadata && frame.module_metadata.dsn,
        )
        .map((v) => v.module_metadata)
        .slice(-1); // using top frame only - you may want to customize this according to your needs

      if (routeTo.length) {
        event.extra = {
          ...event.extra,
          [MULTIPLEXED_TRANSPORT_EXTRA_KEY]: routeTo,
        };
      }
    }

    return event;
  },
});
```

**Replace `__DEFAULT_DSN__` with your actual Sentry project DSN.** This should be the DSN for your default/fallback Sentry project. You can find your DSN in your Sentry project settings under Client Keys (DSN).

Once this is set up, errors - both handled and unhandled - will be automatically routed to the right project.

By default, `args.getEvent` returns only error events. You can match against other event types like so: `args.getEvent(['event', 'transaction', 'replay_event'])`. This `getEvent` snippet will return matches for errors, transactions, and replays.

## [Manually Route Errors to Different Projects](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#manually-route-errors-to-different-projects)

If you want more control to be able to explicitly specify the destination for each individual `captureException`, you can use the multiplexed transport's API to route events to specific projects.

Requires SDK version `7.59.0` or higher.

- [Using the Default Matcher](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#using-the-default-matcher)

The simplest way to manually route events is by using the default matcher with `MULTIPLEXED_TRANSPORT_EXTRA_KEY`:

```js
import {
  captureException,
  init,
  makeFetchTransport,
  makeMultiplexedTransport,
  MULTIPLEXED_TRANSPORT_EXTRA_KEY,
} from "@sentry/browser";

init({
  dsn: "__FALLBACK_DSN__",
  transport: makeMultiplexedTransport(makeFetchTransport),
});

// Route a specific error to different projects
captureException(new Error("oh no!"), {
  extra: {
    [MULTIPLEXED_TRANSPORT_EXTRA_KEY]: [
      { dsn: "__CART_DSN__", release: "cart@1.0.0" },
      { dsn: "__GALLERY_DSN__", release: "gallery@1.2.0" },
    ],
  },
});
```

- [Using a Custom Matcher](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#using-a-custom-matcher)

For more advanced routing logic, you can provide a custom matcher function. The example below uses a `feature` tag to determine which Sentry project to send the event to. If the event doesn't have a `feature` tag, we send it to the fallback DSN defined in `Sentry.init`.

```js
import {
  captureException,
  init,
  makeFetchTransport,
  makeMultiplexedTransport,
} from "@sentry/browser";

init({
  dsn: "__FALLBACK_DSN__",
  transport: makeMultiplexedTransport(makeFetchTransport, ({ getEvent }) => {
    const event = getEvent();

    // Send to different DSNs, based on the event payload
    if (event?.tags?.feature === "cart") {
      return [{ dsn: "__CART_DSN__", release: "cart@1.0.0" }];
    } else if (event?.tags?.feature === "gallery") {
      return [{ dsn: "__GALLERY_DSN__", release: "gallery@1.2.0" }];
    } else {
      return [];
    }
  }),
});
```

**Replace the placeholder DSN values with your actual Sentry project DSNs:**

* Replace `__FALLBACK_DSN__` with the DSN for your fallback/default Sentry project
* Replace `__CART_DSN__` with the DSN for your cart micro frontend's Sentry project
* Replace `__GALLERY_DSN__` with the DSN for your gallery micro frontend's Sentry project

You can find your DSNs in each Sentry project's settings under Client Keys (DSN).

You can then set tags/contexts on events in individual micro-frontends to decide which Sentry project to send the event to as follows:

It's important to always use a local scope when setting the tag (either as shown below or using<!-- -->

[withScope documentation<!-- -->](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#local-scopes)

). Using a global scope, for example, through `Sentry.setTag()` will result in all subsequent events being routed to the same DSN regardless of where they originated.

```typescript
captureException(new Error("oh no!"), (scope) => {
  scope.setTag("feature", "cart");
  return scope;
});
```

## [SDK Version Alignment](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#sdk-version-alignment)

Starting with version [8.7.0](https://github.com/getsentry/sentry-javascript/releases/tag/8.7.0), if you have multiple Sentry JavaScript SDKs on the same page, they [only interact with each other](https://github.com/getsentry/sentry-javascript/pull/12206) if they're using the same version. This prevents unwanted cross-SDK interactions, where calls or accesses to recently added or no longer existing SDK APIs would lead to errors. A classic example for this are browser extensions or 3rd party scripts using Sentry when the host app also uses Sentry.

However, for use cases like micro frontends, where you might *want* SDK interaction across multiple micro frontends or child applications, you'll need to ensure that all SDKs are using the same version. For example, if you initialize the SDK in a host or skeleton application, but make Sentry SDK calls (like `Sentry.captureException` or `Sentry.setTag`) in micro frontend child applications, you need to ensure that the SDK packages in the host and child applications are aligned to the same version.

If you can't get all your micro frontends aligned on the same SDK version, you can [follow this workaround](https://github.com/getsentry/sentry-javascript/discussions/10576#discussioncomment-11446422). However, interoperability isn't guaranteed and you could run into some unexpected behavior.

