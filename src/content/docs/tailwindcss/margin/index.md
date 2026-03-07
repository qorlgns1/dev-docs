---
title: "margin - 간격 - Tailwind CSS"
description: "요소의 모든 방향 margin을 제어하려면 m-<number> 유틸리티(예: m-4, m-8)를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/margin

# margin - 간격 - Tailwind CSS

| 클래스                        | 스타일                                                                                                                                                                                                                                          |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `m-<number>`                  | `margin: calc(var(--spacing) * <number>);`                                                                                                                                                                                                      |
| `-m-<number>`                 | `margin: calc(var(--spacing) * -<number>);`                                                                                                                                                                                                     |
| `m-auto`                      | `margin: auto;`                                                                                                                                                                                                                                 |
| `m-px`                        | `margin: 1px;`                                                                                                                                                                                                                                  |
| `-m-px`                       | `margin: -1px;`                                                                                                                                                                                                                                 |
| `m-(<custom-property>)`       | `margin: var(<custom-property>);`                                                                                                                                                                                                               |
| `m-[<value>]`                 | `margin: <value>;`                                                                                                                                                                                                                              |
| `mx-<number>`                 | `margin-inline: calc(var(--spacing) * <number>);`                                                                                                                                                                                               |
| `-mx-<number>`                | `margin-inline: calc(var(--spacing) * -<number>);`                                                                                                                                                                                              |
| `mx-auto`                     | `margin-inline: auto;`                                                                                                                                                                                                                          |
| `mx-px`                       | `margin-inline: 1px;`                                                                                                                                                                                                                           |
| `-mx-px`                      | `margin-inline: -1px;`                                                                                                                                                                                                                          |
| `mx-(<custom-property>)`      | `margin-inline: var(<custom-property>);`                                                                                                                                                                                                        |
| `mx-[<value>]`                | `margin-inline: <value>;`                                                                                                                                                                                                                       |
| `my-<number>`                 | `margin-block: calc(var(--spacing) * <number>);`                                                                                                                                                                                                |
| `-my-<number>`                | `margin-block: calc(var(--spacing) * -<number>);`                                                                                                                                                                                               |
| `my-auto`                     | `margin-block: auto;`                                                                                                                                                                                                                           |
| `my-px`                       | `margin-block: 1px;`                                                                                                                                                                                                                            |
| `-my-px`                      | `margin-block: -1px;`                                                                                                                                                                                                                           |
| `my-(<custom-property>)`      | `margin-block: var(<custom-property>);`                                                                                                                                                                                                         |
| `my-[<value>]`                | `margin-block: <value>;`                                                                                                                                                                                                                        |
| `ms-<number>`                 | `margin-inline-start: calc(var(--spacing) * <number>);`                                                                                                                                                                                         |
| `-ms-<number>`                | `margin-inline-start: calc(var(--spacing) * -<number>);`                                                                                                                                                                                        |
| `ms-auto`                     | `margin-inline-start: auto;`                                                                                                                                                                                                                    |
| `ms-px`                       | `margin-inline-start: 1px;`                                                                                                                                                                                                                     |
| `-ms-px`                      | `margin-inline-start: -1px;`                                                                                                                                                                                                                    |
| `ms-(<custom-property>)`      | `margin-inline-start: var(<custom-property>);`                                                                                                                                                                                                  |
| `ms-[<value>]`                | `margin-inline-start: <value>;`                                                                                                                                                                                                                 |
| `me-<number>`                 | `margin-inline-end: calc(var(--spacing) * <number>);`                                                                                                                                                                                           |
| `-me-<number>`                | `margin-inline-end: calc(var(--spacing) * -<number>);`                                                                                                                                                                                          |
| `me-auto`                     | `margin-inline-end: auto;`                                                                                                                                                                                                                      |
| `me-px`                       | `margin-inline-end: 1px;`                                                                                                                                                                                                                       |
| `-me-px`                      | `margin-inline-end: -1px;`                                                                                                                                                                                                                      |
| `me-(<custom-property>)`      | `margin-inline-end: var(<custom-property>);`                                                                                                                                                                                                    |
| `me-[<value>]`                | `margin-inline-end: <value>;`                                                                                                                                                                                                                   |
| `mbs-<number>`                | `margin-block-start: calc(var(--spacing) * <number>);`                                                                                                                                                                                          |
| `-mbs-<number>`               | `margin-block-start: calc(var(--spacing) * -<number>);`                                                                                                                                                                                         |
| `mbs-auto`                    | `margin-block-start: auto;`                                                                                                                                                                                                                     |
| `mbs-px`                      | `margin-block-start: 1px;`                                                                                                                                                                                                                      |
| `-mbs-px`                     | `margin-block-start: -1px;`                                                                                                                                                                                                                     |
| `mbs-(<custom-property>)`     | `margin-block-start: var(<custom-property>);`                                                                                                                                                                                                   |
| `mbs-[<value>]`               | `margin-block-start: <value>;`                                                                                                                                                                                                                  |
| `mbe-<number>`                | `margin-block-end: calc(var(--spacing) * <number>);`                                                                                                                                                                                            |
| `-mbe-<number>`               | `margin-block-end: calc(var(--spacing) * -<number>);`                                                                                                                                                                                           |
| `mbe-auto`                    | `margin-block-end: auto;`                                                                                                                                                                                                                       |
| `mbe-px`                      | `margin-block-end: 1px;`                                                                                                                                                                                                                        |
| `-mbe-px`                     | `margin-block-end: -1px;`                                                                                                                                                                                                                       |
| `mbe-(<custom-property>)`     | `margin-block-end: var(<custom-property>);`                                                                                                                                                                                                     |
| `mbe-[<value>]`               | `margin-block-end: <value>;`                                                                                                                                                                                                                    |
| `mt-<number>`                 | `margin-top: calc(var(--spacing) * <number>);`                                                                                                                                                                                                  |
| `-mt-<number>`                | `margin-top: calc(var(--spacing) * -<number>);`                                                                                                                                                                                                 |
| `mt-auto`                     | `margin-top: auto;`                                                                                                                                                                                                                             |
| `mt-px`                       | `margin-top: 1px;`                                                                                                                                                                                                                              |
| `-mt-px`                      | `margin-top: -1px;`                                                                                                                                                                                                                             |
| `mt-(<custom-property>)`      | `margin-top: var(<custom-property>);`                                                                                                                                                                                                           |
| `mt-[<value>]`                | `margin-top: <value>;`                                                                                                                                                                                                                          |
| `mr-<number>`                 | `margin-right: calc(var(--spacing) * <number>);`                                                                                                                                                                                                |
| `-mr-<number>`                | `margin-right: calc(var(--spacing) * -<number>);`                                                                                                                                                                                               |
| `mr-auto`                     | `margin-right: auto;`                                                                                                                                                                                                                           |
| `mr-px`                       | `margin-right: 1px;`                                                                                                                                                                                                                            |
| `-mr-px`                      | `margin-right: -1px;`                                                                                                                                                                                                                           |
| `mr-(<custom-property>)`      | `margin-right: var(<custom-property>);`                                                                                                                                                                                                         |
| `mr-[<value>]`                | `margin-right: <value>;`                                                                                                                                                                                                                        |
| `mb-<number>`                 | `margin-bottom: calc(var(--spacing) * <number>);`                                                                                                                                                                                               |
| `-mb-<number>`                | `margin-bottom: calc(var(--spacing) * -<number>);`                                                                                                                                                                                              |
| `mb-auto`                     | `margin-bottom: auto;`                                                                                                                                                                                                                          |
| `mb-px`                       | `margin-bottom: 1px;`                                                                                                                                                                                                                           |
| `-mb-px`                      | `margin-bottom: -1px;`                                                                                                                                                                                                                          |
| `mb-(<custom-property>)`      | `margin-bottom: var(<custom-property>);`                                                                                                                                                                                                        |
| `mb-[<value>]`                | `margin-bottom: <value>;`                                                                                                                                                                                                                       |
| `ml-<number>`                 | `margin-left: calc(var(--spacing) * <number>);`                                                                                                                                                                                                 |
| `-ml-<number>`                | `margin-left: calc(var(--spacing) * -<number>);`                                                                                                                                                                                                |
| `ml-auto`                     | `margin-left: auto;`                                                                                                                                                                                                                            |
| `ml-px`                       | `margin-left: 1px;`                                                                                                                                                                                                                             |
| `-ml-px`                      | `margin-left: -1px;`                                                                                                                                                                                                                            |
| `ml-(<custom-property>)`      | `margin-left: var(<custom-property>);`                                                                                                                                                                                                          |
| `ml-[<value>]`                | `margin-left: <value>;`                                                                                                                                                                                                                         |
| `space-x-<number>`            | `& > :not(:last-child) { --tw-space-x-reverse: 0; margin-inline-start: calc(calc(var(--spacing) * <number>) * var(--tw-space-x-reverse)); margin-inline-end: calc(calc(var(--spacing) * <number>) * calc(1 - var(--tw-space-x-reverse))); };`   |
| `-space-x-<number>`           | `& > :not(:last-child) { --tw-space-x-reverse: 0; margin-inline-start: calc(calc(var(--spacing) * -<number>) * var(--tw-space-x-reverse)); margin-inline-end: calc(calc(var(--spacing) * -<number>) * calc(1 - var(--tw-space-x-reverse))); };` |
| `space-x-px`                  | `& > :not(:last-child) { --tw-space-x-reverse: 0; margin-inline-start: calc(1px * var(--tw-space-x-reverse)); margin-inline-end: calc(1px * calc(1 - var(--tw-space-x-reverse))); };`                                                           |
| `-space-x-px`                 | `& > :not(:last-child) { --tw-space-x-reverse: 0; margin-inline-start: calc(-1px * var(--tw-space-x-reverse)); margin-inline-end: calc(-1px * calc(1 - var(--tw-space-x-reverse))); };`                                                         |
| `space-x-(<custom-property>)` | `& > :not(:last-child) { --tw-space-x-reverse: 0; margin-inline-start: calc(var(<custom-property>) * var(--tw-space-x-reverse)); margin-inline-end: calc(var(<custom-property>) * calc(1 - var(--tw-space-x-reverse))); };`                     |
| `space-x-[<value>]`           | `& > :not(:last-child) { --tw-space-x-reverse: 0; margin-inline-start: calc(<value> * var(--tw-space-x-reverse)); margin-inline-end: calc(<value> * calc(1 - var(--tw-space-x-reverse))); };`                                                   |
| `space-y-<number>`            | `& > :not(:last-child) { --tw-space-y-reverse: 0; margin-block-start: calc(calc(var(--spacing) * <number>) * var(--tw-space-y-reverse)); margin-block-end: calc(calc(var(--spacing) * <number>) * calc(1 - var(--tw-space-y-reverse))); };`     |
| `-space-y-<number>`           | `& > :not(:last-child) { --tw-space-y-reverse: 0; margin-block-start: calc(calc(var(--spacing) * -<number>) * var(--tw-space-y-reverse)); margin-block-end: calc(calc(var(--spacing) * -<number>) * calc(1 - var(--tw-space-y-reverse))); };`   |
| `space-y-px`                  | `& > :not(:last-child) { --tw-space-y-reverse: 0; margin-block-start: calc(1px * var(--tw-space-y-reverse)); margin-block-end: calc(1px * calc(1 - var(--tw-space-y-reverse))); };`                                                             |
| `-space-y-px`                 | `& > :not(:last-child) { --tw-space-y-reverse: 0; margin-block-start: calc(-1px * var(--tw-space-y-reverse)); margin-block-end: calc(-1px * calc(1 - var(--tw-space-y-reverse))); };`                                                           |
| `space-y-(<custom-property>)` | `& > :not(:last-child) { --tw-space-y-reverse: 0; margin-block-start: calc(var(<custom-property>) * var(--tw-space-y-reverse)); margin-block-end: calc(var(<custom-property>) * calc(1 - var(--tw-space-y-reverse))); };`                       |
| `space-y-[<value>]`           | `& > :not(:last-child) { --tw-space-y-reverse: 0; margin-block-start: calc(<value> * var(--tw-space-y-reverse)); margin-block-end: calc(<value> * calc(1 - var(--tw-space-y-reverse))); };`                                                     |
| `space-x-reverse`             | `& > :not(:last-child)) { --tw-space-x-reverse: 1; }`                                                                                                                                                                                           |
| `space-y-reverse`             | `& > :not(:last-child)) { --tw-space-y-reverse: 1; }`                                                                                                                                                                                           |

