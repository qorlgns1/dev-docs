---
title: "filter: grayscale() - 필터 - Tailwind CSS"
description: "요소에 적용되는 그레이스케일 효과의 양을 제어하려면 grayscale 및 grayscale-75 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/filter-grayscale

# filter: grayscale() - 필터 - Tailwind CSS

| 클래스                          | 스타일                                       |
| ------------------------------- | -------------------------------------------- |
| `grayscale`                     | `filter: grayscale(100%);`                   |
| `grayscale-<number>`            | `filter: grayscale(<number>%);`              |
| `grayscale-(<custom-property>)` | `filter: grayscale(var(<custom-property>));` |
| `grayscale-[<value>]`           | `filter: grayscale(<value>);`                |

## 예제

- 기본 예제

요소에 적용되는 그레이스케일 효과의 양을 제어하려면 `grayscale` 및 `grayscale-75` 같은 유틸리티를 사용하세요:

grayscale-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

grayscale-25

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

grayscale-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

grayscale

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="grayscale-0 ..." src="/img/mountains.jpg" /><img class="grayscale-25 ..." src="/img/mountains.jpg" /><img class="grayscale-50 ..." src="/img/mountains.jpg" /><img class="grayscale ..." src="/img/mountains.jpg" />
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값을 기준으로 그레이스케일을 설정하려면 `grayscale-[<value>]` 구문을 사용하세요:

```
    <img class="grayscale-[0.5] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `grayscale-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <img class="grayscale-(--my-grayscale) ..." src="/img/mountains.jpg" />
```

이것은 `grayscale-[var(<custom-property>)]`의 단축 표기이며, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `filter: grayscale()` 유틸리티 앞에 붙이면 중간 크기 이상의 화면에서만 유틸리티가 적용됩니다:

```
    <img class="grayscale md:grayscale-0 ..." src="/img/mountains.jpg" />
```

variant 사용에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
