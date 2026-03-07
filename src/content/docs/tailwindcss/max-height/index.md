---
title: "max-height - 크기 - Tailwind CSS"
description: "max-h-24, max-h-64 같은 max-h-<number> 유틸리티를 사용하면 간격 스케일을 기준으로 요소의 고정 최대 높이를 설정할 수 있습니다:"
---

# max-height - 크기 - Tailwind CSS

| 클래스                      | 스타일                                         |
| --------------------------- | ---------------------------------------------- |
| `max-h-<number>`            | `max-height: calc(var(--spacing) * <number>);` |
| `max-h-<fraction>`          | `max-height: calc(<fraction> * 100%);`         |
| `max-h-none`                | `max-height: none;`                            |
| `max-h-px`                  | `max-height: 1px;`                             |
| `max-h-full`                | `max-height: 100%;`                            |
| `max-h-screen`              | `max-height: 100vh;`                           |
| `max-h-dvh`                 | `max-height: 100dvh;`                          |
| `max-h-dvw`                 | `max-height: 100dvw;`                          |
| `max-h-lvh`                 | `max-height: 100lvh;`                          |
| `max-h-lvw`                 | `max-height: 100lvw;`                          |
| `max-h-svh`                 | `max-height: 100svh;`                          |
| `max-h-svw`                 | `max-height: 100svw;`                          |
| `max-h-min`                 | `max-height: min-content;`                     |
| `max-h-max`                 | `max-height: max-content;`                     |
| `max-h-fit`                 | `max-height: fit-content;`                     |
| `max-h-lh`                  | `max-height: 1lh;`                             |
| `max-h-(<custom-property>)` | `max-height: var(<custom-property>);`          |
| `max-h-[<value>]`           | `max-height: <value>;`                         |

더 보기

## 예제

- 기본 예제

`max-h-24`, `max-h-64` 같은 `max-h-<number>` 유틸리티를 사용하면 간격 스케일을 기준으로 요소의 고정 최대 높이를 설정할 수 있습니다:

max-h-80

max-h-64

max-h-48

max-h-40

max-h-32

max-h-24

```
    <div class="h-96 ...">  <div class="h-full max-h-80 ...">max-h-80</div>  <div class="h-full max-h-64 ...">max-h-64</div>  <div class="h-full max-h-48 ...">max-h-48</div>  <div class="h-full max-h-40 ...">max-h-40</div>  <div class="h-full max-h-32 ...">max-h-32</div>  <div class="h-full max-h-24 ...">max-h-24</div></div>
```

- 백분율 사용하기

`max-h-full` 또는 `max-h-1/2`, `max-h-2/5` 같은 `max-h-<fraction>` 유틸리티를 사용하면 요소에 백분율 기반 최대 높이를 적용할 수 있습니다:

max-h-9/10

max-h-3/4

max-h-1/2

max-h-1/4

max-h-full

```
    <div class="h-96 ...">  <div class="h-full max-h-9/10 ...">max-h-9/10</div>  <div class="h-full max-h-3/4 ...">max-h-3/4</div>  <div class="h-full max-h-1/2 ...">max-h-1/2</div>  <div class="h-full max-h-1/4 ...">max-h-1/4</div>  <div class="h-full max-h-full ...">max-h-full</div></div>
```

- 사용자 정의 값 사용하기

`max-h-[<value>]` 구문을 사용하면 완전히 사용자 정의한 값으로 최대 높이를 설정할 수 있습니다:

```
    <div class="max-h-[220px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `max-h-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="max-h-(--my-max-height) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `max-h-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `max-height` 유틸리티 앞에 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="h-48 max-h-full md:max-h-screen ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 지정

`max-h-<number>` 유틸리티는 `--spacing` 테마 변수로 구동되며, 사용자 테마에서 이 값을 커스터마이즈할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
