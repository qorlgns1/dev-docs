---
title: 'next.config.js: 리라이트'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites'
---

# next.config.js: 리라이트 | Next.js
원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)리라이트

페이지 복사

# 리라이트

최종 업데이트 2026년 2월 20일

리라이트를 사용하면 들어오는 요청 경로를 다른 대상 경로에 매핑할 수 있습니다.

리라이트는 URL 프록시처럼 동작하여 대상 경로를 가려 주고, 사용자가 사이트에서 위치를 이동하지 않은 것처럼 보이게 합니다. 반면 [리다이렉트](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)는 새 페이지로 다시 라우팅하며 URL 변경 사항을 보여 줍니다.

리라이트를 사용하려면 `next.config.js`에서 `rewrites` 키를 사용할 수 있습니다:

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

리라이트는 클라이언트 측 라우팅에 적용됩니다. 위 예시에서 `<Link href="/about">`로 이동하면 `/about` URL을 유지한 채 `/`의 콘텐츠를 제공합니다.

`rewrites`는 `source`와 `destination` 속성을 가진 객체들을 담은 배열 또는 (아래에서 설명하는) 배열 객체를 반환해야 하는 async 함수입니다:

  * `source`: `String` \- 들어오는 요청 경로 패턴입니다.
  * `destination`: `String` \- 라우팅하려는 경로입니다.
  * `basePath`: `false` 또는 `undefined` \- false일 경우 basePath는 매칭 시 포함되지 않으며, 외부 리라이트에만 사용할 수 있습니다.
  * `locale`: `false` 또는 `undefined` \- 매칭 시 로케일을 포함하지 않을지 여부입니다.
  * `has`는 `type`, `key`, `value` 속성을 가진 [has 객체](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching) 배열입니다.
  * `missing`은 `type`, `key`, `value` 속성을 가진 [missing 객체](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching) 배열입니다.

`rewrites` 함수가 배열을 반환하면, 리라이트는 파일 시스템(페이지와 `/public` 파일) 확인 후 동적 라우트 전에 적용됩니다. `rewrites` 함수가 특정 형태의 배열 객체를 반환하면 Next.js `v10.1`부터 이 동작을 변경하고 더 정밀하게 제어할 수 있습니다:

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

> **알아두면 좋아요** : `beforeFiles`의 리라이트는 source를 매칭한 직후 파일 시스템/동적 라우트를 확인하지 않고, 모든 `beforeFiles`가 확인될 때까지 계속됩니다.

