---
title: '함수: useReportWebVitals'
description: '훅은 Core Web Vitals을 보고할 수 있게 해 주며, 애널리틱스 서비스와 함께 사용할 수 있습니다.'
---

# 함수: useReportWebVitals | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals

Copy page

# useReportWebVitals

최종 업데이트 2026년 2월 20일

`useReportWebVitals` 훅은 [Core Web Vitals](https://web.dev/vitals/)을 보고할 수 있게 해 주며, 애널리틱스 서비스와 함께 사용할 수 있습니다.

`useReportWebVitals`에 전달된 새 함수는 해당 시점까지 이용 가능한 메트릭과 함께 호출됩니다. 중복 데이터를 보고하지 않으려면 콜백 함수 참조가 변경되지 않도록 하세요(아래 코드 예제 참조).

app/_components/web-vitals.js
[code]
    'use client'

    import { useReportWebVitals } from 'next/web-vitals'

    const logWebVitals = (metric) => {
      console.log(metric)
    }

    export function WebVitals() {
      useReportWebVitals(logWebVitals)

      return null
    }
[/code]

app/layout.js
[code]
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
[/code]

> `useReportWebVitals` 훅에는 `'use client'` 지시문이 필요하므로, 루트 레이아웃이 가져오는 별도의 컴포넌트를 만드는 것이 가장 성능이 좋습니다. 이렇게 하면 클라이언트 경계가 `WebVitals` 컴포넌트에만 국한됩니다.

## useReportWebVitals[](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals#usereportwebvitals)

훅의 인자로 전달되는 `metric` 객체는 여러 속성으로 구성됩니다.

  * `id`: 현재 페이지 로드 맥락에서 메트릭의 고유 식별자
  * `name`: 성능 메트릭의 이름입니다. 가능한 값에는 웹 애플리케이션에 특화된 [Web Vitals](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals#web-vitals) 메트릭 이름(TTFB, FCP, LCP, FID, CLS)이 포함됩니다.
  * `delta`: 메트릭의 현재 값과 이전 값의 차이입니다. 일반적으로 밀리초 단위이며, 시간에 따른 메트릭 값 변화량을 나타냅니다.
  * `entries`: 메트릭과 연결된 [Performance Entries](https://developer.mozilla.org/docs/Web/API/PerformanceEntry)의 배열입니다. 여기에는 해당 메트릭과 관련된 성능 이벤트에 대한 자세한 정보가 담깁니다.
  * `navigationType`: 메트릭 수집을 트리거한 [탐색 유형](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming/type)을 나타냅니다. 가능한 값에는 `"navigate"`, `"reload"`, `"back_forward"`, `"prerender"`가 있습니다.
  * `rating`: 메트릭 값에 대한 정성적 평가로, 성능을 진단합니다. 가능한 값은 `"good"`, `"needs-improvement"`, `"poor"`이며, 일반적으로 허용 가능한 성능과 비최적 성능을 구분하는 사전 정의 임계값과 비교하여 결정됩니다.
  * `value`: 성능 엔트리의 실제 값 또는 지속 시간으로, 일반적으로 밀리초 단위입니다. 이는 해당 메트릭이 추적하는 성능 요소에 대한 정량적 측정을 제공합니다. 값의 출처는 측정 중인 특정 메트릭에 따라 다르며 다양한 [Performance API](https://developer.mozilla.org/docs/Web/API/Performance_API)에서 비롯될 수 있습니다.

## Web Vitals[](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals#web-vitals)

[Web Vitals](https://web.dev/vitals/)는 웹 페이지의 사용자 경험을 포착하기 위한 유용한 메트릭 집합입니다. 다음 웹 바이탈이 모두 포함됩니다.

  * [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
  * [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
  * [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
  * [First Input Delay](https://web.dev/fid/) (FID)
  * [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
  * [Interaction to Next Paint](https://web.dev/inp/) (INP)

이들 메트릭의 모든 결과는 `name` 속성을 사용해 처리할 수 있습니다.

app/components/web-vitals.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useReportWebVitals } from 'next/web-vitals'

    type ReportWebVitalsCallback = Parameters<typeof useReportWebVitals>[0]

    const handleWebVitals: ReportWebVitalsCallback = (metric) => {
      switch (metric.name) {
        case 'FCP': {
          // handle FCP results
        }
        case 'LCP': {
          // handle LCP results
        }
        // ...
      }
    }

    export function WebVitals() {
      useReportWebVitals(handleWebVitals)
    }
[/code]

## 외부 시스템으로 결과 전송[](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals#sending-results-to-external-systems)

사이트에서 실제 사용자 성능을 측정·추적하기 위해 어떤 엔드포인트로든 결과를 전송할 수 있습니다. 예시:

[code]
    function postWebVitals(metrics) {
      const body = JSON.stringify(metric)
      const url = 'https://example.com/analytics'

      // Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
      if (navigator.sendBeacon) {
        navigator.sendBeacon(url, body)
      } else {
        fetch(url, { body, method: 'POST', keepalive: true })
      }
    }

    useReportWebVitals(postWebVitals)
[/code]

> **알아두면 좋아요**: [Google Analytics](https://analytics.google.com/analytics/web/)를 사용하는 경우 `id` 값을 활용해 메트릭 분포를 수동으로 구성(백분위 계산 등)할 수 있습니다.

>
[code]
>     useReportWebVitals(metric => {
>       // Use `window.gtag` if you initialized Google Analytics as this example:
>       // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>       window.gtag('event', metric.name, {
>         value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value), // values must be integers
>         event_label: metric.id, // id unique to current page load
>         non_interaction: true, // avoids affecting bounce rate.
>       });
>     }
[/code]
>
> [Google Analytics로 결과를 전송하는 방법](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics)에 대해 더 알아보세요.

Was this helpful?

supported.

Send
