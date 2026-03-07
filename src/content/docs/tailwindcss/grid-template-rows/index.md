---
title: "grid-template-rows - Flexbox & Grid - Tailwind CSS"
description: "grid-rows-2, grid-rows-4 같은 grid-rows-<number> 유틸리티를 사용해 _n_개의 동일한 크기 행으로 이루어진 그리드를 만들 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/grid-template-rows

# grid-template-rows - Flexbox & Grid - Tailwind CSS

| 클래스                          | 스타일                                                  |
| ------------------------------- | ------------------------------------------------------- |
| `grid-rows-<number>`            | `grid-template-rows: repeat(<number>, minmax(0, 1fr));` |
| `grid-rows-none`                | `grid-template-rows: none;`                             |
| `grid-rows-subgrid`             | `grid-template-rows: subgrid;`                          |
| `grid-rows-[<value>]`           | `grid-template-rows: <value>;`                          |
| `grid-rows-(<custom-property>)` | `grid-template-rows: var(<custom-property>);`           |

## 예제

- 그리드 행 지정하기

`grid-rows-2`, `grid-rows-4` 같은 `grid-rows-<number>` 유틸리티를 사용해 *n*개의 동일한 크기 행으로 이루어진 그리드를 만들 수 있습니다:

01

02

03

04

05

06

07

08

09

```
    <div class="grid grid-flow-col grid-rows-4 gap-4">  <div>01</div>  <!-- ... -->  <div>09</div></div>
```

- 서브그리드 구현하기

`grid-rows-subgrid` 유틸리티를 사용하면 항목의 부모에 정의된 행 트랙을 따를 수 있습니다:

01

02

03

04

05

06

07

08

09

10

```
    <div class="grid grid-flow-col grid-rows-4 gap-4">  <div>01</div>  <!-- ... -->  <div>05</div>  <div class="row-span-3 grid grid-rows-subgrid gap-4">    <div class="row-start-2">06</div>  </div>  <div>07</div>  <!-- ... -->  <div>10</div></div>
```

- 사용자 지정 값 사용하기

`grid-rows-[<value>]` 문법을 사용해 완전히 사용자 지정한 값으로 행을 설정할 수 있습니다:

```
    <div class="grid-rows-[200px_minmax(900px,1fr)_100px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `grid-rows-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="grid-rows-(--my-grid-rows) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `grid-rows-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `grid-template-rows` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="grid grid-rows-2 md:grid-rows-6 ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
