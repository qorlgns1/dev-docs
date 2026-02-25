---
title: '날짜 및 시간 형식 지정'
description: '날짜와 시간의 형식은 로케일마다 크게 다릅니다(예: 에서는 “Apr 24, 2023”, 에서는 “24 квіт. 2023 р.”). 의 형식 지정 기능을 사용하면 Next.js 앱에서 i18n 차이를 자동으로 처리할 수 있습니다.'
---

Source URL: https://next-intl.dev/docs/usage/dates-times

[문서](https://next-intl.dev/docs/getting-started "Docs")[사용 가이드](https://next-intl.dev/docs/usage "Usage guide")날짜 및 시간

# 날짜 및 시간 형식 지정

영상으로 보는 것을 선호하시나요?

[날짜 형식 지정](https://learn.next-intl.dev/chapters/05-formatting/03-date-formatting)

날짜와 시간의 형식은 로케일마다 크게 다릅니다(예: `en-US`에서는 “Apr 24, 2023”, `uk-UA`에서는 “24 квіт. 2023 р.”). `next-intl`의 형식 지정 기능을 사용하면 Next.js 앱에서 i18n 차이를 자동으로 처리할 수 있습니다.

## 날짜 및 시간 형식 지정[](https://next-intl.dev/docs/usage/dates-times#dates-times)

메시지의 일부가 아닌 일반 날짜는 `useFormatter` 훅이 반환하는 `dateTime` 함수로 형식 지정할 수 있습니다:
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

`dateTime` 함수에 전달할 수 있는 옵션은 MDN의 [`DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat#Using_options) 문서를 참고하거나, `Intl.DateTimeFormat`의 [인터랙티브 탐색기](https://www.intl-explorer.com/DateTimeFormat)에서 확인해 보세요.

[전역 형식](https://next-intl.dev/docs/usage/configuration#formats)이 구성되어 있다면, 두 번째 인수로 이름을 전달해 참조할 수 있습니다:
```
    // Use a global format
    format.dateTime(dateTime, 'short');

    // Optionally override some options
    format.dateTime(dateTime, 'short', {year: 'numeric'});
```

[](https://next-intl.dev/docs/usage/dates-times#parsing-manipulation)날짜와 시간대는 어떻게 저장하고 파싱해야 하나요?

날짜는 완전한 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열이어야 합니다. 예: `2020-11-20T10:36:01.516Z`.

`next-intl`은 날짜 형식 지정에만 관여하므로, 프런트엔드에서 형식 지정하기 전에 `Date` 생성자를 사용해 파싱하면 됩니다.

**더 알아보기:**

[ 날짜 및 시간대](https://learn.next-intl.dev/chapters/05-formatting/02-dates-timezones)

## 상대 시간 형식 지정[](https://next-intl.dev/docs/usage/dates-times#relative-times)

메시지의 일부가 아닌 일반 날짜는 `relativeTime` 함수로 형식 지정할 수 있습니다:
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

값은 반올림된다는 점에 유의하세요. 예를 들어 126분이 지났다면 “2 hours ago”가 반환됩니다.

**더 알아보기:**

[상대 시간](https://learn.next-intl.dev/chapters/05-formatting/05-relative-times)

### `useNow`[](https://next-intl.dev/docs/usage/dates-times#relative-times-usenow)

`now`를 제공하는 패턴은 매우 일반적이므로, `next-intl`은 현재 날짜와 시간을 가져올 수 있는 편의 훅을 제공합니다:
```
    import {useNow, useFormatter} from 'next-intl';

    function FormattedDate({date}) {
      const now = useNow();
      const format = useFormatter();

      format.relativeTime(date, now);
    }
```

컴포넌트에서 단순히 `new Date()`를 호출하는 것과 달리, `useNow`에는 다음과 같은 장점이 있습니다:

  1. 반환된 값은 클라이언트 측 재렌더링 전반에서 일관성을 유지합니다.
  2. 선택적으로 [`updateInterval`](https://next-intl.dev/docs/usage/dates-times#relative-times-update)을 사용해 값을 계속 업데이트할 수 있습니다.
  3. 선택적으로 [전역 값](https://next-intl.dev/docs/usage/configuration#now)에서 값을 초기화할 수 있습니다. 기본적으로 `useNow`는 현재 시간을 사용합니다.

### `updateInterval`[](https://next-intl.dev/docs/usage/dates-times#relative-times-update)

상대 시간 값이 시간이 지나면서 업데이트되길 원한다면 [`useNow`](https://next-intl.dev/docs/usage/configuration#use-now) 훅으로 처리할 수 있습니다:
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

### 단위 사용자 지정[](https://next-intl.dev/docs/usage/dates-times#relative-times-unit)

기본적으로 `relativeTime`은 전달된 날짜와 `now`의 차이에 따라 “3 seconds” 또는 “5 days” 같은 단위를 선택합니다.

특정 단위를 사용하고 싶다면 두 번째 인수로 옵션을 전달할 수 있습니다:
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

## 날짜 및 시간 범위 형식 지정[](https://next-intl.dev/docs/usage/dates-times#date-time-ranges)

`dateTimeRange` 함수로 날짜 및 시간 범위를 형식 지정할 수 있습니다:
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

[전역 형식](https://next-intl.dev/docs/usage/configuration#formats)이 구성되어 있다면, 세 번째 인수로 이름을 전달해 참조할 수 있습니다:
```
    // Use a global format
    format.dateTimeRange(dateTimeA, dateTimeB, 'short');

    // Optionally override some options
    format.dateTimeRange(dateTimeA, dateTimeB, 'short', {year: 'numeric'});
```

## 메시지 내 날짜 및 시간[](https://next-intl.dev/docs/usage/dates-times#dates-and-times-within-messages)

ICU 구문을 사용해 메시지 안에 날짜와 시간을 포함할 수 있습니다.

en.json
```
    {
      "ordered": "Ordered on {orderDate, date, medium}"
    }
```

다음 형식은 기본으로 지원됩니다: `full`, `long`, `medium`, `short`.

💡

번역가와 함께 작업한다면, 날짜와 시간 ICU 구문을 지원하는 에디터를 사용하는 것이 도움이 될 수 있습니다(예: [Crowdin Editor](https://support.crowdin.com/icu-message-syntax/#date-time)).

날짜 스켈레톤을 사용해 형식을 사용자 지정할 수 있습니다:

en.json
```
    {
      // Renders e.g. "Ordered on Jul 9, 2024"
      "ordered": "Ordered on {orderDate, date, ::yyyyMMMd}"
    }
```

스켈레톤 사용을 나타내기 위해 앞에 `::`가 붙는다는 점에 유의하세요.

**ICU의 다음 형식이 지원됩니다:**

기호| 의미| 패턴| 예시
---|---|---|---
G| 시대 표시자(날짜 포함)| G
GGGG
GGGGG| 7/9/2024 AD
7/9/2024 Anno Domini
7/9/2024 A
y| 연도| y
yy
yyyy| 2024
24
2024
M| 연중 월| M
MM
MMM
MMMM
MMMMM
| 7
07
Jul
July
J
d| 월의 일| d
dd| 9
09
E| 요일| E
EEEE
EEEEE| Tue
Tuesday
T
h| 시간(1-12)| h
hh| 9 AM
09 AM
K| 시간(0-11)| K
KK| 0 AM (12 AM with `h`)
00 AM
H| 시간(0-23)| HH| 09
k| 시간(1-24)| kk| 24 (00 with `H`)
m| 분(초와 함께 사용 시 2자리)| m
mmss| 6
06:03
s| 초(분과 함께 사용 시 2자리)| s
mmss| 3
06:03
z| 시간대| z
zzzz| GMT+2
Central European Summer Time

패턴은 서로 조합할 수 있으므로, 예를 들어 `yyyyMMMd`는 “Jul 9, 2024”를 반환합니다.

### 사용자 지정 날짜 및 시간 형식[](https://next-intl.dev/docs/usage/dates-times#custom-date-and-time-formats)

메시지에서 사용자 지정 형식을 사용하려면, 이름으로 참조할 수 있는 [`DateTimeFormat` options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat#Using_options) 기반 포매터를 제공하면 됩니다.

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

여러 컴포넌트에서 날짜 및 시간 형식을 재사용하려면 [전역 형식](https://next-intl.dev/docs/usage/configuration#formats)을 구성할 수 있습니다.

