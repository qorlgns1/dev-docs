---
title: 'next.config.js: exportPathMap'
description: '이 API는 레거시이므로 더 이상 권장되지 않습니다. 하위 호환성을 위해서만 계속 지원됩니다.'
---

# next.config.js: exportPathMap | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap

Copy page

# exportPathMap

이 API는 레거시이므로 더 이상 권장되지 않습니다. 하위 호환성을 위해서만 계속 지원됩니다.

마지막 업데이트 2026년 2월 20일

> 이 기능은 `next export`에만 해당하며 현재 `pages`에서 `getStaticPaths`, `app`에서 `generateStaticParams`를 사용하는 방식으로 **더 이상 권장되지 않습니다**.

`exportPathMap`은 내보내기 과정에서 사용할 요청 경로와 페이지 목적지 간의 매핑을 지정할 수 있게 해줍니다. `exportPathMap`에 정의된 경로는 [`next dev`](https://nextjs.org/docs/app/api-reference/cli/next#next-dev-options)를 사용할 때도 이용할 수 있습니다.

다음과 같은 페이지를 가진 앱에 대해 커스텀 `exportPathMap`을 만드는 예시로 시작해 보겠습니다.

  * `pages/index.js`
  * `pages/about.js`
  * `pages/post.js`

`next.config.js`를 열어 다음과 같은 `exportPathMap` 설정을 추가하세요:

next.config.js
```js
    module.exports = {
      exportPathMap: async function (
        defaultPathMap,
        { dev, dir, outDir, distDir, buildId }
      ) {
        return {
          '/': { page: '/' },
          '/about': { page: '/about' },
          '/p/hello-nextjs': { page: '/post', query: { title: 'hello-nextjs' } },
          '/p/learn-nextjs': { page: '/post', query: { title: 'learn-nextjs' } },
          '/p/deploy-nextjs': { page: '/post', query: { title: 'deploy-nextjs' } },
        }
      },
    }
```

> **알아두면 좋아요**: `exportPathMap`의 `query` 필드는 [자동 정적 최적화 페이지](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)나 [`getStaticProps` 페이지](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)와 함께 사용할 수 없습니다. 이러한 페이지는 빌드 시 HTML 파일로 렌더링되므로 `next export` 중 추가적인 쿼리 정보를 제공할 수 없습니다.

이후 페이지는 HTML 파일로 내보내지며, 예를 들어 `/about`은 `/about.html`이 됩니다.

`exportPathMap`은 2개의 인수를 받는 `async` 함수입니다. 첫 번째 인수 `defaultPathMap`은 Next.js가 사용하는 기본 매핑입니다. 두 번째 인수는 다음 속성을 가진 객체입니다.

  * `dev` \- 개발 환경에서 `exportPathMap`이 호출되면 `true`, `next export`를 실행 중이면 `false`. 개발 환경에서는 라우트를 정의하기 위해 `exportPathMap`이 사용됩니다.
  * `dir` \- 프로젝트 디렉터리의 절대 경로
  * `outDir` \- `out/` 디렉터리의 절대 경로([`-o`](https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap#customizing-the-output-directory)로 설정 가능). `dev`가 `true`일 때 `outDir` 값은 `null`입니다.
  * `distDir` \- `.next/` 디렉터리의 절대 경로([`distDir`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir) 설정으로 구성 가능)
  * `buildId` \- 생성된 빌드 ID

반환된 객체는 페이지 맵이며 `key`는 `pathname`, `value`는 아래 필드를 받는 객체입니다.

  * `page`: `String` \- 렌더링할 `pages` 디렉터리 내의 페이지
  * `query`: `Object` \- 프리렌더링 시 `getInitialProps`로 전달되는 `query` 객체. 기본값은 `{}`입니다.

> 내보낸 `pathname`은 `/readme.md`와 같이 파일명이 될 수도 있지만, `.html`이 아니라면 콘텐츠를 제공할 때 `Content-Type` 헤더를 `text/html`로 설정해야 할 수 있습니다.

## 슬래시 추가[](https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap#adding-a-trailing-slash)

Next.js가 페이지를 `index.html` 파일로 내보내고 트레일링 슬래시를 요구하도록 구성할 수 있습니다. 이 경우 `/about`은 `/about/index.html`이 되고 `/about/` 경로로 라우팅됩니다. 이는 Next.js 9 이전의 기본 동작이었습니다.

이전 동작으로 돌아가 트레일링 슬래시를 추가하려면, `next.config.js`를 열고 `trailingSlash` 설정을 활성화하면 됩니다.

next.config.js
```js
    module.exports = {
      trailingSlash: true,
    }
```

## 출력 디렉터리 커스터마이징[](https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap#customizing-the-output-directory)

[`next export`](https://nextjs.org/docs/app/guides/static-exports)는 기본적으로 `out` 디렉터리를 출력 디렉터리로 사용하지만, 다음과 같이 `-o` 인수를 사용해 원하는 디렉터리로 변경할 수 있습니다.

Terminal
```
    next export -o outdir
```

> **경고**: `exportPathMap`은 더 이상 권장되지 않으며 `pages` 내부의 `getStaticPaths`에 의해 대체됩니다. 두 기능을 함께 사용하는 것은 권장되지 않습니다.

Was this helpful?

supported.

Send
