---
title: "filter: invert() - 필터 - Tailwind CSS"
description: "요소의 색상 반전을 제어하려면 invert, invert-20 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/filter-invert

# filter: invert() - 필터 - Tailwind CSS

| 클래스                       | 스타일                                    |
| ---------------------------- | ----------------------------------------- |
| `invert`                     | `filter: invert(100%);`                   |
| `invert-<number>`            | `filter: invert(<number>%);`              |
| `invert-(<custom-property>)` | `filter: invert(var(<custom-property>));` |
| `invert-[<value>]`           | `filter: invert(<value>);`                |

## 예제

- 기본 예제

요소의 색상 반전을 제어하려면 `invert`, `invert-20` 같은 유틸리티를 사용하세요:

invert-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

invert-20

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

invert

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="invert-0" src="/img/mountains.jpg" /><img class="invert-20" src="/img/mountains.jpg" /><img class="invert" src="/img/mountains.jpg" />
```

- 사용자 지정 값 사용

색상 반전 값을 완전히 사용자 지정하려면 `invert-[<value>]` 구문을 사용하세요:

```
    <img class="invert-[.25] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `invert-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <img class="invert-(--my-inversion) ..." src="/img/mountains.jpg" />
```

이 구문은 `invert-[var(<custom-property>)]`의 축약형으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

중간 크기 이상의 화면에서만 유틸리티를 적용하려면 `filter: invert()` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <img class="invert md:invert-0 ..." src="/img/mountains.jpg" />
```

variant 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
