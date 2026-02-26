---
title: 'Browser Profiling | Sentry for Next.js'
description: 'Browser Profiling is currently in beta. Beta features are still in progress and may have bugs. We recognize the irony.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser

# Browser Profiling | Sentry for Next.js

Browser Profiling is currently in beta. Beta features are still in progress and may have bugs. We recognize the irony.

[Profiling](https://docs.sentry.io/product/explore/profiling.md) captures function-level data from your production code to enable you to fine-tune your app's performance. It tracks what's being called, how often, and where. In the browser, this helps you pinpoint causes of UI jank, understand why metrics like [Interaction to Next Paint (INP)](https://docs.sentry.io/product/insights/web-vitals/web-vitals-concepts.md#interaction-to-next-paint-inp) are slow, or identify long tasks blocking repaints and causing frame drops.

##### Chromium Only

Browser Profiling uses the [JS Self-Profiling API](https://wicg.github.io/js-self-profiling/), currently only available in Chromium-based browsers (Chrome, Edge). Profiles will only include data from these browsers.

## [Quick Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#quick-setup)

**Requirements**: `@sentry/nextjs `SDK version `10.27.0`+ (or `7.60.0`+ for deprecated transaction-based profiling)

- [1. Install the SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#1-install-the-sdk)

```bash
npm install @sentry/nextjs --save
```

- [2. Add the Document-Policy Header](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#2-add-the-document-policy-header)

Your server must return `Document-Policy: js-profiling` in response headers.

In Next.js you can configure document response headers via the `headers` option in `next.config.js`:

`next.config.mjs`

```javascript
export default withSentryConfig({
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          {
            key: "Document-Policy",
            value: "js-profiling",
          },
        ],
      },
    ];
  },

  // ... other Next.js config options
});
```

- [3. Configure the SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#3-configure-the-sdk)

`instrumentation-client.js|ts`

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Add browser profiling integration to the list of integrations
    Sentry.browserProfilingIntegration(),
  ],

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for tracing.
  // We recommend adjusting this value in production
  tracesSampleRate: 1.0,
  // Set `tracePropagationTargets` to control for which URLs trace propagation should be enabled
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],

  // Set profileSessionSampleRate to 1.0 to profile during every session.
  // The decision, whether to profile or not, is made once per session (when the SDK is initialized).
  profileSessionSampleRate: 1.0,
});
```

## [Profiling Modes](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#profiling-modes)

| Mode                 | Description                                   | Use When                                            |
| -------------------- | --------------------------------------------- | --------------------------------------------------- |
| **Manual** (default) | You control when profiling runs               | Profiling specific user flows or interactions       |
| **Trace**            | Profiler runs automatically with active spans | You want profiles attached to all traced operations |

- [Manual Mode](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#manual-mode)

Start and stop the profiler around code you want to profile:

```javascript
Sentry.uiProfiler.startProfiler();
// Code here will be profiled
Sentry.uiProfiler.stopProfiler();
```

- [Trace Mode](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#trace-mode)

Profiles automatically attach to spans. Enable by setting `profileLifecycle: "trace"`:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.browserTracingIntegration(),
    Sentry.browserProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
  profileSessionSampleRate: 1.0,
  profileLifecycle: "trace",
});
```

## [Sentry vs Chrome DevTools](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#sentry-vs-chrome-devtools)

|                   | Sentry Profiling            | Chrome DevTools     |
| ----------------- | --------------------------- | ------------------- |
| **Environment**   | Production (real users)     | Local development   |
| **Sampling rate** | 100Hz (10ms period)         | 1000Hz (1ms period) |
| **Source maps**   | Deobfuscated function names | Minified names      |
| **Data scope**    | Aggregated across users     | Single session      |

Troubleshooting

**Chrome DevTools shows "Profiling Overhead"**

When `browserProfilingIntegration` is enabled, Chrome DevTools incorrectly attributes rendering work as profiling overhead. Disable the integration when using DevTools locally.

**Profiles only from Chrome users**

This is expected. The JS Self-Profiling API is currently only implemented in Chromium browsers. Consider this bias when analyzing data.

