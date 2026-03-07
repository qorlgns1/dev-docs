---
title: "backdrop-filter - 필터 - Tailwind CSS"
description: "backdrop-blur-xs 및 backdrop-grayscale 같은 유틸리티를 사용해 요소의 배경(backdrop)에 필터를 적용할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/backdrop-filter

# backdrop-filter - 필터 - Tailwind CSS

| 클래스                                | 스타일                                     |
| ------------------------------------- | ------------------------------------------ |
| `backdrop-filter-none`                | `backdrop-filter: none;`                   |
| `backdrop-filter-(<custom-property>)` | `backdrop-filter: var(<custom-property>);` |
| `backdrop-filter-[<value>]`           | `backdrop-filter: <value>;`                |

## 예제

- 기본 예제

`backdrop-blur-xs` 및 `backdrop-grayscale` 같은 유틸리티를 사용해 요소의 배경(backdrop)에 필터를 적용할 수 있습니다:

backdrop-blur-xs

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-grayscale

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

조합

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-blur-xs ..."></div></div><div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-grayscale ..."></div></div><div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-blur-xs backdrop-grayscale ..."></div></div>
```

다음 backdrop filter 유틸리티를 조합할 수 있습니다: [blur](https://tailwindcss.com/docs/backdrop-filter-blur), [brightness](https://tailwindcss.com/docs/backdrop-filter-brightness), [contrast](https://tailwindcss.com/docs/backdrop-filter-contrast), [grayscale](https://tailwindcss.com/docs/backdrop-filter-grayscale), [hue-rotate](https://tailwindcss.com/docs/backdrop-filter-hue-rotate), [invert](https://tailwindcss.com/docs/backdrop-filter-invert), [opacity](https://tailwindcss.com/docs/backdrop-filter-opacity), [saturate](https://tailwindcss.com/docs/backdrop-filter-saturate), [sepia](https://tailwindcss.com/docs/backdrop-filter-sepia).

- 필터 제거

`backdrop-filter-none` 유틸리티를 사용하면 요소에 적용된 모든 backdrop 필터를 제거할 수 있습니다:

```
    <div class="backdrop-blur-md backdrop-brightness-150 md:backdrop-filter-none"></div>
```

- 사용자 정의 값 사용

`backdrop-filter-[<value>]` 문법을 사용해 완전히 사용자 정의한 값으로 backdrop 필터를 설정할 수 있습니다:

```
    <div class="backdrop-filter-[url('filters.svg#filter-id')] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-filter-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="backdrop-filter-(--my-backdrop-filter) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `backdrop-filter-[var(<custom-property>)]`의 단축 문법입니다.

- hover 시 적용

`backdrop-filter` 유틸리티 앞에 `hover:*` 같은 variant를 붙이면 해당 상태에서만 유틸리티가 적용됩니다:

```
    <div class="backdrop-blur-sm hover:backdrop-filter-none ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

- 반응형 디자인

`backdrop-filter` 유틸리티 앞에 `md:` 같은 breakpoint variant를 붙이면 중간 크기 이상의 화면에서만 유틸리티가 적용됩니다:

```
    <div class="backdrop-blur-sm md:backdrop-filter-none ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
