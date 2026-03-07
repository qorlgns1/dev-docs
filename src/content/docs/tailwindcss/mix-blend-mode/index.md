---
title: "mix-blend-mode - 효과 - Tailwind CSS"
description: "mix-blend-overlay 및 mix-blend-soft-light 같은 유틸리티를 사용해 같은 스태킹 컨텍스트에서 요소의 콘텐츠와 배경이 다른 콘텐츠와 혼합되는 방식을 제어하세요:"
---

소스 URL: https://tailwindcss.com/docs/mix-blend-mode

# mix-blend-mode - 효과 - Tailwind CSS

| 클래스                   | 스타일                          |
| ------------------------ | ------------------------------- |
| `mix-blend-normal`       | `mix-blend-mode: normal;`       |
| `mix-blend-multiply`     | `mix-blend-mode: multiply;`     |
| `mix-blend-screen`       | `mix-blend-mode: screen;`       |
| `mix-blend-overlay`      | `mix-blend-mode: overlay;`      |
| `mix-blend-darken`       | `mix-blend-mode: darken;`       |
| `mix-blend-lighten`      | `mix-blend-mode: lighten;`      |
| `mix-blend-color-dodge`  | `mix-blend-mode: color-dodge;`  |
| `mix-blend-color-burn`   | `mix-blend-mode: color-burn;`   |
| `mix-blend-hard-light`   | `mix-blend-mode: hard-light;`   |
| `mix-blend-soft-light`   | `mix-blend-mode: soft-light;`   |
| `mix-blend-difference`   | `mix-blend-mode: difference;`   |
| `mix-blend-exclusion`    | `mix-blend-mode: exclusion;`    |
| `mix-blend-hue`          | `mix-blend-mode: hue;`          |
| `mix-blend-saturation`   | `mix-blend-mode: saturation;`   |
| `mix-blend-color`        | `mix-blend-mode: color;`        |
| `mix-blend-luminosity`   | `mix-blend-mode: luminosity;`   |
| `mix-blend-plus-darker`  | `mix-blend-mode: plus-darker;`  |
| `mix-blend-plus-lighter` | `mix-blend-mode: plus-lighter;` |

더 보기

## 예제

- 기본 예제

`mix-blend-overlay` 및 `mix-blend-soft-light` 같은 유틸리티를 사용해 같은 스태킹 컨텍스트에서 요소의 콘텐츠와 배경이 다른 콘텐츠와 혼합되는 방식을 제어하세요:

```
    <div class="flex justify-center -space-x-14">  <div class="bg-blue-500 mix-blend-multiply ..."></div>  <div class="bg-pink-500 mix-blend-multiply ..."></div></div>
```

- 블렌딩 격리

부모 요소에 `isolate` 유틸리티를 사용해 새 스태킹 컨텍스트를 만들고, 뒤에 있는 콘텐츠와의 블렌딩을 방지하세요:

```
    <div class="isolate flex justify-center -space-x-14">  <div class="bg-yellow-500 mix-blend-multiply ..."></div>  <div class="bg-green-500 mix-blend-multiply ..."></div></div><div class="flex justify-center -space-x-14">  <div class="bg-yellow-500 mix-blend-multiply ..."></div>  <div class="bg-green-500 mix-blend-multiply ..."></div></div>
```

- 반응형 디자인

`mix-blend-mode` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙여, 중간 화면 크기 이상에서만 유틸리티가 적용되도록 하세요:

```
    <div class="mix-blend-multiply md:mix-blend-overlay ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
