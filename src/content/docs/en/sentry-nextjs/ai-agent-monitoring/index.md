---
title: 'Set Up AI Agent Monitoring | Sentry for Next.js'
description: "With Sentry AI Agent Monitoring, you can monitor and debug your AI systems with full-stack context. You'll be able to track key insights like token us..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring

# Set Up AI Agent Monitoring | Sentry for Next.js

With [Sentry AI Agent Monitoring](https://docs.sentry.io/ai/monitoring/agents/dashboard.md), you can monitor and debug your AI systems with full-stack context. You'll be able to track key insights like token usage, latency, tool usage, and error rates. AI Agent Monitoring data will be fully connected to your other Sentry data like logs, errors, and traces.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#prerequisites)

Before setting up AI Agent Monitoring, ensure you have [tracing enabled](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md) in your Sentry configuration.

## [Automatic Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#automatic-instrumentation)

The JavaScript SDK supports automatic instrumentation for AI libraries. Add the integration for your AI library to your Sentry configuration:

* [Vercel AI SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)
* [OpenAI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md)
* [Anthropic](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md)
* [Google Gen AI SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md)
* [LangChain](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md)
* [LangGraph](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md)

```javascript
import * as Sentry from "___SDK_PACKAGE___";
import { openAIIntegration } from "___SDK_PACKAGE___";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
  integrations: [openAIIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#options)

- [Privacy Controls](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#privacy-controls)

All AI integrations support `recordInputs` and `recordOutputs` options to control whether prompts and responses are captured. Both default to `true`.

Set these to `false` if your prompts or responses contain sensitive data you don't want sent to Sentry.

```javascript
import * as Sentry from "___SDK_PACKAGE___";
import { openAIIntegration } from "___SDK_PACKAGE___";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
  integrations: [
    openAIIntegration({
      recordInputs: false, // Don't capture prompts
      recordOutputs: false, // Don't capture responses
    }),
  ],
});
```

## [Tracking Conversations](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#tracking-conversations)

Tracking Conversations has **alpha** stability. Configuration options and behavior may change.

When building AI applications with multi-turn conversations, you can use `setConversationId()` to link all AI spans from the same conversation together. This allows you to analyze entire conversation flows in Sentry.

The conversation ID is automatically applied as the `gen_ai.conversation.id` attribute to all AI-related spans within the current scope. To unset the conversation ID, pass `null`.

```javascript
import * as Sentry from "___SDK_PACKAGE___";

// Set conversation ID at the start of a conversation
Sentry.setConversationId("conv_abc123");

// All subsequent AI calls will be linked to this conversation
await openai.chat.completions.create({
  model: "gpt-4",
  messages: [{ role: "user", content: "Hello" }],
});

// Later in the conversation
await openai.chat.completions.create({
  model: "gpt-4",
  messages: [
    { role: "user", content: "Hello" },
    { role: "assistant", content: "Hi there!" },
    { role: "user", content: "What's the weather?" },
  ],
});

// Both calls will have gen_ai.conversation.id: "conv_abc123"

// To unset it
Sentry.setConversationId(null);
```

## [Manual Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#manual-instrumentation)

If you're using a library that Sentry does not automatically instrument, you can manually instrument your code to capture spans. For your AI agents data to show up in Sentry [AI Agents Insights](https://sentry.io/orgredirect/organizations/:orgslug/insights/ai/agents/), spans must have well-defined names and data attributes.

- [AI Request Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#ai-request-span)

This span represents a request to an LLM model or service that generates a response based on the input prompt.

**Key attributes:**

* `gen_ai.request.model` — The model name (required)
* `gen_ai.request.messages` — The prompts sent to the LLM
* `gen_ai.response.text` — The model's response
* `gen_ai.usage.input_tokens` / `output_tokens` — Token counts

```javascript
const messages = [{ role: "user", content: "Tell me a joke" }];

await Sentry.startSpan(
  {
    op: "gen_ai.request",
    name: "request o3-mini",
    attributes: {
      "gen_ai.request.model": "o3-mini",
      "gen_ai.request.messages": JSON.stringify(messages),
    },
  },
  async (span) => {
    // Call your LLM here
    const result = await client.chat.completions.create({
      model: "o3-mini",
      messages,
    });

    span.setAttribute(
      "gen_ai.response.text",
      JSON.stringify([result.choices[0].message.content]),
    );
    // Set token usage
    span.setAttribute(
      "gen_ai.usage.input_tokens",
      result.usage.prompt_tokens,
    );
    span.setAttribute(
      "gen_ai.usage.output_tokens",
      result.usage.completion_tokens,
    );
  },
);
```

AI Request span attributes

* The span `op` MUST be `"gen_ai.{gen_ai.operation.name}"`. (e.g. `"gen_ai.request"`)
* The span `name` SHOULD be `{gen_ai.operation.name} {gen_ai.request.model}"`. (e.g. `"chat o3-mini"`)
* All [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes) SHOULD be set (all `required` common attributes MUST be set).

