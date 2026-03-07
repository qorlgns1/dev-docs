---
title: "filter - 필터 - Tailwind CSS"
description: "blur-xs 및 grayscale 같은 유틸리티를 사용해 요소에 필터를 적용합니다:"
---

# filter - 필터 - Tailwind CSS

| 클래스                       | 스타일                            |
| ---------------------------- | --------------------------------- |
| `filter-none`                | `filter: none;`                   |
| `filter-(<custom-property>)` | `filter: var(<custom-property>);` |
| `filter-[<value>]`           | `filter: <value>;`                |

## 예제

- 기본 예제

`blur-xs` 및 `grayscale` 같은 유틸리티를 사용해 요소에 필터를 적용합니다:

blur-xs

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

grayscale

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

결합

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="blur-xs" src="/img/mountains.jpg" /><img class="grayscale" src="/img/mountains.jpg" /><img class="blur-xs grayscale" src="/img/mountains.jpg" />
```

다음 필터 유틸리티를 조합할 수 있습니다: [blur](https://tailwindcss.com/docs/filter-blur), [brightness](https://tailwindcss.com/docs/filter-brightness), [contrast](https://tailwindcss.com/docs/filter-contrast), [drop-shadow](https://tailwindcss.com/docs/filter-drop-shadow), [grayscale](https://tailwindcss.com/docs/filter-grayscale), [hue-rotate](https://tailwindcss.com/docs/filter-hue-rotate), [invert](https://tailwindcss.com/docs/filter-invert), [saturate](https://tailwindcss.com/docs/filter-saturate), [sepia](https://tailwindcss.com/docs/filter-sepia).

- 필터 제거

`filter-none` 유틸리티를 사용해 요소에 적용된 모든 필터를 제거합니다:

```
    <img class="blur-md brightness-150 invert md:filter-none" src="/img/mountains.jpg" />
```

- 사용자 지정 값 사용

`filter-[<value>]` 구문을 사용해 완전히 사용자 지정한 값으로 필터를 설정합니다:

```
    <img class="filter-[url('filters.svg#filter-id')] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `filter-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <img class="filter-(--my-filter) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `filter-[var(<custom-property>)]`의 단축 표기입니다.

- hover에서 적용

`filter` 유틸리티 앞에 `hover:*` 같은 variant를 붙이면 해당 상태에서만 유틸리티가 적용됩니다:

```
    <img class="blur-sm hover:filter-none ..." src="/img/mountains.jpg" />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.

- 반응형 디자인

`filter` 유틸리티 앞에 `md:` 같은 breakpoint variant를 붙이면 중간 화면 크기 이상에서만 유틸리티가 적용됩니다:

```
    <img class="blur-sm md:filter-none ..." src="/img/mountains.jpg" />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
