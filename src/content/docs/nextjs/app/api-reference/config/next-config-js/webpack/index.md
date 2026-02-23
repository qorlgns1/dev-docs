---
title: 'next.config.js: webpack'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack'
---

# next.config.js: webpack | Next.js

원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack

# 커스텀 Webpack 구성

마지막 업데이트 2026년 2월 20일

> **알아두면 좋아요** : webpack 구성 변경은 semver 보증을 받지 않으므로 위험을 감수하고 진행하세요.

애플리케이션에 커스텀 webpack 구성을 추가하기 전에 Next.js가 이미 해당 사용 사례를 지원하는지 확인하세요:

  * [CSS imports](https://nextjs.org/docs/app/getting-started/css)
  * [CSS modules](https://nextjs.org/docs/app/getting-started/css#css-modules)
  * [Sass/SCSS imports](https://nextjs.org/docs/app/guides/sass)
  * [Sass/SCSS modules](https://nextjs.org/docs/app/guides/sass)

자주 요청되는 몇몇 기능은 플러그인으로 제공됩니다:

  * [@next/mdx](https://github.com/vercel/next.js/tree/canary/packages/next-mdx)
  * [@next/bundle-analyzer](https://github.com/vercel/next.js/tree/canary/packages/next-bundle-analyzer)

`webpack` 사용을 확장하려면 `next.config.js` 안에서 구성을 확장하는 함수를 다음과 같이 정의할 수 있습니다:

next.config.js
```
    module.exports = {
      webpack: (
        config,
        { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
      ) => {
        // Important: return the modified config
        return config
      },
    }
```

> `webpack` 함수는 서버용(nodejs / edge runtime)으로 두 번, 클라이언트용으로 한 번 총 세 번 실행됩니다. 이를 통해 `isServer` 속성을 사용해 클라이언트와 서버 구성을 구분할 수 있습니다.

`webpack` 함수의 두 번째 인수는 다음 속성을 가진 객체입니다:

  * `buildId`: `String` \- 빌드 간 고유 식별자로 사용되는 빌드 ID입니다.
  * `dev`: `Boolean` \- 컴파일이 개발 환경에서 수행되는지 나타냅니다.
  * `isServer`: `Boolean` \- 서버 사이드 컴파일이면 `true`, 클라이언트 사이드 컴파일이면 `false`입니다.
  * `nextRuntime`: `String | undefined` \- 서버 사이드 컴파일의 대상 런타임으로 `"edge"` 또는 `"nodejs"` 중 하나이며, 클라이언트 사이드 컴파일에서는 `undefined`입니다.
  * `defaultLoaders`: `Object` \- Next.js가 내부적으로 사용하는 기본 로더입니다:
    * `babel`: `Object` \- 기본 `babel-loader` 구성.

`defaultLoaders.babel` 사용 예시:
```
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
```

#### `nextRuntime`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack#nextruntime)

`nextRuntime`가 `"edge"` 또는 `"nodejs"`일 때 `isServer`는 `true`이며, `"edge"`인 `nextRuntime`은 현재 프록시와 Edge Runtime에서의 Server Components에만 사용됩니다.

보내기