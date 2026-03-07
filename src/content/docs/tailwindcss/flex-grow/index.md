---
title: "flex-grow - Flexbox 및 Grid - Tailwind CSS"
description: "grow를 사용하면 flex 아이템이 사용 가능한 공간을 채우도록 늘어날 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/flex-grow

# flex-grow - Flexbox 및 Grid - Tailwind CSS

| 클래스                     | 스타일                               |
| -------------------------- | ------------------------------------ |
| `grow`                     | `flex-grow: 1;`                      |
| `grow-<number>`            | `flex-grow: <number>;`               |
| `grow-[<value>]`           | `flex-grow: <value>;`                |
| `grow-(<custom-property>)` | `flex-grow: var(<custom-property>);` |

## 예제

- 아이템이 늘어나도록 허용하기

`grow`를 사용하면 flex 아이템이 사용 가능한 공간을 채우도록 늘어날 수 있습니다:

01

02

03

```
    <div class="flex ...">  <div class="size-14 flex-none ...">01</div>  <div class="size-14 grow ...">02</div>  <div class="size-14 flex-none ...">03</div></div>
```

- 계수에 따라 아이템 늘리기

`grow-3` 같은 `grow-<number>` 유틸리티를 사용하면 flex 아이템이 성장 계수에 비례하여 늘어나며, 서로에 대한 상대적인 비율로 사용 가능한 공간을 채울 수 있습니다:

01

02

03

```
    <div class="flex ...">  <div class="size-14 grow-3 ...">01</div>  <div class="size-14 grow-7 ...">02</div>  <div class="size-14 grow-3 ...">03</div></div>
```

- 아이템이 늘어나는 것 방지하기

`grow-0`를 사용하면 flex 아이템이 늘어나는 것을 방지할 수 있습니다:

01

02

03

```
    <div class="flex ...">  <div class="size-14 grow ...">01</div>  <div class="size-14 grow-0 ...">02</div>  <div class="size-14 grow ...">03</div></div>
```

- 커스텀 값 사용하기

`grow-[<value>]` 구문을 사용하면 완전히 커스텀한 값을 기준으로 flex grow 계수를 설정할 수 있습니다:

```
    <div class="grow-[25vw] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `grow-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="grow-(--my-grow) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `grow-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`flex-grow` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="grow md:grow-0 ...">  <!-- ... --></div>
```

변형 사용 방법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
