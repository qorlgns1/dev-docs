---
title: 'RequestData | Sentry for Next.js'
description: 'This integration adds data from incoming requests to transaction and error events that occur during request handling done by the backend.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata

# RequestData | Sentry for Next.js

*Import name: `Sentry.Integrations.RequestData`*

This integration adds data from incoming requests to transaction and error events that occur during request handling done by the backend.

Please note that this integration is only available on the server.

## [Options:](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md#options)

* `include` (object)

Controls what types of data are added to the event:

```javascript
{
  cookies: boolean; // default: true,
  data: boolean; // default: true,
  headers: boolean; // default: true,
  ip: boolean; // default: false,
  query_string: boolean; // default: true,
  url: boolean; // default: true,
}
```

* `transactionNamingSchema` (string)

Controls how the transaction will be reported. Options are 'path' (`/some/route`), 'methodPath' (`GET /some/route`), and 'handler' (the name of the route handler function, if available). Defaults to `methodPath`

