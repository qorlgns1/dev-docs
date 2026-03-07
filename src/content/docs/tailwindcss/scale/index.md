---
title: "scale - 변환 - Tailwind CSS"
description: "원래 크기의 백분율로 요소 크기를 조정하려면 `scale-75`, `scale-150` 같은 `scale-<number>` 유틸리티를 사용하세요:"
---

원본 URL: https://tailwindcss.com/docs/scale

# scale - 변환 - Tailwind CSS

| 클래스                        | 스타일                                                               |
| ----------------------------- | -------------------------------------------------------------------- |
| `scale-none`                  | `scale: none;`                                                       |
| `scale-<number>`              | `scale: <number>% <number>%;`                                        |
| `-scale-<number>`             | `scale: calc(<number>% * -1) calc(<number>% * -1);`                  |
| `scale-(<custom-property>)`   | `scale: var(<custom-property>) var(<custom-property>);`              |
| `scale-[<value>]`             | `scale: <value>;`                                                    |
| `scale-x-<number>`            | `scale: <number>% var(--tw-scale-y);`                                |
| `-scale-x-<number>`           | `scale: calc(<number>% * -1) var(--tw-scale-y);`                     |
| `scale-x-(<custom-property>)` | `scale: var(<custom-property>) var(--tw-scale-y);`                   |
| `scale-x-[<value>]`           | `scale: <value> var(--tw-scale-y);`                                  |
| `scale-y-<number>`            | `scale: var(--tw-scale-x) <number>%;`                                |
| `-scale-y-<number>`           | `scale: var(--tw-scale-x) calc(<number>% * -1);`                     |
| `scale-y-(<custom-property>)` | `scale: var(--tw-scale-x) var(<custom-property>);`                   |
| `scale-y-[<value>]`           | `scale: var(--tw-scale-x) <value>;`                                  |
| `scale-z-<number>`            | `scale: var(--tw-scale-x) var(--tw-scale-y) <number>%;`              |
| `-scale-z-<number>`           | `scale: var(--tw-scale-x) var(--tw-scale-y) calc(<number>% * -1);`   |
| `scale-z-(<custom-property>)` | `scale: var(--tw-scale-x) var(--tw-scale-y) var(<custom-property>);` |
| `scale-z-[<value>]`           | `scale: var(--tw-scale-x) var(--tw-scale-y) <value>;`                |
| `scale-3d`                    | `scale: var(--tw-scale-x) var(--tw-scale-y) var(--tw-scale-z);`      |

더 보기

## 예제

- 기본 예제

`scale-75`, `scale-150` 같은 `scale-<number>` 유틸리티를 사용해 요소를 원래 크기의 백분율만큼 스케일하세요:

scale-75

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

scale-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

scale-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="scale-75 ..." src="/img/mountains.jpg" /><img class="scale-100 ..." src="/img/mountains.jpg" /><img class="scale-125 ..." src="/img/mountains.jpg" />
```

- x축에서 스케일링

`scale-x-75`, `-scale-x-150` 같은 `scale-x-<number>` 유틸리티를 사용해 요소를 원래 너비의 백분율만큼 x축에서 스케일하세요:

scale-x-75

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

scale-x-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

scale-x-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="scale-x-75 ..." src="/img/mountains.jpg" /><img class="scale-x-100 ..." src="/img/mountains.jpg" /><img class="scale-x-125 ..." src="/img/mountains.jpg" />
```

- y축에서 스케일링

`scale-y-75`, `scale-y-150` 같은 `scale-y-<number>` 유틸리티를 사용해 요소를 원래 높이의 백분율만큼 y축에서 스케일하세요:

scale-y-75

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

scale-y-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

scale-y-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="scale-y-75 ..." src="/img/mountains.jpg" /><img class="scale-y-100 ..." src="/img/mountains.jpg" /><img class="scale-y-125 ..." src="/img/mountains.jpg" />
```

- 음수 값 사용

`-scale-x-75`, `-scale-125` 같은 `-scale-<number>`, `-scale-x-<number>`, `-scale-y-<number>` 유틸리티를 사용해 요소를 반전(mirror)하고 원래 크기의 백분율만큼 축소하세요:

-scale-x-75

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

-scale-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

-scale-y-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="-scale-x-75 ..." src="/img/mountains.jpg" /><img class="-scale-100 ..." src="/img/mountains.jpg" /><img class="-scale-y-125 ..." src="/img/mountains.jpg" />
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값으로 scale을 설정하려면 `scale-[<value>]` 문법을 사용하세요:

```
    <img class="scale-[1.7] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `scale-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="scale-(--my-scale) ..." src="/img/mountains.jpg" />
```

이 문법은 `var()` 함수를 자동으로 추가해 주는 `scale-[var(<custom-property>)]`의 단축 표현일 뿐입니다.

- hover에서 적용

`hover:*` 같은 variant를 `scale` 유틸리티 앞에 붙이면 해당 상태에서만 유틸리티가 적용됩니다:

```
    <img class="scale-95 hover:scale-120 ..." src="/img/mountains.jpg" />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
