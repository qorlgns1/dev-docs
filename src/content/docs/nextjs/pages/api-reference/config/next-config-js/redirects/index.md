---
title: 'next.config.js 옵션: redirects'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js 옵션: redirects | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects

[구성](https://nextjs.org/docs/pages/api-reference/config)[next.config.js 옵션](https://nextjs.org/docs/pages/api-reference/config/next-config-js)redirects

페이지 복사

# 리디렉션

마지막 업데이트 2026년 2월 20일

리디렉션을 사용하면 들어오는 요청 경로를 다른 목적지 경로로 전달할 수 있습니다.

리디렉션을 설정하려면 `next.config.js`에서 `redirects` 키를 사용하세요:

next.config.js
[code]
    module.exports = {
      async redirects() {
        return [
          {
            source: '/about',
            destination: '/',
            permanent: true,
          },
        ]
      },
    }
[/code]

`redirects`는 `source`, `destination`, `permanent` 속성을 가진 객체 배열을 반환해야 하는 async 함수입니다.

  * `source`는 들어오는 요청 경로 패턴입니다.
  * `destination`은 라우팅하려는 경로입니다.
  * `permanent` `true` 또는 `false` \- `true`이면 클라이언트/검색 엔진에게 리디렉션을 영구적으로 캐시하도록 지시하는 308 상태 코드를, `false`이면 일시적이고 캐시되지 않는 307 상태 코드를 사용합니다.



> **Next.js가 307과 308을 사용하는 이유는 무엇인가요?** 전통적으로 일시적 리디렉션에는 302, 영구 리디렉션에는 301을 사용했지만 많은 브라우저가 원래 메서드와 무관하게 리디렉션 요청 메서드를 `GET`으로 변경했습니다. 예를 들어 브라우저가 `POST /v1/users` 요청을 보냈고 상태 코드 `302`와 위치 `/v2/users`를 받았다면, 이어지는 요청이 예상한 `POST /v2/users` 대신 `GET /v2/users`가 될 수 있습니다. Next.js는 요청 메서드를 명시적으로 유지하기 위해 307 일시적 리디렉션과 308 영구 리디렉션 상태 코드를 사용합니다.

  * `basePath`: `false` 또는 `undefined` \- `false`이면 매칭 시 `basePath`를 포함하지 않으며, 외부 리디렉션에만 사용할 수 있습니다.
  * `locale`: `false` 또는 `undefined` \- 매칭 시 로케일을 포함하지 않을지 여부입니다.
  * `has`는 `type`, `key`, `value` 속성을 가진 [has 객체](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching)의 배열입니다.
  * `missing`은 `type`, `key`, `value` 속성을 가진 [missing 객체](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching)의 배열입니다.



리디렉션은 페이지와 `/public` 파일을 포함한 파일 시스템보다 먼저 확인됩니다.

Pages Router를 사용할 때는 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)가 존재하여 경로와 일치하지 않는 한 클라이언트 측 라우팅(`Link`, `router.push`)에는 리디렉션이 적용되지 않습니다.

리디렉션이 적용되면 요청에 제공된 쿼리 값은 리디렉션 목적지로 그대로 전달됩니다. 예를 들어 다음 리디렉션 구성을 보세요:
[code] 
    {
      source: '/old-blog/:path*',
      destination: '/blog/:path*',
      permanent: false
    }
[/code]

> **알아두면 좋아요** : `source`와 `destination` 경로의 경로 매개변수에서 콜론 `:` 앞에 슬래시 `/`를 반드시 포함하세요. 그렇지 않으면 경로가 리터럴 문자열로 처리되어 무한 리디렉션이 발생할 수 있습니다.

`/old-blog/post-1?hello=world`를 요청하면 클라이언트는 `/blog/post-1?hello=world`로 리디렉션됩니다.

## 경로 매칭[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#path-matching)

경로 매칭이 허용되며, 예를 들어 `/old-blog/:slug`는 `/old-blog/first-post`와 일치합니다(중첩 경로 없음).

next.config.js
[code]
    module.exports = {
      async redirects() {
        return [
          {
            source: '/old-blog/:slug',
            destination: '/news/:slug', // Matched parameters can be used in the destination
            permanent: true,
          },
        ]
      },
    }
[/code]

