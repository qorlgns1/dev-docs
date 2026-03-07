---
title: "filter: brightness() - 필터 - Tailwind CSS"
description: "요소의 밝기를 제어하려면 brightness-50, brightness-100 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/filter-brightness

# filter: brightness() - 필터 - Tailwind CSS

| 클래스                           | 스타일                                        |
| -------------------------------- | --------------------------------------------- |
| `brightness-<number>`            | `filter: brightness(<number>%);`              |
| `brightness-(<custom-property>)` | `filter: brightness(var(<custom-property>));` |
| `brightness-[<value>]`           | `filter: brightness(<value>);`                |

## 예제

- 기본 예제

요소의 밝기를 제어하려면 `brightness-50`, `brightness-100` 같은 유틸리티를 사용하세요:

brightness-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

brightness-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

brightness-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

brightness-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="brightness-50 ..." src="/img/mountains.jpg" /><img class="brightness-100 ..." src="/img/mountains.jpg" /><img class="brightness-125 ..." src="/img/mountains.jpg" /><img class="brightness-200 ..." src="/img/mountains.jpg" />
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값을 기준으로 밝기를 설정하려면 `brightness-[<value>]` 구문을 사용하세요:

```
    <img class="brightness-[1.75] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `brightness-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <img class="brightness-(--my-brightness) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `brightness-[var(<custom-property>)]`의 단축 구문입니다.

- 반응형 디자인

`filter: brightness()` 유틸리티에 `md:` 같은 브레이크포인트 variant를 접두사로 붙이면, 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <img class="brightness-110 md:brightness-150 ..." src="/img/mountains.jpg" />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
