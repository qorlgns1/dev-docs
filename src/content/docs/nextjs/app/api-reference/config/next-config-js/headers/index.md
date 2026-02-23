---
title: 'next.config.js: 헤더'
description: '헤더를 사용하면 특정 경로로 들어오는 요청에 대한 응답에 커스텀 HTTP 헤더를 설정할 수 있습니다.'
---

# next.config.js: 헤더 | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/headers

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)헤더

페이지 복사

# 헤더

최종 업데이트 2026년 2월 20일

헤더를 사용하면 특정 경로로 들어오는 요청에 대한 응답에 커스텀 HTTP 헤더를 설정할 수 있습니다.

커스텀 HTTP 헤더를 설정하려면 `next.config.js`의 `headers` 키를 사용할 수 있습니다:

next.config.js
[code]
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
[/code]

`headers` 는 `source` 및 `headers` 속성을 가진 객체들을 담은 배열을 반환하는 async 함수입니다:

  * `source` 는 들어오는 요청 경로 패턴입니다.
  * `headers` 는 `key` 와 `value` 속성을 가진 응답 헤더 객체의 배열입니다.
  * `basePath`: `false` 또는 `undefined` \- `false` 이면 매칭 시 basePath가 포함되지 않으며, 외부 rewrite에만 사용할 수 있습니다.
  * `locale`: `false` 또는 `undefined` \- 매칭 시 locale을 포함하지 않을지 여부입니다.
  * `has` 는 `type`, `key`, `value` 속성을 가진 [has 객체](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#header-cookie-and-query-matching)의 배열입니다.
  * `missing` 은 `type`, `key`, `value` 속성을 가진 [missing 객체](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#header-cookie-and-query-matching)의 배열입니다.

헤더는 페이지와 `/public` 파일을 포함한 파일 시스템보다 먼저 확인됩니다.

## 헤더 재정의 동작[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#header-overriding-behavior)

두 헤더가 동일한 경로와 동일한 헤더 키를 설정하면 마지막 헤더 키가 첫 번째 것을 재정의합니다. 아래 헤더를 사용하면 경로 `/hello` 에서 최종적으로 설정된 값이 `world` 이므로 `x-hello` 헤더가 `world` 가 됩니다.

next.config.js
[code]
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
[/code]

## 경로 매칭[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#path-matching)

경로 매칭을 사용할 수 있으며, 예를 들어 `/blog/:slug` 는 `/blog/first-post` 와 매칭됩니다(중첩 경로 없음):

next.config.js
[code]
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
[/code]

패턴 `/blog/:slug` 는 `/blog/first-post` 와 `/blog/post-1` 에 매칭되지만 `/blog/a/b` 같은 중첩 경로에는 매칭되지 않습니다. 패턴은 시작 지점에 고정되므로 `/blog/:slug` 는 `/archive/blog/first-post` 에 매칭되지 않습니다.

매개변수에는 `*`(0개 이상), `+`(1개 이상), `?`(0개 또는 1개) 수정자를 사용할 수 있습니다. 예를 들어 `/blog/:slug*` 는 `/blog`, `/blog/a`, `/blog/a/b/c` 에 매칭됩니다.

자세한 내용은 [path-to-regexp](https://github.com/pillarjs/path-to-regexp) 문서를 참조하세요.

### 와일드카드 경로 매칭[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#wildcard-path-matching)

와일드카드 경로를 매칭하려면 매개변수 뒤에 `*` 를 사용할 수 있습니다. 예를 들어 `/blog/:slug*` 는 `/blog/a/b/c/d/hello-world` 와 매칭됩니다:

next.config.js
[code]
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
[/code]

### 정규식 경로 매칭[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#regex-path-matching)

정규식 경로를 매칭하려면 매개변수 뒤에 괄호로 정규식을 감싸면 됩니다. 예를 들어 `/blog/:slug(\\d{1,})` 는 `/blog/123` 와 매칭되지만 `/blog/abc` 와는 매칭되지 않습니다:

next.config.js
[code]
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
[/code]

`(`, `)`, `{`, `}`, `:`, `*`, `+`, `?` 문자는 정규식 경로 매칭에 사용되므로 `source` 에서 특수 문자가 아닌 값으로 사용하려면 앞에 `\\` 를 붙여 이스케이프해야 합니다:

next.config.js
[code]
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
[/code]

## 헤더, 쿠키, 그리고 쿼리 매칭[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#header-cookie-and-query-matching)

헤더, 쿠키, 혹은 쿼리 값이 `has` 필드와 일치하거나 `missing` 필드와 일치하지 않을 때만 헤더를 적용하려면 해당 필드를 사용할 수 있습니다. 헤더가 적용되려면 `source` 와 모든 `has` 항목이 일치해야 하고, 모든 `missing` 항목은 일치하면 안 됩니다.

`has` 와 `missing` 항목은 다음 필드를 가질 수 있습니다:

  * `type`: `String` \- `header`, `cookie`, `host`, `query` 중 하나여야 합니다.
  * `key`: `String` \- 선택한 타입에서 매칭할 키입니다.
  * `value`: `String` 또는 `undefined` \- 확인할 값이며, `undefined` 인 경우 아무 값이나 매칭됩니다. `first-(?<paramName>.*)` 처럼 특정 부분을 캡처하는 정규식 형태의 문자열을 사용할 수 있으며, `first-second` 값에 이를 적용하면 `second` 를 `:paramName` 으로 목적지에서 사용할 수 있습니다.

next.config.js
[code]
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
[/code]

## basePath 지원이 있는 헤더[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#headers-with-basepath-support)

헤더에서 [`basePath` 지원](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)을 활용하면 각 `source` 가 자동으로 `basePath` 로 접두사 처리됩니다. 헤더에 `basePath: false` 를 추가하면 해당 접두사가 적용되지 않습니다:

next.config.js
[code]
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
[/code]

## i18n 지원이 있는 헤더[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#headers-with-i18n-support)

헤더에서 [`i18n` 지원](https://nextjs.org/docs/app/guides/internationalization)을 활용하면 `locale: false` 를 추가하지 않는 한 각 `source` 가 구성된 `locales` 를 다룰 수 있도록 자동으로 접두사 처리됩니다. `locale: false` 를 사용하면 올바르게 매칭되도록 `source` 에 locale을 직접 접두사로 붙여야 합니다.

next.config.js
[code]
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
[/code]

## Cache-Control[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#cache-control)

Next.js는 완전히 변경되지 않는 자산에 대해 `public, max-age=31536000, immutable` 값을 가진 `Cache-Control` 헤더를 설정합니다. 이 설정은 재정의할 수 없습니다. 이러한 변경 불가능한 파일은 파일 이름에 SHA 해시가 포함되어 있어 영구적으로 캐시해도 안전합니다. 예: [Static Image Imports](https://nextjs.org/docs/app/getting-started/images#local-images). 이러한 자산에 대해서는 `next.config.js`에서 `Cache-Control` 헤더를 설정할 수 없습니다.

하지만 다른 응답이나 데이터에 대해서는 `Cache-Control` 헤더를 설정할 수 있습니다.

App Router와 함께하는 [캐싱](https://nextjs.org/docs/app/guides/caching)에 대해 더 알아보세요.

## Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#options)

### CORS[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#cors)

[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/docs/Web/HTTP/CORS)는 어떤 사이트가 리소스에 접근할 수 있는지 제어할 수 있게 해 주는 보안 기능입니다. 특정 오리진이 Route Handler에 접근하도록 허용하려면 `Access-Control-Allow-Origin` 헤더를 설정할 수 있습니다.
[code] 
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
[/code]

### X-DNS-Prefetch-Control[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#x-dns-prefetch-control)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-DNS-Prefetch-Control)는 브라우저가 외부 링크, 이미지, CSS, JavaScript 등에 대해 도메인 이름 해석을 선행하도록 제어합니다. 이 프리페치는 백그라운드에서 수행되므로 참조된 항목이 필요해질 때까지 [DNS](https://developer.mozilla.org/docs/Glossary/DNS)가 미리 해결될 가능성이 높아집니다. 그 결과 사용자가 링크를 클릭할 때 지연 시간이 줄어듭니다.
[code] 
    {
      key: 'X-DNS-Prefetch-Control',
      value: 'on'
    }
[/code]

### Strict-Transport-Security[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#strict-transport-security)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security)는 브라우저에 HTTP 대신 HTTPS로만 접근해야 한다고 알립니다. 아래 구성은 현재와 미래의 모든 서브도메인에 대해 2년(`max-age` 2년) 동안 HTTPS를 사용하도록 강제합니다. 이는 HTTP로만 제공 가능한 페이지나 서브도메인 접근을 차단합니다.
[code] 
    {
      key: 'Strict-Transport-Security',
      value: 'max-age=63072000; includeSubDomains; preload'
    }
[/code]

### X-Frame-Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#x-frame-options)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Frame-Options)는 사이트를 `iframe` 내부에 표시할 수 있는지 여부를 나타냅니다. 이는 클릭재킹 공격을 방지할 수 있습니다.

**이 헤더는 현대 브라우저 지원이 더 나은 CSP의 `frame-ancestors` 옵션으로 대체되었습니다.** 구성 방법은 [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy)를 참고하세요.
[code] 
    {
      key: 'X-Frame-Options',
      value: 'SAMEORIGIN'
    }
[/code]

### Permissions-Policy[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#permissions-policy)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/Permissions-Policy)는 브라우저에서 어떤 기능과 API를 사용할 수 있는지 제어합니다. 이전 명칭은 `Feature-Policy`였습니다.
[code] 
    {
      key: 'Permissions-Policy',
      value: 'camera=(), microphone=(), geolocation=(), browsing-topics=()'
    }
[/code]

### X-Content-Type-Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#x-content-type-options)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Content-Type-Options)는 `Content-Type` 헤더가 명시적으로 설정되지 않은 경우 브라우저가 콘텐츠 유형을 추측하려는 시도를 막습니다. 이는 사용자가 파일을 업로드하고 공유할 수 있는 웹사이트에서 XSS 공격을 예방할 수 있습니다.

예를 들어 사용자가 이미지를 다운로드하려고 했는데 실행 파일과 같은 다른 `Content-Type`으로 처리되어 악성일 수 있는 상황을 막습니다. 이 헤더는 브라우저 확장 프로그램을 다운로드할 때에도 적용됩니다. 사용할 수 있는 유일한 값은 `nosniff`입니다.
[code] 
    {
      key: 'X-Content-Type-Options',
      value: 'nosniff'
    }
[/code]

### Referrer-Policy[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#referrer-policy)

[이 헤더](https://developer.mozilla.org/docs/Web/HTTP/Headers/Referrer-Policy)는 현재 웹사이트(오리진)에서 다른 곳으로 이동할 때 브라우저가 얼마나 많은 정보를 포함할지 제어합니다.
[code] 
    {
      key: 'Referrer-Policy',
      value: 'origin-when-cross-origin'
    }
[/code]

### Content-Security-Policy[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#content-security-policy)

애플리케이션에 [콘텐츠 보안 정책](https://nextjs.org/docs/app/guides/content-security-policy)을 추가하는 방법을 더 알아보세요.

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#version-history)

Version| Changes  
---|---  
`v13.3.0`| `missing`가 추가되었습니다.  
`v10.2.0`| `has`가 추가되었습니다.  
`v9.5.0`| 헤더가 추가되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
