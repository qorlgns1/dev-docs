---
title: 'Runtime requirements'
description: 'The source code of  is compiled for the same browsers that Next.js supports.'
---

Source URL: https://next-intl.dev/docs/environments/runtime-requirements

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Environments](https://next-intl.dev/docs/environments "Environments")Runtime requirements

# Runtime requirements

## Browser[](https://next-intl.dev/docs/environments/runtime-requirements#browser)

The source code of `next-intl` is compiled for the same browsers that [Next.js supports](https://nextjs.org/docs/architecture/supported-browsers).

Based on the features you’re using, you have to make sure your target browsers support the following APIs:

  * Basic usage: `Intl.Locale` ([compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#browser_compatibility))
  * Date & time formatting: `Intl.DateTimeFormat` ([compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#browser_compatibility))
  * Number formatting: `Intl.NumberFormat` ([compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#browser_compatibility))
  * Pluralization: `Intl.PluralRules` ([compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#browser_compatibility))
  * Relative time formatting: `Intl.RelativeTimeFormat` ([compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#browser_compatibility))
  * List formatting: `Intl.ListFormat` ([compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat#browser_compatibility))

If you target a browser that doesn’t support all the required APIs, consider using polyfills.

Cloudflare provides a [polyfill service](https://cdnjs.cloudflare.com/polyfill/) that you can use to load the necessary polyfills for a given locale.

**Example:**

IntlPolyfills.tsx
```
    import {useLocale} from 'next-intl';
    import Script from 'next/script';

    function IntlPolyfills() {
      const locale = useLocale();

      const polyfills = [
        'Intl',
        'Intl.Locale',
        'Intl.DateTimeFormat',
        `Intl.DateTimeFormat.~locale.${locale}`,
        `Intl.NumberFormat`,
        `Intl.NumberFormat.~locale.${locale}`,
        'Intl.PluralRules',
        `Intl.PluralRules.~locale.${locale}`,
        'Intl.RelativeTimeFormat',
        `Intl.RelativeTimeFormat.~locale.${locale}`,
        'Intl.ListFormat',
        `Intl.ListFormat.~locale.${locale}`
      ];

      return (
      );
    }
```

⚠️

Note that the polyfill service doesn’t support every locale. You can find a list of the available polyfills in the [`polyfill-service` repository](https://github.com/cdnjs/polyfill-service/tree/main/polyfill-libraries/3.101.0/polyfills/__dist) (e.g. search for `Intl.DateTimeFormat.~locale.de-AT`).

## Node.js[](https://next-intl.dev/docs/environments/runtime-requirements#nodejs)

The minimum version to support all relevant `Intl` APIs is **Node.js 13**. Starting from this version, all required APIs are available.

