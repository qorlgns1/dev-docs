---
title: 'TypeScript augmentation'
description: 'Prefer to watch a video?'
---

Source URL: https://next-intl.dev/docs/workflows/typescript

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Workflows & integrations](https://next-intl.dev/docs/workflows "Workflows & integrations")TypeScript augmentation

# TypeScript augmentation

Prefer to watch a video?

[Editor tools](https://learn.next-intl.dev/chapters/03-translations/05-tooling)

`next-intl` integrates seamlessly with TypeScript right out of the box, requiring no additional setup.

However, you can optionally provide supplemental definitions to augment the types that `next-intl` works with, enabling improved autocompletion and type safety across your app.

global.ts
```
    import {routing} from '@/i18n/routing';
    import {formats} from '@/i18n/request';
    import messages from './messages/en.json';

    declare module 'next-intl' {
      interface AppConfig {
        Locale: (typeof routing.locales)[number];
        Messages: typeof messages;
        Formats: typeof formats;
      }
    }
```

Type augmentation is available for:

  * [`Locale`](https://next-intl.dev/docs/workflows/typescript#locale)
  * [`Messages`](https://next-intl.dev/docs/workflows/typescript#messages)
  * [`Formats`](https://next-intl.dev/docs/workflows/typescript#formats)

## `Locale`[](https://next-intl.dev/docs/workflows/typescript#locale)

Augmenting the `Locale` type will affect all APIs from `next-intl` that either return or receive a locale:
```
    import {useLocale} from 'next-intl';

    // ✅ 'en' | 'de'
    const locale = useLocale();
```
```
    import {Link} from '@/i18n/routing';

    // ✅ Passes the validation
```

