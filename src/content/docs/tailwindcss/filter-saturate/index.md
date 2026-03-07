---
title: "filter: saturate() - 필터 - Tailwind CSS"
description: "saturate-50, saturate-100 같은 유틸리티를 사용해 요소의 채도를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/filter-saturate

# filter: saturate() - 필터 - Tailwind CSS

| Class                          | Styles                                      |
| ------------------------------ | ------------------------------------------- |
| `saturate-<number>`            | `filter: saturate(<number>%);`              |
| `saturate-(<custom-property>)` | `filter: saturate(var(<custom-property>));` |
| `saturate-[<value>]`           | `filter: saturate(<value>);`                |

## 예제

- 기본 예제

`saturate-50`, `saturate-100` 같은 유틸리티를 사용해 요소의 채도를 제어하세요:

saturate-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

saturate-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

saturate-150

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

saturate-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="saturate-50 ..." src="/img/mountains.jpg" /><img class="saturate-100 ..." src="/img/mountains.jpg" /><img class="saturate-150 ..." src="/img/mountains.jpg" /><img class="saturate-200 ..." src="/img/mountains.jpg" />
```

- 커스텀 값 사용하기

`saturate-[<value>]` 문법을 사용해 완전히 사용자 정의한 값으로 채도를 설정하세요:

```
    <img class="saturate-[.25] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `saturate-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="saturate-(--my-saturation) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `saturate-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `filter: saturate()` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <img class="saturate-50 md:saturate-150 ..." src="/img/mountains.jpg" />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
