---
title: 'Attachments | Sentry for Next.js'
description: 'Sentry can enrich your events for further investigation by storing additional files, such as config or log files, as attachments.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments

# Attachments | Sentry for Next.js

Sentry can enrich your events for further investigation by storing additional files, such as config or log files, as attachments.

## [Uploading Attachments](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md#uploading-attachments)

You'll first need to import the SDK, as usual:

```javascript
import * as Sentry from "@sentry/nextjs";
```

Attachments live on the `Scope` and will be sent with all events.

```javascript
// Add an attachment
Sentry.getCurrentScope().addAttachment({
  filename: "attachment.txt",
  data: "Some content",
});

// Clear attachments
Sentry.getCurrentScope().clearAttachments();
```

An attachment has the following fields:

`filename`

The filename is required and will be displayed in [sentry.io](https://sentry.io).

`data`

The content of the attachment is required and is either a `string` or `Uint8Array`.

`contentType`

The type of content stored in this attachment. Any [MIME type](https://www.iana.org/assignments/media-types/media-types.xhtml) may be used; the default is `application/octet-stream`.

`mimetype`

The specific media content type that determines how the attachment is rendered in the Sentry UI. We currently support and can render the following MIME types:

* `text/plain`
* `text/css`
* `text/csv`
* `text/html`
* `text/javascript`
* `text/json` or `text/x-json` or `application/json` or `application/ld+json`
* `image/jpeg`
* `image/png`
* `image/gif`
* `image/webp`
* `image/avif`
* `video/webm`
* `video/mp4`

## [Add or Modify Attachments Before Sending](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md#add-or-modify-attachments-before-sending)

It's possible to add, remove, or modify attachments before an event is sent by way of the [`beforeSend`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#before-send)hook or a global event processor.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSend: (event, hint) => {
    hint.attachments = [
      { filename: "screenshot.png", data: captureScreen() },
    ];
    return event;
  },
});

Sentry.addEventProcessor((event, hint) => {
  hint.attachments = [{ filename: "log.txt", data: readLogFile() }];
  return event;
});
```

Sentry allows at most 40MB for a compressed request, and at most 200MB of uncompressed attachments per event, including the crash report file (if applicable). Uploads exceeding this size are rejected with HTTP error `413 Payload Too Large` and the data is dropped immediately. To add larger or more files, consider secondary storage options.

Attachments persist for 30 days; if your total storage included in your quota is exceeded, attachments will not be stored. You can delete attachments or their containing events at any time. Deleting an attachment does not affect your quota - Sentry counts an attachment toward your quota as soon as it is stored.

Learn more about how attachments impact your [quota](https://docs.sentry.io/pricing/quotas.md).

- [Access to Attachments](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md#access-to-attachments)

To limit access to attachments, navigate to your organization's **General Settings**, then select the *Attachments Access* dropdown to set appropriate access — any member of your organization, the organization billing owner, member, admin, manager, or owner.

By default, access is granted to all members when storage is enabled. If a member does not have access to the project, the ability to download an attachment is not available; the button will be greyed out in Sentry. The member may only view that an attachment is stored.

## [Viewing Attachments](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md#viewing-attachments)

Attachments display on the bottom of the **Issue Details** page for the event that is shown.

Alternately, attachments also appear in the *Attachments* tab on the **Issue Details** page, where you can view the *Type* of attachment, as well as associated events. Click the Event ID to open the **Issue Details** of that specific event.

