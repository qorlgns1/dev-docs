---
title: 'Event Processors | Sentry for Next.js'
description: 'You can enrich events with additional data by adding your own event processors, either on the scope level or globally. Though event processors are sim...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/event-processors

# Event Processors | Sentry for Next.js

You can enrich events with additional data by adding your own event processors, either on the scope level or globally. Though event processors are similar to `beforeSend` and `beforeSendTransaction`, there are two key differences:

* `beforeSend` and `beforeSendTransaction` are guaranteed to be run last, after all other event processors, (which means they get the final version of the event right before it's sent, hence the name). Event processors added with either of the methods below run in an undetermined order, which means changes to the event may still be made after the event processor runs.
* While `beforeSend`, `beforeSendTransaction`, and processors added with `Sentry.addEventProcessor` run globally, regardless of scope, processors added with `scope.addEventProcessor` only run on events captured while that scope is active.

Like `beforeSend` and `beforeSendTransaction`, event processors are passed two arguments, the event itself and [a `hint` object](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints) containing extra metadata.

Event processors added to the current scope will run on every event sent after they are added.

```javascript
Sentry.addEventProcessor(function (event, hint) {
  // Add anything to the event here
  // returning `null` will drop the event
  return event;
});
```

Event processors added to a local scope using `withScope` only apply to events captured inside that scope.

```javascript
Sentry.withScope(function (scope) {
  scope.addEventProcessor(function (event, hint) {
    // Add anything to the event here
    // returning `null` will drop the event
    return event;
  });
  // The event processor will apply to this event
  Sentry.captureMessage("Test");
});

// The event processor will NOT apply to this event
Sentry.captureMessage("Test2");
```

