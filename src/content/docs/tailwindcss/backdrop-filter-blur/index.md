---
title: "backdrop-filter: blur() - 필터 - Tailwind CSS"
description: "backdrop-blur-sm, backdrop-blur-lg 같은 유틸리티를 사용해 요소의 배경 블러를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/backdrop-filter-blur

# backdrop-filter: blur() - 필터 - Tailwind CSS

| 클래스                              | 스타일                                               |
| ----------------------------------- | ---------------------------------------------------- |
| `backdrop-blur-xs`                  | `backdrop-filter: blur(var(--blur-xs)); /* 4px */`   |
| `backdrop-blur-sm`                  | `backdrop-filter: blur(var(--blur-sm)); /* 8px */`   |
| `backdrop-blur-md`                  | `backdrop-filter: blur(var(--blur-md)); /* 12px */`  |
| `backdrop-blur-lg`                  | `backdrop-filter: blur(var(--blur-lg)); /* 16px */`  |
| `backdrop-blur-xl`                  | `backdrop-filter: blur(var(--blur-xl)); /* 24px */`  |
| `backdrop-blur-2xl`                 | `backdrop-filter: blur(var(--blur-2xl)); /* 40px */` |
| `backdrop-blur-3xl`                 | `backdrop-filter: blur(var(--blur-3xl)); /* 64px */` |
| `backdrop-blur-none`                | `backdrop-filter: ;`                                 |
| `backdrop-blur-(<custom-property>)` | `backdrop-filter: blur(var(<custom-property>));`     |
| `backdrop-blur-[<value>]`           | `backdrop-filter: blur(<value>);`                    |

## 예제

- 기본 예제

`backdrop-blur-sm`, `backdrop-blur-lg` 같은 유틸리티를 사용해 요소의 배경 블러를 제어하세요:

backdrop-blur-none

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-blur-sm

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-blur-md

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-blur-none ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-blur-sm ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-blur-md ..."></div></div>
```

- 사용자 지정 값 사용

`backdrop-blur-[<value>]` 문법을 사용해 완전히 사용자 지정한 값으로 배경 블러를 설정하세요:

```
    <div class="backdrop-blur-[2px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `backdrop-blur-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="backdrop-blur-(--my-backdrop-blur) ...">  <!-- ... --></div>
```

이 문법은 `var()` 함수를 자동으로 추가해 주는 `backdrop-blur-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `backdrop-filter: blur()` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="backdrop-blur-none md:backdrop-blur-lg ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.

## 테마 커스터마이징

`--blur-*` 테마 변수를 사용해 프로젝트의 배경 블러 유틸리티를 커스터마이징하세요:

```
    @theme {  --blur-2xs: 2px; }
```

이제 마크업에서 `backdrop-blur-2xs` 유틸리티를 사용할 수 있습니다:

```
    <div class="backdrop-blur-2xs">  <!-- ... --></div>
```

테마 커스터마이징에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
