---
title: 'Server Actions, Metadata & Route Handlers'
description: 'There are a few places in Next.js apps where you can apply internationalization outside of React components:'
---

Source URL: https://next-intl.dev/docs/environments/actions-metadata-route-handlers

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Environments](https://next-intl.dev/docs/environments "Environments")Server Actions, Metadata & Route Handlers

# Server Actions, Metadata & Route Handlers

There are a few places in Next.js apps where you can apply internationalization outside of React components:

  1. [Metadata API](https://nextjs.org/docs/app/building-your-application/optimizing/metadata)
  2. [Server Actions](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)
  3. [Open Graph images](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
  4. [Manifest](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
  5. [Sitemap](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
  6. [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/router-handlers)

`next-intl/server` provides a set of [awaitable functions](https://next-intl.dev/docs/environments/server-client-components#async-components) that can be used in these cases.

### Metadata API[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#metadata-api)

To internationalize metadata like the page title, you can use functionality from `next-intl` in the [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#generatemetadata-function) function that can be exported from pages and layouts.

layout.tsx
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

💡

By passing an explicit `locale` to the awaitable functions from `next-intl`, you can make the metadata handler eligible for [static rendering](https://next-intl.dev/docs/routing/setup#static-rendering) if you’re using [locale-based routing](https://next-intl.dev/docs/routing).

### Server Actions[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#server-actions)

[Server Actions](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations) provide a mechanism to execute server-side code that is invoked by the client. In case you’re returning user-facing messages, you can use `next-intl` to localize them based on the user’s locale.
```
    import {getTranslations} from 'next-intl/server';

    async function loginAction(data: FormData) {
      'use server';

      const t = await getTranslations('LoginForm');
      const areCredentialsValid = /* ... */;
      if (!areCredentialsValid) {
        return {error: t('invalidCredentials')};
      }
    }
```

Note that when you’re displaying messages generated in Server Actions to the user, you should consider the case if the user can switch the locale while the message is displayed to ensure that the UI is localized consistently. If you’re using [a `[locale]` segment](https://next-intl.dev/docs/routing) as part of your routing strategy then this is handled automatically. If you’re not, you might want to clear the message manually, e.g. by [resetting the state](https://react.dev/learn/preserving-and-resetting-state#resetting-a-form-with-a-key) of the respective component via `key={locale}`.

[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#server-actions-zod)When using Zod for validation, how can I localize error messages?

[Zod](https://zod.dev/) allows you to provide [contextual error maps](https://zod.dev/ERROR_HANDLING?id=contextual-error-map) that can be used to customize error messages per parse invocation. Since the locale is specific to a particular request, this mechanism comes in handy to turn structured errors from `zod` into localized messages:
```
    import {getTranslations} from 'next-intl/server';
    import {loginUser} from '@/services/session';
    import {z} from 'zod';

    const loginFormSchema = z.object({
      email: z.string().email(),
      password: z.string().min(1)
    });

    // ...

    async function loginAction(data: FormData) {
      'use server';

      const t = await getTranslations('LoginForm');
      const values = Object.fromEntries(data);

      const result = loginFormSchema.safeParse(values, {
        error(issue) {
          if (issue.path) {
            const path = issue.path.join('.');
            return {
              email: t('invalidEmail'),
              password: t('invalidPassword')
            }[path];
          }
        }
      });

      // ...
    }
```

### Open Graph images[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#open-graph-images)

If you’re programmatically generating [Open Graph images](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), you can call functions from `next-intl` in the exported component:

app/[locale]/opengraph-image.tsx
```
    import {ImageResponse} from 'next/og';
    import {getTranslations} from 'next-intl/server';

    export default async function OpenGraphImage({params}) {
      const {locale} = await params;
      const t = await getTranslations({locale, namespace: 'OpenGraphImage'});
      return new ImageResponse(<div style={{fontSize: 128}}>{t('title')}</div>);
    }
```

Next.js will create a public route based on the segment where `opengraph-image.tsx` is placed, e.g.:
```
    http://localhost:3000/en/opengraph-image?f87b2d56cee109c7
```

However, if you’re using [locale-based routing](https://next-intl.dev/docs/routing) and you’ve customized the [`localePrefix`](https://next-intl.dev/docs/routing/configuration#locale-prefix) setting, this route might not be accessible since Next.js doesn’t know about potential rewrites of the middleware.

If this applies to your app, you can adapt your [matcher](https://next-intl.dev/docs/routing/middleware#matcher-config) to bypass requests to the `opengraph-image.tsx` file:

proxy.ts
```
    // ...

    export const config = {
      matcher: [
        // Skip all paths that should not be internationalized
        '/((?!api|_next|_vercel|.*/opengraph-image|.*\\..*).*)'

        // ...
      ]
    };
```

### Manifest[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#manifest)

Since the [manifest file](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest) needs to be placed in the root of the `app` folder (outside the `[locale]` dynamic segment), you need to provide a locale explicitly since `next-intl` can’t infer it from the pathname:

app/manifest.ts
```
    import {MetadataRoute} from 'next';
    import {getTranslations} from 'next-intl/server';

    export default async function manifest(): Promise<MetadataRoute.Manifest> {
      // Pick a locale that is representative of the app
      const locale = 'en';

      const t = await getTranslations({
        namespace: 'Manifest',
        locale
      });

      return {
        name: t('name'),
        start_url: '/',
        theme_color: '#101E33'
      };
    }
```

### Sitemap[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#sitemap)

If you’re using a sitemap to inform search engines about all pages of your site, you can attach locale-specific [alternate entries](https://developers.google.com/search/docs/specialty/international/localized-versions#sitemap) to every URL to indicate that a particular page is available in multiple languages or regions.

Note that by default, `next-intl` returns the [`link`](https://next-intl.dev/docs/routing/configuration#alternate-links) response header to instruct search engines that a page is available in multiple languages. While this sufficiently links localized pages for search engines, you may choose to provide this information in a sitemap instead if you have more specific requirements (e.g. when using CMS-driven URLs like `/news/[articleSlug]` where `articleSlug` depends on the locale).

Next.js supports providing alternate URLs per language via the [`alternates`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generate-a-localized-sitemap) entry which can be combined with [`getPathname`](https://next-intl.dev/docs/routing/navigation#getpathname) to construct URLs for each locale:
```
    import {MetadataRoute} from 'next';
    import {getPathname} from '@/i18n/navigation';

    const host = 'https://acme.com';

    export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
      return [
        {
          url: host,
          lastModified: new Date(),
          alternates: {
            languages: {
              es: host + (await getPathname({locale: 'es', href: '/'})),
              de: host + (await getPathname({locale: 'de', href: '/'}))
            }
          }
        }
      ];
    }
```

**Learn more:**

[Sitemaps](https://learn.next-intl.dev/chapters/08-seo/04-sitemap)

[CMS-driven URLs](https://learn.next-intl.dev/chapters/07-content/03-cms-driven-urls)

### Route Handlers[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#route-handlers)

You can use `next-intl` in [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/router-handlers) too. The `locale` can either be received from a search param, a layout segment or by parsing the `accept-language` header of the request.

app/api/hello/route.tsx
```
    import {NextResponse} from 'next/server';
    import {hasLocale} from 'next-intl';
    import {getTranslations} from 'next-intl/server';
    import {routing} from '@/i18n/routing';

    export async function GET(request) {
      // Example: Receive the `locale` via a search param
      const {searchParams} = new URL(request.url);
      const locale = searchParams.get('locale');
      if (!hasLocale(routing.locales, locale)) {
        return NextResponse.json({error: 'Invalid locale'}, {status: 400});
      }

      const t = await getTranslations({locale, namespace: 'Hello'});
      return NextResponse.json({title: t('title')});
    }
```

