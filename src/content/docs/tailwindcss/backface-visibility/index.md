---
title: "backface-visibility - 변환(Transforms) - Tailwind CSS"
description: "회전되어 시야에서 멀어진 경우에도 큐브 같은 요소의 뒷면을 표시하려면 backface-visible 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/backface-visibility

# backface-visibility - 변환(Transforms) - Tailwind CSS

| Class              | Styles                          |
| ------------------ | ------------------------------- |
| `backface-hidden`  | `backface-visibility: hidden;`  |
| `backface-visible` | `backface-visibility: visible;` |

## 예제

- 기본 예제

회전되어 시야에서 멀어진 경우에도 큐브 같은 요소의 뒷면을 표시하려면 `backface-visible` 유틸리티를 사용하세요:

backface-hidden

1

2

3

4

5

6

backface-visible

1

2

3

4

5

6

```
    <div class="size-20 ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 backface-hidden ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 backface-hidden ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 backface-hidden ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 backface-hidden ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 backface-hidden ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 backface-hidden ...">6</div></div><div class="size-20 ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 backface-visible ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 backface-visible ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 backface-visible ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 backface-visible ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 backface-visible ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 backface-visible ...">6</div></div>
```

- 반응형 디자인

`backface-visibility` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 크기 화면 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="backface-visible md:backface-hidden ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 알아보세요.
