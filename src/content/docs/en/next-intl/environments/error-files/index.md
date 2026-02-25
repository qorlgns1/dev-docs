---
title: 'Internationalization in Next.js error files'
description: 'The Next.js App Router’s file convention provides two files that can be used for error handling:'
---

Source URL: https://next-intl.dev/docs/environments/error-files

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Environments](https://next-intl.dev/docs/environments "Environments")Error files (e.g. not-found)

# Internationalization in Next.js error files

The Next.js App Router’s file convention provides two files that can be used for error handling:

  1. [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)
  2. [`error.js`](https://nextjs.org/docs/app/api-reference/file-conventions/error)

This page provides practical guides for these cases.

**Tip:** You can have a look at the [App Router example](https://next-intl.dev/examples#app-router) to explore a working app with error handling.

## `not-found.js`[](https://next-intl.dev/docs/environments/error-files#not-foundjs)

💡

This section is only relevant if you’re using [locale-based routing](https://next-intl.dev/docs/routing).

Next.js renders the closest `not-found` page when a route segment calls the [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) function. We can use this mechanism to provide a localized 404 page by adding a `not-found` file within the `[locale]` folder.

app/[locale]/not-found.tsx
```
    import {useTranslations} from 'next-intl';

    export default function NotFoundPage() {
      const t = useTranslations('NotFoundPage');
      return <h1>{t('title')}</h1>;
    }
```

Note however that Next.js will only render this page when the `notFound` function is called from within a route, not for all unknown routes in general.

### Catching unknown routes[](https://next-intl.dev/docs/environments/error-files#catching-unknown-routes)

To catch unknown routes too, you can define a catch-all route that explicitly calls the `notFound` function.

app/[locale]/[...rest]/page.tsx
```
    import {notFound} from 'next/navigation';

    export default function CatchAllPage() {
      notFound();
    }
```

After this change, all requests that are matched within the `[locale]` segment will render the `not-found` page when an unknown route is encountered (e.g. `/en/unknown`).

### Catching non-localized requests[](https://next-intl.dev/docs/environments/error-files#catching-non-localized-requests)

When the user requests a route that is not matched by the `next-intl` [middleware](https://next-intl.dev/docs/routing/middleware), there’s no locale associated with the request (depending on your [`matcher` config](https://next-intl.dev/docs/routing/middleware#matcher-config), e.g. `/unknown.txt` might not be matched).

You can add a root `not-found` page to handle these cases too.

app/not-found.tsx
```
    'use client';

    import Error from 'next/error';

    export default function NotFound() {
      return (
        <html lang="en">
          <body>
          </body>
        </html>
      );
    }
```

Note that the presence of `app/not-found.tsx` requires that a root layout is available, even if it’s just passing `children` through.

app/layout.tsx
```
    // Since we have a root `not-found.tsx` page, a layout file
    // is required, even if it's just passing children through.
    export default function RootLayout({children}) {
      return children;
    }
```

For the 404 page to render, we need to call the `notFound` function in the root layout when we detect an incoming `locale` param that isn’t valid.

app/[locale]/layout.tsx
```
    import {hasLocale} from 'next-intl';
    import {notFound} from 'next/navigation';
    import {routing} from '@/i18n/routing';

    export default function LocaleLayout({children, params}) {
      const {locale} = await params;
      if (!hasLocale(routing.locales, locale)) {
        notFound();
      }

      // ...
    }
```

## `error.js`[](https://next-intl.dev/docs/environments/error-files#errorjs)

When an `error` file is defined, Next.js creates an [error boundary](https://nextjs.org/docs/app/building-your-application/routing/error-handling#how-errorjs-works) within your layout that wraps pages accordingly to catch runtime errors:
```
```

Schematic component hierarchy that Next.js creates internally.

Since the `error` file must be defined as a Client Component, you have to use [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider) to provide messages in case it renders:

layout.tsx
```
    import pick from 'lodash/pick';
    import {NextIntlClientProvider} from 'next-intl';
    import {getMessages} from 'next-intl/server';

    export default async function RootLayout(/* ... */) {
      const messages = await getMessages();

      return (
        <html lang={locale}>
          <body>
              {children}
          </body>
        </html>
      );
    }
```

Once `NextIntlClientProvider` is in place, you can use functionality from `next-intl` in the `error` file:

error.tsx
```
    'use client';

    import {useTranslations} from 'next-intl';

    export default function Error({error, reset}) {
      const t = useTranslations('Error');

      return (
          <h1>{t('title')}</h1>
          <button onClick={reset}>{t('retry')}</button>
      );
    }
```

Note that `error.tsx` is loaded right after your app has initialized. If your app is performance-sensitive and you want to avoid loading translation functionality from `next-intl` as part of this bundle, you can export a lazy reference from your `error` file:

error.tsx
```
    'use client';

    import {lazy} from 'react';

    // Move error content to a separate chunk and load it only when needed
    export default lazy(() => import('./Error'));
```

