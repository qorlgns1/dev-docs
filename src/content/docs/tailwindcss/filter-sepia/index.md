---
title: "filter: sepia() - 필터 - Tailwind CSS"
description: "sepia 및 sepia-50 같은 유틸리티를 사용해 요소에 적용되는 세피아 효과를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/filter-sepia

# filter: sepia() - 필터 - Tailwind CSS

| 클래스                      | 스타일                                   |
| --------------------------- | ---------------------------------------- |
| `sepia`                     | `filter: sepia(100%);`                   |
| `sepia-<number>`            | `filter: sepia(<number>%);`              |
| `sepia-(<custom-property>)` | `filter: sepia(var(<custom-property>));` |
| `sepia-[<value>]`           | `filter: sepia(<value>);`                |

## 예제

- 기본 예제

`sepia` 및 `sepia-50` 같은 유틸리티를 사용해 요소에 적용되는 세피아 효과를 제어하세요:

sepia-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

sepia-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

sepia

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="sepia-0" src="/img/mountains.jpg" /><img class="sepia-50" src="/img/mountains.jpg" /><img class="sepia" src="/img/mountains.jpg" />
```

- 사용자 지정 값 사용하기

완전히 사용자 지정한 값을 기준으로 세피아 양을 설정하려면 `sepia-[<value>]` 구문을 사용하세요:

```
    <img class="sepia-[.25] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `sepia-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <img class="sepia-(--my-sepia) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `sepia-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `filter: sepia()` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <img class="sepia md:sepia-0 ..." src="/img/mountains.jpg" />
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
