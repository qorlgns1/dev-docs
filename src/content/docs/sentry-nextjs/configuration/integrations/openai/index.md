---
title: 'OpenAI | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai

# OpenAI | Next.js용 Sentry

## [서버 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#server-side-usage)

모든 런타임을 사용하는 메타 프레임워크 애플리케이션에서는 OpenAI 클라이언트 인스턴스를 `instrumentOpenAiClient`로 수동 래핑해야 합니다. [브라우저 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#browser-side-usage) 섹션의 안내를 참고하세요.

## [브라우저 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#browser-side-usage)

*가져오기 이름: `Sentry.instrumentOpenAiClient`*

`instrumentOpenAiClient` 헬퍼는 OpenAI SDK 호출을 래핑하고, 설정 가능한 입력/출력 기록으로 LLM 상호작용을 기록하여 [`openai`](https://www.npmjs.com/package/openai) SDK에서 span을 수집할 수 있도록 계측을 추가합니다. 이 헬퍼로 OpenAI 클라이언트 인스턴스를 수동으로 래핑해야 합니다:

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

캡처되는 데이터(예: 입력 및 출력)를 사용자 지정하려면 Configuration 섹션의 [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#options)를 참고하세요.

## [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#configuration)

- [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#options)

다음 옵션은 OpenAI SDK 호출에서 어떤 데이터가 캡처되는지를 제어합니다:

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#recordinputs)

*유형: `boolean` (선택 사항)*

OpenAI SDK 호출의 입력(예: 프롬프트 및 메시지)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#recordoutputs)

*유형: `boolean` (선택 사항)*

OpenAI SDK 호출의 출력(예: 생성된 텍스트 및 응답)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

**사용법**

`openAIIntegration` integration 사용:

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

`instrumentOpenAiClient` 헬퍼 사용:

```javascript
const client = Sentry.instrumentOpenAiClient(openai, {
  // your options here
});
```

## [지원되는 작업](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#supported-operations)

기본적으로 다음 OpenAI SDK 호출에 tracing 지원이 추가됩니다:

* `chat.completions.create()` - 채팅 완료 요청
* `responses.create()` - Response SDK 요청

스트리밍 및 비스트리밍 요청은 자동으로 감지되어 적절하게 처리됩니다.

OpenAI의 스트리밍 API를 사용할 때는 토큰 사용량 데이터를 받기 위해 `stream_options: { include_usage: true }`도 함께 전달해야 합니다. 이 옵션이 없으면 OpenAI는 스트리밍 응답에 `prompt_tokens` 또는 `completion_tokens`를 포함하지 않으며, Sentry는 결과 span에서 `gen_ai.usage.input_tokens` / `gen_ai.usage.output_tokens`를 캡처할 수 없습니다. 이는 Sentry의 제한이 아니라 OpenAI API 동작입니다. 자세한 내용은 [OpenAI docs on stream options](https://platform.openai.com/docs/api-reference/chat/create#chat-create-stream_options)를 참고하세요.

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md#supported-versions)

* `openai`: `>=4.0.0 <7`

