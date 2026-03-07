---
title: "background-blend-mode - 효과 - Tailwind CSS"
description: "bg-blend-difference, bg-blend-saturation 같은 유틸리티를 사용해 요소의 배경 이미지와 색상이 혼합되는 방식을 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/background-blend-mode

# background-blend-mode - 효과 - Tailwind CSS

| 클래스                 | 스타일                                |
| ---------------------- | ------------------------------------- |
| `bg-blend-normal`      | `background-blend-mode: normal;`      |
| `bg-blend-multiply`    | `background-blend-mode: multiply;`    |
| `bg-blend-screen`      | `background-blend-mode: screen;`      |
| `bg-blend-overlay`     | `background-blend-mode: overlay;`     |
| `bg-blend-darken`      | `background-blend-mode: darken;`      |
| `bg-blend-lighten`     | `background-blend-mode: lighten;`     |
| `bg-blend-color-dodge` | `background-blend-mode: color-dodge;` |
| `bg-blend-color-burn`  | `background-blend-mode: color-burn;`  |
| `bg-blend-hard-light`  | `background-blend-mode: hard-light;`  |
| `bg-blend-soft-light`  | `background-blend-mode: soft-light;`  |
| `bg-blend-difference`  | `background-blend-mode: difference;`  |
| `bg-blend-exclusion`   | `background-blend-mode: exclusion;`   |
| `bg-blend-hue`         | `background-blend-mode: hue;`         |
| `bg-blend-saturation`  | `background-blend-mode: saturation;`  |
| `bg-blend-color`       | `background-blend-mode: color;`       |
| `bg-blend-luminosity`  | `background-blend-mode: luminosity;`  |

더 보기

## 예제

- 기본 예제

`bg-blend-difference`, `bg-blend-saturation` 같은 유틸리티를 사용해 요소의 배경 이미지와 색상이 혼합되는 방식을 제어하세요:

bg-blend-multiply

bg-blend-soft-light

bg-blend-overlay

```
    <div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-multiply ..."></div><div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-soft-light ..."></div><div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-overlay ..."></div>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `background-blend-mode` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-lighten md:bg-blend-darken ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
