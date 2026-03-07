---
title: "max-block-size - 크기 - Tailwind CSS"
description: "간격 스케일을 기준으로 요소의 고정 최대 블록 크기를 설정하려면 max-block-24 및 max-block-64 같은 max-block-<number> 유틸리티를 사용하세요:"
---

# max-block-size - 크기 - Tailwind CSS

| 클래스                          | 스타일                                             |
| ------------------------------- | -------------------------------------------------- |
| `max-block-<number>`            | `max-block-size: calc(var(--spacing) * <number>);` |
| `max-block-<fraction>`          | `max-block-size: calc(<fraction> * 100%);`         |
| `max-block-none`                | `max-block-size: none;`                            |
| `max-block-px`                  | `max-block-size: 1px;`                             |
| `max-block-full`                | `max-block-size: 100%;`                            |
| `max-block-screen`              | `max-block-size: 100vh;`                           |
| `max-block-dvh`                 | `max-block-size: 100dvh;`                          |
| `max-block-dvw`                 | `max-block-size: 100dvw;`                          |
| `max-block-lvh`                 | `max-block-size: 100lvh;`                          |
| `max-block-lvw`                 | `max-block-size: 100lvw;`                          |
| `max-block-svh`                 | `max-block-size: 100svh;`                          |
| `max-block-svw`                 | `max-block-size: 100svw;`                          |
| `max-block-min`                 | `max-block-size: min-content;`                     |
| `max-block-max`                 | `max-block-size: max-content;`                     |
| `max-block-fit`                 | `max-block-size: fit-content;`                     |
| `max-block-lh`                  | `max-block-size: 1lh;`                             |
| `max-block-(<custom-property>)` | `max-block-size: var(<custom-property>);`          |
| `max-block-[<value>]`           | `max-block-size: <value>;`                         |

더 보기

## 예제

- 기본 예제

간격 스케일을 기준으로 요소의 고정 최대 블록 크기를 설정하려면 `max-block-24` 및 `max-block-64` 같은 `max-block-<number>` 유틸리티를 사용하세요:

max-block-80

max-block-64

max-block-48

max-block-40

max-block-32

```
    <div class="block-96 ...">  <div class="block-full max-block-80 ...">max-block-80</div>  <div class="block-full max-block-64 ...">max-block-64</div>  <div class="block-full max-block-48 ...">max-block-48</div>  <div class="block-full max-block-40 ...">max-block-40</div>  <div class="block-full max-block-32 ...">max-block-32</div></div>
```

- 백분율 사용

요소에 백분율 기반 최대 블록 크기를 부여하려면 `max-block-full` 또는 `max-block-1/2`, `max-block-2/5` 같은 `max-block-<fraction>` 유틸리티를 사용하세요:

max-block-9/10

max-block-3/4

max-block-1/2

max-block-full

```
    <div class="block-96 ...">  <div class="block-full max-block-9/10 ...">max-block-9/10</div>  <div class="block-full max-block-3/4 ...">max-block-3/4</div>  <div class="block-full max-block-1/2 ...">max-block-1/2</div>  <div class="block-full max-block-full ...">max-block-full</div></div>
```

- 사용자 지정 값 사용

완전히 사용자 지정된 값을 기준으로 최대 블록 크기를 설정하려면 `max-block-[<value>]` 문법을 사용하세요:

```
    <div class="max-block-[220px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `max-block-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="max-block-(--my-max-block-size) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `max-block-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `max-block-size` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <div class="block-48 max-block-full md:max-block-screen ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 지정

`max-block-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 구동되며, 이 변수는 사용자 테마에서 맞춤 설정할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 사용자 지정에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
