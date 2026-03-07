---
title: "backdrop-filter: hue-rotate() - 필터 - Tailwind CSS"
description: "backdrop-hue-rotate-90 및 backdrop-hue-rotate-180 같은 유틸리티를 사용해 요소 배경의 색조를 회전할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/backdrop-filter-hue-rotate

# backdrop-filter: hue-rotate() - 필터 - Tailwind CSS

| 클래스                                    | 스타일                                                 |
| ----------------------------------------- | ------------------------------------------------------ |
| `backdrop-hue-rotate-<number>`            | `backdrop-filter: hue-rotate(<number>deg);`            |
| `-backdrop-hue-rotate-<number>`           | `backdrop-filter: hue-rotate(calc(<number>deg * -1));` |
| `backdrop-hue-rotate-(<custom-property>)` | `backdrop-filter: hue-rotate(var(<custom-property>));` |
| `backdrop-hue-rotate-[<value>]`           | `backdrop-filter: hue-rotate(<value>);`                |

## 예제

- 기본 예제

`backdrop-hue-rotate-90` 및 `backdrop-hue-rotate-180` 같은 유틸리티를 사용해 요소 배경의 색조를 회전할 수 있습니다:

backdrop-hue-rotate-90

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-hue-rotate-180

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-hue-rotate-270

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-hue-rotate-90 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-hue-rotate-180 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-hue-rotate-270 ..."></div></div>
```

- 음수 값 사용하기

`-backdrop-hue-rotate-90` 및 `-backdrop-hue-rotate-180` 같은 유틸리티를 사용해 음수 배경 색조 회전 값을 설정할 수 있습니다:

-backdrop-hue-rotate-15

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

-backdrop-hue-rotate-45

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

-backdrop-hue-rotate-90

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 -backdrop-hue-rotate-15 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 -backdrop-hue-rotate-45 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 -backdrop-hue-rotate-90 ..."></div></div>
```

- 사용자 지정 값 사용하기

`backdrop-hue-rotate-[<value>]` 구문을 사용하면 완전히 사용자 지정한 값을 기반으로 배경 색조 회전을 설정할 수 있습니다:

```
    <div class="backdrop-hue-rotate-[3.142rad] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-hue-rotate-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="backdrop-hue-rotate-(--my-backdrop-hue-rotation) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `backdrop-hue-rotate-[var(<custom-property>)]`의 단축 구문입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `backdrop-filter: hue-rotate()` 유틸리티 앞에 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="backdrop-hue-rotate-15 md:backdrop-hue-rotate-0 ...">  <!-- ... --></div>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
