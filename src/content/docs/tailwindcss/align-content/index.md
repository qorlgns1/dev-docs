---
title: "align-content - Flexbox & Grid - Tailwind CSS"
description: "content-start를 사용하면 컨테이너의 교차축 시작 지점에 행이 배치됩니다:"
---

출처 URL: https://tailwindcss.com/docs/align-content

# align-content - Flexbox & Grid - Tailwind CSS

| 클래스             | 스타일                          |
| ------------------ | ------------------------------- |
| `content-normal`   | `align-content: normal;`        |
| `content-center`   | `align-content: center;`        |
| `content-start`    | `align-content: flex-start;`    |
| `content-end`      | `align-content: flex-end;`      |
| `content-between`  | `align-content: space-between;` |
| `content-around`   | `align-content: space-around;`  |
| `content-evenly`   | `align-content: space-evenly;`  |
| `content-baseline` | `align-content: baseline;`      |
| `content-stretch`  | `align-content: stretch;`       |

## 예제

- 시작

`content-start`를 사용하면 컨테이너의 교차축 시작 지점에 행이 배치됩니다:

01

02

03

04

05

```
    <div class="grid h-56 grid-cols-3 content-start gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 가운데

`content-center`를 사용하면 컨테이너의 교차축 중앙에 행이 배치됩니다:

01

02

03

04

05

```
    <div class="grid h-56 grid-cols-3 content-center gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 끝

`content-end`를 사용하면 컨테이너의 교차축 끝 지점에 행이 배치됩니다:

01

02

03

04

05

```
    <div class="grid h-56 grid-cols-3 content-end gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 행 사이 간격 균등

`content-between`을 사용하면 각 줄 사이의 간격이 동일하도록 컨테이너의 행이 분배됩니다:

01

02

03

04

05

```
    <div class="grid h-56 grid-cols-3 content-between gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 행 주변 간격 균등

`content-around`를 사용하면 각 줄의 주변 간격이 동일하도록 컨테이너의 행이 분배됩니다:

01

02

03

04

05

```
    <div class="grid h-56 grid-cols-3 content-around gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 균등 간격

`content-evenly`를 사용하면 각 항목 주변의 간격이 동일하도록 행이 분배되며, `content-around` 사용 시 항목 사이에서 일반적으로 보이는 간격이 두 배가 되는 점도 함께 보정됩니다:

01

02

03

04

05

```
    <div class="grid h-56 grid-cols-3 content-evenly gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 늘리기

`content-stretch`를 사용하면 콘텐츠 항목이 컨테이너의 교차축을 따라 사용 가능한 공간을 채울 수 있습니다:

01

02

03

04

05

```
    <div class="grid h-56 grid-cols-3 content-stretch gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 기본값

`content-normal`을 사용하면 `align-content` 값이 설정되지 않은 것처럼 콘텐츠 항목이 기본 위치에 배치됩니다:

01

02

03

04

05

```
    <div class="grid h-56 grid-cols-3 content-normal gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

- 반응형 디자인

`md:` 같은 브레이크포인트 변형으로 `align-content` 유틸리티에 접두사를 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="grid content-start md:content-around ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
