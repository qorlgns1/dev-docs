---
title: 'Anthropic | Sentry for Next.js'
description: 'For meta-framework applications using all runtimes, you need to manually wrap your Anthropic client instance with . See instructions in the Browser-Si...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic

# Anthropic | Sentry for Next.js

## [Server-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#server-side-usage)

For meta-framework applications using all runtimes, you need to manually wrap your Anthropic client instance with `instrumentAnthropicAiClient`. See instructions in the [Browser-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#browser-side-usage) section.

## [Browser-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#browser-side-usage)

*Import name: `Sentry.instrumentAnthropicAiClient`*

The `instrumentAnthropicAiClient` helper adds instrumentation for the [`@anthropic-ai/sdk`](https://www.npmjs.com/package/@anthropic-ai/sdk) API to capture spans by wrapping Anthropic SDK calls and recording LLM interactions with configurable input/output recording. You need to manually wrap your Anthropic client instance with this helper. See example below:

```javascript
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  apiKey: "your-api-key", // Warning: API key will be exposed in browser!
});

const client = Sentry.instrumentAnthropicAiClient(anthropic, {
  recordInputs: true,
  recordOutputs: true,
});

// Use the wrapped client instead of the original anthropic instance
const response = await client.messages.create({
  model: "claude-3-5-sonnet-20241022",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

To customize what data is captured (such as inputs and outputs), see the [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#options) in the Configuration section.

## [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#configuration)

- [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#options)

The following options control what data is captured from Anthropic SDK calls:

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#recordinputs)

*Type: `boolean` (optional)*

Records inputs to Anthropic SDK calls (such as prompts and messages).

Defaults to `true` if `sendDefaultPii` is `true`.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#recordoutputs)

*Type: `boolean` (optional)*

Records outputs from Anthropic SDK calls (such as generated text and responses).

Defaults to `true` if `sendDefaultPii` is `true`.

**Usage**

Using the `anthropicAIIntegration` integration:

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____",
  // Tracing must be enabled for agent monitoring to work
  tracesSampleRate: 1.0,
  integrations: [
    Sentry.anthropicAIIntegration({
      // your options here
    }),
  ],
});
```

Using the `instrumentAnthropicAiClient` helper:

```javascript
const client = Sentry.instrumentAnthropicAiClient(anthropic, {
  // your options here
});
```

## [Supported Operations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#supported-operations)

By default, tracing support is added to the following Anthropic SDK calls:

* `messages.create()` - Create messages with Claude models
* `messages.stream()` - Stream messages with Claude models
* `messages.countTokens()` - Count tokens for messages
* `models.get()` - Get model information
* `completions.create()` - Create completions (legacy)
* `models.retrieve()` - Retrieve model details
* `beta.messages.create()` - Beta messages API

Streaming and non-streaming requests are automatically detected and handled appropriately.

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#supported-versions)

* `@anthropic-ai/sdk`: `>=0.19.2 <1.0.0`