더 보기

## 예제

- 기본 예제

요소의 모든 방향 margin을 제어하려면 `m-<number>` 유틸리티(예: `m-4`, `m-8`)를 사용하세요:

m-8

```
    <div class="m-8 ...">m-8</div>
```

- 한쪽 방향에 margin 추가

요소의 한쪽 방향 margin을 제어하려면 `mt-<number>`, `mr-<number>`, `mb-<number>`, `ml-<number>` 유틸리티(예: `ml-2`, `mt-6`)를 사용하세요:

mt-6

mr-4

mb-8

ml-2

```
    <div class="mt-6 ...">mt-6</div><div class="mr-4 ...">mr-4</div><div class="mb-8 ...">mb-8</div><div class="ml-2 ...">ml-2</div>
```

- 가로 margin 추가

요소의 가로 margin을 제어하려면 `mx-<number>` 유틸리티(예: `mx-4`, `mx-8`)를 사용하세요:

mx-8

```
    <div class="mx-8 ...">mx-8</div>
```

- 세로 margin 추가

요소의 세로 margin을 제어하려면 `my-<number>` 유틸리티(예: `my-4`, `my-8`)를 사용하세요:

my-8

```
    <div class="my-8 ...">my-8</div>
```

- 음수 값 사용

음수 margin 값을 사용하려면 클래스 이름 앞에 대시를 붙여 음수 값으로 변환하세요:

