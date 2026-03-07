---
title: "backdrop-filter: grayscale() - 필터 - Tailwind CSS"
description: "backdrop-grayscale-50 및 backdrop-grayscale 같은 유틸리티를 사용해 요소 배경에 적용되는 그레이스케일 효과를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/backdrop-filter-grayscale

# backdrop-filter: grayscale() - 필터 - Tailwind CSS

| 클래스                                   | 스타일                                                |
| ---------------------------------------- | ----------------------------------------------------- |
| `backdrop-grayscale`                     | `backdrop-filter: grayscale(100%);`                   |
| `backdrop-grayscale-<number>`            | `backdrop-filter: grayscale(<number>%);`              |
| `backdrop-grayscale-(<custom-property>)` | `backdrop-filter: grayscale(var(<custom-property>));` |
| `backdrop-grayscale-[<value>]`           | `backdrop-filter: grayscale(<value>);`                |

## 예제

- 기본 예제

`backdrop-grayscale-50` 및 `backdrop-grayscale` 같은 유틸리티를 사용해 요소 배경에 적용되는 그레이스케일 효과를 제어하세요:

backdrop-grayscale-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-grayscale-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-grayscale

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-grayscale-0 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-grayscale-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-grayscale-200 ..."></div></div>
```

- 사용자 정의 값 사용하기

`backdrop-grayscale-[<value>]` 구문을 사용해 완전히 사용자 정의된 값으로 배경 그레이스케일을 설정할 수 있습니다:

```
    <div class="backdrop-grayscale-[0.5] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-grayscale-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="backdrop-grayscale-(--my-backdrop-grayscale) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `backdrop-grayscale-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `backdrop-filter: grayscale()` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="backdrop-grayscale md:backdrop-grayscale-0 ...">  <!-- ... --></div>
```

[variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 variants 사용법을 더 알아보세요.
