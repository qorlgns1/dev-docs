---
title: 'next.config.js: 리다이렉트'
description: '리다이렉트는 들어오는 요청 경로를 다른 대상 경로로 전환할 수 있게 해 줍니다.'
---

# next.config.js: 리다이렉트 | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects

# 리다이렉트

마지막 업데이트: 2026년 2월 20일

리다이렉트는 들어오는 요청 경로를 다른 대상 경로로 전환할 수 있게 해 줍니다.

리다이렉트를 사용하려면 `next.config.js`에서 `redirects` 키를 사용하면 됩니다:

next.config.js
```
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
```

`redirects`는 `source`, `destination`, `permanent` 속성을 가진 객체를 담은 배열을 반환해야 하는 비동기 함수입니다.

  * `source`는 들어오는 요청 경로 패턴입니다.
  * `destination`은 라우팅하려는 경로입니다.
  * `permanent`는 `true` 또는 `false`입니다. `true`이면 308 상태 코드를 사용하여 클라이언트/검색 엔진이 리다이렉트를 영구적으로 캐시하도록 지시하고, `false`이면 307 상태 코드를 사용하여 일시적이며 캐시되지 않습니다.

> **Next.js가 307과 308을 사용하는 이유는 무엇인가요?** 전통적으로 302는 임시 리다이렉트, 301은 영구 리다이렉트였지만 많은 브라우저가 원래 메서드와 상관없이 리다이렉트 요청 메서드를 `GET`으로 변경했습니다. 예를 들어 브라우저가 `POST /v1/users` 요청을 보냈고 응답이 상태 코드 `302`와 위치 `/v2/users`를 반환하면, 이후 요청이 예상한 `POST /v2/users`가 아니라 `GET /v2/users`가 될 수 있습니다. Next.js는 사용된 요청 메서드를 명시적으로 보존하기 위해 307 임시 리다이렉트와 308 영구 리다이렉트 상태 코드를 사용합니다.

  * `basePath`: `false` 또는 `undefined`. `false`이면 매칭 시 `basePath`가 포함되지 않으며, 외부 리다이렉트에만 사용할 수 있습니다.
  * `locale`: `false` 또는 `undefined`. 매칭 시 locale을 포함하지 않을지 여부입니다.
  * `has`는 `type`, `key`, `value` 속성을 가진 [has 객체](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching)의 배열입니다.
  * `missing`은 `type`, `key`, `value` 속성을 가진 [missing 객체](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching)의 배열입니다.

리다이렉트는 페이지와 `/public` 파일을 포함하는 파일 시스템보다 먼저 확인됩니다.

Pages Router를 사용할 때는 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)가 존재하고 경로를 매칭하지 않는 한 클라이언트 사이드 라우팅(`Link`, `router.push`)에 리다이렉트가 적용되지 않습니다.

리다이렉트가 적용되면 요청에 제공된 모든 쿼리 값이 리다이렉트 대상에 그대로 전달됩니다. 예를 들어 다음 리다이렉트 구성을 살펴보세요:
```
    {
      source: '/old-blog/:path*',
      destination: '/blog/:path*',
      permanent: false
    }
```

> **알아두면 좋은 점**: `source`와 `destination` 경로의 경로 매개변수에서 콜론 `:` 앞에 슬래시 `/`를 포함해야 합니다. 그렇지 않으면 경로가 리터럴 문자열로 처리되어 무한 리다이렉트를 유발할 위험이 있습니다.

`/old-blog/post-1?hello=world`가 요청되면 클라이언트는 `/blog/post-1?hello=world`로 리다이렉트됩니다.

## Path Matching[](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#path-matching)

경로 매칭이 허용되며, 예를 들어 `/old-blog/:slug`는 `/old-blog/first-post`를 매칭합니다(중첩 경로 없음).

next.config.js
```
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
```

패턴 `/old-blog/:slug`는 `/old-blog/first-post`, `/old-blog/post-1`을 매칭하지만 `/old-blog/a/b`는 매칭하지 않습니다(중첩 경로 없음). 패턴은 시작 지점에 고정되어 있으므로 `/old-blog/:slug`는 `/archive/old-blog/first-post`를 매칭하지 않습니다.

매개변수에 `*`(0개 이상), `+`(1개 이상), `?`(0개 또는 1개) 같은 수식자를 사용할 수 있습니다. 예를 들어 `/blog/:slug*`는 `/blog`, `/blog/a`, `/blog/a/b/c`를 매칭합니다.

