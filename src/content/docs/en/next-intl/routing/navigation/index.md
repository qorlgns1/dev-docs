---
title: 'Navigation APIs'
description: 'Prefer to watch a video?'
---

Source URL: https://next-intl.dev/docs/routing/navigation

# Navigation APIs

Prefer to watch a video?

[Navigation APIs](https://learn.next-intl.dev/chapters/06-routing/04-navigation-apis)

`next-intl` provides lightweight wrappers around Next.js’ navigation APIs like [`<Link />`](https://nextjs.org/docs/app/api-reference/components/link) and [`useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router) that automatically handle the user locale and pathnames behind the scenes.

To create these APIs, you can call the `createNavigation` function with your `routing` configuration:

navigation.ts
```
    import {createNavigation} from 'next-intl/navigation';
    import {routing} from './routing';

    export const {Link, redirect, usePathname, useRouter, getPathname} =
      createNavigation(routing);
```

This function is typically called in a central module like [`src/i18n/navigation.ts`](https://next-intl.dev/docs/routing/setup#i18n-navigation) in order to provide easy access to navigation APIs in your components.

[](https://next-intl.dev/docs/routing/navigation#locales-unknown)What if the locales aren’t known at build time?

In case you’re building an app where locales can be added and removed at runtime, `createNavigation` can be called without the `locales` argument, therefore allowing any string that is encountered at runtime to be a valid locale. In this case, you’d not use the [`defineRouting`](https://next-intl.dev/docs/routing/configuration#define-routing) function.

navigation.ts
```
    import {createNavigation} from 'next-intl/navigation';

    export const {Link, redirect, usePathname, useRouter, getPathname} =
      createNavigation({
        // ... potentially other routing
        // config, but no `locales` ...
      });
```

Note however that the `locales` argument for the middleware is still mandatory. If you need to fetch the available locales at runtime, you can provide the routing configuration for the middleware [dynamically per request](https://next-intl.dev/docs/routing/middleware#composing-other-middlewares).

## APIs[](https://next-intl.dev/docs/routing/navigation#apis)

The created navigation APIs are thin wrappers around the equivalents from Next.js and mostly adhere to the same function signatures. Your routing configuration and the user’s locale are automatically incorporated.

If you’re using the [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) setting in your routing configuration, the internal pathnames that are accepted for `href` arguments will be strictly typed and localized to the given locale.

### `Link`[](https://next-intl.dev/docs/routing/navigation#link)

This component wraps [`next/link`](https://nextjs.org/docs/app/api-reference/components/link) and localizes the pathname as necessary.
```
    import {Link} from '@/i18n/navigation';

    // When the user is on `/en`, the link will point to `/en/about`

    // Search params can be added via `query`

    // You can override the `locale` to switch to another language
    // (this will set the `hreflang` attribute on the anchor tag)
```

Depending on if you’re using the [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) setting, dynamic params can either be passed as:
```
    // 1. A final string (when not using `pathnames`)

    // 2. An object (when using `pathnames`)
      Susan
```

[](https://next-intl.dev/docs/routing/navigation#link-active)How can I render a navigation link?

The [`useSelectedLayoutSegment` hook](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment) from Next.js allows you to detect if a given child segment is active from within the parent layout. Since this returns an internal pathname, it can be matched against an `href` that you can pass to `Link`.

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

See also the Next.js docs on [creating an active link component](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment#creating-an-active-link-component).

[](https://next-intl.dev/docs/routing/navigation#link-composition)How can I compose the link with its href prop?

If you need to create a component that receives an `href` prop that is forwarded to `Link` internally, you can compose the props from `Link` with the `ComponentProps` type:

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

In case you’re using the [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) setting, the `href` prop of the wrapping component will now be strictly typed based on your routing configuration.

[](https://next-intl.dev/docs/routing/navigation#link-locale)Why does `<Link />` always set a locale prefix when using the `locale` prop?

If you’re providing a `locale` prop, typically to change the locale of the target page, you might notice that the link’s `href` will always include a locale prefix, even if you’re using a [`localePrefix`](https://next-intl.dev/docs/routing/configuration#locale-prefix) setting other than `always`.

**Example:**

If you’re using [`localePrefix: 'as-needed'`](https://next-intl.dev/docs/routing/configuration#locale-prefix-as-needed) and `en` is your default locale, then the `href` for this link will still be `/en/about`:
```
    // Links to `/en/about`
      About
```

The reason for this is that a potential [cookie](https://next-intl.dev/docs/routing/configuration#locale-cookie) may need to be updated before the user can visit the unprefixed route at `/about`. The prefixed pathname will take care of this and will subsequently redirect to the unprefixed route. This behavior is necessary because links might be interacted with before your page is hydrated and client-side code would have a chance to update the cookie.

If you’d like to avoid this behavior, you can instead use [`useRouter`](https://next-intl.dev/docs/routing/navigation#userouter) to switch the locale, which can rely on updating the cookie on the client side before navigating to the target page.

[](https://next-intl.dev/docs/routing/navigation#link-unknown-routes)How can I link to unknown routes when using the `pathnames` setting?

In this case, the navigation APIs are strictly typed and only allow routes specified in the `pathnames` config. If you need to link to unknown routes in certain places, you can disable the type checking on a case-by-case basis:
```
    // @ts-expect-error
```

Unknown routes will be passed through as-is, but will receive relevant locale prefixes in case of absolute pathnames.

[](https://next-intl.dev/docs/routing/navigation#link-prefetching)How does prefetching of localized links work?

`<Link />` from `next-intl` inherits the default prefetch behavior from `next/link`.

The one exception to this is when you’ve set the `locale` prop. In this case, the link will not be prefetched, because this would otherwise result in prematurely overwriting the [locale cookie](https://next-intl.dev/docs/routing/configuration#locale-cookie) as part of the prefetch request.

### `useRouter`[](https://next-intl.dev/docs/routing/navigation#userouter)

If you need to navigate programmatically, e.g. in an event handler, `next-intl` provides a convience API that wraps [`useRouter` from Next.js](https://nextjs.org/docs/app/api-reference/functions/use-router) and localizes the pathname accordingly.
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

Depending on if you’re using the [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) setting, dynamic params can either be passed as:
```
    // 1. A final string (when not using `pathnames`)
    router.push('/users/12');

    // 2. An object (when using `pathnames`)
    router.push({
      pathname: '/users/[userId]',
      params: {userId: '5'}
    });
```

[](https://next-intl.dev/docs/routing/navigation#userouter-change-locale)How can I change the locale for the current page?

By combining [`usePathname`](https://next-intl.dev/docs/routing/navigation#usepathname) with [`useRouter`](https://next-intl.dev/docs/routing/navigation#userouter), you can change the locale for the current page programmatically by navigating to the same pathname, while overriding the `locale`.

Depending on if you’re using the [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) setting, you optionally have to forward `params` to potentially resolve an internal pathname.
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

**Learn more:**

[ Locale switcher](https://learn.next-intl.dev/chapters/06-routing/05-locale-switcher)

### `usePathname`[](https://next-intl.dev/docs/routing/navigation#usepathname)

To retrieve the current pathname without a potential locale prefix, you can call `usePathname`.
```
    'use client';

    import {usePathname} from '@/i18n/navigation';

    // When the user is on `/en`, this will be `/`
    const pathname = usePathname();
```

Note that if you’re using the [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) setting, the returned pathname will correspond to an internal pathname template (dynamic params will not be replaced by their values).
```
    // When the user is on `/de/über-uns`, this will be `/about`
    const pathname = usePathname();

    // When the user is on `/de/neuigkeiten/produktneuheit`,
    // this will be `/news/[articleSlug]`
    const pathname = usePathname();
```

### `redirect`[](https://next-intl.dev/docs/routing/navigation#redirect)

If you want to interrupt the render and redirect to another page, you can invoke the `redirect` function. This wraps [`redirect` from Next.js](https://nextjs.org/docs/app/api-reference/functions/redirect) and localizes the pathname as necessary.

Note that a `locale` prop is always required, even if you’re just passing the [current locale](https://next-intl.dev/docs/usage/configuration#use-locale).
```
    import {redirect} from '@/i18n/navigation';

    // Redirects to `/en/login`
    redirect({href: '/login', locale: 'en'});

    // Search params can be added via `query`
    redirect({href: '/users', query: {sortBy: 'name'}, locale: 'en'});
```

Depending on if you’re using the [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) setting, dynamic params can either be passed as:
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

When using a [`localePrefix`](https://next-intl.dev/docs/routing/configuration#localeprefix) setting other than `always`, you can enforce a locale prefix by setting the `forcePrefix` option to `true`. This is useful when changing the user’s locale and you need to update the [locale cookie](https://next-intl.dev/docs/routing/configuration#locale-cookie) first:
```
    // Will initially redirect to `/en/about` to update the locale
    // cookie, regardless of your `localePrefix` setting
    redirect({href: '/about', locale: 'en', forcePrefix: true});
```

💡

[`permanentRedirect`](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect) is supported too.

[](https://next-intl.dev/docs/routing/navigation#redirect-typescript-narrowing)Why does TypeScript not narrow types correctly after calling `redirect`?

TypeScript currently has a [limitation](https://github.com/amannn/next-intl/issues/823#issuecomment-2421891151) with control flow analysis, which results in not being able to narrow types correctly after calling `redirect` as well as detecting unreachable code:
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

To work around this limitation, you can return the call to the `redirect` function:
```
    if (!userId) {
      return redirect({href: '/login', locale: 'en'});
    }

    // ✅ `userId` is narrowed to `string` here
```

### `getPathname`[](https://next-intl.dev/docs/routing/navigation#getpathname)

If you need to construct a particular pathname based on a locale, you can call the `getPathname` function.
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

Depending on if you’re using the [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) setting, dynamic params can either be passed as:
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

**Use cases:**

[Sitemaps](https://learn.next-intl.dev/chapters/08-seo/04-sitemap)

[hreflang & canonicals](https://learn.next-intl.dev/chapters/08-seo/03-alternate-links)

