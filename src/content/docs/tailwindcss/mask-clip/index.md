---
title: "mask-clip - 효과 - Tailwind CSS"
description: "mask-clip-border, mask-clip-padding, mask-clip-content 같은 유틸리티를 사용해 요소 마스크의 경계 상자를 제어합니다:"
---

출처 URL: https://tailwindcss.com/docs/mask-clip

# mask-clip - 효과 - Tailwind CSS

| 클래스              | 스타일                    |
| ------------------- | ------------------------- |
| `mask-clip-border`  | `mask-clip: border-box;`  |
| `mask-clip-padding` | `mask-clip: padding-box;` |
| `mask-clip-content` | `mask-clip: content-box;` |
| `mask-clip-fill`    | `mask-clip: fill-box;`    |
| `mask-clip-stroke`  | `mask-clip: stroke-box;`  |
| `mask-clip-view`    | `mask-clip: view-box;`    |
| `mask-no-clip`      | `mask-clip: no-clip;`     |

## 예제

- 기본 예제

`mask-clip-border`, `mask-clip-padding`, `mask-clip-content` 같은 유틸리티를 사용해 요소 마스크의 경계 상자를 제어합니다:

mask-clip-border

mask-clip-padding

mask-clip-content

```
    <div class="mask-clip-border border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-clip-padding border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-clip-content border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 반응형 디자인

`mask-clip` 유틸리티에 `md:` 같은 브레이크포인트 variant 접두사를 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="mask-clip-border md:mask-clip-padding ...">  <!-- ... --></div>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
