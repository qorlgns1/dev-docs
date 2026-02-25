---
title: 'Date and time formatting'
description: 'Prefer to watch a video?'
---

Source URL: https://next-intl.dev/docs/usage/dates-times

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Usage guide](https://next-intl.dev/docs/usage "Usage guide")Dates and times

# Date and time formatting

Prefer to watch a video?

[Date formatting](https://learn.next-intl.dev/chapters/05-formatting/03-date-formatting)

The formatting of dates and times varies greatly between locales (e.g. “Apr 24, 2023” in `en-US` vs. “24 квіт. 2023 р.” in `uk-UA`). By using the formatting capabilities of `next-intl`, you can handle i18n differences in your Next.js app automatically.

## Formatting dates and times[](https://next-intl.dev/docs/usage/dates-times#dates-times)

You can format plain dates that are not part of a message with the `dateTime` function that is returned from the `useFormatter` hook:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();
      const dateTime = new Date('2020-11-20T10:36:01.516Z');

      // Renders "Nov 20, 2020"
      format.dateTime(dateTime, {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      });

      // Renders "11:36 AM"
      format.dateTime(dateTime, {hour: 'numeric', minute: 'numeric'});
    }
```

See the MDN docs on [`DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat#Using_options) to learn more about the options that you can provide to the `dateTime` function or try the [interactive explorer](https://www.intl-explorer.com/DateTimeFormat) for `Intl.DateTimeFormat`.

If you have [global formats](https://next-intl.dev/docs/usage/configuration#formats) configured, you can reference them by passing a name as the second argument:
```
    // Use a global format
    format.dateTime(dateTime, 'short');

    // Optionally override some options
    format.dateTime(dateTime, 'short', {year: 'numeric'});
```

[](https://next-intl.dev/docs/usage/dates-times#parsing-manipulation)How should I store and parse dates and time zones?

You should ensure that dates are full [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) strings, e.g. `2020-11-20T10:36:01.516Z`.

Since `next-intl` is only concerned with formatting dates, you can use the `Date` constructor to parse them before formatting them in the frontend.

**Learn more:**

[ Dates & time zones](https://learn.next-intl.dev/chapters/05-formatting/02-dates-timezones)

## Formatting relative times[](https://next-intl.dev/docs/usage/dates-times#relative-times)

You can format plain dates that are not part of a message with the `relativeTime` function:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();
      const dateTime = new Date('2020-11-20T08:30:00.000Z');

      // A reference point in time
      const now = new Date('2020-11-20T10:36:00.000Z');

      // This will render "2 hours ago"
      format.relativeTime(dateTime, now);
    }
```

Note that values are rounded, so e.g. if 126 minutes have passed, “2 hours ago” will be returned.

**Learn more:**

[Relative times](https://learn.next-intl.dev/chapters/05-formatting/05-relative-times)

### `useNow`[](https://next-intl.dev/docs/usage/dates-times#relative-times-usenow)

Since providing `now` is a common pattern, `next-intl` provides a convenience hook that can be used to retrieve the current date and time:
```
    import {useNow, useFormatter} from 'next-intl';

    function FormattedDate({date}) {
      const now = useNow();
      const format = useFormatter();

      format.relativeTime(date, now);
    }
```

In contrast to simply calling `new Date()` in your component, `useNow` has some benefits:

  1. The returned value is consistent across re-renders on the client side.
  2. You can optionally use [`updateInterval`](https://next-intl.dev/docs/usage/dates-times#relative-times-update) to update the value continuously.
  3. The value can optionally be initialized from a [global value](https://next-intl.dev/docs/usage/configuration#now). By default, `useNow` will use the current time.

### `updateInterval`[](https://next-intl.dev/docs/usage/dates-times#relative-times-update)

In case you want a relative time value to update over time, you can do so with the [`useNow`](https://next-intl.dev/docs/usage/configuration#use-now) hook:
```
    import {useNow, useFormatter} from 'next-intl';

    function Component() {
      // Use the global now value initially …
      const now = useNow({
        // … and update it every 10 seconds
        updateInterval: 1000 * 10
      });

      const format = useFormatter();
      const dateTime = new Date('2020-11-20T10:36:01.516Z');

      // Renders e.g. "2 hours ago" and updates continuously
      format.relativeTime(dateTime, now);
    }
```

### Customizing the unit[](https://next-intl.dev/docs/usage/dates-times#relative-times-unit)

By default, `relativeTime` will pick a unit based on the difference between the passed date and `now` like “3 seconds” or “5 days”.

If you want to use a specific unit, you can provide options via the second argument:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();
      const dateTime = new Date('2020-03-20T08:30:00.000Z');
      const now = new Date('2020-11-22T10:36:00.000Z');

      // Renders "247 days ago"
      format.relativeTime(dateTime, {now, unit: 'day'});
    }
```

## Formatting date and time ranges[](https://next-intl.dev/docs/usage/dates-times#date-time-ranges)

You can format ranges of dates and times with the `dateTimeRange` function:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();
      const dateTimeA = new Date('2020-11-20T08:30:00.000Z');
      const dateTimeB = new Date('2021-01-24T08:30:00.000Z');

      // Renders "Nov 20, 2020 – Jan 24, 2021"
      format.dateTimeRange(dateTimeA, dateTimeB, {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      });
    }
```

If you have [global formats](https://next-intl.dev/docs/usage/configuration#formats) configured, you can reference them by passing a name as the third argument:
```
    // Use a global format
    format.dateTimeRange(dateTimeA, dateTimeB, 'short');

    // Optionally override some options
    format.dateTimeRange(dateTimeA, dateTimeB, 'short', {year: 'numeric'});
```

## Dates and times within messages[](https://next-intl.dev/docs/usage/dates-times#dates-and-times-within-messages)

Dates and times can be embedded within messages by using the ICU syntax.

en.json
```
    {
      "ordered": "Ordered on {orderDate, date, medium}"
    }
```

These formats are supported out of the box: `full`, `long`, `medium` and `short`.

💡

If you work with translators, it can be helpful for them to use an editor that supports the ICU syntax for dates and times (e.g. the [Crowdin Editor](https://support.crowdin.com/icu-message-syntax/#date-time)).

You can customize the formatting by using date skeletons:

en.json
```
    {
      // Renders e.g. "Ordered on Jul 9, 2024"
      "ordered": "Ordered on {orderDate, date, ::yyyyMMMd}"
    }
```

Note the leading `::` that is used to indicate that a skeleton should be used.

**These formats from ICU are supported:**

Symbol| Meaning| Pattern| Example
---|---|---|---
G| Era designator (includes the date)| G
GGGG
GGGGG| 7/9/2024 AD
7/9/2024 Anno Domini
7/9/2024 A
y| Year| y
yy
yyyy| 2024
24
2024
M| Month in year| M
MM
MMM
MMMM
MMMMM
| 7
07
Jul
July
J
d| Day in month| d
dd| 9
09
E| Day of week| E
EEEE
EEEEE| Tue
Tuesday
T
h| Hour (1-12)| h
hh| 9 AM
09 AM
K| Hour (0-11)| K
KK| 0 AM (12 AM with `h`)
00 AM
H| Hour (0-23)| HH| 09
k| Hour (1-24)| kk| 24 (00 with `H`)
m| Minute (2 digits if used with seconds)| m
mmss| 6
06:03
s| Second (2 digits if used with minutes)| s
mmss| 3
06:03
z| Time zone| z
zzzz| GMT+2
Central European Summer Time

Patterns can be combined with each other, therefore e.g. `yyyyMMMd` would return “Jul 9, 2024”.

### Custom date and time formats[](https://next-intl.dev/docs/usage/dates-times#custom-date-and-time-formats)

To use custom formats in messages, you can provide formatters based on [`DateTimeFormat` options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat#Using_options) that can be referenced by name.

en.json
```
    {
      "ordered": "Ordered on {orderDate, date, short}"
    }
```
```
    t(
      'ordered',
      {orderDate: new Date('2020-11-20T10:36:01.516Z')},
      {
        dateTime: {
          short: {
            day: 'numeric',
            month: 'short',
            year: 'numeric'
          }
        }
      }
    );
```

💡

To reuse date and time formats for multiple components, you can configure [global formats](https://next-intl.dev/docs/usage/configuration#formats).

