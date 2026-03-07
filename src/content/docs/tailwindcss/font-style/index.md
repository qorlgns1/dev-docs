---
title: "font-style - 타이포그래피 - Tailwind CSS"
description: "italic 유틸리티를 사용해 텍스트를 기울임꼴로 만드세요:"
---

출처 URL: https://tailwindcss.com/docs/font-style

# font-style - 타이포그래피 - Tailwind CSS

| 클래스       | 스타일                |
| ------------ | --------------------- |
| `italic`     | `font-style: italic;` |
| `not-italic` | `font-style: normal;` |

## 예제

- 텍스트를 기울임꼴로 표시하기

`italic` 유틸리티를 사용해 텍스트를 기울임꼴로 만드세요:

The quick brown fox jumps over the lazy dog.

```
    <p class="italic ...">The quick brown fox ...</p>
```

- 텍스트를 일반 스타일로 표시하기

`not-italic` 유틸리티를 사용해 텍스트를 일반 스타일로 표시하세요:

The quick brown fox jumps over the lazy dog.

```
    <p class="not-italic ...">The quick brown fox ...</p>
```

- 반응형 디자인

`font-style` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 유틸리티가 적용됩니다:

```
    <p class="italic md:not-italic ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
