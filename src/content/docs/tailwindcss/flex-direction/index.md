---
title: "flex-direction - Flexbox 및 Grid - Tailwind CSS"
description: "텍스트와 같은 방향으로 flex 항목을 가로로 배치하려면 flex-row를 사용하세요:"
---

# flex-direction - Flexbox 및 Grid - Tailwind CSS

| 클래스             | 스타일                            |
| ------------------ | --------------------------------- |
| `flex-row`         | `flex-direction: row;`            |
| `flex-row-reverse` | `flex-direction: row-reverse;`    |
| `flex-col`         | `flex-direction: column;`         |
| `flex-col-reverse` | `flex-direction: column-reverse;` |

## 예제

- 행

텍스트와 같은 방향으로 flex 항목을 가로로 배치하려면 `flex-row`를 사용하세요:

01

02

03

```
    <div class="flex flex-row ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 행 반전

반대 방향으로 flex 항목을 가로로 배치하려면 `flex-row-reverse`를 사용하세요:

01

02

03

```
    <div class="flex flex-row-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 열

flex 항목을 세로로 배치하려면 `flex-col`을 사용하세요:

01

02

03

```
    <div class="flex flex-col ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 열 반전

반대 방향으로 flex 항목을 세로로 배치하려면 `flex-col-reverse`를 사용하세요:

01

02

03

```
    <div class="flex flex-col-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 반응형 디자인

중간 크기 화면 이상에서만 유틸리티를 적용하려면 `flex-direction` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="flex flex-col md:flex-row ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
