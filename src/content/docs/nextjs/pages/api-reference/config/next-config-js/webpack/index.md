---
title: 'next.config.js 옵션: webpack'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js 옵션: webpack | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack

[구성](https://nextjs.org/docs/pages/api-reference/config)[next.config.js 옵션](https://nextjs.org/docs/pages/api-reference/config/next-config-js)webpack

Copy page

# 사용자 지정 Webpack 구성

마지막 업데이트 2026년 2월 20일

> **알아두면 좋아요**: webpack 구성 변경은 semver 보장에 포함되지 않으므로 위험을 감수하고 진행하세요

애플리케이션에 사용자 지정 webpack 구성을 추가하기 전에 Next.js가 이미 사용 사례를 지원하는지 확인하세요:

  * [CSS imports](https://nextjs.org/docs/app/getting-started/css)
  * [CSS modules](https://nextjs.org/docs/app/getting-started/css)
  * [Sass/SCSS imports](https://nextjs.org/docs/pages/guides/sass)
  * [Sass/SCSS modules](https://nextjs.org/docs/pages/guides/sass)
  * [babel 구성 사용자 지정](https://nextjs.org/docs/pages/guides/babel)



일부 자주 요청되는 기능은 플러그인으로 사용할 수 있습니다:

  * [@next/mdx](https://github.com/vercel/next.js/tree/canary/packages/next-mdx)
  * [@next/bundle-analyzer](https://github.com/vercel/next.js/tree/canary/packages/next-bundle-analyzer)



`webpack` 사용을 확장하려면 `next.config.js` 내부에서 구성 객체를 확장하는 함수를 아래와 같이 정의할 수 있습니다:

next.config.js
[code]
    module.exports = {
      webpack: (
        config,
        { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
      ) => {
        // Important: return the modified config
        return config
      },
    }
[/code]

> `webpack` 함수는 총 세 번 실행되며, 서버(nodejs / edge 런타임)를 위해 두 번, 클라이언트를 위해 한 번 실행됩니다. 이를 통해 `isServer` 속성을 사용해 클라이언트와 서버 구성을 구분할 수 있습니다.

`webpack` 함수의 두 번째 인수는 다음 속성을 가진 객체입니다:

  * `buildId`: `String` - 빌드 간 고유 식별자로 사용되는 빌드 ID.
  * `dev`: `Boolean` - 개발 모드로 컴파일되는지 여부를 나타냅니다.
  * `isServer`: `Boolean` - 서버 사이드 컴파일이면 `true`, 클라이언트 사이드 컴파일이면 `false`입니다.
  * `nextRuntime`: `String | undefined` - 서버 사이드 컴파일의 대상 런타임으로 `"edge"` 또는 `"nodejs"` 중 하나이며, 클라이언트 사이드 컴파일에서는 `undefined`입니다.
  * `defaultLoaders`: `Object` - Next.js가 내부적으로 사용하는 기본 로더:
    * `babel`: `Object` - 기본 `babel-loader` 구성.



`defaultLoaders.babel` 사용 예시:
[code] 
    // Example config for adding a loader that depends on babel-loader
    // This source was taken from the @next/mdx plugin source:
    // https://github.com/vercel/next.js/tree/canary/packages/next-mdx
    module.exports = {
      webpack: (config, options) => {
        config.module.rules.push({
          test: /\.mdx/,
          use: [
            options.defaultLoaders.babel,
            {
              loader: '@mdx-js/loader',
              options: pluginOptions.options,
            },
          ],
        })
     
        return config
      },
    }
[/code]

#### `nextRuntime`[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack#nextruntime)

`nextRuntime`가 `"edge"` 또는 `"nodejs"`일 때 `isServer`는 `true`임에 유의하세요. `nextRuntime` `"edge"`는 현재 프록시 및 edge 런타임의 Server Components에만 사용됩니다.

Was this helpful?

supported.

Send
