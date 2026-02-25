---
title: 'Breadcrumbs | Sentry for Next.js'
description: "Manual breadcrumbs had a good run, but Sentry's got logs. Structured, searchable, and way easier to alert or query on. Check them out!"
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs

# Breadcrumbs | Sentry for Next.js

##### Hey... did you mean Logs? Sentry has them now!

Manual breadcrumbs had a good run, but [Sentry's got logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md). Structured, searchable, and way easier to alert or query on. Check them out!

Sentry uses *breadcrumbs* to create a trail of events that happened prior to an issue. These events are very similar to traditional logs, but can record more rich structured data.

This page provides an overview of manual breadcrumb recording and customization. Learn more about the information that displays on the **Issue Details** page and how you can filter breadcrumbs to quickly resolve issues in [Using Breadcrumbs](https://docs.sentry.io/product/error-monitoring/breadcrumbs.md).

##### Learn about SDK usage

Developers who want to modify the breadcrumbs interface can learn more in our [developer documentation about the Breadcrumbs Interface](https://develop.sentry.dev/sdk/foundations/transport/event-payloads/breadcrumbs/).

## [Manual Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md#manual-breadcrumbs)

You can manually add breadcrumbs whenever something interesting happens. For example, you might manually record a breadcrumb if the user authenticates or another state change occurs.

You'll first need to import the SDK, as usual:

```javascript
import * as Sentry from "@sentry/nextjs";
```

Manually record a breadcrumb:

```javascript
Sentry.addBreadcrumb({
  category: "auth",
  message: "Authenticated user " + user.email,
  level: "info",
});
```

The available breadcrumb keys are `type`, `category`, `message`, `level`, `timestamp` (which many SDKs will set automatically for you), and `data`, which is the place to put any additional information you'd like the breadcrumb to include. Using keys other than these six won't cause an error, but will result in the data being dropped when the event is processed by Sentry.

You can choose from the following breadcrumb log levels: `"fatal"`, `"error"`, `"warning"`, `"log"`, `"info"`, and `"debug"`.

## [Automatic Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md#automatic-breadcrumbs)

SDKs and their associated integrations will automatically record many types of breadcrumbs. For example, the browser JavaScript SDK will automatically record clicks and key presses on DOM elements, XHR/fetch requests, console API calls, and all location changes.

## [Customize Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md#customize-breadcrumbs)

SDKs allow you to customize breadcrumbs through the `beforeBreadcrumb` hook.

You'll first need to import the SDK, as usual:

```javascript
import * as Sentry from "@sentry/nextjs";
```

This hook is passed an already assembled breadcrumb and, in some SDKs, an optional hint. The function can modify the breadcrumb or decide to discard it entirely by returning `null`:

```javascript
Sentry.init({
  // ...
  beforeBreadcrumb(breadcrumb, hint) {
    return breadcrumb.category === "ui.click" ? null : breadcrumb;
  },
});
```

For information about what can be done with the hint, see [Filtering Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints).

