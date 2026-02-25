---
title: 'Google Gen AI | Next.js용 Sentry'
description: '모든 런타임을 사용하는 메타 프레임워크 애플리케이션의 경우, Google Gen AI 클라이언트 인스턴스를 로 수동으로 래핑해야 합니다. 브라우저 사이드 사용 섹션의 안내를 참고하세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai

# Google Gen AI | Next.js용 Sentry

## [서버 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#server-side-usage)

모든 런타임을 사용하는 메타 프레임워크 애플리케이션의 경우, Google Gen AI 클라이언트 인스턴스를 `instrumentGoogleGenAIClient`로 수동으로 래핑해야 합니다. [브라우저 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#browser-side-usage) 섹션의 안내를 참고하세요.

## [브라우저 사이드 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#browser-side-usage)

*가져오기 이름: `Sentry.instrumentGoogleGenAIClient`*

`instrumentGoogleGenAIClient` 헬퍼는 [`@google/genai`](https://www.npmjs.com/package/@google/genai) SDK 호출을 래핑하고 입력/출력 기록을 구성 가능하게 하여 LLM 상호작용을 기록함으로써 span을 수집할 수 있도록 계측을 추가합니다. 이 헬퍼로 Google Gen AI 클라이언트 인스턴스를 수동으로 래핑해야 합니다. 아래 예시를 참고하세요.

```javascript
import { GoogleGenAI } from "@google/genai";

const genAI = new GoogleGenAI({
  apiKey: "your-api-key", // Warning: API key will be exposed in browser!
});

const client = Sentry.instrumentGoogleGenAIClient(genAI, {
  recordInputs: true,
  recordOutputs: true,
});

// Use the wrapped client instead of the original genAI instance
const result = await client.models.generateContent("Hello!");
```

캡처되는 데이터(예: 입력 및 출력)를 사용자 지정하려면 Configuration 섹션의 [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#options)를 참고하세요.

## [설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#configuration)

- [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#options)

다음 옵션은 Google Gen AI SDK 호출에서 어떤 데이터를 캡처할지 제어합니다.

#
- [`recordInputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#recordinputs)

*유형: `boolean` (선택 사항)*

Google Gen AI SDK 호출의 입력(예: 프롬프트 및 메시지)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

#
- [`recordOutputs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#recordoutputs)

*유형: `boolean` (선택 사항)*

Google Gen AI SDK 호출의 출력(예: 생성된 텍스트 및 응답)을 기록합니다.

`sendDefaultPii`가 `true`이면 기본값은 `true`입니다.

**사용법**

`googleGenAIIntegration` 통합 사용:

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____",
  // Tracing must be enabled for agent monitoring to work
  tracesSampleRate: 1.0,
  integrations: [
    Sentry.googleGenAIIntegration({
      // your options here
    }),
  ],
});
```

`instrumentGoogleGenAIClient` 헬퍼 사용:

```javascript
const client = Sentry.instrumentGoogleGenAIClient(genAI, {
  // your options here
});
```

## [지원 작업](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#supported-operations)

기본적으로 다음 Google Gen AI SDK 호출에 트레이싱 지원이 추가됩니다:

* `models.generateContent()` - 지정한 모델로 콘텐츠 생성
* `models.generateContentStream()` - 지정한 모델로 콘텐츠 생성 스트리밍
* `chats.create()` - 채팅 세션 생성
* `sendMessage()` - 채팅 세션에서 메시지 전송
* `sendMessageStream()` - 채팅 세션에서 메시지 스트리밍 전송

스트리밍 및 비스트리밍 요청은 자동으로 감지되어 적절히 처리됩니다.

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md#supported-versions)

* `@google/genai`: `>=0.10.0 <2`

