---
title: '렌더링: 자동 정적 최적화'
description: '마지막 업데이트 2026년 2월 20일'
---

# 렌더링: 자동 정적 최적화 | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization

[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application)[렌더링](https://nextjs.org/docs/pages/building-your-application/rendering)자동 정적 최적화

페이지 복사

# 자동 정적 최적화

마지막 업데이트 2026년 2월 20일

Next.js는 페이지에 차단형 데이터 요구 사항이 없으면 해당 페이지가 정적(사전 렌더링 가능)이라고 자동으로 판단합니다. 이 판단은 페이지에 `getServerSideProps`와 `getInitialProps`가 없는지 여부로 이루어집니다.

이 기능을 통해 Next.js는 **서버 렌더링 페이지와 정적으로 생성된 페이지를 모두 포함하는** 하이브리드 애플리케이션을 생성할 수 있습니다.

> **알아두면 좋아요** : 정적으로 생성된 페이지도 여전히 반응형입니다. Next.js는 애플리케이션을 클라이언트 측에서 하이드레이션하여 완전한 인터랙티브성을 제공합니다.

이 기능의 주요 이점 중 하나는 최적화된 페이지가 서버 측 연산을 필요로 하지 않으며, 여러 CDN 위치에서 즉시 최종 사용자에게 스트리밍될 수 있다는 점입니다. 그 결과 사용자에게 _매우 빠른_ 로딩 경험을 제공합니다.

## 작동 방식[](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization#how-it-works)

페이지에 `getServerSideProps` 또는 `getInitialProps`가 있으면 Next.js는 해당 페이지를 요청마다 온디맨드로 렌더링하도록 전환합니다(즉, [서버 사이드 렌더링](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering))을 의미).

위 조건이 아니라면 Next.js는 페이지를 정적 HTML로 사전 렌더링하여 자동으로 **정적 최적화**합니다.

사전 렌더링 중에는 이 단계에서 제공할 `query` 정보가 없기 때문에 라우터의 `query` 객체가 비어 있습니다. 하이드레이션 이후 Next.js는 애플리케이션을 업데이트하여 `query` 객체에 경로 매개변수를 제공합니다.

하이드레이션 후 다시 렌더링이 트리거되면서 `query`가 업데이트되는 경우는 다음과 같습니다.

  * 페이지가 [동적 경로](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)인 경우
  * 페이지 URL에 쿼리 값이 있는 경우
  * `next.config.js`에 [Rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites)를 구성한 경우(해석하여 `query`에 제공해야 할 매개변수가 있을 수 있음)

`query`가 완전히 업데이트되어 사용할 준비가 됐는지 구분하려면 [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)의 `isReady` 필드를 활용할 수 있습니다.

> **알아두면 좋아요** : [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)를 사용하는 페이지에 [동적 경로](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)로 추가된 매개변수는 항상 `query` 객체 안에서 사용할 수 있습니다.

`next build`는 정적으로 최적화된 페이지에 대해 `.html` 파일을 생성합니다. 예를 들어 `pages/about.js` 페이지의 결과는 다음과 같습니다.

Terminal
[code]
    .next/server/pages/about.html
[/code]

그리고 페이지에 `getServerSideProps`를 추가하면 다음과 같이 JavaScript가 생성됩니다.

Terminal
[code]
    .next/server/pages/about.js
[/code]

## 주의사항[](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization#caveats)

  * `getInitialProps`가 있는 [사용자 정의 `App`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)을 사용하면 [정적 생성](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)이 없는 페이지에서는 이 최적화가 비활성화됩니다.
  * `getInitialProps`가 있는 [사용자 정의 `Document`](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)를 사용하는 경우 페이지가 서버 사이드 렌더링된다고 가정하기 전에 반드시 `ctx.req`가 정의되어 있는지 확인하세요. 사전 렌더링된 페이지에서는 `ctx.req`가 `undefined`입니다.
  * 라우터의 `isReady` 필드가 `true`가 될 때까지 렌더링 트리에서 [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)의 `asPath` 값을 사용하는 것을 피하세요. 정적으로 최적화된 페이지는 서버가 아닌 클라이언트에서만 `asPath`를 알 수 있으므로 이를 prop으로 사용하면 불일치 오류가 발생할 수 있습니다. [`active-class-name` 예제](https://github.com/vercel/next.js/tree/canary/examples/active-class-name)는 `asPath`를 prop으로 사용하는 한 가지 방법을 보여줍니다.

도움이 되었나요?

지원됨.

전송
