---
title: '로케일 기반 라우팅 설정'
description: '원본 URL: https://next-intl.dev/docs/routing/setup'
---

원본 URL: https://next-intl.dev/docs/routing/setup

# 로케일 기반 라우팅 설정

영상으로 보는 편이 좋으신가요?

[라우팅 설정](https://learn.next-intl.dev/chapters/06-routing/01-setup)

앱이 지원하는 각 언어마다 고유한 경로명을 사용하기 위해 `next-intl`은 다음 라우팅 구성을 처리하는 데 사용할 수 있습니다:

  1. 프리픽스 기반 라우팅 (예: `/en/about`)
  2. 도메인 기반 라우팅 (예: `en.example.com/about`)

어느 경우든 `next-intl`은 최상위 `[locale]` [동적 세그먼트](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes)를 사용해 App Router와 통합되며, 이를 통해 다양한 언어의 콘텐츠를 제공할 수 있습니다.

## 초기 설정[](https://next-intl.dev/docs/routing/setup#initial-setup)

로케일 기반 라우팅을 시작하기 위해 다음 파일들을 설정하겠습니다:

### `src/i18n/routing.ts`[](https://next-intl.dev/docs/routing/setup#i18n-routing)

라우팅 구성을 정의하는 중앙 위치로 `routing.ts`를 사용합니다:

src/i18n/routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // A list of all locales that are supported
      locales: ['en', 'de'],

      // Used when no locale matches
      defaultLocale: 'en'
    });
```

요구사항에 따라 이후 라우팅 구성을 커스터마이징할 수 있지만, 우선 설정을 먼저 마무리해 보겠습니다.

### `src/proxy.ts`[](https://next-intl.dev/docs/routing/setup#proxy)

라우팅 구성이 준비되면 이를 사용해 프록시를 설정할 수 있습니다:

src/proxy.ts
```
    import createMiddleware from 'next-intl/middleware';
    import {routing} from './i18n/routing';

    export default createMiddleware(routing);

    export const config = {
      // Match all pathnames except for
      // - … if they start with `/api`, `/trpc`, `/_next` or `/_vercel`
      // - … the ones containing a dot (e.g. `favicon.ico`)
      matcher: '/((?!api|trpc|_next|_vercel|.*\\..*).*)'
    };
```

**참고:** `proxy.ts`는 Next.js 16 이전까지 `middleware.ts`라고 불렸습니다.

[](https://next-intl.dev/docs/routing/setup#proxy-matcher-dots)`/users/jane.doe`처럼 점이 포함된 경로명은 어떻게 매칭하나요?

점이 포함되는 경로명을 예상하는 경우, 명시적인 항목으로 매칭할 수 있습니다:

src/proxy.ts
```
    // ...

    export const config = {
      matcher: [
        // Match all pathnames except for
        // - … if they start with `/api`, `/trpc`, `/_next` or `/_vercel`
        // - … the ones containing a dot (e.g. `favicon.ico`)
        '/((?!api|trpc|_next|_vercel|.*\\..*).*)',

        // Match all pathnames within `{/:locale}/users`
        '/([\\w-]+)?/users/(.+)'
      ]
    };
```

이렇게 하면 예를 들어 `/users/jane.doe`를 매칭하며, 로케일 프리픽스가 있는 경우도 선택적으로 매칭합니다.

### `src/i18n/navigation.ts`[](https://next-intl.dev/docs/routing/setup#i18n-navigation)

추가로, 라우팅 구성을 사용해 내비게이션 API를 설정할 수 있습니다:

src/i18n/navigation.ts
```
    import {createNavigation} from 'next-intl/navigation';
    import {routing} from './routing';

    // Lightweight wrappers around Next.js' navigation
    // APIs that consider the routing configuration
    export const {Link, redirect, usePathname, useRouter, getPathname} =
      createNavigation(routing);
