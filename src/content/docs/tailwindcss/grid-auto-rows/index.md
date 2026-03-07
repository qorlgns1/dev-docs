---
title: "grid-auto-rows - 플렉스박스 및 그리드 - Tailwind CSS"
description: "암시적으로 생성된 그리드 행의 크기를 제어하려면 auto-rows-min, auto-rows-max 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/grid-auto-rows

# grid-auto-rows - 플렉스박스 및 그리드 - Tailwind CSS

| 클래스                          | 스타일                                    |
| ------------------------------- | ----------------------------------------- |
| `auto-rows-auto`                | `grid-auto-rows: auto;`                   |
| `auto-rows-min`                 | `grid-auto-rows: min-content;`            |
| `auto-rows-max`                 | `grid-auto-rows: max-content;`            |
| `auto-rows-fr`                  | `grid-auto-rows: minmax(0, 1fr);`         |
| `auto-rows-(<custom-property>)` | `grid-auto-rows: var(<custom-property>);` |
| `auto-rows-[<value>]`           | `grid-auto-rows: <value>;`                |

## 예제

- 기본 예제

암시적으로 생성된 그리드 행의 크기를 제어하려면 `auto-rows-min`, `auto-rows-max` 같은 유틸리티를 사용하세요:

```
    <div class="grid grid-flow-row auto-rows-max">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 사용자 정의 값 사용

완전히 사용자 정의한 값을 기준으로 암시적으로 생성된 그리드 행의 크기를 설정하려면 `auto-rows-[<value>]` 구문을 사용하세요:

```
    <div class="auto-rows-[minmax(0,2fr)] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `auto-rows-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="auto-rows-(--my-auto-rows) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `auto-rows-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `grid-auto-rows` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="grid grid-flow-row auto-rows-max md:auto-rows-min ...">  <!-- ... --></div>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
