---
title: 'Node Profiling | Sentry for Next.js'
description: 'By default, Sentry error events will not get trace context unless you configure the scope with the transaction, as illustrated in the example below.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node

# Node Profiling | Sentry for Next.js

By default, Sentry error events will not get trace context unless you configure the scope with the transaction, as illustrated in the example below.

If you're adopting Profiling in a high-throughput environment, we recommend testing prior to deployment to ensure that your service's performance characteristics maintain expectations.

## [Installation](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#installation)

You have to install the `@sentry/profiling-node` package in addition to your main SDK package:

```bash
npm install @sentry/profiling-node --save
```

The version of the `@sentry/profiling-node` package must match the version of the main SDK package exactly.

## [Enabling Profiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#enabling-profiling)

Profiling supports two modes: `manual` and `trace`. These modes are mutually exclusive and cannot be used at the same time.

In `manual` mode, the profiling data collection can be managed via calls to `Sentry.profiler.startProfiler` and `Sentry.profiler.stopProfiler`. You are entirely in the in control of when the profiler runs.

In `trace` mode, the profiler manages its own start and stop calls, which are based on spans: the profiler continues to run while there is at least one active span, and stops when there are no active spans.

- [Enabling Trace Lifecycle Profiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#enabling-trace-lifecycle-profiling)

To enable profiling, add `@sentry/profiling-node` to your imports and set up `nodeProfilingIntegration` in your Sentry config.

```javascript
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Add our Profiling integration
+   nodeProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
+ profileSessionSampleRate: 1.0,
+ profileLifecycle: 'trace',
});

// Profiling happens automatically after setting it up with `Sentry.init()`.
// All spans (unless those discarded by sampling) will have profiling data attached to them.
Sentry.startSpan(
  {
    op: "rootSpan",
    name: "My root span",
  },
  () => {
    // The code executed here will be profiled
  }
);
```

- [Enabling Manual Lifecycle Profiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#enabling-manual-lifecycle-profiling)

To enable profiling, add `@sentry/profiling-node` to your imports and set up `nodeProfilingIntegration` in your Sentry config.

```javascript
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Add our Profiling integration
+   nodeProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
+ profileSessionSampleRate: 1.0,
+ profileLifecycle: 'manual',
});

// All spans (unless those discarded by sampling) will have profiling data attached to them.
Sentry.profiler.startProfiler();
// Code executed between these two calls will be profiled
Sentry.profiler.stopProfiler();
```

- [Managing profile sampling rates](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#managing-profile-sampling-rates)

Sentry SDK supports an additional `profileSessionSampleRate` that will enable or disable profiling for the entire session. This can be used if you want to control session sampling rates at the service level as the sampling decision is evaluated only once at SDK init.

This is useful for cases where you deploy your service many times, but would only like a subset of those services to be profiled.

```javascript
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Add our Profiling integration
    nodeProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
+ profileSessionSampleRate: 0.0
});
```

## [How Does It Work?](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#how-does-it-work)

Under the hood, the Sentry profiler uses V8's [CpuProfiler](https://v8docs.nodesource.com/node-18.2/d2/d34/classv8_1_1_cpu_profiler.html) to collect stack samples. This means that `sentry/profiling-node` is written as a [native add-on](https://nodejs.org/docs/latest-v18.x/api/addons.html) for Node and won't run in environments like Deno or Bun. Profiling enhances tracing by providing profiles for individual transactions. This allows you to look at higher level performance information like transaction and span durations before diving deeper and looking at profiles.

## [Runtime Flags](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#runtime-flags)

There are three runtime flags you can set that control the behavior of the profiler. Two of the flags relate to how the SDK resolves the profiler binaries. The third alters how the underlying profiler is initialized by [v8](https://v8docs.nodesource.com/).

These flags are intended for advanced use cases only. Setting them isn't required for most use cases.

* SENTRY\_PROFILER\_BINARY\_PATH

This flag sets the profiler binary path and bypasses arch, platform, and libc checks. It can be useful in some build configurations if you want to override which binary is required at runtime.

* SENTRY\_PROFILER\_BINARY\_DIR

Acts similarly to the flag above, however, this flag only specifies the directory where the binaries are located and defers to the runtime to resolve the correct binary depending on the arch, platform, and libc version.

* SENTRY\_PROFILER\_LOGGING\_MODE

The default mode of the v8 CpuProfiler is [kEagerLogging](https://v8docs.nodesource.com/node-18.2/d2/dc3/namespacev8.html#a874b4921ddee43bef58d8538e3149374), which enables the profiler even when no profiles are active—this is good because it makes calls to startProfgiler faster with the tradeoff of constant CPU overhead. This behavior can be controlled via the `SENTRY_PROFILER_LOGGING_MODE` environment variable with values of `eager|lazy`. If you opt to use the lazy-logging mode, calls to `startProfiler` may be slow. (Depending on environment and node version, it can be in the order of a few hundred ms.)

Here's an example of starting a server with lazy-logging mode:

```bash
# Run profiler in lazy mode
SENTRY_PROFILER_LOGGING_MODE=lazy node server.js
```

## [Precompiled Binaries](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#precompiled-binaries)

The `@sentry/profiling-node` package precompiles binaries for a number of common architectures. This minimizes the tooling required to run the package and avoids compiling the package from source in most cases, which speeds up installation. Currently, we ship prebuilt binaries for the following architectures and Node versions:

* macOS x64: Node v18, v20, v22, v24
* Linux ARM64 (musl): Node v18, v20, v22, v24
* Linux x64 (glibc): Node v18, v20, v22, v24
* Windows x64: Node v18, v20, v22, v24

The set of common architectures should cover a wide variety of use cases, but if you have feedback or experience different behavior, please open an issue in the [Sentry JavaScript SDK](https://github.com/getsentry/sentry-javascript) repository.

