---
title: "grid-auto-columns - Flexbox & Grid - Tailwind CSS"
description: "auto-cols-min 및 auto-cols-max 같은 유틸리티를 사용해 암시적으로 생성된 그리드 열의 크기를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/grid-auto-columns

# grid-auto-columns - Flexbox & Grid - Tailwind CSS

| 클래스                          | 스타일                                       |
| ------------------------------- | -------------------------------------------- |
| `auto-cols-auto`                | `grid-auto-columns: auto;`                   |
| `auto-cols-min`                 | `grid-auto-columns: min-content;`            |
| `auto-cols-max`                 | `grid-auto-columns: max-content;`            |
| `auto-cols-fr`                  | `grid-auto-columns: minmax(0, 1fr);`         |
| `auto-cols-(<custom-property>)` | `grid-auto-columns: var(<custom-property>);` |
| `auto-cols-[<value>]`           | `grid-auto-columns: <value>;`                |

## 예제

- 기본 예제

`auto-cols-min` 및 `auto-cols-max` 같은 유틸리티를 사용해 암시적으로 생성된 그리드 열의 크기를 제어하세요:

```
    <div class="grid auto-cols-max grid-flow-col">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 사용자 정의 값 사용

`auto-cols-[<value>]` 문법을 사용하면 완전히 사용자 정의한 값을 기준으로 암시적으로 생성된 그리드 열의 크기를 설정할 수 있습니다:

```
    <div class="auto-cols-[minmax(0,2fr)] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `auto-cols-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="auto-cols-(--my-auto-cols) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `auto-cols-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `grid-auto-columns` 유틸리티 앞에 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="grid grid-flow-col auto-cols-max md:auto-cols-min ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
