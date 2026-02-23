---
title: '가이드: Analytics'
description: '최종 업데이트: 2026년 2월 20일'
---

# 가이드: Analytics | Next.js

Source URL: https://nextjs.org/docs/pages/guides/analytics

# 애널리틱스 설정 방법

최종 업데이트: 2026년 2월 20일

Next.js는 성능 메트릭을 측정하고 보고하는 기능을 기본 제공한다. [`useReportWebVitals`](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals) 훅을 사용해 직접 보고 로직을 관리할 수도 있고, Vercel이 제공하는 [관리형 서비스](https://vercel.com/analytics?utm_source=next-site&utm_medium=docs&utm_campaign=next-website)를 통해 메트릭을 자동으로 수집하고 시각화할 수도 있다.

## 클라이언트 계측[](https://nextjs.org/docs/pages/guides/analytics#client-instrumentation)

고급 애널리틱스와 모니터링이 필요하다면, Next.js는 애플리케이션 프런트엔드 코드가 실행되기 전에 동작하는 `instrumentation-client.js|ts` 파일을 제공한다. 이를 활용해 글로벌 애널리틱스, 오류 추적, 성능 모니터링 도구를 설정하기에 적합하다.

사용하려면 애플리케이션 루트 디렉터리에 `instrumentation-client.js` 또는 `instrumentation-client.ts` 파일을 생성한다:

instrumentation-client.js
[code]
    // Initialize analytics before the app starts
    console.log('Analytics initialized')

    // Set up global error tracking
    window.addEventListener('error', (event) => {
      // Send to your error tracking service
      reportError(event.error)
    })
[/code]

## 직접 구축하기[](https://nextjs.org/docs/pages/guides/analytics#build-your-own)

pages/_app.js
[code]
    import { useReportWebVitals } from 'next/web-vitals'

    function MyApp({ Component, pageProps }) {
      useReportWebVitals((metric) => {
        console.log(metric)
      })

      return <Component {...pageProps} />
    }
[/code]

자세한 내용은 [API Reference](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals)를 참고한다.

## Web Vitals[](https://nextjs.org/docs/pages/guides/analytics#web-vitals)

[Web Vitals](https://web.dev/vitals/)는 웹 페이지의 사용자 경험을 포착하기 위한 유용한 메트릭 모음이다. 다음 Web Vitals가 모두 포함된다.

  * [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
  * [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
  * [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
  * [First Input Delay](https://web.dev/fid/) (FID)
  * [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
  * [Interaction to Next Paint](https://web.dev/inp/) (INP)

`name` 속성을 사용하면 이러한 메트릭의 모든 결과를 처리할 수 있다.

pages/_app.js
[code]
    import { useReportWebVitals } from 'next/web-vitals'

    function MyApp({ Component, pageProps }) {
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

      return <Component {...pageProps} />
    }
[/code]

## 사용자 지정 메트릭[](https://nextjs.org/docs/pages/guides/analytics#custom-metrics)

앞서 나열한 핵심 메트릭 외에도 페이지가 하이드레이션 및 렌더링되는 데 걸리는 시간을 측정하는 추가 사용자 지정 메트릭이 있다.

  * `Next.js-hydration`: 페이지가 하이드레이션을 시작해 완료하기까지 걸린 시간(ms)
  * `Next.js-route-change-to-render`: 라우트 변경 후 페이지가 렌더링을 시작하기까지 걸린 시간(ms)
  * `Next.js-render`: 라우트 변경 후 페이지가 렌더링을 완료하기까지 걸린 시간(ms)

이러한 메트릭 결과를 각각 처리할 수 있다.
[code]
    export function reportWebVitals(metric) {
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
[/code]

이 메트릭은 [User Timing API](https://caniuse.com/#feat=user-timing)를 지원하는 모든 브라우저에서 동작한다.

## 외부 시스템으로 결과 전송[](https://nextjs.org/docs/pages/guides/analytics#sending-results-to-external-systems)

사이트의 실제 사용자 성능을 측정하고 추적하기 위해 어떤 엔드포인트로든 결과를 전송할 수 있다. 예를 들어:
[code]
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
[/code]

> **알아두면 좋은 점**: [Google Analytics](https://analytics.google.com/analytics/web/)를 사용하는 경우 `id` 값을 활용해 직접 메트릭 분포를 구성(백분위 계산 등)할 수 있다.

>
[code]
>     useReportWebVitals((metric) => {
>       // Use `window.gtag` if you initialized Google Analytics as this example:
>       // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>       window.gtag('event', metric.name, {
>         value: Math.round(
>           metric.name === 'CLS' ? metric.value * 1000 : metric.value
>         ), // values must be integers
>         event_label: metric.id, // id unique to current page load
>         non_interaction: true, // avoids affecting bounce rate.
>       })
>     })
[/code]
>
> [Google Analytics로 결과를 전송하는 방법](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics)에 대해 더 읽어보기.

보내기
