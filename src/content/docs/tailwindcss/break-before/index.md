---
title: "break-before - 레이아웃 - Tailwind CSS"
description: "요소 앞에서 열 또는 페이지 나누기가 어떻게 동작할지 제어하려면 break-before-column, break-before-page 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/break-before

# break-before - 레이아웃 - Tailwind CSS

| 클래스                    | 스타일                      |
| ------------------------- | --------------------------- |
| `break-before-auto`       | `break-before: auto;`       |
| `break-before-avoid`      | `break-before: avoid;`      |
| `break-before-all`        | `break-before: all;`        |
| `break-before-avoid-page` | `break-before: avoid-page;` |
| `break-before-page`       | `break-before: page;`       |
| `break-before-left`       | `break-before: left;`       |
| `break-before-right`      | `break-before: right;`      |
| `break-before-column`     | `break-before: column;`     |

## 예제

- 기본 예제

요소 앞에서 열 또는 페이지 나누기가 어떻게 동작할지 제어하려면 `break-before-column`, `break-before-page` 같은 유틸리티를 사용하세요:

```
    <div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-before-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>
```

- 반응형 디자인

`md:` 같은 브레이크포인트 variant 접두사를 `break-before` 유틸리티에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="break-before-column md:break-before-auto ...">  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
