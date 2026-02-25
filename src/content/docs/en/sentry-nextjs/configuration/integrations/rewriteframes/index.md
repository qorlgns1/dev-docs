---
title: 'RewriteFrames | Sentry for Next.js'
description: 'This integration allows you to apply a transformation to each frame of the stack trace. In the streamlined scenario, it can be used to change the name...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes

# RewriteFrames | Sentry for Next.js

*Import name: `Sentry.rewriteFramesIntegration`*

This integration allows you to apply a transformation to each frame of the stack trace. In the streamlined scenario, it can be used to change the name of the file frame it originates from, or it can be fed with an iterated function to apply any arbitrary transformation.

On Windows machines, you have to use Unix paths and skip the volume letter in the `root` option to enable it. For example, `C:\\Program Files\\Apache\\www` won't work, however, `/Program Files/Apache/www` will.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.rewriteFramesIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#options)

- [`root`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#root)

*Type: `string`*

Root path that will be stripped from the current frame's filename by the default iteratee if the filename is an absolute path.

- [`prefix`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#prefix)

*Type: `string`*

A custom prefix that will be used by the default iteratee. Default: `app://`

- [`iteratee`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#iteratee)

*Type: `(frame) => frame`*

Function that takes the frame, applies a transformation, and returns it.

## [Usage Examples](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#usage-examples)

For example, if the full path to your file is `/www/src/app/file.js`:

| Usage                                        | Path in Stack Trace      | Description                                                                                                                   |
| -------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `rewriteFramesIntegration()`                 | `app:///file.js`         | The default behavior is to replace the absolute path, except the filename, and prefix it with the default prefix (`app:///`). |
| `rewriteFramesIntegration({prefix: 'foo/'})` | `foo/file.js`            | Prefix `foo/` is used instead of the default prefix `app:///`.                                                                |
| `rewriteFramesIntegration({root: '/www'})`   | `app:///src/app/file.js` | `root` is defined as `/www`, so only that part is trimmed from the beginning of the path.                                     |

