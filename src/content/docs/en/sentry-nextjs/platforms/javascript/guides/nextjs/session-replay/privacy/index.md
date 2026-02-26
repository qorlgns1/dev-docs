---
title: 'Privacy | Sentry for Next.js'
description: 'If you have any questions, feedback or would like to report a bug, please open a GitHub issue with a link to a relevant replay or, if possible, a publ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy

# Privacy | Sentry for Next.js

If you have any questions, feedback or would like to report a bug, please open a [GitHub issue](https://github.com/getsentry/sentry/issues/new?assignees=\&labels=\&template=bug.yml) with a link to a relevant replay or, if possible, a publicly accessible URL to the page you're attempting to record a replay of.

Before enabling Session Replay in production, verify your masking configuration to ensure no sensitive data is captured. Our default settings aggressively mask potentially sensitive data, but if you modify these settings or update UI frameworks or system SDKs, you must thoroughly test your application. If you find any masking issues or sensitive data that should be masked but isn't, please [create a GitHub issue](https://github.com/getsentry/sentry-javascript/issues/new/choose) and avoid deploying to production with Session Replay enabled until the issue is resolved.

There are several ways to deal with personally identifiable information (PII). By default, the Session Replay SDK will mask all text content with `*` and block all media elements (`img`, `svg`, `video`, `object`, `picture`, `embed`, `map`, `audio`) on the client, before it is sent to the server. This can be disabled by setting `maskAllText` to `false`. It's also possible to add the following CSS classes to specific DOM elements to prevent recording their contents: `sentry-block`, `sentry-ignore`, and `sentry-mask`. The following sections will show examples of how content is handled by the differing methods.

## [Masking](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#masking)

Masking replaces the text content with something else. The default masking behavior is to replace each character with a `*`. Elements with class name `sentry-mask` or the attribute `data-sentry-mask` will be blocked. In this example, the relevant HTML code is: `<table class="sentry-mask">...</table>`:

You can configure what to mask or unmask via the following [configuration](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#privacy-configuration):

```javascript
replayIntegration({
  mask: [".mask-me"],
  unmask: [".unmask-me"],
});
```

## [Blocking](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#blocking)

Blocking replaces the element with a placeholder that has the same dimensions. The recording will show an empty space in place of the content. Elements with class name `sentry-block` or the attribute `data-sentry-block` will be blocked. In this example, the relevant HTML code is: `<table data-sentry-block>...</table>`:

You can configure what to block or unblock via the following [configuration](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#privacy-configuration):

```javascript
replayIntegration({
  block: [".block-me"],
  unblock: [".unblock-me"],
});
```

## [Ignoring](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#ignoring)

Ignoring only applies to form inputs. Events will be ignored on the input element so that the replay doesn't show what occurs inside of the input. Any event on an input element with class name `sentry-ignore` or the attribute `data-sentry-ignore` will be ignored. Notice how the results in the table below show input changes, but no visible text:

You can configure what to ignore via the following [configuration](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#privacy-configuration):

```javascript
replayIntegration({
  ignore: [".ignore-me"],
});
```

## [Privacy Configuration](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#privacy-configuration)

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

| key           | type                       | default                                      | description                                                                                                                                                                                                                                          |
| ------------- | -------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mask          | `string[]`                 | `['.sentry-mask', '[data-sentry-mask]']`     | Mask all elements that match the given DOM selectors. See [Masking](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#masking) section for an example. Note that any configured selectors will be in *addition* to the defaults. |
| maskAllText   | `boolean`                  | `true`                                       | Mask *all* text content. Will pass text content through `maskFn` before sending to server.                                                                                                                                                           |
| maskAllInputs | `boolean`                  | `true`                                       | Mask values of `<input>` elements. Passes input values through `maskFn` before sending to server.                                                                                                                                                    |
| block         | `string[]`                 | `['.sentry-block', '[data-sentry-block]']`   | Redact all elements that match the DOM selector(s). See [Blocking](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#blocking) section for an example. Note that any configured selectors will be in *addition* to the defaults. |
| blockAllMedia | `boolean`                  | `true`                                       | Block *all* media elements (`img`, `svg`, `video`, `object`, `picture`, `embed`, `map`, `audio`).                                                                                                                                                    |
| ignore        | `string[]`                 | `['.sentry-ignore', '[data-sentry-ignore]']` | Ignores all events on the matching input fields. See [Ignoring](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#ignoring) above for an example.                                                                                |
| maskFn        | `(text: string) => string` | `(s) => '*'.repeat(s.length)`                | Function to customize how text content is masked before sending to server. By default, masks text with `*`.                                                                                                                                          |
| unblock       | `string[]`                 | `[]`                                         | Don't redact any elements that match the DOM selectors. Used to unblock specific media elements that are blocked with `blockAllMedia`. This doesn't affect sensitive elements such as `password`.                                                    |
| unmask        | `string[]`                 | `[]`                                         | Unmask all elements that match the given DOM selectors. Used to unmask specific elements that are masked with `maskAllText`.                                                                                                                         |

## [Network Request and Response Bodies and Headers](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#network-request-and-response-bodies-and-headers)

Collecting request and response bodies is an opt-in feature. That's because the best way to avoid getting PII into Sentry is by not adding URLs of endpoints that may contain PII. Additionally, Sentry attempts to [scrub](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md) certain types of sensitive data from request and response bodies, if you accidentally opt-in to a URL that includes this type of data. This mechanism happens on our ingestion service, before data hits our disks. This is a best effort approach which pattern-matches the content with things like credit card information, social security numbers, and [passwords](https://github.com/search?q=repo%3Agetsentry%2Frelay%20PASSWORD_KEY_REGEX\&type=code).

More details about this feature can be found in the [configuration page](https://docs.sentry.io/platforms/javascript/session-replay/configuration.md#network-details).

## [Custom Scrubbing](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#custom-scrubbing)

The `beforeAddRecordingEvent` has been added starting with SDK version 7.53.0. It allows you to modify, scrub the recordings to remove PII, or ignore recording events before they leave the browser. These events include console logs, network requests, and response data.

```javascript
Sentry.replayIntegration({
  beforeAddRecordingEvent: (event) => {
    // Filter out specific events
    if (event.data.tag === "foo") {
      return null;
    }

    // Remember to return an event if you want to keep it!
    return event;
  },
});
```

- [Example: Capturing 500 Status Codes Only](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#example-capturing-500-status-codes-only)

Here's an example showing how to only capture fetch requests that return a 500 status code. (Non-fetch requests would continue to be captured normally.)

```javascript
Sentry.replayIntegration({
  beforeAddRecordingEvent: (event) => {
    // Do not capture fetch/xhr requests, unless the response code is 500
    if (
      event.data.tag === "performanceSpan" &&
      (event.data.payload.op === "resource.fetch" ||
        event.data.payload.op === "resource.xhr") &&
      event.data.payload.data.statusCode !== 500
    ) {
      return null;
    }

    return event;
  },
});
```

We also have [server-side PII scrubbing](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md) for this data. It looks for certain patterns such as American social security numbers, credit cards, and private keys.

- [Example: Scrubbing URLs](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#example-scrubbing-urls)

By default, URLs are stored in both recording and replay events.

To scrub the URL in a recording event, use the above `beforeAddRecordingEvent`.

To scrub the URL in a replay event, use `addEventProcessor`:

```javascript
Sentry.addEventProcessor((event) => {
  // Ensure that we specifically look at replay events
  if (event.type !== "replay_event") {
    // Return the event, otherwise the event will be dropped
    return event;
  }

  // Your URL scrubbing function
  function urlScrubber(url) {
    return url.replace(/([a-z0-9]{3}\.[a-z]{5}\.[a-z]{7})/, "[Filtered]");
  }

  // Scrub all URLs with your scrubbing function
  event.urls = event.urls && event.urls.map(urlScrubber);

  return event;
});
```

- [Deprecated Options](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#deprecated-options)

Note that the privacy API prior to version 7.35.0 has been deprecated and replaced with the options above. Please see the [Replay migration guide](https://github.com/getsentry/sentry-javascript/blob/master/packages/replay/MIGRATION.md#upgrading-replay-from-7340-to-7350---6645) for further information.

