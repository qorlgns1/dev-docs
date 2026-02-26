---
title: 'FileSystem | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs

# FileSystem | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.fsIntegration`*

The `fsIntegration` creates spans for `fs` API operations, like reading and writing files. The integration uses the [`@opentelemetry/instrumentation-fs`](https://www.npmjs.com/package/@opentelemetry/instrumentation-fs) package.

##### Potential Performance Overhead

The `fsIntegration` may add significant overhead to your application. Especially in scenarios with a lot of file I/O, like for example when you are running a framework dev server, including this integration can massively slow down your application.

```JavaScript
Sentry.init({
  integrations: [Sentry.fsIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md#options)

- [`recordFilePaths`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md#recordfilepaths)

*Type: `boolean | undefined`*

Setting this option to `true` will include any filepath arguments from your `fs` API calls as span attributes. Defaults to `false`.

- [`recordErrorMessagesAsSpanAttributes`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md#recorderrormessagesasspanattributes)

*Type: `boolean | undefined`*

Setting this option to `true` will include the error messages of failed `fs` API calls as a span attribute. Defaults to `false`.

