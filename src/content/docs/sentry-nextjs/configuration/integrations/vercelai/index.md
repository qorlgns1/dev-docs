---
title: 'Vercel AI | Next.js용 Sentry'
description: 'Node.js, Cloudflare Workers, Vercel Edge Functions, Bun에서는 SDK 버전  이상이 필요합니다. Deno에서는 SDK 버전  이상이 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai

# Vercel AI | Next.js용 Sentry

Node.js, Cloudflare Workers, Vercel Edge Functions, Bun에서는 SDK 버전 `10.6.0` 이상이 필요합니다. Deno에서는 SDK 버전 `10.12.0` 이상이 필요합니다.

*Import name: `Sentry.vercelAIIntegration`*

`vercelAIIntegration`은 Vercel의 [`ai`](https://www.npmjs.com/package/ai) SDK에 대한 계측을 추가하여 [`AI SDK's built-in Telemetry`](https://sdk.vercel.ai/docs/ai-sdk-core/telemetry)를 사용해 스팬을 수집합니다.

이 통합은 Node 런타임에서는 기본적으로 활성화되지만 Edge 런타임에서는 활성화되지 않습니다. `sentry.edge.config.js` 파일의 `Sentry.init`에 `Sentry.vercelAIIntegration()`을 전달해 수동으로 활성화해야 합니다:

`'sentry.edge.config.(js|ts)'`

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____"
  tracesSampleRate: 1.0,
  integrations: [Sentry.vercelAIIntegration()],
});
```

스팬을 올바르게 수집하려면 모든 `generateText`, `generateObject`, `streamText` 함수 호출에 `experimental_telemetry` 객체와 `isEnabled: true`를 전달하세요. 자세한 내용은 [AI SDK Telemetry Metadata docs](https://sdk.vercel.ai/docs/ai-sdk-core/telemetry#telemetry-metadata)를 참고하세요.

```javascript
const result = await generateText({
  model: openai("gpt-4o"),
  experimental_telemetry: {
    isEnabled: true,
    recordInputs: true,
    recordOutputs: true,
  },
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md#options)

- [`force`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md#force)

SDK 버전 `9.29.0` 이상이 필요합니다.

*Type: `boolean`*

`ai` 모듈이 감지되지 않거나 사용할 수 없는 경우에도 통합을 강제로 활성화합니다. 모듈 감지 여부와 관계없이 통합이 항상 활성화되도록 보장하려는 경우에 유용합니다.

기본값은 `false`입니다.

```javascript
Sentry.init({
  integrations: [Sentry.vercelAIIntegration({ force: true })],
});
```

이 옵션은 Edge 런타임에서는 사용할 수 없습니다. Edge 런타임에서는 통합이 활성화되면 강제 적용됩니다.

## [함수 식별](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md#identifying-functions)

수집된 스팬을 함수 호출과 더 쉽게 연관 지을 수 있도록, 모든 생성 함수 호출의 `experimental_telemetry`에 `functionId`를 설정하는 것을 권장합니다:

```javascript
const result = await generateText({
  model: openai("gpt-4o"),
  experimental_telemetry: {
    isEnabled: true,
    functionId: "my-awesome-function",
  },
});
```

## [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md#configuration)

기본적으로 이 통합은 모든 `ai` 함수 호출 위치에 트레이싱 지원을 추가합니다. 특정 호출에 대해 스팬 수집을 비활성화해야 하는 경우, 함수 호출의 첫 번째 인자에서 `experimental_telemetry.isEnabled`를 `false`로 설정하면 됩니다.

```javascript
const result = await generateText({
  model: openai("gpt-4o"),
  experimental_telemetry: { isEnabled: false },
});
```

`experimental_telemetry.recordInputs`와 `experimental_telemetry.recordOutputs`를 설정하면 해당 함수 호출의 입력 및 출력 수집 기본 동작을 덮어씁니다.

```javascript
const result = await generateText({
  model: openai("gpt-4o"),
  experimental_telemetry: {
    isEnabled: true,
    recordInputs: true,
    recordOutputs: true,
  },
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md#supported-versions)

* `ai`: `>=3.0.0 <=6`

## [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md#troubleshooting)

Vercel에서 내 AI 스팬이 왜 `'gen_ai.execute_tool'` 대신 `'ai.toolCall'`로 표시되나요?

Vercel에 배포할 때 AI SDK 스팬 이름이 `gen_ai.execute_tool` 또는 `gen_ai.stream_text` 같은 예상되는 시맨틱 이름 대신 `ai.toolCall` 또는 `ai.streamText` 같은 원시 이름으로 표시될 수 있습니다.

이는 Next.js 프로덕션 빌드에서 `ai` 패키지가 외부화되지 않고 번들링되기 때문에, 통합이 모듈을 자동으로 감지하고 계측하지 못하기 때문입니다.

이 문제를 해결하려면 `sentry.server.config.ts`에서 `force: true`로 통합을 명시적으로 활성화하세요:

```javascript
Sentry.init({
  dsn: "____PUBLIC_DSN____",
  integrations: [Sentry.vercelAIIntegration({ force: true })],
});
```

`force` 옵션은 모듈 감지 여부와 관계없이 통합이 스팬 프로세서를 등록하도록 보장합니다.

