---
title: "box-decoration-break - 레이아웃 - Tailwind CSS"
description: "box-decoration-slice 및 box-decoration-clone 유틸리티를 사용해 background, border, border-image, box-shadow, clip-path, margin, padding 같은 속성을 요소가 하나의 연속된 조각인 ..."
---

출처 URL: https://tailwindcss.com/docs/box-decoration-break

# box-decoration-break - 레이아웃 - Tailwind CSS

| 클래스                 | 스타일                         |
| ---------------------- | ------------------------------ |
| `box-decoration-clone` | `box-decoration-break: clone;` |
| `box-decoration-slice` | `box-decoration-break: slice;` |

## 예제

- 기본 예제

`box-decoration-slice` 및 `box-decoration-clone` 유틸리티를 사용해 background, border, border-image, box-shadow, clip-path, margin, padding 같은 속성을 요소가 하나의 연속된 조각인 것처럼 렌더링할지, 아니면 분리된 블록으로 렌더링할지 제어할 수 있습니다:

box-decoration-slice

안녕하세요
세계

box-decoration-clone

안녕하세요
세계

```
    <span class="box-decoration-slice bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">  Hello<br />World</span><span class="box-decoration-clone bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">  Hello<br />World</span>
```

- 반응형 디자인

`box-decoration-break` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="box-decoration-clone md:box-decoration-slice ...">  <!-- ... --></div>
```

variant 사용법은 [variant 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
