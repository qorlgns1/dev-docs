---
title: 'Anthropic | Next.js용 Sentry'
description: '모든 런타임을 사용하는 메타 프레임워크 애플리케이션에서는 Anthropic 클라이언트 인스턴스를 로 수동으로 래핑해야 합니다. 브라우저 사이드 사용 섹션의 안내를 참고하세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic

# Anthropic | Next.js용 Sentry

## [서버 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#server-side-usage)

모든 런타임을 사용하는 메타 프레임워크 애플리케이션에서는 Anthropic 클라이언트 인스턴스를 `instrumentAnthropicAiClient`로 수동으로 래핑해야 합니다. [브라우저 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#browser-side-usage) 섹션의 안내를 참고하세요.

## [브라우저 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#browser-side-usage)

*임포트 이름: `Sentry.instrumentAnthropicAiClient`*

`instrumentAnthropicAiClient` 헬퍼는 Anthropic SDK 호출을 래핑하고 입력/출력 기록을 구성 가능하게 하여 LLM 상호작용을 기록함으로써, [`@anthropic-ai/sdk`](https://www.npmjs.com/package/@anthropic-ai/sdk) API에서 span을 수집하기 위한 계측을 추가합니다. 이 헬퍼로 Anthropic 클라이언트 인스턴스를 수동으로 래핑해야 합니다. 아래 예시를 참고하세요:

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

캡처되는 데이터(예: 입력 및 출력)를 사용자 지정하려면 Configuration 섹션의 [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#options)를 참고하세요.

## [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#configuration)

- [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#options)

다음 옵션은 Anthropic SDK 호출에서 어떤 데이터를 캡처할지 제어합니다:

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#recordinputs)

*유형: `boolean` (선택 사항)*

Anthropic SDK 호출의 입력(예: 프롬프트 및 메시지)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#recordoutputs)

*유형: `boolean` (선택 사항)*

Anthropic SDK 호출의 출력(예: 생성된 텍스트 및 응답)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

**사용법**

`anthropicAIIntegration` 통합 사용:

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

`instrumentAnthropicAiClient` 헬퍼 사용:

```javascript
const client = Sentry.instrumentAnthropicAiClient(anthropic, {
  // your options here
});
```

## [지원되는 작업](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#supported-operations)

기본적으로 다음 Anthropic SDK 호출에 트레이싱 지원이 추가됩니다:

* `messages.create()` - Claude 모델로 메시지 생성
* `messages.stream()` - Claude 모델로 메시지 스트리밍
* `messages.countTokens()` - 메시지의 토큰 수 계산
* `models.get()` - 모델 정보 가져오기
* `completions.create()` - completions 생성(레거시)
* `models.retrieve()` - 모델 세부 정보 조회
* `beta.messages.create()` - Beta 메시지 API

스트리밍 및 비스트리밍 요청은 자동으로 감지되어 적절히 처리됩니다.

## [지원되는 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md#supported-versions)

* `@anthropic-ai/sdk`: `>=0.19.2 <1.0.0`