Next.js에서 라우트를 확인하는 순서는 다음과 같습니다:

  1. [headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)를 확인/적용
  2. [redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)를 확인/적용
  3. [proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  4. `beforeFiles` 리라이트를 확인/적용
  5. [public 디렉터리](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)의 정적 파일, `_next/static` 파일, 비동적 페이지를 확인/제공
  6. `afterFiles` 리라이트를 확인/적용하며, 이 중 하나가 매칭되면 매칭마다 동적 라우트/정적 파일을 확인
  7. `fallback` 리라이트를 확인/적용하며, 이는 404 페이지 렌더링 전에, 그리고 동적 라우트/모든 정적 자산을 확인한 뒤 적용됩니다. `getStaticPaths`에서 [fallback: true/'blocking'](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)을 사용하면, `next.config.js`에 정의된 fallback `rewrites`는 실행되지 않습니다.

## 리라이트 매개변수[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#rewrite-parameters)

리라이트에서 매개변수를 사용할 때, 해당 매개변수가 `destination`에 사용되지 않으면 기본적으로 쿼리에 전달됩니다.

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

매개변수가 destination에서 사용되면 어떤 매개변수도 자동으로 쿼리에 전달되지 않습니다.

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

이미 destination에서 하나의 매개변수를 사용하고 있더라도, `destination`에서 쿼리를 지정하여 매개변수를 수동으로 전달할 수 있습니다.

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

> **알아두면 좋아요** : [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)의 정적 페이지나 [프리렌더링](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)에서 리라이트로 전달된 매개변수는 하이드레이션 이후 클라이언트에서 파싱되어 쿼리로 제공됩니다.

## 경로 매칭[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#path-matching)

경로 매칭이 허용되며, 예를 들어 `/blog/:slug`는 `/blog/first-post`와 매칭됩니다(중첩 경로 없음).

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

`/blog/:slug` 패턴은 `/blog/first-post`, `/blog/post-1`과 매칭되지만 `/blog/a/b`와는 매칭되지 않습니다(중첩 경로 없음). 패턴은 시작 지점에 고정되므로 `/blog/:slug`는 `/archive/blog/first-post`와 매칭되지 않습니다.

매개변수에 `*`(0개 이상), `+`(1개 이상), `?`(0개 또는 1개)와 같은 수식어를 사용할 수 있습니다. 예를 들어 `/blog/:slug*`는 `/blog`, `/blog/a`, `/blog/a/b/c`와 매칭됩니다.

자세한 내용은 [path-to-regexp](https://github.com/pillarjs/path-to-regexp) 문서를 참고하세요.

### 와일드카드 경로 매칭[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#wildcard-path-matching)

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

### 정규식 경로 매칭[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#regex-path-matching)

정규식 경로를 매칭하려면 매개변수 뒤에 괄호로 정규식을 감싸면 됩니다. 예를 들어 `/blog/:slug(\\d{1,})`는 `/blog/123`와 매칭되지만 `/blog/abc`와는 매칭되지 않습니다:

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

정규식 경로 매칭에 사용되는 문자는 `(`, `)`, `{`, `}`, `[`, `]`, `|`, `\`, `^`, `.`, `:`, `*`, `+`, `-`, `?`, `$`이며, `source`에서 특수 용도가 아닌 값으로 사용하려면 앞에 `\\`를 추가해 이스케이프해야 합니다:

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

## 헤더, 쿠키, 쿼리 매칭[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching)

헤더, 쿠키, 쿼리 값이 `has` 필드와 일치하거나 `missing` 필드와 일치하지 않을 때만 리라이트를 매칭하도록 제한할 수 있습니다. 리라이트가 적용되려면 `source`와 모든 `has` 항목이 일치해야 하고, 모든 `missing` 항목은 일치하지 않아야 합니다.

`has`와 `missing` 항목에는 다음 필드를 사용할 수 있습니다:

  * `type`: `String` \- `header`, `cookie`, `host`, `query` 중 하나여야 합니다.
  * `key`: `String` \- 선택한 타입에서 매칭하려는 키입니다.
  * `value`: `String` 또는 `undefined` \- 확인할 값이며, undefined면 아무 값이나 매칭됩니다. `value`에 `first-(?<paramName>.*)`와 같은 정규식 문자열을 사용하면, `first-second` 값에서 `second`를 추출해 `:paramName`으로 destination에서 사용할 수 있습니다.

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
[/code]

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

## 외부 URL로 재작성[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#rewriting-to-an-external-url)

예시

  * [여러 영역 사용](https://github.com/vercel/next.js/tree/canary/examples/with-zones)



리라이트를 사용하면 외부 URL로 라우트를 재작성할 수 있으므로 Next.js를 점진적으로 도입할 때 특히 유용합니다. 아래 예시는 메인 앱의 `/blog` 라우트를 외부 사이트로 리디렉션하기 위한 리라이트입니다.

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

`trailingSlash: true`를 사용하는 경우 `source` 파라미터에도 슬래시를 추가해야 합니다. 대상 서버가 트레일링 슬래시를 기대한다면 `destination` 파라미터에도 포함해야 합니다.

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

### Next.js 점진적 도입[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#incremental-adoption-of-nextjs)

모든 Next.js 라우트를 확인한 뒤 기존 웹사이트로 프록시하도록 Next.js를 폴백시킬 수도 있습니다.

이렇게 하면 더 많은 페이지를 Next.js로 마이그레이션할 때마다 리라이트 구성을 변경할 필요가 없습니다.

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

### basePath 지원과 함께하는 리라이트[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#rewrites-with-basepath-support)

리라이트와 함께 [`basePath` 지원](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)을 활용하면 `basePath: false`를 리라이트에 추가하지 않는 한 각 `source`와 `destination`이 자동으로 `basePath`로 접두사 처리됩니다.

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

## 버전 기록[](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#version-history)

버전| 변경 사항  
---|---  
`v13.3.0`| `missing`이 추가되었습니다.  
`v10.2.0`| `has`가 추가되었습니다.  
`v9.5.0`| Headers가 추가되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
