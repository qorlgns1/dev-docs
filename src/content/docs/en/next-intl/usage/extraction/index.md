---
title: 'useExtracted (experimental)'
description: 'As an alternative to managing namespaces and keys manually,  provides an additional API that works similar to  but automatically extracts messages fro...'
---

Source URL: https://next-intl.dev/docs/usage/extraction

# `useExtracted` (experimental)

As an alternative to managing namespaces and keys manually, `next-intl` provides an additional API that works similar to [`useTranslations`](https://next-intl.dev/docs/usage/translations) but automatically extracts messages from your source files.
```
    import {useExtracted} from 'next-intl';

    function InlineMessages() {
      const t = useExtracted();
      return <h1>{t('Look ma, no keys!')}</h1>;
    }
```

Extraction integrates automatically with `next dev` and `next build` via a Turbo- or Webpack loader, you don’t need to manually trigger it.

When the above file is compiled, this will:

  1. Extract the inline message with an automatically assigned key to your source locale:

messages/en.json
```
    {
      "VgH3tb": "Look ma, no keys!"
    }
```

  2. Keeps target locales in sync by either adding empty entries or removing outdated ones:

messages/de.json
```
    {
      "VgH3tb": ""
    }
```

  3. Compiles the file to replace `useExtracted` with `useTranslations`

```
    import {useTranslations} from 'next-intl';

    function InlineMessages() {
      const t = useTranslations();
      return <h1>{t('VgH3tb')}</h1>;
    }
```

**Links:**

  * [Introduction blog post](https://next-intl.dev/blog/use-extracted)
  * [Example app](https://next-intl.dev/examples#app-router-extracted)

## Getting started[](https://next-intl.dev/docs/usage/extraction#getting-started)

This API is currently experimental, and needs to be enabled in `next.config.ts`:

next.config.ts
```
    import {NextConfig} from 'next';
    import createNextIntlPlugin from 'next-intl/plugin';

    const withNextIntl = createNextIntlPlugin({
      experimental: {
        // Relative path(s) to source files
        srcPath: './src',

        extract: {
          // Defines which locale to extract to
          sourceLocale: 'en'
        },

        messages: {
          // Relative path to the directory
          path: './messages',

          // Either 'json', 'po', or a custom format (see below)
          format: 'json',

          // Either 'infer' to automatically detect locales based on
          // matching files in `path` or an explicit array of locales
          locales: 'infer'
        }
      }
    });

    const config: NextConfig = {};
    export default withNextIntl(config);
```

With this, every time you call `next dev` or `next build`, messages will be extracted as they are discovered and your messages will be kept in sync.

See [`createNextIntlPlugin`](https://next-intl.dev/docs/usage/plugin#extract) for details.

[](https://next-intl.dev/docs/usage/extraction#manual)Can I extract messages manually?

While message extraction is designed to seamlessly integrate with your development workflow based on running `next dev` and `next build`, you can also extract messages manually:
```
    import {unstable_extractMessages} from 'next-intl/extractor';

    await unstable_extractMessages({
      srcPath: './src',
      sourceLocale: 'en',
      messages: {
        path: './messages',
        format: 'json',
        locales: 'infer'
      }
    });

    console.log('✔ Messages extracted');
```

This can be useful when you’re developing a package like a component library, where you don’t have a Next.js dev server running and you want to provide messages along with the package.

## Inline messages[](https://next-intl.dev/docs/usage/extraction#inline-messages)

### ICU messages[](https://next-intl.dev/docs/usage/extraction#icu-messages)

All [ICU features](https://next-intl.dev/docs/usage/translations#icu-messages) you are familiar with from `useTranslations` are supported and can be used as usual:
```
    // Interpolation of arguments
    t('Hello {name}!', {name: 'Jane'});
```
```
    // Cardinal pluralization
    t(
      'You have {count, plural, =0 {no followers yet} =1 {one follower} other {# followers}}.',
      {count: 3580}
    );
```
```
    // Ordinal pluralization
    t(
      "It's your {year, selectordinal, one {#st} two {#nd} few {#rd} other {#th}} birthday!",
      {year: 22}
    );
```
```
    // Select values
    t('{gender, select, female {She is} male {He is} other {They are}} online.', {
      gender: 'female'
    });
```
```
    // Rich text
    t.rich('Please refer to the <link>guidelines</link>.', {
      link: (chunks) => <Link href="/guidelines">{chunks}</Link>
    });
```

The one exception is `t.raw`, this feature is not intended to be used with message extraction.

### Descriptions[](https://next-intl.dev/docs/usage/extraction#descriptions)

In order to provide more context about a message for (AI) translators, you can provide descriptions:
```
    <button onClick={onSlideRight}>
      {t({
        message: 'Right',
        description: 'Advance to the next slide'
      })}
    </button>
```

### Explicit IDs[](https://next-intl.dev/docs/usage/extraction#explicit-ids)

If you want to use an explicit ID instead of the auto-generated one, you can optionally provide one:
```
    <button onClick={onSlideRight}>
      {t({
        id: 'carousel.next',
        message: 'Right'
      })}
    </button>
```

This can be useful when you have a label that is used in multiple places, but should have different translations in other languages. This is an escape hatch that should rarely be necessary.

### Namespaces[](https://next-intl.dev/docs/usage/extraction#namespaces)

If you want to organize your messages under a specific namespace, you can pass it to `useExtracted`:
```
    function Modal() {
      const t = useExtracted('design-system');
      return (
        <>
          <button>{t('Close')}</button>
          ...
        </>
      );
    }
```

This will extract messages associated with a call to `t` to the given namespace:
```
    {
      "design-system": {
        "5VpL9Z": "Close"
      }
    }
```

Namespaces are useful in situations like:

  1. **Libraries:** If you have multiple packages in a monorepo, you can merge messages from different packages into a single catalog and avoid key collisions between packages.
  2. **Splitting:** If you want to pass only certain messages to the client side, this can help to group them accordingly (e.g. `<NextIntlClientProvider messages={messages.client}>`).

It’s a good idea to not overuse namespaces, as they can make moving messages between components more difficult if this involves refactoring the namespace.

### `await getExtracted()`[](https://next-intl.dev/docs/usage/extraction#get-extracted)

For usage in async functions like Server Components, Metadata and Server Actions, you use an asynchronous variant from `next-intl/server`:

page.tsx
```
    import {getExtracted} from 'next-intl/server';

    export default async function ProfilePage() {
      const user = await fetchUser();
      const t = await getExtracted();

      return (
      );
    }
```

### Optional compilation[](https://next-intl.dev/docs/usage/extraction#optional-compilation)

While message extraction is primarily designed to be used with a running Next.js app, `useExtracted` works perfectly fine without being compiled into `useTranslations`. In this case, the inline message will be used directly instead of being replaced with a translation key.

This can for example be useful for tests:
```
    import {expect, it} from 'vitest';
    import {NextIntlClientProvider} from 'next-intl';
    import {renderToString} from 'react-dom/server';

    function Component() {
      const t = useExtracted();
      return t('Hello {name}!', {name: 'Jane'});
    }

    it('renders', () => {
      const html = renderToString(
        // No need to pass any messages
      );

      // ✅ The inline message will be used
      expect(html).toContain('Hello Jane!');
    });
```

## Formats[](https://next-intl.dev/docs/usage/extraction#formats)

Messages can be extracted as [`.json`](https://next-intl.dev/docs/usage/plugin#formats-json), [`.po`](https://next-intl.dev/docs/usage/plugin#formats-po), or with [custom file formats](https://next-intl.dev/docs/usage/plugin#formats-custom)—see [`messages.format`](https://next-intl.dev/docs/usage/plugin#format) for configuration details.

**Recommendation:** As keys are auto-generated with `useExtracted`, it’s recommended to use **PO files** as they support providing more context about a message like file references and descriptions. This can be helpful for (AI) translators.

💡

AI-based translation can be automated with a translation management system like [Crowdin](https://next-intl.dev/docs/workflows/localization-management).

