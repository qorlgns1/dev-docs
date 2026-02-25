---
title: 'Navigation API'
description: '은 ,  같은 Next.js의 내비게이션 API를 감싸는 가벼운 wrapper를 제공하며, 내부적으로 사용자 locale과 pathname을 자동으로 처리합니다.'
---

Source URL: https://next-intl.dev/docs/routing/navigation

# Navigation API

영상으로 보는 편이신가요?

[Navigation APIs](https://learn.next-intl.dev/chapters/06-routing/04-navigation-apis)

`next-intl`은 [`<Link />`](https://nextjs.org/docs/app/api-reference/components/link), [`useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router) 같은 Next.js의 내비게이션 API를 감싸는 가벼운 wrapper를 제공하며, 내부적으로 사용자 locale과 pathname을 자동으로 처리합니다.

이 API들을 만들려면 `routing` 설정과 함께 `createNavigation` 함수를 호출하면 됩니다.

navigation.ts
```
    import {createNavigation} from 'next-intl/navigation';
    import {routing} from './routing';

    export const {Link, redirect, usePathname, useRouter, getPathname} =
      createNavigation(routing);
```

이 함수는 보통 컴포넌트에서 내비게이션 API에 쉽게 접근할 수 있도록 [`src/i18n/navigation.ts`](https://next-intl.dev/docs/routing/setup#i18n-navigation) 같은 중앙 모듈에서 호출합니다.

[](https://next-intl.dev/docs/routing/navigation#locales-unknown)빌드 시점에 locale을 알 수 없다면 어떻게 하나요?

런타임에 locale이 추가되거나 제거될 수 있는 앱을 만드는 경우, `createNavigation`을 `locales` 인자 없이 호출할 수 있습니다. 이렇게 하면 런타임에 발견되는 모든 문자열을 유효한 locale로 허용할 수 있습니다. 이 경우 [`defineRouting`](https://next-intl.dev/docs/routing/configuration#define-routing) 함수는 사용하지 않습니다.

navigation.ts
```
    import {createNavigation} from 'next-intl/navigation';

    export const {Link, redirect, usePathname, useRouter, getPathname} =
      createNavigation({
        // ... potentially other routing
        // config, but no `locales` ...
      });
```

다만 middleware의 `locales` 인자는 여전히 필수입니다. 런타임에 사용 가능한 locale 목록을 가져와야 한다면, middleware용 routing 설정을 [요청별로 동적으로](https://next-intl.dev/docs/routing/middleware#composing-other-middlewares) 제공할 수 있습니다.

## API[](https://next-intl.dev/docs/routing/navigation#apis)

생성된 내비게이션 API는 Next.js의 대응 API를 얇게 감싼 wrapper이며, 대부분 동일한 함수 시그니처를 따릅니다. routing 설정과 사용자 locale이 자동으로 반영됩니다.

routing 설정에서 [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames)을 사용 중이라면, `href` 인자로 받을 수 있는 내부 pathname이 엄격한 타입으로 제한되고 지정된 locale에 맞게 현지화됩니다.

### `Link`[](https://next-intl.dev/docs/routing/navigation#link)

이 컴포넌트는 [`next/link`](https://nextjs.org/docs/app/api-reference/components/link)를 감싸며, 필요에 따라 pathname을 현지화합니다.
```
    import {Link} from '@/i18n/navigation';

    // When the user is on `/en`, the link will point to `/en/about`

    // Search params can be added via `query`

    // You can override the `locale` to switch to another language
    // (this will set the `hreflang` attribute on the anchor tag)
```

[`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) 사용 여부에 따라 동적 params는 다음과 같이 전달할 수 있습니다.
```
    // 1. A final string (when not using `pathnames`)

    // 2. An object (when using `pathnames`)
      Susan
```

[](https://next-intl.dev/docs/routing/navigation#link-active)내비게이션 링크를 어떻게 렌더링하나요?

Next.js의 [`useSelectedLayoutSegment` hook](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment)을 사용하면 부모 레이아웃 내부에서 특정 자식 segment가 활성 상태인지 감지할 수 있습니다. 이 값은 내부 pathname을 반환하므로, `Link`에 전달할 `href`와 매칭할 수 있습니다.

NavigationLink.tsx
```
    'use client';

    import {useSelectedLayoutSegment} from 'next/navigation';
    import {ComponentProps} from 'react';
    import {Link} from '@/i18n/navigation';

    export default function NavigationLink({
      href,
      ...rest
    }: ComponentProps<typeof Link>) {
      const selectedLayoutSegment = useSelectedLayoutSegment();
      const pathname = selectedLayoutSegment ? `/${selectedLayoutSegment}` : '/';
      const isActive = pathname === href;

      return (
      );
    }
```
```
    <nav>
    </nav>
```

[활성 링크 컴포넌트 만들기](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment#creating-an-active-link-component)에 관한 Next.js 문서도 참고하세요.

[](https://next-intl.dev/docs/routing/navigation#link-composition)`href` prop을 가진 링크를 어떻게 조합하나요?

내부적으로 `Link`에 전달되는 `href` prop을 받는 컴포넌트를 만들어야 한다면, `ComponentProps` 타입으로 `Link`의 props를 조합할 수 있습니다.

StyledLink.tsx
```
    import {ComponentProps} from 'react';
    import {Link} from '@/i18n/navigation';

    type Props = ComponentProps<typeof Link> & {
      color: 'blue' | 'red';
    };

    export default function StyledLink({color, href, ...rest}: Props) {
      return <Link href={href} style={{color}} {...rest} />;
    }
```

[`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames)을 사용 중인 경우, 래핑 컴포넌트의 `href` prop도 routing 설정 기반의 엄격한 타입이 적용됩니다.

[](https://next-intl.dev/docs/routing/navigation#link-locale)`locale` prop을 사용할 때 `<Link />`가 항상 locale prefix를 붙이는 이유는 무엇인가요?

보통 대상 페이지의 locale을 변경하기 위해 `locale` prop을 제공하면, [`localePrefix`](https://next-intl.dev/docs/routing/configuration#locale-prefix) 설정이 `always`가 아니어도 링크의 `href`에 항상 locale prefix가 포함되는 것을 볼 수 있습니다.

**예시:**

[`localePrefix: 'as-needed'`](https://next-intl.dev/docs/routing/configuration#locale-prefix-as-needed)를 사용하고 기본 locale이 `en`이라면, 아래 링크의 `href`는 여전히 `/en/about`입니다.
```
    // Links to `/en/about`
      About
```

그 이유는 사용자가 `/about` 같은 prefix 없는 라우트로 이동하기 전에 [cookie](https://next-intl.dev/docs/routing/configuration#locale-cookie)를 업데이트해야 할 수 있기 때문입니다. prefix가 붙은 pathname은 이를 처리한 뒤 prefix 없는 라우트로 리디렉션합니다. 페이지가 hydrate되기 전에 링크가 클릭될 수 있어 클라이언트 코드가 cookie를 업데이트할 기회를 갖지 못할 수 있으므로, 이 동작이 필요합니다.

이 동작을 피하고 싶다면 [`useRouter`](https://next-intl.dev/docs/routing/navigation#userouter)로 locale을 전환할 수 있습니다. 이 방식은 대상 페이지로 이동하기 전에 클라이언트에서 cookie를 업데이트하는 흐름을 활용할 수 있습니다.

[](https://next-intl.dev/docs/routing/navigation#link-unknown-routes)`pathnames` 설정 사용 시 알 수 없는 라우트에 어떻게 링크하나요?

이 경우 내비게이션 API는 엄격한 타입이 적용되어 `pathnames` 설정에 지정된 라우트만 허용합니다. 특정 위치에서 알 수 없는 라우트로 링크해야 한다면, 케이스별로 타입 체크를 비활성화할 수 있습니다.
```
    // @ts-expect-error
```

알 수 없는 라우트는 그대로 전달되지만, 절대 pathname인 경우에는 შესაბამის locale prefix가 붙습니다.

[](https://next-intl.dev/docs/routing/navigation#link-prefetching)현지화된 링크의 prefetch는 어떻게 동작하나요?

`next-intl`의 `<Link />`는 `next/link`의 기본 prefetch 동작을 상속합니다.

유일한 예외는 `locale` prop을 설정한 경우입니다. 이때는 링크를 prefetch하지 않는데, 그렇지 않으면 prefetch 요청 과정에서 [locale cookie](https://next-intl.dev/docs/routing/configuration#locale-cookie)가 너무 이르게 덮어써질 수 있기 때문입니다.

### `useRouter`[](https://next-intl.dev/docs/routing/navigation#userouter)

이벤트 핸들러처럼 프로그래밍 방식으로 이동해야 한다면, `next-intl`은 [Next.js의 `useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router)를 감싸고 pathname을 համապատասխան하게 현지화하는 편의 API를 제공합니다.
```
    'use client';

    import {useRouter} from '@/i18n/navigation';

    const router = useRouter();

    // When the user is on `/en`, the router will navigate to `/en/about`
    router.push('/about');

    // Search params can be added via `query`
    router.push({
      pathname: '/users',
      query: {sortBy: 'name'}
    });

    // You can override the `locale` to switch to another language
    router.replace('/about', {locale: 'de'});
```

[`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) 사용 여부에 따라 동적 params는 다음과 같이 전달할 수 있습니다.
```
    // 1. A final string (when not using `pathnames`)
    router.push('/users/12');

    // 2. An object (when using `pathnames`)
    router.push({
      pathname: '/users/[userId]',
      params: {userId: '5'}
    });
```

[](https://next-intl.dev/docs/routing/navigation#userouter-change-locale)현재 페이지의 locale을 어떻게 변경하나요?

[`usePathname`](https://next-intl.dev/docs/routing/navigation#usepathname)과 [`useRouter`](https://next-intl.dev/docs/routing/navigation#userouter)를 함께 사용하면, 같은 pathname으로 이동하면서 `locale`만 덮어써서 현재 페이지의 locale을 프로그래밍 방식으로 변경할 수 있습니다.

[`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) 사용 여부에 따라 내부 pathname을 해석하기 위해 `params`를 전달해야 할 수도 있습니다.
```
    'use client';

    import {usePathname, useRouter} from '@/i18n/navigation';
    import {useParams} from 'next/navigation';

    const pathname = usePathname();
    const router = useRouter();

    // Without `pathnames`: Pass the current `pathname`
    router.replace(pathname, {locale: 'de'});

    // With `pathnames`: Pass `params` as well
    const params = useParams();
    router.replace(
      // @ts-expect-error -- TypeScript will validate that only known `params`
      // are used in combination with a given `pathname`. Since the two will
      // always match for the current route, we can skip runtime checks.
      {pathname, params},
      {locale: 'de'}
    );
```

**더 알아보기:**

[ Locale switcher](https://learn.next-intl.dev/chapters/06-routing/05-locale-switcher)

### `usePathname`[](https://next-intl.dev/docs/routing/navigation#usepathname)

locale prefix가 포함될 수 있는 현재 pathname에서 prefix를 제외한 값을 가져오려면 `usePathname`을 호출하면 됩니다.
```
    'use client';

    import {usePathname} from '@/i18n/navigation';

    // When the user is on `/en`, this will be `/`
    const pathname = usePathname();
```

[`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames)을 사용 중이라면, 반환되는 pathname은 내부 pathname 템플릿에 해당합니다(동적 params는 실제 값으로 치환되지 않음).
```
    // When the user is on `/de/über-uns`, this will be `/about`
    const pathname = usePathname();

    // When the user is on `/de/neuigkeiten/produktneuheit`,
    // this will be `/news/[articleSlug]`
    const pathname = usePathname();
```

### `redirect`[](https://next-intl.dev/docs/routing/navigation#redirect)

렌더링을 중단하고 다른 페이지로 리디렉션하려면 `redirect` 함수를 호출하면 됩니다. 이 함수는 [Next.js의 `redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect)를 감싸며, 필요에 따라 pathname을 현지화합니다.

현재 [locale](https://next-intl.dev/docs/usage/configuration#use-locale)만 전달하는 경우라도 `locale` prop은 항상 필수입니다.
```
    import {redirect} from '@/i18n/navigation';

    // Redirects to `/en/login`
    redirect({href: '/login', locale: 'en'});

    // Search params can be added via `query`
    redirect({href: '/users', query: {sortBy: 'name'}, locale: 'en'});
```

[`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) 사용 여부에 따라 동적 params는 다음과 같이 전달할 수 있습니다.
```
    // 1. A final string (when not using `pathnames`)
    redirect({href: '/users/12', locale: 'en'});

    // 2. An object (when using `pathnames`)
    redirect({
      href: {
        pathname: '/users/[userId]',
        params: {userId: '5'}
      },
      locale: 'en'
    });
```

[`localePrefix`](https://next-intl.dev/docs/routing/configuration#localeprefix) 설정이 `always`가 아닌 경우, `forcePrefix` 옵션을 `true`로 설정해 locale prefix를 강제할 수 있습니다. 사용자의 locale을 변경하면서 먼저 [locale cookie](https://next-intl.dev/docs/routing/configuration#locale-cookie)를 업데이트해야 할 때 유용합니다.
```
    // Will initially redirect to `/en/about` to update the locale
    // cookie, regardless of your `localePrefix` setting
    redirect({href: '/about', locale: 'en', forcePrefix: true});
```

💡

[`permanentRedirect`](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)도 지원됩니다.

[](https://next-intl.dev/docs/routing/navigation#redirect-typescript-narrowing)`redirect` 호출 후 TypeScript가 타입을 올바르게 좁히지 못하는 이유는 무엇인가요?

TypeScript는 현재 제어 흐름 분석(control flow analysis)에 [제한](https://github.com/amannn/next-intl/issues/823#issuecomment-2421891151)이 있어, `redirect` 호출 이후 타입을 정확히 좁히거나 도달 불가능 코드를 감지하지 못할 수 있습니다.
```
    import {redirect} from '@/i18n/navigation';

    function UserProfile({userId}: {userId?: string}) {
      if (!userId) {
        redirect({href: '/login', locale: 'en'});
      }

      // `userId` should be narrowed to `string` here,
      // but TypeScript doesn't analyze this correctly
    }
```

이 제한을 우회하려면 `redirect` 함수 호출을 `return`하면 됩니다.
```
    if (!userId) {
      return redirect({href: '/login', locale: 'en'});
    }

    // ✅ `userId` is narrowed to `string` here
```

### `getPathname`[](https://next-intl.dev/docs/routing/navigation#getpathname)

locale 기반으로 특정 pathname을 구성해야 한다면 `getPathname` 함수를 호출하면 됩니다.
```
    import {getPathname} from '@/i18n/navigation';

    // Will return `/en/about`
    const pathname = getPathname({
      locale: 'en',
      href: '/about'
    });

    // Search params can be added via `query`
    const pathname = getPathname({
      locale: 'en',
      href: {
        pathname: '/users',
        query: {sortBy: 'name'}
      }
    });
```

[`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) 사용 여부에 따라 동적 params는 다음과 같이 전달할 수 있습니다.
```
    // 1. A final string (when not using `pathnames`)
    const pathname = getPathname({
      locale: 'en',
      href: '/users/12'
    });

    // 2. An object (when using `pathnames`)
    const pathname = getPathname({
      locale: 'en',
      href: {
        pathname: '/users/[userId]',
        params: {userId: '5'}
      }
    });
```

**사용 사례:**

[Sitemaps](https://learn.next-intl.dev/chapters/08-seo/04-sitemap)

[hreflang & canonicals](https://learn.next-intl.dev/chapters/08-seo/03-alternate-links)

