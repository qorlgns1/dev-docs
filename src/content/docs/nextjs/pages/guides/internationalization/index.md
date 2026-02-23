---
title: '가이드: 국제화'
description: 'Next.js는 부터 국제화(i18n) 라우팅을 기본 지원합니다. 로케일 목록, 기본 로케일, 도메인별 로케일을 지정하면 Next.js가 라우팅을 자동으로 처리합니다.'
---

# 가이드: 국제화 | Next.js
소스 URL: https://nextjs.org/docs/pages/guides/internationalization

# Next.js에서 국제화를 구현하는 방법
마지막 업데이트 2026년 2월 20일

예제

  * [i18n 라우팅](https://github.com/vercel/next.js/tree/canary/examples/i18n-routing-pages)

Next.js는 `v10.0.0`부터 국제화([i18n](https://en.wikipedia.org/wiki/Internationalization_and_localization#Naming)) 라우팅을 기본 지원합니다. 로케일 목록, 기본 로케일, 도메인별 로케일을 지정하면 Next.js가 라우팅을 자동으로 처리합니다.

이 i18n 라우팅 지원은 [`react-intl`](https://formatjs.io/docs/getting-started/installation), [`react-i18next`](https://react.i18next.com/), [`lingui`](https://lingui.dev/), [`rosetta`](https://github.com/lukeed/rosetta), [`next-intl`](https://github.com/amannn/next-intl), [`next-translate`](https://github.com/aralroca/next-translate), [`next-multilingual`](https://github.com/Avansai/next-multilingual), [`tolgee`](https://tolgee.io/integrations/next), [`paraglide-next`](https://inlang.com/m/osslbuzt/paraglide-next-i18n), [`next-intlayer`](https://intlayer.org/doc/environment/nextjs/next-with-page-router), [`gt-react`](https://generaltranslation.com/en/docs/react) 등 기존 i18n 라이브러리 솔루션이 라우트와 로케일 파싱을 간소화할 수 있도록 보완하는 용도로 설계되었습니다.

## 시작하기[](https://nextjs.org/docs/pages/guides/internationalization#getting-started)

먼저 `next.config.js` 파일에 `i18n` 설정을 추가하세요.

로케일은 표준화된 로케일 정의 형식인 [UTS Locale Identifier](https://www.unicode.org/reports/tr35/tr35-59/tr35.html#Identifiers)를 사용합니다.

일반적으로 Locale Identifier는 언어, 지역, 스크립트를 하이픈으로 구분한 `language-region-script` 형태이며, 지역과 스크립트는 선택 사항입니다. 예를 들면 다음과 같습니다.

  * `en-US` \- 미국에서 사용되는 영어
  * `nl-NL` \- 네덜란드에서 사용되는 네덜란드어
  * `nl` \- 특정 지역을 지정하지 않은 네덜란드어

사용자 로케일이 `nl-BE`인데 설정에 없다면, `nl`이 있다면 그쪽으로, 없다면 기본 로케일로 리디렉션됩니다. 특정 국가의 모든 지역을 지원할 계획이 없다면, 폴백 역할을 할 국가 로케일을 포함해 두는 것이 좋습니다.

next.config.js
```
    module.exports = {
      i18n: {
        // These are all the locales you want to support in
        // your application
        locales: ['en-US', 'fr', 'nl-NL'],
        // This is the default locale you want to be used when visiting
        // a non-locale prefixed path e.g. `/hello`
        defaultLocale: 'en-US',
        // This is a list of locale domains and the default locale they
        // should handle (these are only required when setting up domain routing)
        // Note: subdomains must be included in the domain value to be matched e.g. "fr.example.com".
        domains: [
          {
            domain: 'example.com',
            defaultLocale: 'en-US',
          },
          {
            domain: 'example.nl',
            defaultLocale: 'nl-NL',
          },
          {
            domain: 'example.fr',
            defaultLocale: 'fr',
            // an optional http field can also be used to test
            // locale domains locally with http instead of https
            http: true,
          },
        ],
      },
    }
```

## 로케일 전략[](https://nextjs.org/docs/pages/guides/internationalization#locale-strategies)

로케일을 처리하는 전략은 서브 경로 라우팅(Sub-path Routing)과 도메인 라우팅(Domain Routing) 두 가지가 있습니다.

### 서브 경로 라우팅[](https://nextjs.org/docs/pages/guides/internationalization#sub-path-routing)

서브 경로 라우팅은 URL 경로에 로케일을 포함합니다.

next.config.js
```
    module.exports = {
      i18n: {
        locales: ['en-US', 'fr', 'nl-NL'],
        defaultLocale: 'en-US',
      },
    }
```

위 설정을 사용하면 `en-US`, `fr`, `nl-NL`로 라우팅할 수 있고, `en-US`가 기본 로케일입니다. `pages/blog.js`가 있다면 다음 URL을 사용할 수 있습니다.

  * `/blog`
  * `/fr/blog`
  * `/nl-nl/blog`

기본 로케일에는 접두사가 붙지 않습니다.

### 도메인 라우팅[](https://nextjs.org/docs/pages/guides/internationalization#domain-routing)

도메인 라우팅을 사용하면 로케일별로 서로 다른 도메인에서 콘텐츠를 제공하도록 구성할 수 있습니다.

next.config.js
```
    module.exports = {
      i18n: {
        locales: ['en-US', 'fr', 'nl-NL', 'nl-BE'],
        defaultLocale: 'en-US',

        domains: [
          {
            // Note: subdomains must be included in the domain value to be matched
            // e.g. www.example.com should be used if that is the expected hostname
            domain: 'example.com',
            defaultLocale: 'en-US',
          },
          {
            domain: 'example.fr',
            defaultLocale: 'fr',
          },
          {
            domain: 'example.nl',
            defaultLocale: 'nl-NL',
            // specify other locales that should be redirected
            // to this domain
            locales: ['nl-BE'],
          },
        ],
      },
    }
```

예를 들어 `pages/blog.js`가 있다면 다음 URL이 제공됩니다.

  * `example.com/blog`
  * `www.example.com/blog`
  * `example.fr/blog`
  * `example.nl/blog`
  * `example.nl/nl-BE/blog`

## 자동 로케일 감지[](https://nextjs.org/docs/pages/guides/internationalization#automatic-locale-detection)

사용자가 애플리케이션 루트(일반적으로 `/`)에 방문하면, Next.js는 [`Accept-Language`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Accept-Language) 헤더와 현재 도메인을 기준으로 사용자가 선호하는 로케일을 자동으로 감지하려고 시도합니다.

기본 로케일과 다른 로케일이 감지되면 사용자는 다음 중 한 곳으로 리디렉션됩니다.

  * **서브 경로 라우팅을 사용하는 경우:** 로케일 접두사가 붙은 경로
  * **도메인 라우팅을 사용하는 경우:** 해당 로케일이 기본으로 지정된 도메인

도메인 라우팅을 사용할 때 `Accept-Language` 헤더가 `fr;q=0.9`인 사용자가 `example.com`에 방문하면, `fr` 로케일을 처리하는 기본 도메인인 `example.fr`로 리디렉션됩니다.

서브 경로 라우팅을 사용할 때는 `/fr`로 리디렉션됩니다.

### 기본 로케일에 접두사 추가[](https://nextjs.org/docs/pages/guides/internationalization#prefixing-the-default-locale)

Next.js 12와 [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)를 함께 사용하면 [우회 방법](https://github.com/vercel/next.js/discussions/18419)을 통해 기본 로케일에도 접두사를 붙일 수 있습니다.

예를 들어, 몇 가지 언어를 지원하는 `next.config.js`는 다음과 같습니다. `"default"` 로케일을 의도적으로 추가했다는 점에 주목하세요.

next.config.js
```
    module.exports = {
      i18n: {
        locales: ['default', 'en', 'de', 'fr'],
        defaultLocale: 'default',
        localeDetection: false,
      },
      trailingSlash: true,
    }
```

이제 [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)를 사용해 사용자 지정 라우팅 규칙을 추가할 수 있습니다.

proxy.ts
```
    import { NextRequest, NextResponse } from 'next/server'

    const PUBLIC_FILE = /\.(.*)$/

    export async function proxy(req: NextRequest) {
      if (
        req.nextUrl.pathname.startsWith('/_next') ||
        req.nextUrl.pathname.includes('/api/') ||
        PUBLIC_FILE.test(req.nextUrl.pathname)
      ) {
        return
      }

      if (req.nextUrl.locale === 'default') {
        const locale = req.cookies.get('NEXT_LOCALE')?.value || 'en'

        return NextResponse.redirect(
          new URL(`/${locale}${req.nextUrl.pathname}${req.nextUrl.search}`, req.url)
        )
      }
    }
```

이 [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)는 [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)와 [public](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder) 폴더의 글꼴·이미지 같은 파일에는 기본 접두사를 추가하지 않습니다. 기본 로케일로 요청이 들어오면 `/en` 접두사로 리디렉션합니다.

### 자동 로케일 감지 비활성화[](https://nextjs.org/docs/pages/guides/internationalization#disabling-automatic-locale-detection)

자동 로케일 감지는 다음 설정으로 비활성화할 수 있습니다.

next.config.js
```
    module.exports = {
      i18n: {
        localeDetection: false,
      },
    }
```

`localeDetection`을 `false`로 설정하면, Next.js는 더 이상 사용자가 선호하는 로케일을 기반으로 자동 리디렉션하지 않고, 앞서 설명한 대로 로케일 기반 도메인이나 경로에서 감지한 로케일 정보만 제공합니다.

## 로케일 정보에 접근하기[](https://nextjs.org/docs/pages/guides/internationalization#accessing-the-locale-information)

Next.js 라우터를 통해 로케일 정보를 가져올 수 있습니다. 예를 들어 [`useRouter()`](https://nextjs.org/docs/pages/api-reference/functions/use-router) 훅을 사용하면 다음 속성을 확인할 수 있습니다.

  * `locale`에는 현재 활성 로케일이 들어 있습니다.
  * `locales`에는 구성된 모든 로케일이 들어 있습니다.
  * `defaultLocale`에는 구성된 기본 로케일이 들어 있습니다.

`getStaticProps` 또는 `getServerSideProps`로 [사전 렌더링](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)할 때 함수에 제공되는 [context](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)에 로케일 정보가 포함됩니다.

`getStaticPaths`를 사용할 때는 함수의 context 매개변수에서 구성된 로케일을 `locales`로, 구성된 기본 로케일을 `defaultLocale`로 전달받습니다.

## 로케일 간 전환[](https://nextjs.org/docs/pages/guides/internationalization#transition-between-locales)

`next/link` 또는 `next/router`를 사용해 로케일 간 전환을 수행할 수 있습니다.

`next/link`에서는 현재 활성 로케일과 다른 로케일로 전환하려면 `locale` prop을 제공하면 됩니다. `locale` prop을 제공하지 않으면 클라이언트 전환 동안 현재 활성 `locale`이 사용됩니다. 예:

```
    import Link from 'next/link'

    export default function IndexPage(props) {
      return (
        <Link href="/another" locale="fr">
          To /fr/another
        </Link>
      )
    }
```

`next/router` 메서드를 직접 사용할 때는 전환 옵션으로 사용할 `locale`을 지정할 수 있습니다. 예:

```
    import { useRouter } from 'next/router'

    export default function IndexPage(props) {
      const router = useRouter()

      return (
        <div
          onClick={() => {
            router.push('/another', '/another', { locale: 'fr' })
          }}
        >
          to /fr/another
        </div>
      )
    }
```

[동적 라우트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)의 쿼리 값이나 숨겨진 href 쿼리 값 등 모든 라우팅 정보를 유지하면서 `locale`만 전환하려면 `href` 매개변수를 객체로 전달할 수 있습니다.
```
    import { useRouter } from 'next/router'
    const router = useRouter()
    const { pathname, asPath, query } = router
    // change just the locale and maintain all other route information including href's query
    router.push({ pathname, query }, asPath, { locale: nextLocale })
```

`router.push`에서 URL 객체 구조를 사용하는 방법은 [여기](https://nextjs.org/docs/pages/api-reference/functions/use-router#with-url-object)를 참고하세요.

이미 로케일이 포함된 `href`가 있다면 로케일 접두사를 자동으로 처리하는 동작을 비활성화할 수 있습니다.
```
    import Link from 'next/link'

    export default function IndexPage(props) {
      return (
        <Link href="/fr/another" locale={false}>

To /fr/another
        </Link>
      )
    }
```

## `NEXT_LOCALE` 쿠키 활용하기[](https://nextjs.org/docs/pages/guides/internationalization#leveraging-the-next_locale-cookie)

Next.js는 `NEXT_LOCALE=the-locale` 쿠키 설정을 허용하며, 이는 accept-language 헤더보다 우선합니다. 이 쿠키는 언어 전환기를 통해 설정할 수 있고, 사용자가 사이트에 다시 방문하면 `/`에서 올바른 로케일 위치로 리디렉션할 때 쿠키에 지정된 로케일을 활용합니다.

예를 들어, 사용자의 accept-language 헤더가 로케일 `fr`를 선호하더라도 `NEXT_LOCALE=en` 쿠키가 설정되어 있으면 `/`를 방문할 때 쿠키가 제거되거나 만료될 때까지 사용자는 `en` 로케일 위치로 리디렉션됩니다.

## 검색 엔진 최적화[](https://nextjs.org/docs/pages/guides/internationalization#search-engine-optimization)

Next.js는 사용자가 어떤 언어로 사이트를 방문하는지 알고 있으므로 `<html>` 태그에 `lang` 속성을 자동으로 추가합니다.

Next.js는 페이지 변형을 알지 못하므로 [`next/head`](https://nextjs.org/docs/pages/api-reference/components/head)를 사용해 `hreflang` 메타 태그를 직접 추가해야 합니다. `hreflang`에 대해 더 알아보려면 [Google Webmasters documentation](https://support.google.com/webmasters/answer/189077)을 참고하세요.

## 정적 생성과 함께 작동하는 방식[](https://nextjs.org/docs/pages/guides/internationalization#how-does-this-work-with-static-generation)

> 국제화 라우팅은 Next.js 라우팅 계층을 활용하지 않으므로 [`output: 'export'`](https://nextjs.org/docs/pages/guides/static-exports)와 통합되지 않습니다. `output: 'export'`를 사용하지 않는 하이브리드 Next.js 애플리케이션은 완전히 지원됩니다.

### 동적 라우트와 `getStaticProps` 페이지[](https://nextjs.org/docs/pages/guides/internationalization#dynamic-routes-and-getstaticprops-pages)

`getStaticProps`를 [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)와 함께 사용하는 페이지의 경우, 사전 렌더링하려는 페이지의 모든 로케일 변형을 [`getStaticPaths`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)에서 반환해야 합니다. `paths`에 대해 반환되는 `params` 객체와 함께, 렌더링하려는 로케일을 지정하는 `locale` 필드를 반환할 수도 있습니다. 예:

pages/blog/[slug].js
```
    export const getStaticPaths = ({ locales }) => {
      return {
        paths: [
          // if no `locale` is provided only the defaultLocale will be generated
          { params: { slug: 'post-1' }, locale: 'en-US' },
          { params: { slug: 'post-1' }, locale: 'fr' },
        ],
        fallback: true,
      }
    }
```

[Automatically Statically Optimized](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) 페이지와 비동적 `getStaticProps` 페이지의 경우 **각 로케일마다 페이지 버전이 생성됩니다.** 이는 `getStaticProps`에 구성된 로케일 수에 따라 빌드 시간이 늘어날 수 있으므로 중요합니다.

예를 들어, `getStaticProps`를 사용하는 비동적 페이지 10개에 대해 50개의 로케일을 구성하면 `getStaticProps`가 500번 호출됩니다. 각 빌드마다 10개 페이지의 50개 버전이 생성됩니다.

`getStaticProps`를 사용하는 동적 페이지의 빌드 시간을 줄이려면 [`fallback` 모드](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)를 사용하세요. 그러면 빌드 중에 사전 렌더링할 가장 인기 있는 경로와 로케일만 `getStaticPaths`에서 반환할 수 있으며, Next.js가 나머지 페이지를 요청 시 런타임에 생성합니다.

### 자동 정적 최적화 페이지[](https://nextjs.org/docs/pages/guides/internationalization#automatically-statically-optimized-pages)

[자동으로 정적 최적화되는](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) 페이지에는 각 로케일 버전이 생성됩니다.

### 비동적 getStaticProps 페이지[](https://nextjs.org/docs/pages/guides/internationalization#non-dynamic-getstaticprops-pages)

비동적 `getStaticProps` 페이지도 위와 같이 각 로케일 버전이 생성됩니다. `getStaticProps`는 렌더링되는 각 `locale`과 함께 호출됩니다. 특정 로케일을 사전 렌더링에서 제외하려면 `getStaticProps`에서 `notFound: true`를 반환하면 해당 페이지 변형이 생성되지 않습니다.
```
    export async function getStaticProps({ locale }) {
      // Call an external API endpoint to get posts.
      // You can use any data fetching library
      const res = await fetch(`https://.../posts?locale=${locale}`)
      const posts = await res.json()

      if (posts.length === 0) {
        return {
          notFound: true,
        }
      }

      // By returning { props: posts }, the Blog component
      // will receive `posts` as a prop at build time
      return {
        props: {
          posts,
        },
      }
    }
```

## i18n 구성 한계[](https://nextjs.org/docs/pages/guides/internationalization#limits-for-the-i18n-config)

  * `locales`: 총 100개의 로케일
  * `domains`: 총 100개의 로케일 도메인 항목

> **알아두면 좋은 점** : 이러한 한계는 [빌드 시간 성능 문제](https://nextjs.org/docs/pages/guides/internationalization#dynamic-routes-and-getstaticprops-pages)를 방지하기 위해 처음 도입되었습니다. Next.js 12에서 [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)를 사용하는 사용자 지정 라우팅으로 이 한계를 우회할 수 있습니다.

보내기