---
title: 'Google Gen AI | Sentry for Next.js'
description: 'For meta-framework applications using all runtimes, you need to manually wrap your Google Gen AI client instance with . See instructions in the Browse...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai

# Google Gen AI | Sentry for Next.js

## [Server-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#server-side-usage)

For meta-framework applications using all runtimes, you need to manually wrap your Google Gen AI client instance with `instrumentGoogleGenAIClient`. See instructions in the [Browser-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#browser-side-usage) section.

## [Browser-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#browser-side-usage)

*Import name: `Sentry.instrumentGoogleGenAIClient`*

The `instrumentGoogleGenAIClient` helper adds instrumentation for the [`@google/genai`](https://www.npmjs.com/package/@google/genai) SDK to capture spans by wrapping Google Gen AI SDK calls and recording LLM interactions with configurable input/output recording. You need to manually wrap your Google Gen AI client instance with this helper. See example below:

```javascript
import { GoogleGenAI } from "@google/genai";

const genAI = new GoogleGenAI({
  apiKey: "your-api-key", // Warning: API key will be exposed in browser!
});

const client = Sentry.instrumentGoogleGenAIClient(genAI, {
  recordInputs: true,
  recordOutputs: true,
});

// Use the wrapped client instead of the original genAI instance
const result = await client.models.generateContent("Hello!");
```

To customize what data is captured (such as inputs and outputs), see the [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#options) in the Configuration section.

## [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#configuration)

- [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#options)

The following options control what data is captured from Google Gen AI SDK calls:

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#recordinputs)

*Type: `boolean` (optional)*

Records inputs to Google Gen AI SDK calls (such as prompts and messages).

Defaults to `true` if `sendDefaultPii` is `true`.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#recordoutputs)

*Type: `boolean` (optional)*

Records outputs from Google Gen AI SDK calls (such as generated text and responses).

Defaults to `true` if `sendDefaultPii` is `true`.

**Usage**

Using the `googleGenAIIntegration` integration:

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____",
  // Tracing must be enabled for agent monitoring to work
  tracesSampleRate: 1.0,
  integrations: [
    Sentry.googleGenAIIntegration({
      // your options here
    }),
  ],
});
```

Using the `instrumentGoogleGenAIClient` helper:

```javascript
const client = Sentry.instrumentGoogleGenAIClient(genAI, {
  // your options here
});
```

## [Supported Operations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#supported-operations)

By default, tracing support is added to the following Google Gen AI SDK calls:

* `models.generateContent()` - Generate content with a given model
* `models.generateContentStream()` - Stream content generation with a given model
* `chats.create()` - Create chat sessions
* `sendMessage()` - Send messages in chat sessions
* `sendMessageStream()` - Stream messages in chat sessions

Streaming and non-streaming requests are automatically detected and handled appropriately.

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#supported-versions)

* `@google/genai`: `>=0.10.0 <2`

