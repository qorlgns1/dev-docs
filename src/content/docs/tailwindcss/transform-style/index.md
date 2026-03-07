---
title: "transform-style - Transforms - Tailwind CSS"
description: "transform-3d를 사용해 자식 요소를 3D 공간에 배치합니다:"
---

출처 URL: https://tailwindcss.com/docs/transform-style

# transform-style - Transforms - Tailwind CSS

| 클래스           | 스타일                          |
| ---------------- | ------------------------------- |
| `transform-3d`   | `transform-style: preserve-3d;` |
| `transform-flat` | `transform-style: flat;`        |

## 예제

- 기본 예제

`transform-3d`를 사용해 자식 요소를 3D 공간에 배치합니다:

transform-flat

1

2

3

4

5

6

transform-3d

1

2

3

4

5

6

```
    <div class="size-20 transform-flat ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div><div class="size-20 transform-3d ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div>
```

이 설정이 없으면 모든 자식 요소는 3D가 아닌 2D 공간에서만 변형됩니다.

- 반응형 디자인

`transform-style` 유틸리티에 `md:` 같은 브레이크포인트 변형을 접두사로 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="transform-3d md:transform-flat ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 확인하세요.
