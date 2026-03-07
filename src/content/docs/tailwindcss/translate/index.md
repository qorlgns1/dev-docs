---
title: "translate - 변환 - Tailwind CSS"
description: "translate-2 및 -translate-4 같은 translate-<number> 유틸리티를 사용해 간격 스케일을 기준으로 요소를 양쪽 축에서 이동할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/translate

# translate - 변환 - Tailwind CSS

| 클래스                            | 스타일                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| `translate-<number>`              | `translate: calc(var(--spacing) * <number>) calc(var(--spacing) * <number>);`              |
| `-translate-<number>`             | `translate: calc(var(--spacing) * -<number>) calc(var(--spacing) * -<number>);`            |
| `translate-<fraction>`            | `translate: calc(<fraction> * 100%) calc(<fraction> * 100%);`                              |
| `-translate-<fraction>`           | `translate: calc(<fraction> * -100%) calc(<fraction> * -100%);`                            |
| `translate-full`                  | `translate: 100% 100%;`                                                                    |
| `-translate-full`                 | `translate: -100% -100%;`                                                                  |
| `translate-px`                    | `translate: 1px 1px;`                                                                      |
| `-translate-px`                   | `translate: -1px -1px;`                                                                    |
| `translate-(<custom-property>)`   | `translate: var(<custom-property>) var(<custom-property>);`                                |
| `translate-[<value>]`             | `translate: <value> <value>;`                                                              |
| `translate-x-<number>`            | `translate: calc(var(--spacing) * <number>) var(--tw-translate-y);`                        |
| `-translate-x-<number>`           | `translate: calc(var(--spacing) * -<number>) var(--tw-translate-y);`                       |
| `translate-x-<fraction>`          | `translate: calc(<fraction> * 100%) var(--tw-translate-y);`                                |
| `-translate-x-<fraction>`         | `translate: calc(<fraction> * -100%) var(--tw-translate-y);`                               |
| `translate-x-full`                | `translate: 100% var(--tw-translate-y);`                                                   |
| `-translate-x-full`               | `translate: -100% var(--tw-translate-y);`                                                  |
| `translate-x-px`                  | `translate: 1px var(--tw-translate-y);`                                                    |
| `-translate-x-px`                 | `translate: -1px var(--tw-translate-y);`                                                   |
| `translate-x-(<custom-property>)` | `translate: var(<custom-property>) var(--tw-translate-y);`                                 |
| `translate-x-[<value>]`           | `translate: <value> var(--tw-translate-y);`                                                |
| `translate-y-<number>`            | `translate: var(--tw-translate-x) calc(var(--spacing) * <number>);`                        |
| `-translate-y-<number>`           | `translate: var(--tw-translate-x) calc(var(--spacing) * -<number>);`                       |
| `translate-y-<fraction>`          | `translate: var(--tw-translate-x) calc(<fraction> * 100%);`                                |
| `-translate-y-<fraction>`         | `translate: var(--tw-translate-x) calc(<fraction> * -100%);`                               |
| `translate-y-full`                | `translate: var(--tw-translate-x) 100%;`                                                   |
| `-translate-y-full`               | `translate: var(--tw-translate-x) -100%;`                                                  |
| `translate-y-px`                  | `translate: var(--tw-translate-x) 1px;`                                                    |
| `-translate-y-px`                 | `translate: var(--tw-translate-x) -1px;`                                                   |
| `translate-y-(<custom-property>)` | `translate: var(--tw-translate-x) var(<custom-property>);`                                 |
| `translate-y-[<value>]`           | `translate: var(--tw-translate-x) <value>;`                                                |
| `translate-z-<number>`            | `translate: var(--tw-translate-x) var(--tw-translate-y) calc(var(--spacing) * <number>);`  |
| `-translate-z-<number>`           | `translate: var(--tw-translate-x) var(--tw-translate-y) calc(var(--spacing) * -<number>);` |
| `translate-z-px`                  | `translate: var(--tw-translate-x) var(--tw-translate-y) 1px;`                              |
| `-translate-z-px`                 | `translate: var(--tw-translate-x) var(--tw-translate-y) -1px;`                             |
| `translate-z-(<custom-property>)` | `translate: var(--tw-translate-x) var(--tw-translate-y) var(<custom-property>);`           |
| `translate-z-[<value>]`           | `translate: var(--tw-translate-x) var(--tw-translate-y) <value>;`                          |
| `translate-none`                  | `translate: none;`                                                                         |

더 보기

## 예제

- 간격 스케일 사용하기

`translate-2` 및 `-translate-4` 같은 `translate-<number>` 유틸리티를 사용해 간격 스케일을 기준으로 요소를 양쪽 축에서 이동할 수 있습니다:

-translate-6

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-2

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-8

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="-translate-6 ..." src="/img/mountains.jpg" /><img class="translate-2 ..." src="/img/mountains.jpg" /><img class="translate-8 ..." src="/img/mountains.jpg" />
```

- 백분율 사용하기

`translate-1/4` 및 `-translate-full` 같은 `translate-<fraction>` 유틸리티를 사용해 요소 크기 대비 백분율로 요소를 양쪽 축에서 이동할 수 있습니다:

-translate-1/4

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-1/6

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-1/2

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="-translate-1/4 ..." src="/img/mountains.jpg" /><img class="translate-1/6 ..." src="/img/mountains.jpg" /><img class="translate-1/2 ..." src="/img/mountains.jpg" />
```

- x축으로 이동하기

`translate-x-4` 및 `translate-x-1/4` 같은 `translate-x-<number>` 또는 `translate-x-<fraction>` 유틸리티를 사용해 요소를 x축으로 이동할 수 있습니다:

-translate-x-4

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-x-2

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-x-1/2

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="-translate-x-4 ..." src="/img/mountains.jpg" /><img class="translate-x-2 ..." src="/img/mountains.jpg" /><img class="translate-x-1/2 ..." src="/img/mountains.jpg" />
```

- y축으로 이동하기

`translate-y-6` 및 `translate-y-1/3` 같은 `translate-y-<number>` 또는 `translate-y-<fraction>` 유틸리티를 사용해 요소를 y축으로 이동할 수 있습니다:

-translate-y-4

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-y-2

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-y-1/2

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="-translate-y-4 ..." src="/img/mountains.jpg" /><img class="translate-y-2 ..." src="/img/mountains.jpg" /><img class="translate-y-1/2 ..." src="/img/mountains.jpg" />
```

- z축으로 이동하기

`translate-z-6` 및 `-translate-z-12` 같은 `translate-z-<number>` 유틸리티를 사용해 요소를 z축으로 이동할 수 있습니다:

-translate-z-8

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-z-4

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

translate-z-12

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="transform-3d">  <img class="-translate-z-8 rotate-x-50 rotate-z-45 ..." src="/img/mountains.jpg" />  <img class="translate-z-2 rotate-x-50 rotate-z-45 ..." src="/img/mountains.jpg" />  <img class="translate-z-1/2 rotate-x-50 rotate-z-45 ..." src="/img/mountains.jpg" /></div>
```

`translate-z-<number>` 유틸리티를 사용하려면 부모 요소에 `transform-3d` 유틸리티가 적용되어 있어야 합니다.

- 사용자 지정 값 사용하기

`translate-[<value>]` 문법을 사용해 완전히 사용자 지정한 값으로 이동을 설정할 수 있습니다:

```
    <img class="translate-[3.142rad] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `translate-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="translate-(--my-translate) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `translate-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `translate` 유틸리티 앞에 붙이면, 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <img class="translate-45 md:translate-60 ..." src="/img/mountains.jpg" />
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
