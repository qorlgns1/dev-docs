---
title: "background-clip - 배경 - Tailwind CSS"
description: "요소 배경의 경계 박스를 제어하려면 bg-clip-border, bg-clip-padding, bg-clip-content 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/background-clip

# background-clip - 배경 - Tailwind CSS

| 클래스            | 스타일                          |
| ----------------- | ------------------------------- |
| `bg-clip-border`  | `background-clip: border-box;`  |
| `bg-clip-padding` | `background-clip: padding-box;` |
| `bg-clip-content` | `background-clip: content-box;` |
| `bg-clip-text`    | `background-clip: text;`        |

## 예제

- 기본 예제

요소 배경의 경계 박스를 제어하려면 `bg-clip-border`, `bg-clip-padding`, `bg-clip-content` 유틸리티를 사용하세요:

bg-clip-border

bg-clip-padding

bg-clip-content

```
    <div class="border-4 bg-indigo-500 bg-clip-border p-3"></div><div class="border-4 bg-indigo-500 bg-clip-padding p-3"></div><div class="border-4 bg-indigo-500 bg-clip-content p-3"></div>
```

- 텍스트에 맞게 자르기

요소의 배경을 텍스트 모양에 맞춰 자르려면 `bg-clip-text` 유틸리티를 사용하세요:

안녕하세요 세계

```
    <p class="bg-linear-to-r from-pink-500 to-violet-500 bg-clip-text text-5xl font-extrabold text-transparent ...">  Hello world</p>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `background-clip` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="bg-clip-border md:bg-clip-padding ...">  <!-- ... --></div>
```

variant 사용법은 [variant 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
