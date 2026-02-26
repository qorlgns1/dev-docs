---
title: '자동 계측 | Next.js용 Sentry'
description: '스팬을 수집하려면, 아직 설정하지 않았다면 먼저 앱에서 트레이싱을 설정해야 합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation

# 자동 계측 | Next.js용 Sentry

스팬을 수집하려면, 아직 설정하지 않았다면 먼저 앱에서 [트레이싱을 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)해야 합니다.

`@sentry/nextjs`는 브라우저 애플리케이션 성능 모니터링을 위한 자동 계측을 추가하는 `BrowserTracing` 통합을 제공하며, 앱에서 트레이싱을 설정하면 기본적으로 활성화됩니다. 또한 SDK는 API 라우트와 [Next.js Data Fetchers](https://nextjs.org/docs/basic-features/data-fetching/overview)에서 오류 수집과 트레이싱을 자동으로 활성화합니다.

## [자동으로 수집되는 항목](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#whats-captured-automatically)

트레이싱을 활성화하면 SDK가 추가 코드 없이 성능 데이터를 자동으로 수집합니다:

| 항목                  | 설명                             | 메트릭                |
| --------------------- | -------------------------------- | --------------------- |
| **페이지 로드**       | 전체 페이지 로드 성능            | LCP, CLS, TTFB        |
| **내비게이션**        | 클라이언트 측 라우트 변경        | Duration, Web Vitals  |
| **HTTP 요청**         | 모든 fetch/XHR 호출              | Duration, status, URL |
| **사용자 상호작용**   | 작업을 유발하는 클릭, 입력       | INP (responsiveness)  |
| **긴 작업**           | 메인 스레드 블로킹 > 50ms        | Duration, attribution |

`BrowserTracing` 통합은 각 페이지 로드 및 내비게이션 이벤트마다 새 트랜잭션을 만들고, 해당 트랜잭션이 열려 있는 동안 발생하는 모든 `XMLHttpRequest` 또는 `fetch` 요청에 대해 자식 스팬을 생성합니다. 또한 SDK는 API 라우트와 [Next.js data fetchers](https://nextjs.org/docs/basic-features/data-fetching/overview)로의 모든 요청에 대해 트랜잭션을 생성합니다. [traces, transactions, and spans](https://docs.sentry.io/product/sentry-basics/tracing/distributed-tracing.md)에 대해 자세히 알아보세요.

## [계측 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enable-instrumentation)

트레이싱을 활성화하려면 [Set Up Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)에 설명된 대로 SDK 구성 옵션에서 `tracesSampleRate` 또는 `tracesSampler` 중 하나를 설정하면 됩니다.

## [일반 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#common-configuration)

대부분의 앱은 다음 옵션만 필요합니다:

* [Distributed Tracing Targets](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#distributed-tracing-targets) — 프런트엔드와 백엔드 스팬 연결
* [Customize Span Names](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#customize-span-names) — URL 정규화 또는 컨텍스트 추가
* [Filter Out Unwanted Requests](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#filter-out-unwanted-requests) — 헬스 체크, 분석 요청 제외

- [Distributed Tracing Targets](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#distributed-tracing-targets)

- [tracePropagationTargets](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#tracePropagationTargets)

| Type    | `Array<string \| RegExp>` |
| ------- | ------------------------- |
| Default | `['localhost', /^\/$/]`   |

어떤 외부 요청에 트레이싱 헤더(`sentry-trace` 및 `baggage`)를 포함할지 제어합니다. **프런트엔드 스팬과 백엔드 스팬을 연결하려면 필수입니다.**

기본적으로 트레이싱 헤더는 `localhost`를 포함하거나 `/`로 시작하는 요청에만 첨부됩니다. 서비스 간 요청을 추적하려면 API 도메인을 추가하세요:

예시:

* 프런트엔드 애플리케이션은 `example.com`에서 제공됩니다.
* 백엔드 서비스는 `api.example.com`에서 제공됩니다.
* 개발 환경에서는 백엔드 서비스가 `localhost`에서 제공됩니다.
* 프런트엔드 애플리케이션이 백엔드로 API 호출을 보냅니다.
* `tracePropagationTargets` 옵션을 `["localhost", /^https:\/\/api\.example\.com/]`로 설정합니다.
* 이제 백엔드 서비스로 향하는 외부 XHR/fetch 요청에 `sentry-trace` 및 `baggage` 헤더가 첨부됩니다.

```javascript
Sentry.init({
  // ...
  integrations: [Sentry.browserTracingIntegration()],

  // Set `tracePropagationTargets` to control for which URLs trace propagation should be enabled
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],
});
```

서버는 CORS를 통해 다음 헤더를 허용해야 합니다: `Access-Control-Allow-Headers: sentry-trace, baggage`

- [Customize Span Names](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#customize-span-names)

- [beforeStartSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#beforeStartSpan)

| Type | `(options: StartSpanOptions) => StartSpanOptions` |
| ---- | ------------------------------------------------- |

수집되기 전에 스팬 데이터를 수정합니다. 컨텍스트를 추가하거나 동적 세그먼트를 포함한 URL을 정규화할 때 유용합니다:

```javascript
Sentry.init({
  // ...
  integrations: [
    Sentry.browserTracingIntegration({
      beforeStartSpan: (context) => {
        return {
          ...context,
          attributes: {
            ...context.attributes,
            resultFormat: "legacy",
          },
        };
      },
    }),
  ],
});
```

- [Filter Out Unwanted Requests](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#filter-out-unwanted-requests)

- [shouldCreateSpanForRequest](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#shouldCreateSpanForRequest)

| Type | `(url: string) => boolean` |
| ---- | -------------------------- |

헬스 체크나 분석 핑 같은 요청을 트레이싱에서 제외합니다:

```javascript
Sentry.init({
  // ...
  integrations: [
    Sentry.browserTracingIntegration({
      shouldCreateSpanForRequest: (url) => {
        // Do not create spans for outgoing requests to a `/health/` endpoint
        return !url.match(/\/health\/?$/);
      },
    }),
  ],
});
```

## [Web Vitals 및 상호작용](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#web-vitals--interactions)

- [Interaction to Next Paint (INP)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#interaction-to-next-paint-inp)

- [enableInp](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableInp)

| Available since | `7.104.0`                         |
| --------------- | --------------------------------- |
| Type            | `boolean`                         |
| Default         | `true` (<!-- -->참고<!-- -->) |

반응성을 측정하기 위해 [INP](https://docs.sentry.io/product/insights/web-vitals/web-vitals-concepts.md#interaction-to-next-paint-inp) 이벤트를 자동으로 수집합니다. 결과는 [Web Vitals](https://docs.sentry.io/product/insights/web-vitals.md) 모듈에 표시됩니다.

기본값: SDK 8.x+에서는 `true`, 7.x에서는 `false`.

##### INP가 FID를 대체합니다

SDK 버전 10.0.0부터 First Input Delay (FID)는 더 이상 보고되지 않습니다. Google이 FID를 더 포괄적인 반응성 지표인 INP로 대체했기 때문입니다. FID 기반 알림이나 대시보드가 있다면 INP를 사용하도록 업데이트하세요.

```javascript
Sentry.init({
  // ...
  integrations: [
    Sentry.browserTracingIntegration({
      enableInp: true,
    }),
  ],
});
```

- [interactionsSampleRate](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#interactionsSampleRate)

| Type    | `number` |
| ------- | -------- |
| Default | `1.0`    |

`tracesSampleRate` 위에 추가로 적용되는 INP 스팬 샘플링 비율입니다. 예를 들어 `tracesSampleRate: 0.1`에서 `interactionsSampleRate: 0.5`를 사용하면 상호작용의 5%가 수집됩니다.

## [고급 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#advanced-options)

타이밍 및 타임아웃 옵션

- [idleTimeout](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#idleTimeout)

| Type    | `number` |
| ------- | -------- |
| Default | `1000`   |

미완료 자식 스팬이 더 이상 없을 때 페이지 로드/내비게이션 스팬을 종료하기 전에 대기하는 시간(ms)입니다.

- [finalTimeout](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#finalTimeout)

| Type    | `number` |
| ------- | -------- |
| Default | `30000`  |

페이지 로드/내비게이션 스팬의 최대 지속 시간(ms)입니다. 이를 초과하면 스팬이 자동으로 종료됩니다.

- [childSpanTimeout](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#childSpanTimeout)

| Type    | `number` |
| ------- | -------- |
| Default | `15000`  |

부모 페이지 로드/내비게이션 스팬이 종료되기 전, 자식 스팬이 실행될 수 있는 최대 시간(ms)입니다.

특정 계측 활성화/비활성화

- [instrumentPageLoad](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#instrumentPageLoad)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

초기 페이지 로드 시 자동 `pageload` 스팬 생성 활성화/비활성화.

- [instrumentNavigation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#instrumentNavigation)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

히스토리 변경 시 자동 `navigation` 스팬 생성 활성화/비활성화.

- [enableLongTask](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableLongTask)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

긴 작업(메인 스레드 블로킹 > 50ms)에 대한 자동 스팬 활성화/비활성화.

- [enableLongAnimationFrame](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableLongAnimationFrame)

| Available since | `8.18.0`  |
| --------------- | --------- |
| Type            | `boolean` |
| Default         | `true`    |

긴 애니메이션 프레임에 대한 스팬 활성화/비활성화. 브라우저가 긴 애니메이션 프레임을 지원하지 않으면 긴 작업으로 대체됩니다.

- [markBackgroundSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#markBackgroundSpan)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

탭이 백그라운드로 이동할 때 페이지 로드/내비게이션 스팬을 "cancelled"로 표시합니다. 정확한 측정을 위해 활성화 상태 유지가 권장됩니다.

- [enableReportPageLoaded](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableReportPageLoaded)

| Available since | `10.13.0` |
| --------------- | --------- |
| Type            | `boolean` |
| Default         | `false`   |

[`Sentry.reportPageLoaded()` function](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#reportPageLoaded)을 활성화합니다.

- [traceFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#traceFetch)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

`fetch` 요청에 대한 자동 스팬 생성 활성화/비활성화.

- [traceXHR](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#traceXHR)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

`XMLHttpRequest` (XHR) 요청에 대한 자동 스팬 생성 활성화/비활성화.

- [enableHTTPTimings](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableHTTPTimings)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Performance Resource Timing API를 통해 fetch/XHR 스팬에 상세 HTTP 타이밍 데이터(DNS 조회, TLS 핸드셰이크 등) 추가를 활성화/비활성화합니다.

- [linkPreviousTrace](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#linkPreviousTrace)

| Type    | `'in-memory' \| 'session-storage' \| false` |
| ------- | ------------------------------------------- |

| 기본값 | `'in-memory'`                               |

새로운 pageload span을 이전 trace에 어떻게 연결할지 제어합니다. 동일한 페이지 라이프사이클 내에서 연결하려면 `'in-memory'`, session storage를 통해 페이지 리로드 간에도 연결을 유지하려면 `'session-storage'`, trace 연결을 비활성화하려면 `false`로 설정하세요.

Span 필터링 및 무시

- [ignoreResourceSpans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#ignoreResourceSpans)

| 지원 버전 | `9.23.0`        |
| --------- | --------------- |
| 유형      | `Array<string>` |
| 기본값    | `[]`            |

`op` 기준(예: `resource.script`, `resource.css`)으로 특정 리소스 span 카테고리를 무시합니다:

```javascript
Sentry.init({
  integrations: [
    Sentry.browserTracingIntegration({
      ignoreResourceSpans: ["resource.css", "resource.script"],
    }),
  ],
});
```

- [ignorePerformanceApiSpans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#ignorePerformanceApiSpans)

| 지원 버전 | `9.23.0`                  |
| --------- | ------------------------- |
| 유형      | `Array<string \| RegExp>` |
| 기본값    | `[]`                      |

`performance.mark()` 및 `performance.measure()`에서 생성된 span을 무시합니다:

```javascript
Sentry.init({
  integrations: [
    Sentry.browserTracingIntegration({
      ignorePerformanceApiSpans: ["myMeasurement", /myMark/],
    }),
  ],
});
```

- [onRequestSpanStart](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#onRequestSpanStart)

| 유형 | `(span: Span, requestInformation: { headers?: WebFetchHeaders }): void` |
| ---- | ----------------------------------------------------------------------- |

나가는 fetch/XHR 요청에 대한 span이 시작될 때 호출되는 콜백입니다. 요청 헤더를 기반으로 추가 속성을 span에 주석 처리(annotate)하는 데 사용합니다.

## [Next.js 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#nextjs-configuration)

`browserTracingIntegration`은 `@sentry/nextjs`에서 자동으로 활성화됩니다. 옵션을 사용자 지정하려면 `instrumentation-client.js`에 이를 명시적으로 포함하세요:

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.browserTracingIntegration({
      // your options here
    }),
  ],
  tracesSampleRate: 1.0,
  tracePropagationTargets: [
    "localhost",
    /^\//,
    /^https:\/\/yourserver\.io\/api/,
  ],
});
```

