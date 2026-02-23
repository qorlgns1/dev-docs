---
title: 'Webpack 5 도입'
description: 'Next.js는 기본 컴파일러로 webpack 5를 채택했습니다. webpack 4에서 5로 전환이 최대한 원활하도록 많은 노력을 기울였습니다.'
---

# Webpack 5 도입 | Next.js

출처 URL: https://nextjs.org/docs/messages/webpack5

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)Webpack 5 도입

# Webpack 5 도입

## 이 메시지가 표시된 이유[](https://nextjs.org/docs/messages/webpack5#why-this-message-occurred)

Next.js는 기본 컴파일러로 webpack 5를 채택했습니다. webpack 4에서 5로 전환이 최대한 원활하도록 많은 노력을 기울였습니다.

현재 애플리케이션에서는 Next.js 12에서 제거된 `webpack5: false` 플래그를 사용해 webpack 5를 비활성화하고 있습니다:

next.config.js
```
    module.exports = {
      // Webpack 5 is enabled by default
      // You can still use webpack 4 while upgrading to the latest version of Next.js by adding the "webpack5: false" flag
      webpack5: false,
    }
```

애플리케이션에서 webpack 5를 사용하면 특히 다음과 같은 이점이 있습니다.

  * 향상된 디스크 캐싱: 이후 `next build` 실행 속도가 크게 빨라집니다
  * 향상된 Fast Refresh: Fast Refresh 작업이 우선 처리됩니다
  * 향상된 장기 자산 캐싱: 빌드 간 변경 가능성이 낮은 결정적 코드 출력
  * 향상된 트리 셰이킹
  * `new URL("file.png", import.meta.url)`을 사용하는 자산 지원
  * `new Worker(new URL("worker.js", import.meta.url))`을 사용하는 웹 워커 지원
  * `package.json`의 `exports`/`imports` 필드 지원

과거 릴리스에서는 Next.js 애플리케이션에 webpack 5를 점진적으로 도입했습니다.

  * Next.js 10.2에서는 `next.config.js`에 커스텀 webpack 구성이 없는 애플리케이션을 자동으로 옵트인했습니다
  * Next.js 10.2에서는 `next.config.js`가 없는 애플리케이션을 자동으로 옵트인했습니다
  * Next.js 11에서는 모든 애플리케이션에서 기본적으로 webpack 5가 활성화되었습니다. 여전히 `next.config.js`에 `webpack5: false`를 설정해 webpack 4를 사용하며 하위 호환성을 유지할 수 있었습니다
  * Next.js 12에서는 webpack 4 지원이 제거되었습니다

## 커스텀 webpack 구성[](https://nextjs.org/docs/messages/webpack5#custom-webpack-configuration)

커스텀 플러그인이나 자체 수정으로 webpack 구성을 사용 중인 경우, 애플리케이션이 webpack 5와 호환되도록 몇 가지 단계를 따라야 합니다.

  * `next-transpile-modules`를 사용할 때는 [이 패치](https://github.com/martpie/next-transpile-modules/pull/179)가 포함된 최신 버전을 사용하세요
  * `@zeit/next-css` / `@zeit/next-sass`를 사용할 때는 대신 [내장 CSS/Sass 지원](https://nextjs.org/docs/app/getting-started/css)을 사용하세요
  * `@zeit/next-preact`를 사용할 때는 [이 예제](https://github.com/vercel/next.js/tree/canary/examples/using-preact)를 사용하세요
  * `@zeit/next-source-maps`를 사용할 때는 [내장 프로덕션 소스 맵 지원](https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)을 사용하세요
  * webpack 플러그인을 사용할 때는 해당 플러그인이 최신 버전으로 업그레이드되었는지 확인하세요. 대부분의 경우 최신 버전에 webpack 5 지원이 포함됩니다. 일부 업그레이드된 플러그인은 webpack 5만 지원할 수 있습니다

## 유용한 링크[](https://nextjs.org/docs/messages/webpack5#useful-links)

문제가 발생하면 [이 도움말 토론](https://github.com/vercel/next.js/discussions/23498)에서 커뮤니티와 교류할 수 있습니다.