Additional attributes on the span:

| Data Attribute                          | Type   | Requirement Level | Description                                                                          | Example                                                                                                           |
| --------------------------------------- | ------ | ----------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `gen_ai.request.available_tools`        | string | optional          | List of objects describing the available tools. **\[0]**                             | `"[{\"name\": \"random_number\", \"description\": \"...\"}, {\"name\": \"query_db\", \"description\": \"...\"}]"` |
| `gen_ai.request.frequency_penalty`      | float  | optional          | Model configuration parameter.                                                       | `0.5`                                                                                                             |
| `gen_ai.request.max_tokens`             | int    | optional          | Model configuration parameter.                                                       | `500`                                                                                                             |
| `gen_ai.request.messages`               | string | optional          | List of objects describing the messages (prompts) sent to the LLM **\[0]**, **\[1]** | `"[{\"role\": \"system\", \"content\": [{...}]}, {\"role\": \"system\", \"content\": [{...}]}]"`                  |
| `gen_ai.request.presence_penalty`       | float  | optional          | Model configuration parameter.                                                       | `0.5`                                                                                                             |
| `gen_ai.request.temperature`            | float  | optional          | Model configuration parameter.                                                       | `0.1`                                                                                                             |
| `gen_ai.request.top_p`                  | float  | optional          | Model configuration parameter.                                                       | `0.7`                                                                                                             |
| `gen_ai.response.tool_calls`            | string | optional          | The tool calls in the model's response. **\[0]**                                     | `"[{\"name\": \"random_number\", \"type\": \"function_call\", \"arguments\": \"...\"}]"`                          |
| `gen_ai.response.text`                  | string | optional          | The text representation of the model's responses. **\[0]**                           | `"[\"The weather in Paris is rainy\", \"The weather in London is sunny\"]"`                                       |
| `gen_ai.usage.input_tokens.cache_write` | int    | optional          | The number of tokens written to the cache when processing the AI input (prompt).     | `100`                                                                                                             |
| `gen_ai.usage.input_tokens.cached`      | int    | optional          | The number of cached tokens used in the AI input (prompt)                            | `50`                                                                                                              |
| `gen_ai.usage.input_tokens`             | int    | optional          | The number of tokens used in the AI input (prompt).                                  | `10`                                                                                                              |
| `gen_ai.usage.output_tokens.reasoning`  | int    | optional          | The number of tokens used for reasoning.                                             | `30`                                                                                                              |
| `gen_ai.usage.output_tokens`            | int    | optional          | The number of tokens used in the AI response.                                        | `100`                                                                                                             |
| `gen_ai.usage.total_tokens`             | int    | optional          | The total number of tokens used to process the prompt. (input and output)            | `190`                                                                                                             |

* **\[0]:** Span attributes only allow primitive data types. This means you need to use a stringified version of a list of dictionaries. Do NOT set `[{"foo": "bar"}]` but rather the string `"[{\"foo\": \"bar\"}]"`.
* **\[1]:** Each message item uses the format `{role:"", content:""}`. The `role` can be `"user"`, `"assistant"`, or `"system"`. The `content` can be either a string or a list of dictionaries.

