---
title: "order - Flexbox 및 Grid - Tailwind CSS"
description: "문서에 나타나는 순서와 다르게 flex 및 grid 아이템을 렌더링하려면 order-1, order-3 같은 order-<number> 유틸리티를 사용하세요:"
---

Source URL: https://tailwindcss.com/docs/order

# order - Flexbox 및 Grid - Tailwind CSS

| 클래스                      | 스타일                           |
| --------------------------- | -------------------------------- |
| `order-<number>`            | `order: <number>;`               |
| `-order-<number>`           | `order: calc(<number> * -1);`    |
| `order-first`               | `order: -9999;`                  |
| `order-last`                | `order: 9999;`                   |
| `order-none`                | `order: 0;`                      |
| `order-(<custom-property>)` | `order: var(<custom-property>);` |
| `order-[<value>]`           | `order: <value>;`                |

## 예제

- 정렬 순서 명시적으로 설정하기

문서에 나타나는 순서와 다르게 flex 및 grid 아이템을 렌더링하려면 `order-1`, `order-3` 같은 `order-<number>` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex justify-between ...">  <div class="order-3 ...">01</div>  <div class="order-1 ...">02</div>  <div class="order-2 ...">03</div></div>
```

- 아이템을 처음 또는 마지막에 배치하기

flex 및 grid 아이템을 처음이나 마지막에 렌더링하려면 `order-first` 및 `order-last` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex justify-between ...">  <div class="order-last ...">01</div>  <div class="...">02</div>  <div class="order-first ...">03</div></div>
```

- 음수 값 사용하기

음수 order 값을 사용하려면 클래스 이름 앞에 대시를 붙여 음수 값으로 변환하세요:

```
    <div class="-order-1">  <!-- ... --></div>
```

- 사용자 정의 값 사용하기

완전히 사용자 정의한 값으로 order를 설정하려면 `order-[<value>]` 구문을 사용하세요:

```
    <div class="order-[min(var(--total-items),10)] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `order-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="order-(--my-order) ...">  <!-- ... --></div>
```

이는 `order-[var(<custom-property>)]`의 단축 구문으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `order` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="order-first md:order-last ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