-mt-8

```
    <div class="h-16 w-36 bg-sky-400 opacity-20 ..."></div><div class="-mt-8 bg-sky-300 ...">-mt-8</div>
```

- 논리 속성 사용

`margin-inline-start` 및 `margin-inline-end` 논리 속성을 설정하려면 `ms-<number>` 또는 `me-<number>` 유틸리티(예: `ms-4`, `me-8`)를 사용하세요:

왼쪽에서 오른쪽

ms-8

me-8

오른쪽에서 왼쪽

ms-8

me-8

```
    <div>  <div dir="ltr">    <div class="ms-8 ...">ms-8</div>    <div class="me-8 ...">me-8</div>  </div>  <div dir="rtl">    <div class="ms-8 ...">ms-8</div>    <div class="me-8 ...">me-8</div>  </div></div>
```

`mbs-<number>` 및 `mbe-<number>` 유틸리티를 사용하면 `margin-block-start` 및 `margin-block-end` 논리 속성을 설정할 수 있으며, 이 속성들은 writing mode에 따라 위쪽 또는 아래쪽 방향에 매핑됩니다:

```
    <div class="mbs-8 ...">mbs-8</div>
```

- 자식 요소 사이 간격 추가

요소 사이의 간격을 제어하려면 `space-x-<number>` 또는 `space-y-<number>` 유틸리티(예: `space-x-4`, `space-y-8`)를 사용하세요:

