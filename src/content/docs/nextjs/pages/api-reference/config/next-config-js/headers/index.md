---
title: 'next.config.js 옵션: 헤더'
description: '헤더를 사용하면 특정 경로로 들어오는 요청에 대한 응답에 사용자 지정 HTTP 헤더를 설정할 수 있습니다.'
---

# next.config.js 옵션: 헤더 | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers

# 헤더

최종 업데이트 2026년 2월 20일

헤더를 사용하면 특정 경로로 들어오는 요청에 대한 응답에 사용자 지정 HTTP 헤더를 설정할 수 있습니다.

사용자 지정 HTTP 헤더를 설정하려면 `next.config.js`의 `headers` 키를 사용할 수 있습니다:

next.config.js
```
    module.exports = {
      async headers() {
        return [
          {
            source: '/about',
            headers: [
              {
                key: 'x-custom-header',
                value: 'my custom header value',
              },
              {
                key: 'x-another-custom-header',
                value: 'my other custom header value',
              },
            ],
          },
        ]
      },
    }
```

`headers`는 `source`와 `headers` 속성을 가진 객체가 들어 있는 배열을 반환해야 하는 async 함수입니다:

  * `source`는 들어오는 요청 경로 패턴입니다.
  * `headers`는 `key`와 `value` 속성을 가진 응답 헤더 객체 배열입니다.
  * `basePath`: `false` 또는 `undefined` \- false이면 일치 시 basePath가 포함되지 않으며, 외부 rewrite에만 사용할 수 있습니다.
  * `locale`: `false` 또는 `undefined` \- 일치 시 locale을 포함하지 않을지 여부입니다.
  * `has`는 `type`, `key`, `value` 속성을 가진 [has 객체](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-cookie-and-query-matching) 배열입니다.
  * `missing`은 `type`, `key`, `value` 속성을 가진 [missing 객체](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-cookie-and-query-matching) 배열입니다.

헤더는 페이지와 `/public` 파일을 포함하는 파일 시스템보다 먼저 확인됩니다.

## 헤더 재정의 동작[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-overriding-behavior)

두 개의 헤더가 동일한 경로와 동일한 헤더 키에 일치하면 마지막 헤더 키가 첫 번째 것을 덮어씁니다. 아래 헤더 구성을 사용하면 `/hello` 경로는 마지막으로 설정된 값이 `world`이므로 `x-hello` 헤더가 `world`가 됩니다.

next.config.js
```
    module.exports = {
      async headers() {
        return [
          {
            source: '/:path*',
            headers: [
              {
                key: 'x-hello',
                value: 'there',
              },
            ],
          },
          {
            source: '/hello',
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
        ]
      },
    }
```

## 경로 매칭[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#path-matching)

경로 매칭이 허용되므로 `/blog/:slug`는 `/blog/first-post`에 일치합니다(중첩 경로 없음):

next.config.js
```
    module.exports = {
      async headers() {
        return [
          {
            source: '/blog/:slug',
            headers: [
              {
                key: 'x-slug',
                value: ':slug', // Matched parameters can be used in the value
              },
              {
                key: 'x-slug-:slug', // Matched parameters can be used in the key
                value: 'my other custom header value',
              },
            ],
          },
        ]
      },
    }
```

패턴 `/blog/:slug`는 `/blog/first-post`와 `/blog/post-1`에는 일치하지만 `/blog/a/b` 같은 중첩 경로에는 일치하지 않습니다. 패턴은 시작 지점에 고정되므로 `/blog/:slug`는 `/archive/blog/first-post`와 일치하지 않습니다.

매개변수에 수식어 `*`(0개 이상), `+`(1개 이상), `?`(0개 또는 1개)를 사용할 수 있습니다. 예를 들어 `/blog/:slug*`는 `/blog`, `/blog/a`, `/blog/a/b/c`에 일치합니다.

