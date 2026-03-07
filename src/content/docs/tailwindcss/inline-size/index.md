---
title: "inline-size - 크기 조정 - Tailwind CSS"
description: "inline-24, inline-64 같은 inline-<number> 유틸리티를 사용해, 간격 스케일을 기준으로 요소의 고정 inline-size를 설정할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/inline-size

# inline-size - 크기 조정 - Tailwind CSS

| 클래스                       | 스타일                                                    |
| ---------------------------- | --------------------------------------------------------- |
| `inline-<number>`            | `inline-size: calc(var(--spacing) * <number>);`           |
| `inline-<fraction>`          | `inline-size: calc(<fraction> * 100%);`                   |
| `inline-3xs`                 | `inline-size: var(--container-3xs); /* 16rem (256px) */`  |
| `inline-2xs`                 | `inline-size: var(--container-2xs); /* 18rem (288px) */`  |
| `inline-xs`                  | `inline-size: var(--container-xs); /* 20rem (320px) */`   |
| `inline-sm`                  | `inline-size: var(--container-sm); /* 24rem (384px) */`   |
| `inline-md`                  | `inline-size: var(--container-md); /* 28rem (448px) */`   |
| `inline-lg`                  | `inline-size: var(--container-lg); /* 32rem (512px) */`   |
| `inline-xl`                  | `inline-size: var(--container-xl); /* 36rem (576px) */`   |
| `inline-2xl`                 | `inline-size: var(--container-2xl); /* 42rem (672px) */`  |
| `inline-3xl`                 | `inline-size: var(--container-3xl); /* 48rem (768px) */`  |
| `inline-4xl`                 | `inline-size: var(--container-4xl); /* 56rem (896px) */`  |
| `inline-5xl`                 | `inline-size: var(--container-5xl); /* 64rem (1024px) */` |
| `inline-6xl`                 | `inline-size: var(--container-6xl); /* 72rem (1152px) */` |
| `inline-7xl`                 | `inline-size: var(--container-7xl); /* 80rem (1280px) */` |
| `inline-auto`                | `inline-size: auto;`                                      |
| `inline-px`                  | `inline-size: 1px;`                                       |
| `inline-full`                | `inline-size: 100%;`                                      |
| `inline-screen`              | `inline-size: 100vw;`                                     |
| `inline-dvw`                 | `inline-size: 100dvw;`                                    |
| `inline-dvh`                 | `inline-size: 100dvh;`                                    |
| `inline-lvw`                 | `inline-size: 100lvw;`                                    |
| `inline-lvh`                 | `inline-size: 100lvh;`                                    |
| `inline-svw`                 | `inline-size: 100svw;`                                    |
| `inline-svh`                 | `inline-size: 100svh;`                                    |
| `inline-min`                 | `inline-size: min-content;`                               |
| `inline-max`                 | `inline-size: max-content;`                               |
| `inline-fit`                 | `inline-size: fit-content;`                               |
| `inline-(<custom-property>)` | `inline-size: var(<custom-property>);`                    |
| `inline-[<value>]`           | `inline-size: <value>;`                                   |

더 보기

## 예제

- 기본 예제

`inline-24`, `inline-64` 같은 `inline-<number>` 유틸리티를 사용해, 간격 스케일을 기준으로 요소의 고정 `inline-size`를 설정할 수 있습니다:

inline-96

inline-80

inline-64

inline-48

inline-40

inline-32

```
    <div class="inline-96 ...">inline-96</div><div class="inline-80 ...">inline-80</div><div class="inline-64 ...">inline-64</div><div class="inline-48 ...">inline-48</div><div class="inline-40 ...">inline-40</div><div class="inline-32 ...">inline-32</div>
```

- 백분율 사용

`inline-full` 또는 `inline-1/2`, `inline-2/5` 같은 `inline-<fraction>` 유틸리티를 사용해 요소에 백분율 기반 `inline-size`를 지정할 수 있습니다:

inline-1/2

inline-1/2

inline-2/5

inline-3/5

inline-1/3

inline-2/3

inline-full

```
    <div class="flex ...">  <div class="inline-1/2 ...">inline-1/2</div>  <div class="inline-1/2 ...">inline-1/2</div></div><div class="flex ...">  <div class="inline-2/5 ...">inline-2/5</div>  <div class="inline-3/5 ...">inline-3/5</div></div><div class="flex ...">  <div class="inline-1/3 ...">inline-1/3</div>  <div class="inline-2/3 ...">inline-2/3</div></div><div class="inline-full ...">inline-full</div>
```

- 컨테이너 스케일 사용

`inline-sm`, `inline-xl` 같은 유틸리티를 사용해 컨테이너 스케일을 기준으로 요소의 고정 `inline-size`를 설정할 수 있습니다:

inline-xl

inline-lg

inline-md

inline-sm

inline-xs

inline-2xs

inline-3xs

```
    <div class="inline-xl ...">inline-xl</div><div class="inline-lg ...">inline-lg</div><div class="inline-md ...">inline-md</div><div class="inline-sm ...">inline-sm</div><div class="inline-xs ...">inline-xs</div><div class="inline-2xs ...">inline-2xs</div><div class="inline-3xs ...">inline-3xs</div>
```

- 뷰포트에 맞추기

`inline-screen` 유틸리티를 사용하면 요소가 뷰포트의 전체 `inline-size`를 차지하게 할 수 있습니다:

```
    <div class="inline-screen">  <!-- ... --></div>
```

- `inline-size` 재설정

특정 브레이크포인트와 같은 조건에서 요소에 지정된 `inline-size`를 제거하려면 `inline-auto` 유틸리티를 사용하세요:

```
    <div class="inline-full md:inline-auto">  <!-- ... --></div>
```

- 사용자 정의 값 사용

`inline-[<value>]` 문법을 사용해 완전히 사용자 정의한 값으로 `inline-size`를 설정할 수 있습니다:

```
    <div class="inline-[5px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `inline-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="inline-(--my-inline-size) ...">  <!-- ... --></div>
```

이 문법은 `var()` 함수를 자동으로 추가해 주는 `inline-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `inline-size` 유틸리티 앞에 붙이면, 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="inline-1/2 md:inline-full ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.

## 테마 사용자 정의

`inline-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 구동되며, 사용자 테마에서 이를 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
