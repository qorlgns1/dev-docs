---
title: '함수: useReportWebVitals'
description: '훅을 사용하면 Core Web Vitals를 보고할 수 있으며 분석 서비스와 함께 활용할 수 있습니다.'
---

# 함수: useReportWebVitals | Next.js

소스 URL: https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals

# useReportWebVitals

마지막 업데이트: 2026년 2월 20일

`useReportWebVitals` 훅을 사용하면 [Core Web Vitals](https://web.dev/vitals/)를 보고할 수 있으며 분석 서비스와 함께 활용할 수 있습니다.

`useReportWebVitals`에 전달한 새 함수는 그 시점까지 수집된 측정값과 함께 호출됩니다. 중복 보고를 방지하려면 아래 코드 예시처럼 콜백 함수의 참조가 변하지 않도록 하세요.

pages/_app.js
```
    import { useReportWebVitals } from 'next/web-vitals'

    const logWebVitals = (metric) => {
      console.log(metric)
    }

    function MyApp({ Component, pageProps }) {
      useReportWebVitals(logWebVitals)

      return <Component {...pageProps} />
    }
```

## useReportWebVitals[](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals#usereportwebvitals)

훅 인수로 전달되는 `metric` 객체에는 다음 속성이 포함됩니다:

  * `id`: 현재 페이지 로드 맥락에서 메트릭을 식별하는 고유 ID
  * `name`: 성능 메트릭 이름. 웹 애플리케이션에 특화된 [Web Vitals](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals#web-vitals) 지표 이름(TTFB, FCP, LCP, FID, CLS 등)일 수 있습니다.
  * `delta`: 현재 값과 이전 값의 차이. 보통 밀리초 단위로, 시간에 따른 메트릭 변화량을 나타냅니다.
  * `entries`: 해당 메트릭과 연관된 [Performance Entries](https://developer.mozilla.org/docs/Web/API/PerformanceEntry) 배열로, 관련 성능 이벤트에 대한 상세 정보를 제공합니다.
  * `navigationType`: 메트릭 수집을 촉발한 [탐색 유형](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming/type)을 나타냅니다. 가능한 값은 `"navigate"`, `"reload"`, `"back_forward"`, `"prerender"`입니다.
  * `rating`: 메트릭 값을 정성적으로 평가한 결과로, 성능 상태를 알려줍니다. 가능한 값은 `"good"`, `"needs-improvement"`, `"poor"`이며, 미리 정의된 임계값과 비교해 결정합니다.
  * `value`: 성능 항목의 실제 값 또는 지속 시간(보통 밀리초). 측정 중인 메트릭에 따라 다양한 [Performance API](https://developer.mozilla.org/docs/Web/API/Performance_API)에서 가져옵니다.

## 웹 바이탈(Web Vitals)[](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals#web-vitals)

[Web Vitals](https://web.dev/vitals/)는 웹 페이지의 사용자 경험을 포착하기 위한 유용한 지표 모음입니다. 다음 지표가 모두 포함됩니다:

  * [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
  * [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
  * [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
  * [First Input Delay](https://web.dev/fid/) (FID)
  * [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
  * [Interaction to Next Paint](https://web.dev/inp/) (INP)

`name` 속성을 사용하면 이러한 모든 메트릭 결과를 처리할 수 있습니다.

pages/_app.js
```
    import { useReportWebVitals } from 'next/web-vitals'

    const handleWebVitals = (metric) => {
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

    function MyApp({ Component, pageProps }) {
      useReportWebVitals(handleWebVitals)

      return <Component {...pageProps} />
    }
```

## 맞춤 메트릭[](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals#custom-metrics)

위 핵심 지표 외에도 페이지가 하이드레이션되고 렌더링되는 데 걸리는 시간을 측정하는 맞춤 메트릭이 있습니다:

  * `Next.js-hydration`: 페이지가 하이드레이션을 시작하고 완료하는 데 걸린 시간(ms)
  * `Next.js-route-change-to-render`: 라우트 변경 이후 렌더링이 시작되기까지 걸린 시간(ms)
  * `Next.js-render`: 라우트 변경 이후 렌더링이 완료될 때까지 걸린 시간(ms)

이 메트릭 결과는 각각 별도로 처리할 수 있습니다:

pages/_app.js
```
    import { useReportWebVitals } from 'next/web-vitals'

    function handleCustomMetrics(metrics) {
      switch (metric.name) {
        case 'Next.js-hydration':
          // handle hydration results
          break
        case 'Next.js-route-change-to-render':
          // handle route-change to render results
          break
        case 'Next.js-render':
          // handle render results
          break
        default:
          break
      }
    }

    function MyApp({ Component, pageProps }) {
      useReportWebVitals(handleCustomMetrics)

      return <Component {...pageProps} />
    }
```

이 메트릭은 [User Timing API](https://caniuse.com/#feat=user-timing)를 지원하는 모든 브라우저에서 동작합니다.

## 결과를 외부 시스템으로 보내기[](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals#sending-results-to-external-systems)

사이트의 실제 사용자 성능을 측정하고 추적할 수 있도록 어떤 엔드포인트로든 결과를 전송할 수 있습니다. 예:

```
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
```

> **알아두면 좋아요** : [Google Analytics](https://analytics.google.com/analytics/web/)를 사용한다면 `id` 값을 통해 직접 메트릭 분포(백분위수 계산 등)를 구성할 수 있습니다.
>
> ```
>     useReportWebVitals(metric => {
>       // Use `window.gtag` if you initialized Google Analytics as this example:
>       // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>       window.gtag('event', metric.name, {
>         value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value), // values must be integers
>         event_label: metric.id, // id unique to current page load
>         non_interaction: true, // avoids affecting bounce rate.
>       });
>     }
> ```
>
> [Google Analytics로 결과 보내기](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics)에 대해 더 알아보세요.