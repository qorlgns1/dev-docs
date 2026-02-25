---
title: 'Next.js Pages Router internationalization (i18n)'
description: 'DocsGetting startedPages Router'
---

Source URL: https://next-intl.dev/docs/getting-started/pages-router

Docs[Getting started](https://next-intl.dev/docs/getting-started "Getting started")Pages Router

# Next.js Pages Router internationalization (i18n)

While it’s recommended to [use `next-intl` with the App Router](https://next-intl.dev/docs/getting-started/app-router), the Pages Router is still fully supported.

Multiple languagesSingle language

  1. `npm install next-intl`
  2. Set up [internationalized routing](https://nextjs.org/docs/advanced-features/i18n-routing)
  3. Add the provider in `_app.tsx`

_app.tsx
```
    import {NextIntlClientProvider} from 'next-intl';
    import {useRouter} from 'next/router';

    export default function App({Component, pageProps}) {
      const router = useRouter();

      return (
      );
    }
```

  4. Provide messages on a page-level

pages/index.tsx
```
    export async function getStaticProps(context) {
      return {
        props: {
          // You can get the messages from anywhere you like. The recommended
          // pattern is to put them in JSON files separated by locale and read
          // the desired one based on the `locale` received from Next.js.
          messages: (await import(`../../messages/${context.locale}.json`)).default
        }
      };
    }
```

  5. Use translations in your components!

Even if you only support a single language, `next-intl` can still be helpful to separate your labels and formatting concerns from your application logic.

  1. `npm install next-intl`

  2. Add the provider in `_app.tsx`

_app.tsx
```
    import {NextIntlClientProvider} from 'next-intl';

    export default function App({Component, pageProps}) {
      return (
      );
    }
```

  3. Provide messages on a page-level

pages/index.tsx
```
    export async function getStaticProps() {
      const locale = 'en';

      return {
        props: {
          // You can get the messages from anywhere you like. The recommended pattern
          // is to put them in JSON files separated by locale (e.g. `en.json`).
          messages: (await import(`../../messages/${locale}.json`)).default
        }
      };
    }
```

  4. Use translations in your components!

💡

**Next steps:**

  * Exploring `next-intl`? Check out the [usage guide](https://next-intl.dev/docs/usage).
  * Ran into an issue? Have a look at the [Pages Router example](https://next-intl.dev/examples#pages-router) to explore a working app.

  * Are you transitioning from the Pages to the App Router? Check out [the migration example](https://next-intl.dev/examples#app-router-migration).

