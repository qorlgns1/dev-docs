---
title: 'Set Up Session Replay | Sentry for Next.js'
description: 'If you have any questions, feedback or would like to report a bug, please open a GitHub issue with a link to a relevant replay or, if possible, a publ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay

# Set Up Session Replay | Sentry for Next.js

If you have any questions, feedback or would like to report a bug, please open a [GitHub issue](https://github.com/getsentry/sentry/issues/new?assignees=\&labels=\&template=bug.yml) with a link to a relevant replay or, if possible, a publicly accessible URL to the page you're attempting to record a replay of.

[Session Replay](https://docs.sentry.io/product/explore/session-replay.md) helps you get to the root cause of an error or latency issue faster by providing you with a video-like reproduction of what was happening in the user's browser before, during, and after the issue. You can rewind and replay your application's DOM state and see key user interactions, like mouse clicks, scrolls, network requests, and console entries, in a single combined UI inspired by your browser's DevTools.

By default, our Session Replay SDK masks all DOM text content, images, and user input, giving you heightened confidence that no sensitive data will leave the browser. To learn more, see [Session Replay Privacy](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md).

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#prerequisites)

Session Replay requires your SDK to be version `7.27.0` or higher. If you're on an older version, please check the [migration document](https://github.com/getsentry/sentry-javascript/blob/master/MIGRATION.md).

Session Replay requires Node 12+, and browsers newer than IE11.

## [Install](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#install)

Session Replay is included with `@sentry/nextjs`. If you haven't installed Sentry yet, run the wizard:

```bash
npx @sentry/wizard@latest -i nextjs
```

If you already have Sentry installed, skip to [Set Up](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#set-up) below.

## [Set Up](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#set-up)

To set up the integration, add the following to your Sentry initialization. There are several options you can pass to the integration constructor. See the [configuration documentation](https://docs.sentry.io/platforms/javascript/session-replay/configuration.md) for more details.

Session Replay only runs in the browser, so you only need to configure it in `instrumentation-client.ts`. The server (`sentry.server.config.ts`) and edge (`sentry.edge.config.ts`) entry points run in Node.js and Edge runtimes where Replay is not available.

#
- [Add Replay Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#add-replay-integration)

Add `replayIntegration()` to your client initialization and configure the sample rates.

**Testing tip:** Set `replaysSessionSampleRate: 1.0` during development to capture all sessions.

`instrumentation-client.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // This sets the sample rate to be 10%. You may want this to be 100% while
  // in development and sample at a lower rate in production
  replaysSessionSampleRate: 0.1,

  // If the entire session is not sampled, use the below sample rate to sample
  // sessions when an error occurs.
  replaysOnErrorSampleRate: 1.0,

  integrations: [Sentry.replayIntegration()],
});
```

#
- [Privacy Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#privacy-options)

By default, Replay masks all text and blocks media. Customize privacy settings based on your needs.

See [Session Replay Privacy](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md) for all options.

`instrumentation-client.ts`

```typescript
Sentry.replayIntegration({
  // Text masking (default: true)
  maskAllText: true,

  // Block images/videos (default: true)
  blockAllMedia: true,

  // Mask specific inputs
  maskAllInputs: true,
}),
```

- [PII & Privacy Considerations](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#pii--privacy-considerations)

Personally identifiable information (PII) and privacy are important considerations when enabling Session Replay. There are multiple ways in which Sentry helps you avoid collecting PII, including:

* [Masking](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#masking), which replaces text content with something else (the default behavior being to replace each character with a `*`).
* Making [network request and response bodies](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#network-request-and-response-bodies-and-headers) opt-in, to avoid capturing endpoints that may contain PII.

For static websites without sensitive data, you can opt out of the default masking and blocking settings.

#
- [Lazy-Loading Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#lazy-loading-replay)

Load Replay only when needed instead of at startup. Useful for reducing initial bundle size.

`instrumentation-client.ts`

```typescript
// Don't add replayIntegration to init
Sentry.init({
  integrations: [],
});

// Later, when you want to start recording:
import("@sentry/nextjs").then((lazyLoadedSentry) => {
  Sentry.addIntegration(lazyLoadedSentry.replayIntegration());
});
```

- [Canvas Recording](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#canvas-recording)

There is currently no PII scrubbing in canvas recordings!

#
- [Enable Canvas Recording](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#enable-canvas-recording)

Add `replayCanvasIntegration()` to record HTML canvas elements. This is opt-in and tree-shaken from your bundle if not used.

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,

  integrations: [
    // Keep the Replay integration as before
    Sentry.replayIntegration(),

    // The following is all you need to enable canvas recording with Replay

    Sentry.replayCanvasIntegration(),

  ],
});
```

#
- [3D and WebGL Canvases](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#3d-and-webgl-canvases)

For 3D/WebGL canvases, the integration needs `preserveDrawingBuffer` to export images, which can affect performance. To avoid this, enable manual snapshotting and call `snapshot()` inside your paint loop.

Call `snapshot()` in the same execution loop as draw commands to avoid capturing empty buffers.

```javascript
// Step 1: Enable manual snapshotting
Sentry.replayCanvasIntegration({
  enableManualSnapshot: true,
});

// Step 2: Call snapshot in your paint loop
function paint() {
  const canvasRef = document.querySelector("#my-canvas");
  Sentry.getClient()
    ?.getIntegrationByName("ReplayCanvas")
    ?.snapshot(canvasRef);
}
```

#
- [WebGPU Canvases](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#webgpu-canvases)

WebGPU canvas textures expire after the current task completes. Use `skipRequestAnimationFrame: true` to capture immediately after rendering.

```javascript
// Step 1: Enable manual snapshotting
Sentry.replayCanvasIntegration({
  enableManualSnapshot: true,
});

// Step 2: Snapshot immediately after rendering
function paint() {
  const canvasRef = document.querySelector("#my-canvas");
  const canvasIntegration =
    Sentry.getClient()?.getIntegrationByName("ReplayCanvas");

  // ... your WebGPU rendering commands ...

  // Capture immediately - required for WebGPU
  canvasIntegration?.snapshot(canvasRef, {
    skipRequestAnimationFrame: true,
  });
}
```

- [Content Security Policy (CSP)](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#content-security-policy-csp)

#
- [Configure CSP for Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#configure-csp-for-replay)

Session Replay uses a WebWorker for compression off the main UI thread. Add these CSP entries to allow workers to load.

Safari versions ≤ 15.4 also need `child-src`.

```text
worker-src 'self' blob:
child-src 'self' blob:
```

If you're unable to update your CSP policy to allow inline web workers, you can also [use a custom compression worker](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#using-a-custom-compression-worker) instead.

## [User Session](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#user-session)

A user session starts when the Session Replay SDK is first loaded and initialized. The session will capture any pageloads, refreshes, or navigations as long as the SDK is re-initialized on the same domain, and in the same browser tab, each time. Sessions continue capturing data until 5 minutes pass without any user interactions **or** until a maximum of 60 minutes have elapsed. Closing the browser tab will end the session immediately, according to the rules for [SessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage).

An *interaction* refers to either a mouse click or a browser navigation event.

- [Replay Captures on Errors Only](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#replay-captures-on-errors-only)

If you prefer not to record an entire session, you can elect to capture a replay only if an error occurs. In this case, the integration will buffer up to one minute worth of events prior to the error being thrown. It will continue to record the session, following the rules above regarding session life and activity. Read the [sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#sampling) section for configuration options.

## [Sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#sampling)

Sampling controls how much traffic results in a Session Replay.

#
- [Configure Sample Rates](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#configure-sample-rates)

* `replaysSessionSampleRate` - Percentage of sessions to record fully
* `replaysOnErrorSampleRate` - Percentage of sessions to record when an error occurs (buffers 1 minute before the error)

**Tip:** Keep `replaysOnErrorSampleRate` at `1.0` - error sessions provide the most debugging value.

#
- [Recommended Production Sample Rates](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#recommended-production-sample-rates)

| Traffic Volume            | Session Rate | Error Rate |
| ------------------------- | ------------ | ---------- |
| **High** (100k+/day)      | `0.01` (1%)  | `1.0`      |
| **Medium** (10k-100k/day) | `0.1` (10%)  | `1.0`      |
| **Low** (under 10k/day)   | `0.25` (25%) | `1.0`      |

`instrumentation-client.ts`

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Capture 10% of all sessions
  replaysSessionSampleRate: 0.1,

  // Capture 100% of sessions with errors
  replaysOnErrorSampleRate: 1.0,

  integrations: [Sentry.replayIntegration()],
});
```

- [How Sampling Works](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#how-sampling-works)

Sampling begins as soon as a session starts. When someone visits your application, sampling decisions happen in this order:

1. **`replaysSessionSampleRate` is checked first**

   * If sampled: Full session recording starts and is sent to Sentry in real-time
   * If not sampled: Recording is buffered in memory only (last 60 seconds kept)

2. **If an error occurs** (and session wasn't selected for full recording):

   * `replaysOnErrorSampleRate` is checked
   * If sampled: Buffered 60 seconds + rest of session is sent to Sentry
   * If not sampled: Buffer is discarded, nothing sent

**When data leaves your browser:**

| Scenario                             | Data Sent to Sentry                         |
| ------------------------------------ | ------------------------------------------- |
| Selected for session sampling        | Immediately (real-time chunks)              |
| Not selected, no error occurs        | Never (buffer discarded)                    |
| Not selected, error occurs & sampled | After error (60s before + everything after) |

Read more about [understanding sessions](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md).

## [Error Linking](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#error-linking)

Errors that happen on the page while a replay is running will be linked to the replay, making it possible to jump between related issues and replays. However, it's **possible** that in some cases the error count reported on the **Replays Details** page won't match the actual errors that have been captured. That's because errors can be lost, and while this is uncommon, there are a few reasons why it could happen:

* The replay was rate-limited and couldn't be accepted.
* The replay was deleted by a member of your org.
* There were network errors and the replay wasn't saved.

## [Trace Linking](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#trace-linking)

When [tracing](https://docs.sentry.io/product/explore/traces.md) is enabled, traces are visible in the Replay timeline. This lets you see performance data in the context of what the user was doing — you can watch a user click a button, then see the corresponding network request and how long it took.

From the Replay Details page, click on any trace span in the timeline to jump directly to the trace view. From there, you can drill into individual spans, see database queries, API calls, and identify performance bottlenecks that affected the user's experience.

This connection works both ways: when viewing a trace, you can jump to the associated replay to see exactly what the user experienced during that operation.

## [Verify](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#verify)

While you're testing, we recommend that you set `replaysSessionSampleRate` to `1.0`. This ensures that every user session will be sent to Sentry.

Once testing is complete, **we recommend lowering this value in production**. We still recommend keeping `replaysOnErrorSampleRate` set to `1.0`.

## [Related Features](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#related-features)

* [Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md) — Traces are visible in the Replay timeline, showing you performance data in context.
* [Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md) — Logs emitted during a replay session are automatically linked for easy navigation.

## [Replay Next Steps](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#replay-next-steps)

*
- [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md)

  Learn about the general Session Replay configuration fields.

*
- [Privacy](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)

  Configuring Session Replay to maintain user and data privacy.

*
- [Replay Issues](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/issue-types.md)

  Learn about the Issue types that Session Replay can detect.

*
- [Understanding Sessions](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md)

  Learn about customizing sessions with the Session Replay SDK.

*
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/troubleshooting.md)

  Troubleshooting Session Replay-specific Issues

## Pages in this section

- [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md)
- [Privacy](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)
- [Replay Issues](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/issue-types.md)
- [Understanding Sessions](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/troubleshooting.md)

