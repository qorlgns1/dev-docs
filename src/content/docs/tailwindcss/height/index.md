---
title: "height - 크기 조절 - Tailwind CSS"
description: "h-24, h-64 같은 h-<number> 유틸리티를 사용해 간격 스케일을 기준으로 요소의 높이를 고정값으로 설정합니다:"
---

# height - 크기 조절 - Tailwind CSS

| 클래스                     | 스타일                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------- |
| `h-<number>`               | `height: calc(var(--spacing) * <number>);`                                         |
| `h-<fraction>`             | `height: calc(<fraction> * 100%);`                                                 |
| `h-auto`                   | `height: auto;`                                                                    |
| `h-px`                     | `height: 1px;`                                                                     |
| `h-full`                   | `height: 100%;`                                                                    |
| `h-screen`                 | `height: 100vh;`                                                                   |
| `h-dvh`                    | `height: 100dvh;`                                                                  |
| `h-dvw`                    | `height: 100dvw;`                                                                  |
| `h-lvh`                    | `height: 100lvh;`                                                                  |
| `h-lvw`                    | `height: 100lvw;`                                                                  |
| `h-svh`                    | `height: 100svh;`                                                                  |
| `h-svw`                    | `height: 100svw;`                                                                  |
| `h-min`                    | `height: min-content;`                                                             |
| `h-max`                    | `height: max-content;`                                                             |
| `h-fit`                    | `height: fit-content;`                                                             |
| `h-lh`                     | `height: 1lh;`                                                                     |
| `h-(<custom-property>)`    | `height: var(<custom-property>);`                                                  |
| `h-[<value>]`              | `height: <value>;`                                                                 |
| `size-<number>`            | `width: calc(var(--spacing) * <number>); height: calc(var(--spacing) * <number>);` |
| `size-<fraction>`          | `width: calc(<fraction> * 100%); height: calc(<fraction> * 100%);`                 |
| `size-auto`                | `width: auto; height: auto;`                                                       |
| `size-px`                  | `width: 1px; height: 1px;`                                                         |
| `size-full`                | `width: 100%; height: 100%;`                                                       |
| `size-dvw`                 | `width: 100dvw; height: 100dvw;`                                                   |
| `size-dvh`                 | `width: 100dvh; height: 100dvh;`                                                   |
| `size-lvw`                 | `width: 100lvw; height: 100lvw;`                                                   |
| `size-lvh`                 | `width: 100lvh; height: 100lvh;`                                                   |
| `size-svw`                 | `width: 100svw; height: 100svw;`                                                   |
| `size-svh`                 | `width: 100svh; height: 100svh;`                                                   |
| `size-min`                 | `width: min-content; height: min-content;`                                         |
| `size-max`                 | `width: max-content; height: max-content;`                                         |
| `size-fit`                 | `width: fit-content; height: fit-content;`                                         |
| `size-(<custom-property>)` | `width: var(<custom-property>); height: var(<custom-property>);`                   |
| `size-[<value>]`           | `width: <value>; height: <value>;`                                                 |

더 보기

## 예제

- 기본 예제

`h-24`, `h-64` 같은 `h-<number>` 유틸리티를 사용해 간격 스케일을 기준으로 요소의 높이를 고정값으로 설정합니다:

h-96

h-80

h-64

h-48

h-40

h-32

h-24

```
    <div class="h-96 ...">h-96</div><div class="h-80 ...">h-80</div><div class="h-64 ...">h-64</div><div class="h-48 ...">h-48</div><div class="h-40 ...">h-40</div><div class="h-32 ...">h-32</div><div class="h-24 ...">h-24</div>
```

- 백분율 사용하기

`h-full`, `h-1/2`, `h-2/5` 같은 `h-<fraction>` 유틸리티를 사용해 요소에 백분율 기반 높이를 지정합니다:

h-full

h-9/10

h-3/4

h-1/2

h-1/3

```
    <div class="h-full ...">h-full</div><div class="h-9/10 ...">h-9/10</div><div class="h-3/4 ...">h-3/4</div><div class="h-1/2 ...">h-1/2</div><div class="h-1/3 ...">h-1/3</div>
```

- 뷰포트에 맞추기

`h-screen` 유틸리티를 사용해 요소가 뷰포트 전체 높이를 차지하도록 만듭니다:

```
    <div class="h-screen">  <!-- ... --></div>
```

- 동적 뷰포트에 맞추기

`h-dvh` 유틸리티를 사용해 요소가 뷰포트 전체 높이를 차지하도록 만듭니다. 이 높이는 브라우저 UI가 확장되거나 축소될 때 함께 변합니다:

뷰포트를 스크롤해 뷰포트 높이 변화 확인

tailwindcss.com

h-dvh

```
    <div class="h-dvh">  <!-- ... --></div>
```

- 큰 뷰포트에 맞추기

`h-lvh` 유틸리티를 사용해 요소 높이를 뷰포트의 가능한 최대 높이로 설정합니다:

뷰포트를 스크롤해 뷰포트 높이 변화 확인

tailwindcss.com

h-lvh

```
    <div class="h-lvh">  <!-- ... --></div>
```

- 작은 뷰포트에 맞추기

`h-svh` 유틸리티를 사용해 요소 높이를 뷰포트의 가능한 최소 높이로 설정합니다:

뷰포트를 스크롤해 뷰포트 높이 변화 확인

tailwindcss.com

h-svh

```
    <div class="h-svh">  <!-- ... --></div>
```

- 너비와 높이를 함께 설정하기

`size-px`, `size-4`, `size-full` 같은 유틸리티를 사용해 요소의 너비와 높이를 동시에 설정합니다:

size-16

size-20

size-24

size-32

size-40

```
    <div class="size-16 ...">size-16</div><div class="size-20 ...">size-20</div><div class="size-24 ...">size-24</div><div class="size-32 ...">size-32</div><div class="size-40 ...">size-40</div>
```

- 사용자 지정 값 사용하기

`h-[<value>]` 문법을 사용해 완전히 사용자 지정한 값으로 높이를 설정합니다:

```
    <div class="h-[32rem] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `h-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="h-(--my-height) ...">  <!-- ... --></div>
```

이 문법은 `var()` 함수를 자동으로 추가해 주는 `h-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`height` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 이상 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="h-1/2 md:h-full ...">  <!-- ... --></div>
```

변형 사용 방법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 확인하세요.

## 테마 커스터마이징

`h-<number>`와 `size-<number>` 유틸리티는 `--spacing` 테마 변수로 구동되며, 이를 사용자 테마에서 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
