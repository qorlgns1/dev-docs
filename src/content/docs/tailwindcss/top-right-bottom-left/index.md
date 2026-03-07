---
title: "top / right / bottom / left - 레이아웃 - Tailwind CSS"
description: "top-<number>, right-<number>, bottom-<number>, left-<number>, inset-<number> 유틸리티(top-0, bottom-4 등)를 사용해 positioned element의 가로 또는 세로 위치를 설정합니다:"
---

# top / right / bottom / left - 레이아웃 - Tailwind CSS

| 클래스                         | 스타일                                                  |
| ------------------------------ | ------------------------------------------------------- |
| `inset-<number>`               | `inset: calc(var(--spacing) * <number>);`               |
| `-inset-<number>`              | `inset: calc(var(--spacing) * -<number>);`              |
| `inset-<fraction>`             | `inset: calc(<fraction> * 100%);`                       |
| `-inset-<fraction>`            | `inset: calc(<fraction> * -100%);`                      |
| `inset-px`                     | `inset: 1px;`                                           |
| `-inset-px`                    | `inset: -1px;`                                          |
| `inset-full`                   | `inset: 100%;`                                          |
| `-inset-full`                  | `inset: -100%;`                                         |
| `inset-auto`                   | `inset: auto;`                                          |
| `inset-(<custom-property>)`    | `inset: var(<custom-property>);`                        |
| `inset-[<value>]`              | `inset: <value>;`                                       |
| `inset-x-<number>`             | `inset-inline: calc(var(--spacing) * <number>);`        |
| `-inset-x-<number>`            | `inset-inline: calc(var(--spacing) * -<number>);`       |
| `inset-x-<fraction>`           | `inset-inline: calc(<fraction> * 100%);`                |
| `-inset-x-<fraction>`          | `inset-inline: calc(<fraction> * -100%);`               |
| `inset-x-px`                   | `inset-inline: 1px;`                                    |
| `-inset-x-px`                  | `inset-inline: -1px;`                                   |
| `inset-x-full`                 | `inset-inline: 100%;`                                   |
| `-inset-x-full`                | `inset-inline: -100%;`                                  |
| `inset-x-auto`                 | `inset-inline: auto;`                                   |
| `inset-x-(<custom-property>)`  | `inset-inline: var(<custom-property>);`                 |
| `inset-x-[<value>]`            | `inset-inline: <value>;`                                |
| `inset-y-<number>`             | `inset-block: calc(var(--spacing) * <number>);`         |
| `-inset-y-<number>`            | `inset-block: calc(var(--spacing) * -<number>);`        |
| `inset-y-<fraction>`           | `inset-block: calc(<fraction> * 100%);`                 |
| `-inset-y-<fraction>`          | `inset-block: calc(<fraction> * -100%);`                |
| `inset-y-px`                   | `inset-block: 1px;`                                     |
| `-inset-y-px`                  | `inset-block: -1px;`                                    |
| `inset-y-full`                 | `inset-block: 100%;`                                    |
| `-inset-y-full`                | `inset-block: -100%;`                                   |
| `inset-y-auto`                 | `inset-block: auto;`                                    |
| `inset-y-(<custom-property>)`  | `inset-block: var(<custom-property>);`                  |
| `inset-y-[<value>]`            | `inset-block: <value>;`                                 |
| `inset-s-<number>`             | `inset-inline-start: calc(var(--spacing) * <number>);`  |
| `-inset-s-<number>`            | `inset-inline-start: calc(var(--spacing) * -<number>);` |
| `inset-s-<fraction>`           | `inset-inline-start: calc(<fraction> * 100%);`          |
| `-inset-s-<fraction>`          | `inset-inline-start: calc(<fraction> * -100%);`         |
| `inset-s-px`                   | `inset-inline-start: 1px;`                              |
| `-inset-s-px`                  | `inset-inline-start: -1px;`                             |
| `inset-s-full`                 | `inset-inline-start: 100%;`                             |
| `-inset-s-full`                | `inset-inline-start: -100%;`                            |
| `inset-s-auto`                 | `inset-inline-start: auto;`                             |
| `inset-s-(<custom-property>)`  | `inset-inline-start: var(<custom-property>);`           |
| `inset-s-[<value>]`            | `inset-inline-start: <value>;`                          |
| `inset-e-<number>`             | `inset-inline-end: calc(var(--spacing) * <number>);`    |
| `-inset-e-<number>`            | `inset-inline-end: calc(var(--spacing) * -<number>);`   |
| `inset-e-<fraction>`           | `inset-inline-end: calc(<fraction> * 100%);`            |
| `-inset-e-<fraction>`          | `inset-inline-end: calc(<fraction> * -100%);`           |
| `inset-e-px`                   | `inset-inline-end: 1px;`                                |
| `-inset-e-px`                  | `inset-inline-end: -1px;`                               |
| `inset-e-full`                 | `inset-inline-end: 100%;`                               |
| `-inset-e-full`                | `inset-inline-end: -100%;`                              |
| `inset-e-auto`                 | `inset-inline-end: auto;`                               |
| `inset-e-(<custom-property>)`  | `inset-inline-end: var(<custom-property>);`             |
| `inset-e-[<value>]`            | `inset-inline-end: <value>;`                            |
| `inset-bs-<number>`            | `inset-block-start: calc(var(--spacing) * <number>);`   |
| `-inset-bs-<number>`           | `inset-block-start: calc(var(--spacing) * -<number>);`  |
| `inset-bs-<fraction>`          | `inset-block-start: calc(<fraction> * 100%);`           |
| `-inset-bs-<fraction>`         | `inset-block-start: calc(<fraction> * -100%);`          |
| `inset-bs-px`                  | `inset-block-start: 1px;`                               |
| `-inset-bs-px`                 | `inset-block-start: -1px;`                              |
| `inset-bs-full`                | `inset-block-start: 100%;`                              |
| `-inset-bs-full`               | `inset-block-start: -100%;`                             |
| `inset-bs-auto`                | `inset-block-start: auto;`                              |
| `inset-bs-(<custom-property>)` | `inset-block-start: var(<custom-property>);`            |
| `inset-bs-[<value>]`           | `inset-block-start: <value>;`                           |
| `inset-be-<number>`            | `inset-block-end: calc(var(--spacing) * <number>);`     |
| `-inset-be-<number>`           | `inset-block-end: calc(var(--spacing) * -<number>);`    |
| `inset-be-<fraction>`          | `inset-block-end: calc(<fraction> * 100%);`             |
| `-inset-be-<fraction>`         | `inset-block-end: calc(<fraction> * -100%);`            |
| `inset-be-px`                  | `inset-block-end: 1px;`                                 |
| `-inset-be-px`                 | `inset-block-end: -1px;`                                |
| `inset-be-full`                | `inset-block-end: 100%;`                                |
| `-inset-be-full`               | `inset-block-end: -100%;`                               |
| `inset-be-auto`                | `inset-block-end: auto;`                                |
| `inset-be-(<custom-property>)` | `inset-block-end: var(<custom-property>);`              |
| `inset-be-[<value>]`           | `inset-block-end: <value>;`                             |
| `top-<number>`                 | `top: calc(var(--spacing) * <number>);`                 |
| `-top-<number>`                | `top: calc(var(--spacing) * -<number>);`                |
| `top-<fraction>`               | `top: calc(<fraction> * 100%);`                         |
| `-top-<fraction>`              | `top: calc(<fraction> * -100%);`                        |
| `top-px`                       | `top: 1px;`                                             |
| `-top-px`                      | `top: -1px;`                                            |
| `top-full`                     | `top: 100%;`                                            |
| `-top-full`                    | `top: -100%;`                                           |
| `top-auto`                     | `top: auto;`                                            |
| `top-(<custom-property>)`      | `top: var(<custom-property>);`                          |
| `top-[<value>]`                | `top: <value>;`                                         |
| `right-<number>`               | `right: calc(var(--spacing) * <number>);`               |
| `-right-<number>`              | `right: calc(var(--spacing) * -<number>);`              |
| `right-<fraction>`             | `right: calc(<fraction> * 100%);`                       |
| `-right-<fraction>`            | `right: calc(<fraction> * -100%);`                      |
| `right-px`                     | `right: 1px;`                                           |
| `-right-px`                    | `right: -1px;`                                          |
| `right-full`                   | `right: 100%;`                                          |
| `-right-full`                  | `right: -100%;`                                         |
| `right-auto`                   | `right: auto;`                                          |
| `right-(<custom-property>)`    | `right: var(<custom-property>);`                        |
| `right-[<value>]`              | `right: <value>;`                                       |
| `bottom-<number>`              | `bottom: calc(var(--spacing) * <number>);`              |
| `-bottom-<number>`             | `bottom: calc(var(--spacing) * -<number>);`             |
| `bottom-<fraction>`            | `bottom: calc(<fraction> * 100%);`                      |
| `-bottom-<fraction>`           | `bottom: calc(<fraction> * -100%);`                     |
| `bottom-px`                    | `bottom: 1px;`                                          |
| `-bottom-px`                   | `bottom: -1px;`                                         |
| `bottom-full`                  | `bottom: 100%;`                                         |
| `-bottom-full`                 | `bottom: -100%;`                                        |
| `bottom-auto`                  | `bottom: auto;`                                         |
| `bottom-(<custom-property>)`   | `bottom: var(<custom-property>);`                       |
| `bottom-[<value>]`             | `bottom: <value>;`                                      |
| `left-<number>`                | `left: calc(var(--spacing) * <number>);`                |
| `-left-<number>`               | `left: calc(var(--spacing) * -<number>);`               |
| `left-<fraction>`              | `left: calc(<fraction> * 100%);`                        |
| `-left-<fraction>`             | `left: calc(<fraction> * -100%);`                       |
| `left-px`                      | `left: 1px;`                                            |
| `-left-px`                     | `left: -1px;`                                           |
| `left-full`                    | `left: 100%;`                                           |
| `-left-full`                   | `left: -100%;`                                          |
| `left-auto`                    | `left: auto;`                                           |
| `left-(<custom-property>)`     | `left: var(<custom-property>);`                         |
| `left-[<value>]`               | `left: <value>;`                                        |

