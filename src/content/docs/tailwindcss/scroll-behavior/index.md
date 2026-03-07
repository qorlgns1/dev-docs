---
title: "scroll-behavior - 인터랙티비티 - Tailwind CSS"
description: "요소 내에서 부드러운 스크롤을 활성화하려면 `scroll-smooth` 유틸리티를 사용하세요:"
---

원문 URL: https://tailwindcss.com/docs/scroll-behavior

# scroll-behavior - 인터랙티비티 - Tailwind CSS

| 클래스          | 스타일                     |
| --------------- | -------------------------- |
| `scroll-auto`   | `scroll-behavior: auto;`   |
| `scroll-smooth` | `scroll-behavior: smooth;` |

## 예제

- 부드러운 스크롤 사용하기

요소 내에서 부드러운 스크롤을 활성화하려면 `scroll-smooth` 유틸리티를 사용하세요:

```
    <html class="scroll-smooth">  <!-- ... --></html>
```

`scroll-behavior` 설정은 브라우저에 의해 트리거되는 스크롤 이벤트에만 영향을 줍니다.

- 일반 스크롤 사용하기

스크롤의 기본 브라우저 동작으로 되돌리려면 `scroll-auto` 유틸리티를 사용하세요:

```
    <html class="scroll-smooth md:scroll-auto">  <!-- ... --></html>
```
