---
title: "place-content - Flexbox 및 Grid - Tailwind CSS"
description: "인라인 축과 블록 축의 중앙에 항목을 배치하려면 place-content-center를 사용하세요:"
---

원본 URL: https://tailwindcss.com/docs/place-content

# place-content - Flexbox 및 Grid - Tailwind CSS

| 클래스                      | 스타일                          |
| --------------------------- | ------------------------------- |
| `place-content-center`      | `place-content: center;`        |
| `place-content-center-safe` | `place-content: safe center;`   |
| `place-content-start`       | `place-content: start;`         |
| `place-content-end`         | `place-content: end;`           |
| `place-content-end-safe`    | `place-content: safe end;`      |
| `place-content-between`     | `place-content: space-between;` |
| `place-content-around`      | `place-content: space-around;`  |
| `place-content-evenly`      | `place-content: space-evenly;`  |
| `place-content-baseline`    | `place-content: baseline;`      |
| `place-content-stretch`     | `place-content: stretch;`       |

## 예제

- 가운데

인라인 축과 블록 축의 중앙에 항목을 배치하려면 `place-content-center`를 사용하세요:

01

02

03

04

```
    <div class="grid h-48 grid-cols-2 place-content-center gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

- 시작

인라인 축과 블록 축의 시작 지점에 맞춰 항목을 배치하려면 `place-content-start`를 사용하세요:

01

02

03

04

```
    <div class="grid h-48 grid-cols-2 place-content-start gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

- 끝

인라인 축과 블록 축의 끝 지점에 맞춰 항목을 배치하려면 `place-content-end`를 사용하세요:

01

02

03

04

```
    <div class="grid h-48 grid-cols-2 place-content-end gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

- 항목 사이 간격

각 축에서 각 행과 열 사이의 간격이 동일해지도록 인라인 축과 블록 축을 따라 그리드 항목을 배치하려면 `place-content-between`을 사용하세요:

01

02

03

04

```
    <div class="grid h-48 grid-cols-2 place-content-between gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

- 주변 간격

각 축에서 각 행과 열 주변의 간격이 동일해지도록 인라인 축과 블록 축을 따라 그리드 항목을 배치하려면 `place-content-around`를 사용하세요:

01

02

03

04

```
    <div class="grid h-48 grid-cols-2 place-content-around gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

- 균등 간격

인라인 축과 블록 축에서 그리드 항목이 균등한 간격으로 배치되도록 하려면 `place-content-evenly`를 사용하세요:

01

02

03

04

```
    <div class="grid h-48 grid-cols-2 place-content-evenly gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

- 늘이기

인라인 축과 블록 축에서 그리드 항목이 자신의 그리드 영역을 따라 늘어나도록 하려면 `place-content-stretch`를 사용하세요:

01

02

03

04

```
    <div class="grid h-48 grid-cols-2 place-content-stretch gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `place-content` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <div class="grid place-content-start md:place-content-center ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
