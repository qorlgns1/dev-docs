---
title: 'Data Collected | Sentry for Next.js'
description: 'Sentry takes data privacy very seriously and has default settings in place that prioritize data safety, especially when it comes to personally identif...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected

# Data Collected | Sentry for Next.js

Sentry takes data privacy very seriously and has default settings in place that prioritize data safety, especially when it comes to personally identifiable information (PII) data. When you add the Sentry SDK to your application, you allow it to collect data and send it to Sentry during the runtime and build time of your application.

The category types and amount of data collected vary, depending on the integrations you've enabled in the Sentry SDK. This page lists data categories that the Sentry JavaScript SDK collects.

Many of the categories listed here require you to enable the [sendDefaultPii option](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii).

## [HTTP Headers](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#http-headers)

By default, the Sentry SDK sends HTTP response or request headers.

## [Cookies](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#cookies)

By default, the Sentry SDK doesn't send cookies.

If you want to send cookies, set `sendDefaultPii: true` in the `Sentry.init()` call. This will send the cookie headers `Cookie` and `Set-Cookie` from fetch and XHR requests.

## [Information About Logged-in User](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#information-about-logged-in-user)

By default, the Sentry SDK doesn't send any information about the logged-in user, such as email address, user ID, or username.

The type of logged-in user information you'll be able to send depends on the integrations you enable in Sentry's SDK. Most integrations won't send any user information. Some integrations (e.g. [User Feedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md)) make it possible to send data like the user ID, username, and email address.

## [Users' IP Address and Location](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#users-ip-address-and-location)

By default, the Sentry SDK doesn't send the user's IP address.

To enable sending the user's IP address and infer the location, set [`sendDefaultPii: true`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii). In some integrations such as [`handleRequest`](https://docs.sentry.io/platforms/javascript/guides/nextjs/guides/astro.md#customize-server-instrumentation) in Astro, you can send the user's IP address by enabling `trackClientIp`.

If sending the IP address is enabled we will try to infer the IP address or use the IP address provided by `ip_address` in [`Sentry.setUser()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setUser). If you set `ip_address: null`, the IP address won't be inferred.

## [Request URL](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#request-url)

The full request URL of outgoing and incoming HTTP requests is **always sent to Sentry**. Depending on your application, this could contain PII data. For example, a URL like `/users/1234/details`, where `1234` is a user id (which may be considered PII).

## [Request Query String](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#request-query-string)

The full request query string of outgoing and incoming HTTP requests is **always sent to Sentry**. Depending on your application, this could contain PII data. For example, a query string like `?user_id=1234`, where `1234` is a user id (which may be considered PII).

However, Sentry has some default [server-side data scrubbing](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md) in place to remove sensitive data from the query string. For example, the `apiKey` and `token` query parameters are removed by default.

## [Request Body](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#request-body)

By default, Sentry sends the size of the body content of incoming HTTP requests. This is inferred from the `content-length` header. Sentry does not send the request body itself on the client-side.

On the server-side, the incoming request body is captured by default. You can disable sending the incoming request body by configuring `ignoreIncomingRequestBody` in the [HTTP Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md).

## [Server-Side Request Data](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#server-side-request-data)

On the server-side, the [RequestData Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md) captures incoming request data including cookies, headers, query strings, request body (`data`), URL, and user information. By default, most of these fields are captured (except IP address).

##### Upcoming Changes in v11

In version 11, the default behavior of the RequestData integration will likely change to be more privacy-conscious. Fields like `cookies`, `data`, `headers`, `query_string`, and `user` will default to `false` instead of `true`. To continue capturing this data after upgrading to v11, you'll need to either explicitly configure the [RequestData Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md) or set [`sendDefaultPii: true`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii).

## [Response Body](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#response-body)

By default, the Sentry SDK doesn't send the body content of responses received from outgoing requests. By default, the SDK will send the response body size based on the `content-length` header.

## [Source Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#source-context)

By default, SDKs set up by the Sentry CLI Wizard (`@sentry/wizard`) will enable uploading source maps to Sentry.

To disable source map upload, see [the Source Maps documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md).

## [Local Variables In Stack Trace](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#local-variables-in-stack-trace)

The Sentry SDK does not send local variables in the error stack trace in client-side JavaScript SDKs.

You can enable sending local variables by setting `includeLocalVariables: true` in the `Sentry.init()` call. This activates the [Local Variables Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md). The integration is added by default in Node.js-based runtimes.

## [Device, Browser, OS and Runtime Information](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#device-browser-os-and-runtime-information)

By default, the Sentry SDK sends information about the device and runtime to Sentry.

In browser environments, this information is obtained by the User Agent string. The User Agent string contains information about the browser, operating system, and device type.

In server-side environments, the Sentry SDK uses the `os` module to get information about the operating system and architecture.

## [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#session-replay)

By default, our Session Replay SDK masks all text content, images, web views, and user input. This helps ensure that no sensitive data is exposed. You can find [more details in the Session Replay documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md).

Session Replay also captures basic information about all outgoing fetch and XHR requests in your application. This includes the URL, request and response body size, method, and status code. If [`networkDetailAllowUrls`](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#network-details) are defined, the request and response body will be sent to Sentry as well. This can include PII data if the request or response body contains PII information.

Console messages are also captured by default in Session Replay. To scrub console messages, you can use the [`beforeAddRecordingEvent`](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#custom-scrubbing) option to filter console messages before they are sent to Sentry.

## [Console Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#console-logs)

By default, the Sentry SDK sends JS console logs to Sentry as breadcrumbs which may contain PII data.

To disable sending console messages, set `console: false` in your `Sentry.breadcrumbsIntegration` config, see [the Breadcrumbs documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md).

## [Referrer URL](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#referrer-url)

By default, the Sentry SDK sends the referrer URL to Sentry. This is the URL of the page that linked to the current page.

## [Stack Trace Context Lines](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#stack-trace-context-lines)

By default, the [Context Lines Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md) is enabled. This integration sends the surrounding lines of code for each frame in the stack trace. This can include PII data if the code contains PII information.

## [LLM Inputs And Responses](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#llm-inputs-and-responses)

When using the [Vercel AI Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md), the used prompt is sent to Sentry along with meta data like model ID and used tokens. Check out the full list of attributes [in the code](https://github.com/getsentry/sentry-javascript/blob/master/packages/node/src/integrations/tracing/vercelai/index.ts).

## [Database Queries](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#database-queries)

By default, the Sentry SDK sends SQL queries to Sentry. The SQL queries can include PII information if the statement is not parametrized.

MongoDB queries are sent as well, but the Sentry SDK will not send the full MongoDB query. Instead, it will send a parameterized version of the query.

## [tRPC Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#trpc-context)

By default, the Sentry SDK doesn't send tRPC input from the tRPC context.

If you want to send the tRPC input you can enable it by setting `sendDefaultPii: true` in the `Sentry.init()` call or by setting `attachRpcInput: true` in the [`Sentry.trpcMiddleware()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md) options.

