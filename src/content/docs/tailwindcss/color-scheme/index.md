---
title: "color-scheme - 인터랙티비티 - Tailwind CSS"
description: "요소가 렌더링되는 방식을 제어하려면 scheme-light, scheme-light-dark 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/color-scheme

# color-scheme - 인터랙티비티 - Tailwind CSS

| 클래스              | 스타일                      |
| ------------------- | --------------------------- |
| `scheme-normal`     | `color-scheme: normal;`     |
| `scheme-dark`       | `color-scheme: dark;`       |
| `scheme-light`      | `color-scheme: light;`      |
| `scheme-light-dark` | `color-scheme: light dark;` |
| `scheme-only-dark`  | `color-scheme: only dark;`  |
| `scheme-only-light` | `color-scheme: only light;` |

## 예시

- 기본 예시

요소가 렌더링되는 방식을 제어하려면 `scheme-light`, `scheme-light-dark` 같은 유틸리티를 사용하세요:

차이를 확인하려면 시스템 색상 스킴을 전환해 보세요

scheme-light

scheme-dark

scheme-light-dark

```
    <div class="scheme-light ...">  <input type="date" /></div><div class="scheme-dark ...">  <input type="date" /></div><div class="scheme-light-dark ...">  <input type="date" /></div>
```

- 다크 모드에서 적용하기

특정 상태에서만 유틸리티를 적용하려면 `color-scheme` 유틸리티 앞에 `dark:*` 같은 variant를 붙이세요:

```
    <html class="scheme-light dark:scheme-dark ...">  <!-- ... --></html>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
