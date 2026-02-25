---
title: '분산 추적 설정 | Sentry for Next.js'
description: '분산 추적은 요청이 애플리케이션 아키텍처의 여러 계층을 통과할 때 그 경로를 연결하고 기록합니다. 아키텍처가 서로 다른 서브도메인(예: , )에 있는 여러 서비스로 구성되어 있다면, 분산 추적을 통해 이벤트가 한 서비스에서 다른 서비스로 이동하는 경로를 따라갈 수 있습...'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing

# 분산 추적 설정 | Sentry for Next.js

분산 추적은 요청이 애플리케이션 아키텍처의 여러 계층을 통과할 때 그 경로를 연결하고 기록합니다. 아키텍처가 서로 다른 서브도메인(예: `fe.example.com`, `api.example.com`)에 있는 여러 서비스로 구성되어 있다면, 분산 추적을 통해 이벤트가 한 서비스에서 다른 서비스로 이동하는 경로를 따라갈 수 있습니다.

이러한 엔드투엔드 가시성 덕분에 개발자는 병목 지점을 식별하고, 오류의 근본 원인을 정확히 찾아내며, 컴포넌트 간 상호작용을 이해할 수 있습니다. 즉, 복잡한 디버깅 악몽을 시스템 신뢰성과 성능을 높이는 관리 가능한 프로세스로 바꿔줍니다.

## [기본 예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#basic-example)

다음은 Sentry에서 분산 추적이 어떻게 보이는지 보여주는 예시입니다.

이 분산 추적은 Vue 앱의 `pageload`가 Python 백엔드로 요청을 보내고, 그 백엔드가 다시 Ruby 마이크로서비스의 `/api` 엔드포인트를 호출하는 흐름을 보여줍니다.

백그라운드에서는 Sentry가 애플리케이션 간에 다음 두 HTTP 헤더를 읽고 계속 전파합니다.

* `sentry-trace`
* `baggage`

분산 시스템에서 JavaScript 애플리케이션을 실행한다면, 이 두 헤더가 CORS 허용 목록에 추가되어 있고 프록시 서버, 게이트웨이, 방화벽에서 차단되거나 제거되지 않도록 해야 합니다.

## [분산 추적 사용 방법](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#how-to-use-distributed-tracing)

현재 버전의 Next.js SDK를 사용 중이라면, 분산 추적은 클라이언트, 서버, 엣지 런타임에서 별도 설정 없이 동작합니다.

Next.js 14의 App Router를 위한 추가 구성

Next.js 14의 App Router에서 분산 추적을 활성화하려면 루트 레이아웃의 `generateMetadata` 함수를 추가하거나 수정해야 합니다.

`app/layout.tsx`

```typescript
import * as Sentry from "@sentry/nextjs";
import type { Metadata } from "next";

export function generateMetadata(): Metadata {
  return {
    // ... your existing metadata
    other: {
      ...Sentry.getTraceData(),
    },
  };
}
```

클라이언트 측에서는 외부 API 시스템과 상호작용할 때 [Browser CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) 이슈를 피하기 위해 `tracePropagationTargets`를 정의해야 할 수 있습니다.

참고: 포트 번호는 trace 전파와 origin에 중요합니다. 서비스가 서로 다른 포트에서 실행되는 경우 trace가 서비스 간에 전파되도록 `tracePropagationTargets`를 구성해야 할 수 있습니다.

예를 들어 포트 3000에서 로컬로 실행되는 Node.js 백엔드가 있다면, CORS가 trace 전파를 제한하지 않도록 해당 대상(`http://localhost:3000`)을 프론트엔드의 `tracePropagationTargets` 배열에 추가해야 합니다.

```javascript
// instrumentation-client.js
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracePropagationTargets: ["https://myproject.org", /^\/api\//],
});
```

`7.57.x` 이하 버전을 사용 중이라면, 분산 추적이 동작하려면 [tracing 기능](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)을 활성화해야 합니다.

