---
title: 'next.config.js 옵션: webVitalsAttribution'
description: '원본 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution'
---

# next.config.js 옵션: webVitalsAttribution | Next.js

원본 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution

# webVitalsAttribution

최종 업데이트 2026년 2월 20일

웹 바이탈(Web Vitals)과 관련된 문제를 디버깅할 때는 문제의 근원을 정확히 찾아내면 큰 도움이 됩니다. 예를 들어 CLS(Cumulative Layout Shift)가 발생했을 때는 가장 큰 레이아웃 시프트가 일어났을 당시 처음으로 이동한 요소가 무엇인지 알고 싶을 수 있습니다. LCP(Largest Contentful Paint)의 경우에는 해당 페이지의 LCP에 해당하는 요소를 찾아야 할 수 있습니다. LCP 요소가 이미지라면 해당 이미지 리소스의 URL을 알면 최적화해야 할 에셋을 파악하는 데 도움이 됩니다.

웹 바이탈 점수에 가장 큰 영향을 주는 원인을 찾아내는, 즉 [어트리뷰션](https://github.com/GoogleChrome/web-vitals/blob/4ca38ae64b8d1e899028c692f94d4c56acfc996c/README.md#attribution)을 수행하면 [PerformanceEventTiming](https://developer.mozilla.org/docs/Web/API/PerformanceEventTiming), [PerformanceNavigationTiming](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming), [PerformanceResourceTiming](https://developer.mozilla.org/docs/Web/API/PerformanceResourceTiming) 항목처럼 더욱 심층적인 정보를 얻을 수 있습니다.

어트리뷰션은 Next.js에서 기본적으로 비활성화되어 있으며, 아래와 같이 `next.config.js`에서 **메트릭별로** 설정해 활성화할 수 있습니다.

next.config.js
```
    module.exports = {
      experimental: {
        webVitalsAttribution: ['CLS', 'LCP'],
      },
    }
```

허용되는 어트리뷰션 값은 [`NextWebVitalsMetric`](https://github.com/vercel/next.js/blob/442378d21dd56d6e769863eb8c2cb521a463a2e0/packages/next/shared/lib/utils.ts#L43) 타입에 지정된 모든 `web-vitals` 메트릭입니다.