자세한 내용은 [path-to-regexp](https://github.com/pillarjs/path-to-regexp) 문서를 참고하세요.

### Wildcard Path Matching[](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#wildcard-path-matching)

와일드카드 경로를 매칭하려면 매개변수 뒤에 `*`를 사용할 수 있습니다. 예를 들어 `/blog/:slug*`는 `/blog/a/b/c/d/hello-world`를 매칭합니다.

next.config.js
```
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
```

### Regex Path Matching[](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#regex-path-matching)

정규식 경로를 매칭하려면 매개변수 뒤에 괄호로 정규식을 감싸면 됩니다. 예를 들어 `/post/:slug(\\d{1,})`는 `/post/123`을 매칭하지만 `/post/abc`는 매칭하지 않습니다.

next.config.js
```
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
```

정규식 경로 매칭에 사용되는 문자 `(`, `)`, `{`, `}`, `:`, `*`, `+`, `?`는 `source`에서 특수 문자가 아닌 값으로 사용될 때 앞에 `\\`를 추가하여 이스케이프해야 합니다.

next.config.js
```
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
```

## Header, Cookie, and Query Matching[](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching)

헤더, 쿠키 또는 쿼리 값이 `has` 필드와 일치하거나 `missing` 필드와 일치하지 않을 때만 리다이렉트를 적용하려면 해당 필드를 사용합니다. 리다이렉트가 적용되려면 `source`와 모든 `has` 항목이 매칭되고, 모든 `missing` 항목은 매칭되지 않아야 합니다.

`has`와 `missing` 항목에는 다음 필드를 사용할 수 있습니다.

  * `type`: `String`. `header`, `cookie`, `host`, `query` 중 하나여야 합니다.
  * `key`: `String`. 선택한 타입에서 매칭할 키입니다.
  * `value`: `String` 또는 `undefined`. 확인할 값이며, `undefined`이면 어떤 값이든 매칭됩니다. 값에 정규식과 유사한 문자열을 사용하여 특정 부분을 캡처할 수 있습니다. 예를 들어 `first-(?<paramName>.*)` 값을 `first-second`에 사용하면 `second`를 `:paramName`으로 대상에서 사용할 수 있습니다.

next.config.js
```
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
```

### basePath 지원과 함께하는 리다이렉트[](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#redirects-with-basepath-support)

리다이렉트에서 [`basePath` 지원](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)을 활용할 때 `basePath: false`를 리다이렉트에 추가하지 않는 이상 각 `source`와 `destination`은 자동으로 `basePath`가 접두사로 붙습니다.

next.config.js
```
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
```

### i18n 지원과 함께하는 리다이렉트[](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#redirects-with-i18n-support)

App Router에서 국제화를 포함한 리다이렉트를 구현할 때는 `next.config.js` 리다이렉트에 locale을 포함할 수 있지만, 하드코딩된 경로로만 가능합니다.

요청마다 동적인 locale 처리가 필요하면 [dynamic route segments and proxy](https://nextjs.org/docs/app/guides/internationalization)를 사용하여 사용자의 선호 언어에 따라 리다이렉트하세요.

next.config.js
```
    module.exports = {
      async redirects() {
        return [
          {
            // Manually handle locale prefixes for App Router
            source: '/en/old-path',
            destination: '/en/new-path',
            permanent: false,
          },
          {
            // Redirect for all locales using a parameter
            source: '/:locale/old-path',
            destination: '/:locale/new-path',
            permanent: false,
          },
          {
            // Redirect from one locale to another
            source: '/de/old-path',
            destination: '/en/new-path',
            permanent: false,
          },
          {
            // Catch-all redirect for multiple locales
            source: '/:locale(en|fr|de)/:path*',
            destination: '/:locale/new-section/:path*',
            permanent: false,
          },
        ]
      },
    }
```

드물지만 이전 HTTP 클라이언트가 올바르게 리디렉션되도록 사용자 지정 상태 코드를 할당해야 하는 경우가 있습니다. 이런 상황에서는 `permanent` 속성 대신 `statusCode` 속성을 사용할 수 있지만, 두 속성을 동시에 사용할 수는 없습니다. IE11 호환성을 보장하기 위해 308 상태 코드에는 자동으로 `Refresh` 헤더가 추가됩니다.

## Other Redirects[](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#other-redirects)

  * [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)와 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) 내부에서는 들어오는 요청을 기반으로 리디렉션할 수 있습니다.
  * [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)와 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) 내부에서는 요청 시점에 특정 페이지를 리디렉션할 수 있습니다.

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#version-history)

Version| Changes
---|---
`v13.3.0`| `missing` 추가.
`v10.2.0`| `has` 추가.
`v9.5.0`| `redirects` 추가.

보내기