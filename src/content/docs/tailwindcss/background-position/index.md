---
title: "background-position - 배경 - Tailwind CSS"
description: "요소의 배경 이미지 위치를 제어하려면 bg-center, bg-right, bg-top-left 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/background-position

# background-position - 배경 - Tailwind CSS

| 클래스                            | 스타일                                         |
| --------------------------------- | ---------------------------------------------- |
| `bg-top-left`                     | `background-position: top left;`               |
| `bg-top`                          | `background-position: top;`                    |
| `bg-top-right`                    | `background-position: top right;`              |
| `bg-left`                         | `background-position: left;`                   |
| `bg-center`                       | `background-position: center;`                 |
| `bg-right`                        | `background-position: right;`                  |
| `bg-bottom-left`                  | `background-position: bottom left;`            |
| `bg-bottom`                       | `background-position: bottom;`                 |
| `bg-bottom-right`                 | `background-position: bottom right;`           |
| `bg-position-(<custom-property>)` | `background-position: var(<custom-property>);` |
| `bg-position-[<value>]`           | `background-position: <value>;`                |

## 예제

- 기본 예제

요소의 배경 이미지 위치를 제어하려면 `bg-center`, `bg-right`, `bg-top-left` 같은 유틸리티를 사용하세요:

전체 이미지를 보려면 아래 예제에 마우스를 올려보세요

bg-top-left

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

bg-top

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

bg-top-right

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

bg-left

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

bg-center

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

bg-right

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

bg-bottom-left

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

bg-bottom

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

bg-bottom-right

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)] bg-top-left"></div><div class="bg-[url(/img/mountains.jpg)] bg-top"></div><div class="bg-[url(/img/mountains.jpg)] bg-top-right"></div><div class="bg-[url(/img/mountains.jpg)] bg-left"></div><div class="bg-[url(/img/mountains.jpg)] bg-center"></div><div class="bg-[url(/img/mountains.jpg)] bg-right"></div><div class="bg-[url(/img/mountains.jpg)] bg-bottom-left"></div><div class="bg-[url(/img/mountains.jpg)] bg-bottom"></div><div class="bg-[url(/img/mountains.jpg)] bg-bottom-right"></div>
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값으로 배경 위치를 설정하려면 `bg-position-[<value>]` 구문을 사용하세요:

```
    <div class="bg-position-[center_top_1rem] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `bg-position-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="bg-position-(--my-bg-position) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `bg-position-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`background-position` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="bg-center md:bg-top ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
