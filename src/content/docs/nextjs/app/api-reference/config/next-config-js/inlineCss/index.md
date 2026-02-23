---
title: 'next.config.js: inlineCss'
description: '이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 사용해 보고 GitHub에 피드백을 공유해 주세요.'
---

# next.config.js: inlineCss | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss

# inlineCss

이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에 피드백을 공유해 주세요.

마지막 업데이트 2026년 2월 20일

## 사용법[](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss#usage)

`<head>` 안에 CSS를 인라인하는 실험적 지원입니다. 이 플래그를 활성화하면 일반적으로 `<link>` 태그를 생성하던 모든 위치에 대신 생성된 `<style>` 태그가 사용됩니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        inlineCss: true,
      },
    }

    export default nextConfig
[/code]

## 트레이드오프[](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss#trade-offs)

  * **활성화** : Tailwind 같은 아토믹 CSS를 사용하며 신규 방문자의 첫 로드 성능을 최적화하고 싶을 때
  * **건너뛰기** : 재방문자가 많고 캐시된 스타일시트의 이점을 제공하고 싶을 때

### 인라인 CSS가 도움이 되는 경우[](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss#when-inline-css-helps)

일반적으로 브라우저는 HTML을 다운로드하고 파싱한 뒤 CSS `<link>` 태그를 찾아 스타일시트를 요청해야 렌더링할 수 있습니다. 인라인 처리로 [이 요청 워터폴을 제거](https://web.dev/learn/performance/optimize-resource-loading#inline_critical_css)하면 스타일이 HTML과 함께 도착하므로 브라우저가 즉시 렌더링할 수 있습니다.

이 이점은 다음과 같은 상황에서 가장 큽니다.

  * **첫 방문자** : CSS 파일은 렌더링을 차단하므로 인라인하면 첫 방문자가 겪는 초기 다운로드 지연을 제거합니다. 스타일시트를 캐시한 재방문자는 이 혜택을 보지 못합니다.

  * **성능 지표** : CSS 파일에 대한 추가 네트워크 요청을 제거하면 [First Contentful Paint(FCP)](https://web.dev/articles/fcp) 및 [Largest Contentful Paint(LCP)](https://web.dev/articles/lcp)를 크게 개선할 수 있습니다.

  * **느린 연결** : 지연 시간이 높은 네트워크에서는 요청 하나마다 지연이 누적됩니다. 인라인은 왕복 횟수를 줄여 연결이 느릴수록 효과가 큽니다.

  * **아토믹 CSS(Tailwind)** : Utility-first 프레임워크는 사용한 클래스만 생성하여 CSS를 작게 유지합니다. 페이지 스타일이 UI 복잡도에 비례해 커지지 않고 전반적으로 compact 하므로, 성능 이점을 얻으면서 HTML에 큰 부담을 주지 않아 인라인이 실용적입니다.

### 외부 CSS가 더 나은 경우[](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss#when-external-css-is-better)

인라인된 스타일은 HTML과 별도로 캐시할 수 없습니다. 페이지를 불러올 때마다 동일한 CSS가 다시 다운로드됩니다.

이 트레이드오프는 다음 상황에서 특히 중요합니다.

  * **재방문자** : 사이트를 반복 방문하는 사용자는 캐시된 외부 스타일시트의 이점을 봅니다. 인라인하면 방문 때마다 스타일을 다시 다운로드합니다.

  * **큰 CSS 번들** : 외부 스타일시트는 독립적으로 캐시되어 최신 인프라에서 효율적으로 로드됩니다. 인라인 CSS는 모든 HTML 응답에 함께 도착해 [Time to First Byte(TTFB)](https://web.dev/articles/ttfb)를 증가시키고 브라우저가 스타일을 별도로 캐시하지 못하게 합니다. 작은 CSS(예: Tailwind 같은 아토믹 프레임워크)에는 쓸 만하지만, Bootstrap이나 Material UI 같은 대형 번들에는 오버헤드가 커집니다.

  * **스타일을 공유하는 많은 페이지** : 외부 스타일시트를 한 페이지에서 캐시하면 다른 페이지로 이동할 때도 속도가 빨라집니다. 인라인 스타일은 페이지 간 캐시 이점이 없습니다.

> **알아두면 좋은 점** :
>
> 이 기능은 현재 실험 단계이며 다음과 같은 알려진 제한 사항이 있습니다.
>
>   * CSS 인라인은 전역으로 적용되며 페이지별로 구성할 수 없습니다.
>   * 초기 페이지 로드 시 스타일이 `<style>` 태그(SSR)와 RSC 페이로드에 각각 한 번씩 중복됩니다.
>   * 정적으로 렌더링된 페이지로 이동할 때는 중복을 피하기 위해 인라인 CSS 대신 `<link>` 태그를 사용합니다.
>   * 이 기능은 개발 모드에서는 사용할 수 없으며 프로덕션 빌드에서만 동작합니다.
>

supported.

Send