```

### `src/i18n/request.ts`[](https://next-intl.dev/docs/routing/setup#i18n-request)

이제 요청 구성에서 매칭된 로케일을 읽을 수 있습니다:

src/i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';
    import {hasLocale} from 'next-intl';
    import {routing} from './routing';

    export default getRequestConfig(async ({requestLocale}) => {
      // Typically corresponds to the `[locale]` segment
      const requested = await requestLocale;
      const locale = hasLocale(routing.locales, requested)
        ? requested
        : routing.defaultLocale;

      return {
        locale
        // ...
      };
    });
```

### `src/app/[locale]/layout.tsx`[](https://next-intl.dev/docs/routing/setup#layout)

설정을 완료하기 위해 기존의 모든 레이아웃과 페이지를 `[locale]` 세그먼트로 이동합니다:
```
    src
    └── app
        └── [locale]
            ├── layout.tsx
            ├── page.tsx
            └── ...
```

이제 매칭된 `locale`은 `[locale]` 파라미터를 통해 사용할 수 있습니다:

app/[locale]/layout.tsx
```
    import {NextIntlClientProvider, hasLocale} from 'next-intl';
    import {notFound} from 'next/navigation';
    import {routing} from '@/i18n/routing';

    type Props = {
      children: React.ReactNode;
      params: Promise<{locale: string}>;
    };

    export default async function LocaleLayout({children, params}: Props) {
      // Ensure that the incoming `locale` is valid
      const {locale} = await params;
      if (!hasLocale(routing.locales, locale)) {
        notFound();
      }

      // ...
    }
```

