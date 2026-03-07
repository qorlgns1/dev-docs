---
title: "box-sizing - 레이아웃 - Tailwind CSS"
description: "box-border 유틸리티를 사용해 요소의 box-sizing을 border-box로 설정하면, 요소에 높이나 너비를 지정했을 때 브라우저가 요소의 테두리와 패딩을 포함해서 계산합니다."
---

출처 URL: https://tailwindcss.com/docs/box-sizing

# box-sizing - 레이아웃 - Tailwind CSS

| 클래스        | 스타일                     |
| ------------- | -------------------------- |
| `box-border`  | `box-sizing: border-box;`  |
| `box-content` | `box-sizing: content-box;` |

## 예제

- 테두리와 패딩 포함

`box-border` 유틸리티를 사용해 요소의 `box-sizing`을 `border-box`로 설정하면, 요소에 높이나 너비를 지정했을 때 브라우저가 요소의 테두리와 패딩을 포함해서 계산합니다.

즉, 모든 면에 2px 테두리와 4px 패딩이 있는 100px × 100px 요소는 내부 콘텐츠 영역이 88px × 88px이면서, 최종적으로 100px × 100px로 렌더링됩니다:

128px

128px

```
    <div class="box-border size-32 border-4 p-4 ...">  <!-- ... --></div>
```

Tailwind는 [preflight base styles](https://tailwindcss.com/docs/preflight)에서 모든 요소에 대해 이것을 기본값으로 사용합니다.

- 테두리와 패딩 제외

`box-content` 유틸리티를 사용해 요소의 `box-sizing`을 `content-box`로 설정하면, 브라우저가 요소에 지정된 너비나 높이에 테두리와 패딩을 추가로 더해 계산합니다.

즉, 모든 면에 2px 테두리와 4px 패딩이 있는 100px × 100px 요소는 실제로 112px × 112px로 렌더링되며, 내부 콘텐츠 영역은 100px × 100px가 됩니다:

128px

128px

```
    <div class="box-content size-32 border-4 p-4 ...">  <!-- ... --></div>
```

- 반응형 디자인

`box-sizing` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="box-content md:box-border ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
