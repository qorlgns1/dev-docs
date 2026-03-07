---
title: "place-self - Flexbox 및 Grid - Tailwind CSS"
description: "컨테이너의 `place-items` 속성 값을 기준으로 항목을 정렬하려면 `place-self-auto`를 사용하세요:"
---

원본 URL: https://tailwindcss.com/docs/place-self

# place-self - Flexbox 및 Grid - Tailwind CSS

| 클래스                   | 스타일                     |
| ------------------------ | -------------------------- |
| `place-self-auto`        | `place-self: auto;`        |
| `place-self-start`       | `place-self: start;`       |
| `place-self-end`         | `place-self: end;`         |
| `place-self-end-safe`    | `place-self: safe end;`    |
| `place-self-center`      | `place-self: center;`      |
| `place-self-center-safe` | `place-self: safe center;` |
| `place-self-stretch`     | `place-self: stretch;`     |

## 예제

- 자동

컨테이너의 `place-items` 속성 값을 기준으로 항목을 정렬하려면 `place-self-auto`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-auto ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 시작

두 축 모두에서 항목을 시작 지점에 정렬하려면 `place-self-start`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-start ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 가운데

두 축 모두에서 항목을 중앙에 정렬하려면 `place-self-center`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-center ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 끝

두 축 모두에서 항목을 끝 지점에 정렬하려면 `place-self-end`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-end ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 늘이기

두 축 모두에서 항목을 늘이려면 `place-self-stretch`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-stretch ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `place-self` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <div class="place-self-start md:place-self-end ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
