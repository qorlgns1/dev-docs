---
title: 'HttpClient | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient

# HttpClient | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.httpClientIntegration`*

This integration captures errors on failed requests from Fetch and XHR and attaches request and response information.

By default, error events don't contain header or cookie data. You can change this behavior by setting `sendDefaultPii: true` in your root `Sentry.init({})` config.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.httpClientIntegration()]

  // This option is required for capturing headers and cookies.
  sendDefaultPii: true,
});
```

##### Note

Due to the limitations of the Fetch and XHR API, the cookie and header collection for requests and responses is based on best effort. This means that certain headers may be missing in the event created by the integration.

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md#options)

- [`failedRequestStatusCodes`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md#failedrequeststatuscodes)

*Type: `(number|[number, number])[]`*

This array can contain tuples of `[begin, end]` (both inclusive), single status codes, or a combination of the two. Default: `[[500, 599]]`

- [`failedRequestTargets`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md#failedrequesttargets)

*Type: `(string|RegExp)[]`*

An array of request targets that should be considered, for example `['http://example.com/api/test']` would interpret any request to this URL as a failure. This array can contain Regexes, strings, or a combination of the two. Default: `[/.*/]`

- [`sendDefaultPii`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md#senddefaultpii)

*Type: `boolean`*

This option has to be specified on the root Sentry.init options, not the integration options!

This option is required for capturing headers and cookies.

