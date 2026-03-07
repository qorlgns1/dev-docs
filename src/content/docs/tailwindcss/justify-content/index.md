---
title: "justify-content - Flexbox & Grid - Tailwind CSS"
description: "justify-start 유틸리티를 사용해 아이템을 컨테이너 주축의 시작 지점에 정렬합니다:"
---

출처 URL: https://tailwindcss.com/docs/justify-content

# justify-content - Flexbox & Grid - Tailwind CSS

| 클래스                | 스타일                            |
| --------------------- | --------------------------------- |
| `justify-start`       | `justify-content: flex-start;`    |
| `justify-end`         | `justify-content: flex-end;`      |
| `justify-end-safe`    | `justify-content: safe flex-end;` |
| `justify-center`      | `justify-content: center;`        |
| `justify-center-safe` | `justify-content: safe center;`   |
| `justify-between`     | `justify-content: space-between;` |
| `justify-around`      | `justify-content: space-around;`  |
| `justify-evenly`      | `justify-content: space-evenly;`  |
| `justify-stretch`     | `justify-content: stretch;`       |
| `justify-baseline`    | `justify-content: baseline;`      |
| `justify-normal`      | `justify-content: normal;`        |

## Examples

- 시작

`justify-start` 유틸리티를 사용해 아이템을 컨테이너 주축의 시작 지점에 정렬합니다:

01

02

03

```
    <div class="flex justify-start ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 가운데

`justify-center` 또는 `justify-center-safe` 유틸리티를 사용해 아이템을 컨테이너 주축의 중앙에 정렬합니다:

컨테이너 크기를 조절해 정렬 동작을 확인해 보세요

justify-center

01

02

03

04

justify-center-safe

01

02

03

04

justify-center

```
    <div class="flex justify-center ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

justify-center-safe

```
    <div class="flex justify-center-safe ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

사용 가능한 공간이 충분하지 않으면 `justify-center-safe` 유틸리티는 아이템을 중앙이 아니라 컨테이너의 시작 지점에 정렬합니다.

- 끝

`justify-end` 또는 `justify-end-safe` 유틸리티를 사용해 아이템을 컨테이너 주축의 끝 지점에 정렬합니다:

컨테이너 크기를 조절해 정렬 동작을 확인해 보세요

justify-end

01

02

03

04

justify-end-safe

01

02

03

04

justify-end

```
    <div class="flex justify-end ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>03</div></div>
```

justify-end-safe

```
    <div class="flex justify-end-safe ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>03</div></div>
```

사용 가능한 공간이 충분하지 않으면 `justify-end-safe` 유틸리티는 아이템을 끝이 아니라 컨테이너의 시작 지점에 정렬합니다.

- 아이템 사이 간격

`justify-between` 유틸리티를 사용해 각 아이템 사이의 간격이 동일해지도록 컨테이너 주축을 따라 아이템을 정렬합니다:

01

02

03

```
    <div class="flex justify-between ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 아이템 둘레 간격

`justify-around` 유틸리티를 사용해 각 아이템의 양옆 간격이 동일해지도록 컨테이너 주축을 따라 아이템을 정렬합니다:

01

02

03

```
    <div class="flex justify-around ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 균등 간격

`justify-evenly` 유틸리티를 사용해 각 아이템 주위 간격이 동일해지도록 컨테이너 주축을 따라 아이템을 정렬합니다. 또한 `justify-around` 사용 시 보통 아이템 사이에 보이는 두 배 간격도 보정합니다:

01

02

03

```
    <div class="flex justify-evenly ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 늘리기

`justify-stretch` 유틸리티를 사용해 자동 크기 콘텐츠 아이템이 컨테이너 주축의 사용 가능한 공간을 채우도록 합니다:

01

02

03

```
    <div class="grid grid-cols-[4rem_auto_4rem] justify-stretch ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 기본값

`justify-normal` 유틸리티를 사용해 `justify-content` 값을 설정하지 않은 것처럼 콘텐츠 아이템을 기본 위치로 배치합니다:

01

02

03

```
    <div class="flex justify-normal ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 반응형 디자인

`justify-content` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="flex justify-start md:justify-between ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