`/old-blog/:slug` 패턴은 `/old-blog/first-post`와 `/old-blog/post-1`에는 매칭되지만 `/old-blog/a/b`에는 매칭되지 않습니다(중첩 경로 없음). 패턴은 시작 위치에 고정되므로 `/old-blog/:slug`는 `/archive/old-blog/first-post`와 일치하지 않습니다.

매개변수에 수식어를 사용할 수 있습니다: `*`(0개 이상), `+`(1개 이상), `?`(0개 또는 1개). 예를 들어 `/blog/:slug*`는 `/blog`, `/blog/a`, `/blog/a/b/c`와 일치합니다.

자세한 내용은 [path-to-regexp](https://github.com/pillarjs/path-to-regexp) 문서를 참고하세요.

### 와일드카드 경로 매칭[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#wildcard-path-matching)

와일드카드 경로를 매칭하려면 매개변수 뒤에 `*`를 사용할 수 있습니다. 예를 들어 `/blog/:slug*`는 `/blog/a/b/c/d/hello-world`와 일치합니다.

next.config.js
[code]
    module.exports = {
      async redirects() {
        return [
          {
            source: '/blog/:slug*',
            destination: '/news/:slug*', // Matched parameters can be used in the destination
            permanent: true,
          },
        ]
      },
    }
[/code]

### 정규식 경로 매칭[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#regex-path-matching)

정규식 경로를 매칭하려면 매개변수 뒤를 괄호로 감싼 정규식으로 정의할 수 있습니다. 예를 들어 `/post/:slug(\\d{1,})`는 `/post/123`과는 매칭되지만 `/post/abc`와는 매칭되지 않습니다.

next.config.js
[code]
    module.exports = {
      async redirects() {
        return [
          {
            source: '/post/:slug(\\d{1,})',
            destination: '/news/:slug', // Matched parameters can be used in the destination
            permanent: false,
          },
        ]
      },
    }
[/code]

`(`, `)`, `{`, `}`, `:`, `*`, `+`, `?` 문자는 정규식 경로 매칭에 사용되므로 `source`에서 특수 문자가 아닌 값으로 사용하려면 앞에 `\\`를 붙여 이스케이프해야 합니다.

next.config.js
[code]
    module.exports = {
      async redirects() {
        return [
          {
            // this will match `/english(default)/something` being requested
            source: '/english\\(default\\)/:slug',
            destination: '/en-us/:slug',
            permanent: false,
          },
        ]
      },
    }
[/code]

## 헤더, 쿠키, 쿼리 매칭[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching)

헤더, 쿠키 또는 쿼리 값이 `has` 필드와 일치하거나 `missing` 필드와 일치하지 않을 때만 리디렉션을 적용하려면 해당 필드를 사용할 수 있습니다. 리디렉션이 적용되려면 `source`와 모든 `has` 항목이 일치하고 모든 `missing` 항목이 일치하지 않아야 합니다.

`has`와 `missing` 항목에는 다음 필드를 사용할 수 있습니다.

  * `type`: `String` \- `header`, `cookie`, `host`, `query` 중 하나여야 합니다.
  * `key`: `String` \- 선택한 타입에서 매칭할 키입니다.
  * `value`: `String` 또는 `undefined` \- 확인할 값이며, undefined이면 모든 값과 일치합니다. `first-(?<paramName>.*)`처럼 특정 부분을 캡처하는 정규식 형태의 문자열을 사용할 수 있으며, `first-second` 값에 사용하면 `second`를 `:paramName`으로 목적지에서 참조할 수 있습니다.



next.config.js
[code]
    module.exports = {
      async redirects() {
        return [
          // if the header `x-redirect-me` is present,
          // this redirect will be applied
          {
            source: '/:path((?!another-page$).*)',
            has: [
              {
                type: 'header',
                key: 'x-redirect-me',
              },
            ],
            permanent: false,
            destination: '/another-page',
          },
          // if the header `x-do-not-redirect` is present,
          // this redirect will NOT be applied
          {
            source: '/:path((?!another-page$).*)',
            missing: [
              {
                type: 'header',
                key: 'x-do-not-redirect',
              },
            ],
            permanent: false,
            destination: '/another-page',
          },
          // if the source, query, and cookie are matched,
          // this redirect will be applied
          {
            source: '/specific/:path*',
            has: [
              {
                type: 'query',
                key: 'page',
                // the page value will not be available in the
                // destination since value is provided and doesn't
                // use a named capture group e.g. (?<page>home)
                value: 'home',
              },
              {
                type: 'cookie',
                key: 'authorized',
                value: 'true',
              },
            ],
            permanent: false,
            destination: '/another/:path*',
          },
          // if the header `x-authorized` is present and
          // contains a matching value, this redirect will be applied
          {
            source: '/',
            has: [
              {
                type: 'header',
                key: 'x-authorized',
                value: '(?<authorized>yes|true)',
              },
            ],
            permanent: false,
            destination: '/home?authorized=:authorized',
          },
          // if the host is `example.com`,
          // this redirect will be applied
          {
            source: '/:path((?!another-page$).*)',
            has: [
              {
                type: 'host',
                value: 'example.com',
              },
            ],
            permanent: false,
            destination: '/another-page',
          },
        ]
      },
    }
[/code]

### basePath 지원과 함께 사용하는 리디렉션[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#redirects-with-basepath-support)

리디렉션에서 [`basePath` 지원](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)을 사용하는 경우 `basePath: false`를 추가하지 않는 한 각 `source`와 `destination`에 `basePath`가 자동으로 접두사로 붙습니다.

next.config.js
[code]
    module.exports = {
      basePath: '/docs',
     
      async redirects() {
        return [
          {
            source: '/with-basePath', // automatically becomes /docs/with-basePath
            destination: '/another', // automatically becomes /docs/another
            permanent: false,
          },
          {
            // does not add /docs since basePath: false is set
            source: '/without-basePath',
            destination: 'https://example.com',
            basePath: false,
            permanent: false,
          },
        ]
      },
    }
[/code]

### i18n 지원과 함께 사용하는 리디렉션[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#redirects-with-i18n-support)

리디렉션에서 [`i18n` 지원](https://nextjs.org/docs/pages/guides/internationalization)을 사용하는 경우 `locale: false`를 추가하지 않는 한 각 `source`와 `destination`은 구성된 `locales`를 처리하도록 자동으로 접두사가 붙습니다. `locale: false`를 사용하면 올바르게 매칭되도록 `source`와 `destination` 앞에 로케일을 명시해야 합니다.

next.config.js
[code]
    module.exports = {
      i18n: {
        locales: ['en', 'fr', 'de'],
        defaultLocale: 'en',
      },
     
      async redirects() {
        return [
          {
            source: '/with-locale', // automatically handles all locales
            destination: '/another', // automatically passes the locale on
            permanent: false,
          },
          {
            // does not handle locales automatically since locale: false is set
            source: '/nl/with-locale-manual',
            destination: '/nl/another',
            locale: false,
            permanent: false,
          },
          {
            // this matches '/' since `en` is the defaultLocale
            source: '/en',
            destination: '/en/another',
            locale: false,
            permanent: false,
          },
          // it's possible to match all locales even when locale: false is set
          {

```
source: '/:locale/page',
            destination: '/en/newpage',
            permanent: false,
            locale: false,
          },
          {
            // this gets converted to /(en|fr|de)/(.*) so will not match the top-level
            // `/` or `/fr` routes like /:path* would
            source: '/(.*)',
            destination: '/another',
            permanent: false,
          },
        ]
      },
    }
[/code]
```

드물게는 이전 HTTP 클라이언트가 올바르게 리디렉션되도록 맞춤 상태 코드를 지정해야 할 수 있습니다. 이런 경우 `permanent` 속성 대신 `statusCode` 속성을 사용할 수 있지만 두 가지를 동시에 사용할 수는 없습니다. IE11 호환성을 보장하기 위해 308 상태 코드에는 자동으로 `Refresh` 헤더가 추가됩니다.

## 기타 리디렉트[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#other-redirects)
- [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) 및 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) 내부에서는 들어오는 요청을 기준으로 리디렉션할 수 있습니다.
- [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)와 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) 내부에서는 요청 시점에 특정 페이지를 리디렉션할 수 있습니다.

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects#version-history)
버전|변경 사항  
---|---  
`v13.3.0`| `missing` 추가.  
`v10.2.0`| `has` 추가.  
`v9.5.0`| `redirects` 추가.  

도움이 되었나요?

지원됨.

보내기
