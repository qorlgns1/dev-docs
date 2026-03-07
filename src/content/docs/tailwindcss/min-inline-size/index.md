---
title: "min-inline-size - 크기 조절 - Tailwind CSS"
description: "간격 스케일을 기준으로 요소에 고정 최소 인라인 크기를 설정하려면 min-inline-24, min-inline-64 같은 min-inline-<number> 유틸리티를 사용하세요:"
---

소스 URL: https://tailwindcss.com/docs/min-inline-size

# min-inline-size - 크기 조절 - Tailwind CSS

| 클래스                           | 스타일                                                        |
| -------------------------------- | ------------------------------------------------------------- |
| `min-inline-<number>`            | `min-inline-size: calc(var(--spacing) * <number>);`           |
| `min-inline-<fraction>`          | `min-inline-size: calc(<fraction> * 100%);`                   |
| `min-inline-3xs`                 | `min-inline-size: var(--container-3xs); /* 16rem (256px) */`  |
| `min-inline-2xs`                 | `min-inline-size: var(--container-2xs); /* 18rem (288px) */`  |
| `min-inline-xs`                  | `min-inline-size: var(--container-xs); /* 20rem (320px) */`   |
| `min-inline-sm`                  | `min-inline-size: var(--container-sm); /* 24rem (384px) */`   |
| `min-inline-md`                  | `min-inline-size: var(--container-md); /* 28rem (448px) */`   |
| `min-inline-lg`                  | `min-inline-size: var(--container-lg); /* 32rem (512px) */`   |
| `min-inline-xl`                  | `min-inline-size: var(--container-xl); /* 36rem (576px) */`   |
| `min-inline-2xl`                 | `min-inline-size: var(--container-2xl); /* 42rem (672px) */`  |
| `min-inline-3xl`                 | `min-inline-size: var(--container-3xl); /* 48rem (768px) */`  |
| `min-inline-4xl`                 | `min-inline-size: var(--container-4xl); /* 56rem (896px) */`  |
| `min-inline-5xl`                 | `min-inline-size: var(--container-5xl); /* 64rem (1024px) */` |
| `min-inline-6xl`                 | `min-inline-size: var(--container-6xl); /* 72rem (1152px) */` |
| `min-inline-7xl`                 | `min-inline-size: var(--container-7xl); /* 80rem (1280px) */` |
| `min-inline-auto`                | `min-inline-size: auto;`                                      |
| `min-inline-px`                  | `min-inline-size: 1px;`                                       |
| `min-inline-full`                | `min-inline-size: 100%;`                                      |
| `min-inline-screen`              | `min-inline-size: 100vw;`                                     |
| `min-inline-dvw`                 | `min-inline-size: 100dvw;`                                    |
| `min-inline-dvh`                 | `min-inline-size: 100dvh;`                                    |
| `min-inline-lvw`                 | `min-inline-size: 100lvw;`                                    |
| `min-inline-lvh`                 | `min-inline-size: 100lvh;`                                    |
| `min-inline-svw`                 | `min-inline-size: 100svw;`                                    |
| `min-inline-svh`                 | `min-inline-size: 100svh;`                                    |
| `min-inline-min`                 | `min-inline-size: min-content;`                               |
| `min-inline-max`                 | `min-inline-size: max-content;`                               |
| `min-inline-fit`                 | `min-inline-size: fit-content;`                               |
| `min-inline-(<custom-property>)` | `min-inline-size: var(<custom-property>);`                    |
| `min-inline-[<value>]`           | `min-inline-size: <value>;`                                   |

더 보기

## 예제

- 기본 예제

간격 스케일을 기준으로 요소에 고정 최소 인라인 크기를 설정하려면 `min-inline-24`, `min-inline-64` 같은 `min-inline-<number>` 유틸리티를 사용하세요:

min-inline-80

min-inline-64

min-inline-48

min-inline-40

min-inline-32

min-inline-24

```
    <div class="inline-20 ...">  <div class="min-inline-80 ...">min-inline-80</div>  <div class="min-inline-64 ...">min-inline-64</div>  <div class="min-inline-48 ...">min-inline-48</div>  <div class="min-inline-40 ...">min-inline-40</div>  <div class="min-inline-32 ...">min-inline-32</div>  <div class="min-inline-24 ...">min-inline-24</div></div>
```

- 백분율 사용하기

요소에 백분율 기반 최소 인라인 크기를 지정하려면 `min-inline-full` 또는 `min-inline-1/2`, `min-inline-2/5` 같은 `min-inline-<fraction>` 유틸리티를 사용하세요:

min-inline-3/4

inline-full

```
    <div class="flex ...">  <div class="min-inline-3/4 ...">min-inline-3/4</div>  <div class="inline-full ...">inline-full</div></div>
```

- 컨테이너 스케일 사용하기

컨테이너 스케일을 기준으로 요소에 고정 최소 인라인 크기를 설정하려면 `min-inline-sm`, `min-inline-xl` 같은 유틸리티를 사용하세요:

min-inline-lg

min-inline-md

min-inline-sm

min-inline-xs

min-inline-2xs

min-inline-3xs

```
    <div class="inline-40 ...">  <div class="min-inline-lg ...">min-inline-lg</div>  <div class="min-inline-md ...">min-inline-md</div>  <div class="min-inline-sm ...">min-inline-sm</div>  <div class="min-inline-xs ...">min-inline-xs</div>  <div class="min-inline-2xs ...">min-inline-2xs</div>  <div class="min-inline-3xs ...">min-inline-3xs</div></div>
```

- 사용자 정의 값 사용하기

완전히 사용자 정의한 값을 기준으로 최소 인라인 크기를 설정하려면 `min-inline-[<value>]` 구문을 사용하세요:

```
    <div class="min-inline-[220px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `min-inline-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="min-inline-(--my-min-inline-size) ...">  <!-- ... --></div>
```

이 구문은 `var()` 함수를 자동으로 추가해 주는 `min-inline-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `min-inline-size` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="inline-24 min-inline-full md:min-inline-0 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

`min-inline-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 동작하며, 이 변수는 사용자 테마에서 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징에 대해서는 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 자세히 알아보세요.
