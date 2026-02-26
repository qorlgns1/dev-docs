---
title: 'Event Fingerprinting | Sentry for Next.js'
description: 'All events have a fingerprint. Events with the same fingerprint are grouped together into an issue.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting

# Event Fingerprinting | Sentry for Next.js

All events have a fingerprint. Events with the same fingerprint are grouped together into an issue.

By default, Sentry will run one of our built-in grouping algorithms to generate a fingerprint based on information available within the event such as `stacktrace`, `exception`, and `message`. To extend the default grouping behavior or change it completely, you can use a combination of the following options:

1. In your SDK, using SDK Fingerprinting, as documented below
2. In your project, using [Fingerprint Rules](https://docs.sentry.io/concepts/data-management/event-grouping/fingerprint-rules.md) or [Stack Trace Rules](https://docs.sentry.io/concepts/data-management/event-grouping/stack-trace-rules.md)

In supported SDKs, you can override Sentry's default grouping that passes the fingerprint attribute as an array of strings. The length of a fingerprint's array is not restricted. This works similarly to the [fingerprint rules functionality](https://docs.sentry.io/concepts/data-management/event-grouping/fingerprint-rules.md), which is always available and can achieve similar results.

## [Basic Example](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md#basic-example)

In the most basic case, values are passed directly:

```javascript
function makeRequest(method, path, options) {
  return fetch(method, path, options).catch(function (err) {
    Sentry.withScope(function (scope) {
      // group errors together based on their request and response
      scope.setFingerprint([method, path, String(err.statusCode)]);
      Sentry.captureException(err);
    });
  });
}
```

You can use variable substitution to fill dynamic values into the fingerprint generally computed on the server. For instance, the value `{{ default }}` can be added to add the entire normally generated grouping hash into the fingerprint. These values are the same as for server-side fingerprinting. See [Variables](https://docs.sentry.io/concepts/data-management/event-grouping/fingerprint-rules.md#variables) for more information.

## [Group Errors With Greater Granularity](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md#group-errors-with-greater-granularity)

In some scenarios, you'll want to group errors more granularly.

For example, if your application queries a Remote Procedure Call Model (RPC) interface or external Application Programming Interface (API) service, the stack trace is generally the same, even if the outgoing request is very different.

The following example will split up the default group Sentry would create (represented by `{{ default }}`) further, taking some attributes on the error object into account:

```javascript
class MyRPCError extends Error {
  constructor(message, functionName, errorCode) {
    super(message);

    // The name of the RPC function that was called (e.g. "getAllBlogArticles")
    this.functionName = functionName;

    // For example a HTTP status code returned by the server.
    this.errorCode = errorCode;
  }
}

Sentry.init({
  // ...
  beforeSend: function (event, hint) {
    const exception = hint.originalException;

    if (exception instanceof MyRPCError) {
      event.fingerprint = [
        "{{ default }}",
        String(exception.functionName),
        String(exception.errorCode),
      ];
    }

    return event;
  },
});
```

## [Group Errors More Aggressively](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md#group-errors-more-aggressively)

You can also overwrite Sentry's grouping entirely.

For example, if a generic error, such as a database connection error, has many different stack traces and never groups them together, you can overwrite Sentry's grouping by omitting `{{ default }}` from the array:

```javascript
class DatabaseConnectionError extends Error {}

Sentry.init({
  // ...
  beforeSend: function (event, hint) {
    const exception = hint.originalException;

    if (exception instanceof DatabaseConnectionError) {
      event.fingerprint = ["database-connection-error"];
    }

    return event;
  },
});
```

