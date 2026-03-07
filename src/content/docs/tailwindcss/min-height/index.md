---
title: "min-height - 크기 조절 - Tailwind CSS"
description: "min-h-24, min-h-64 같은 min-h-<number> 유틸리티를 사용해 간격 스케일을 기준으로 요소의 최소 높이를 고정값으로 설정하세요:"
---

원문 URL: https://tailwindcss.com/docs/min-height

# min-height - 크기 조절 - Tailwind CSS

| 클래스                      | 스타일                                         |
| --------------------------- | ---------------------------------------------- |
| `min-h-<number>`            | `min-height: calc(var(--spacing) * <number>);` |
| `min-h-<fraction>`          | `min-height: calc(<fraction> * 100%);`         |
| `min-h-px`                  | `min-height: 1px;`                             |
| `min-h-full`                | `min-height: 100%;`                            |
| `min-h-screen`              | `min-height: 100vh;`                           |
| `min-h-dvh`                 | `min-height: 100dvh;`                          |
| `min-h-dvw`                 | `min-height: 100dvw;`                          |
| `min-h-lvh`                 | `min-height: 100lvh;`                          |
| `min-h-lvw`                 | `min-height: 100lvw;`                          |
| `min-h-svw`                 | `min-height: 100svw;`                          |
| `min-h-svh`                 | `min-height: 100svh;`                          |
| `min-h-auto`                | `min-height: auto;`                            |
| `min-h-min`                 | `min-height: min-content;`                     |
| `min-h-max`                 | `min-height: max-content;`                     |
| `min-h-fit`                 | `min-height: fit-content;`                     |
| `min-h-lh`                  | `min-height: 1lh;`                             |
| `min-h-(<custom-property>)` | `min-height: var(<custom-property>);`          |
| `min-h-[<value>]`           | `min-height: <value>;`                         |

더 보기

## 예제

- 기본 예제

`min-h-24`, `min-h-64` 같은 `min-h-<number>` 유틸리티를 사용해 간격 스케일을 기준으로 요소의 최소 높이를 고정값으로 설정하세요:

min-h-96

min-h-80

min-h-64

min-h-48

min-h-40

min-h-32

min-h-24

```
    <div class="h-20 ...">  <div class="min-h-80 ...">min-h-80</div>  <div class="min-h-64 ...">min-h-64</div>  <div class="min-h-48 ...">min-h-48</div>  <div class="min-h-40 ...">min-h-40</div>  <div class="min-h-32 ...">min-h-32</div>  <div class="min-h-24 ...">min-h-24</div></div>
```

- 백분율 사용하기

`min-h-full` 또는 `min-h-1/2`, `min-h-2/5` 같은 `min-h-<fraction>` 유틸리티를 사용해 요소에 백분율 기반 최소 높이를 지정하세요:

min-h-full

min-h-9/10

min-h-3/4

min-h-1/2

min-h-1/3

```
    <div class="min-h-full ...">min-h-full</div><div class="min-h-9/10 ...">min-h-9/10</div><div class="min-h-3/4 ...">min-h-3/4</div><div class="min-h-1/2 ...">min-h-1/2</div><div class="min-h-1/3 ...">min-h-1/3</div>
```

- 사용자 지정 값 사용하기

`min-h-[<value>]` 문법을 사용해 완전히 사용자 지정한 값을 기준으로 최소 높이를 설정하세요:

```
    <div class="min-h-[220px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `min-h-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="min-h-(--my-min-height) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `min-h-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `min-height` 유틸리티 앞에 붙이면 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="h-24 min-h-0 md:min-h-full ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

`min-h-<number>` 유틸리티는 `--spacing` 테마 변수로 구동되며, 사용자 테마에서 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 자세히 알아보세요。