- [Invoke Agent Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#invoke-agent-span)

This span represents the execution of an AI agent, capturing the full lifecycle from receiving a task to producing a final response.

**Key attributes:**

* `gen_ai.agent.name` — The agent's name (e.g., "Weather Agent")
* `gen_ai.request.model` — The underlying model used
* `gen_ai.response.text` — The agent's final output
* `gen_ai.usage.input_tokens` / `output_tokens` — Total token counts

```javascript
await Sentry.startSpan(
  {
    op: "gen_ai.invoke_agent",
    name: "invoke_agent Weather Agent",
    attributes: {
      "gen_ai.request.model": "o3-mini",
      "gen_ai.agent.name": "Weather Agent",
    },
  },
  async (span) => {
    // Run the agent
    const result = await myAgent.run();

    span.setAttribute(
      "gen_ai.response.text",
      JSON.stringify([result.output]),
    );
    // Set token usage
    span.setAttribute(
      "gen_ai.usage.input_tokens",
      result.usage.inputTokens,
    );
    span.setAttribute(
      "gen_ai.usage.output_tokens",
      result.usage.outputTokens,
    );
  },
);
```

Invoke Agent span attributes

Describes AI agent invocation.

* The spans `op` MUST be `"gen_ai.invoke_agent"`.
* The span `name` SHOULD be `"invoke_agent {gen_ai.agent.name}"`.
* The `gen_ai.operation.name` attribute MUST be `"invoke_agent"`.
* The `gen_ai.agent.name` attribute SHOULD be set to the agent's name. (e.g. `"Weather Agent"`)
* All [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes) SHOULD be set (all `required` common attributes MUST be set).

Additional attributes on the span:

| Data Attribute                          | Type   | Requirement Level | Description                                                                          | Example                                                                                                           |
| --------------------------------------- | ------ | ----------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `gen_ai.request.available_tools`        | string | optional          | List of objects describing the available tools. **\[0]**                             | `"[{\"name\": \"random_number\", \"description\": \"...\"}, {\"name\": \"query_db\", \"description\": \"...\"}]"` |
| `gen_ai.request.frequency_penalty`      | float  | optional          | Model configuration parameter.                                                       | `0.5`                                                                                                             |
| `gen_ai.request.max_tokens`             | int    | optional          | Model configuration parameter.                                                       | `500`                                                                                                             |
| `gen_ai.request.messages`               | string | optional          | List of objects describing the messages (prompts) sent to the LLM **\[0]**, **\[1]** | `"[{\"role\": \"system\", \"content\": [{...}]}, {\"role\": \"system\", \"content\": [{...}]}]"`                  |
| `gen_ai.request.presence_penalty`       | float  | optional          | Model configuration parameter.                                                       | `0.5`                                                                                                             |
| `gen_ai.request.temperature`            | float  | optional          | Model configuration parameter.                                                       | `0.1`                                                                                                             |
| `gen_ai.request.top_p`                  | float  | optional          | Model configuration parameter.                                                       | `0.7`                                                                                                             |
| `gen_ai.response.tool_calls`            | string | optional          | The tool calls in the model’s response. **\[0]**                                     | `"[{\"name\": \"random_number\", \"type\": \"function_call\", \"arguments\": \"...\"}]"`                          |
| `gen_ai.response.text`                  | string | optional          | The text representation of the model's responses. **\[0]**                           | `"[\"The weather in Paris is rainy\", \"The weather in London is sunny\"]"`                                       |
| `gen_ai.usage.input_tokens.cache_write` | int    | optional          | The number of tokens written to the cache when processing the AI input (prompt).     | `100`                                                                                                             |
| `gen_ai.usage.input_tokens.cached`      | int    | optional          | The number of cached tokens used in the AI input (prompt)                            | `50`                                                                                                              |
| `gen_ai.usage.input_tokens`             | int    | optional          | The number of tokens used in the AI input (prompt).                                  | `10`                                                                                                              |
| `gen_ai.usage.output_tokens.reasoning`  | int    | optional          | The number of tokens used for reasoning.                                             | `30`                                                                                                              |
| `gen_ai.usage.output_tokens`            | int    | optional          | The number of tokens used in the AI response.                                        | `100`                                                                                                             |
| `gen_ai.usage.total_tokens`             | int    | optional          | The total number of tokens used to process the prompt. (input and output)            | `190`                                                                                                             |

* **\[0]:** Span attributes only allow primitive data types (like `int`, `float`, `boolean`, `string`). This means you need to use a stringified version of a list of dictionaries. Do NOT set `[{"foo": "bar"}]` but rather the string `"[{\"foo\": \"bar\"}]"`.
* **\[1]:** Each message item uses the format `{role:"", content:""}`. The `role` can be `"user"`, `"assistant"`, or `"system"`. The `content` can be either a string or a list of dictionaries.

- [Execute Tool Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#execute-tool-span)

This span represents the execution of a tool or function that was requested by an AI model, including the input arguments and resulting output.

**Key attributes:**

* `gen_ai.tool.name` — The tool's name (e.g., "get\_weather")
* `gen_ai.tool.input` — The arguments passed to the tool
* `gen_ai.tool.output` — The tool's return value

```javascript
await Sentry.startSpan(
  {
    op: "gen_ai.execute_tool",
    name: "execute_tool get_weather",
    attributes: {
      "gen_ai.tool.name": "get_weather",
      "gen_ai.tool.input": JSON.stringify({ location: "Paris" }),
    },
  },
  async (span) => {
    // Call the tool
    const result = await getWeather({ location: "Paris" });

    span.setAttribute("gen_ai.tool.output", JSON.stringify(result));
  },
);
```

Execute Tool span attributes

Describes a tool execution.

* The span `op` MUST be `"gen_ai.execute_tool"`.
* The span `name` SHOULD be `"execute_tool {gen_ai.tool.name}"`. (e.g. `"execute_tool query_database"`)
* The `gen_ai.tool.name` attribute SHOULD be set to the name of the tool. (e.g. `"query_database"`)
* All [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes) SHOULD be set (all `required` common attributes MUST be set).

Additional attributes on the span:

| Data Attribute            | Type   | Requirement Level | Description                                          | Example                                    |
| ------------------------- | ------ | ----------------- | ---------------------------------------------------- | ------------------------------------------ |
| `gen_ai.tool.description` | string | optional          | Description of the tool executed.                    | `"Tool returning a random number"`         |
| `gen_ai.tool.input`       | string | optional          | Input that was given to the executed tool as string. | `"{\"max\":10}"`                           |
| `gen_ai.tool.name`        | string | optional          | Name of the tool executed.                           | `"random_number"`                          |
| `gen_ai.tool.output`      | string | optional          | The output from the tool.                            | `"7"`                                      |
| `gen_ai.tool.type`        | string | optional          | The type of the tools.                               | `"function"`; `"extension"`; `"datastore"` |

- [Handoff Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#handoff-span)

This span marks the transition of control from one agent to another, typically when the current agent determines another agent is better suited to handle the task.

**Requirements:**

* `op` must be `"gen_ai.handoff"`
* `name` should follow the pattern `"handoff from {source} to {target}"`
* All [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes) should be set

The handoff span itself has no body — it just marks the transition point before the target agent starts.

```javascript
await Sentry.startSpan(
  {
    op: "gen_ai.handoff",
    name: "handoff from Weather Agent to Travel Agent",
  },
  () => {}, // Handoff span just marks the transition
);

await Sentry.startSpan(
  { op: "gen_ai.invoke_agent", name: "invoke_agent Travel Agent" },
  async () => {
    // Run the target agent here
  },
);
```

## [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes)

Some attributes are common to all AI Agents spans:

| Data Attribute          | Type   | Requirement Level | Description                                          | Example           |
| ----------------------- | ------ | ----------------- | ---------------------------------------------------- | ----------------- |
| `gen_ai.request.model`  | string | required          | The name of the AI model a request is being made to. | `"o3-mini"`       |
| `gen_ai.operation.name` | string | optional          | The name of the operation being performed.           | `"summarize"`     |
| `gen_ai.agent.name`     | string | optional          | The name of the agent this span belongs to.          | `"Weather Agent"` |

## [Token Usage and Cost Gotchas](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#token-usage-and-cost-gotchas)

When manually setting token attributes, be aware of how Sentry uses them to [calculate model costs](https://docs.sentry.io/ai/monitoring/agents/costs.md).

**Cached and reasoning tokens are subsets, not separate counts.** `gen_ai.usage.input_tokens` is the **total** input token count that already includes any cached tokens. Similarly, `gen_ai.usage.output_tokens` already includes reasoning tokens. Sentry subtracts the cached/reasoning counts from the totals to compute the "raw" portion, so reporting them incorrectly can produce wrong or negative costs.

For example, say your LLM call uses 100 input tokens total, 90 of which were served from cache. Using a standard rate of $0.01 per token and a cached rate of $0.001 per token:

**Correct** — `input_tokens` is the total (includes cached):

* `gen_ai.usage.input_tokens = 100`
* `gen_ai.usage.input_tokens.cached = 90`
* Sentry calculates: `(100 - 90) × $0.01 + 90 × $0.001` = `$0.10 + $0.09` = **$0.19** ✓

**Wrong** — `input_tokens` set to only the non-cached tokens, making cached larger than total:

* `gen_ai.usage.input_tokens = 10`
* `gen_ai.usage.input_tokens.cached = 90`
* Sentry calculates: `(10 - 90) × $0.01 + 90 × $0.001` = `−$0.80 + $0.09` = **−$0.71**

Because `input_tokens.cached` (90) is larger than `input_tokens` (10), the subtraction goes negative, resulting in a negative total cost.

The same applies to `gen_ai.usage.output_tokens` and `gen_ai.usage.output_tokens.reasoning`.

## [Framework Exporters](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#framework-exporters)

If you're using an AI framework with a Sentry exporter, you can send traces to Sentry:

* [Mastra Sentry Exporter](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md)

## [MCP Server Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#mcp-server-monitoring)

If you're building MCP (Model Context Protocol) servers, Sentry can also track tool executions, prompt retrievals, and resource access. See [Instrument MCP Servers](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md) for setup instructions.

## Pages in this section

- [Mastra](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md)

