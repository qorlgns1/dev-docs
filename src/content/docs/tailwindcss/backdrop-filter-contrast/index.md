---
title: "backdrop-filter: contrast() - 필터 - Tailwind CSS"
description: "backdrop-contrast-50, backdrop-contrast-100 같은 유틸리티를 사용해 요소의 배경 대비를 제어할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/backdrop-filter-contrast

# backdrop-filter: contrast() - 필터 - Tailwind CSS

| 클래스                                  | 스타일                                               |
| --------------------------------------- | ---------------------------------------------------- |
| `backdrop-contrast-<number>`            | `backdrop-filter: contrast(<number>%);`              |
| `backdrop-contrast-(<custom-property>)` | `backdrop-filter: contrast(var(<custom-property>));` |
| `backdrop-contrast-[<value>]`           | `backdrop-filter: contrast(<value>);`                |

## 예제

- 기본 예제

`backdrop-contrast-50`, `backdrop-contrast-100` 같은 유틸리티를 사용해 요소의 배경 대비를 제어할 수 있습니다:

backdrop-contrast-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-contrast-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-contrast-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-contrast-200 ..."></div></div>
```

- 사용자 정의 값 사용하기

완전히 사용자 정의한 값을 기준으로 배경 대비를 설정하려면 `backdrop-contrast-[<value>]` 문법을 사용하세요:

```
    <div class="backdrop-contrast-[.25] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-contrast-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="backdrop-contrast-(--my-backdrop-contrast) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `backdrop-contrast-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `backdrop-filter: contrast()` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="backdrop-contrast-125 md:backdrop-contrast-150 ...">  <!-- ... --></div>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 확인할 수 있습니다.
