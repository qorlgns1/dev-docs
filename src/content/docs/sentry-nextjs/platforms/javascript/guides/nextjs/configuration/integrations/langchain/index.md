---
title: 'LangChain | Next.js용 Sentry'
description: '모든 런타임을 사용하는 메타 프레임워크 애플리케이션의 경우, 로 LangChain 콜백 핸들러를 수동으로 생성해야 합니다. 브라우저 측 사용 섹션의 안내를 참고하세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain

# LangChain | Next.js용 Sentry

## [서버 측 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#server-side-usage)

모든 런타임을 사용하는 메타 프레임워크 애플리케이션의 경우, `createLangChainCallbackHandler`로 LangChain 콜백 핸들러를 수동으로 생성해야 합니다. [브라우저 측 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#browser-side-usage) 섹션의 안내를 참고하세요.

## [브라우저 측 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#browser-side-usage)

*Import name: `Sentry.createLangChainCallbackHandler`*

`createLangChainCallbackHandler` 헬퍼는 [`langchain`](https://www.npmjs.com/package/langchain)용 계측을 추가하여, LangChain 작업을 래핑하는 콜백 핸들러를 생성하고 구성 가능한 입력/출력 기록과 함께 AI 에이전트 상호작용을 기록해 span을 수집합니다. 이 콜백 핸들러는 수동으로 생성해 LangChain 작업에 전달해야 합니다. 아래 예시를 참고하세요.

```javascript
import { ChatAnthropic } from "@langchain/anthropic";

// Create a LangChain callback handler
const callbackHandler = Sentry.createLangChainCallbackHandler({
  recordInputs: true,
  recordOutputs: true,
});

// Use with chat models
const model = new ChatAnthropic({
  model: "claude-3-5-sonnet-20241022",
  apiKey: "your-api-key", // Warning: API key will be exposed in browser!
});

await model.invoke("Tell me a joke", {
  callbacks: [callbackHandler],
});
```

수집되는 데이터(예: 입력 및 출력)를 사용자 지정하려면 Configuration 섹션의 [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#options)를 참고하세요.

## [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#configuration)

- [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#options)

다음 옵션은 LangChain 작업에서 어떤 데이터를 수집할지 제어합니다.

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#recordinputs)

*Type: `boolean` (optional)*

LangChain 작업에 대한 입력(예: 프롬프트와 메시지)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#recordoutputs)

*Type: `boolean` (optional)*

LangChain 작업의 출력(예: 생성된 텍스트와 응답)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

**사용법**

`langChainIntegration` 통합 사용:

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____",
  // Tracing must be enabled for agent monitoring to work
  tracesSampleRate: 1.0,
  integrations: [
    Sentry.langChainIntegration({
      // your options here
    }),
  ],
});
```

`createLangChainCallbackHandler` 헬퍼 사용:

```javascript
const callbackHandler = Sentry.createLangChainCallbackHandler({
  // your options here
});
```

## [지원되는 작업](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#supported-operations)

기본적으로 다음 LangChain SDK 호출에 추적 지원이 추가됩니다.

* **채팅 모델 호출** - 채팅 모델 호출에 대한 span을 수집합니다.
* **LLM 호출** - LLM 파이프라인 실행에 대한 span을 수집합니다.
* **체인 실행** - 체인 호출에 대한 span을 수집합니다.
* **도구 실행** - 도구 호출에 대한 span을 수집합니다.

- [Runnables](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#runnables)

통합은 다음 LangChain runnable 메서드를 자동으로 계측합니다.

* `invoke()` - 단일 실행
* `stream()` - 스트리밍 실행
* `batch()` - 배치 실행

- [Providers](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#providers)

자동 계측은 다음 LangChain provider 패키지를 지원합니다.

* `@langchain/anthropic`
* `@langchain/openai`
* `@langchain/google-genai`
* `@langchain/mistralai`
* `@langchain/google-vertexai`
* `@langchain/groq`

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md#supported-versions)

* `langchain`: `>=0.1.0 <2.0.0`

