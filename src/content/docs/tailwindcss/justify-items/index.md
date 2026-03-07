---
title: "justify-items - Flexbox & Grid - Tailwind CSS"
description: "justify-items-start 유틸리티를 사용해 그리드 아이템을 인라인 축의 시작 지점에 맞춰 정렬합니다:"
---

출처 URL: https://tailwindcss.com/docs/justify-items

# justify-items - Flexbox & Grid - Tailwind CSS

| 클래스                      | 스타일                        |
| --------------------------- | ----------------------------- |
| `justify-items-start`       | `justify-items: start;`       |
| `justify-items-end`         | `justify-items: end;`         |
| `justify-items-end-safe`    | `justify-items: safe end;`    |
| `justify-items-center`      | `justify-items: center;`      |
| `justify-items-center-safe` | `justify-items: safe center;` |
| `justify-items-stretch`     | `justify-items: stretch;`     |
| `justify-items-normal`      | `justify-items: normal;`      |

## 예제

- 시작

`justify-items-start` 유틸리티를 사용해 그리드 아이템을 인라인 축의 시작 지점에 맞춰 정렬합니다:

01

02

03

04

05

06

```
    <div class="grid justify-items-start ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 끝

`justify-items-end` 또는 `justify-items-end-safe` 유틸리티를 사용해 그리드 아이템을 인라인 축의 끝 지점에 맞춰 정렬합니다:

정렬 동작을 확인하려면 컨테이너 크기를 조절하세요

justify-items-end

01

02

03

justify-items-end-safe

01

02

03

justify-items-end

```
    <div class="grid grid-flow-col justify-items-end ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

justify-items-end-safe

```
    <div class="grid grid-flow-col justify-items-end-safe ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

사용 가능한 공간이 충분하지 않을 때 `justify-items-end-safe` 유틸리티는 아이템을 끝이 아니라 컨테이너의 시작 지점에 정렬합니다.

- 가운데

`justify-items-center` 또는 `justify-items-center-safe` 유틸리티를 사용해 그리드 아이템을 인라인 축의 끝 지점에 맞춰 정렬합니다:

정렬 동작을 확인하려면 컨테이너 크기를 조절하세요

justify-items-center

01

02

03

justify-items-center-safe

01

02

03

justify-items-center

```
    <div class="grid grid-flow-col justify-items-center ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

justify-items-center-safe

```
    <div class="grid grid-flow-col justify-items-center-safe ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

사용 가능한 공간이 충분하지 않을 때 `justify-items-center-safe` 유틸리티는 아이템을 가운데가 아니라 컨테이너의 시작 지점에 정렬합니다.

- 늘리기

`justify-items-stretch` 유틸리티를 사용해 아이템을 인라인 축을 따라 늘립니다:

01

02

03

04

05

06

```
    <div class="grid justify-items-stretch ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 반응형 디자인

`justify-items` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="grid justify-items-start md:justify-items-center ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
