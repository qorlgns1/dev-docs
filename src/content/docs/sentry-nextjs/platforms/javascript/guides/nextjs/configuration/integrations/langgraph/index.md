---
title: 'LangGraph | Next.js용 Sentry'
description: '모든 런타임을 사용하는 메타 프레임워크 애플리케이션에서는 컴파일된 그래프를 로 수동 래핑해야 합니다. 브라우저 측 사용 섹션의 안내를 참고하세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph

# LangGraph | Next.js용 Sentry

## [서버 측 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#server-side-usage)

모든 런타임을 사용하는 메타 프레임워크 애플리케이션에서는 컴파일된 그래프를 `instrumentLangGraph`로 수동 래핑해야 합니다. [브라우저 측 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#browser-side-usage) 섹션의 안내를 참고하세요.

## [브라우저 측 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#browser-side-usage)

*가져오기 이름: `Sentry.instrumentLangGraph`*

`instrumentLangGraph` 헬퍼는 컴파일된 LangGraph 그래프를 래핑하고, 설정 가능한 입력/출력 기록으로 AI 에이전트 상호작용을 기록해 스팬을 수집하도록 [`@langchain/langgraph`](https://www.npmjs.com/package/@langchain/langgraph)에 대한 계측을 추가합니다. 이 헬퍼로 컴파일된 그래프를 수동으로 래핑해야 합니다. 아래 예시를 참고하세요:

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

어떤 데이터를 수집할지(예: 입력 및 출력) 사용자 지정하려면 Configuration 섹션의 [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#options)를 참고하세요.

## [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#configuration)

- [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#options)

다음 옵션은 LangGraph 작업에서 어떤 데이터를 수집할지 제어합니다:

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#recordinputs)

*유형: `boolean` (선택 사항)*

LangGraph 작업에 대한 입력(예: 그래프에 전달되는 메시지 및 상태 데이터)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#recordoutputs)

*유형: `boolean` (선택 사항)*

LangGraph 작업의 출력(예: 생성된 응답, 에이전트 출력, 최종 상태)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

**사용법**

`langGraphIntegration` 통합 사용:

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

`instrumentLangGraph` 헬퍼 사용:

```javascript
Sentry.instrumentLangGraph(graph, {
  // your options here
});
```

## [지원되는 작업](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#supported-operations)

기본적으로 다음 LangGraph SDK 호출에 추적 지원이 추가됩니다:

* **에이전트 생성** (`gen_ai.create_agent`) - StateGraph를 실행 가능한 에이전트로 컴파일할 때 스팬을 수집합니다
* **에이전트 호출** (`gen_ai.invoke_agent`) - `invoke()`를 통한 에이전트 실행의 스팬을 수집합니다

## [지원되는 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md#supported-versions)

* `@langchain/langgraph`: `>=0.2.0 <2.0.0`

