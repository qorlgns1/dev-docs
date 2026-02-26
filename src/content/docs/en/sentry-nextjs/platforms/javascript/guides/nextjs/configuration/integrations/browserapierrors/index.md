---
title: 'BrowserApiErrors | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors

# BrowserApiErrors | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.browserApiErrorsIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

This integration wraps native time and event APIs (`setTimeout`, `setInterval`, `requestAnimationFrame`, `addEventListener/removeEventListener`) in `try/catch` blocks to handle async exceptions.

```JavaScript
Sentry.init({
  integrations: [
    Sentry.browserApiErrorsIntegration({
      setTimeout: true,
      setInterval: true,
      requestAnimationFrame: true,
      XMLHttpRequest: true,
      eventTarget: true,
      unregisterOriginalCallbacks: true,
    }),
  ],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#options)

- [`setTimeout`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#settimeout)

*Type: `boolean`*

Instrument the `setTimeout` browser built-in method.

- [`setInterval`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#setinterval)

*Type: `boolean`*

Instrument the `setInterval` browser built-in method.

- [`requestAnimationFrame`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#requestanimationframe)

*Type: `boolean`*

Instrument the `requestAnimationFrame` browser built-in method.

- [`XMLHttpRequest`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#xmlhttprequest)

*Type: `boolean`*

Instrument the `XMLHttpRequest` browser built-in method.

- [`eventTarget`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#eventtarget)

*Type: `boolean | string[]`*

Instrument the `addEventListener` browser built-in method for a set number of default event targets. To override the default event targets, provide an array of strings with the event target names.

List of default event targets:

* `EventTarget`
* `Window`
* `Node`
* `ApplicationCache`
* `AudioTrackList`
* `BroadcastChannel`
* `ChannelMergerNode`
* `CryptoOperation`
* `EventSource`
* `FileReader`
* `HTMLUnknownElement`
* `IDBDatabase`
* `IDBRequest`
* `IDBTransaction`
* `KeyOperation`
* `MediaController`
* `MessagePort`
* `ModalWindow`
* `Notification`
* `SVGElementInstance`
* `Screen`
* `SharedWorker`
* `TextTrack`
* `TextTrackCue`
* `TextTrackList`
* `WebSocket`
* `WebSocketWorker`
* `Worker`
* `XMLHttpRequest`
* `XMLHttpRequestEventTarget`
* `XMLHttpRequestUpload`

- [`unregisterOriginalCallbacks`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#unregisteroriginalcallbacks)

*Type: `boolean`*

Unregister the original `EventTarget.addEventListener` callbacks. If you experience issues with this integration (or the SDK) causing double invocations of an `addEventListener` callback, set this option to `true`. This is usually a sign of the SDK being initialized too late in the lifecycle of the page. If this is the case, you might want to consider initializing the SDK as early as possible to avoid this issue.

