---
title: "min-block-size - 크기 조절 - Tailwind CSS"
description: "min-block-24, min-block-64 같은 min-block-<number> 유틸리티를 사용하면 간격 스케일을 기준으로 요소의 최소 블록 크기를 고정값으로 설정할 수 있습니다:"
---

원문 URL: https://tailwindcss.com/docs/min-block-size

# min-block-size - 크기 조절 - Tailwind CSS

| 클래스                          | 스타일                                             |
| ------------------------------- | -------------------------------------------------- |
| `min-block-<number>`            | `min-block-size: calc(var(--spacing) * <number>);` |
| `min-block-<fraction>`          | `min-block-size: calc(<fraction> * 100%);`         |
| `min-block-px`                  | `min-block-size: 1px;`                             |
| `min-block-full`                | `min-block-size: 100%;`                            |
| `min-block-screen`              | `min-block-size: 100vh;`                           |
| `min-block-dvh`                 | `min-block-size: 100dvh;`                          |
| `min-block-dvw`                 | `min-block-size: 100dvw;`                          |
| `min-block-lvh`                 | `min-block-size: 100lvh;`                          |
| `min-block-lvw`                 | `min-block-size: 100lvw;`                          |
| `min-block-svw`                 | `min-block-size: 100svw;`                          |
| `min-block-svh`                 | `min-block-size: 100svh;`                          |
| `min-block-auto`                | `min-block-size: auto;`                            |
| `min-block-min`                 | `min-block-size: min-content;`                     |
| `min-block-max`                 | `min-block-size: max-content;`                     |
| `min-block-fit`                 | `min-block-size: fit-content;`                     |
| `min-block-lh`                  | `min-block-size: 1lh;`                             |
| `min-block-(<custom-property>)` | `min-block-size: var(<custom-property>);`          |
| `min-block-[<value>]`           | `min-block-size: <value>;`                         |

더 보기

## 예제

- 기본 예제

`min-block-24`, `min-block-64` 같은 `min-block-<number>` 유틸리티를 사용하면 간격 스케일을 기준으로 요소의 최소 블록 크기를 고정값으로 설정할 수 있습니다:

min-block-96

min-block-80

min-block-64

min-block-48

min-block-40

min-block-32

```
    <div class="block-20 ...">  <div class="min-block-80 ...">min-block-80</div>  <div class="min-block-64 ...">min-block-64</div>  <div class="min-block-48 ...">min-block-48</div>  <div class="min-block-40 ...">min-block-40</div>  <div class="min-block-32 ...">min-block-32</div></div>
```

- 백분율 사용하기

`min-block-full` 또는 `min-block-1/2`, `min-block-2/5` 같은 `min-block-<fraction>` 유틸리티를 사용해 요소에 백분율 기반 최소 블록 크기를 지정할 수 있습니다:

min-block-full

min-block-9/10

min-block-3/4

min-block-1/2

min-block-1/3

```
    <div class="min-block-full ...">min-block-full</div><div class="min-block-9/10 ...">min-block-9/10</div><div class="min-block-3/4 ...">min-block-3/4</div><div class="min-block-1/2 ...">min-block-1/2</div><div class="min-block-1/3 ...">min-block-1/3</div>
```

- 사용자 정의 값 사용하기

`min-block-[<value>]` 구문을 사용하면 완전히 사용자 정의한 값을 기준으로 최소 블록 크기를 설정할 수 있습니다:

```
    <div class="min-block-[220px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `min-block-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="min-block-(--my-min-block-size) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `min-block-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `min-block-size` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="block-24 min-block-0 md:min-block-full ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.

## 테마 사용자 정의

`min-block-<number>` 유틸리티는 `--spacing` 테마 변수로 구동되며, 이 변수는 사용자 테마에서 커스터마이즈할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이즈에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
