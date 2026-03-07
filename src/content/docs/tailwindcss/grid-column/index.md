---
title: "grid-column - Flexbox 및 Grid - Tailwind CSS"
description: "col-span-2, col-span-4 같은 col-span-<number> 유틸리티를 사용해 요소가 _n_개의 열을 차지하도록 만드세요:"
---

출처 URL: https://tailwindcss.com/docs/grid-column

# grid-column - Flexbox 및 Grid - Tailwind CSS

| 클래스                          | 스타일                                                                    |
| ------------------------------- | ------------------------------------------------------------------------- |
| `col-span-<number>`             | `grid-column: span <number> / span <number>;`                             |
| `col-span-full`                 | `grid-column: 1 / -1;`                                                    |
| `col-span-(<custom-property>)`  | `grid-column: span var(<custom-property>) / span var(<custom-property>);` |
| `col-span-[<value>]`            | `grid-column: span <value> / span <value>;`                               |
| `col-start-<number>`            | `grid-column-start: <number>;`                                            |
| `-col-start-<number>`           | `grid-column-start: calc(<number> * -1);`                                 |
| `col-start-auto`                | `grid-column-start: auto;`                                                |
| `col-start-(<custom-property>)` | `grid-column-start: var(<custom-property>);`                              |
| `col-start-[<value>]`           | `grid-column-start: <value>;`                                             |
| `col-end-<number>`              | `grid-column-end: <number>;`                                              |
| `-col-end-<number>`             | `grid-column-end: calc(<number> * -1);`                                   |
| `col-end-auto`                  | `grid-column-end: auto;`                                                  |
| `col-end-(<custom-property>)`   | `grid-column-end: var(<custom-property>);`                                |
| `col-end-[<value>]`             | `grid-column-end: <value>;`                                               |
| `col-auto`                      | `grid-column: auto;`                                                      |
| `col-<number>`                  | `grid-column: <number>;`                                                  |
| `-col-<number>`                 | `grid-column: calc(<number> * -1);`                                       |
| `col-(<custom-property>)`       | `grid-column: var(<custom-property>);`                                    |
| `col-[<value>]`                 | `grid-column: <value>;`                                                   |

더 보기

## 예제

- 열 확장하기

`col-span-2`, `col-span-4` 같은 `col-span-<number>` 유틸리티를 사용해 요소가 *n*개의 열을 차지하도록 만드세요:

01

02

03

04

05

06

07

```
    <div class="grid grid-cols-3 gap-4">  <div class="...">01</div>  <div class="...">02</div>  <div class="...">03</div>  <div class="col-span-2 ...">04</div>  <div class="...">05</div>  <div class="...">06</div>  <div class="col-span-2 ...">07</div></div>
```

- 시작선과 끝선 지정하기

`col-start-2`, `col-end-3` 같은 `col-start-<number>` 또는 `col-end-<number>` 유틸리티를 사용해 요소가 _n번째_ 그리드 라인에서 시작하거나 끝나도록 만드세요:

01

02

03

04

```
    <div class="grid grid-cols-6 gap-4">  <div class="col-span-4 col-start-2 ...">01</div>  <div class="col-start-1 col-end-3 ...">02</div>  <div class="col-span-2 col-end-7 ...">03</div>  <div class="col-start-1 col-end-7 ...">04</div></div>
```

이 유틸리티들은 `col-span-<number>` 유틸리티와 함께 조합해 특정 개수의 열을 차지하도록 설정할 수도 있습니다.

- 사용자 정의 값 사용하기

`col-[<value>]`,`col-span-[<value>]`,`col-start-[<value>]`,`col-end-[<value>]` 같은 유틸리티를 사용해 완전히 사용자 정의한 값을 기준으로 그리드 열의 크기와 위치를 설정하세요:

```
    <div class="col-[16_/_span_16] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `col-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="col-(--my-columns) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `col-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `grid-column`, `grid-column-start`, `grid-column-end` 유틸리티 앞에 붙이면 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="col-span-2 md:col-span-6 ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