01

02

03

```
    <div class="flex space-x-4 ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

#

- 자식 요소 순서 뒤집기

요소가 역순(`flex-row-reverse` 또는 `flex-col-reverse` 등)인 경우, 각 요소의 올바른 방향에 간격이 추가되도록 `space-x-reverse` 또는 `space-y-reverse` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex flex-row-reverse space-x-4 space-x-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

#

- 제한 사항

space 유틸리티는 사실상 그룹에서 마지막 아이템을 제외한 모든 아이템에 margin을 추가하는 단축 문법일 뿐이며, grid, 줄바꿈되는 레이아웃, 또는 자연스러운 DOM 순서가 아닌 복잡한 사용자 정의 순서로 자식이 렌더링되는 상황 같은 복잡한 케이스를 처리하도록 설계되지 않았습니다.

이런 경우에는 가능하면 [gap utilities](https://tailwindcss.com/docs/gap)를 사용하는 것이 더 좋고, 또는 부모에 대응되는 음수 margin을 주면서 모든 요소에 margin을 추가하는 방식이 좋습니다.

또한 space 유틸리티는 [divide utilities](https://tailwindcss.com/docs/border-width#between-children)와 함께 동작하도록 설계되지 않았습니다. 이런 경우에는 대신 자식 요소에 margin/padding 유틸리티를 추가하는 것을 고려하세요.

- 사용자 지정 값 사용

완전히 사용자 지정한 값으로 margin을 설정하려면 `m-[<value>]`, `mx-[<value>]`, `mb-[<value>]` 같은 유틸리티를 사용하세요:

```
    <div class="m-[5px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `m-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="m-(--my-margin) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `m-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `margin` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="mt-4 md:mt-8 ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 알아보세요.

## 테마 사용자 정의

`m-<number>`, `mx-<number>`, `my-<number>`, `ms-<number>`, `me-<number>`, `mbs-<number>`, `mbe-<number>`, `mt-<number>`, `mr-<number>`, `mb-<number>`, `ml-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 동작하며, 이 변수는 사용자 테마에서 커스터마이즈할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일을 커스터마이즈하는 방법은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 더 자세히 알아보세요.
