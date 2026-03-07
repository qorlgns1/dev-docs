---
title: "touch-action - 상호작용 - Tailwind CSS"
description: "touch-pan-y, touch-pinch-zoom 같은 유틸리티를 사용해 터치스크린에서 요소를 스크롤(패닝)하고 확대/축소(핀치)하는 방식을 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/touch-action

# touch-action - 상호작용 - Tailwind CSS

| 클래스               | 스타일                        |
| -------------------- | ----------------------------- |
| `touch-auto`         | `touch-action: auto;`         |
| `touch-none`         | `touch-action: none;`         |
| `touch-pan-x`        | `touch-action: pan-x;`        |
| `touch-pan-left`     | `touch-action: pan-left;`     |
| `touch-pan-right`    | `touch-action: pan-right;`    |
| `touch-pan-y`        | `touch-action: pan-y;`        |
| `touch-pan-up`       | `touch-action: pan-up;`       |
| `touch-pan-down`     | `touch-action: pan-down;`     |
| `touch-pinch-zoom`   | `touch-action: pinch-zoom;`   |
| `touch-manipulation` | `touch-action: manipulation;` |

## 예제

- 기본 예제

`touch-pan-y`, `touch-pinch-zoom` 같은 유틸리티를 사용해 터치스크린에서 요소를 스크롤(패닝)하고 확대/축소(핀치)하는 방식을 제어하세요:

터치스크린에서 이 이미지들을 패닝해 보세요

touch-auto

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80)

touch-none

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80)

touch-pan-x

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80)

touch-pan-y

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80)

```
    <div class="h-48 w-full touch-auto overflow-auto ...">  <img class="h-auto w-[150%] max-w-none" src="..." /></div><div class="h-48 w-full touch-none overflow-auto ...">  <img class="h-auto w-[150%] max-w-none" src="..." /></div><div class="h-48 w-full touch-pan-x overflow-auto ...">  <img class="h-auto w-[150%] max-w-none" src="..." /></div><div class="h-48 w-full touch-pan-y overflow-auto ...">  <img class="h-auto w-[150%] max-w-none" src="..." /></div>
```

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `touch-action` 유틸리티 앞에 붙여, 중간 크기 이상의 화면에서만 유틸리티가 적용되도록 하세요:

```
    <div class="touch-pan-x md:touch-auto ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
