---
title: "flex-shrink - Flexbox & Grid - Tailwind CSS"
description: "필요한 경우 플렉스 아이템이 줄어들 수 있도록 shrink를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/flex-shrink

# flex-shrink - Flexbox & Grid - Tailwind CSS

| Class                        | Styles                                 |
| ---------------------------- | -------------------------------------- |
| `shrink`                     | `flex-shrink: 1;`                      |
| `shrink-<number>`            | `flex-shrink: <number>;`               |
| `shrink-[<value>]`           | `flex-shrink: <value>;`                |
| `shrink-(<custom-property>)` | `flex-shrink: var(<custom-property>);` |

## 예제

- 플렉스 아이템 축소 허용

필요한 경우 플렉스 아이템이 줄어들 수 있도록 `shrink`를 사용하세요:

01

02

03

```
    <div class="flex ...">  <div class="h-14 w-14 flex-none ...">01</div>  <div class="h-14 w-64 shrink ...">02</div>  <div class="h-14 w-14 flex-none ...">03</div></div>
```

- 아이템 축소 방지

플렉스 아이템이 줄어들지 않도록 `shrink-0`을 사용하세요:

01

02

03

```
    <div class="flex ...">  <div class="h-16 flex-1 ...">01</div>  <div class="h-16 w-32 shrink-0 ...">02</div>  <div class="h-16 flex-1 ...">03</div></div>
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값으로 flex shrink 계수를 설정하려면 `shrink-[<value>]` 구문을 사용하세요:

```
    <div class="shrink-[calc(100vw-var(--sidebar))] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `shrink-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="shrink-(--my-shrink) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `shrink-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `flex-shrink` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="shrink md:shrink-0 ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
