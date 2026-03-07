---
title: "mask-type - 효과 - Tailwind CSS"
description: "mask-type-alpha 및 mask-type-luminance 유틸리티를 사용해 SVG 마스크의 유형을 제어합니다:"
---

출처 URL: https://tailwindcss.com/docs/mask-type

# mask-type - 효과 - Tailwind CSS

| 클래스                | 스타일                  |
| --------------------- | ----------------------- |
| `mask-type-alpha`     | `mask-type: alpha;`     |
| `mask-type-luminance` | `mask-type: luminance;` |

## 예제

- 기본 예제

`mask-type-alpha` 및 `mask-type-luminance` 유틸리티를 사용해 SVG 마스크의 유형을 제어합니다:

mask-type-alpha

mask-type-luminance

```
    <svg>  <mask id="blob1" class="mask-type-alpha fill-gray-700/70">    <path d="..."></path>  </mask>  <image href="/img/mountains.jpg" height="100%" width="100%" mask="url(#blob1)" /></svg><svg>  <mask id="blob2" class="mask-type-luminance fill-gray-700/70">    <path d="..."></path>  </mask>  <image href="/img/mountains.jpg" height="100%" width="100%" mask="url(#blob2)" /></svg>
```

`mask-type-luminance`를 사용할 때는 SVG 마스크의 휘도 값이 가시성을 결정하므로, 회색조 색상을 사용하면 가장 예측 가능한 결과를 얻을 수 있습니다. `mask-alpha`에서는 SVG 마스크의 불투명도가 마스킹된 요소의 가시성을 결정합니다.

- 반응형 디자인

`mask-type` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <mask class="mask-type-alpha md:mask-type-luminance ...">  <!-- ... --></mask>
```

variant 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
