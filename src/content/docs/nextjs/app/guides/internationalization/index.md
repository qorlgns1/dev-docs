---
title: '가이드: 국제화'
description: '원본 URL: https://nextjs.org/docs/app/guides/internationalization'
---

# 가이드: 국제화 | Next.js

원본 URL: https://nextjs.org/docs/app/guides/internationalization

# 국제화

최종 업데이트 2026년 2월 20일

Next.js는 여러 언어를 지원하도록 콘텐츠의 라우팅과 렌더링을 구성할 수 있게 해 줍니다. 사이트를 다양한 로케일에 맞게 조정하려면 번역된 콘텐츠(로컬라이제이션)와 국제화된 라우트를 포함해야 합니다.

## 용어[](https://nextjs.org/docs/app/guides/internationalization#terminology)

  * **Locale:** 언어 및 형식 지정 기본 설정 세트를 나타내는 식별자입니다. 보통 사용자 선호 언어와 경우에 따라 지리적 지역을 포함합니다.
    * `en-US`: 미국에서 사용하는 영어
    * `nl-NL`: 네덜란드에서 사용하는 네덜란드어
    * `nl`: 특정 지역이 없는 네덜란드어

## 라우팅 개요[](https://nextjs.org/docs/app/guides/internationalization#routing-overview)

어느 로케일을 사용할지 선택할 때는 브라우저의 사용자 언어 기본 설정을 사용하는 것이 좋습니다. 기본 언어를 변경하면 애플리케이션으로 들어오는 `Accept-Language` 헤더가 수정됩니다.

예를 들어 다음 라이브러리를 사용하면 들어오는 `Request`를 살펴보고 `Headers`, 지원하려는 로케일, 기본 로케일에 따라 어떤 로케일을 선택할지 결정할 수 있습니다.

proxy.js
```
    import { match } from '@formatjs/intl-localematcher'
    import Negotiator from 'negotiator'

    let headers = { 'accept-language': 'en-US,en;q=0.5' }
    let languages = new Negotiator({ headers }).languages()
    let locales = ['en-US', 'nl-NL', 'nl']
    let defaultLocale = 'en-US'

    match(languages, locales, defaultLocale) // -> 'en-US'
```

라우팅은 서브 경로(`/fr/products`)나 도메인(`my-site.fr/products`) 중 하나로 국제화할 수 있습니다. 이 정보를 바탕으로 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) 내에서 로케일에 따라 사용자를 리디렉션할 수 있습니다.

proxy.js
```
    import { NextResponse } from "next/server";

    let locales = ['en-US', 'nl-NL', 'nl']

    // Get the preferred locale, similar to the above or using a library
    function getLocale(request) { ... }

    export function proxy(request) {
      // Check if there is any supported locale in the pathname
      const { pathname } = request.nextUrl
      const pathnameHasLocale = locales.some(
        (locale) => pathname.startsWith(`/${locale}/`) || pathname === `/${locale}`
      )

      if (pathnameHasLocale) return

      // Redirect if there is no locale
      const locale = getLocale(request)
      request.nextUrl.pathname = `/${locale}${pathname}`
      // e.g. incoming request is /products
      // The new URL is now /en-US/products
      return NextResponse.redirect(request.nextUrl)
    }

    export const config = {
      matcher: [
        // Skip all internal paths (_next)
        '/((?!_next).*)',
        // Optional: only run on root (/) URL
        // '/'
      ],
    }
```

마지막으로 `app/` 내부의 모든 특별 파일이 `app/[lang]` 하위에 중첩되어 있는지 확인하세요. 이렇게 하면 Next.js 라우터가 라우트에서 다양한 로케일을 동적으로 처리하고 `lang` 매개변수를 모든 레이아웃과 페이지에 전달할 수 있습니다. 예:

app/[lang]/page.tsx

JavaScriptTypeScript
```
    // You now have access to the current locale
    // e.g. /en-US/products -> `lang` is "en-US"
    export default async function Page({ params }: PageProps<'/[lang]'>) {
      const { lang } = await params
      return ...
    }
```

> **알아두면 좋아요:** `PageProps`와 `LayoutProps`는 라우트 매개변수에 대한 강력한 타입을 제공하는 전역 TypeScript 헬퍼입니다. 자세한 내용은 [PageProps](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)와 [LayoutProps](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)를 참조하세요.

