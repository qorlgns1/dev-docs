---
title: "backdrop-filter: brightness() - 필터 - Tailwind CSS"
description: "backdrop-brightness-50, backdrop-brightness-100 같은 유틸리티를 사용해 요소의 배경 밝기를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/backdrop-filter-brightness

# backdrop-filter: brightness() - 필터 - Tailwind CSS

| 클래스                                    | 스타일                                                 |
| ----------------------------------------- | ------------------------------------------------------ |
| `backdrop-brightness-<number>`            | `backdrop-filter: brightness(<number>%);`              |
| `backdrop-brightness-(<custom-property>)` | `backdrop-filter: brightness(var(<custom-property>));` |
| `backdrop-brightness-[<value>]`           | `backdrop-filter: brightness(<value>);`                |

## 예제

- 기본 예제

`backdrop-brightness-50`, `backdrop-brightness-100` 같은 유틸리티를 사용해 요소의 배경 밝기를 제어하세요:

backdrop-brightness-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-brightness-150

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-brightness-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-brightness-150 ..."></div></div>
```

- 커스텀 값 사용하기

`backdrop-brightness-[<value>]` 구문을 사용해 완전히 사용자 정의한 값으로 배경 밝기를 설정할 수 있습니다:

```
    <div class="backdrop-brightness-[1.75] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-brightness-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="backdrop-brightness-(--my-backdrop-brightness) ...">  <!-- ... --></div>
```

이는 `backdrop-brightness-[var(<custom-property>)]`의 단축 표기이며, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`backdrop-filter: brightness()` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="backdrop-brightness-110 md:backdrop-brightness-150 ...">  <!-- ... --></div>
```

변형 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 알아보세요.