더 보기

## 예제

- 기본 예제

`top-<number>`, `right-<number>`, `bottom-<number>`, `left-<number>`, `inset-<number>` 유틸리티(`top-0`, `bottom-4` 등)를 사용해 [positioned element](https://tailwindcss.com/docs/position)의 가로 또는 세로 위치를 설정합니다:

01

02

03

04

05

06

07

08

09

```
    <!-- Pin to top left corner --><div class="relative size-32 ...">  <div class="absolute top-0 left-0 size-16 ...">01</div></div><!-- Span top edge --><div class="relative size-32 ...">  <div class="absolute inset-x-0 top-0 h-16 ...">02</div></div><!-- Pin to top right corner --><div class="relative size-32 ...">  <div class="absolute top-0 right-0 size-16 ...">03</div></div><!-- Span left edge --><div class="relative size-32 ...">  <div class="absolute inset-y-0 left-0 w-16 ...">04</div></div><!-- Fill entire parent --><div class="relative size-32 ...">  <div class="absolute inset-0 ...">05</div></div><!-- Span right edge --><div class="relative size-32 ...">  <div class="absolute inset-y-0 right-0 w-16 ...">06</div></div><!-- Pin to bottom left corner --><div class="relative size-32 ...">  <div class="absolute bottom-0 left-0 size-16 ...">07</div></div><!-- Span bottom edge --><div class="relative size-32 ...">  <div class="absolute inset-x-0 bottom-0 h-16 ...">08</div></div><!-- Pin to bottom right corner --><div class="relative size-32 ...">  <div class="absolute right-0 bottom-0 size-16 ...">09</div></div>
```

- 음수 값 사용하기

음수 top/right/bottom/left 값을 사용하려면 클래스 이름 앞에 대시를 붙여 음수 값으로 변환하세요:

```
    <div class="relative size-32 ...">  <div class="absolute -top-4 -left-4 size-14 ..."></div></div>
```

- 논리 속성 사용하기

`inset-s-<number>` 또는 `inset-e-<number>` 유틸리티(`inset-s-0`, `inset-e-4` 등)를 사용해 `inset-inline-start`와 `inset-inline-end` [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts)를 설정할 수 있으며, 이는 텍스트 방향에 따라 왼쪽 또는 오른쪽에 매핑됩니다:

Left-to-right

Right-to-left

```
    <div dir="ltr">  <div class="relative size-32 ...">    <div class="absolute inset-s-0 top-0 size-14 ..."></div>  </div>  <div>    <div dir="rtl">      <div class="relative size-32 ...">        <div class="absolute inset-s-0 top-0 size-14 ..."></div>      </div>      <div></div>    </div>  </div></div>
```

더 세밀하게 제어하려면 [LTR and RTL modifiers](https://tailwindcss.com/docs/hover-focus-and-other-states#rtl-support)를 사용해 현재 텍스트 방향에 따라 특정 스타일을 조건부로 적용할 수도 있습니다.

- 사용자 정의 값 사용하기

`inset-[<value>]`, `top-[<value>]` 같은 유틸리티를 사용해 완전히 사용자 정의한 값을 기준으로 위치를 설정할 수 있습니다:

```
    <div class="inset-[3px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `inset-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="inset-(--my-position) ...">  <!-- ... --></div>
```

이것은 `inset-[var(<custom-property>)]`의 축약형으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`inset`, `inset-x`, `inset-y`, `inset-s`, `inset-e`, `inset-bs`, `inset-be`, `top`, `left`, `bottom`, `right` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙여 중간 화면 크기 이상에서만 유틸리티가 적용되게 할 수 있습니다:

```
    <div class="top-4 md:top-6 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 정의

`inset-<number>`, `inset-x-<number>`, `inset-y-<number>`, `inset-s-<number>`, `inset-e-<number>`, `inset-bs-<number>`, `inset-be-<number>`, `top-<number>`, `left-<number>`, `bottom-<number>`, `right-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 구동되며, 이를 자신의 테마에서 사용자 정의할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 사용자 정의에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
