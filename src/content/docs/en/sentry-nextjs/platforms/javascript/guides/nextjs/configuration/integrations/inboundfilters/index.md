---
title: 'InboundFilters | Sentry for Next.js'
description: "This integration is enabled by default. If you'd like to modify your default integrations, read this."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters

# InboundFilters | Sentry for Next.js

*Import name: `Sentry.inboundFiltersIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

This integration allows you to ignore specific errors based on the type, message, or URLs in a given exception.

By default, it'll ignore errors that start with `Script error` or `JavaScript error: Script error`.

To configure this integration, use the `ignoreErrors`, `ignoreTransactions`, `denyUrls`, and `allowUrls` SDK options directly. For example:

```javascript
Sentry.init({
  ignoreErrors: ["ignore-this-error"],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#options)

Remember to pass these options to the root Sentry.init call, not the integration!

- [`ignoreErrors`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#ignoreerrors)

*Type: `(string|RegExp)[]`*

A list of strings or regex patterns that match error messages that shouldn't be sent to Sentry. Messages that match these strings or regular expressions will be filtered out before they're sent to Sentry. When using strings, partial matches will be filtered out, so if you need to filter by exact match, use regex patterns instead. By default, all errors are sent.

- [`ignoreTransactions`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#ignoretransactions)

*Type: `(string|RegExp)[]`*

A list of strings or regex patterns that match transaction names that shouldn't be sent to Sentry. Transactions that match these strings or regular expressions will be filtered out before they're sent to Sentry. When using strings, partial matches will be filtered out, so if you need to filter by exact match, use regex patterns instead. By default, transactions spanning typical API health check requests are filtered out.

- [`allowUrls`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#allowurls)

*Type: `(string|RegExp)[]`*

An array of strings or regex patterns that match the URLs of scripts where errors have been created. Only errors that have been created on these URLs will be sent to Sentry. If you use this option, errors will only be sent when the top stack frame file URL contains or matches at least one entry in the allowUrls array. All string entries in the array will be matched with `stackFrameUrl.contains(entry)`, while all RegEx entries will be matched with `stackFrameUrl.match(entry)`.

For example, if you add `'foo.com'` to the array, errors created on `https://bar.com/myfile/foo.com` will be captured because URL will be matched with "contains" logic and the last segment of the URL contains `foo.com`.

This matching logic applies for captured exceptions, not raw message events. By default, all errors are sent.

If your scripts are loaded from `cdn.example.com` and your site is `example.com`, you can set `allowUrls` to the following to exclusively capture errors being created in scripts in these locations:

```javascript
Sentry.init({
  allowUrls: [/https?:\/\/((cdn|www)\.)?example\.com/],
});
```

- [`denyUrls`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#denyurls)

*Type: `(string|RegExp)[]`*

An array of strings or regex patterns that match the URLs of scripts where errors have been created. Errors that have been created on these URLs won't be sent to Sentry. If you use this option, errors will not be sent when the top stack frame file URL contains or matches at least one entry in the `denyUrls` array. All string entries in the array will be matched with `stackFrameUrl.contains(entry)`, while all RegEx entries will be matched with `stackFrameUrl.match(entry)`.

This option checks the source file URL in the stack trace, not the HTTP URL where the error was reported. For more fine grained filtering please refer to [beforeSend](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#beforeSend).

This matching logic applies to captured exceptions not raw message events. By default, all errors are sent.

