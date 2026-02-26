---
title: 'ZodErrors | Sentry for Next.js'
description: 'The Zod Errors integration enhances error reporting for applications using Zod schema validation. When Zod validation fails, this integration captures...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors

# ZodErrors | Sentry for Next.js

*Import name: `Sentry.zodErrorsIntegration`*

The Zod Errors integration enhances error reporting for applications using [Zod](https://zod.dev/) schema validation. When Zod validation fails, this integration captures detailed validation errors (`ZodError` instances) and attaches them as additional data to Sentry events.

The Zod Errors integration is not enabled by default. You need to add it to your Sentry configuration:

```javascript
Sentry.init({
  integrations: [Sentry.zodErrorsIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md#options)

The `zodErrorsIntegration` accepts the following options:

- [`limit`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md#limit)

*Type: `number`* *Default: `10`*

Limits the number of Zod errors inlined in each Sentry event.

- [`saveZodIssuesAsAttachment`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md#savezodissuesasattachment)

*Type: `boolean`* *Default: `false`*

Save full list of Zod issues as a JSON attachment in Sentry.

## [Example Additional Error Data](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md#example-additional-error-data)

When a Zod validation error occurs, you'll see enhanced error information in Sentry like this:

```json
[
  {
    "code": "too_small",
    "path": ["name"],
    "message": "Name is required",
    "minimum": 1,
    "type": "string",
    "inclusive": true,
    "received": ""
  },
  {
    "code": "invalid_string",
    "path": ["email"],
    "message": "Invalid email format",
    "validation": "email",
    "received": "invalid-email"
  }
]
```

