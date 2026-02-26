---
title: 'Scrubbing Sensitive Data | Sentry for Next.js'
description: "As with any third-party service it's important to understand what data is being sent to Sentry, and where relevant ensure sensitive data either never ..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/sensitive-data

# Scrubbing Sensitive Data | Sentry for Next.js

As with any third-party service it's important to understand what data is being sent to Sentry, and where relevant ensure sensitive data either never reaches the Sentry servers, or at the very least it doesn’t get stored.

These are some great examples for data scrubbing that every company should think about:

* PII (Personally Identifiable Information) such as a user's name or email address, which post-GDPR should be on every company's mind.
* Authentication credentials, like your AWS password or key.
* Confidential IP (Intellectual Property), such as your favorite color, or your upcoming plans for world domination.

We offer the following options depending on your legal and operational needs:

* filtering or scrubbing sensitive data within the SDK, so that data is *not sent to* Sentry. Different SDKs have different capabilities, and configuration changes require a redeployment of your application.
* [configuring server-side scrubbing](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md) to ensure Sentry does *not store* data. Configuration changes are done in the Sentry UI and apply immediately for new events.
* [running a local Relay](https://docs.sentry.io/product/relay.md) on your own server between the SDK and Sentry, so that data is *not sent to* Sentry while configuration can still be applied without deploying.

Ensure that your team is aware of your company's policy around what can and cannot be sent to Sentry. We recommend determining this policy early in your implementation and communicating it as well as enforcing it via code review.

If you are using Sentry in your mobile app, read our [frequently asked questions about mobile data privacy](https://docs.sentry.io/security-legal-pii/security/mobile-privacy.md) to assist with Apple App Store and Google Play app privacy details.

If you *do not* wish to use the default PII behavior, you can also choose to identify users in a more controlled manner, using our [user identity context](https://docs.sentry.io/platforms/javascript/guides/koa/enriching-events/identify-user.md).

## [Scrubbing Data](https://docs.sentry.io/platforms/javascript/guides/koa/data-management/sensitive-data.md#scrubbing-data)

- [`beforeSend` & `beforeSendTransaction`](https://docs.sentry.io/platforms/javascript/guides/koa/data-management/sensitive-data.md#before-send-before-send-transaction)

SDKs provide a `beforeSend` hook, which is invoked before an error or message event is sent and can be used to modify event data to remove sensitive information. Some SDKs also provide a `beforeSendTransaction` hook which does the same thing for transactions. We recommend using `beforeSend` and `beforeSendTransaction` in the SDKs to **scrub any data before it is sent**, to ensure that sensitive data never leaves the local environment.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSend(event) {
    if (event.user) {
      // Don't send user's email address
      delete event.user.email;
    }
    return event;
  },
});
```

Sensitive data may appear in the following areas:

* Stack-locals → Some SDKs (Python, PHP and Node) will pick up variable values within the stack trace. These can be scrubbed, or this behavior can be disabled altogether if necessary.
* Breadcrumbs → Some SDKs (JavaScript and the Java logging integrations, for example) will pick up previously executed log statements. **Do not log PII** if using this feature and including log statements as breadcrumbs in the event. Some backend SDKs will also record database queries, which may need to be scrubbed. Most SDKs will add the HTTP query string and fragment as a data attribute to the breadcrumb, which may need to be scrubbed.
* User context → Automated behavior is controlled via `sendDefaultPii`.
* HTTP context → Query strings may be picked up in some frameworks as part of the HTTP request context.
* Transaction Names → In certain situations, transaction names might contain sensitive data. For example, a browser's pageload transaction might have a raw URL like `/users/1234/details` as its name (where `1234` is a user id, which may be considered PII). In most cases, our SDKs can parameterize URLs and routes successfully, that is, turn `/users/1234/details` into `/users/:userid/details`. However, depending on the framework, your routing configuration, race conditions, and a few other factors, the SDKs might not be able to completely parameterize all of your URLs.
* HTTP Spans → Most SDKs will include the HTTP query string and fragment as a data attribute, which means the HTTP span may need to be scrubbed.

For more details and data filtering instructions, see [Filtering Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md).

- [Examples](https://docs.sentry.io/platforms/javascript/guides/koa/data-management/sensitive-data.md#examples)

**Contextual information**

Instead of sending confidential information in plaintext, consider hashing it:

```javascript
Sentry.setTag("birthday", checksumOrHash("08/12/1990"));
```

This will allow you to correlate it within internal systems if needed, but keep it confidential from Sentry.

**User details**

Your organization may determine that emails are not considered confidential, but if they are, consider instead sending your internal identifier:

```javascript
Sentry.setUser({ id: user.id });

// or

Sentry.setUser({ username: user.username });
```

Doing this will ensure you still benefit from user-impact related features.

**Logging integrations**

As a best practice you should always avoid logging confidential information. If you have legacy systems you need to work around, consider the following:

* Anonymize the confidential information within the log statements (for example, swap out email addresses -> for internal identifiers)
* Use `beforeBreadcrumb` to filter it out from breadcrumbs before it is attached
* Disable logging breadcrumb integration (for example, as described [here](https://docs.sentry.io/platforms/javascript/configuration/integrations/breadcrumbs.md))

