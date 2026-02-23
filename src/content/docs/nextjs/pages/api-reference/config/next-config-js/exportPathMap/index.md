---
title: 'next.config.js 옵션: exportPathMap'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js 옵션: exportPathMap | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)exportPathMap

Copy page

# exportPathMap

마지막 업데이트 2026년 2월 20일

> 이 기능은 `next export` 전용이며 현재 `pages`의 `getStaticPaths`나 `app`의 `generateStaticParams`를 대신하도록 **deprecated** 상태입니다.

`exportPathMap`을 사용하면 내보내기 시 요청 경로와 페이지 목적지 간의 매핑을 지정할 수 있습니다. `exportPathMap`에 정의된 경로는 [`next dev`](https://nextjs.org/docs/app/api-reference/cli/next#next-dev-options)를 사용할 때도 제공됩니다.

다음과 같은 페이지를 가진 앱에서 사용자 지정 `exportPathMap`을 만드는 예시로 시작해 보겠습니다.

  * `pages/index.js`
  * `pages/about.js`
  * `pages/post.js`



`next.config.js`를 열고 다음 `exportPathMap` 구성을 추가합니다:

next.config.js
[code]
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
[/code]

> **알아두면 좋은 점**: `exportPathMap`의 `query` 필드는 [자동 정적 최적화 페이지](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)나 [`getStaticProps` 페이지](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)와 함께 사용할 수 없습니다. 이들은 빌드 타임에 HTML 파일로 렌더링되므로 `next export` 중 추가 쿼리 정보를 전달할 수 없습니다.

이후 페이지는 HTML 파일로 내보내지며, 예를 들어 `/about`은 `/about.html`이 됩니다.

`exportPathMap`은 두 개의 인수를 받는 `async` 함수입니다. 첫 번째 인수 `defaultPathMap`은 Next.js가 사용하는 기본 맵입니다. 두 번째 인수는 다음 속성을 가진 객체입니다.

  * `dev` \- 개발 환경에서 `exportPathMap`이 호출되면 `true`, `next export` 실행 시에는 `false`. 개발 환경에서는 `exportPathMap`으로 라우트를 정의합니다.
  * `dir` \- 프로젝트 디렉터리의 절대 경로
  * `outDir` \- `out/` 디렉터리의 절대 경로 ([`-o`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap#customizing-the-output-directory)로 구성 가능). `dev`가 `true`이면 `outDir` 값은 `null`입니다.
  * `distDir` \- `.next/` 디렉터리의 절대 경로 ([`distDir`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir) 구성으로 설정 가능)
  * `buildId` \- 생성된 빌드 ID



반환된 객체는 페이지 맵이며 `key`는 `pathname`, `value`는 다음 필드를 받는 객체입니다.

  * `page`: `String` \- 렌더링할 `pages` 디렉터리 내부 페이지
  * `query`: `Object` \- 프리렌더링 시 `getInitialProps`에 전달되는 `query` 객체. 기본값은 `{}`



> 내보낸 `pathname`은 `/readme.md`처럼 파일 이름이 될 수도 있지만, 확장자가 `.html`이 아니라면 콘텐츠를 서빙할 때 `Content-Type` 헤더를 `text/html`로 설정해야 할 수 있습니다.

## 후행 슬래시 추가하기[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap#adding-a-trailing-slash)

Next.js를 구성해 페이지를 `index.html` 파일로 내보내고 후행 슬래시를 요구하도록 할 수 있습니다. `/about`은 `/about/index.html`이 되고 `/about/` 경로로 라우팅됩니다. 이는 Next.js 9 이전의 기본 동작이었습니다.

다시 이 방식으로 전환하고 후행 슬래시를 추가하려면 `next.config.js`를 열고 `trailingSlash` 구성을 활성화하세요:

next.config.js
[code]
    module.exports = {
      trailingSlash: true,
    }
[/code]

## 출력 디렉터리 사용자 지정하기[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap#customizing-the-output-directory)

[`next export`](https://nextjs.org/docs/pages/guides/static-exports)는 기본 출력 디렉터리로 `out`을 사용합니다. `-o` 인수를 사용해 다음과 같이 사용자 지정할 수 있습니다:

Terminal
[code]
    next export -o outdir
[/code]

> **Warning** : `exportPathMap` 사용은 deprecated 상태이며 `pages` 내부의 `getStaticPaths`가 우선합니다. 두 기능을 함께 사용하는 것은 권장하지 않습니다.

Was this helpful?

supported.

Send
