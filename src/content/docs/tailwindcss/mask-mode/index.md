---
title: "mask-mode - 효과 - Tailwind CSS"
description: "요소의 마스크 모드를 제어하려면 mask-alpha, mask-luminance, mask-match 유틸리티를 사용하세요:"
---

# mask-mode - 효과 - Tailwind CSS

| 클래스           | 스타일                     |
| ---------------- | -------------------------- |
| `mask-alpha`     | `mask-mode: alpha;`        |
| `mask-luminance` | `mask-mode: luminance;`    |
| `mask-match`     | `mask-mode: match-source;` |

## 예제

- 기본 예제

요소의 마스크 모드를 제어하려면 `mask-alpha`, `mask-luminance`, `mask-match` 유틸리티를 사용하세요:

mask-alpha

mask-luminance

```
    <div class="mask-alpha mask-r-from-black mask-r-from-50% mask-r-to-transparent bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-luminance mask-r-from-white mask-r-from-50% mask-r-to-black bg-[url(/img/mountains.jpg)] ..."></div>
```

`mask-luminance`를 사용할 때는 마스크의 휘도 값이 가시성을 결정하므로, 회색조 색상을 사용하는 것이 가장 예측 가능한 결과를 제공합니다. `mask-alpha`에서는 마스크의 불투명도가 마스킹된 요소의 가시성을 결정합니다.

- 반응형 디자인

`mask-mode` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="mask-alpha md:mask-luminance ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