이것으로 충분합니다! 여기서부터는 [라우팅 구성](https://next-intl.dev/docs/routing/configuration)을 통해 필요에 맞게 조정할 수 있습니다.

문제가 발생했다면, 동작하는 앱을 확인할 수 있는 [App Router 예제](https://next-intl.dev/examples#app-router)를 참고해 보세요.

## 정적 렌더링[](https://next-intl.dev/docs/routing/setup#static-rendering)

로케일 기반 라우팅을 사용할 때 현재 `next-intl`은 Server Components에서 `useTranslations` 같은 API를 사용하면 동적 렌더링을 선택합니다. 이는 향후 제거를 목표로 하는 제한사항이지만, 임시 해결책으로 `next-intl`은 정적 렌더링을 활성화할 수 있는 임시 API를 제공합니다.

### `generateStaticParams` 추가[](https://next-intl.dev/docs/routing/setup#add-generatestaticparams)

`[locale]` 파라미터에 동적 라우트 세그먼트를 사용하고 있으므로, 빌드 시점에 라우트를 렌더링할 수 있도록 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)를 사용해야 합니다.

필요에 따라 `generateStaticParams`를 레이아웃 또는 페이지에 추가할 수 있습니다:

  1. **레이아웃**: 이 레이아웃 내 모든 페이지에 정적 렌더링을 활성화합니다 (예: `app/[locale]/layout.tsx`)
  2. **개별 페이지**: 특정 페이지에 정적 렌더링을 활성화합니다 (예: `app/[locale]/page.tsx`)

**예시:**
```
     import {routing} from '@/i18n/routing';

    export function generateStaticParams() {
      return routing.locales.map((locale) => ({locale}));
    }
```

[](https://next-intl.dev/docs/routing/setup#generatestaticparams-locales)`generateStaticParams`에서 모든 로케일을 반환해야 하나요?

빌드 시점에 특정 로케일만 렌더링하거나 아예 렌더링하지 않으려면, `generateStaticParams`에서 반환할 항목을 선택적으로 지정할 수 있습니다 (Next.js 문서의 [Static Rendering](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#static-rendering) 참고).

### 관련된 모든 레이아웃과 페이지에 `setRequestLocale` 추가[](https://next-intl.dev/docs/routing/setup#add-setrequestlocale-to-all-relevant-layouts-and-pages)

`next-intl`은 레이아웃과 페이지에서 `params`를 통해 전달받은 로케일을 분배하여, 해당 요청의 일부로 렌더링되는 모든 Server Components에서 사용할 수 있게 하는 API를 제공합니다.

app/[locale]/layout.tsx
```
    import {setRequestLocale} from 'next-intl/server';
    import {hasLocale} from 'next-intl';
    import {notFound} from 'next/navigation';
    import {routing} from '@/i18n/routing';

    type Props = {
      children: React.ReactNode;
      params: Promise<{locale: string}>;
    };

    export default async function LocaleLayout({children, params}: Props) {
      const {locale} = await params;
      if (!hasLocale(routing.locales, locale)) {
        notFound();
      }

      // Enable static rendering
      setRequestLocale(locale);

      return (
        // ...
      );
    }
```

app/[locale]/page.tsx
```
    import {use} from 'react';
    import {setRequestLocale} from 'next-intl/server';
    import {useTranslations} from 'next-intl';

    export default function IndexPage({params}) {
      const {locale} = use(params);

      // Enable static rendering
      setRequestLocale(locale);

      // Once the request locale is set, you
      // can call hooks from `next-intl`
      const t = useTranslations('IndexPage');

      return (
        // ...
      );
    }
```

**다음 사항을 유의하세요:**

  1. `setRequestLocale`에 전달하는 로케일은 검증되어야 합니다 (예: [루트 레이아웃](https://next-intl.dev/docs/routing/setup#layout)에서).
  2. Next.js는 레이아웃과 페이지를 독립적으로 렌더링할 수 있으므로, 정적 렌더링을 활성화하려는 모든 페이지와 모든 레이아웃에서 이 함수를 호출해야 합니다.
  3. `useTranslations` 또는 `getMessages` 같은 `next-intl` 함수들을 호출하기 전에 `setRequestLocale`를 호출해야 합니다.

[](https://next-intl.dev/docs/routing/setup#setrequestlocale-implementation)`setRequestLocale`는 어떻게 동작하나요?

`next-intl`은 현재 로케일을 저장하는 변경 가능한 저장소를 만들기 위해 [`cache()`](https://react.dev/reference/react/cache)를 사용합니다. `setRequestLocale`를 호출하면 현재 로케일이 저장소에 기록되어, 로케일이 필요한 모든 API에서 사용할 수 있게 됩니다.

이 저장소는 요청 범위로 한정되므로, 특정 요청이 비동기로 처리되는 동안 병렬로 처리되는 다른 요청에는 영향을 주지 않습니다.

[](https://next-intl.dev/docs/routing/setup#setrequestlocale-background)왜 이 API가 필요한가요?

현재 Next.js는 Server Components의 임의 위치에서 `locale` 같은 라우트 파라미터를 읽는 API를 제공하지 않습니다 ([`vercel/next.js`#58862](https://github.com/vercel/next.js/discussions/58862) 참고). `locale`은 `next-intl`이 제공하는 모든 API의 핵심이므로, 이를 트리 전체에 prop으로 계속 전달하는 방식은 사용성이 좋지 않습니다.

이 때문에 `next-intl`은 미들웨어를 사용해 협상된 로케일 값을 담은 `x-next-intl-locale` 헤더를 들어오는 요청에 추가합니다. 이 방식으로 `headers().get('x-next-intl-locale')`를 통해 임의 위치에서 로케일을 읽을 수 있습니다.

하지만 `headers`를 사용하면 해당 라우트는 동적 렌더링으로 전환됩니다.

`setRequestLocale`를 사용하면 레이아웃과 페이지에서 `params`로 받은 로케일을 `next-intl`에 제공할 수 있습니다. 이제 `next-intl`의 모든 API는 헤더 대신 이 값을 읽을 수 있으므로 정적 렌더링이 가능해집니다.

### 메타데이터에서 `locale` 파라미터 사용[](https://next-intl.dev/docs/routing/setup#use-the-locale-param-in-metadata)

페이지 렌더링뿐 아니라 페이지 메타데이터도 정적 렌더링 조건을 충족해야 합니다.

이를 위해 Next.js에서 `params`로 받은 `locale`을 [`next-intl`의 await 가능한 함수들](https://next-intl.dev/docs/environments/server-client-components#async-components)에 전달할 수 있습니다.

page.tsx
```
    import {getTranslations} from 'next-intl/server';

    export async function generateMetadata({params}) {
      const {locale} = await params;
      const t = await getTranslations({locale, namespace: 'Metadata'});

      return {
        title: t('title')
      };
    }
```

