---
title: "grid-auto-flow - Flexbox & Grid - Tailwind CSS"
description: "grid-flow-col, grid-flow-row-dense 같은 유틸리티를 사용해 그리드 레이아웃에서 자동 배치 알고리즘이 동작하는 방식을 제어할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/grid-auto-flow

# grid-auto-flow - Flexbox & Grid - Tailwind CSS

| 클래스                | 스타일                          |
| --------------------- | ------------------------------- |
| `grid-flow-row`       | `grid-auto-flow: row;`          |
| `grid-flow-col`       | `grid-auto-flow: column;`       |
| `grid-flow-dense`     | `grid-auto-flow: dense;`        |
| `grid-flow-row-dense` | `grid-auto-flow: row dense;`    |
| `grid-flow-col-dense` | `grid-auto-flow: column dense;` |

## 예제

- 기본 예제

`grid-flow-col`, `grid-flow-row-dense` 같은 유틸리티를 사용해 그리드 레이아웃에서 자동 배치 알고리즘이 동작하는 방식을 제어할 수 있습니다:

01

02

03

04

05

```
    <div class="grid grid-flow-row-dense grid-cols-3 grid-rows-3 ...">  <div class="col-span-2">01</div>  <div class="col-span-2">02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 반응형 디자인

`grid-auto-flow` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="grid grid-flow-col md:grid-flow-row ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
