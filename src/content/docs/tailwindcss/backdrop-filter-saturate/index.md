---
title: "backdrop-filter: saturate() - 필터 - Tailwind CSS"
description: "backdrop-saturate-50 및 backdrop-saturate-100 같은 유틸리티를 사용해 요소 배경의 채도를 제어할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/backdrop-filter-saturate

# backdrop-filter: saturate() - 필터 - Tailwind CSS

| Class                                   | Styles                                               |
| --------------------------------------- | ---------------------------------------------------- |
| `backdrop-saturate-<number>`            | `backdrop-filter: saturate(<number>%);`              |
| `backdrop-saturate-(<custom-property>)` | `backdrop-filter: saturate(var(<custom-property>));` |
| `backdrop-saturate-[<value>]`           | `backdrop-filter: saturate(<value>);`                |

## 예제

- 기본 예제

`backdrop-saturate-50` 및 `backdrop-saturate-100` 같은 유틸리티를 사용해 요소 배경의 채도를 제어할 수 있습니다:

backdrop-saturate-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-saturate-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-saturate-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-saturate-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-saturate-125 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-saturate-200 ..."></div></div>
```

- 사용자 지정 값 사용하기

`backdrop-saturate-[<value>]` 구문을 사용하면 완전히 사용자 지정한 값을 기준으로 배경 채도를 설정할 수 있습니다:

```
    <div class="backdrop-saturate-[.25] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-saturate-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="backdrop-saturate-(--my-backdrop-saturation) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `backdrop-saturate-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`backdrop-filter: saturate()` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="backdrop-saturate-50 md:backdrop-saturate-150 ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
