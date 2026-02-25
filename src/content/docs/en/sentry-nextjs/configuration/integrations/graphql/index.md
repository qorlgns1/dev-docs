---
title: 'GraphQL | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql

# GraphQL | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.graphqlIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `graphqlIntegration` adds instrumentation for the `graphql` library to capture spans using [`@opentelemetry/instrumentation-graphql`](https://www.npmjs.com/package/@opentelemetry/instrumentation-graphql).

```JavaScript
Sentry.init({
  integrations: [Sentry.graphqlIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#supported-versions)

* `graphql`: `>=14.0.0 <17`

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#options)

- [`ignoreResolveSpans`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#ignoreresolvespans)

*Type: `boolean`*

If spans for resolver functions should not be created. Default is `true`.

- [`ignoreTrivialResolveSpans`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#ignoretrivialresolvespans)

*Type: `boolean`*

If spans for the execution of the default resolver on object properties should not be created. Default is `true`.

When a resolver function is not defined on the schema for a field, GraphQL will use the default resolver which just looks for a property with that name on the object. If the property is not a function, it's not very interesting to trace. This option can reduce noise and number of spans created.

- [`useOperationNameForRootSpan`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#useoperationnameforrootspan)

*Type: `boolean`*

By default, this option is `true`.

With this setting enabled, the GraphQL instrumentation dynamically updates the name of the `http.server` root span by appending the operation names. Instead of generic span names like `POST /graphql`, span names will be more descriptive, such as `POST /graphql (query MyQuery)`. For requests containing multiple operations, the span names will aggregate operation names, for example `POST /graphql (query Query1, query Query2)`

Set the option to `false` to preserve the default `http.server` span name without this additional context.

