---
title: '가이드: Analytics'
description: '최종 업데이트: 2026년 2월 20일'
---

# 가이드: Analytics | Next.js

출처 URL: https://nextjs.org/docs/app/guides/analytics

# Next.js 애플리케이션에 분석 기능을 추가하는 방법

최종 업데이트: 2026년 2월 20일

Next.js는 성능 지표를 측정하고 보고하는 기능을 기본 제공한다. [`useReportWebVitals`](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals) 훅을 사용해 직접 보고 흐름을 제어할 수도 있고, Vercel에서 제공하는 [관리형 서비스](https://vercel.com/analytics?utm_source=next-site&utm_medium=docs&utm_campaign=next-website)를 통해 지표를 자동으로 수집하고 시각화할 수도 있다.

## Client Instrumentation[](https://nextjs.org/docs/app/guides/analytics#client-instrumentation)

더 고급 분석 및 모니터링이 필요하다면 Next.js는 애플리케이션의 프런트엔드 코드가 실행되기 전에 동작하는 `instrumentation-client.js|ts` 파일을 제공한다. 이는 전역 분석, 오류 추적, 성능 모니터링 도구를 설정하기에 적합하다.

사용하려면 애플리케이션 루트 디렉터리에 `instrumentation-client.js` 또는 `instrumentation-client.ts` 파일을 생성한다:

instrumentation-client.js
```
// Initialize analytics before the app starts
console.log('Analytics initialized')

// Set up global error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

## Build Your Own[](https://nextjs.org/docs/app/guides/analytics#build-your-own)

app/_components/web-vitals.js
```
'use client'

import { useReportWebVitals } from 'next/web-vitals'

export function WebVitals() {
  useReportWebVitals((metric) => {
    console.log(metric)
  })
}
```

app/layout.js
```
import { WebVitals } from './_components/web-vitals'

export default function Layout({ children }) {
  return (
    <html>
      <body>
        <WebVitals />
        {children}
      </body>
    </html>
  )
}
```

> `useReportWebVitals` 훅에는 `'use client'` 지시어가 필요하므로, 루트 레이아웃이 가져오는 별도 컴포넌트를 만드는 것이 가장 성능이 좋다. 이렇게 하면 클라이언트 경계를 `WebVitals` 컴포넌트에만 한정할 수 있다.

자세한 내용은 [API Reference](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals)를 확인하라.

## Web Vitals[](https://nextjs.org/docs/app/guides/analytics#web-vitals)

[Web Vitals](https://web.dev/vitals/)는 웹페이지의 사용자 경험을 포착하려는 유용한 지표 모음이다. 다음 웹 바이탈이 모두 포함된다:

  * [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
  * [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
  * [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
  * [First Input Delay](https://web.dev/fid/) (FID)
  * [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
  * [Interaction to Next Paint](https://web.dev/inp/) (INP)

이 지표들의 결과는 모두 `name` 속성을 사용해 처리할 수 있다.

app/_components/web-vitals.tsx

JavaScriptTypeScript
```
'use client'

import { useReportWebVitals } from 'next/web-vitals'

export function WebVitals() {
  useReportWebVitals((metric) => {
    switch (metric.name) {
      case 'FCP': {
        // handle FCP results
      }
      case 'LCP': {
        // handle LCP results
      }
      // ...
    }
  })
}
```

## 외부 시스템으로 결과 전송[](https://nextjs.org/docs/app/guides/analytics#sending-results-to-external-systems)

사이트에서 실제 사용자 성능을 측정하고 추적하기 위해 결과를 원하는 엔드포인트로 전송할 수 있다. 예:

```
useReportWebVitals((metric) => {
  const body = JSON.stringify(metric)
  const url = 'https://example.com/analytics'

  // Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url, body)
  } else {
    fetch(url, { body, method: 'POST', keepalive: true })
  }
})
```

> **알아두면 좋은 점**: [Google Analytics](https://analytics.google.com/analytics/web/)를 사용하는 경우 `id` 값을 활용하면 지표 분포를 수동으로 구성해(예: 백분위수 계산) 더 세밀한 분석을 수행할 수 있다.

>
> ```
> useReportWebVitals((metric) => {
>   // Use `window.gtag` if you initialized Google Analytics as this example:
>   // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>   window.gtag('event', metric.name, {
>     value: Math.round(
>       metric.name === 'CLS' ? metric.value * 1000 : metric.value
>     ), // values must be integers
>     event_label: metric.id, // id unique to current page load
>     non_interaction: true, // avoids affecting bounce rate.
>   })
> })
> ```
>
> [Google Analytics로 결과를 전송하는 방법](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics)에 대해 더 알아보라.