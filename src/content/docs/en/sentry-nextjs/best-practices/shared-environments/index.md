---
title: 'Shared Environments / Browser Extensions | Sentry for Next.js'
description: 'We recommend using JavaScript SDK  and above when using the SDK with shared environments. Check out our migration docs to upgrade from an older SDK ve...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments

# Shared Environments / Browser Extensions | Sentry for Next.js

We recommend using JavaScript SDK `8.x` and above when using the SDK with shared environments. Check out our [migration docs](https://docs.sentry.io/platforms/javascript/migration.md) to upgrade from an older SDK version to `8.x` and above.

These best practices are relevant for you if you set up Sentry in one of the following use-cases:

* Browser Extensions
* VSCode Extensions
* Third-Party Widgets
* Plugin Architecture
* Libraries
* Any other scenario where you might have multiple Sentry instances running in the same environment

When setting up Sentry in a shared environment where multiple Sentry instances may run, you should **not use `Sentry.init()`**, as this will pollute the global state. If your browser extension uses `Sentry.init()`, and a website also uses Sentry, the extension may send events to the website's Sentry project, or vice versa.

## [Shared Environment Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments.md#shared-environment-setup)

For the use cases listed above, set up a client manually as seen in the example below. In addition, avoid adding any integrations that use global state, like `Breadcrumbs` or `GlobalHandlers` (see code snippet below). Furthermore, some default integrations that use the global state have to be filtered as in the example below. In these scenarios, it's a best practice to avoid using any integrations and to rely on manually capturing errors.

```javascript
import {
  BrowserClient,
  defaultStackParser,
  getDefaultIntegrations,
  makeFetchTransport,
  Scope,
} from "@sentry/browser";

// filter integrations that use the global variable
const integrations = getDefaultIntegrations({}).filter(
  (defaultIntegration) => {
    return ![
      "BrowserApiErrors",
      "BrowserSession",
      "Breadcrumbs",
      "ConversationId",
      "GlobalHandlers",
      "FunctionToString",
    ].includes(defaultIntegration.name);
  },
);

const client = new BrowserClient({
  dsn: "___PUBLIC_DSN___",
  transport: makeFetchTransport,
  stackParser: defaultStackParser,
  integrations: integrations,
});

const scope = new Scope();
scope.setClient(client);

client.init(); // initializing has to be done after setting the client on the scope

// You can capture exceptions manually for this client like this:
scope.captureException(new Error("example"));
```

To make it a bit simpler but somewhat still maintain "Let Sentry handle unhandled errors" you can use the following code:

```javascript
// Init Sentry as shown above

try {
  // Your goes code here
  // as in import and execute your code here
  // and if an error occurs, Sentry will capture it
} catch (error) {
  scope.captureException(error);
}
```

## [Sending logs from shared environments](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments.md#sending-logs-from-shared-environments)

You can pass the scope directly into the logger API methods to make shared environments work.

```js
const scope = new Scope();
scope.setClient(client);

client.init(); // initializing has to be done after setting the client on the scope

Sentry.logger.info("my logger message", {}, { scope });
```

## [Browser Extension Filter](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments.md#browser-extension-filter)

If you notice that Sentry is not capturing error events from the browser extension, an Inbound Filter might be active. You can disable that by going to your **Project Settings > Inbound Filters** and disabling filtering out errors known to be caused by browser extensions.

Read more about Inbound Filters in the product documentation under [Inbound filters](https://docs.sentry.io/concepts/data-management/filtering.md#inbound-data-filters).

## [Skipping the Browser Extension Check](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments.md#skipping-the-browser-extension-check)

*Available in all browser-based SDKs since version `8.37.0`*

If for some reason, the SDK wrongfully detects that it's initialized in a browser extension, you can skip the check by specifying the `skipBrowserExtensionCheck` option when initializing the SDK:

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  skipBrowserExtensionCheck: true,
  // ...
});
```

You shouldn't use this option if you're in fact using the SDK in a browser extension or another shared environment. Initializing the SDK via `Sentry.init` has no advantages over manually setting up the client and scope as described on this page. You'd risk quota increases with unactionable issues, interference with other Sentry SDKs, and data leakage by doing so.

This option is purely meant as an escape hatch if our browser extension check is incorrectly detecting a browser extension. An example for this might be a cross-platform application framework that exposes similar global APIs like browser extensions.

