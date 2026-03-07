---
title: "mask-origin - 효과 - Tailwind CSS"
description: "요소의 마스크가 렌더링되는 위치를 제어하려면 mask-origin-border, mask-origin-padding, mask-origin-content 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/mask-origin

# mask-origin - 효과 - Tailwind CSS

| 클래스                | 스타일                      |
| --------------------- | --------------------------- |
| `mask-origin-border`  | `mask-origin: border-box;`  |
| `mask-origin-padding` | `mask-origin: padding-box;` |
| `mask-origin-content` | `mask-origin: content-box;` |
| `mask-origin-fill`    | `mask-origin: fill-box;`    |
| `mask-origin-stroke`  | `mask-origin: stroke-box;`  |
| `mask-origin-view`    | `mask-origin: view-box;`    |

## 예제

- 기본 예제

요소의 마스크가 렌더링되는 위치를 제어하려면 `mask-origin-border`, `mask-origin-padding`, `mask-origin-content` 같은 유틸리티를 사용하세요:

mask-origin-border

mask-origin-padding

mask-origin-content

```
    <div class="mask-origin-border border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-origin-padding border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-origin-content border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `mask-origin` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="mask-origin-border md:mask-origin-padding ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
