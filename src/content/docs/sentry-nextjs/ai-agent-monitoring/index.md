---
title: 'AI Agent Monitoring 설정 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring

# AI Agent Monitoring 설정 | Next.js용 Sentry

[Sentry AI Agent Monitoring](https://docs.sentry.io/ai/monitoring/agents/dashboard.md)을 사용하면 전체 스택 컨텍스트와 함께 AI 시스템을 모니터링하고 디버그할 수 있습니다. 토큰 사용량, 지연 시간, 도구 사용량, 오류율 같은 핵심 인사이트를 추적할 수 있습니다. AI Agent Monitoring 데이터는 로그, 오류, 트레이스 같은 다른 Sentry 데이터와 완전히 연결됩니다.

## [사전 요구 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#prerequisites)

AI Agent Monitoring을 설정하기 전에 Sentry 구성에서 [tracing enabled](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)가 되어 있는지 확인하세요.

## [자동 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#automatic-instrumentation)

JavaScript SDK는 AI 라이브러리에 대한 자동 계측을 지원합니다. 사용 중인 AI 라이브러리의 integration을 Sentry 구성에 추가하세요:

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

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#options)

- [개인정보 보호 제어](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#privacy-controls)

모든 AI integration은 프롬프트와 응답을 수집할지 제어하는 `recordInputs` 및 `recordOutputs` 옵션을 지원합니다. 두 옵션의 기본값은 `true`입니다.

프롬프트나 응답에 Sentry로 전송하고 싶지 않은 민감한 데이터가 포함되어 있다면 이 값을 `false`로 설정하세요.

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

## [대화 추적](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#tracking-conversations)

대화 추적은 **alpha** 안정성 단계입니다. 구성 옵션과 동작은 변경될 수 있습니다.

멀티턴 대화를 사용하는 AI 애플리케이션을 구축할 때는 `setConversationId()`를 사용해 같은 대화에서 발생한 모든 AI span을 서로 연결할 수 있습니다. 이를 통해 Sentry에서 전체 대화 흐름을 분석할 수 있습니다.

대화 ID는 현재 scope 내의 모든 AI 관련 span에 `gen_ai.conversation.id` 속성으로 자동 적용됩니다. 대화 ID를 해제하려면 `null`을 전달하세요.

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

## [수동 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#manual-instrumentation)

Sentry가 자동으로 계측하지 않는 라이브러리를 사용 중이라면, span을 수집하도록 코드를 수동 계측할 수 있습니다. AI 에이전트 데이터가 Sentry [AI Agents Insights](https://sentry.io/orgredirect/organizations/:orgslug/insights/ai/agents/)에 표시되려면, span에 잘 정의된 이름과 데이터 속성이 있어야 합니다.

- [AI Request Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#ai-request-span)

이 span은 입력 프롬프트를 기반으로 응답을 생성하는 LLM 모델 또는 서비스로의 요청을 나타냅니다.

**핵심 속성:**

* `gen_ai.request.model` — 모델 이름(필수)
* `gen_ai.request.messages` — LLM에 전송된 프롬프트
* `gen_ai.response.text` — 모델의 응답
* `gen_ai.usage.input_tokens` / `output_tokens` — 토큰 수

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

AI Request span 속성

* span `op`는 반드시 `"gen_ai.{gen_ai.operation.name}"`여야 합니다. (예: `"gen_ai.request"`)
* span `name`은 `{gen_ai.operation.name} {gen_ai.request.model}"`이어야 합니다. (예: `"chat o3-mini"`)
* 모든 [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes)를 설정해야 합니다 (`required` 공통 속성은 모두 반드시 설정).

span의 추가 속성:

| 데이터 속성                              | 타입   | 요구 수준        | 설명                                                                                 | 예시                                                                                                              |
| --------------------------------------- | ------ | ---------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `gen_ai.request.available_tools`        | string | optional         | 사용 가능한 도구를 설명하는 객체 목록. **\[0]**                                      | `"[{\"name\": \"random_number\", \"description\": \"...\"}, {\"name\": \"query_db\", \"description\": \"...\"}]"` |
| `gen_ai.request.frequency_penalty`      | float  | optional         | 모델 구성 파라미터.                                                                  | `0.5`                                                                                                             |
| `gen_ai.request.max_tokens`             | int    | optional         | 모델 구성 파라미터.                                                                  | `500`                                                                                                             |
| `gen_ai.request.messages`               | string | optional         | LLM에 전송된 메시지(프롬프트)를 설명하는 객체 목록 **\[0]**, **\[1]**                | `"[{\"role\": \"system\", \"content\": [{...}]}, {\"role\": \"system\", \"content\": [{...}]}]"`                  |
| `gen_ai.request.presence_penalty`       | float  | optional         | 모델 구성 파라미터.                                                                  | `0.5`                                                                                                             |
| `gen_ai.request.temperature`            | float  | optional         | 모델 구성 파라미터.                                                                  | `0.1`                                                                                                             |
| `gen_ai.request.top_p`                  | float  | optional         | 모델 구성 파라미터.                                                                  | `0.7`                                                                                                             |
| `gen_ai.response.tool_calls`            | string | optional         | 모델 응답의 tool call. **\[0]**                                                      | `"[{\"name\": \"random_number\", \"type\": \"function_call\", \"arguments\": \"...\"}]"`                          |
| `gen_ai.response.text`                  | string | optional         | 모델 응답의 텍스트 표현. **\[0]**                                                    | `"[\"The weather in Paris is rainy\", \"The weather in London is sunny\"]"`                                       |
| `gen_ai.usage.input_tokens.cache_write` | int    | optional         | AI 입력(프롬프트) 처리 시 캐시에 기록된 토큰 수.                                     | `100`                                                                                                             |
| `gen_ai.usage.input_tokens.cached`      | int    | optional         | AI 입력(프롬프트)에서 사용된 캐시 토큰 수                                             | `50`                                                                                                              |
| `gen_ai.usage.input_tokens`             | int    | optional         | AI 입력(프롬프트)에서 사용된 토큰 수.                                                 | `10`                                                                                                              |
| `gen_ai.usage.output_tokens.reasoning`  | int    | optional         | 추론에 사용된 토큰 수.                                                               | `30`                                                                                                              |
| `gen_ai.usage.output_tokens`            | int    | optional         | AI 응답에서 사용된 토큰 수.                                                          | `100`                                                                                                             |
| `gen_ai.usage.total_tokens`             | int    | optional         | 프롬프트 처리에 사용된 전체 토큰 수(입력 + 출력).                                    | `190`                                                                                                             |

* **\[0]:** Span 속성은 원시 데이터 타입만 허용합니다. 즉, 딕셔너리 목록의 문자열화된 버전을 사용해야 합니다. `[{"foo": "bar"}]`를 설정하지 말고 문자열 `"[{\"foo\": \"bar\"}]"`를 설정하세요.
* **\[1]:** 각 메시지 항목은 `{role:"", content:""}` 형식을 사용합니다. `role`은 `"user"`, `"assistant"`, `"system"` 중 하나일 수 있습니다. `content`는 문자열이거나 딕셔너리 목록일 수 있습니다.

- [Invoke Agent Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#invoke-agent-span)

이 span은 작업 수신부터 최종 응답 생성까지의 전체 수명 주기를 포착하며 AI 에이전트 실행을 나타냅니다.

**핵심 속성:**

* `gen_ai.agent.name` — 에이전트 이름 (예: "Weather Agent")
* `gen_ai.request.model` — 사용된 기반 모델
* `gen_ai.response.text` — 에이전트의 최종 출력
* `gen_ai.usage.input_tokens` / `output_tokens` — 전체 토큰 수

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

Invoke Agent span 속성

AI 에이전트 호출을 설명합니다.

* span `op`는 반드시 `"gen_ai.invoke_agent"`여야 합니다.
* span `name`은 `"invoke_agent {gen_ai.agent.name}"`이어야 합니다.
* `gen_ai.operation.name` 속성은 반드시 `"invoke_agent"`여야 합니다.
* `gen_ai.agent.name` 속성은 에이전트 이름으로 설정해야 합니다. (예: `"Weather Agent"`)
* 모든 [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes)를 설정해야 합니다 (`required` 공통 속성은 모두 반드시 설정).

span의 추가 속성:

| 데이터 속성                              | 타입   | 요구 수준        | 설명                                                                                 | 예시                                                                                                              |
| --------------------------------------- | ------ | ---------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `gen_ai.request.available_tools`        | string | optional         | 사용 가능한 도구를 설명하는 객체 목록. **\[0]**                                      | `"[{\"name\": \"random_number\", \"description\": \"...\"}, {\"name\": \"query_db\", \"description\": \"...\"}]"` |
| `gen_ai.request.frequency_penalty`      | float  | optional         | 모델 구성 파라미터.                                                                  | `0.5`                                                                                                             |
| `gen_ai.request.max_tokens`             | int    | optional         | 모델 구성 파라미터.                                                                  | `500`                                                                                                             |

| `gen_ai.request.messages`               | string | 선택 사항         | LLM에 전송된 메시지(프롬프트)를 설명하는 객체 목록 **\[0]**, **\[1]** | `"[{\"role\": \"system\", \"content\": [{...}]}, {\"role\": \"system\", \"content\": [{...}]}]"`                  |
| `gen_ai.request.presence_penalty`       | float  | 선택 사항         | 모델 구성 파라미터.                                                              | `0.5`                                                                                                             |
| `gen_ai.request.temperature`            | float  | 선택 사항         | 모델 구성 파라미터.                                                              | `0.1`                                                                                                             |
| `gen_ai.request.top_p`                  | float  | 선택 사항         | 모델 구성 파라미터.                                                              | `0.7`                                                                                                             |
| `gen_ai.response.tool_calls`            | string | 선택 사항         | 모델 응답의 tool call. **\[0]**                                                  | `"[{\"name\": \"random_number\", \"type\": \"function_call\", \"arguments\": \"...\"}]"`                          |
| `gen_ai.response.text`                  | string | 선택 사항         | 모델 응답의 텍스트 표현. **\[0]**                                                | `"[\"The weather in Paris is rainy\", \"The weather in London is sunny\"]"`                                       |
| `gen_ai.usage.input_tokens.cache_write` | int    | 선택 사항         | AI 입력(프롬프트) 처리 시 캐시에 기록된 토큰 수.                                 | `100`                                                                                                             |
| `gen_ai.usage.input_tokens.cached`      | int    | 선택 사항         | AI 입력(프롬프트)에서 사용된 캐시 토큰 수                                        | `50`                                                                                                              |
| `gen_ai.usage.input_tokens`             | int    | 선택 사항         | AI 입력(프롬프트)에서 사용된 토큰 수.                                            | `10`                                                                                                              |
| `gen_ai.usage.output_tokens.reasoning`  | int    | 선택 사항         | 추론에 사용된 토큰 수.                                                           | `30`                                                                                                              |
| `gen_ai.usage.output_tokens`            | int    | 선택 사항         | AI 응답에서 사용된 토큰 수.                                                      | `100`                                                                                                             |
| `gen_ai.usage.total_tokens`             | int    | 선택 사항         | 프롬프트 처리에 사용된 총 토큰 수. (입력 및 출력)                                | `190`                                                                                                             |

* **\[0]:** Span 속성은 기본 데이터 타입(`int`, `float`, `boolean`, `string`)만 허용합니다. 즉, 딕셔너리 목록을 문자열화한 버전을 사용해야 합니다. `[{"foo": "bar"}]`로 설정하지 말고 문자열 `"[{\"foo\": \"bar\"}]"`를 사용하세요.
* **\[1]:** 각 메시지 항목은 `{role:"", content:""}` 형식을 사용합니다. `role`은 `"user"`, `"assistant"`, `"system"` 중 하나일 수 있습니다. `content`는 문자열 또는 딕셔너리 목록일 수 있습니다.

- [Execute Tool Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#execute-tool-span)

이 span은 AI 모델이 요청한 도구 또는 함수의 실행을 나타내며, 입력 인수와 결과 출력이 포함됩니다.

**주요 속성:**

* `gen_ai.tool.name` — 도구 이름(예: "get\_weather")
* `gen_ai.tool.input` — 도구에 전달된 인수
* `gen_ai.tool.output` — 도구의 반환값

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

Execute Tool span 속성

도구 실행을 설명합니다.

* span `op`는 반드시 `"gen_ai.execute_tool"`이어야 합니다.
* span `name`은 `"execute_tool {gen_ai.tool.name}"`이어야 합니다. (예: `"execute_tool query_database"`)
* `gen_ai.tool.name` 속성은 도구 이름으로 설정해야 합니다. (예: `"query_database"`)
* 모든 [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes)를 설정해야 합니다 (모든 `required` 공통 속성은 반드시 설정).

span의 추가 속성:

| Data Attribute            | Type   | Requirement Level | Description                                  | Example                                    |
| ------------------------- | ------ | ----------------- | -------------------------------------------- | ------------------------------------------ |
| `gen_ai.tool.description` | string | optional          | 실행된 도구에 대한 설명.                     | `"Tool returning a random number"`         |
| `gen_ai.tool.input`       | string | optional          | 실행된 도구에 전달된 입력(문자열).           | `"{\"max\":10}"`                           |
| `gen_ai.tool.name`        | string | optional          | 실행된 도구의 이름.                          | `"random_number"`                          |
| `gen_ai.tool.output`      | string | optional          | 도구의 출력값.                               | `"7"`                                      |
| `gen_ai.tool.type`        | string | optional          | 도구 유형.                                   | `"function"`; `"extension"`; `"datastore"` |

- [Handoff Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#handoff-span)

이 span은 한 에이전트에서 다른 에이전트로 제어가 전환되는 지점을 표시합니다. 일반적으로 현재 에이전트가 다른 에이전트가 작업에 더 적합하다고 판단할 때 사용됩니다.

**요구사항:**

* `op`는 `"gen_ai.handoff"`여야 합니다.
* `name`은 `"handoff from {source} to {target}"` 패턴을 따라야 합니다.
* 모든 [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#common-span-attributes)를 설정해야 합니다.

handoff span 자체에는 본문이 없으며, 대상 에이전트가 시작되기 전 전환 지점만 표시합니다.

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

일부 속성은 모든 AI Agents span에 공통으로 적용됩니다:

| Data Attribute          | Type   | Requirement Level | Description                                        | Example           |
| ----------------------- | ------ | ----------------- | -------------------------------------------------- | ----------------- |
| `gen_ai.request.model`  | string | required          | 요청 대상 AI 모델의 이름.                          | `"o3-mini"`       |
| `gen_ai.operation.name` | string | optional          | 수행 중인 작업의 이름.                             | `"summarize"`     |
| `gen_ai.agent.name`     | string | optional          | 이 span이 속한 에이전트의 이름.                    | `"Weather Agent"` |

## [Token Usage and Cost Gotchas](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#token-usage-and-cost-gotchas)

토큰 속성을 수동으로 설정할 때는 Sentry가 이를 사용해 [모델 비용을 계산](https://docs.sentry.io/ai/monitoring/agents/costs.md)하는 방식을 유의하세요.

**캐시 토큰과 추론 토큰은 별도 합계가 아니라 부분집합입니다.** `gen_ai.usage.input_tokens`는 캐시 토큰을 이미 포함한 **총** 입력 토큰 수입니다. 마찬가지로 `gen_ai.usage.output_tokens`는 추론 토큰을 이미 포함합니다. Sentry는 총계에서 캐시/추론 수를 빼서 "raw" 부분을 계산하므로, 잘못 보고하면 비용이 틀리거나 음수가 될 수 있습니다.

예를 들어 LLM 호출이 총 100개의 입력 토큰을 사용했고, 그중 90개가 캐시에서 제공되었다고 가정해 보겠습니다. 일반 요금이 토큰당 $0.01이고 캐시 요금이 토큰당 $0.001일 때:

**정상** — `input_tokens`는 총계(캐시 포함):

* `gen_ai.usage.input_tokens = 100`
* `gen_ai.usage.input_tokens.cached = 90`
* Sentry 계산: `(100 - 90) × $0.01 + 90 × $0.001` = `$0.10 + $0.09` = **$0.19** ✓

**잘못된 설정** — `input_tokens`를 비캐시 토큰만으로 설정해 캐시가 총계보다 커진 경우:

* `gen_ai.usage.input_tokens = 10`
* `gen_ai.usage.input_tokens.cached = 90`
* Sentry 계산: `(10 - 90) × $0.01 + 90 × $0.001` = `−$0.80 + $0.09` = **−$0.71**

`input_tokens.cached`(90)가 `input_tokens`(10)보다 크기 때문에 뺄셈 결과가 음수가 되어 총 비용이 음수가 됩니다.

동일한 원리가 `gen_ai.usage.output_tokens`와 `gen_ai.usage.output_tokens.reasoning`에도 적용됩니다.

## [Framework Exporters](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#framework-exporters)

AI 프레임워크에서 Sentry exporter를 사용하는 경우, 트레이스를 Sentry로 보낼 수 있습니다:

* [Mastra Sentry Exporter](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md)

## [MCP Server Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md#mcp-server-monitoring)

MCP(Model Context Protocol) 서버를 구축하는 경우, Sentry는 도구 실행, 프롬프트 조회, 리소스 접근도 추적할 수 있습니다. 설정 방법은 [Instrument MCP Servers](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md)를 참고하세요.

## 이 섹션의 페이지

- [Mastra](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md)

