---
title: "flex - Flexbox 및 Grid - Tailwind CSS"
description: "flex-1 같은 flex-<number> 유틸리티를 사용하면 flex 항목의 초기 크기를 무시하고, 필요에 따라 확장 및 축소되도록 할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/flex

# flex - Flexbox 및 Grid - Tailwind CSS

| 클래스                     | 스타일                           |
| -------------------------- | -------------------------------- |
| `flex-<number>`            | `flex: <number>;`                |
| `flex-<fraction>`          | `flex: calc(<fraction> * 100%);` |
| `flex-auto`                | `flex: auto;`                    |
| `flex-initial`             | `flex: 0 auto;`                  |
| `flex-none`                | `flex: none;`                    |
| `flex-(<custom-property>)` | `flex: var(<custom-property>);`  |
| `flex-[<value>]`           | `flex: <value>;`                 |

## 예제

- 기본 예제

`flex-1` 같은 `flex-<number>` 유틸리티를 사용하면 flex 항목의 초기 크기를 무시하고, 필요에 따라 확장 및 축소되도록 할 수 있습니다:

01

02

03

```
    <div class="flex">  <div class="w-14 flex-none ...">01</div>  <div class="w-64 flex-1 ...">02</div>  <div class="w-32 flex-1 ...">03</div></div>
```

- Initial

`flex-initial`을 사용하면 flex 항목의 초기 크기를 고려하면서, 확장은 하지 않고 축소만 가능하게 할 수 있습니다:

01

02

03

```
    <div class="flex">  <div class="w-14 flex-none ...">01</div>  <div class="w-64 flex-initial ...">02</div>  <div class="w-32 flex-initial ...">03</div></div>
```

- Auto

`flex-auto`를 사용하면 flex 항목의 초기 크기를 고려하면서 확장 및 축소가 가능해집니다:

01

02

03

```
    <div class="flex ...">  <div class="w-14 flex-none ...">01</div>  <div class="w-64 flex-auto ...">02</div>  <div class="w-32 flex-auto ...">03</div></div>
```

- None

`flex-none`을 사용하면 flex 항목이 확장되거나 축소되지 않도록 할 수 있습니다:

01

02

03

```
    <div class="flex ...">  <div class="w-14 flex-none ...">01</div>  <div class="w-32 flex-none ...">02</div>  <div class="flex-1 ...">03</div></div>
```

- 사용자 지정 값 사용하기

`flex-[<value>]` 문법을 사용하면 완전히 사용자 지정한 값으로 flex 단축 속성을 설정할 수 있습니다:

```
    <div class="flex-[3_1_auto] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `flex-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="flex-(--my-flex) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `flex-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `flex` 유틸리티 앞에 붙이면, 해당 유틸리티를 중간 크기 이상의 화면에서만 적용할 수 있습니다:

```
    <div class="flex-none md:flex-1 ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 확인하세요.
