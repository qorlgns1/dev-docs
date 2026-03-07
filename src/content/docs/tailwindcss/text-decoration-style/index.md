---
title: "text-decoration-style - 타이포그래피 - Tailwind CSS"
description: "decoration-dotted 및 decoration-dashed 같은 유틸리티를 사용해 요소의 text decoration 스타일을 변경하세요:"
---

# text-decoration-style - 타이포그래피 - Tailwind CSS

| 클래스              | 스타일                           |
| ------------------- | -------------------------------- |
| `decoration-solid`  | `text-decoration-style: solid;`  |
| `decoration-double` | `text-decoration-style: double;` |
| `decoration-dotted` | `text-decoration-style: dotted;` |
| `decoration-dashed` | `text-decoration-style: dashed;` |
| `decoration-wavy`   | `text-decoration-style: wavy;`   |

## 예제

- 기본 예제

`decoration-dotted` 및 `decoration-dashed` 같은 유틸리티를 사용해 요소의 [text decoration](https://tailwindcss.com/docs/text-decoration-line) 스타일을 변경하세요:

decoration-solid

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

decoration-double

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

decoration-dotted

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

decoration-dashed

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

decoration-wavy

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="underline decoration-solid">The quick brown fox...</p><p class="underline decoration-double">The quick brown fox...</p><p class="underline decoration-dotted">The quick brown fox...</p><p class="underline decoration-dashed">The quick brown fox...</p><p class="underline decoration-wavy">The quick brown fox...</p>
```

- 반응형 디자인

`text-decoration-style` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙여, 중간 화면 크기 이상에서만 해당 유틸리티가 적용되도록 하세요:

```
    <p class="underline md:decoration-dashed ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
