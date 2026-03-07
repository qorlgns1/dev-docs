---
title: "block-size - 크기 조절 - Tailwind CSS"
description: "block-24, block-64 같은 block-<number> 유틸리티를 사용해 spacing 스케일을 기준으로 요소의 고정 블록 크기를 설정하세요:"
---

# block-size - 크기 조절 - Tailwind CSS

| 클래스                      | 스타일                                         |
| --------------------------- | ---------------------------------------------- |
| `block-<number>`            | `block-size: calc(var(--spacing) * <number>);` |
| `block-<fraction>`          | `block-size: calc(<fraction> * 100%);`         |
| `block-auto`                | `block-size: auto;`                            |
| `block-px`                  | `block-size: 1px;`                             |
| `block-full`                | `block-size: 100%;`                            |
| `block-screen`              | `block-size: 100vh;`                           |
| `block-dvh`                 | `block-size: 100dvh;`                          |
| `block-dvw`                 | `block-size: 100dvw;`                          |
| `block-lvh`                 | `block-size: 100lvh;`                          |
| `block-lvw`                 | `block-size: 100lvw;`                          |
| `block-svh`                 | `block-size: 100svh;`                          |
| `block-svw`                 | `block-size: 100svw;`                          |
| `block-min`                 | `block-size: min-content;`                     |
| `block-max`                 | `block-size: max-content;`                     |
| `block-fit`                 | `block-size: fit-content;`                     |
| `block-lh`                  | `block-size: 1lh;`                             |
| `block-(<custom-property>)` | `block-size: var(<custom-property>);`          |
| `block-[<value>]`           | `block-size: <value>;`                         |

더 보기

## 예제

- 기본 예제

`block-24`, `block-64` 같은 `block-<number>` 유틸리티를 사용해 spacing 스케일을 기준으로 요소의 고정 블록 크기를 설정하세요:

block-96

block-80

block-64

block-48

block-40

block-32

block-24

```
    <div class="block-96 ...">block-96</div><div class="block-80 ...">block-80</div><div class="block-64 ...">block-64</div><div class="block-48 ...">block-48</div><div class="block-40 ...">block-40</div><div class="block-32 ...">block-32</div><div class="block-24 ...">block-24</div>
```

- 백분율 사용하기

`block-full` 또는 `block-1/2`, `block-2/5` 같은 `block-<fraction>` 유틸리티를 사용해 요소에 백분율 기반 블록 크기를 지정하세요:

block-full

block-9/10

block-3/4

block-1/2

block-1/3

```
    <div class="block-full ...">block-full</div><div class="block-9/10 ...">block-9/10</div><div class="block-3/4 ...">block-3/4</div><div class="block-1/2 ...">block-1/2</div><div class="block-1/3 ...">block-1/3</div>
```

- 뷰포트에 맞추기

`block-screen` 유틸리티를 사용해 요소가 뷰포트의 전체 블록 크기를 차지하도록 만드세요:

```
    <div class="block-screen">  <!-- ... --></div>
```

- 동적 뷰포트에 맞추기

`block-dvh` 유틸리티를 사용해 요소가 뷰포트의 전체 블록 크기를 차지하도록 만드세요. 이 크기는 브라우저 UI가 확장되거나 축소될 때 함께 변경됩니다:

```
    <div class="block-dvh">  <!-- ... --></div>
```

- 큰 뷰포트에 맞추기

`block-lvh` 유틸리티를 사용해 요소의 블록 크기를 뷰포트에서 가능한 가장 큰 크기로 설정하세요:

```
    <div class="block-lvh">  <!-- ... --></div>
```

- 작은 뷰포트에 맞추기

`block-svh` 유틸리티를 사용해 요소의 블록 크기를 뷰포트에서 가능한 가장 작은 크기로 설정하세요:

```
    <div class="block-svh">  <!-- ... --></div>
```

- 사용자 정의 값 사용하기

`block-[<value>]` 문법을 사용해 완전히 사용자 정의한 값으로 블록 크기를 설정하세요:

```
    <div class="block-[32rem] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `block-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="block-(--my-block-size) ...">  <!-- ... --></div>
```

이 문법은 `var()` 함수를 자동으로 추가해 주는 `block-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `block-size` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="block-1/2 md:block-full ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 정의

`block-<number>` 유틸리티는 `--spacing` 테마 변수로 구동되며, 자신의 테마에서 사용자 정의할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

spacing 스케일 사용자 정의에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
