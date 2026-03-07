---
title: "min-width - 크기 조절 - Tailwind CSS"
description: "min-w-24, min-w-64 같은 min-w-<number> 유틸리티를 사용해 간격 스케일을 기준으로 요소의 고정 최소 너비를 설정하세요:"
---

Source URL: https://tailwindcss.com/docs/min-width

# min-width - 크기 조절 - Tailwind CSS

| 클래스                      | 스타일                                                  |
| --------------------------- | ------------------------------------------------------- |
| `min-w-<number>`            | `min-width: calc(var(--spacing) * <number>);`           |
| `min-w-<fraction>`          | `min-width: calc(<fraction> * 100%);`                   |
| `min-w-3xs`                 | `min-width: var(--container-3xs); /* 16rem (256px) */`  |
| `min-w-2xs`                 | `min-width: var(--container-2xs); /* 18rem (288px) */`  |
| `min-w-xs`                  | `min-width: var(--container-xs); /* 20rem (320px) */`   |
| `min-w-sm`                  | `min-width: var(--container-sm); /* 24rem (384px) */`   |
| `min-w-md`                  | `min-width: var(--container-md); /* 28rem (448px) */`   |
| `min-w-lg`                  | `min-width: var(--container-lg); /* 32rem (512px) */`   |
| `min-w-xl`                  | `min-width: var(--container-xl); /* 36rem (576px) */`   |
| `min-w-2xl`                 | `min-width: var(--container-2xl); /* 42rem (672px) */`  |
| `min-w-3xl`                 | `min-width: var(--container-3xl); /* 48rem (768px) */`  |
| `min-w-4xl`                 | `min-width: var(--container-4xl); /* 56rem (896px) */`  |
| `min-w-5xl`                 | `min-width: var(--container-5xl); /* 64rem (1024px) */` |
| `min-w-6xl`                 | `min-width: var(--container-6xl); /* 72rem (1152px) */` |
| `min-w-7xl`                 | `min-width: var(--container-7xl); /* 80rem (1280px) */` |
| `min-w-auto`                | `min-width: auto;`                                      |
| `min-w-px`                  | `min-width: 1px;`                                       |
| `min-w-full`                | `min-width: 100%;`                                      |
| `min-w-screen`              | `min-width: 100vw;`                                     |
| `min-w-dvw`                 | `min-width: 100dvw;`                                    |
| `min-w-dvh`                 | `min-width: 100dvh;`                                    |
| `min-w-lvw`                 | `min-width: 100lvw;`                                    |
| `min-w-lvh`                 | `min-width: 100lvh;`                                    |
| `min-w-svw`                 | `min-width: 100svw;`                                    |
| `min-w-svh`                 | `min-width: 100svh;`                                    |
| `min-w-min`                 | `min-width: min-content;`                               |
| `min-w-max`                 | `min-width: max-content;`                               |
| `min-w-fit`                 | `min-width: fit-content;`                               |
| `min-w-(<custom-property>)` | `min-width: var(<custom-property>);`                    |
| `min-w-[<value>]`           | `min-width: <value>;`                                   |

더 보기

## 예제

- 기본 예제

`min-w-24`, `min-w-64` 같은 `min-w-<number>` 유틸리티를 사용해 간격 스케일을 기준으로 요소의 고정 최소 너비를 설정하세요:

min-w-80

min-w-64

min-w-48

min-w-40

min-w-32

min-w-24

```
    <div class="w-20 ...">  <div class="min-w-80 ...">min-w-80</div>  <div class="min-w-64 ...">min-w-64</div>  <div class="min-w-48 ...">min-w-48</div>  <div class="min-w-40 ...">min-w-40</div>  <div class="min-w-32 ...">min-w-32</div>  <div class="min-w-24 ...">min-w-24</div></div>
```

- 백분율 사용하기

`min-w-full` 또는 `min-w-1/2`, `min-w-2/5` 같은 `min-w-<fraction>` 유틸리티를 사용해 요소에 백분율 기반 최소 너비를 지정하세요:

min-w-3/4

w-full

```
    <div class="flex ...">  <div class="min-w-3/4 ...">min-w-3/4</div>  <div class="w-full ...">w-full</div></div>
```

- 컨테이너 스케일 사용하기

`min-w-sm`, `min-w-xl` 같은 유틸리티를 사용해 컨테이너 스케일을 기준으로 요소의 고정 최소 너비를 설정하세요:

min-w-lg

min-w-md

min-w-sm

min-w-xs

min-w-2xs

min-w-3xs

```
    <div class="w-40 ...">  <div class="min-w-lg ...">min-w-lg</div>  <div class="min-w-md ...">min-w-md</div>  <div class="min-w-sm ...">min-w-sm</div>  <div class="min-w-xs ...">min-w-xs</div>  <div class="min-w-2xs ...">min-w-2xs</div>  <div class="min-w-3xs ...">min-w-3xs</div></div>
```

- 사용자 지정 값 사용하기

`min-w-[<value>]` 문법을 사용해 완전히 사용자 지정한 값을 기준으로 최소 너비를 설정하세요:

```
    <div class="min-w-[220px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `min-w-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="min-w-(--my-min-width) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `min-w-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `min-width` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="w-24 min-w-full md:min-w-0 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

`min-w-<number>` 유틸리티는 `--spacing` 테마 변수로 구동되며, 직접 만든 테마에서 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
