---
title: "break-inside - 레이아웃 - Tailwind CSS"
description: "break-inside-column 및 break-inside-avoid-page 같은 유틸리티를 사용해 요소 내부에서 열 또는 페이지 나누기가 동작하는 방식을 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/break-inside

# break-inside - 레이아웃 - Tailwind CSS

| 클래스                      | 스타일                        |
| --------------------------- | ----------------------------- |
| `break-inside-auto`         | `break-inside: auto;`         |
| `break-inside-avoid`        | `break-inside: avoid;`        |
| `break-inside-avoid-page`   | `break-inside: avoid-page;`   |
| `break-inside-avoid-column` | `break-inside: avoid-column;` |

## 예시

- 기본 예시

`break-inside-column` 및 `break-inside-avoid-page` 같은 유틸리티를 사용해 요소 내부에서 열 또는 페이지 나누기가 동작하는 방식을 제어하세요:

```
    <div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-inside-avoid-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>
```

- 반응형 디자인

`break-inside` 유틸리티에 `md:` 같은 브레이크포인트 variant를 접두사로 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="break-inside-avoid-column md:break-inside-auto ...">  <!-- ... --></div>
```

variant 사용 방법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
