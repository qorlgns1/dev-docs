---
title: 'OpenAI | Sentry for Next.js'
description: 'For meta-framework applications using all runtimes, you need to manually wrap your OpenAI client instance with . See instructions in the Browser-Side ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai

# OpenAI | Sentry for Next.js

## [Server-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#server-side-usage)

For meta-framework applications using all runtimes, you need to manually wrap your OpenAI client instance with `instrumentOpenAiClient`. See instructions in the [Browser-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#browser-side-usage) section.

## [Browser-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#browser-side-usage)

*Import name: `Sentry.instrumentOpenAiClient`*

The `instrumentOpenAiClient` helper adds instrumentation for the [`openai`](https://www.npmjs.com/package/openai) SDK to capture spans by wrapping OpenAI SDK calls and recording LLM interactions with configurable input/output recording. You need to manually wrap your OpenAI client instance with this helper:

```javascript
import OpenAI from "openai";

const openai = new OpenAI({
  // Warning: API key will be exposed in browser!
  apiKey: "your-api-key",
});

const client = Sentry.instrumentOpenAiClient(openai, {
  recordInputs: true,
  recordOutputs: true,
});

// Use the wrapped client instead of the original openai instance
const response = await client.chat.completions.create({
  model: "gpt-4o",
  messages: [{ role: "user", content: "Hello!" }],
});
```

To customize what data is captured (such as inputs and outputs), see the [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#options) in the Configuration section.

## [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#configuration)

- [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#options)

The following options control what data is captured from OpenAI SDK calls:

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#recordinputs)

*Type: `boolean` (optional)*

Records inputs to OpenAI SDK calls (such as prompts and messages).

Defaults to `true` if `sendDefaultPii` is `true`.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#recordoutputs)

*Type: `boolean` (optional)*

Records outputs from OpenAI SDK calls (such as generated text and responses).

Defaults to `true` if `sendDefaultPii` is `true`.

**Usage**

Using the `openAIIntegration` integration:

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____",
  // Tracing must be enabled for agent monitoring to work
  tracesSampleRate: 1.0,
  integrations: [
    Sentry.openAIIntegration({
      // your options here
    }),
  ],
});
```

Using the `instrumentOpenAiClient` helper:

```javascript
const client = Sentry.instrumentOpenAiClient(openai, {
  // your options here
});
```

## [Supported Operations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#supported-operations)

By default, tracing support is added to the following OpenAI SDK calls:

* `chat.completions.create()` - Chat completion requests
* `responses.create()` - Response SDK requests

Streaming and non-streaming requests are automatically detected and handled appropriately.

When using OpenAI's streaming API, you must also pass `stream_options: { include_usage: true }` to receive token usage data. Without this option, OpenAI does not include `prompt_tokens` or `completion_tokens` in streamed responses, and Sentry will be unable to capture `gen_ai.usage.input_tokens` / `gen_ai.usage.output_tokens` on the resulting span. This is an OpenAI API behavior, not a Sentry limitation. See [OpenAI docs on stream options](https://platform.openai.com/docs/api-reference/chat/create#chat-create-stream_options).

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#supported-versions)

* `openai`: `>=4.0.0 <7`

