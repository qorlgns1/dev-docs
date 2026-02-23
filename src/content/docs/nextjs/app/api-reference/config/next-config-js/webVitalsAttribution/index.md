---
title: 'next.config.js: webVitalsAttribution'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에는 권장되지 않습니다. 대신 사용해 보고 GitHub에서 피드백을 공유해주세요.'
---

# next.config.js: webVitalsAttribution | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)webVitalsAttribution

페이지 복사

# webVitalsAttribution

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에는 권장되지 않습니다. 대신 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해주세요.

마지막 업데이트: 2026년 2월 20일

Web Vitals 관련 문제를 디버깅할 때는 문제의 근원을 정확히 짚어내는 것이 도움이 됩니다. 예를 들어 CLS(Cumulative Layout Shift)의 경우, 가장 큰 단일 레이아웃 시프트가 발생했을 때 처음으로 이동한 요소가 무엇인지 알고 싶을 수 있습니다. LCP(Largest Contentful Paint)의 경우 페이지에서 LCP에 해당하는 요소가 무엇인지 식별하고 싶을 수 있습니다. LCP 요소가 이미지라면 해당 이미지 리소스의 URL을 알면 최적화해야 할 자산을 빠르게 찾을 수 있습니다.

[attribution](https://github.com/GoogleChrome/web-vitals/blob/4ca38ae64b8d1e899028c692f94d4c56acfc996c/README.md#attribution)이라고도 부르는 Web Vitals 점수에 가장 크게 기여하는 요소를 정확히 짚어내면, [PerformanceEventTiming](https://developer.mozilla.org/docs/Web/API/PerformanceEventTiming), [PerformanceNavigationTiming](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming), [PerformanceResourceTiming](https://developer.mozilla.org/docs/Web/API/PerformanceResourceTiming) 항목처럼 보다 심층적인 정보를 얻을 수 있습니다.

Next.js에서는 기본적으로 attribution이 비활성화되어 있지만, `next.config.js`에서 다음과 같이 **지표별로** 설정해 활성화할 수 있습니다.

next.config.js
```js
    module.exports = {
      experimental: {
        webVitalsAttribution: ['CLS', 'LCP'],
      },
    }
```

유효한 attribution 값은 [`NextWebVitalsMetric`](https://github.com/vercel/next.js/blob/442378d21dd56d6e769863eb8c2cb521a463a2e0/packages/next/shared/lib/utils.ts#L43) 타입에 지정된 모든 `web-vitals` 지표입니다.

도움이 되었나요?

지원됨.

보내기
