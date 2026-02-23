---
title: 'next.config.js Options: rewrites'
description: 'Rewrites를 사용하면 들어오는 요청 경로를 다른 목적지 경로로 매핑할 수 있습니다.'
---

# next.config.js Options: rewrites | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)rewrites

Copy page

# rewrites

마지막 업데이트 2026년 2월 20일

Rewrites를 사용하면 들어오는 요청 경로를 다른 목적지 경로로 매핑할 수 있습니다.

Rewrites는 URL 프록시처럼 동작하여 목적지 경로를 숨기므로, 사용자는 사이트 내에서 자신의 위치가 변경되지 않은 것처럼 보입니다. 반면 [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)는 새 페이지로 이동하며 URL 변경 사항을 표시합니다.

rewrites를 사용하려면 `next.config.js`에서 `rewrites` 키를 사용할 수 있습니다:

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            source: '/about',
            destination: '/',
          },
        ]
      },
    }
[/code]

Rewrites는 클라이언트 측 라우팅에 적용됩니다. 위 예제에서 `<Link href="/about">`로 이동하면 URL을 `/about`으로 유지하면서 `/`의 콘텐츠를 제공합니다.

`rewrites`는 배열 또는 배열 객체(아래 참조)를 반환해야 하는 async 함수이며, 각 객체에는 `source`와 `destination` 속성이 포함됩니다:

  * `source`: `String` \- 들어오는 요청 경로 패턴입니다.
  * `destination`: `String` \- 라우팅하려는 경로입니다.
  * `basePath`: `false` 또는 `undefined` \- false인 경우 매칭 시 basePath가 포함되지 않으며, 외부 rewrites에만 사용할 수 있습니다.
  * `locale`: `false` 또는 `undefined` \- 매칭 시 locale을 포함하지 않을지 여부입니다.
  * `has`는 `type`, `key`, `value` 속성을 가진 [has objects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching)의 배열입니다.
  * `missing`은 `type`, `key`, `value` 속성을 가진 [missing objects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching)의 배열입니다.



`rewrites` 함수가 배열을 반환하면 rewrites는 파일 시스템(페이지 및 `/public` 파일)을 확인한 후, 동적 라우트 이전에 적용됩니다. `rewrites` 함수가 특정 형태의 배열 객체를 반환하면 이 동작을 변경하고 `v10.1`부터 더 세밀하게 제어할 수 있습니다:

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return {
          beforeFiles: [
            // These rewrites are checked after headers/redirects
            // and before all files including _next/public files which
            // allows overriding page files
            {
              source: '/some-page',
              destination: '/somewhere-else',
              has: [{ type: 'query', key: 'overrideMe' }],
            },
          ],
          afterFiles: [
            // These rewrites are checked after pages/public files
            // are checked but before dynamic routes
            {
              source: '/non-existent',
              destination: '/somewhere-else',
            },
          ],
          fallback: [
            // These rewrites are checked after both pages/public files
            // and dynamic routes are checked
            {
              source: '/:path*',
              destination: `https://my-old-site.com/:path*`,
            },
          ],
        }
      },
    }
[/code]

> **알아두면 좋아요** : `beforeFiles`의 rewrites는 source가 매칭되더라도 즉시 파일 시스템/동적 라우트를 확인하지 않고, 모든 `beforeFiles`가 확인될 때까지 계속됩니다.

Next.js 라우트가 확인되는 순서는 다음과 같습니다:

  1. [headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)가 확인/적용됩니다.
  2. [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)가 확인/적용됩니다.
  3. `beforeFiles` rewrites가 확인/적용됩니다.
  4. [public directory](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder)의 정적 파일, `_next/static` 파일, 비동적 페이지가 확인/제공됩니다.
  5. `afterFiles` rewrites가 확인/적용되며, 이 중 하나가 매칭되면 매칭마다 동적 라우트/정적 파일을 확인합니다.
  6. `fallback` rewrites가 확인/적용되며, 이는 404 페이지 렌더링 전에, 동적 라우트/모든 정적 자산을 확인한 후에 적용됩니다. `getStaticPaths`에서 [fallback: true/'blocking'](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)을 사용하면 `next.config.js`에 정의된 fallback `rewrites`는 실행되지 않습니다.



## Rewrite parameters[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#rewrite-parameters)

Rewrite에서 매개변수를 사용할 때, 해당 매개변수들이 `destination`에서 사용되지 않으면 기본적으로 쿼리에 전달됩니다.

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            source: '/old-about/:path*',
            destination: '/about', // The :path parameter isn't used here so will be automatically passed in the query
          },
        ]
      },
    }
[/code]

매개변수가 destination에서 사용되면 매개변수는 자동으로 쿼리에 전달되지 않습니다.

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            source: '/docs/:path*',
            destination: '/:path*', // The :path parameter is used here so will not be automatically passed in the query
          },
        ]
      },
    }
[/code]

