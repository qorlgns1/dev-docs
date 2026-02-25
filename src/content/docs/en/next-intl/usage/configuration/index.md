---
title: 'Request configuration'
description: 'Configuration properties that you use across your Next.js app can be set per request.'
---

Source URL: https://next-intl.dev/docs/usage/configuration

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Usage guide](https://next-intl.dev/docs/usage "Usage guide")Request configuration

# Request configuration

Configuration properties that you use across your Next.js app can be set per request.

## Server & Client Components[](https://next-intl.dev/docs/usage/configuration#server-client-components)

Depending on if you handle internationalization in [Server- or Client Components](https://next-intl.dev/docs/environments/server-client-components), the configuration from `i18n/request.ts` or `NextIntlClientProvider` will be applied respectively.

### `i18n/request.ts` & `getRequestConfig`[](https://next-intl.dev/docs/usage/configuration#i18n-request)

`i18n/request.ts` can be used to provide configuration for **server-only** code, i.e. Server Components, Server Actions & friends. The configuration is provided via the `getRequestConfig` function and provides a `requestLocale` parameter in case you’re using [locale-based routing](https://next-intl.dev/docs/routing).

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';
    import {routing} from '@/i18n/routing';

    export default getRequestConfig(async ({requestLocale}) => {
      // ...

      return {
        locale,
        messages
        // ...
      };
    });
```

The configuration object is created once for each request by internally using React’s [`cache`](https://react.dev/reference/react/cache). The first component to use internationalization will call the function defined with `getRequestConfig`.

Since this function is executed during the Server Components render pass, you can call functions like [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies) and [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers) to return configuration that is request-specific.

### `NextIntlClientProvider`[](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider)

`NextIntlClientProvider` can be used to provide configuration for **Client Components**.

layout.tsx
```
    import {NextIntlClientProvider} from 'next-intl';
    import {getMessages} from 'next-intl/server';

    export default async function RootLayout(/* ... */) {
      // ...

      return (
        <html lang={locale}>
          <body>
          </body>
        </html>
      );
    }
```

These props are inherited if you’re rendering `NextIntlClientProvider` from a Server Component:

  1. `locale`
  2. `messages`
  3. `now`
  4. `timeZone`
  5. `formats`

If you don’t want to inherit some of these props, e.g. because you’re selective about how you use internationalization in [Server & Client Components](https://next-intl.dev/docs/environments/server-client-components), you can opt-out:

layout.tsx
```
      ...
```

Additionally, nested instances of `NextIntlClientProvider` will inherit configuration from their respective ancestors. Note however that individual props are treated as atomic, therefore e.g. `messages` need to be merged manually—if necessary.

In contrast, these props are not inherited:

  1. `onError`
  2. `getMessageFallback`

[](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider-non-serializable-props)How can I provide non-serializable props like `onError` to `NextIntlClientProvider`?

React limits the types of props that can be passed to Client Components to the ones that are [serializable](https://react.dev/reference/rsc/use-client#serializable-types). Since `onError` and `getMessageFallback` can receive functions, these configuration options can’t be automatically inherited by the client side.

In order to define these values on the client side, you can add a provider that defines these props:

IntlErrorHandlingProvider.tsx
```
    'use client';

    import {NextIntlClientProvider} from 'next-intl';

    export default function IntlErrorHandlingProvider({children}) {
      return (
          {children}
      );
    }
```

Once you have defined your client-side provider component, you can use it in a Server Component:

layout.tsx
```
    import {NextIntlClientProvider} from 'next-intl';
    import {getLocale} from 'next-intl/server';
    import IntlErrorHandlingProvider from './IntlErrorHandlingProvider';

    export default async function RootLayout({children}) {
      const locale = await getLocale();

      return (
        <html lang={locale}>
          <body>
          </body>
        </html>
      );
    }
```

By doing this, your provider component will already be part of the client-side bundle and can therefore define and pass functions as props.

Note that the inner `NextIntlClientProvider` inherits the configuration from the outer one, only the `onError` and `getMessageFallback` functions are added.

## Locale[](https://next-intl.dev/docs/usage/configuration#locale)

The `locale` represents an identifier that contains the language and formatting preferences of users, optionally including regional information (e.g. `en-US`). Locales are specified as [IETF BCP 47 language tags](https://en.wikipedia.org/wiki/IETF_language_tag).

i18n/request.tsProvider

Depending on if you’re using [locale-based routing](https://next-intl.dev/docs/routing), you can read the locale from the `requestLocale` parameter or provide a value on your own:

**With locale-based routing:**

i18n/request.ts
```
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

**Without locale-based routing:**

i18n/request.ts
```
    export default getRequestConfig(async () => {
      // Provide a static locale, fetch a user setting,
      // read from `cookies()`, `headers()`, etc.
      const locale = 'en';

      return {
        locale
        // ...
      };
    });
```

[](https://next-intl.dev/docs/usage/configuration#server-request-locale)Which values can the `requestLocale` parameter hold?

While the `requestLocale` parameter typically corresponds to the `[locale]` segment that was matched by the middleware, there are three special cases to consider:

  1. **Overrides** : When an explicit `locale` is passed to [awaitable functions](https://next-intl.dev/docs/environments/actions-metadata-route-handlers) like `getTranslations({locale: 'en'})`, then this value will be used instead of the segment.
  2. **`undefined`** : The value can be `undefined` when a page outside of the `[locale]` segment renders (e.g. a language selection page at `app/page.tsx`).
  3. **Invalid values** : Since the `[locale]` segment effectively acts like a catch-all for unknown routes (e.g. `/unknown.txt`), invalid values should be replaced with a valid locale. In addition to this, you might want to call `notFound()` in the [root layout](https://next-intl.dev/docs/routing/setup#layout) to abort the render in this case.

```
```

[](https://next-intl.dev/docs/usage/configuration#locale-change)How can I change the locale?

Depending on if you’re using [locale-based routing](https://next-intl.dev/docs/routing), the locale can be changed as follows:

  1. **With locale-based routing** : The locale is managed by the router and can be changed by using navigation APIs from `next-intl` like [`Link`](https://next-intl.dev/docs/routing/navigation#link) or [`useRouter`](https://next-intl.dev/docs/routing/navigation#userouter).
  2. **Without locale-based routing** : You can change the locale by updating the value where the locale is read from (e.g. a cookie, a user setting, etc.).

Learn more:

[Locale switcher](https://learn.next-intl.dev/chapters/04-adding-locales/02-locale-switcher)

### `useLocale` & `getLocale`[](https://next-intl.dev/docs/usage/configuration#use-locale)

The current locale of your app is automatically incorporated into hooks like `useTranslations` & `useFormatter` and will affect the rendered output.

In case you need to use this value in other places of your app, e.g. to implement a locale switcher or to pass it to API calls, you can read it via `useLocale` or `getLocale`:
```
    // Regular components
    import {useLocale} from 'next-intl';
    const locale = useLocale();

    // Async Server Components
    import {getLocale} from 'next-intl/server';
    const locale = await getLocale();
```

[](https://next-intl.dev/docs/usage/configuration#locale-return-value)Which value is returned from `useLocale`?

Depending on how a component renders, the returned locale corresponds to:

  1. **Server Components** : The locale represents the value returned in [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#i18n-request).
  2. **Client Components** : The locale is received from [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider).

Note that `NextIntlClientProvider` automatically inherits the locale if it is rendered by a Server Component, therefore you rarely need to pass a locale to `NextIntlClientProvider` yourself.

[](https://next-intl.dev/docs/usage/configuration#locale-pages-router)I’m using the Pages Router, how can I access the locale?

If you use [internationalized routing with the Pages Router](https://nextjs.org/docs/pages/building-your-application/routing/internationalization), you can receive the locale from the router in order to pass it to `NextIntlClientProvider`:

_app.tsx
```
    import {useRouter} from 'next/router';

    // ...

    const router = useRouter();

    return (
        ...
      </NextIntlClientProvider>;
    );
```

### `Locale` type[](https://next-intl.dev/docs/usage/configuration#locale-type)

When passing a `locale` to another function, you can use the `Locale` type for the receiving parameter:
```
    import {Locale} from 'next-intl';

    async function getPosts(locale: Locale) {
      // ...
    }
```

This can be helpful when integrating with backend services or a CMS:

[Backend content](https://learn.next-intl.dev/chapters/07-content/01-overview)

💡

By default, `Locale` is typed as `string`. However, you can optionally provide a strict union based on your supported locales for this type by [augmenting the `Locale` type](https://next-intl.dev/docs/workflows/typescript#locale).

## Messages[](https://next-intl.dev/docs/usage/configuration#messages)

The most crucial aspect of internationalization is providing labels based on the user’s language. The recommended workflow is to store your messages in your repository along with the code.
```
    ├── messages
    │   ├── en.json
    │   ├── de-AT.json
    │   └── ...
    ...
```

Colocating your messages with app code is beneficial because it allows developers to make changes quickly and additionally, you can use the shape of your local messages for [type checking](https://next-intl.dev/docs/workflows/typescript#messages).

If your team ships frequently, you can consider automating the translation process:

[AI translations with Crowdin](https://learn.next-intl.dev/chapters/10-continuous-localization/01-local-workflow)

That being said, `next-intl` is agnostic to how you store messages and allows you to freely define an async function that fetches them while your app renders:

i18n/request.tsProvider

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';

    export default getRequestConfig(async () => {
      return {
        messages: (await import(`../../messages/${locale}.json`)).default
        // ...
      };
    });
```

After messages are configured, they can be used via [`useTranslations`](https://next-intl.dev/docs/usage/translations#rendering-messages-with-usetranslations).

Since `getRequestConfig` can execute arbitrary code, you can also:

  * Share messages across multiple locales
  * Merge messages from another locale as fallbacks
  * Load messages from a remote source

**Learn more:**

[ Providing messages](https://learn.next-intl.dev/chapters/04-adding-locales/01-messages)

[](https://next-intl.dev/docs/usage/configuration#messages-split-files)How can I split my messages into multiple files?

Since messages can be freely defined and loaded, you can split them into multiple files and merge them later at runtime if you prefer:
```
    const messages = {
      ...(await import(`../../messages/${locale}/login.json`)).default,
      ...(await import(`../../messages/${locale}/dashboard.json`)).default
    };
```

Note that the [VSCode integration](https://next-intl.dev/docs/workflows/vscode-integration) for `next-intl` can help you manage messages within a single, large file. If you’re splitting messages purely for organizational reasons, you might want to consider using this instead.

### `useMessages` & `getMessages`

In case you require access to messages in a component, you can read them via `useMessages()` or `getMessages()` from your configuration:
```
    // Regular components
    import {useMessages} from 'next-intl';
    const messages = useMessages();

    // Async Server Components
    import {getMessages} from 'next-intl/server';
    const messages = await getMessages();
```
```
    import {NextIntlClientProvider} from 'next-intl';
    import {getMessages} from 'next-intl/server';
    import pick from 'lodash/pick';

    async function Component({children}) {
      // Read messages configured via `i18n/request.ts`
      const messages = await getMessages();

      return (
          ...
      );
    }
```

## Time zone[](https://next-intl.dev/docs/usage/configuration#time-zone)

Specifying a time zone affects the rendering of dates and times. By default, the time zone of the server runtime will be used, but can be customized as necessary.

i18n/request.tsProvider

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';

    export default getRequestConfig(async () => {
      return {
        // The time zone can either be statically defined, read from the
        // user profile if you store such a setting, or based on dynamic
        // request information like the locale or a cookie.
        timeZone: 'Europe/Vienna'

        // ...
      };
    });
```
```
    // The time zone can either be statically defined, read from the
    // user profile if you store such a setting, or based on dynamic
    // request information like the locale or a cookie.
    const timeZone = 'Europe/Vienna';

```

The available time zone names can be looked up in the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

The time zone in Client Components is automatically inherited from the server side if you wrap the relevant components in a `NextIntlClientProvider` that is rendered by a Server Component. For all other cases, you can specify the value explicitly on a wrapping `NextIntlClientProvider`.

**Learn more:**

[Dates & time zones](https://learn.next-intl.dev/chapters/05-formatting/02-dates-timezones)

### `useTimeZone` & `getTimeZone`[](https://next-intl.dev/docs/usage/configuration#use-time-zone)

The configured time zone can be read via `useTimeZone` or `getTimeZone` in components:
```
    // Regular components
    import {useTimeZone} from 'next-intl';
    const timeZone = useTimeZone();

    // Async Server Components
    import {getTimeZone} from 'next-intl/server';
    const timeZone = await getTimeZone();
```

## Now value[](https://next-intl.dev/docs/usage/configuration#now)

When formatting [relative dates and times](https://next-intl.dev/docs/usage/dates-times#relative-times), `next-intl` will format times in relation to a reference point in time that is referred to as “now”. While it can be beneficial in terms of caching to [provide this value](https://next-intl.dev/docs/usage/dates-times#relative-times-usenow) where necessary, you can provide a global value for `now`, e.g. to ensure consistency when running tests.

i18n/request.tsProvider

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';

    export default getRequestConfig(async () => {
      return {
        now: new Date('2024-11-14T10:36:01.516Z')

        // ...
      };
    });
```
```
    const now = new Date('2024-11-14T10:36:01.516Z');

      ...
```

Once you have `formats` set up, you can use them in your components via `useFormatter`:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();

      format.dateTime(new Date('2020-11-20T10:36:01.516Z'), 'short');
      format.number(47.414329182, 'precise');
      format.list(['HTML', 'CSS', 'JavaScript'], 'enumeration');
    }
```

💡

By default, format names are loosely typed as `string`. However, you can optionally use strict types by [augmenting the `Formats` type](https://next-intl.dev/docs/workflows/typescript#formats).

Global formats for numbers, dates and times can be referenced in messages too:

en.json
```
    {
      "ordered": "You've ordered this product on {orderDate, date, short}",
      "latitude": "Latitude: {latitude, number, precise}"
    }
```
```
    import {useTranslations} from 'next-intl';

    function Component() {
      const t = useTranslations();

      t('ordered', {orderDate: new Date('2020-11-20T10:36:01.516Z')});
      t('latitude', {latitude: 47.414329182});
    }
```

Formats are automatically inherited from the server side if you wrap the relevant components in a `NextIntlClientProvider` that is rendered by a Server Component.

## Error handling (`onError` & `getMessageFallback`)[](https://next-intl.dev/docs/usage/configuration#error-handling)

By default, when a message fails to resolve or when the formatting failed, an error will be printed on the console. In this case `${namespace}.${key}` will be rendered instead to keep your app running.

This behavior can be customized with the `onError` and `getMessageFallback` configuration option.

i18n/request.tsProvider

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';
    import {IntlErrorCode} from 'next-intl';

    export default getRequestConfig(async () => {
      return {
        onError(error) {
          if (error.code === IntlErrorCode.MISSING_MESSAGE) {
            // Missing translations are expected and should only log an error
            console.error(error);
          } else {
            // Other errors indicate a bug in the app and should be reported
            reportToErrorTracking(error);
          }
        },

        getMessageFallback({namespace, key, error}) {
          const path = [namespace, key].filter((part) => part != null).join('.');

          if (error.code === IntlErrorCode.MISSING_MESSAGE) {
            return path + ' is not yet translated';
          } else {
            return 'Dear developer, please fix this message: ' + path;
          }
        }

        // ...
      };
    });
```

Note that `onError` and `getMessageFallback` are not automatically inherited by Client Components. If you want to make this functionality available in Client Components too, you can however create a [client-side provider](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider-non-serializable-props) that defines these props.

[](https://next-intl.dev/docs/usage/configuration#error-handling-fallback)How can I use messages from another locale as a fallback?

The `getMessageFallback` setting is intended to customize the error case for apps which want to treat missing messages as errors.

If you expect missing messages for certain locales, you can consider merging messages e.g. from the default locale with the ones for the current locale when providing [messages](https://next-intl.dev/docs/usage/configuration#messages).

**Learn more:**

[ Providing messages](https://learn.next-intl.dev/chapters/04-adding-locales/01-messages)
```
    import {NextIntlClientProvider, IntlErrorCode} from 'next-intl';

    function onError(error) {
      if (error.code === IntlErrorCode.MISSING_MESSAGE) {
        // Missing translations are expected and should only log an error
        console.error(error);
      } else {
        // Other errors indicate a bug in the app and should be reported
        reportToErrorTracking(error);
      }
    }

    function getMessageFallback({namespace, key, error}) {
      const path = [namespace, key].filter((part) => part != null).join('.');

      if (error.code === IntlErrorCode.MISSING_MESSAGE) {
        return path + ' is not yet translated';
      } else {
        return 'Dear developer, please fix this message: ' + path;
      }
    }

      ...
    </NextIntlClientProvider>;
```

