---
title: "backdrop-filter: invert() - 필터 - Tailwind CSS"
description: "backdrop-invert, backdrop-invert-65 같은 유틸리티를 사용해 요소 배경의 색상 반전 정도를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/backdrop-filter-invert

# backdrop-filter: invert() - 필터 - Tailwind CSS

| 클래스                                | 스타일                                            |
| ------------------------------------- | ------------------------------------------------- |
| `backdrop-invert`                     | `backdrop-filter: invert(100%);`                  |
| `backdrop-invert-<number>`            | `backdrop-filter: invert(<number>%);`             |
| `backdrop-invert-(<custom-property>)` | `backdrop-filter: invert(var(<custom-property>))` |
| `backdrop-invert-[<value>]`           | `backdrop-filter: invert(<value>);`               |

## 예제

- 기본 예제

`backdrop-invert`, `backdrop-invert-65` 같은 유틸리티를 사용해 요소 배경의 색상 반전 정도를 제어하세요:

backdrop-invert-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-invert-65

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-invert

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert-0 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert-65 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert ..."></div></div>
```

- 사용자 정의 값 사용하기

`backdrop-invert-[<value>]` 문법을 사용해 완전히 사용자 정의한 값을 기준으로 배경 반전을 설정하세요:

```
    <div class="backdrop-invert-[.25] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-invert-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="backdrop-invert-(--my-backdrop-inversion) ...">  <!-- ... --></div>
```

이는 `backdrop-invert-[var(<custom-property>)]`의 단축 문법으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `backdrop-filter: invert()` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="backdrop-invert-0 md:backdrop-invert ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
