---
title: "gap - Flexbox 및 Grid - Tailwind CSS"
description: "gap-2, gap-4 같은 gap-<number> 유틸리티를 사용해 grid 및 flexbox 레이아웃에서 행과 열 사이의 간격을 함께 변경할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/gap

# gap - Flexbox 및 Grid - Tailwind CSS

| Class                       | Styles                                        |
| --------------------------- | --------------------------------------------- |
| `gap-<number>`              | `gap: calc(var(--spacing) * <value>);`        |
| `gap-(<custom-property>)`   | `gap: var(<custom-property>);`                |
| `gap-[<value>]`             | `gap: <value>;`                               |
| `gap-x-<number>`            | `column-gap: calc(var(--spacing) * <value>);` |
| `gap-x-(<custom-property>)` | `column-gap: var(<custom-property>);`         |
| `gap-x-[<value>]`           | `column-gap: <value>;`                        |
| `gap-y-<number>`            | `row-gap: calc(var(--spacing) * <value>);`    |
| `gap-y-(<custom-property>)` | `row-gap: var(<custom-property>);`            |
| `gap-y-[<value>]`           | `row-gap: <value>;`                           |

## 예제

- 기본 예제

`gap-2`, `gap-4` 같은 `gap-<number>` 유틸리티를 사용해 grid 및 flexbox 레이아웃에서 행과 열 사이의 간격을 함께 변경할 수 있습니다:

01

02

03

04

```
    <div class="grid grid-cols-2 gap-4">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

- 행/열 간격을 각각 변경하기

`gap-x-8`, `gap-y-4` 같은 `gap-x-<number>` 또는 `gap-y-<number>` 유틸리티를 사용해 열과 행 사이의 간격을 각각 독립적으로 변경할 수 있습니다:

01

02

03

04

05

06

```
    <div class="grid grid-cols-3 gap-x-8 gap-y-4">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 사용자 정의 값 사용하기

`gap-[<value>]`, `gap-x-[<value>]`, `gap-y-[<value>]` 같은 유틸리티를 사용해 완전히 사용자 정의한 값으로 간격을 설정할 수 있습니다:

```
    <div class="gap-[10vw] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `gap-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="gap-(--my-gap) ...">  <!-- ... --></div>
```

이 구문은 `var()` 함수를 자동으로 추가해 주는 `gap-[var(<custom-property>)]`의 단축 표현입니다.

- 반응형 디자인

`gap`, `column-gap`, `row-gap` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="grid gap-4 md:gap-6 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 확인하세요.
