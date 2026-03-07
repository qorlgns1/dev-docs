---
title: "justify-self - Flexbox & Grid - Tailwind CSS"
description: "그리드의 justify-items 속성 값을 기준으로 항목을 정렬하려면 justify-self-auto 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/justify-self

# justify-self - Flexbox & Grid - Tailwind CSS

| 클래스                     | 스타일                       |
| -------------------------- | ---------------------------- |
| `justify-self-auto`        | `justify-self: auto;`        |
| `justify-self-start`       | `justify-self: start;`       |
| `justify-self-center`      | `justify-self: center;`      |
| `justify-self-center-safe` | `justify-self: safe center;` |
| `justify-self-end`         | `justify-self: end;`         |
| `justify-self-end-safe`    | `justify-self: safe end;`    |
| `justify-self-stretch`     | `justify-self: stretch;`     |

## 예제

- 자동

그리드의 `justify-items` 속성 값을 기준으로 항목을 정렬하려면 `justify-self-auto` 유틸리티를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid justify-items-stretch ...">  <!-- ... -->  <div class="justify-self-auto ...">02</div>  <!-- ... --></div>
```

- 시작

그리드 항목을 인라인 축의 시작 지점에 정렬하려면 `justify-self-start` 유틸리티를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid justify-items-stretch ...">  <!-- ... -->  <div class="justify-self-start ...">02</div>  <!-- ... --></div>
```

- 가운데

그리드 항목을 인라인 축의 중앙에 정렬하려면 `justify-self-center` 또는 `justify-self-center-safe` 유틸리티를 사용하세요:

정렬 동작을 확인하려면 컨테이너 크기를 조절하세요

justify-self-center

01

02

03

justify-self-center-safe

01

02

03

justify-self-center

```
    <div class="grid justify-items-stretch ...">  <!-- ... -->  <div class="justify-self-center ...">02</div>  <!-- ... --></div>
```

justify-self-center-safe

```
    <div class="grid justify-items-stretch ...">  <!-- ... -->  <div class="justify-self-center-safe ...">02</div>  <!-- ... --></div>
```

사용 가능한 공간이 충분하지 않으면 `justify-self-center-safe` 유틸리티는 항목을 끝이 아니라 컨테이너의 시작 지점에 정렬합니다.

- 끝

그리드 항목을 인라인 축의 끝 지점에 정렬하려면 `justify-self-end` 또는 `justify-self-end-safe` 유틸리티를 사용하세요:

정렬 동작을 확인하려면 컨테이너 크기를 조절하세요

justify-self-end

01

02

03

justify-self-end-safe

01

02

03

justify-self-end

```
    <div class="grid justify-items-stretch ...">  <!-- ... -->  <div class="justify-self-end ...">02</div>  <!-- ... --></div>
```

justify-self-end-safe

```
    <div class="grid justify-items-stretch ...">  <!-- ... -->  <div class="justify-self-end-safe ...">02</div>  <!-- ... --></div>
```

사용 가능한 공간이 충분하지 않으면 `justify-self-end-safe` 유틸리티는 항목을 끝이 아니라 컨테이너의 시작 지점에 정렬합니다.

- 늘리기

그리드 항목을 인라인 축에서 그리드 영역을 채우도록 늘리려면 `justify-self-stretch` 유틸리티를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid justify-items-start ...">  <!-- ... -->  <div class="justify-self-stretch ...">02</div>  <!-- ... --></div>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `justify-self` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="justify-self-start md:justify-self-end ...">  <!-- ... --></div>
```

variants 사용 방법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
