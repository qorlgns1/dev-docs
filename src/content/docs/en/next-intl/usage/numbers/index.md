---
title: 'Number formatting'
description: 'Prefer to watch a video?'
---

Source URL: https://next-intl.dev/docs/usage/numbers

# Number formatting

Prefer to watch a video?

[Number formatting](https://learn.next-intl.dev/chapters/05-formatting/01-number-formatting)

The formatting of numbers can vary depending on the user’s locale and may include different rules such as:

  1. Decimal separators (e.g. “12.3” in `en-US` vs. “12,3” in `de-DE`)
  2. Digit grouping (e.g. “120,000” in `en-US` vs. “1,20,000” in `hi-IN`)
  3. Currency sign position (e.g. “12 €” in `de-DE` vs. ”€ 12” in `de-AT`)

By using the formatting capabilities provided by `next-intl`, you can adjust to these variations and ensure that numbers are displayed accurately across your Next.js app for all users.

## Formatting plain numbers[](https://next-intl.dev/docs/usage/numbers#formatting-plain-numbers)

When you’re formatting plain numbers that are not part of a message, you can use a separate hook:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();

      // Renders "$499.90"
      format.number(499.9, {style: 'currency', currency: 'USD'});
    }
```

See the MDN docs about [`NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat#Using_options) to learn more about the options you can pass to the `number` function or try the [interactive explorer](https://www.intl-explorer.com/NumberFormat) for `Intl.NumberFormat`.

If you have [global formats](https://next-intl.dev/docs/usage/configuration#formats) configured, you can reference them by passing a name as the second argument:
```
    // Use a global format
    format.number(499.9, 'precise');

    // Optionally override some options
    format.number(499.9, 'price', {currency: 'USD'});
```

## Numbers within messages[](https://next-intl.dev/docs/usage/numbers#numbers-within-messages)

Numbers can be embedded within messages by using the ICU syntax.

en.json
```
    {
      "basic": "Basic formatting: {value, number}",
      "percentage": "Displayed as a percentage: {value, number, percent}",
      "custom": "At most 2 fraction digits: {value, number, ::.##}"
    }
```

Note the leading `::` that is used to indicate that a skeleton should be used. See the ICU docs on [number skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.html) to learn more about this.

These formats are supported out of the box: `currency` and `percent`.

💡

If you work with translators, it can be helpful for them to use an editor that supports the ICU syntax for numbers (e.g. the [Crowdin Editor](https://support.crowdin.com/icu-message-syntax/#number)).

### Custom number formats[](https://next-intl.dev/docs/usage/numbers#custom-number-formats)

To use custom formats in messages, you can provide formatters that can be referenced by name.

en.json
```
    {
      "price": "This product costs {price, number, currency}"
    }
```
```
    t(
      'price',
      {price: 32000.99},
      {
        number: {
          currency: {
            style: 'currency',
            currency: 'EUR'
          }
        }
      }
    );
```

💡

To reuse number formats for multiple components, you can configure [global formats](https://next-intl.dev/docs/usage/configuration#formats).

