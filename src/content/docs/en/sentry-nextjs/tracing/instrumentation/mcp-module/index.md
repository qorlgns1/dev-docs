---
title: 'Instrument MCP Servers | Sentry for Next.js'
description: "With Sentry's MCP monitoring, you can track and debug MCP servers with full-stack context. You'll be able to monitor tool executions, prompt retrieval..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module

# Instrument MCP Servers | Sentry for Next.js

With Sentry's [MCP monitoring](https://docs.sentry.io/ai/monitoring/mcp.md), you can track and debug MCP servers with full-stack context. You'll be able to monitor tool executions, prompt retrievals, resource access, and error rates. MCP monitoring data will be fully connected to your other Sentry data like logs, errors, and traces.

As a prerequisite to setting up MCP monitoring with JavaScript, you'll need to first [set up tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md). Once this is done, the JavaScript SDK will automatically instrument MCP servers created with supported libraries. If that doesn't fit your use case, you can use custom instrumentation described below.

## [Automatic Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#automatic-instrumentation)

The JavaScript SDK supports automatic instrumentation for MCP servers. We recommend adding the MCP integration to your Sentry configuration to automatically capture spans for MCP operations.

* [MCP (Model Context Protocol)](https://docs.sentry.io/ai/monitoring/mcp/getting-started.md)

## [Manual Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#manual-instrumentation)

For your MCP data to show up in Sentry, spans must be created with well-defined names and data attributes. See below for the different types of MCP operations you can instrument.

The [Sentry.startSpan()](https://docs.sentry.io/platforms/javascript/tracing/instrumentation/custom-instrumentation.md#starting-a-span) method can be used to create these spans.

## [Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#spans)

- [Tool Execution Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#tool-execution-span)

Describes MCP tool execution.

The [@sentry\_sdk.trace()](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md#span-templates) decorator can also be used to create this span.

* The span's `op` MUST be `"mcp.server"`.
* The span `name` SHOULD be `"tools/call {mcp.tool.name}"`.
* The `mcp.tool.name` attribute MUST be set to the tool's name. (e.g. `"get_weather"`)
* The `mcp.method.name` attribute SHOULD be set to `"tools/call"`.
* All [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#common-span-attributes) SHOULD be set.

Additional attributes on the span:

| Data Attribute                  | Type    | Requirement Level | Description                                              | Example                                           |
| ------------------------------- | ------- | ----------------- | -------------------------------------------------------- | ------------------------------------------------- |
| `mcp.tool.name`                 | string  | required          | The name of the MCP tool being called.                   | `"get_weather"`                                   |
| `mcp.method.name`               | string  | recommended       | Should be set to "tools/call".                           | `"tools/call"`                                    |
| `mcp.request.id`                | string  | optional          | The unique identifier for the MCP request.               | `"req_123abc"`                                    |
| `mcp.request.argument.*`        | any     | optional          | Tool input arguments (requires `send_default_pii=True`). | `"San Francisco"` for `mcp.request.argument.city` |
| `mcp.tool.result.content`       | string  | optional          | The result/output content from the tool execution.       | `"The weather is sunny"`                          |
| `mcp.tool.result.content_count` | int     | optional          | The number of items/keys in the tool result.             | `5`                                               |
| `mcp.tool.result.is_error`      | boolean | optional          | Whether the tool execution resulted in an error.         | `True`                                            |

#
- [Example Tool Execution Span:](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#example-tool-execution-span)

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  // ... your Sentry configuration
});

// Example tool execution
const toolName = "get_weather";
const toolArguments = { city: "San Francisco" };

await Sentry.startSpan(
  {
    op: "mcp.server",
    name: `tools/call ${toolName}`,
  },
  async (span) => {
    // Set MCP-specific attributes
    span.setAttribute("mcp.tool.name", toolName);
    span.setAttribute("mcp.method.name", "tools/call");

    // Set request metadata
    span.setAttribute("mcp.request.id", "req_123abc");
    span.setAttribute("mcp.session.id", "session_xyz789");
    span.setAttribute("mcp.transport", "stdio"); // or "http", "sse" for HTTP/WebSocket/SSE
    span.setAttribute("network.transport", "pipe"); // or "tcp" for HTTP/SSE

    // Set tool arguments (optional, requires recordInputs: true)
    for (const [key, value] of Object.entries(toolArguments)) {
      span.setAttribute(`mcp.request.argument.${key}`, value);
    }

    // Execute the tool
    try {
      const result = executeTool(toolName, toolArguments);

      // Set result data
      span.setAttribute("mcp.tool.result.content", JSON.stringify(result));
      span.setAttribute("mcp.tool.result.is_error", false);

      // Set result content count if applicable
      if (
        Array.isArray(result) ||
        (typeof result === "object" && result !== null)
      ) {
        span.setAttribute(
          "mcp.tool.result.content_count",
          Array.isArray(result)
            ? result.length
            : Object.keys(result).length,
        );
      }
    } catch (error) {
      span.setAttribute("mcp.tool.result.is_error", true);
      throw error;
    }
  },
);
```

- [Prompt Retrieval Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#prompt-retrieval-span)

Describes MCP prompt retrieval.

The [@sentry\_sdk.trace()](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md#span-templates) decorator can also be used to create this span.

* The span's `op` MUST be `"mcp.server"`.
* The span `name` SHOULD be `"prompts/get {mcp.prompt.name}"`.
* The `mcp.prompt.name` attribute MUST be set to the prompt's name. (e.g. `"code_review"`)
* The `mcp.method.name` attribute SHOULD be set to `"prompts/get"`.
* All [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#common-span-attributes) SHOULD be set.

Additional attributes on the span:

| Data Attribute                      | Type   | Requirement Level | Description                                                                       | Example                                        |
| ----------------------------------- | ------ | ----------------- | --------------------------------------------------------------------------------- | ---------------------------------------------- |
| `mcp.prompt.name`                   | string | required          | The name of the MCP prompt being retrieved.                                       | `"code_review"`                                |
| `mcp.method.name`                   | string | recommended       | Should be set to "prompts/get".                                                   | `"prompts/get"`                                |
| `mcp.request.id`                    | string | optional          | The unique identifier for the MCP request.                                        | `"req_456def"`                                 |
| `mcp.request.argument.*`            | any    | optional          | Prompt input arguments (requires `send_default_pii=True`).                        | `"python"` for `mcp.request.argument.language` |
| `mcp.prompt.result.message_content` | string | optional          | The message content from the prompt retrieval (requires `send_default_pii=True`). | `"Review the following code..."`               |
| `mcp.prompt.result.message_role`    | string | optional          | The role of the message (only for single-message prompts).                        | `"user"`, `"assistant"`, `"system"`            |
| `mcp.prompt.result.message_count`   | int    | optional          | The number of messages in the prompt result.                                      | `1`, `3`                                       |

#
- [Example Prompt Retrieval Span:](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#example-prompt-retrieval-span)

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  // ... your Sentry configuration
});

// Example prompt retrieval
const promptName = "code_review";
const promptArguments = { language: "python" };

await Sentry.startSpan(
  {
    op: "mcp.server",
    name: `prompts/get ${promptName}`,
  },
  async (span) => {
    // Set MCP-specific attributes
    span.setAttribute("mcp.prompt.name", promptName);
    span.setAttribute("mcp.method.name", "prompts/get");

    // Set request metadata
    span.setAttribute("mcp.request.id", "req_456def");
    span.setAttribute("mcp.session.id", "session_xyz789");
    span.setAttribute("mcp.transport", "http");
    span.setAttribute("network.transport", "tcp");

    // Set prompt arguments (optional, requires recordInputs: true)
    for (const [key, value] of Object.entries(promptArguments)) {
      span.setAttribute(`mcp.request.argument.${key}`, value);
    }

    // Retrieve the prompt
    const promptResult = getPrompt(promptName, promptArguments);

    // Set result data
    const messages = promptResult.messages || [];
    span.setAttribute("mcp.prompt.result.message_count", messages.length);

    // For single-message prompts, set role and content
    if (messages.length === 1) {
      span.setAttribute(
        "mcp.prompt.result.message_role",
        messages[0].role,
      );
      // Content may contain sensitive data, only set if recordOutputs: true
      span.setAttribute(
        "mcp.prompt.result.message_content",
        JSON.stringify(messages[0].content),
      );
    }
  },
);
```

- [Resource Read Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#resource-read-span)

Describes MCP resource access.

The [@sentry\_sdk.trace()](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md#span-templates) decorator can also be used to create this span.

* The span's `op` MUST be `"mcp.server"`.
* The span `name` SHOULD be `"resources/read {mcp.resource.uri}"`.
* The `mcp.resource.uri` attribute MUST be set to the resource's URI. (e.g. `"file:///path/to/resource"`)
* The `mcp.method.name` attribute SHOULD be set to `"resources/read"`.
* All [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#common-span-attributes) SHOULD be set.

Additional attributes on the span:

| Data Attribute          | Type   | Requirement Level | Description                                  | Example                       |
| ----------------------- | ------ | ----------------- | -------------------------------------------- | ----------------------------- |
| `mcp.resource.uri`      | string | required          | The URI of the MCP resource being accessed.  | `"file:///path/to/resource"`  |
| `mcp.method.name`       | string | recommended       | Should be set to "resources/read"            | `"resources/read"`            |
| `mcp.request.id`        | string | optional          | The unique identifier for the MCP request.   | `"req_789ghi"`                |
| `mcp.resource.protocol` | string | optional          | The protocol/scheme of the MCP resource URI. | `"file"`, `"http"`, `"https"` |

#
- [Example Resource Read Span:](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#example-resource-read-span)

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  // ... your Sentry configuration
});

// Example resource access
const resourceUri = "file:///path/to/resource.txt";

await Sentry.startSpan(
  {
    op: "mcp.server",
    name: `resources/read ${resourceUri}`,
  },
  async (span) => {
    // Set MCP-specific attributes
    span.setAttribute("mcp.resource.uri", resourceUri);
    span.setAttribute("mcp.method.name", "resources/read");

    // Set request metadata
    span.setAttribute("mcp.request.id", "req_789ghi");
    span.setAttribute("mcp.session.id", "session_xyz789");
    span.setAttribute("mcp.transport", "http");
    span.setAttribute("network.transport", "tcp");

    // Access the resource
    const resourceData = readResource(resourceUri);
  },
);
```

## [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#common-span-attributes)

The following attributes are common across all MCP span types and SHOULD be set when available:

| Data Attribute      | Type   | Requirement Level | Description                                      | Example                    |
| ------------------- | ------ | ----------------- | ------------------------------------------------ | -------------------------- |
| `mcp.transport`     | string | recommended       | The transport method used for MCP communication. | `"stdio"`, `"sse", "http"` |
| `network.transport` | string | recommended       | The network transport used.                      | `"pipe"`, `"tcp"`          |
| `mcp.session.id`    | string | recommended       | The session identifier for the MCP connection.   | `"a1b2c3d4e5f6"`           |
| `mcp.request.id`    | string | optional          | The unique identifier for the MCP request.       | `"req_123abc"`             |

