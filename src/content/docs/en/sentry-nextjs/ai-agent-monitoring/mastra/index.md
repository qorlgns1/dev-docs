---
title: 'Mastra | Sentry for Next.js'
description: 'This is a server-side exporter for Mastra AI tracing that uses the Node.js Sentry SDK. It requires Node.js or compatible runtimes. Requires  package.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra

# Mastra | Sentry for Next.js

This is a server-side exporter for Mastra AI tracing that uses the Node.js Sentry SDK. It requires Node.js or compatible runtimes. Requires `@mastra/sentry@beta` package.

[Mastra](https://mastra.ai/) is a framework for building AI-powered applications and agents with a modern TypeScript stack. The Mastra Sentry Exporter sends tracing data to Sentry using OpenTelemetry semantic conventions, providing insights into model performance, token usage, and tool executions.

## [Installation](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#installation)

Install the Mastra Sentry exporter package:

```bash
npm install @mastra/sentry@beta
```

## [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#configuration)

- [Zero-Config Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#zero-config-setup)

The Sentry exporter can automatically read configuration from environment variables:

```javascript
import { SentryExporter } from "@mastra/sentry";

// Reads from SENTRY_DSN, SENTRY_ENVIRONMENT, SENTRY_RELEASE
const exporter = new SentryExporter();
```

- [Explicit Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#explicit-configuration)

You can also configure the exporter explicitly:

```javascript
import { SentryExporter } from "@mastra/sentry";

const exporter = new SentryExporter({
  dsn: process.env.SENTRY_DSN,
  environment: "production",
  tracesSampleRate: 1.0,
  release: "1.0.0",
});
```

Span Mapping

Mastra automatically maps its span types to Sentry operations for proper visualization in Sentry's AI monitoring dashboards:

| Mastra Span Type       | Sentry Operation       |
| ---------------------- | ---------------------- |
| `AGENT_RUN`            | `gen_ai.invoke_agent`  |
| `MODEL_GENERATION`     | `gen_ai.chat`          |
| `TOOL_CALL`            | `gen_ai.execute_tool`  |
| `MCP_TOOL_CALL`        | `gen_ai.execute_tool`  |
| `WORKFLOW_RUN`         | `workflow.run`         |
| `WORKFLOW_STEP`        | `workflow.step`        |
| `WORKFLOW_CONDITIONAL` | `workflow.conditional` |
| `WORKFLOW_PARALLEL`    | `workflow.parallel`    |
| `WORKFLOW_LOOP`        | `workflow.loop`        |
| `PROCESSOR_RUN`        | `ai.processor`         |
| `GENERIC`              | `ai.span`              |

**Note:** `MODEL_STEP` and `MODEL_CHUNK` spans are automatically skipped to simplify trace hierarchy. Their data is aggregated into parent `MODEL_GENERATION` spans.

Captured Data

The Sentry exporter captures comprehensive trace data following OpenTelemetry semantic conventions:

#
- [Common Attributes (All spans)](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#common-attributes-all-spans)

* `sentry.origin`: `auto.ai.mastra` (identifies spans from Mastra)
* `ai.span.type`: Mastra span type

#
- [Model Generation Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#model-generation-spans)

* `gen_ai.operation.name`: Operation name (e.g., `chat`)
* `gen_ai.system`: Model provider (e.g., OpenAI, Anthropic)
* `gen_ai.request.model`: Model identifier
* `gen_ai.request.messages`: Input messages/prompts (JSON)
* `gen_ai.response.model`: Response model
* `gen_ai.response.text`: Output text
* `gen_ai.response.tool_calls`: Tool calls made during generation
* `gen_ai.usage.input_tokens`: Input token count
* `gen_ai.usage.output_tokens`: Output token count
* `gen_ai.usage.total_tokens`: Total tokens used
* `gen_ai.request.stream`: Whether streaming was used
* `gen_ai.request.temperature`: Temperature parameter
* `gen_ai.completion_start_time`: Time to first token

#
- [Tool Call Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#tool-call-spans)

* `gen_ai.operation.name`: `execute_tool`
* `gen_ai.tool.name`: Tool identifier
* `gen_ai.tool.type`: `function`
* `gen_ai.tool.call.id`: Tool call ID
* `gen_ai.tool.input`: Tool input parameters
* `gen_ai.tool.output`: Tool output result
* `tool.success`: Success flag

#
- [Agent Run Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#agent-run-spans)

* `gen_ai.operation.name`: `invoke_agent`
* `gen_ai.agent.name`: Agent identifier
* `gen_ai.pipeline.name`: Agent name
* `gen_ai.agent.instructions`: Agent instructions/system prompt
* `gen_ai.response.model`: Model from child generation
* `gen_ai.response.text`: Output from child generation
* `gen_ai.usage.*`: Token usage aggregated from child spans

## [Methods](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#methods)

- [`exportTracingEvent()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#exporttracingevent)

Exports a tracing event to Sentry. Handles `SPAN_STARTED`, `SPAN_UPDATED`, and `SPAN_ENDED` events.

```javascript
await exporter.exportTracingEvent(event);
```

- [`flush()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#flush)

Force flushes any pending spans to Sentry without shutting down the exporter. Waits up to 2 seconds for pending data to be sent. Useful in serverless environments where you need to ensure spans are exported before the runtime terminates.

```javascript
await exporter.flush();
```

- [`shutdown()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#shutdown)

Ends all active spans, clears internal state, and closes the Sentry connection. Waits up to 2 seconds for pending data to be sent.

```javascript
await exporter.shutdown();
```

## [Learn More](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#learn-more)

For complete documentation on using Mastra with Sentry, see the [Mastra Sentry Exporter documentation](https://mastra.ai/docs/observability/tracing/exporters/sentry).

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#supported-versions)

* `@mastra/sentry`: `>=1.0.0-beta.2`

