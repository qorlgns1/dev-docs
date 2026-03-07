---
title: "rotate - 변환 - Tailwind CSS"
description: "`rotate-45`, `rotate-90` 같은 `rotate-<number>` 유틸리티를 사용해 요소를 각도 단위로 회전합니다:"
---

원본 URL: https://tailwindcss.com/docs/rotate

# rotate - 변환 - Tailwind CSS

| 클래스                         | 스타일                                                                              |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `rotate-none`                  | `rotate: none;`                                                                     |
| `rotate-<number>`              | `rotate: <number>deg;`                                                              |
| `-rotate-<number>`             | `rotate: calc(<number>deg * -1);`                                                   |
| `rotate-(<custom-property>)`   | `rotate: var(<custom-property>);`                                                   |
| `rotate-[<value>]`             | `rotate: <value>;`                                                                  |
| `rotate-x-<number>`            | `transform: rotateX(<number>deg) var(--tw-rotate-y);`                               |
| `-rotate-x-<number>`           | `transform: rotateX(-<number>deg) var(--tw-rotate-y);`                              |
| `rotate-x-(<custom-property>)` | `transform: rotateX(var(<custom-property>)) var(--tw-rotate-y);`                    |
| `rotate-x-[<value>]`           | `transform: rotateX(<value>) var(--tw-rotate-y);`                                   |
| `rotate-y-<number>`            | `transform: var(--tw-rotate-x) rotateY(<number>deg);`                               |
| `-rotate-y-<number>`           | `transform: var(--tw-rotate-x) rotateY(-<number>deg);`                              |
| `rotate-y-(<custom-property>)` | `transform: var(--tw-rotate-x) rotateY(var(<custom-property>));`                    |
| `rotate-y-[<value>]`           | `transform: var(--tw-rotate-x) rotateY(<value>);`                                   |
| `rotate-z-<number>`            | `transform: var(--tw-rotate-x) var(--tw-rotate-y) rotateZ(<number>deg);`            |
| `-rotate-z-<number>`           | `transform: var(--tw-rotate-x) var(--tw-rotate-y) rotateZ(-<number>deg);`           |
| `rotate-z-(<custom-property>)` | `transform: var(--tw-rotate-x) var(--tw-rotate-y) rotateZ(var(<custom-property>));` |
| `rotate-z-[<value>]`           | `transform: var(--tw-rotate-x) var(--tw-rotate-y) rotateZ(<value>);`                |

더 보기

## 예제

- 기본 예제

`rotate-45`, `rotate-90` 같은 `rotate-<number>` 유틸리티를 사용해 요소를 각도 단위로 회전합니다:

rotate-45

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

rotate-90

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

rotate-210

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="rotate-45 ..." src="/img/mountains.jpg" /><img class="rotate-90 ..." src="/img/mountains.jpg" /><img class="rotate-210 ..." src="/img/mountains.jpg" />
```

- 음수 값 사용하기

`-rotate-45`, `-rotate-90` 같은 `-rotate-<number>` 유틸리티를 사용해 요소를 각도 단위로 반시계 방향 회전합니다:

-rotate-45

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

-rotate-90

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

-rotate-210

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="-rotate-45 ..." src="/img/mountains.jpg" /><img class="-rotate-90 ..." src="/img/mountains.jpg" /><img class="-rotate-210 ..." src="/img/mountains.jpg" />
```

- 3D 공간에서 회전하기

`rotate-x-50`, `-rotate-y-30`, `rotate-z-45`처럼 `rotate-x-<number>`, `rotate-y-<number>`, `rotate-z-<number>` 유틸리티를 함께 사용해 요소를 3D 공간에서 회전합니다:

rotate-x-50

rotate-z-45

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

rotate-x-15

-rotate-y-30

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

rotate-y-25

rotate-z-30

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="rotate-x-50 rotate-z-45 ..." src="/img/mountains.jpg" /><img class="rotate-x-15 -rotate-y-30 ..." src="/img/mountains.jpg" /><img class="rotate-y-25 rotate-z-30 ..." src="/img/mountains.jpg" />
```

- 사용자 정의 값 사용하기

`rotate-[<value>]` 문법을 사용해 완전히 사용자 정의한 값으로 회전 값을 설정할 수 있습니다:

```
    <img class="rotate-[3.142rad] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `rotate-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="rotate-(--my-rotation) ..." src="/img/mountains.jpg" />
```

이 방식은 `var()` 함수를 자동으로 추가해 주는 `rotate-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`rotate` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <img class="rotate-45 md:rotate-60 ..." src="/img/mountains.jpg" />
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
