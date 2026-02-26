---
title: 'ExtraErrorData | Sentry for Next.js'
description: 'This integration extracts all non-native attributes from the error object and attaches them to the event as extra data. If the error object has a .toJ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata

# ExtraErrorData | Sentry for Next.js

*Import name: `Sentry.extraErrorDataIntegration`*

This integration extracts all non-native attributes from the error object and attaches them to the event as extra data. If the error object has a .toJSON() method, the ExtraErrorData integration will run it to extract additional information.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.extraErrorDataIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md#options)

- [`depth`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md#depth)

*Type: `number`*

Limit of how deep the object serializer should go. The default is 3. Anything deeper than the set limit will be replaced with standard Node.js REPL notation of \[Object], \[Array], \[Function], or a primitive value.

- [`captureErrorCause`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md#captureerrorcause)

*Type: `boolean`*

Indicates if the serializer should catch the `cause` of the error. The default is true. For more information, see the [Error: cause MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause).

