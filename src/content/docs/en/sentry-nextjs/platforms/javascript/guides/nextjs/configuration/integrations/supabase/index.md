---
title: 'Supabase | Sentry for Next.js'
description: 'The  adds instrumentation for the Supabase client to capture spans for both authentication and database operations.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase

# Supabase | Sentry for Next.js

*Import name: `Sentry.supabaseIntegration`*

The `supabaseIntegration` adds instrumentation for the Supabase client to capture spans for both authentication and database operations.

## [Installation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#installation)

You need to have both the Sentry SDK and the Supabase library installed. For Supabase installation instructions, refer to the [Supabase JavaScript documentation](https://supabase.com/docs/reference/javascript/introduction).

## [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#configuration)

This is the preferred method for most use cases. and follows Sentry's standard integration pattern.

```javascript
import { createClient } from "@supabase/supabase-js";

const supabaseClient = createClient(
  "YOUR_SUPABASE_URL",
  "YOUR_SUPABASE_KEY",
);

Sentry.init({
  dsn: "YOUR_DSN",
  integrations: [Sentry.supabaseIntegration({ supabaseClient })],
  tracesSampleRate: 1.0,
});
```

## [Generated Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#generated-spans)

The integration provides comprehensive monitoring for both authentication and database operations:

- [Authentication Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#authentication-spans)

The integration automatically instruments the following auth operations:

* `signInWithPassword`
* `signOut`
* `signInAnonymously`
* `signInWithOAuth`
* `signInWithIdToken`
* `signInWithOtp`
* `signInWithSSO`
* `signUp`
* `verifyOtp`
* `reauthenticate`

Admin operations are also instrumented:

* `createUser`
* `deleteUser`
* `listUsers`
* `getUserById`
* `updateUserById`
* `inviteUserByEmail`

- [Database Operation Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#database-operation-spans)

These spans are used to populate Sentry's [Query Insights](https://docs.sentry.io/product/insights/backend/queries.md) feature, which provides performance metrics and analysis for your database operations. With Query Insights, you can identify slow queries, track query frequency, and optimize your database interactions.

* `db.table`: The table being queried
* `db.schema`: The database schema
* `db.url`: The Supabase instance URL
* `db.sdk`: Client information
* `db.system`: Set to 'postgresql'
* `db.query`: The query parameters
* `db.body`: The request body (for mutations)

- [Queue Operation Spans (in progress)](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#queue-operation-spans-in-progress)

Coming soon, the Sentry SDK will also support generating spans for interactions with Supabase queues. For more information, please follow [this GitHub issue](https://github.com/getsentry/sentry-javascript/issues/14611).

## [Error Tracking](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#error-tracking)

The integration automatically:

* Captures errors from failed operations
* Adds breadcrumbs for database operations
* Includes detailed context about the operation that failed

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#supported-versions)

* `@supabase/supabase-js`: `>=2.0.0`

