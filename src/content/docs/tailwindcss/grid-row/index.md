---
title: "grid-row - Flexbox & Grid - Tailwind CSS"
description: "row-span-2 및 row-span-4 같은 row-span-<number> 유틸리티를 사용해 요소가 _n_개의 행을 차지하도록 만듭니다:"
---

출처 URL: https://tailwindcss.com/docs/grid-row

# grid-row - Flexbox & Grid - Tailwind CSS

| 클래스                          | 스타일                                                                 |
| ------------------------------- | ---------------------------------------------------------------------- |
| `row-span-<number>`             | `grid-row: span <number> / span <number>;`                             |
| `row-span-full`                 | `grid-row: 1 / -1;`                                                    |
| `row-span-(<custom-property>)`  | `grid-row: span var(<custom-property>) / span var(<custom-property>);` |
| `row-span-[<value>]`            | `grid-row: span <value> / span <value>;`                               |
| `row-start-<number>`            | `grid-row-start: <number>;`                                            |
| `-row-start-<number>`           | `grid-row-start: calc(<number> * -1);`                                 |
| `row-start-auto`                | `grid-row-start: auto;`                                                |
| `row-start-(<custom-property>)` | `grid-row-start: var(<custom-property>);`                              |
| `row-start-[<value>]`           | `grid-row-start: <value>;`                                             |
| `row-end-<number>`              | `grid-row-end: <number>;`                                              |
| `-row-end-<number>`             | `grid-row-end: calc(<number> * -1);`                                   |
| `row-end-auto`                  | `grid-row-end: auto;`                                                  |
| `row-end-(<custom-property>)`   | `grid-row-end: var(<custom-property>);`                                |
| `row-end-[<value>]`             | `grid-row-end: <value>;`                                               |
| `row-auto`                      | `grid-row: auto;`                                                      |
| `row-<number>`                  | `grid-row: <number>;`                                                  |
| `-row-<number>`                 | `grid-row: calc(<number> * -1);`                                       |
| `row-(<custom-property>)`       | `grid-row: var(<custom-property>);`                                    |
| `row-[<value>]`                 | `grid-row: <value>;`                                                   |

더 보기

## 예제

- 행 확장하기

`row-span-2` 및 `row-span-4` 같은 `row-span-<number>` 유틸리티를 사용해 요소가 *n*개의 행을 차지하도록 만듭니다:

01

02

03

```
    <div class="grid grid-flow-col grid-rows-3 gap-4">  <div class="row-span-3 ...">01</div>  <div class="col-span-2 ...">02</div>  <div class="col-span-2 row-span-2 ...">03</div></div>
```

- 시작선과 끝선

`row-start-2` 및 `row-end-3` 같은 `row-start-<number>` 또는 `row-end-<number>` 유틸리티를 사용해 요소가 _n번째_ 그리드 라인에서 시작하거나 끝나도록 만듭니다:

01

02

03

```
    <div class="grid grid-flow-col grid-rows-3 gap-4">  <div class="row-span-2 row-start-2 ...">01</div>  <div class="row-span-2 row-end-3 ...">02</div>  <div class="row-start-1 row-end-4 ...">03</div></div>
```

이 유틸리티들은 `row-span-<number>` 유틸리티와 함께 조합해 특정 개수의 행을 차지하도록 설정할 수도 있습니다.

- 사용자 정의 값 사용하기

`row-[<value>]`,`row-span-[<value>]`,`row-start-[<value>]`, `row-end-[<value>]` 같은 유틸리티를 사용해 완전히 사용자 정의한 값을 기준으로 그리드 행 크기와 위치를 설정합니다:

```
    <div class="row-[span_16_/_span_16] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `row-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="row-(--my-rows) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `row-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`grid-row`,`grid-row-start`, `grid-row-end` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="row-span-3 md:row-span-4 ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
