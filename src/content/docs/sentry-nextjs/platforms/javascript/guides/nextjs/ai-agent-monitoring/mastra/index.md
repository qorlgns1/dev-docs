---
title: 'Mastra | Next.js용 Sentry'
description: '이는 Node.js Sentry SDK를 사용하는 Mastra AI 트레이싱용 서버 사이드 exporter입니다. Node.js 또는 호환 런타임이 필요합니다.  패키지가 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra

# Mastra | Next.js용 Sentry

이는 Node.js Sentry SDK를 사용하는 Mastra AI 트레이싱용 서버 사이드 exporter입니다. Node.js 또는 호환 런타임이 필요합니다. `@mastra/sentry@beta` 패키지가 필요합니다.

[Mastra](https://mastra.ai/)는 최신 TypeScript 스택으로 AI 기반 애플리케이션과 에이전트를 구축하기 위한 프레임워크입니다. Mastra Sentry Exporter는 OpenTelemetry 시맨틱 컨벤션을 사용해 트레이싱 데이터를 Sentry로 전송하여, 모델 성능, 토큰 사용량, 도구 실행에 대한 인사이트를 제공합니다.

## [설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#installation)

Mastra Sentry exporter 패키지를 설치하세요:

```bash
npm install @mastra/sentry@beta
```

## [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#configuration)

- [제로 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#zero-config-setup)

Sentry exporter는 환경 변수에서 구성을 자동으로 읽을 수 있습니다:

```javascript
import { SentryExporter } from "@mastra/sentry";

// Reads from SENTRY_DSN, SENTRY_ENVIRONMENT, SENTRY_RELEASE
const exporter = new SentryExporter();
```

- [명시적 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#explicit-configuration)

exporter를 명시적으로 구성할 수도 있습니다:

```javascript
import { SentryExporter } from "@mastra/sentry";

const exporter = new SentryExporter({
  dsn: process.env.SENTRY_DSN,
  environment: "production",
  tracesSampleRate: 1.0,
  release: "1.0.0",
});
```

스팬 매핑

Mastra는 Sentry의 AI 모니터링 대시보드에서 올바르게 시각화되도록 자체 스팬 타입을 Sentry 작업으로 자동 매핑합니다:

| Mastra 스팬 타입       | Sentry 작업            |
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

**참고:** `MODEL_STEP` 및 `MODEL_CHUNK` 스팬은 트레이스 계층을 단순화하기 위해 자동으로 건너뜁니다. 해당 데이터는 상위 `MODEL_GENERATION` 스팬에 집계됩니다.

수집되는 데이터

Sentry exporter는 OpenTelemetry 시맨틱 컨벤션을 따라 포괄적인 트레이스 데이터를 수집합니다:

#
- [공통 속성(모든 스팬)](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#common-attributes-all-spans)

* `sentry.origin`: `auto.ai.mastra` (Mastra에서 생성된 스팬 식별)
* `ai.span.type`: Mastra 스팬 타입

#
- [모델 생성 스팬](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#model-generation-spans)

* `gen_ai.operation.name`: 작업 이름 (예: `chat`)
* `gen_ai.system`: 모델 제공자 (예: OpenAI, Anthropic)
* `gen_ai.request.model`: 모델 식별자
* `gen_ai.request.messages`: 입력 메시지/프롬프트 (JSON)
* `gen_ai.response.model`: 응답 모델
* `gen_ai.response.text`: 출력 텍스트
* `gen_ai.response.tool_calls`: 생성 중 수행된 도구 호출
* `gen_ai.usage.input_tokens`: 입력 토큰 수
* `gen_ai.usage.output_tokens`: 출력 토큰 수
* `gen_ai.usage.total_tokens`: 총 사용 토큰 수
* `gen_ai.request.stream`: 스트리밍 사용 여부
* `gen_ai.request.temperature`: Temperature 파라미터
* `gen_ai.completion_start_time`: 첫 토큰까지 걸린 시간

#
- [도구 호출 스팬](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#tool-call-spans)

* `gen_ai.operation.name`: `execute_tool`
* `gen_ai.tool.name`: 도구 식별자
* `gen_ai.tool.type`: `function`
* `gen_ai.tool.call.id`: 도구 호출 ID
* `gen_ai.tool.input`: 도구 입력 파라미터
* `gen_ai.tool.output`: 도구 출력 결과
* `tool.success`: 성공 플래그

#
- [에이전트 실행 스팬](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#agent-run-spans)

* `gen_ai.operation.name`: `invoke_agent`
* `gen_ai.agent.name`: 에이전트 식별자
* `gen_ai.pipeline.name`: 에이전트 이름
* `gen_ai.agent.instructions`: 에이전트 지시사항/시스템 프롬프트
* `gen_ai.response.model`: 하위 생성에서의 모델
* `gen_ai.response.text`: 하위 생성의 출력
* `gen_ai.usage.*`: 하위 스팬에서 집계된 토큰 사용량

## [메서드](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#methods)

- [`exportTracingEvent()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#exporttracingevent)

트레이싱 이벤트를 Sentry로 내보냅니다. `SPAN_STARTED`, `SPAN_UPDATED`, `SPAN_ENDED` 이벤트를 처리합니다.

```javascript
await exporter.exportTracingEvent(event);
```

- [`flush()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#flush)

exporter를 종료하지 않고 대기 중인 스팬을 Sentry로 강제 flush합니다. 대기 중 데이터 전송을 위해 최대 2초까지 기다립니다. 런타임이 종료되기 전에 스팬이 내보내졌는지 보장해야 하는 serverless 환경에서 유용합니다.

```javascript
await exporter.flush();
```

- [`shutdown()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#shutdown)

활성 상태의 모든 스팬을 종료하고, 내부 상태를 정리한 뒤, Sentry 연결을 닫습니다. 대기 중 데이터 전송을 위해 최대 2초까지 기다립니다.

```javascript
await exporter.shutdown();
```

## [더 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#learn-more)

Sentry와 함께 Mastra를 사용하는 전체 문서는 [Mastra Sentry Exporter documentation](https://mastra.ai/docs/observability/tracing/exporters/sentry)를 참고하세요.

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring/mastra.md#supported-versions)

* `@mastra/sentry`: `>=1.0.0-beta.2`

