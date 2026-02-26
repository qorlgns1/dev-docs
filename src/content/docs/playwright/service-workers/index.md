---
title: "Service Workers"
description: "Service workers are only supported on Chromium-based browsers."
---

Source URL: https://playwright.dev/docs/service-workers

# Service Workers | Playwright

## Introduction[​](https://playwright.dev/docs/service-workers#introduction "Direct link to Introduction")

warning

Service workers are only supported on Chromium-based browsers.

note

If you're looking to do general network mocking, routing, and interception, please see the [Network Guide](https://playwright.dev/docs/network) first. Playwright provides built-in APIs for this use case that don't require the information below. However, if you're interested in requests made by Service Workers themselves, please read below.

[Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) provide a browser-native method of handling requests made by a page with the native [Fetch API (`fetch`)](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) along with other network-requested assets (like scripts, css, and images).

They can act as a **network proxy** between the page and the external network to perform caching logic or can provide users with an offline experience if the Service Worker adds a [FetchEvent](https://developer.mozilla.org/en-US/docs/Web/API/FetchEvent#examples) listener.

Many sites that use Service Workers simply use them as a transparent optimization technique. While users might notice a faster experience, the app's implementation is unaware of their existence. Running the app with or without Service Workers enabled appears functionally equivalent.

## How to Disable Service Workers[​](https://playwright.dev/docs/service-workers#how-to-disable-service-workers "Direct link to How to Disable Service Workers")

Playwright allows to disable Service Workers during testing. This makes tests more predictable and performant. However, if your actual page uses a Service Worker, the behavior might be different.

To disable service workers, set [testOptions.serviceWorkers](https://playwright.dev/docs/api/class-testoptions#test-options-service-workers) to `'block'`.

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        serviceWorkers: 'allow'
      },
    });

```

## Accessing Service Workers and Waiting for Activation[​](https://playwright.dev/docs/service-workers#accessing-service-workers-and-waiting-for-activation "Direct link to Accessing Service Workers and Waiting for Activation")

You can use [browserContext.serviceWorkers()](https://playwright.dev/docs/api/class-browsercontext#browser-context-service-workers) to list the Service [Worker](https://playwright.dev/docs/api/class-worker "Worker")s, or specifically watch for the Service [Worker](https://playwright.dev/docs/api/class-worker "Worker") if you anticipate a page will trigger its [registration](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register):

```
    const serviceWorkerPromise = context.waitForEvent('serviceworker');
    await page.goto('/example-with-a-service-worker.html');
    const serviceworker = await serviceWorkerPromise;

```

[browserContext.on('serviceworker')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-service-worker) event is fired _**before**_ the Service Worker has taken control over the page, so _**before**_ evaluating in the worker with [worker.evaluate()](https://playwright.dev/docs/api/class-worker#worker-evaluate) you should wait on its activation.

There are more idiomatic methods of waiting for a Service Worker to be activated, but the following is an implementation agnostic method:

```
    await page.evaluate(async () => {
      const registration = await window.navigator.serviceWorker.getRegistration();
      if (registration.active?.state === 'activated')
        return;
      await new Promise(resolve => {
        window.navigator.serviceWorker.addEventListener('controllerchange', resolve);
      });
    });

```

## Network Events and Routing[​](https://playwright.dev/docs/service-workers#network-events-and-routing "Direct link to Network Events and Routing")

Any network request made by the **Service Worker** is reported through the [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext") object:

- [browserContext.on('request')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request), [browserContext.on('requestfinished')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request-finished), [browserContext.on('response')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-response) and [browserContext.on('requestfailed')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request-failed) are fired
- [browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route) sees the request
- [request.serviceWorker()](https://playwright.dev/docs/api/class-request#request-service-worker) will be set to the Service [Worker](https://playwright.dev/docs/api/class-worker "Worker") instance, and [request.frame()](https://playwright.dev/docs/api/class-request#request-frame) will **throw**

Additionally, for any network request made by the **Page** , method [response.fromServiceWorker()](https://playwright.dev/docs/api/class-response#response-from-service-worker) return `true` when the request was handled a Service Worker's fetch handler.

Consider a simple service worker that fetches every request made by the page:

transparent-service-worker.js

```
    self.addEventListener('fetch', event => {
      // actually make the request
      const responsePromise = fetch(event.request);
      // send it back to the page
      event.respondWith(responsePromise);
    });

    self.addEventListener('activate', event => {
      event.waitUntil(clients.claim());
    });

```

If `index.html` registers this service worker, and then fetches `data.json`, the following Request/Response events would be emitted (along with the corresponding network lifecycle events):

| Event | Owner | URL | Routed | [response.fromServiceWorker()](https://playwright.dev/docs/api/class-response#response-from-service-worker) | [browserContext.on('request')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request) | [Frame](https://playwright.dev/docs/api/class-frame "Frame") | index.html | Yes |     | [page.on('request')](https://playwright.dev/docs/api/class-page#page-event-request) | [Frame](https://playwright.dev/docs/api/class-frame "Frame") | index.html | Yes |     | [browserContext.on('request')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request) | Service [Worker](https://playwright.dev/docs/api/class-worker "Worker") | transparent-service-worker.js | Yes |     | [browserContext.on('request')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request) | Service [Worker](https://playwright.dev/docs/api/class-worker "Worker") | data.json | Yes |     | [browserContext.on('request')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request) | [Frame](https://playwright.dev/docs/api/class-frame "Frame") | data.json |     | Yes | [page.on('request')](https://playwright.dev/docs/api/class-page#page-event-request) | [Frame](https://playwright.dev/docs/api/class-frame "Frame") | data.json |     | Yes |
| ----- | ----- | --- | ------ | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | --- | --- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------- | --- | --- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------- | --- | --- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | --------- | --- | --- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | --------- | --- | --- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------- | --- | --- |

Since the example Service Worker just acts a basic transparent "proxy":

- There's 2 [browserContext.on('request')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request) events for `data.json`; one [Frame](https://playwright.dev/docs/api/class-frame "Frame")-owned, the other Service [Worker](https://playwright.dev/docs/api/class-worker "Worker")-owned.
- Only the Service [Worker](https://playwright.dev/docs/api/class-worker "Worker")-owned request for the resource was routable via [browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route); the [Frame](https://playwright.dev/docs/api/class-frame "Frame")-owned events for `data.json` are not routeable, as they would not have even had the possibility to hit the external network since the Service Worker has a fetch handler registered.

caution

It's important to note: calling [request.frame()](https://playwright.dev/docs/api/class-request#request-frame) or [response.frame()](https://playwright.dev/docs/api/class-response#response-frame) will **throw** an exception, if called on a [Request](https://playwright.dev/docs/api/class-request "Request")/[Response](https://playwright.dev/docs/api/class-response "Response") that has a non-null [request.serviceWorker()](https://playwright.dev/docs/api/class-request#request-service-worker).

## Routing Service Worker Requests Only[​](https://playwright.dev/docs/service-workers#routing-service-worker-requests-only "Direct link to Routing Service Worker Requests Only")

```
    await context.route('**', async route => {
      if (route.request().serviceWorker()) {
        // NB: calling route.request().frame() here would THROW
        await route.fulfill({
          contentType: 'text/plain',
          status: 200,
          body: 'from sw',
        });
      } else {
        await route.continue();
      }
    });

```

## Known Limitations[​](https://playwright.dev/docs/service-workers#known-limitations "Direct link to Known Limitations")

Requests for updated Service Worker main script code currently cannot be routed (<https://github.com/microsoft/playwright/issues/14711>).
