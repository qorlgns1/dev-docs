---
title: "background-origin - 배경 - Tailwind CSS"
description: "bg-origin-border, bg-origin-padding, bg-origin-content 유틸리티를 사용해 요소의 배경이 렌더링되는 위치를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/background-origin

# background-origin - 배경 - Tailwind CSS

| 클래스              | 스타일                            |
| ------------------- | --------------------------------- |
| `bg-origin-border`  | `background-origin: border-box;`  |
| `bg-origin-padding` | `background-origin: padding-box;` |
| `bg-origin-content` | `background-origin: content-box;` |

## 예제

- 기본 예제

`bg-origin-border`, `bg-origin-padding`, `bg-origin-content` 유틸리티를 사용해 요소의 배경이 렌더링되는 위치를 제어하세요:

bg-origin-border

bg-origin-padding

bg-origin-content

```
    <div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-border p-3 ..."></div><div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-padding p-3 ..."></div><div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-content p-3 ..."></div>
```

- 반응형 디자인

`background-origin` 유틸리티에 `md:` 같은 브레이크포인트 variant를 접두어로 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="bg-origin-border md:bg-origin-padding ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
