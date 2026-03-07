---
title: "font-variant-numeric - 타이포그래피 - Tailwind CSS"
description: "지원되는 폰트에서 서수 표기에 대한 특수 글리프를 활성화하려면 ordinal 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/font-variant-numeric

# font-variant-numeric - 타이포그래피 - Tailwind CSS

| 클래스               | 스타일                                      |
| -------------------- | ------------------------------------------- |
| `normal-nums`        | `font-variant-numeric: normal;`             |
| `ordinal`            | `font-variant-numeric: ordinal;`            |
| `slashed-zero`       | `font-variant-numeric: slashed-zero;`       |
| `lining-nums`        | `font-variant-numeric: lining-nums;`        |
| `oldstyle-nums`      | `font-variant-numeric: oldstyle-nums;`      |
| `proportional-nums`  | `font-variant-numeric: proportional-nums;`  |
| `tabular-nums`       | `font-variant-numeric: tabular-nums;`       |
| `diagonal-fractions` | `font-variant-numeric: diagonal-fractions;` |
| `stacked-fractions`  | `font-variant-numeric: stacked-fractions;`  |

## 예제

- 서수 글리프 사용하기

지원되는 폰트에서 서수 표기에 대한 특수 글리프를 활성화하려면 `ordinal` 유틸리티를 사용하세요:

1st

```
    <p class="ordinal ...">1st</p>
```

- 슬래시 0 사용하기

지원되는 폰트에서 슬래시가 있는 0을 강제로 사용하려면 `slashed-zero` 유틸리티를 사용하세요:

0

```
    <p class="slashed-zero ...">0</p>
```

- 라이닝 숫자 사용하기

지원되는 폰트에서 기준선에 맞춰 정렬되는 숫자 글리프를 사용하려면 `lining-nums` 유틸리티를 사용하세요:

1234567890

```
    <p class="lining-nums ...">1234567890</p>
```

- 올드스타일 숫자 사용하기

지원되는 폰트에서 일부 숫자에 디센더가 있는 숫자 글리프를 사용하려면 `oldstyle-nums` 유틸리티를 사용하세요:

1234567890

```
    <p class="oldstyle-nums ...">1234567890</p>
```

- 비례 숫자 사용하기

지원되는 폰트에서 비례 너비를 가지는 숫자 글리프를 사용하려면 `proportional-nums` 유틸리티를 사용하세요:

12121

90909

```
    <p class="proportional-nums ...">12121</p><p class="proportional-nums ...">90909</p>
```

- 테이블형 숫자 사용하기

지원되는 폰트에서 균일한/테이블형 너비를 가지는 숫자 글리프를 사용하려면 `tabular-nums` 유틸리티를 사용하세요:

12121

90909

```
    <p class="tabular-nums ...">12121</p><p class="tabular-nums ...">90909</p>
```

- 대각 분수 사용하기

지원되는 폰트에서 슬래시로 구분된 숫자를 일반적인 대각 분수로 바꾸려면 `diagonal-fractions` 유틸리티를 사용하세요:

1/2 3/4 5/6

```
    <p class="diagonal-fractions ...">1/2 3/4 5/6</p>
```

- 누적 분수 사용하기

지원되는 폰트에서 슬래시로 구분된 숫자를 일반적인 누적 분수로 바꾸려면 `stacked-fractions` 유틸리티를 사용하세요:

1/2 3/4 5/6

```
    <p class="stacked-fractions ...">1/2 3/4 5/6</p>
```

- 여러 유틸리티 함께 쌓기

`font-variant-numeric` 유틸리티는 조합 가능하므로, 함께 결합해서 여러 variant를 활성화할 수 있습니다:

소계
$100.00
세금
$14.50
합계
$114.50

```
    <dl class="...">  <dt class="...">Subtotal</dt>  <dd class="text-right slashed-zero tabular-nums ...">$100.00</dd>  <dt class="...">Tax</dt>  <dd class="text-right slashed-zero tabular-nums ...">$14.50</dd>  <dt class="...">Total</dt>  <dd class="text-right slashed-zero tabular-nums ...">$114.50</dd></dl>
```

- 숫자 폰트 variant 초기화하기

숫자 폰트 variant를 초기화하려면 `normal-nums` 속성을 사용하세요:

```
    <p class="slashed-zero tabular-nums md:normal-nums ...">  <!-- ... --></p>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `font-variant-numeric` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <p class="proportional-nums md:tabular-nums ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용 방법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
