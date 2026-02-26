---
title: 'trpcMiddleware | Sentry for Next.js'
description: 'This integration only works inside server environments (Node.js, Bun, Deno).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc

# trpcMiddleware | Sentry for Next.js

This integration only works inside server environments (Node.js, Bun, Deno).

*Import name: `Sentry.trpcMiddleware`*

The Sentry tRPC middleware creates spans for you and improves error capturing for tRPC handlers.

The `trpcMiddleware` is not a traditional SDK integration in the sense that your are **not** supposed to add it to the `integrations` option. Instead, add it as a middleware to your tRPC router.

```javascript
import * as Sentry from "@sentry/node";
import { initTRPC } from "@trpc/server";

const t = initTRPC.context().create();

const sentryMiddleware = t.middleware(
  Sentry.trpcMiddleware({
    attachRpcInput: true,
  }),
);

const sentrifiedProcedure = t.procedure.use(sentryMiddleware);
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md#options)

- [`attachRpcInput`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md#attachrpcinput)

*Type: `boolean`*

Defaults to `false`. If enabled, the RPC input will be captured in error events as `trpc` context.

##### Truncated Input

If you observe nested objects in the `trpc` context being truncated with "`[Object]`", you can define a [`normalizeDepth` value](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#normalizeDepth) to allow for more deeply nested objects in context. Note that the default depth for `trpc` context is 5.