destination에서 이미 사용 중인 매개변수가 있더라도 쿼리에 명시하여 수동으로 매개변수를 전달할 수 있습니다.

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            source: '/:first/:second',
            destination: '/:first?second=:second',
            // Since the :first parameter is used in the destination the :second parameter
            // will not automatically be added in the query although we can manually add it
            // as shown above
          },
        ]
      },
    }
[/code]

> **알아두면 좋아요** : [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) 또는 [prerendering](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)의 정적 페이지에서 rewrites로 전달된 params는 하이드레이션 이후 클라이언트에서 파싱되며 쿼리로 제공됩니다.

## Path Matching[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#path-matching)

경로 매칭이 허용되며, 예를 들어 `/blog/:slug`는 `/blog/first-post`(중첩 경로 없음)와 일치합니다:

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            source: '/blog/:slug',
            destination: '/news/:slug', // Matched parameters can be used in the destination
          },
        ]
      },
    }
[/code]

패턴 `/blog/:slug`는 `/blog/first-post`와 `/blog/post-1`에 매칭되지만 `/blog/a/b`에는 매칭되지 않습니다(중첩 경로 없음). 패턴은 시작 지점에 고정되므로 `/blog/:slug`는 `/archive/blog/first-post`와 매칭되지 않습니다.

매개변수에 `*`(0개 이상), `+`(1개 이상), `?`(0 또는 1개)와 같은 수정자를 사용할 수 있습니다. 예를 들어 `/blog/:slug*`는 `/blog`, `/blog/a`, `/blog/a/b/c`와 매칭됩니다.

자세한 내용은 [path-to-regexp](https://github.com/pillarjs/path-to-regexp) 문서를 확인하세요.

### Wildcard Path Matching[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#wildcard-path-matching)

와일드카드 경로를 매칭하려면 매개변수 뒤에 `*`를 사용할 수 있습니다. 예를 들어 `/blog/:slug*`는 `/blog/a/b/c/d/hello-world`와 매칭됩니다:

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            source: '/blog/:slug*',
            destination: '/news/:slug*', // Matched parameters can be used in the destination
          },
        ]
      },
    }
[/code]

### Regex Path Matching[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#regex-path-matching)

정규식 경로를 매칭하려면 매개변수 뒤에 괄호로 정규식을 감싸면 됩니다. 예를 들어 `/blog/:slug(\\d{1,})`는 `/blog/123`과 매칭되지만 `/blog/abc`와는 매칭되지 않습니다:

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            source: '/old-blog/:post(\\d{1,})',
            destination: '/blog/:post', // Matched parameters can be used in the destination
          },
        ]
      },
    }
[/code]

다음 문자는 정규식 경로 매칭에 사용되므로, `source`에서 일반 문자로 사용하려면 앞에 `\\`를 붙여 이스케이프해야 합니다: `(`, `)`, `{`, `}`, `[`, `]`, `|`, `\`, `^`, `.`, `:`, `*`, `+`, `-`, `?`, `$`

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            // this will match `/english(default)/something` being requested
            source: '/english\\(default\\)/:slug',
            destination: '/en-us/:slug',
          },
        ]
      },
    }
[/code]

## Header, Cookie, and Query Matching[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching)

헤더, 쿠키, 쿼리 값이 `has` 필드와 일치하거나 `missing` 필드와 일치하지 않을 때에만 rewrite를 매칭하려면 해당 필드를 사용할 수 있습니다. rewrite가 적용되려면 `source`와 모든 `has` 항목이 매칭되고, 모든 `missing` 항목이 매칭되지 않아야 합니다.

`has`와 `missing` 항목은 다음 필드를 가질 수 있습니다:

  * `type`: `String` \- `header`, `cookie`, `host`, `query` 중 하나여야 합니다.
  * `key`: `String` \- 선택된 타입에서 매칭할 키입니다.
  * `value`: `String` 또는 `undefined` \- 확인할 값입니다. `undefined`이면 어떤 값이든 매칭됩니다. 값에 정규식 형태의 문자열을 사용하여 특정 부분을 캡처할 수 있습니다. 예를 들어 값으로 `first-(?<paramName>.*)`를 사용하고 `first-second`가 들어오면 `second`를 `:paramName`으로 destination에서 사용할 수 있습니다.



next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          // if the header `x-rewrite-me` is present,
          // this rewrite will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'header',
                key: 'x-rewrite-me',
              },
            ],
            destination: '/another-page',
          },
          // if the header `x-rewrite-me` is not present,
          // this rewrite will be applied
          {
            source: '/:path*',
            missing: [
              {
                type: 'header',
                key: 'x-rewrite-me',
              },
            ],
            destination: '/another-page',
          },
          // if the source, query, and cookie are matched,
          // this rewrite will be applied
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
            destination: '/:path*/home',
          },
          // if the header `x-authorized` is present and
          // contains a matching value, this rewrite will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'header',
                key: 'x-authorized',
                value: '(?<authorized>yes|true)',
              },
            ],

destination: '/home?authorized=:authorized',
          },
          // if the host is `example.com`,
          // this rewrite will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'host',
                value: 'example.com',
              },
            ],
            destination: '/another-page',
          },
        ]
      },
    }
[/code]

## 외부 URL로 리라이트하기[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#rewriting-to-an-external-url)

예시

  * [Using Multiple Zones](https://github.com/vercel/next.js/tree/canary/examples/with-zones)

리라이트를 사용하면 외부 URL로 라우트를 리라이트할 수 있습니다. 이는 Next.js를 점진적으로 도입할 때 특히 유용합니다. 아래는 메인 앱의 `/blog` 경로를 외부 사이트로 리다이렉트하는 리라이트 예시입니다.

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return [
          {
            source: '/blog',
            destination: 'https://example.com/blog',
          },
          {
            source: '/blog/:slug',
            destination: 'https://example.com/blog/:slug', // Matched parameters can be used in the destination
          },
        ]
      },
    }
[/code]

`trailingSlash: true`를 사용 중이라면 `source` 파라미터에도 트레일링 슬래시를 추가해야 합니다. 대상 서버도 트레일링 슬래시를 기대한다면 `destination` 파라미터에도 포함해야 합니다.

next.config.js
[code]
    module.exports = {
      trailingSlash: true,
      async rewrites() {
        return [
          {
            source: '/blog/',
            destination: 'https://example.com/blog/',
          },
          {
            source: '/blog/:path*/',
            destination: 'https://example.com/blog/:path*/',
          },
        ]
      },
    }
[/code]

### Next.js의 점진적 도입[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#incremental-adoption-of-nextjs)

모든 Next.js 라우트를 확인한 뒤에도 기존 웹사이트로 프록시하도록 Next.js가 폴백하도록 구성할 수 있습니다.

이렇게 하면 더 많은 페이지를 Next.js로 마이그레이션할 때 리라이트 구성을 변경할 필요가 없습니다.

next.config.js
[code]
    module.exports = {
      async rewrites() {
        return {
          fallback: [
            {
              source: '/:path*',
              destination: `https://custom-routes-proxying-endpoint.vercel.app/:path*`,
            },
          ],
        }
      },
    }
