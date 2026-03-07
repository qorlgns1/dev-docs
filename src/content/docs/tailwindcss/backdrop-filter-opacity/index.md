---
title: "backdrop-filter: opacity() - 필터 - Tailwind CSS"
description: "backdrop-opacity-50, backdrop-opacity-75 같은 유틸리티를 사용해 요소에 적용된 모든 백드롭 필터의 opacity를 제어할 수 있습니다:"
---

# backdrop-filter: opacity() - 필터 - Tailwind CSS

| 클래스                                 | 스타일                                              |
| -------------------------------------- | --------------------------------------------------- |
| `backdrop-opacity-<number>`            | `backdrop-filter: opacity(<number>%);`              |
| `backdrop-opacity-(<custom-property>)` | `backdrop-filter: opacity(var(<custom-property>));` |
| `backdrop-opacity-[<value>]`           | `backdrop-filter: opacity(<value>);`                |

## 예제

- 기본 예제

`backdrop-opacity-50`, `backdrop-opacity-75` 같은 유틸리티를 사용해 요소에 적용된 모든 백드롭 필터의 opacity를 제어할 수 있습니다:

backdrop-opacity-10

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-opacity-60

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-opacity-95

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert backdrop-opacity-10 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert backdrop-opacity-60 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert backdrop-opacity-95 ..."></div></div>
```

- 사용자 정의 값 사용

`backdrop-opacity-[<value>]` 문법을 사용하면 완전히 사용자 정의한 값으로 backdrop filter opacity를 설정할 수 있습니다:

```
    <div class="backdrop-opacity-[.15] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-opacity-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="backdrop-opacity-(--my-backdrop-filter-opacity) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `backdrop-opacity-[var(<custom-property>)]`의 축약 문법입니다.

- 반응형 디자인

`backdrop-filter: opacity()` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 유틸리티가 적용됩니다:

```
    <div class="backdrop-opacity-100 md:backdrop-opacity-60 ...">  <!-- ... --></div>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
