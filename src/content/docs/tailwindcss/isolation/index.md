---
title: "isolation - 레이아웃 - Tailwind CSS"
description: "요소가 명시적으로 새로운 스태킹 컨텍스트를 생성할지 제어하려면 isolate 및 isolation-auto 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/isolation

# isolation - 레이아웃 - Tailwind CSS

| 클래스           | 스타일                |
| ---------------- | --------------------- |
| `isolate`        | `isolation: isolate;` |
| `isolation-auto` | `isolation: auto;`    |

## 예제

- 기본 예제

요소가 명시적으로 새로운 스태킹 컨텍스트를 생성할지 제어하려면 `isolate` 및 `isolation-auto` 유틸리티를 사용하세요:

```
    <div class="isolate ...">  <!-- ... --></div>
```

- 반응형 디자인

`isolation` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 크기 이상의 화면에서만 유틸리티가 적용됩니다:

```
    <div class="isolate md:isolation-auto ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
