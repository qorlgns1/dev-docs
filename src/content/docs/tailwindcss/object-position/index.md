---
title: "object-position - 레이아웃 - Tailwind CSS"
description: " 및  같은 유틸리티를 사용해 대체 요소의 콘텐츠가 컨테이너 내에서 어떻게 배치될지 지정하세요:"
---

소스 URL: https://tailwindcss.com/docs/object-position

# object-position - 레이아웃 - Tailwind CSS

| 클래스                       | 스타일                                     |
| ---------------------------- | ------------------------------------------ |
| `object-top-left`            | `object-position: top left;`               |
| `object-top`                 | `object-position: top;`                    |
| `object-top-right`           | `object-position: top right;`              |
| `object-left`                | `object-position: left;`                   |
| `object-center`              | `object-position: center;`                 |
| `object-right`               | `object-position: right;`                  |
| `object-bottom-left`         | `object-position: bottom left;`            |
| `object-bottom`              | `object-position: bottom;`                 |
| `object-bottom-right`        | `object-position: bottom right;`           |
| `object-(<custom-property>)` | `object-position: var(<custom-property>);` |
| `object-[<value>]`           | `object-position: <value>;`                |

## 예제

- 기본 예제

`object-left` 및 `object-bottom-right` 같은 유틸리티를 사용해 대체 요소의 콘텐츠가 컨테이너 내에서 어떻게 배치될지 지정하세요:

전체 이미지를 보려면 예제 위에 마우스를 올리세요

object-top-left

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

object-top

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

object-top-right

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

object-left

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

object-center

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

object-right

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

object-bottom-left

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

object-bottom

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

object-bottom-right

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="size-24 object-top-left ..." src="/img/mountains.jpg" /><img class="size-24 object-top ..." src="/img/mountains.jpg" /><img class="size-24 object-top-right ..." src="/img/mountains.jpg" /><img class="size-24 object-left ..." src="/img/mountains.jpg" /><img class="size-24 object-center ..." src="/img/mountains.jpg" /><img class="size-24 object-right ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom-left ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom-right ..." src="/img/mountains.jpg" />
```

- 커스텀 값 사용하기

`object-[<value>]` 문법을 사용해 완전히 커스텀한 값을 기준으로 object position을 설정하세요:

```
    <img class="object-[25%_75%] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `object-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="object-(--my-object) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `object-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `object-position` 유틸리티 앞에 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <img class="object-center md:object-top ..." src="/img/mountains.jpg" />
```

변형 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
