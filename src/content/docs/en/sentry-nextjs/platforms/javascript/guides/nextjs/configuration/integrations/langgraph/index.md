---
title: 'LangGraph | Sentry for Next.js'
description: 'For meta-framework applications using all runtimes, you need to manually wrap your compiled graph with . See instructions in the Browser-Side Usage se...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph

# LangGraph | Sentry for Next.js

## [Server-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#server-side-usage)

For meta-framework applications using all runtimes, you need to manually wrap your compiled graph with `instrumentLangGraph`. See instructions in the [Browser-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#browser-side-usage) section.

## [Browser-Side Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#browser-side-usage)

*Import name: `Sentry.instrumentLangGraph`*

The `instrumentLangGraph` helper adds instrumentation for [`@langchain/langgraph`](https://www.npmjs.com/package/@langchain/langgraph) to capture spans by wrapping a compiled LangGraph graph and recording AI agent interactions with configurable input/output recording. You need to manually wrap your compiled graph with this helper. See example below:

```javascript
import { ChatOpenAI } from "@langchain/openai";
import {
  StateGraph,
  MessagesAnnotation,
  START,
  END,
} from "@langchain/langgraph";

// Create LLM call
const llm = new ChatOpenAI({
  modelName: "gpt-4o",
  apiKey: "your-api-key", // Warning: API key will be exposed in browser!
});

async function callLLM(state) {
  const response = await llm.invoke(state.messages);

  return {
    messages: [...state.messages, response],
  };
}

// Create the agent
const agent = new StateGraph(MessagesAnnotation)
  .addNode("agent", callLLM)
  .addEdge(START, "agent")
  .addEdge("agent", END);

const graph = agent.compile({ name: "my_agent" });

// Manually instrument the graph
Sentry.instrumentLangGraph(graph, {
  recordInputs: true,
  recordOutputs: true,
});

// Invoke the agent
const result = await graph.invoke({
  messages: [
    new SystemMessage("You are a helpful assistant."),
    new HumanMessage("Hello!"),
  ],
});
```

To customize what data is captured (such as inputs and outputs), see the [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#options) in the Configuration section.

## [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#configuration)

- [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#options)

The following options control what data is captured from LangGraph operations:

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#recordinputs)

*Type: `boolean` (optional)*

Records inputs to LangGraph operations (such as messages and state data passed to the graph).

Defaults to `true` if `sendDefaultPii` is `true`.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#recordoutputs)

*Type: `boolean` (optional)*

Records outputs from LangGraph operations (such as generated responses, agent outputs, and final state).

Defaults to `true` if `sendDefaultPii` is `true`.

**Usage**

Using the `langGraphIntegration` integration:

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____",
  // Tracing must be enabled for agent monitoring to work
  tracesSampleRate: 1.0,
  integrations: [
    Sentry.langGraphIntegration({
      // your options here
    }),
  ],
});
```

Using the `instrumentLangGraph` helper:

```javascript
Sentry.instrumentLangGraph(graph, {
  // your options here
});
```

## [Supported Operations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#supported-operations)

By default, tracing support is added to the following LangGraph SDK calls:

* **Agent Creation** (`gen_ai.create_agent`) - Captures spans when compiling a StateGraph into an executable agent
* **Agent Invocation** (`gen_ai.invoke_agent`) - Captures spans for agent execution via `invoke()`

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#supported-versions)

* `@langchain/langgraph`: `>=0.2.0 <2.0.0`

