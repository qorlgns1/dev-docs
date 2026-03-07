---
title: "filter: contrast() - 필터 - Tailwind CSS"
description: "contrast-50, contrast-100 같은 유틸리티를 사용해 요소의 대비를 제어할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/filter-contrast

# filter: contrast() - 필터 - Tailwind CSS

| 클래스                         | 스타일                                      |
| ------------------------------ | ------------------------------------------- |
| `contrast-<number>`            | `filter: contrast(<number>%);`              |
| `contrast-(<custom-property>)` | `filter: contrast(var(<custom-property>));` |
| `contrast-[<value>]`           | `filter: contrast(<value>);`                |

## 예제

- 기본 예제

`contrast-50`, `contrast-100` 같은 유틸리티를 사용해 요소의 대비를 제어할 수 있습니다:

contrast-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

contrast-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

contrast-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

contrast-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="contrast-50 ..." src="/img/mountains.jpg" /><img class="contrast-100 ..." src="/img/mountains.jpg" /><img class="contrast-125 ..." src="/img/mountains.jpg" /><img class="contrast-200 ..." src="/img/mountains.jpg" />
```

- 사용자 지정 값 사용하기

`contrast-[<value>]` 문법을 사용하면 완전히 사용자 지정한 값으로 대비를 설정할 수 있습니다:

```
    <img class="contrast-[.25] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `contrast-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="contrast-(--my-contrast) ..." src="/img/mountains.jpg" />
```

이 문법은 `var()` 함수를 자동으로 추가해 주는 `contrast-[var(<custom-property>)]`의 단축 표현입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `filter: contrast()` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <img class="contrast-125 md:contrast-150 ..." src="/img/mountains.jpg" />
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
