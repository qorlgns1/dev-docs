---
title: "max-width - 크기 조절 - Tailwind CSS"
description: "max-w-24 및 max-w-64 같은 max-w-<number> 유틸리티를 사용해 간격 스케일을 기준으로 요소의 고정 최대 너비를 설정하세요:"
---

출처 URL: https://tailwindcss.com/docs/max-width

# max-width - 크기 조절 - Tailwind CSS

| 클래스                      | 스타일                                                                                                                                                                                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max-w-<number>`            | `max-width: calc(var(--spacing) * <number>);`                                                                                                                                                                                                        |
| `max-w-<fraction>`          | `max-width: calc(<fraction> * 100%);`                                                                                                                                                                                                                |
| `max-w-3xs`                 | `max-width: var(--container-3xs); /* 16rem (256px) */`                                                                                                                                                                                               |
| `max-w-2xs`                 | `max-width: var(--container-2xs); /* 18rem (288px) */`                                                                                                                                                                                               |
| `max-w-xs`                  | `max-width: var(--container-xs); /* 20rem (320px) */`                                                                                                                                                                                                |
| `max-w-sm`                  | `max-width: var(--container-sm); /* 24rem (384px) */`                                                                                                                                                                                                |
| `max-w-md`                  | `max-width: var(--container-md); /* 28rem (448px) */`                                                                                                                                                                                                |
| `max-w-lg`                  | `max-width: var(--container-lg); /* 32rem (512px) */`                                                                                                                                                                                                |
| `max-w-xl`                  | `max-width: var(--container-xl); /* 36rem (576px) */`                                                                                                                                                                                                |
| `max-w-2xl`                 | `max-width: var(--container-2xl); /* 42rem (672px) */`                                                                                                                                                                                               |
| `max-w-3xl`                 | `max-width: var(--container-3xl); /* 48rem (768px) */`                                                                                                                                                                                               |
| `max-w-4xl`                 | `max-width: var(--container-4xl); /* 56rem (896px) */`                                                                                                                                                                                               |
| `max-w-5xl`                 | `max-width: var(--container-5xl); /* 64rem (1024px) */`                                                                                                                                                                                              |
| `max-w-6xl`                 | `max-width: var(--container-6xl); /* 72rem (1152px) */`                                                                                                                                                                                              |
| `max-w-7xl`                 | `max-width: var(--container-7xl); /* 80rem (1280px) */`                                                                                                                                                                                              |
| `max-w-none`                | `max-width: none;`                                                                                                                                                                                                                                   |
| `max-w-px`                  | `max-width: 1px;`                                                                                                                                                                                                                                    |
| `max-w-full`                | `max-width: 100%;`                                                                                                                                                                                                                                   |
| `max-w-dvw`                 | `max-width: 100dvw;`                                                                                                                                                                                                                                 |
| `max-w-dvh`                 | `max-width: 100dvh;`                                                                                                                                                                                                                                 |
| `max-w-lvw`                 | `max-width: 100lvw;`                                                                                                                                                                                                                                 |
| `max-w-lvh`                 | `max-width: 100lvh;`                                                                                                                                                                                                                                 |
| `max-w-svw`                 | `max-width: 100svw;`                                                                                                                                                                                                                                 |
| `max-w-svh`                 | `max-width: 100svh;`                                                                                                                                                                                                                                 |
| `max-w-screen`              | `max-width: 100vw;`                                                                                                                                                                                                                                  |
| `max-w-min`                 | `max-width: min-content;`                                                                                                                                                                                                                            |
| `max-w-max`                 | `max-width: max-content;`                                                                                                                                                                                                                            |
| `max-w-fit`                 | `max-width: fit-content;`                                                                                                                                                                                                                            |
| `container`                 | `width: 100%; @media (width >= 40rem) { max-width: 40rem; } @media (width >= 48rem) { max-width: 48rem; } @media (width >= 64rem) { max-width: 64rem; } @media (width >= 80rem) { max-width: 80rem; } @media (width >= 96rem) { max-width: 96rem; }` |
| `max-w-(<custom-property>)` | `max-width: var(<custom-property>);`                                                                                                                                                                                                                 |
| `max-w-[<value>]`           | `max-width: <value>;`                                                                                                                                                                                                                                |

더 보기

## 예제

- 기본 예제

`max-w-24` 및 `max-w-64` 같은 `max-w-<number>` 유틸리티를 사용해 간격 스케일을 기준으로 요소의 고정 최대 너비를 설정하세요:

예제를 리사이즈해 예상 동작을 확인하세요

max-w-96

max-w-80

max-w-64

max-w-48

max-w-40

max-w-32

max-w-24

```
    <div class="w-full max-w-96 ...">max-w-96</div><div class="w-full max-w-80 ...">max-w-80</div><div class="w-full max-w-64 ...">max-w-64</div><div class="w-full max-w-48 ...">max-w-48</div><div class="w-full max-w-40 ...">max-w-40</div><div class="w-full max-w-32 ...">max-w-32</div><div class="w-full max-w-24 ...">max-w-24</div>
```

- 백분율 사용

`max-w-full` 또는 `max-w-1/2`, `max-w-2/5` 같은 `max-w-<fraction>` 유틸리티를 사용해 요소에 백분율 기반 최대 너비를 지정하세요:

예제를 리사이즈해 예상 동작을 확인하세요

max-w-9/10

max-w-3/4

max-w-1/2

max-w-1/3

```
    <div class="w-full max-w-9/10 ...">max-w-9/10</div><div class="w-full max-w-3/4 ...">max-w-3/4</div><div class="w-full max-w-1/2 ...">max-w-1/2</div><div class="w-full max-w-1/3 ...">max-w-1/3</div>
```

- 컨테이너 스케일 사용

`max-w-sm`, `max-w-xl` 같은 유틸리티를 사용해 컨테이너 스케일을 기준으로 요소의 고정 최대 너비를 설정하세요:

예제를 리사이즈해 예상 동작을 확인하세요

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

Andrew Alfred

이동 비서 보좌관

```
    <div class="max-w-md ...">  <!-- ... --></div>
```

- 브레이크포인트 컨테이너 사용

`container` 유틸리티를 사용하면 요소의 최대 너비를 현재 브레이크포인트의 `min-width`에 맞출 수 있습니다. 완전히 유동적인 뷰포트를 수용하려 하기보다 고정된 화면 크기 집합을 기준으로 디자인하고 싶을 때 유용합니다:

```
    <div class="container">  <!-- ... --></div>
```

다른 프레임워크에서 사용했을 수 있는 컨테이너와 달리, Tailwind의 container는 자동으로 중앙 정렬되지 않으며 기본 가로 패딩도 없습니다. 이를 추가하려면 `mx-auto`와 `px-<number>` 유틸리티를 사용하세요:

```
    <div class="container mx-auto px-4">  <!-- ... --></div>
```

- 사용자 정의 값 사용

`max-w-[<value>]` 문법을 사용해 완전히 사용자 정의한 값을 기준으로 최대 너비를 설정하세요:

```
    <div class="max-w-[220px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `max-w-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="max-w-(--my-max-width) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `max-w-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `max-width` 유틸리티 앞에 붙이면, 해당 유틸리티가 중간 화면 크기 이상에서만 적용됩니다:

```
    <div class="max-w-sm md:max-w-lg ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

`max-w-<number>` 유틸리티는 `--spacing` 테마 변수로 구동되며, 자신의 테마에서 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
