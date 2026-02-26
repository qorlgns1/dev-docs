---
title: 'Configuration | Sentry for Next.js'
description: 'If you have any questions, feedback or would like to report a bug, please open a GitHub issue with a link to a relevant replay or, if possible, a publ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration

# Configuration | Sentry for Next.js

If you have any questions, feedback or would like to report a bug, please open a [GitHub issue](https://github.com/getsentry/sentry/issues/new?assignees=\&labels=\&template=bug.yml) with a link to a relevant replay or, if possible, a publicly accessible URL to the page you're attempting to record a replay of.

## [General Integration Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#general-integration-configuration)

The following options can be configured on the root level of your browser-based Sentry SDK, in `init({})`:

| Key                      | Type     | Default | Description                                                                                                                                                                                                                                                       |
| ------------------------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| replaysSessionSampleRate | `number` | `0`     | The sample rate for replays that begin recording immediately and last the entirety of the user's session. `1.0` collects all replays, and `0` collects none.                                                                                                      |
| replaysOnErrorSampleRate | `number` | `0`     | The sample rate for replays that are recorded when an error happens. This type of replay will record up to a minute of events prior to the error and continue recording until the session ends. `1.0` captures all sessions with an error, and `0` captures none. |

The following can be configured as integration options in `replayIntegration({})`:

| Key                      | Type                     | Default     | Description                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| stickySession            | `boolean`                | `true`      | Keeps track of a user regardless of a page refresh. Note that closing a tab ends a session, so a single user using multiple tabs will be recorded as multiple sessions.                                                                                                                                                        |
| mutationLimit            | `number`                 | 10000       | The upper bound of mutations to process before Session Replay stops recording due to performance impacts. See [Mutation Limits](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#mutation-limits)                                                                                     |
| mutationBreadcrumbLimit  | `number`                 | 750         | The upper bound of mutations to process before Session Replay sends a breadcrumb to warn of large mutations. See [Mutation Limits](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#mutation-limits)                                                                                  |
| minReplayDuration        | `number`                 | 5000        | The length of the replay, **in milliseconds**, before the SDK should start sending to Sentry. Max value is 15000. **Note:** This only applies to session-based sampling (`replaysSessionSampleRate`). For error/buffer-based sampling (`replaysOnErrorSampleRate`), replays are captured immediately when an error is sampled. |
| maxReplayDuration        | `number`                 | 3600000     | The maximum length of the replay, **in milliseconds**, that the SDK should send to Sentry. Max value is 3600000 (1 hour).                                                                                                                                                                                                      |
| workerUrl                | `string`                 | `undefined` | A URL for a self-hosted worker for compression Replay data. See [Using a Custom Compression Worker](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#using-a-custom-compression-worker) to learn more.                                                                                |
| networkDetailAllowUrls   | `(string\|RegExp)[]`     | `[]`        | Capture request and response details for XHR and fetch requests that match the given URLs.                                                                                                                                                                                                                                     |
| networkDetailDenyUrls    | `(string\|RegExp)[]`     | `[]`        | Do not capture request and response details for these URLs. Takes precedence over `networkDetailAllowUrls`.                                                                                                                                                                                                                    |
| networkCaptureBodies     | `boolean`                | `true`      | Decide whether to capture request and response bodies for URLs defined in `networkDetailAllowUrls`.                                                                                                                                                                                                                            |
| networkRequestHeaders    | `string[]`               | `[]`        | Additional request headers to capture for URLs defined in `networkDetailAllowUrls`. See [Network Details](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#network-details) to learn more.                                                                                            |
| networkResponseHeaders   | `string[]`               | `[]`        | Additional response headers to capture for URLs defined in `networkDetailAllowUrls`. See [Network Details](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#network-details) to learn more.                                                                                           |
| beforeAddRecordingEvent  | `(event) => event\|null` | `i => i`    | Filter additional recording events that include console logs and network requests/responses.                                                                                                                                                                                                                                   |
| beforeErrorSampling      | `(event) => boolean`     | `i => true` | Filter error events which should be skipped for error sampling. Return `false` if error sampling should be skipped for this error event, or `true` to sample for this error. Will only be called in `buffer` mode.                                                                                                             |
| slowClickIgnoreSelectors | `string[]`               | `[]`        | Ignore slow/rage click detection on elements matching the given CSS selector(s).                                                                                                                                                                                                                                               |

## [Privacy Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#privacy-configuration)

We take privacy seriously, so we provide a number of privacy-oriented settings. Learn more about these in our our [Session Replay privacy documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md).

If you're working on a static website that's free of personal identifiable or other type of private data, you can opt out of the default text masking and image blocking by configuring the `maskAllText` and `blockAllMedia` configuration options respectively:

```javascript
Sentry.replayIntegration({
  // NOTE: This will disable built-in masking. Only use this if your site has no sensitive data, or if you've already set up other options for masking or blocking relevant data, such as 'ignore', 'block', 'mask' and 'maskFn'.
  maskAllText: false,
  blockAllMedia: false,
});
```

Starting with v8, the options `unblock` and `unmask` do not add default DOM selectors anymore. If you want to keep the default behavior of previous versions, then you should explicitly specify them in your configuration:

```javascript
Sentry.replayIntegration({
  unblock: [".sentry-unblock, [data-sentry-unblock]"],
  unmask: [".sentry-unmask, [data-sentry-unmask]"],
});
```

The following is a complete list of options that can be used in `replayIntegration({})`:

| key           | type                       | default                                      | description                                                                                                                                                                                                                                                              |
| ------------- | -------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mask          | `string[]`                 | `['.sentry-mask', '[data-sentry-mask]']`     | Mask all elements that match the given DOM selectors. See [Masking](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#masking) section for an example. Note that any configured selectors will be in *addition* to the defaults. |
| maskAllText   | `boolean`                  | `true`                                       | Mask *all* text content. Will pass text content through `maskFn` before sending to server.                                                                                                                                                                               |
| maskAllInputs | `boolean`                  | `true`                                       | Mask values of `<input>` elements. Passes input values through `maskFn` before sending to server.                                                                                                                                                                        |
| block         | `string[]`                 | `['.sentry-block', '[data-sentry-block]']`   | Redact all elements that match the DOM selector(s). See [Blocking](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#blocking) section for an example. Note that any configured selectors will be in *addition* to the defaults. |
| blockAllMedia | `boolean`                  | `true`                                       | Block *all* media elements (`img`, `svg`, `video`, `object`, `picture`, `embed`, `map`, `audio`).                                                                                                                                                                        |
| ignore        | `string[]`                 | `['.sentry-ignore', '[data-sentry-ignore]']` | Ignores all events on the matching input fields. See [Ignoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#ignoring) above for an example.                                                                                |
| maskFn        | `(text: string) => string` | `(s) => '*'.repeat(s.length)`                | Function to customize how text content is masked before sending to server. By default, masks text with `*`.                                                                                                                                                              |
| unblock       | `string[]`                 | `[]`                                         | Don't redact any elements that match the DOM selectors. Used to unblock specific media elements that are blocked with `blockAllMedia`. This doesn't affect sensitive elements such as `password`.                                                                        |
| unmask        | `string[]`                 | `[]`                                         | Unmask all elements that match the given DOM selectors. Used to unmask specific elements that are masked with `maskAllText`.                                                                                                                                             |

- [Sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#sampling)

To learn more about how session sampling works, check out our [Default Session Initialization](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#default-session-initialization) docs.

- [Network Details](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#network-details)

By default, Replay will capture basic information about all outgoing fetch and XHR requests in your application. This includes the URL, request and response body size, method, and status code. The intention is to limit the chance of collecting private data.

To capture additional information such as request and response headers or bodies, you'll need to opt-in via `networkDetailAllowUrls` (requires SDK version >= [7.50.0](https://github.com/getsentry/sentry-javascript/releases/tag/7.50.0)). This will make it possible for you to elect to only add URLs that are safe for capturing bodies and avoid any endpoints that may contain Personal Identifiable Information, (PII).

Content in bodies will be PII-sanitized server-side, based on object keys and values. Refer to our [Replay Privacy section](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#network-request-and-response-bodies-and-headers) for more details.

Any URL matching the given pattern(s) will then be captured with additional details:

```javascript
replayIntegration({
  networkDetailAllowUrls: [window.location.origin],
});
```

If you give us a string, we'll match any URL that contains that string. You can use a regex to handle exact or more complex matches.

Requests to a URL matched by the configured patterns will be enhanced with the request and response body, as well as the following default headers:

* `Content-Type`
* `Content-Length`
* `Accept`

If you want to capture additional headers, you'll have to configure them with the options `networkRequestHeaders` and `networkResponseHeaders`, for example:

```javascript
replayIntegration({
  networkDetailAllowUrls: [
    window.location.origin,
    "api.example.com",
    /^https:\/\/api\.example\.com/,
  ],

  networkRequestHeaders: ["Cache-Control"],
  networkResponseHeaders: ["Referrer-Policy"],

});
```

Captured bodies will be truncated to 150k characters max.

## [Identifying Users](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#identifying-users)

You can use the Sentry SDK to link a user to a session, and add user information to events to help you identify users that are experiencing an issue. See [setUser](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setUser) to learn how to to set the user on Sentry events.

```javascript
Sentry.setUser({ email: "jane.doe@example.com" });
```

## [Using a Custom Compression Worker](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#using-a-custom-compression-worker)

By default, Session Replay will use an inlined web worker script to compress Replay data before sending it over the network. This drastically reduces the amount of data transferred, improving performance and reducing network overhead. Because compressing data is CPU intensive, we use a web worker to offload this work to a separate thread.

While an inlined worker will work well for most applications, there are two main problems with this:

1. Since the worker code is inlined, it increases the main bundle size of your application.
2. Using inline workers can cause CSP violations if your application has a very strict CSP policy. See our [CSP](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#content-security-policy-csp) docs for more information.

To solve these problems, we provide the ability to use a custom worker script. This allows you to host the worker script on your own domain, and avoid the CSP issues that come with inline workers. Additionally, the worker script can then be removed from the main application bundle and served and cached separately.

Follow these steps in order to use a custom compression worker:

1. Download the [example worker script](https://github.com/getsentry/sentry-javascript/blob/develop/packages/replay-worker/examples/worker.min.js) from our GitHub repository.
2. Host this worker script on the same domain as your application. For example, if your application is hosted at `https://example.com`, you could host the worker script at `https://example.com/assets/worker.min.js`.
3. Configure your custom worker script in Replay:

```javascript
replayIntegration({
  workerUrl: "/assets/worker.min.js",
});
```

4. (optional) To reduce bundle size, you can now [Tree Shake](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md) the default included worker script. If you are using one of the [Sentry Bundler Plugins](https://github.com/getsentry/sentry-javascript-bundler-plugins) (version 2.10.0 or later):

```javascript
sentryPlugin({
  // other config
  bundleSizeOptimizations: {
    excludeReplayWorker: true,
  },
});
```

Since you are hosting this script yourself, you are responsible for keeping it up to date. We recommend that you check for updates to the worker script periodically, and update it as needed. The worker script API is guaranteed to remain stable inside of a major version, so any v7 worker script should be backward and forward compatible with any v7 SDK version. However, we may make improvements or bug fixes to the worker script, which you will miss out on if you don't update it.

## [Mutation Limits](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#mutation-limits)

Session Replay works by recording incremental DOM changes that occur in your web application. Generally, these changes occur in small batches and cause minimal overhead. However, it can be easy to overlook cases that will cause a large amount of DOM mutations to happen in a single update. An example is a custom dropdown component that has an unbounded list of options to render. This can negatively impact performance without Session Replay and its effects will be magnified with Session Replay enabled. In order to avoid this scenario, Session Replay will stop recording if it detects a large number of mutations (default: 10,000), which can be configured by setting `mutationLimit`. Additionally, we provide breadcrumbs in the replay to warn you when a large number of mutations are detected (default: 750).

```javascript
replayIntegration({
  mutationBreadcrumbLimit: 1000,
  mutationLimit: 1500,
});
```

## [Custom breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#custom-breadcrumbs)

Our SDKs allow you to send custom breadcrumbs, which will appear in the Replay Details UI alongside existing breadcrumbs. To learn how to send custom breadcrumbs, [read the docs here](https://docs.sentry.io/platforms/javascript/enriching-events/breadcrumbs.md#customize-breadcrumbs). Note that any custom breadcrumbs you send will be reflected in both the Issue Details breadcrumbs UI and the Replay Details breadcrumbs tab.

All custom breadcrumbs in the Replay Details will appear grey, and can be identified by the terminal logo.

In Replay Details, the breadcrumb `message` will take precedence over the `data` property. If the `message` property is set, then the string will be displayed like this:

If `message` is not set, then the breadcrumb will display the `data` property by default. For example:

The title of the breadcrumb will be the breadcrumb `category` that you set. If no `category` is set, then we will use the breadcrumb `message`. If that doesn't exist, we'll use the `description`. The last fallback with be a default title of "Custom".

