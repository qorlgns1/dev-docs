---
title: '브라우저 프로파일링 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser

# 브라우저 프로파일링 | Next.js용 Sentry

브라우저 프로파일링은 현재 베타입니다. 베타 기능은 아직 개발 중이며 버그가 있을 수 있습니다. 아이러니한 점이라는 건 저희도 알고 있습니다.

[프로파일링](https://docs.sentry.io/product/explore/profiling.md)은 프로덕션 코드에서 함수 수준 데이터를 수집하여 앱 성능을 더 정밀하게 튜닝할 수 있게 해줍니다. 무엇이 호출되는지, 얼마나 자주 호출되는지, 어디에서 호출되는지를 추적합니다. 브라우저에서는 이를 통해 UI 끊김(jank)의 원인을 정확히 파악하고, [Interaction to Next Paint (INP)](https://docs.sentry.io/product/insights/web-vitals/web-vitals-concepts.md#interaction-to-next-paint-inp) 같은 지표가 왜 느린지 이해하거나, 리페인트를 막아 프레임 드롭을 유발하는 긴 작업을 식별할 수 있습니다.

##### Chromium 전용

브라우저 프로파일링은 [JS Self-Profiling API](https://wicg.github.io/js-self-profiling/)를 사용하며, 현재 Chromium 기반 브라우저(Chrome, Edge)에서만 사용할 수 있습니다. 프로파일에는 이 브라우저들의 데이터만 포함됩니다.

## [빠른 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#quick-setup)

**요구 사항**: `@sentry/nextjs `SDK 버전 `10.27.0`+ (또는 더 이상 권장되지 않는 transaction-based profiling의 경우 `7.60.0`+)

- [1. SDK 설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#1-install-the-sdk)

```bash
npm install @sentry/nextjs --save
```

- [2. Document-Policy Header 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#2-add-the-document-policy-header)

서버는 응답 헤더에 `Document-Policy: js-profiling`를 반환해야 합니다.

Next.js에서는 `next.config.js`의 `headers` 옵션을 통해 문서 응답 헤더를 구성할 수 있습니다.

`next.config.mjs`

```javascript
export default withSentryConfig({
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          {
            key: "Document-Policy",
            value: "js-profiling",
          },
        ],
      },
    ];
  },

  // ... other Next.js config options
});
```

- [3. SDK 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#3-configure-the-sdk)

`instrumentation-client.js|ts`

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Add browser profiling integration to the list of integrations
    Sentry.browserProfilingIntegration(),
  ],

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for tracing.
  // We recommend adjusting this value in production
  tracesSampleRate: 1.0,
  // Set `tracePropagationTargets` to control for which URLs trace propagation should be enabled
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],

  // Set profileSessionSampleRate to 1.0 to profile during every session.
  // The decision, whether to profile or not, is made once per session (when the SDK is initialized).
  profileSessionSampleRate: 1.0,
});
```

## [프로파일링 모드](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#profiling-modes)

| 모드                 | 설명                                            | 사용 시점                                           |
| -------------------- | ----------------------------------------------- | --------------------------------------------------- |
| **Manual** (기본값)  | 프로파일링 실행 시점을 직접 제어                | 특정 사용자 플로우 또는 상호작용을 프로파일링할 때 |
| **Trace**            | 활성 span과 함께 프로파일러가 자동 실행         | 추적되는 모든 작업에 프로파일을 연결하고 싶을 때   |

- [Manual 모드](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#manual-mode)

프로파일링하려는 코드 구간 전후로 프로파일러를 시작하고 중지하세요:

```javascript
Sentry.uiProfiler.startProfiler();
// Code here will be profiled
Sentry.uiProfiler.stopProfiler();
```

- [Trace 모드](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#trace-mode)

프로파일이 span에 자동으로 연결됩니다. `profileLifecycle: "trace"`를 설정해 활성화하세요:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.browserTracingIntegration(),
    Sentry.browserProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
  profileSessionSampleRate: 1.0,
  profileLifecycle: "trace",
});
```

## [Sentry와 Chrome DevTools](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/browser.md#sentry-vs-chrome-devtools)

|                   | Sentry Profiling            | Chrome DevTools     |
| ----------------- | --------------------------- | ------------------- |
| **환경**          | 프로덕션 (실사용자)         | 로컬 개발           |
| **샘플링 비율**   | 100Hz (10ms 주기)           | 1000Hz (1ms 주기)   |
| **소스 맵**       | 난독화 해제된 함수 이름     | 난독화된 이름       |
| **데이터 범위**   | 사용자 전반에 걸친 집계 데이터 | 단일 세션         |

문제 해결

**Chrome DevTools에 "Profiling Overhead"가 표시됨**

`browserProfilingIntegration`이 활성화되면 Chrome DevTools는 렌더링 작업을 프로파일링 오버헤드로 잘못 분류합니다. 로컬에서 DevTools를 사용할 때는 이 integration을 비활성화하세요.

**프로파일이 Chrome 사용자에게서만 수집됨**

정상 동작입니다. JS Self-Profiling API는 현재 Chromium 브라우저에서만 구현되어 있습니다. 데이터를 분석할 때 이 편향을 고려하세요.

