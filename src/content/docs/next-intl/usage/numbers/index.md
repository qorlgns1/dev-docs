---
title: '숫자 서식 지정'
description: '숫자의 서식은 사용자의 로캘에 따라 달라질 수 있으며, 다음과 같은 서로 다른 규칙이 포함될 수 있습니다.'
---

Source URL: https://next-intl.dev/docs/usage/numbers

# 숫자 서식 지정

영상으로 확인하고 싶으신가요?

[숫자 서식 지정](https://learn.next-intl.dev/chapters/05-formatting/01-number-formatting)

숫자의 서식은 사용자의 로캘에 따라 달라질 수 있으며, 다음과 같은 서로 다른 규칙이 포함될 수 있습니다.

  1. 소수 구분자 (예: `en-US`에서는 “12.3”, `de-DE`에서는 “12,3”)
  2. 자릿수 그룹화 (예: `en-US`에서는 “120,000”, `hi-IN`에서는 “1,20,000”)
  3. 통화 기호 위치 (예: `de-DE`에서는 “12 €”, `de-AT`에서는 ”€ 12”)

`next-intl`에서 제공하는 서식 지정 기능을 사용하면 이러한 차이에 맞게 조정할 수 있고, 모든 사용자의 Next.js 앱에서 숫자가 정확하게 표시되도록 보장할 수 있습니다.

## 일반 숫자 서식 지정[](https://next-intl.dev/docs/usage/numbers#formatting-plain-numbers)

메시지의 일부가 아닌 일반 숫자를 서식 지정할 때는 별도의 훅을 사용할 수 있습니다:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();

      // Renders "$499.90"
      format.number(499.9, {style: 'currency', currency: 'USD'});
    }
```

`number` 함수에 전달할 수 있는 옵션을 더 알아보려면 [`NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat#Using_options)에 대한 MDN 문서를 참고하거나, `Intl.NumberFormat`의 [interactive explorer](https://www.intl-explorer.com/NumberFormat)를 사용해 보세요.

[global formats](https://next-intl.dev/docs/usage/configuration#formats)가 구성되어 있다면, 두 번째 인수로 이름을 전달해 이를 참조할 수 있습니다:
```
    // Use a global format
    format.number(499.9, 'precise');

    // Optionally override some options
    format.number(499.9, 'price', {currency: 'USD'});
```

## 메시지 내 숫자[](https://next-intl.dev/docs/usage/numbers#numbers-within-messages)

ICU 문법을 사용해 메시지 안에 숫자를 포함할 수 있습니다.

en.json
```
    {
      "basic": "Basic formatting: {value, number}",
      "percentage": "Displayed as a percentage: {value, number, percent}",
      "custom": "At most 2 fraction digits: {value, number, ::.##}"
    }
```

스켈레톤을 사용해야 함을 나타내기 위해 앞에 `::`를 붙인다는 점에 유의하세요. 자세한 내용은 [number skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.html)에 대한 ICU 문서를 참고하세요.

다음 형식은 기본으로 지원됩니다: `currency`, `percent`.

💡

번역가와 협업하는 경우, 숫자용 ICU 문법을 지원하는 에디터를 사용하는 것이 도움이 될 수 있습니다(예: [Crowdin Editor](https://support.crowdin.com/icu-message-syntax/#number)).

### 사용자 지정 숫자 형식[](https://next-intl.dev/docs/usage/numbers#custom-number-formats)

메시지에서 사용자 지정 형식을 사용하려면, 이름으로 참조할 수 있는 포매터를 제공하면 됩니다.

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

여러 컴포넌트에서 숫자 형식을 재사용하려면 [global formats](https://next-intl.dev/docs/usage/configuration#formats)를 구성할 수 있습니다.

