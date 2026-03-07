---
title: "max-inline-size - 크기 조절 - Tailwind CSS"
description: "간격 스케일을 기준으로 요소의 최대 인라인 크기를 고정값으로 설정하려면 max-inline-24 및 max-inline-64 같은 max-inline-<number> 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/max-inline-size

# max-inline-size - 크기 조절 - Tailwind CSS

| Class                            | Styles                                                        |
| -------------------------------- | ------------------------------------------------------------- |
| `max-inline-<number>`            | `max-inline-size: calc(var(--spacing) * <number>);`           |
| `max-inline-<fraction>`          | `max-inline-size: calc(<fraction> * 100%);`                   |
| `max-inline-3xs`                 | `max-inline-size: var(--container-3xs); /* 16rem (256px) */`  |
| `max-inline-2xs`                 | `max-inline-size: var(--container-2xs); /* 18rem (288px) */`  |
| `max-inline-xs`                  | `max-inline-size: var(--container-xs); /* 20rem (320px) */`   |
| `max-inline-sm`                  | `max-inline-size: var(--container-sm); /* 24rem (384px) */`   |
| `max-inline-md`                  | `max-inline-size: var(--container-md); /* 28rem (448px) */`   |
| `max-inline-lg`                  | `max-inline-size: var(--container-lg); /* 32rem (512px) */`   |
| `max-inline-xl`                  | `max-inline-size: var(--container-xl); /* 36rem (576px) */`   |
| `max-inline-2xl`                 | `max-inline-size: var(--container-2xl); /* 42rem (672px) */`  |
| `max-inline-3xl`                 | `max-inline-size: var(--container-3xl); /* 48rem (768px) */`  |
| `max-inline-4xl`                 | `max-inline-size: var(--container-4xl); /* 56rem (896px) */`  |
| `max-inline-5xl`                 | `max-inline-size: var(--container-5xl); /* 64rem (1024px) */` |
| `max-inline-6xl`                 | `max-inline-size: var(--container-6xl); /* 72rem (1152px) */` |
| `max-inline-7xl`                 | `max-inline-size: var(--container-7xl); /* 80rem (1280px) */` |
| `max-inline-none`                | `max-inline-size: none;`                                      |
| `max-inline-px`                  | `max-inline-size: 1px;`                                       |
| `max-inline-full`                | `max-inline-size: 100%;`                                      |
| `max-inline-dvw`                 | `max-inline-size: 100dvw;`                                    |
| `max-inline-dvh`                 | `max-inline-size: 100dvh;`                                    |
| `max-inline-lvw`                 | `max-inline-size: 100lvw;`                                    |
| `max-inline-lvh`                 | `max-inline-size: 100lvh;`                                    |
| `max-inline-svw`                 | `max-inline-size: 100svw;`                                    |
| `max-inline-svh`                 | `max-inline-size: 100svh;`                                    |
| `max-inline-screen`              | `max-inline-size: 100vw;`                                     |
| `max-inline-min`                 | `max-inline-size: min-content;`                               |
| `max-inline-max`                 | `max-inline-size: max-content;`                               |
| `max-inline-fit`                 | `max-inline-size: fit-content;`                               |
| `max-inline-(<custom-property>)` | `max-inline-size: var(<custom-property>);`                    |
| `max-inline-[<value>]`           | `max-inline-size: <value>;`                                   |

더 보기

## 예제

- 기본 예제

간격 스케일을 기준으로 요소의 최대 인라인 크기를 고정값으로 설정하려면 `max-inline-24` 및 `max-inline-64` 같은 `max-inline-<number>` 유틸리티를 사용하세요:

예제 크기를 조정해 예상 동작을 확인하세요

max-inline-96

max-inline-80

max-inline-64

max-inline-48

max-inline-40

max-inline-32

```
    <div class="inline-full max-inline-96 ...">max-inline-96</div><div class="inline-full max-inline-80 ...">max-inline-80</div><div class="inline-full max-inline-64 ...">max-inline-64</div><div class="inline-full max-inline-48 ...">max-inline-48</div><div class="inline-full max-inline-40 ...">max-inline-40</div><div class="inline-full max-inline-32 ...">max-inline-32</div>
```

- 백분율 사용

요소에 백분율 기반 최대 인라인 크기를 적용하려면 `max-inline-full` 또는 `max-inline-1/2`, `max-inline-2/5` 같은 `max-inline-<fraction>` 유틸리티를 사용하세요:

예제 크기를 조정해 예상 동작을 확인하세요

max-inline-9/10

max-inline-3/4

max-inline-1/2

max-inline-1/3

```
    <div class="inline-full max-inline-9/10 ...">max-inline-9/10</div><div class="inline-full max-inline-3/4 ...">max-inline-3/4</div><div class="inline-full max-inline-1/2 ...">max-inline-1/2</div><div class="inline-full max-inline-1/3 ...">max-inline-1/3</div>
```

- 컨테이너 스케일 사용

컨테이너 스케일을 기준으로 요소의 최대 인라인 크기를 고정값으로 설정하려면 `max-inline-sm`, `max-inline-xl` 같은 유틸리티를 사용하세요:

예제 크기를 조정해 예상 동작을 확인하세요

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

Andrew Alfred

여행 비서 보좌관

```
    <div class="max-inline-md ...">  <!-- ... --></div>
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값을 기준으로 최대 인라인 크기를 설정하려면 `max-inline-[<value>]` 구문을 사용하세요:

```
    <div class="max-inline-[220px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `max-inline-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="max-inline-(--my-max-inline-size) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `max-inline-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `max-inline-size` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <div class="max-inline-sm md:max-inline-lg ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 지정

`max-inline-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 구동되며, 이 변수는 사용자 테마에서 커스터마이즈할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이즈에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