자세한 내용은 [path-to-regexp](https://github.com/pillarjs/path-to-regexp) 문서를 참고하세요.

### 와일드카드 경로 매칭[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#wildcard-path-matching)

와일드카드 경로를 매칭하려면 매개변수 뒤에 `*`를 사용할 수 있습니다. 예를 들어 `/blog/:slug*`는 `/blog/a/b/c/d/hello-world`에 일치합니다:

next.config.js
```
    module.exports = {
      async headers() {
        return [
          {
            source: '/blog/:slug*',
            headers: [
              {
                key: 'x-slug',
                value: ':slug*', // Matched parameters can be used in the value
              },
              {
                key: 'x-slug-:slug*', // Matched parameters can be used in the key
                value: 'my other custom header value',
              },
            ],
          },
        ]
      },
    }
```

### 정규식 경로 매칭[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#regex-path-matching)

정규식 경로를 매칭하려면 매개변수 뒤에 괄호로 정규식을 감쌀 수 있습니다. 예를 들어 `/blog/:slug(\\d{1,})`는 `/blog/123`에는 일치하지만 `/blog/abc`에는 일치하지 않습니다:

next.config.js
```
    module.exports = {
      async headers() {
        return [
          {
            source: '/blog/:post(\\d{1,})',
            headers: [
              {
                key: 'x-post',
                value: ':post',
              },
            ],
          },
        ]
      },
    }
```

`(`, `)`, `{`, `}`, `:`, `*`, `+`, `?` 문자는 정규식 경로 매칭에 사용되므로 `source`에서 특수 의미 없이 사용하려면 앞에 `\\`를 붙여 이스케이프해야 합니다:

next.config.js
```
    module.exports = {
      async headers() {
        return [
          {
            // this will match `/english(default)/something` being requested
            source: '/english\\(default\\)/:slug',
            headers: [
              {
                key: 'x-header',
                value: 'value',
              },
            ],
          },
        ]
      },
    }
```

## 헤더, 쿠키, 쿼리 매칭[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-cookie-and-query-matching)

헤더, 쿠키, 쿼리 값이 `has` 필드와 일치하거나 `missing` 필드와 일치하지 않을 때만 헤더를 적용하고 싶다면 해당 필드를 사용할 수 있습니다. 헤더가 적용되려면 `source`와 모든 `has` 항목이 일치하고, 모든 `missing` 항목은 일치하지 않아야 합니다.

`has`와 `missing` 항목에는 아래 필드를 사용할 수 있습니다:

  * `type`: `String` \- `header`, `cookie`, `host`, `query` 중 하나여야 합니다.
  * `key`: `String` \- 선택한 타입에서 일치시킬 키입니다.
  * `value`: `String` 또는 `undefined` \- 확인할 값이며, undefined이면 아무 값이나 일치합니다. 값으로 `first-(?<paramName>.*)`와 같은 정규식 형태의 문자열을 사용하면 `first-second`에서 `second`를 캡처하고 목적지에서 `:paramName`으로 사용할 수 있습니다.

next.config.js
```
    module.exports = {
      async headers() {
        return [
          // if the header `x-add-header` is present,
          // the `x-another-header` header will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'header',
                key: 'x-add-header',
              },
            ],
            headers: [
              {
                key: 'x-another-header',
                value: 'hello',
              },
            ],
          },
          // if the header `x-no-header` is not present,
          // the `x-another-header` header will be applied
          {
            source: '/:path*',
            missing: [
              {
                type: 'header',
                key: 'x-no-header',
              },
            ],
            headers: [
              {
                key: 'x-another-header',
                value: 'hello',
              },
            ],
          },
          // if the source, query, and cookie are matched,
          // the `x-authorized` header will be applied
          {
            source: '/specific/:path*',
            has: [
              {
                type: 'query',
                key: 'page',
                // the page value will not be available in the
                // header key/values since value is provided and
                // doesn't use a named capture group e.g. (?<page>home)
                value: 'home',
              },
              {
                type: 'cookie',
                key: 'authorized',
                value: 'true',
              },
            ],
            headers: [
              {
                key: 'x-authorized',
                value: ':authorized',
              },
            ],
          },
          // if the header `x-authorized` is present and
          // contains a matching value, the `x-another-header` will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'header',
                key: 'x-authorized',
                value: '(?<authorized>yes|true)',
              },
            ],
            headers: [
              {
                key: 'x-another-header',
                value: ':authorized',
              },
            ],
          },
          // if the host is `example.com`,
          // this header will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'host',
                value: 'example.com',
              },
            ],
            headers: [
              {
                key: 'x-another-header',
                value: ':authorized',
              },
            ],
          },
        ]
      },
    }
```

## basePath 지원을 사용하는 헤더[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#headers-with-basepath-support)

헤더에서 [`basePath` 지원](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)을 사용할 때 `basePath: false`를 헤더에 추가하지 않는 이상 각 `source`는 자동으로 `basePath`가 접두사로 붙습니다:

next.config.js
```
    module.exports = {
      basePath: '/docs',

      async headers() {
        return [
          {
            source: '/with-basePath', // becomes /docs/with-basePath
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
          {
            source: '/without-basePath', // is not modified since basePath: false is set
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
            basePath: false,
          },
        ]
      },
    }
```

## i18n 지원을 사용하는 헤더[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#headers-with-i18n-support)

헤더에서 [`i18n` 지원](https://nextjs.org/docs/pages/guides/internationalization)을 사용할 때는 `locale: false`를 헤더에 추가하지 않는 이상 각 `source`가 구성된 `locales`를 처리하도록 자동으로 접두사가 붙습니다. `locale: false`를 사용하면 올바르게 매칭되도록 `source`를 locale로 직접 접두사 처리해야 합니다.

next.config.js
```
    module.exports = {
      i18n: {
        locales: ['en', 'fr', 'de'],
        defaultLocale: 'en',
      },

      async headers() {
        return [
          {
            source: '/with-locale', // automatically handles all locales
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
          {
            // does not handle locales automatically since locale: false is set
            source: '/nl/with-locale-manual',
            locale: false,
            headers: [
              {
                key: 'x-hello',
                value: 'world',

},
            ],
          },
          {
            // this matches '/' since `en` is the defaultLocale
            source: '/en',
            locale: false,
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
          {
            // this gets converted to /(en|fr|de)/(.*) so will not match the top-level
            // `/` or `/fr` routes like /:path* would
            source: '/(.*)',
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
        ]
      },
    }
```

## Cache-Control[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#cache-control)

Next.js는 진정으로 변하지 않는 자산에 대해 `public, max-age=31536000, immutable` 값을 가진 `Cache-Control` 헤더를 설정하며, 이는 재정의할 수 없습니다. 이러한 불변 파일은 파일 이름에 SHA 해시가 포함되어 있어 무기한 안전하게 캐시할 수 있습니다. 예: [Static Image Imports](https://nextjs.org/docs/app/getting-started/images#local-images). 이러한 자산에 대해서는 `next.config.js`에서 `Cache-Control` 헤더를 설정할 수 없습니다.

하지만 다른 응답이나 데이터에 대해서는 `Cache-Control` 헤더를 설정할 수 있습니다.

[정적 생성](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)된 페이지의 캐시를 재검증해야 한다면, 해당 페이지의 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) 함수에서 `revalidate` prop을 설정하면 됩니다.

[API Route](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)의 응답을 캐시하려면 `res.setHeader`를 사용할 수 있습니다.

pages/api/hello.ts

JavaScriptTypeScript
```
    import type { NextApiRequest, NextApiResponse } from 'next'

    type ResponseData = {
      message: string
    }

    export default function handler(
      req: NextApiRequest,
      res: NextApiResponse<ResponseData>
    ) {
      res.setHeader('Cache-Control', 's-maxage=86400')
      res.status(200).json({ message: 'Hello from Next.js!' })
    }
```

동적 응답을 캐시하려면 `getServerSideProps` 내부에서 `Cache-Control` 헤더를 사용할 수도 있습니다. 예를 들어 [`stale-while-revalidate`](https://web.dev/stale-while-revalidate/)을 사용할 수 있습니다.

pages/index.tsx

JavaScriptTypeScript
```
    import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'

    // This value is considered fresh for ten seconds (s-maxage=10).
    // If a request is repeated within the next 10 seconds, the previously
    // cached value will still be fresh. If the request is repeated before 59 seconds,
    // the cached value will be stale but still render (stale-while-revalidate=59).
    //
    // In the background, a revalidation request will be made to populate the cache
    // with a fresh value. If you refresh the page, you will see the new value.
    export const getServerSideProps = (async (context) => {
      context.res.setHeader(
        'Cache-Control',
        'public, s-maxage=10, stale-while-revalidate=59'
      )

      return {
        props: {},
      }
    }) satisfies GetServerSideProps
```

## Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#options)

### CORS[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#cors)

[교차 출처 리소스 공유(CORS)](https://developer.mozilla.org/docs/Web/HTTP/CORS)는 어떤 사이트가 리소스에 접근할 수 있는지를 제어할 수 있게 해주는 보안 기능입니다. 특정 출처가 API Endpoints에 접근하도록 허용하려면 `Access-Control-Allow-Origin` 헤더를 설정할 수 있습니다.
```
    async headers() {
        return [
          {
            source: "/api/:path*",
            headers: [
              {
                key: "Access-Control-Allow-Origin",
                value: "*", // Set your origin
              },
              {
                key: "Access-Control-Allow-Methods",
                value: "GET, POST, PUT, DELETE, OPTIONS",
              },
              {
                key: "Access-Control-Allow-Headers",
                value: "Content-Type, Authorization",
              },
            ],
          },
        ];
      },
```

### X-DNS-Prefetch-Control[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#x-dns-prefetch-control)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-DNS-Prefetch-Control)는 DNS 프리패칭을 제어하여 브라우저가 외부 링크, 이미지, CSS, JavaScript 등을 미리 도메인 이름 해석하도록 허용합니다. 프리패칭은 백그라운드에서 수행되므로 참조된 항목이 필요해질 시점에는 [DNS](https://developer.mozilla.org/docs/Glossary/DNS)가 이미 해석되어 있을 가능성이 높습니다. 이를 통해 사용자가 링크를 클릭할 때 지연 시간이 줄어듭니다.
```
    {
      key: 'X-DNS-Prefetch-Control',
      value: 'on'
    }
```

### Strict-Transport-Security[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#strict-transport-security)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security)는 브라우저에 HTTP 대신 HTTPS로만 접근해야 한다고 알립니다. 아래 구성에서는 현재와 미래의 모든 하위 도메인이 2년(`max-age=63072000`) 동안 HTTPS를 사용하도록 강제합니다. 이는 HTTP로만 제공되는 페이지나 하위 도메인에 대한 접근을 차단합니다.
```
    {
      key: 'Strict-Transport-Security',
      value: 'max-age=63072000; includeSubDomains; preload'
    }
```

### X-Frame-Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#x-frame-options)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Frame-Options)는 사이트가 `iframe` 안에 표시될 수 있는지를 나타내며, 클릭재킹 공격을 방지할 수 있습니다.

**이 헤더는 CSP의 `frame-ancestors` 옵션으로 대체되었으며**, 최신 브라우저에서 더 나은 지원을 제공합니다(구성 방법은 [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy)를 참조하세요).
```
    {
      key: 'X-Frame-Options',
      value: 'SAMEORIGIN'
    }
```

### Permissions-Policy[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#permissions-policy)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/Permissions-Policy)를 사용하면 브라우저에서 어떤 기능과 API를 사용할 수 있는지 제어할 수 있습니다. 이전에는 `Feature-Policy`라는 이름이었습니다.
```
    {
      key: 'Permissions-Policy',
      value: 'camera=(), microphone=(), geolocation=(), browsing-topics=()'
    }
```

### X-Content-Type-Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#x-content-type-options)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Content-Type-Options)는 `Content-Type` 헤더가 명시적으로 설정되지 않은 경우 브라우저가 콘텐츠 유형을 추측하려는 시도를 막습니다. 이는 사용자가 파일 업로드와 공유를 할 수 있는 웹사이트에서 XSS 공격을 예방할 수 있습니다.

예를 들어 사용자가 이미지를 다운로드하려고 했지만 실행 파일과 같은 다른 `Content-Type`으로 처리되는 경우, 악성일 수 있습니다. 이 헤더는 브라우저 확장 프로그램을 다운로드할 때도 적용됩니다. 이 헤더에 사용할 수 있는 유일한 값은 `nosniff`입니다.
```
    {
      key: 'X-Content-Type-Options',
      value: 'nosniff'
    }
```

### Referrer-Policy[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#referrer-policy)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/Referrer-Policy)는 현재 웹사이트(오리진)에서 다른 곳으로 이동할 때 브라우저가 얼마나 많은 정보를 포함할지를 제어합니다.
```
    {
      key: 'Referrer-Policy',
      value: 'origin-when-cross-origin'
    }
```

### Content-Security-Policy[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#content-security-policy)

애플리케이션에 [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy)를 추가하는 방법을 더 알아보세요.

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#version-history)

Version| Changes
---|---
`v13.3.0`| `missing` 추가.
`v10.2.0`| `has` 추가.
`v9.5.0`| Headers 추가.

보내기