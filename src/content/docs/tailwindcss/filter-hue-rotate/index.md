---
title: "filter: hue-rotate() - 필터 - Tailwind CSS"
description: "hue-rotate-90, hue-rotate-180 같은 유틸리티를 사용해 요소의 색조를 각도 단위로 회전할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/filter-hue-rotate

# filter: hue-rotate() - 필터 - Tailwind CSS

| 클래스                           | 스타일                                        |
| -------------------------------- | --------------------------------------------- |
| `hue-rotate-<number>`            | `filter: hue-rotate(<number>deg);`            |
| `-hue-rotate-<number>`           | `filter: hue-rotate(calc(<number>deg * -1));` |
| `hue-rotate-(<custom-property>)` | `filter: hue-rotate(var(<custom-property>));` |
| `hue-rotate-[<value>]`           | `filter: hue-rotate(<value>);`                |

## 예제

- 기본 예제

`hue-rotate-90`, `hue-rotate-180` 같은 유틸리티를 사용해 요소의 색조를 각도 단위로 회전할 수 있습니다:

hue-rotate-15

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

hue-rotate-90

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

hue-rotate-180

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

hue-rotate-270

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="hue-rotate-15" src="/img/mountains.jpg" /><img class="hue-rotate-90" src="/img/mountains.jpg" /><img class="hue-rotate-180" src="/img/mountains.jpg" /><img class="hue-rotate-270" src="/img/mountains.jpg" />
```

- 음수 값 사용하기

`-hue-rotate-15`, `-hue-rotate-45` 같은 유틸리티를 사용해 음수 색조 회전 값을 설정할 수 있습니다:

-hue-rotate-15

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

-hue-rotate-45

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

-hue-rotate-90

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="-hue-rotate-15" src="/img/mountains.jpg" /><img class="-hue-rotate-45" src="/img/mountains.jpg" /><img class="-hue-rotate-90" src="/img/mountains.jpg" />
```

- 사용자 정의 값 사용하기

완전히 사용자 정의한 값을 기준으로 색조 회전을 설정하려면 `hue-rotate-[<value>]` 구문을 사용하세요:

```
    <img class="hue-rotate-[3.142rad] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `hue-rotate-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <img class="hue-rotate-(--my-hue-rotate) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `hue-rotate-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `filter: hue-rotate()` 유틸리티 앞에 붙이면, 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <img class="hue-rotate-60 md:hue-rotate-0 ..." src="/img/mountains.jpg" />
```

변형 사용 방법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