루트 레이아웃 또한 새 폴더(예: `app/[lang]/layout.js`)에 중첩할 수 있습니다.

## 로컬라이제이션[](https://nextjs.org/docs/app/guides/internationalization#localization)

사용자의 선호 로케일에 따라 표시되는 콘텐츠를 변경하는 로컬라이제이션은 Next.js에만 국한된 개념이 아닙니다. 아래에 설명한 패턴은 어떤 웹 애플리케이션에서도 동일하게 작동합니다.

애플리케이션에서 영어와 네덜란드어 콘텐츠를 모두 지원한다고 가정해 보겠습니다. 우리는 키를 로컬라이즈된 문자열과 매핑해 주는 두 개의 서로 다른 “사전” 객체를 유지할 수 있습니다. 예:

dictionaries/en.json
```
    {
      "products": {
        "cart": "Add to Cart"
      }
    }
```

dictionaries/nl.json
```
    {
      "products": {
        "cart": "Toevoegen aan Winkelwagen"
      }
    }
```

그런 다음 요청된 로케일에 대한 번역을 불러오기 위해 `getDictionary` 함수를 만들 수 있습니다.

app/[lang]/dictionaries.ts

JavaScriptTypeScript
```
    import 'server-only'

    const dictionaries = {
      en: () => import('./dictionaries/en.json').then((module) => module.default),
      nl: () => import('./dictionaries/nl.json').then((module) => module.default),
    }

    export type Locale = keyof typeof dictionaries

    export const hasLocale = (locale: string): locale is Locale =>
      locale in dictionaries

    export const getDictionary = async (locale: Locale) => dictionaries[locale]()
```

현재 선택된 언어를 기준으로 레이아웃이나 페이지 내부에서 사전을 가져올 수 있습니다.

`lang`는 기본적으로 `string` 타입이므로 `hasLocale`을 사용하면 타입을 지원되는 로케일로 좁힐 수 있습니다. 또한 번역이 누락된 경우 런타임 오류 대신 404를 반환하도록 보장합니다.

app/[lang]/page.tsx

JavaScriptTypeScript
```
    import { notFound } from 'next/navigation'
    import { getDictionary, hasLocale } from './dictionaries'

    export default async function Page({ params }: PageProps<'/[lang]'>) {
      const { lang } = await params

      if (!hasLocale(lang)) notFound()

      const dict = await getDictionary(lang)
      return <button>{dict.products.cart}</button> // Add to Cart
    }
```

`app/` 디렉터리의 모든 레이아웃과 페이지는 기본적으로 [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)이므로, 번역 파일의 크기가 클라이언트 측 JavaScript 번들 크기에 영향을 줄까 걱정할 필요가 없습니다. 이 코드는 **서버에서만 실행되며**, 브라우저로 전송되는 것은 결과 HTML뿐입니다.

## 정적 렌더링[](https://nextjs.org/docs/app/guides/internationalization#static-rendering)

특정 로케일 세트에 대한 정적 라우트를 생성하려면 페이지나 레이아웃에서 `generateStaticParams`를 사용할 수 있습니다. 예를 들어 루트 레이아웃에서 전역으로 사용할 수 있습니다.

app/[lang]/layout.tsx

JavaScriptTypeScript
```
    export async function generateStaticParams() {
      return [{ lang: 'en-US' }, { lang: 'de' }]
    }

    export default async function RootLayout({
      children,
      params,
    }: LayoutProps<'/[lang]'>) {
      return (
        <html lang={(await params).lang}>
          <body>{children}</body>
        </html>
      )
    }
```

## 리소스[](https://nextjs.org/docs/app/guides/internationalization#resources)

  * [Minimal i18n routing and translations](https://github.com/vercel/next.js/tree/canary/examples/i18n-routing)
  * [`next-intl`](https://next-intl.dev)
  * [`next-international`](https://github.com/QuiiBz/next-international)
  * [`next-i18n-router`](https://github.com/i18nexus/next-i18n-router)
  * [`paraglide-next`](https://inlang.com/m/osslbuzt/paraglide-next-i18n)
  * [`lingui`](https://lingui.dev)
  * [`tolgee`](https://tolgee.io/apps-integrations/next)
  * [`next-intlayer`](https://intlayer.org/doc/environment/nextjs)
  * [`gt-next`](https://generaltranslation.com/en/docs/next)