---
title: 'Enriching Events | Sentry for Next.js'
description: 'In addition to the data that the Sentry SDK automatically captures, you can add additional data to events to help you debug them.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events

# Enriching Events | Sentry for Next.js

In addition to the data that the Sentry SDK automatically captures, you can add additional data to events to help you debug them.

## [Adding Additional Event Data](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#adding-additional-event-data)

There are many ways to enrich events with additional data:

- [Identifying Users](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#identifying-users)

You can add user information to events to help you identify the user that is experiencing an issue. See [setUser](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setUser) to learn how to to set the user on Sentry events.

- [Setting Tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#setting-tags)

Tags are a way to add additional metadata to events. They can be used to filter events in the Sentry UI. See [Tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/tags.md) to learn more about tags, or [setTag](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setTag) & [setTags](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setTags) to learn how to set tags on Sentry events.

- [Setting Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#setting-context)

Context is a way to add additional metadata to events. While you cannot filter by contexts in the Sentry UI, context information is displayed in the event details. See [setContext](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setContext) to learn how to set context data on Sentry events.

- [Adding Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#adding-breadcrumbs)

Breadcrumbs are a way to add information about steps that happened prior to an event. See [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md) to learn how to add breadcrumbs to Sentry events.

- [Adding Attachments](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#adding-attachments)

Attachments are a way to add additional files to events. See [Attachments](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md) to learn how to add attachments to Sentry events.

- [Event Processors](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#event-processors)

Event processors are a way to mutate events before they are sent to Sentry. See [Event Processors](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/event-processors.md) to learn how to use event processors.

## [Adding Additional Event Data To Certain Events Only](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#adding-additional-event-data-to-certain-events-only)

All APIs described above will attach data to all events for the current request.

If you only want to attach data to certain events, you can use [withScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#using-withscope) to create a new scope and attach data to that scope only.

## [Custom Fingerprinting](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#custom-fingerprinting)

All events have a fingerprint. Events with the same fingerprint are grouped together into an issue. If the default grouping for a specific type of event does not work for you, you can customize this by setting a custom fingerprint. See [Event Fingerprinting](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md) to learn how to set a custom fingerprint.

## [Scopes](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#scopes)

When an event is captured and sent to Sentry, SDKs will merge that event data with extra information from the current scope. SDKs will typically automatically manage the scopes for you in the framework integrations and you don't need to think about them. However, if you want to better understand how scopes work and how you can leverage them for your use case, you can [learn more about scopes](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md).

## [Request Isolation](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#request-isolation)

Learn more about how to [isolate requests](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/request-isolation.md) in order to ensure that set data does not leak between requests.

## [Size Limitations](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#size-limitations)

When sending context, *consider payload size limits*. Sentry does not recommend sending the entire application state and large data blobs in contexts. If you exceed the maximum payload size, Sentry will respond with HTTP error `413 Payload Too Large` and reject the event. When `keepalive: true` is used, the request may additionally stay pending forever.

The Sentry SDK will try its best to accommodate the data you send and trim large context payloads. Some SDKs can truncate parts of the event; for more details, see the [developer documentation on SDK data handling](https://develop.sentry.dev/sdk/expected-features/data-handling/).

## Pages in this section

- [Attachments](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md)
- [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md)
- [Event Fingerprinting](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md)
- [Event Level](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/level.md)
- [Event Processors](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/event-processors.md)
- [Request Isolation](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/request-isolation.md)
- [Scopes](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md)
- [Tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/tags.md)

