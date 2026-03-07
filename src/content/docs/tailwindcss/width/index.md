---
title: "width - 크기 조절 - Tailwind CSS"
description: "w-24, w-64 같은 w-<number> 유틸리티를 사용하면 spacing scale을 기준으로 요소에 고정 너비를 설정할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/width

# width - 크기 조절 - Tailwind CSS

| Class                      | 스타일                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------- |
| `w-<number>`               | `width: calc(var(--spacing) * <number>);`                                          |
| `w-<fraction>`             | `width: calc(<fraction> * 100%);`                                                  |
| `w-3xs`                    | `width: var(--container-3xs); /* 16rem (256px) */`                                 |
| `w-2xs`                    | `width: var(--container-2xs); /* 18rem (288px) */`                                 |
| `w-xs`                     | `width: var(--container-xs); /* 20rem (320px) */`                                  |
| `w-sm`                     | `width: var(--container-sm); /* 24rem (384px) */`                                  |
| `w-md`                     | `width: var(--container-md); /* 28rem (448px) */`                                  |
| `w-lg`                     | `width: var(--container-lg); /* 32rem (512px) */`                                  |
| `w-xl`                     | `width: var(--container-xl); /* 36rem (576px) */`                                  |
| `w-2xl`                    | `width: var(--container-2xl); /* 42rem (672px) */`                                 |
| `w-3xl`                    | `width: var(--container-3xl); /* 48rem (768px) */`                                 |
| `w-4xl`                    | `width: var(--container-4xl); /* 56rem (896px) */`                                 |
| `w-5xl`                    | `width: var(--container-5xl); /* 64rem (1024px) */`                                |
| `w-6xl`                    | `width: var(--container-6xl); /* 72rem (1152px) */`                                |
| `w-7xl`                    | `width: var(--container-7xl); /* 80rem (1280px) */`                                |
| `w-auto`                   | `width: auto;`                                                                     |
| `w-px`                     | `width: 1px;`                                                                      |
| `w-full`                   | `width: 100%;`                                                                     |
| `w-screen`                 | `width: 100vw;`                                                                    |
| `w-dvw`                    | `width: 100dvw;`                                                                   |
| `w-dvh`                    | `width: 100dvh;`                                                                   |
| `w-lvw`                    | `width: 100lvw;`                                                                   |
| `w-lvh`                    | `width: 100lvh;`                                                                   |
| `w-svw`                    | `width: 100svw;`                                                                   |
| `w-svh`                    | `width: 100svh;`                                                                   |
| `w-min`                    | `width: min-content;`                                                              |
| `w-max`                    | `width: max-content;`                                                              |
| `w-fit`                    | `width: fit-content;`                                                              |
| `w-(<custom-property>)`    | `width: var(<custom-property>);`                                                   |
| `w-[<value>]`              | `width: <value>;`                                                                  |
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

`w-24`, `w-64` 같은 `w-<number>` 유틸리티를 사용하면 spacing scale을 기준으로 요소에 고정 너비를 설정할 수 있습니다:

w-96

w-80

w-64

w-48

w-40

w-32

w-24

```
    <div class="w-96 ...">w-96</div><div class="w-80 ...">w-80</div><div class="w-64 ...">w-64</div><div class="w-48 ...">w-48</div><div class="w-40 ...">w-40</div><div class="w-32 ...">w-32</div><div class="w-24 ...">w-24</div>
```

- 백분율 사용하기

`w-full`, `w-1/2`, `w-2/5` 같은 `w-<fraction>` 유틸리티를 사용하면 요소에 백분율 기반 너비를 줄 수 있습니다:

w-1/2

w-1/2

w-2/5

w-3/5

w-1/3

w-2/3

w-1/4

w-3/4

w-1/5

w-4/5

w-1/6

w-5/6

w-full

```
    <div class="flex ...">  <div class="w-1/2 ...">w-1/2</div>  <div class="w-1/2 ...">w-1/2</div></div><div class="flex ...">  <div class="w-2/5 ...">w-2/5</div>  <div class="w-3/5 ...">w-3/5</div></div><div class="flex ...">  <div class="w-1/3 ...">w-1/3</div>  <div class="w-2/3 ...">w-2/3</div></div><div class="flex ...">  <div class="w-1/4 ...">w-1/4</div>  <div class="w-3/4 ...">w-3/4</div></div><div class="flex ...">  <div class="w-1/5 ...">w-1/5</div>  <div class="w-4/5 ...">w-4/5</div></div><div class="flex ...">  <div class="w-1/6 ...">w-1/6</div>  <div class="w-5/6 ...">w-5/6</div></div><div class="w-full ...">w-full</div>
```

- 컨테이너 스케일 사용하기

`w-sm`, `w-xl` 같은 유틸리티를 사용하면 container scale을 기준으로 요소에 고정 너비를 설정할 수 있습니다:

w-xl

w-lg

w-md

w-sm

w-xs

w-2xs

w-3xs

```
    <div class="w-xl ...">w-xl</div><div class="w-lg ...">w-lg</div><div class="w-md ...">w-md</div><div class="w-sm ...">w-sm</div><div class="w-xs ...">w-xs</div><div class="w-2xs ...">w-2xs</div><div class="w-3xs ...">w-3xs</div>
```

- 뷰포트와 맞추기

`w-screen` 유틸리티를 사용하면 요소가 뷰포트 전체 너비를 차지하게 만들 수 있습니다:

```
    <div class="w-screen">  <!-- ... --></div>
```

또는 `w-lvw`, `w-svw`, `w-dvw` 유틸리티를 사용해 large, small, dynamic viewport의 너비에 맞출 수도 있습니다.

- 너비 재설정하기

특정 브레이크포인트 등 특정 조건에서 요소에 지정된 너비를 제거하려면 `w-auto` 유틸리티를 사용하세요:

```
    <div class="w-full md:w-auto">  <!-- ... --></div>
```

- 너비와 높이 함께 설정하기

`size-px`, `size-4`, `size-full` 같은 유틸리티를 사용하면 너비와 높이를 동시에 설정할 수 있습니다:

size-16

size-20

size-24

size-32

size-40

```
    <div class="size-16 ...">size-16</div><div class="size-20 ...">size-20</div><div class="size-24 ...">size-24</div><div class="size-32 ...">size-32</div><div class="size-40 ...">size-40</div>
```

- 사용자 지정 값 사용하기

`w-[<value>]` 문법을 사용하면 완전히 사용자 지정한 값으로 너비를 설정할 수 있습니다:

```
    <div class="w-[5px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `w-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="w-(--my-width) ...">  <!-- ... --></div>
```

이 문법은 `var()` 함수를 자동으로 추가해 주는 `w-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `width` 유틸리티 앞에 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="w-1/2 md:w-full ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 지정

`w-<number>` 및 `size-<number>` 유틸리티는 `--spacing` 테마 변수를 기반으로 하며, 이 변수는 사용자 테마에서 커스터마이즈할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

spacing scale 커스터마이징에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
