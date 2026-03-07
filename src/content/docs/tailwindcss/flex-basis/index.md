---
title: "flex-basis - Flexbox & Grid - Tailwind CSS"
description: "basis-64, basis-128 같은 basis-<number> 유틸리티를 사용해 간격 스케일을 기준으로 flex 항목의 초기 크기를 설정합니다:"
---

출처 URL: https://tailwindcss.com/docs/flex-basis

# flex-basis - Flexbox & Grid - Tailwind CSS

| 클래스                      | 스타일                                                   |
| --------------------------- | -------------------------------------------------------- |
| `basis-<number>`            | `flex-basis: calc(var(--spacing) * <number>);`           |
| `basis-<fraction>`          | `flex-basis: calc(<fraction> * 100%);`                   |
| `basis-full`                | `flex-basis: 100%;`                                      |
| `basis-auto`                | `flex-basis: auto;`                                      |
| `basis-3xs`                 | `flex-basis: var(--container-3xs); /* 16rem (256px) */`  |
| `basis-2xs`                 | `flex-basis: var(--container-2xs); /* 18rem (288px) */`  |
| `basis-xs`                  | `flex-basis: var(--container-xs); /* 20rem (320px) */`   |
| `basis-sm`                  | `flex-basis: var(--container-sm); /* 24rem (384px) */`   |
| `basis-md`                  | `flex-basis: var(--container-md); /* 28rem (448px) */`   |
| `basis-lg`                  | `flex-basis: var(--container-lg); /* 32rem (512px) */`   |
| `basis-xl`                  | `flex-basis: var(--container-xl); /* 36rem (576px) */`   |
| `basis-2xl`                 | `flex-basis: var(--container-2xl); /* 42rem (672px) */`  |
| `basis-3xl`                 | `flex-basis: var(--container-3xl); /* 48rem (768px) */`  |
| `basis-4xl`                 | `flex-basis: var(--container-4xl); /* 56rem (896px) */`  |
| `basis-5xl`                 | `flex-basis: var(--container-5xl); /* 64rem (1024px) */` |
| `basis-6xl`                 | `flex-basis: var(--container-6xl); /* 72rem (1152px) */` |
| `basis-7xl`                 | `flex-basis: var(--container-7xl); /* 80rem (1280px) */` |
| `basis-(<custom-property>)` | `flex-basis: var(<custom-property>);`                    |
| `basis-[<value>]`           | `flex-basis: <value>;`                                   |

더 보기

## 예제

- 간격 스케일 사용하기

`basis-64`, `basis-128` 같은 `basis-<number>` 유틸리티를 사용해 간격 스케일을 기준으로 flex 항목의 초기 크기를 설정합니다:

01

02

03

```
    <div class="flex flex-row">  <div class="basis-64">01</div>  <div class="basis-64">02</div>  <div class="basis-128">03</div></div>
```

- 컨테이너 스케일 사용하기

`basis-xs`, `basis-sm` 같은 유틸리티를 사용해 컨테이너 스케일을 기준으로 flex 항목의 초기 크기를 설정합니다:

01

02

03

04

```
    <div class="flex flex-row">  <div class="basis-3xs">01</div>  <div class="basis-2xs">02</div>  <div class="basis-xs">03</div>  <div class="basis-sm">04</div></div>
```

- 퍼센트 사용하기

`basis-1/2`, `basis-2/3` 같은 `basis-<fraction>` 유틸리티를 사용해 flex 항목의 초기 크기를 설정합니다:

01

02

```
    <div class="flex flex-row">  <div class="basis-1/3">01</div>  <div class="basis-2/3">02</div></div>
```

- 사용자 정의 값 사용하기

`basis-[<value>]` 문법을 사용해 완전히 사용자 정의한 값을 기준으로 basis를 설정합니다:

```
    <div class="basis-[30vw] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `basis-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="basis-(--my-basis) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `basis-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형으로 `flex-basis` 유틸리티에 접두사를 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="flex flex-row">  <div class="basis-1/4 md:basis-1/3">01</div>  <div class="basis-1/4 md:basis-1/3">02</div>  <div class="basis-1/2 md:basis-1/3">03</div></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.

## 테마 사용자 정의

프로젝트에서 고정 너비 basis 유틸리티를 사용자 정의하려면 `--container-*` 테마 변수를 사용하세요:

```
    @theme {  --container-4xs: 14rem; }
```

이제 마크업에서 `basis-4xs` 유틸리티를 사용할 수 있습니다:

```
    <div class="basis-4xs">  <!-- ... --></div>
```

`basis-<number>` 유틸리티는 `--spacing` 테마 변수로 구동되며, 이 값도 사용자 정의할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 사용자 정의에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
