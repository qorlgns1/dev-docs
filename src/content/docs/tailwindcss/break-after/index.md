---
title: "break-after - 레이아웃 - Tailwind CSS"
description: "요소 뒤에서 열 또는 페이지 나누기가 어떻게 동작할지 제어하려면 break-after-column 및 break-after-page 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/break-after

# break-after - 레이아웃 - Tailwind CSS

| 클래스                   | 스타일                     |
| ------------------------ | -------------------------- |
| `break-after-auto`       | `break-after: auto;`       |
| `break-after-avoid`      | `break-after: avoid;`      |
| `break-after-all`        | `break-after: all;`        |
| `break-after-avoid-page` | `break-after: avoid-page;` |
| `break-after-page`       | `break-after: page;`       |
| `break-after-left`       | `break-after: left;`       |
| `break-after-right`      | `break-after: right;`      |
| `break-after-column`     | `break-after: column;`     |

## 예제

- 기본 예제

요소 뒤에서 열 또는 페이지 나누기가 어떻게 동작할지 제어하려면 `break-after-column` 및 `break-after-page` 같은 유틸리티를 사용하세요:

```
    <div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-after-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `break-after` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="break-after-column md:break-after-auto ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
