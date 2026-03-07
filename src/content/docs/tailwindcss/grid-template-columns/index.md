---
title: "grid-template-columns - Flexbox & Grid - Tailwind CSS"
description: "grid-cols-2, grid-cols-4 같은 grid-cols-<number> 유틸리티를 사용해, 크기가 동일한 _n_개의 열로 구성된 그리드를 만들 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/grid-template-columns

# grid-template-columns - Flexbox & Grid - Tailwind CSS

| 클래스                          | 스타일                                                     |
| ------------------------------- | ---------------------------------------------------------- |
| `grid-cols-<number>`            | `grid-template-columns: repeat(<number>, minmax(0, 1fr));` |
| `grid-cols-none`                | `grid-template-columns: none;`                             |
| `grid-cols-subgrid`             | `grid-template-columns: subgrid;`                          |
| `grid-cols-[<value>]`           | `grid-template-columns: <value>;`                          |
| `grid-cols-(<custom-property>)` | `grid-template-columns: var(<custom-property>);`           |

## 예시

- 그리드 열 지정하기

`grid-cols-2`, `grid-cols-4` 같은 `grid-cols-<number>` 유틸리티를 사용해, 크기가 동일한 *n*개의 열로 구성된 그리드를 만들 수 있습니다:

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
    <div class="grid grid-cols-4 gap-4">  <div>01</div>  <!-- ... -->  <div>09</div></div>
```

- 서브그리드 구현하기

`grid-cols-subgrid` 유틸리티를 사용하면 해당 아이템의 부모에 정의된 열 트랙을 그대로 따를 수 있습니다:

01

02

03

04

05

06

```
    <div class="grid grid-cols-4 gap-4">  <div>01</div>  <!-- ... -->  <div>05</div>  <div class="col-span-3 grid grid-cols-subgrid gap-4">    <div class="col-start-2">06</div>  </div></div>
```

- 커스텀 값 사용하기

`grid-cols-[<value>]` 문법을 사용해 완전히 사용자 정의된 값으로 열을 설정할 수 있습니다:

```
    <div class="grid-cols-[200px_minmax(900px,_1fr)_100px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `grid-cols-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="grid-cols-(--my-grid-cols) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `grid-cols-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `grid-template-columns` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="grid grid-cols-1 md:grid-cols-6 ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
