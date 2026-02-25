---
title: 'Internationalization of Server & Client Components'
description: 'This applies to handling internationalization too.'
---

Source URL: https://next-intl.dev/docs/environments/server-client-components

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Environments](https://next-intl.dev/docs/environments "Environments")Server & Client Components

# Internationalization of Server & Client Components

[React Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components) allow you to implement components that remain server-side only if they don’t require React’s interactive features, such as `useState` and `useEffect`.

This applies to handling internationalization too.

page.tsx
```
    import {useTranslations} from 'next-intl';

    // Since this component doesn't use any interactive features
    // from React, it can be run as a Server Component.

    export default function HomePage() {
      const t = useTranslations('HomePage');
      return <h1>{t('title')}</h1>;
    }
```

Moving internationalization to the server side unlocks new levels of performance, leaving the client side for interactive features.

**Benefits of server-side internationalization:**

  1. Your messages never leave the server and don’t need to be passed to the client side
  2. Library code for internationalization doesn’t need to be loaded on the client side
  3. No need to split your messages, e.g. based on routes or components
  4. No runtime cost on the client side

## Using internationalization in Server Components[](https://next-intl.dev/docs/environments/server-client-components#using-internationalization-in-server-components)

Server Components can be declared in two ways:

  1. Async components
  2. Non-async, regular components

In a typical app, you’ll likely find both types of components. `next-intl` provides corresponding APIs that work for the given component type.

### Async components[](https://next-intl.dev/docs/environments/server-client-components#async-components)

These are primarly concerned with fetching data and [can not use hooks](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md#capabilities--constraints-of-server-and-client-components). Due to this, `next-intl` provides a set of awaitable versions of the functions that you usually call as hooks from within components.

page.tsx
```
    import {getTranslations} from 'next-intl/server';

    export default async function ProfilePage() {
      const user = await fetchUser();
      const t = await getTranslations('ProfilePage');

      return (
      );
    }
```

These functions are available:

  * `getTranslations`
  * `getFormatter`
  * `getNow`
  * `getTimeZone`
  * `getMessages`
  * `getLocale`

### Non-async components[](https://next-intl.dev/docs/environments/server-client-components#shared-components)

Components that aren’t declared with the `async` keyword and don’t use interactive features like `useState`, are referred to as [shared components](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md#sharing-code-between-server-and-client). These can render either as a Server or Client Component, depending on where they are imported from.

In Next.js, Server Components are the default, and therefore shared components will typically execute as Server Components:

UserDetails.tsx
```
    import {useTranslations} from 'next-intl';

    export default function UserDetails({user}) {
      const t = useTranslations('UserProfile');

      // This component will execute as a Server Component by default.
      // However, if it is imported from a Client Component, it will
      // execute as a Client Component.
      return (
          <h2>{t('title')}</h2>
          <p>{t('followers', {count: user.numFollowers})}</p>
      );
    }
```

If you import `useTranslations`, `useFormatter`, `useLocale`, `useNow` and `useTimeZone` from a shared component, `next-intl` will automatically provide an implementation that works best for the environment this component executes in (server or client).

[](https://next-intl.dev/docs/environments/server-client-components#rsc-background)How does the Server Components integration work?

`next-intl` uses [`react-server` conditional exports](https://github.com/reactjs/rfcs/blob/main/text/0227-server-module-conventions.md#react-server-conditional-exports) to load code that is optimized for the usage in Server or Client Components. While configuration for hooks like `useTranslations` is read via `useContext` on the client side, on the server side it is loaded via [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#i18n-request).

Hooks are currently primarly known for being used in Client Components since they are typically stateful or don’t apply to a server environment. However, hooks like [`useId`](https://react.dev/reference/react/useId) can be used in Server Components too. Similarly, `next-intl` provides a hooks-based API that looks identical, regardless of if it’s used in a Server or Client Component.

The one restriction that currently comes with this pattern is that hooks can not be called from `async` components. `next-intl` therefore provides a separate set of [awaitable APIs](https://next-intl.dev/docs/environments/server-client-components#async-components) for this use case.

[](https://next-intl.dev/docs/environments/server-client-components#async-or-non-async)Should I use async or non-async functions for my components?

If you implement components that qualify as shared components, it can be beneficial to implement them as non-async functions. This allows to use these components either in a server or client environment, making them really flexible. Even if you don’t intend to to ever run a particular component on the client side, this compatibility can still be helpful, e.g. for simplified testing.

However, there’s no need to dogmatically use non-async functions exclusively for handling internationalization—use what fits your app best.

Regarding performance, async functions and hooks can be used interchangeably. The configuration from [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#i18n-request) is only loaded once upon first usage and both implementations use request-based caching internally where relevant. The only minor difference is that async functions have the benefit that rendering can be resumed right after an async function has been invoked. In contrast, in case a hook call triggers the initialization in `i18n/request.ts`, the component will suspend until the config is resolved and will re-render subsequently, possibly re-executing component logic prior to the hook call. However, once config has been resolved as part of a request, hooks will execute synchronously without suspending, resulting in less overhead in comparison to async functions since rendering can be resumed without having to wait for the microtask queue to flush (see [resuming a suspended component by replaying its execution](https://github.com/acdlite/rfcs/blob/first-class-promises/text/0000-first-class-support-for-promises.md#resuming-a-suspended-component-by-replaying-its-execution) in the corresponding React RFC).

## Using internationalization in Client Components[](https://next-intl.dev/docs/environments/server-client-components#using-internationalization-in-client-components)

Depending on your situation, you may need to handle internationalization in Client Components. Providing all messages to the client side is the easiest way to get started, therefore `next-intl` automatically does this when you render [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider). This is a reasonable approach for many apps.

However, you can be more selective about which messages are passed to the client side if you’re interested in optimizing the performance of your app:

layout.tsx
```
      ...
```

You can still add another instance of `NextIntlClientProvider` for certain parts of your app in case you want to pass `messages` to the client there.

There are several options for using translations from `next-intl` in Client Components, listed here in order of enabling the best performance:

### Option 1: Passing translated labels to Client Components[](https://next-intl.dev/docs/environments/server-client-components#option-1-passing-translated-labels-to-client-components)

The preferred approach is to pass the processed labels as props or `children` from a Server Component.

FAQEntry.tsx
```
    import {useTranslations} from 'next-intl';
    import Expandable from './Expandable'; // A Client Component
    import FAQContent from './FAQContent';

    export default function FAQEntry() {
      // Call `useTranslations` in a Server Component ...
      const t = useTranslations('FAQEntry');

      // ... and pass translated content to a Client Component
      return (
      );
    }
```

Expandable.tsx
```
    'use client';

    import {useState} from 'react';

    function Expandable({title, children}) {
      const [expanded, setExpanded] = useState(false);

      function onToggle() {
        setExpanded(!expanded);
      }

      return (
          <button onClick={onToggle}>{title}</button>
          {expanded && <div>{children}</div>}
      );
    }
```

By doing this, we can use interactive features from React like `useState` on translated content, even though the translation only runs on the server side.

Learn more in the Next.js docs: [Passing Server Components to Client Components as Props](https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns#supported-pattern-passing-server-components-to-client-components-as-props)

[](https://next-intl.dev/docs/environments/server-client-components#example-locale-switcher)Example: How can I implement a locale switcher?

If you implement a locale switcher as an interactive select, you can keep internationalization on the server side by rendering the labels from a Server Component and only marking the `select` element as a Client Component.

LocaleSwitcher.tsx
```
    import {useLocale, useTranslations} from 'next-intl';
    import {locales} from '@/config';

    // A Client Component that registers an event listener for
    // the `change` event of the select, uses `useRouter`
    // to change the locale and uses `useTransition` to display
    // a loading state during the transition.
    import LocaleSwitcherSelect from './LocaleSwitcherSelect';

    export default function LocaleSwitcher() {
      const t = useTranslations('LocaleSwitcher');
      const locale = useLocale();

      return (
          {locales.map((cur) => (
            <option key={cur} value={cur}>
              {t('locale', {locale: cur})}
            </option>
          ))}
      );
    }
```

[Example implementation](https://github.com/amannn/next-intl/blob/main/examples/example-app-router/src/components/LocaleSwitcher.tsx) ([demo](https://next-intl-example-app-router.vercel.app/en))

See also: [`useRouter`](https://next-intl.dev/docs/routing/navigation#userouter)

[](https://next-intl.dev/docs/environments/server-client-components#example-form)Example: How can I implement a form?

Forms need client-side state for showing loading indicators and validation errors.

To keep internationalization on the server side, it can be helpful to structure your components in a way where the interactive parts are moved out to leaf components instead of marking the whole form with `'use client';`.

**Example:**

app/register/page.tsx
```
    import {useTranslations} from 'next-intl';

    // A Client Component, so that `useActionState` can be used
    // to potentially display errors received after submission.
    import RegisterForm from './RegisterForm';

    // A Client Component, so that `useFormStatus` can be used
    // to disable the input field during submission.
    import FormField from './FormField';

    // A Client Component, so that `useFormStatus` can be used
    // to disable the submit button during submission.
    import FormSubmitButton from './FormSubmitButton';

    export default function RegisterPage() {
      const t = useTranslations('RegisterPage');

      function registerAction() {
        'use server';
        // ...
      }

      return (
      );
    }
```

### Option 2: Moving state to the server side[](https://next-intl.dev/docs/environments/server-client-components#option-2-moving-state-to-the-server-side)

You might run into cases where you have dynamic state, such as pagination, that should be reflected in translated messages.

Pagination.tsx
```
    function Pagination({curPage, totalPages}) {
      const t = useTranslations('Pagination');
      return <p>{t('info', {curPage, totalPages})}</p>;
    }
```

You can still manage your translations on the server side by using:

  1. Page or search params
  2. Cookies
  3. Database state

In particular, page and search params are often a great option because they offer additional benefits such as preserving the state of the app when the URL is shared, as well as integration with the browser history.

💡

There’s an article on Smashing Magazine about [using `next-intl` in Server Components](https://www.smashingmagazine.com/2023/03/internationalization-nextjs-13-react-server-components) which explores the usage of search params through a real-world example (specifically the section about [adding interactivity](https://www.smashingmagazine.com/2023/03/internationalization-nextjs-13-react-server-components/#adding-interactivity-dynamic-ordering-of-photos)).

### Option 3: Providing individual messages[](https://next-intl.dev/docs/environments/server-client-components#option-3-providing-individual-messages)

If you need to incorporate dynamic state into components that can not be moved to the server side, you can wrap these components with `NextIntlClientProvider` and provide the relevant messages.

Counter.tsx
```
    import pick from 'lodash/pick';
    import {NextIntlClientProvider, useMessages} from 'next-intl';
    import ClientCounter from './ClientCounter';

    export default function Counter() {
      // Receive messages provided in `i18n/request.ts` …
      const messages = useMessages();

      return (
      );
    }
```

[](https://next-intl.dev/docs/environments/server-client-components#messages-client-namespaces)How can I know which messages I need to provide to the client side?

Currently, the messages you select for being passed to the client side need to be picked based on knowledge about the implementation of the wrapped components.

An automatic, compiler-driven approach is being evaluated in [`next-intl#1`](https://github.com/amannn/next-intl/issues/1).

### Option 4: Providing all messages[](https://next-intl.dev/docs/environments/server-client-components#option-4-providing-all-messages)

If you’re building a highly dynamic app where most components use React’s interactive features, you may prefer to make all messages available to Client Components—this is the default behavior of `next-intl`.

layout.tsx
```
    import {NextIntlClientProvider} from 'next-intl';

    export default async function RootLayout(/* ... */) {
      return (
        <html lang={locale}>
          <body>
          </body>
        </html>
      );
    }
```

[](https://next-intl.dev/docs/environments/server-client-components#client-messages-performance)How does loading messages on the client side relate to performance?

Depending on the requirements for your app, you might want to monitor your [Core Web Vitals](https://web.dev/articles/vitals) to ensure your app meets your performance goals.

If you pass messages to `NextIntlClientProvider`, Next.js will emit them during the streaming render to the markup of the page so that they can be used by Client Components. This can contribute to the [total blocking time](https://web.dev/articles/tbt), which in turn can relate to the [interaction to next paint](https://web.dev/articles/inp) metric. If you’re seeking to improve these metrics in your app, you can be more selective about which messages are passed to the client side.

However, as the general rule for optimization goes: Always measure before you optimize. If your app already performs well, there’s no need for optimization.

There are currently two research areas that aim to maximize the performance of using messages on the client side:

  1. [Automatic tree shaking of messages](https://github.com/amannn/next-intl/issues/1)
  2. [Ahead-of-time compilation of messages](https://github.com/amannn/next-intl/issues/962)

The goal of these are to optimize the patterns you’re already using with `next-intl`, enabling best-in-class performance for your app without changes to your code.

## Troubleshooting[](https://next-intl.dev/docs/environments/server-client-components#troubleshooting)

### ”Failed to call `useTranslations` because the context from `NextIntlClientProvider` was not found.”[](https://next-intl.dev/docs/environments/server-client-components#missing-context)

You might encounter this error or a similar one referencing `useFormatter` while working on your app.

This can happen because:

  1. You’re intentionally calling the hook from a Client Component, but `NextIntlClientProvider` is not present as an ancestor in the component tree. If this is the case, you can [wrap your component in `NextIntlClientProvider`](https://next-intl.dev/docs/environments/server-client-components#option-3-providing-individual-messages) to resolve this error.
  2. The component that calls the hook accidentally ended up in a client-side module graph, but you expected it to render as a Server Component. If this is the case, try to [pass this component via `children`](https://next-intl.dev/docs/environments/server-client-components#option-1-passing-translations-to-client-components) to the Client Component instead.

### ”Functions cannot be passed directly to Client Components because they’re not serializable.”[](https://next-intl.dev/docs/environments/server-client-components#non-serializable-props)

You might encounter this error when you try to pass a non-serializable prop to `NextIntlClientProvider`.

The component accepts the following props that are not serializable:

  1. [`onError`](https://next-intl.dev/docs/usage/configuration#error-handling)
  2. [`getMessageFallback`](https://next-intl.dev/docs/usage/configuration#error-handling)

To configure these, you can wrap `NextIntlClientProvider` with another component that is marked with `'use client'` and defines the relevant props.

See: [How can I provide non-serializable props like `onError` to `NextIntlClientProvider`?](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider-non-serializable-props)