- [Trace 전파 예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#trace-propagation-examples)

#
- [예시 1: 마이크로서비스 이커머스 플랫폼](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#example-1-microservices-e-commerce-platform)

```javascript
// instrumentation-client.js
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracePropagationTargets: [
    "https://api.myecommerce.com",
    "https://auth.myecommerce.com",
  ],
});
```

이 설정은 Sentry가 다음 경로 전반에 trace 헤더를 전달하도록 지시합니다.

* 메인 API 서버(상품 데이터 제공)
* 인증 서버(로그인 처리)

이렇게 하면 고객이 체크아웃 중 오류를 겪거나 특정 엔드포인트의 성능을 확인하려는 경우, 해당 요청이 이들 서비스 전반에서 어떤 전체 경로를 거쳤는지 확인할 수 있습니다.

#
- [예시 2: 백엔드 서비스를 사용하는 모바일 앱](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#example-2-mobile-app-with-backend-services)

```javascript
// instrumentation-client.js
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  // Capture 100% of spans. This is useful for development and debugging. Consider reducing in production or using traceSampler
  tracesSampleRate: 1.0,
  tracePropagationTargets: [
    "https://api.myapp.com",
    "https://media.myapp.com",
    /^\/local-api\//,
  ],
});
```

이 구성은 앱이 다음 전반에서 사용자 동작을 추적할 수 있게 합니다.

* 메인 API 서버(앱의 대부분 기능 처리)
* 미디어 서버(이미지, 비디오 등 처리)
* 앱 내 모든 로컬 API 엔드포인트

사용자가 사진을 업로드하는 중 앱이 크래시하면, 문제 지점을 앱 자체인지, 메인 API인지, 미디어 서비스인지 정확히 추적할 수 있습니다.

- [엄격한 Trace 연속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#strict-trace-continuation)

지원 버전: `v10`

\_

애플리케이션이 요청을 수신할 때, 상류 서비스(역시 Sentry 사용)에서 전달된 `sentry-trace` 및 `baggage` 헤더가 포함되어 있을 수 있습니다. 기본적으로 SDK는 이 들어온 헤더를 기반으로 trace를 이어갑니다. 하지만 요청이 서드파티 서비스에서 온 경우에는 원치 않는 trace, 청구 증가, 왜곡된 성능 데이터로 이어질 수 있어 이 동작이 바람직하지 않을 수 있습니다.

이를 방지하려면 `strictTraceContinuation`을 활성화할 수 있습니다. 이 옵션을 `true`로 설정하면 SDK가 들어온 요청의 Sentry trace 정보를 검사하고, 같은 Sentry organization에 속하는 경우에만 trace를 이어갑니다. 그렇지 않으면 새 trace를 시작합니다. 애플리케이션이 공개 API이거나 organization 외부 서비스로부터 요청을 받는 경우에 유용합니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
  // Ensure that only traces from your own organization are continued

  strictTraceContinuation: true,

});
```

SDK는 DSN에서 organization ID를 자동으로 파싱합니다. organization ID(숫자 뒤에 문자 `"o"`가 오는 형식)를 포함하지 않는 DSN 형식을 사용하거나 이를 재정의해야 하는 경우, `orgId` 옵션으로 수동 지정할 수 있습니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
  strictTraceContinuation: true,
  // Manually provide your organization ID (overrides organization ID parsed from DSN)

  orgId: 12345,

});
```

- [분산 추적 비활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#disabling-distributed-tracing)

분산 추적을 비활성화하고 Sentry trace 헤더가 전송되지 않도록 하려면 SDK를 다음과 같이 구성할 수 있습니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Overwrite the defaults to ensure no trace headers are sent
  tracePropagationTargets: [],
});
```

분산 시스템 전체로 trace 정보를 전파하려면, 관련된 모든 서비스와 애플리케이션에서 Sentry를 사용해야 한다는 점을 기억하세요. 각 플랫폼에서 분산 추적을 활성화하는 방법은 해당 SDK 문서를 확인하세요.

## [Trace 지속 시간](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#trace-duration)

브라우저에서 SDK는 다음 상황에서 자동으로 새 trace를 시작합니다.

* 페이지 로드 시: 페이지가 (재)로드될 때마다 새 trace가 시작됩니다. 동시에 `pageload` span이 생성됩니다([Performance Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md) 참조). 이 span이 종료된 후에도 trace는 다음 탐색 또는 페이지 로드까지 유지됩니다. 초기 페이지를 제공한 서버가 이미 trace를 시작하고 브라우저에 필요한 [HTML tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#extract-tracing-information-from-html-meta-tags)를 보낸 경우, SDK는 새 trace를 시작하지 않고 해당 trace를 이어갑니다.
* 탐색 시: 사용자가 탐색할 때마다(예: 단일 페이지 애플리케이션) 새 trace가 시작됩니다. 동시에 `navigation` span이 생성됩니다([Performance Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md) 참조). 이 span이 종료된 후에도 trace는 다음 탐색 또는 페이지 로드까지 유지됩니다.

두 경우 모두, 자동 `pageload` 및 `navigation` span이 끝난 뒤에 span을 시작하더라도 같은 trace의 일부가 됩니다. 덕분에 해당 span 전후에 무슨 일이 있었는지 쉽게 연결할 수 있습니다.

서버 측 SDK는 요청 단위로 trace를 자동 처리합니다. 즉 SDK는 다음과 같이 동작합니다.

* 들어오는 요청에 trace 헤더가 있으면 기존 trace를 이어갑니다.
* 들어오는 요청에 trace 헤더가 없으면 새 trace를 시작합니다. 이 trace는 응답이 전송될 때까지 활성 상태로 유지됩니다.

필요하면 [수동으로 새 trace를 시작](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#starting-a-new-trace)하여 기본 trace 지속 시간을 재정의할 수 있습니다.

## [분산 Trace에서 샘플링 전파 방식](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#how-sampling-propagates-in-distributed-traces)

Sentry는 "head-based" 샘플링 방식을 사용합니다.

* 샘플링 결정은 시작 서비스(즉 "head")에서 이루어집니다.
* 이 결정은 모든 다운스트림 서비스로 전파됩니다.

핵심 헤더 두 가지는 다음과 같습니다.

* `sentry-trace`: trace ID, span ID, 샘플링 결정을 포함
* `baggage`: sample rate를 포함한 추가 trace 메타데이터를 포함

Sentry는 `browserTracingIntegration`을 사용할 때 나가는 HTTP 요청에 이 헤더들을 자동으로 첨부합니다. WebSockets 같은 다른 통신 채널에서는 trace 정보를 수동으로 전파할 수 있습니다.

```javascript
// Extract trace data from the current scope
const traceData = Sentry.getTraceData();
const sentryTraceHeader = traceData["sentry-trace"];
const sentryBaggageHeader = traceData["baggage"];

// Add to your custom request (example using WebSocket)
webSocket.send(
  JSON.stringify({
    message: "Your data here",
    metadata: {
      sentryTrace: sentryTraceHeader,
      baggage: sentryBaggageHeader,
    },
  }),
);
```

## 이 섹션의 페이지

- [커스텀 Trace 전파](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md)
- [CORS 이슈 처리](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md)

