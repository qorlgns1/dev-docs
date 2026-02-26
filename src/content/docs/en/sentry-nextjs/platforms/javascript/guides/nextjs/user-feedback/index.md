---
title: 'Set Up User Feedback | Sentry for Next.js'
description: 'The User Feedback feature allows you to collect user feedback from anywhere inside your application at any time, without needing an error event to occ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback

# Set Up User Feedback | Sentry for Next.js

The User Feedback feature allows you to collect user feedback from anywhere inside your application at any time, without needing an error event to occur first. The [Crash-Report Modal](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#crash-report-modal) feature, on the other hand, lets you prompt for user feedback when an error event occurs.

If you're using a self-hosted Sentry instance, you'll need to be on version 24.4.2 or higher in order to use the full functionality of the User Feedback feature. Lower versions may have limited functionality.

## [User Feedback Widget](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#user-feedback-widget)

The embeddable JavaScript widget allows users to submit feedback from anywhere inside your application. The [Crash-Report Modal](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#crash-report-modal) collects reactive feedback tied to an error event.

- [Pre-requisites](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#pre-requisites)

For the User Feedback integration to work, you must have the [Sentry browser SDK package](https://www.npmjs.com/package/@sentry/browser), or an equivalent framework SDK (for example, [@sentry/react](https://www.npmjs.com/package/@sentry/react)) installed. The minimum version required for the SDK is [7.85.0](https://github.com/getsentry/sentry-javascript/releases/tag/7.85.0). If you're on an older version of the SDK, please check this [migration document](https://github.com/getsentry/sentry-javascript/blob/master/MIGRATION.md).

User Feedback requires browsers that support [Shadow DOM](https://caniuse.com/shadowdomv1) and [the Dialog element](https://caniuse.com/mdn-html_elements_dialog).

- [Installation](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#installation)

The User Feedback integration is already included with the Sentry SDK. We recommend installing the SDK through our installation wizard:

```bash
npx @sentry/wizard@latest -i nextjs
```

- [Set Up](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#set-up)

To set up the integration, add the following to your Sentry initialization. There are many options you can pass to the integration constructor. See the [configuration documentation](https://docs.sentry.io/platforms/javascript/user-feedback/configuration.md) for more details.

On your client-side NextJS app, add:

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.feedbackIntegration({
      // Additional SDK configuration goes in here, for example:
      colorScheme: "system",
    }),
  ],
});
```

By default, this will insert the widget into the bottom right corner of your website. You're free to customize nearly every aspect of the widget, including replacing it completely with your own UI.

On SDK version 8.0.0 and above, users can send screenshots with their feedback. If you're self-hosting, you also need release 24.4.2 and above. You can configure this using the `enableScreenshot` option, by default it is set to `true`. Screenshots aren't supported on mobile devices, so the screenshot button will be hidden automatically in this case.

Screenshots use your [attachments quota](https://docs.sentry.io/pricing/quotas/manage-attachments-quota.md). All plans come with 1GB of attachments, which is approximately 2500 screenshots.

- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#session-replay)

The User Feedback widget integrates easily with [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md). First, make sure that the Session Replay integration is configured correctly and that `replaysOnErrorSampleRate` is greater than 0. When this is done, the Replay SDK will buffer up to 30 seconds of the user's session until the user *opens* the User Feedback widget. If the user submits feedback, you'll be able to view the feedback (including the replay), in sentry.io.

## [User Feedback API](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#user-feedback-api)

The user feedback API allows you to collect user feedback while utilizing your own UI. You can use the same programming language you have in your app to send user feedback. In this case, the SDK creates the HTTP request so you don't have to deal with posting data via HTTP.

You can optionally pass in an `associatedEventId` to associate user feedback with an error event, giving you additional insight into issues. To get an event ID, you have 2 options:

1. Use the return value of a method capturing an event.
2. Use [`beforeSend`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#before-send)
   <!-- -->
   and `Sentry.lastEventId()`.

```javascript
// All feedback fields are optional, except `message`.
const userFeedback = {
  name: "John Doe",
  email: "john@doe.com",
  message: "I really like your App, thanks!",
};
Sentry.captureFeedback(userFeedback);
```

You can also attach further data to the feedback event by passing a hint as a second argument. This is similar to other `capture` methods:

```javascript
const base64ScreenShot = "data:image/jpeg;base64...";
const res = await fetch(base64ScreenShot);
const buffer = await res.arrayBuffer();

Sentry.captureFeedback(
  { message: "I really like your App, thanks!" },
  {
    captureContext: {
      tags: { key: "value" },
    },
    attachments: [
      {
        filename: "screenshot.png",
        data: new Uint8Array(buffer),
      },
    ],
  },
);
```

## [Crash-Report Modal](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#crash-report-modal)

Our embeddable, JavaScript-based, Crash-Report modal is useful when you would typically render a plain error page (the classic `500.html`) on your website.

To collect feedback, the Crash-Report modal requests and collects the user's name, email address, and a description of what occurred. When feedback is provided, Sentry pairs the feedback with the original event, giving you additional insights into issues.

The screenshot below provides an example of the Crash-Report modal, though yours may differ depending on your customization:

- [Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#integration)

The modal authenticates with your public DSN, then passes in the Event ID that was generated on your backend.

If you're using a framework like [React](https://docs.sentry.io/platforms/javascript/guides/react.md) or [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md), the best place to collect user feedback is in your error-handling component. (Please see platform-specific docs for examples.) If you're not using a framework, you can collect feedback right before the event is sent, using `beforeSend`:

```html
<script>
  Sentry.init({
    dsn: "___PUBLIC_DSN___",
    beforeSend(event, hint) {
      // Check if it is an exception, and if so, show the report dialog
      if (event.exception && event.event_id) {
        Sentry.showReportDialog({ eventId: event.event_id });
      }
      return event;
    },
  });
</script>
```

## Pages in this section

- [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md)
- [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x.md)