[/code]

### basePath 지원이 있는 리라이트[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#rewrites-with-basepath-support)

리라이트와 함께 [`basePath` 지원](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)을 사용할 때는 각 `source`와 `destination` 앞에 `basePath`가 자동으로 붙습니다. 특정 리라이트에서 `basePath`를 붙이지 않으려면 `basePath: false`를 추가하세요.

next.config.js
[code]
    module.exports = {
      basePath: '/docs',
     
      async rewrites() {
        return [
          {
            source: '/with-basePath', // automatically becomes /docs/with-basePath
            destination: '/another', // automatically becomes /docs/another
          },
          {
            // does not add /docs to /without-basePath since basePath: false is set
            // Note: this cannot be used for internal rewrites e.g. `destination: '/another'`
            source: '/without-basePath',
            destination: 'https://example.com',
            basePath: false,
          },
        ]
      },
    }
[/code]

### i18n 지원이 있는 리라이트[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#rewrites-with-i18n-support)

리라이트와 함께 [`i18n` 지원](https://nextjs.org/docs/pages/guides/internationalization)을 사용할 때는 구성된 `locales`를 처리하기 위해 각 `source`와 `destination` 앞에 로케일 접두사가 자동으로 붙습니다. 리라이트에 `locale: false`를 추가하면 자동 접두사가 비활성화되므로, 이 경우 올바르게 매칭되도록 `source`와 `destination`에 로케일을 직접 붙여야 합니다.

next.config.js
[code]
    module.exports = {
      i18n: {
        locales: ['en', 'fr', 'de'],
        defaultLocale: 'en',
      },
     
      async rewrites() {
        return [
          {
            source: '/with-locale', // automatically handles all locales
            destination: '/another', // automatically passes the locale on
          },
          {
            // does not handle locales automatically since locale: false is set
            source: '/nl/with-locale-manual',
            destination: '/nl/another',
            locale: false,
          },
          {
            // this matches '/' since `en` is the defaultLocale
            source: '/en',
            destination: '/en/another',
            locale: false,
          },
          {
            // it's possible to match all locales even when locale: false is set
            source: '/:locale/api-alias/:path*',
            destination: '/api/:path*',
            locale: false,
          },
          {
            // this gets converted to /(en|fr|de)/(.*) so will not match the top-level
            // `/` or `/fr` routes like /:path* would
            source: '/(.*)',
            destination: '/another',
          },
        ]
      },
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#version-history)

Version| Changes  
---|---  
`v13.3.0`| `missing` 추가.  
`v10.2.0`| `has` 추가.  
`v9.5.0`| 헤더 추가.  
  
도움이 되었나요?

지원됨.

보내기
