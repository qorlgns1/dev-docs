---
title: "transform-origin - 변환 - Tailwind CSS"
description: "origin-top, origin-bottom-left 같은 유틸리티를 사용해 요소의 transform origin을 설정할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/transform-origin

# transform-origin - 변환 - Tailwind CSS

| 클래스                       | 스타일                                      |
| ---------------------------- | ------------------------------------------- |
| `origin-center`              | `transform-origin: center;`                 |
| `origin-top`                 | `transform-origin: top;`                    |
| `origin-top-right`           | `transform-origin: top right;`              |
| `origin-right`               | `transform-origin: right;`                  |
| `origin-bottom-right`        | `transform-origin: bottom right;`           |
| `origin-bottom`              | `transform-origin: bottom;`                 |
| `origin-bottom-left`         | `transform-origin: bottom left;`            |
| `origin-left`                | `transform-origin: left;`                   |
| `origin-top-left`            | `transform-origin: top left;`               |
| `origin-(<custom-property>)` | `transform-origin: var(<custom-property>);` |
| `origin-[<value>]`           | `transform-origin: <value>;`                |

## 예제

- 기본 예제

`origin-top`, `origin-bottom-left` 같은 유틸리티를 사용해 요소의 transform origin을 설정할 수 있습니다:

origin-center

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

origin-top-left

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

origin-bottom

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="origin-center rotate-45 ..." src="/img/mountains.jpg" /><img class="origin-top-left rotate-12 ..." src="/img/mountains.jpg" /><img class="origin-bottom -rotate-12 ..." src="/img/mountains.jpg" />
```

- 사용자 정의 값 사용하기

`origin-[<value>]` 문법을 사용하면 완전히 사용자 정의한 값으로 transform origin을 설정할 수 있습니다:

```
    <img class="origin-[33%_75%] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `origin-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="origin-(--my-transform-origin) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `origin-[var(<custom-property>)]`의 축약 문법입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `transform-origin` 유틸리티 앞에 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <img class="origin-center md:origin-top ..." src="/img/mountains.jpg" />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
