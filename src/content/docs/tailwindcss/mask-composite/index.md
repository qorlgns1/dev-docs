---
title: "mask-composite - 효과 - Tailwind CSS"
description: "mask-add, mask-intersect 같은 유틸리티를 사용해 요소의 마스크가 서로 결합되는 방식을 제어합니다:"
---

출처 URL: https://tailwindcss.com/docs/mask-composite

# mask-composite - 효과 - Tailwind CSS

| 클래스           | 스타일                       |
| ---------------- | ---------------------------- |
| `mask-add`       | `mask-composite: add;`       |
| `mask-subtract`  | `mask-composite: subtract;`  |
| `mask-intersect` | `mask-composite: intersect;` |
| `mask-exclude`   | `mask-composite: exclude;`   |

## 예시

- 기본 예시

`mask-add`, `mask-intersect` 같은 유틸리티를 사용해 요소의 마스크가 서로 결합되는 방식을 제어합니다:

mask-add

mask-subtract

mask-intersect

mask-exclude

```
    <div class="mask-add mask-[url(/img/circle.png),url(/img/circle.png)] mask-[position:30%_50%,70%_50%] bg-[url(/img/mountains.jpg)]"></div><div class="mask-subtract mask-[url(/img/circle.png),url(/img/circle.png)] mask-[position:30%_50%,70%_50%] bg-[url(/img/mountains.jpg)]"></div><div class="mask-intersect mask-[url(/img/circle.png),url(/img/circle.png)] mask-[position:30%_50%,70%_50%] bg-[url(/img/mountains.jpg)]"></div><div class="mask-exclude mask-[url(/img/circle.png),url(/img/circle.png)] mask-[position:30%_50%,70%_50%] bg-[url(/img/mountains.jpg)]"></div>
```

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `mask-composite` 유틸리티 앞에 붙여, 중간 크기 이상의 화면에서만 유틸리티가 적용되도록 할 수 있습니다:

```
    <div class="mask-add md:mask-subtract ...">  <!-- ... --></div>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
