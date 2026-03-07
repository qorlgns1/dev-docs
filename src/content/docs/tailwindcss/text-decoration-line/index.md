---
title: "text-decoration-line - 타이포그래피 - Tailwind CSS"
description: "요소의 텍스트에 밑줄을 추가하려면 underline 유틸리티를 사용하세요:"
---

# text-decoration-line - 타이포그래피 - Tailwind CSS

| Class          | 스타일                                |
| -------------- | ------------------------------------- |
| `underline`    | `text-decoration-line: underline;`    |
| `overline`     | `text-decoration-line: overline;`     |
| `line-through` | `text-decoration-line: line-through;` |
| `no-underline` | `text-decoration-line: none;`         |

## 예제

- 텍스트에 밑줄 추가

요소의 텍스트에 밑줄을 추가하려면 `underline` 유틸리티를 사용하세요:

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="underline">The quick brown fox...</p>
```

- 텍스트에 윗줄 추가

요소의 텍스트에 윗줄을 추가하려면 `overline` 유틸리티를 사용하세요:

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="overline">The quick brown fox...</p>
```

- 텍스트에 취소선 추가

요소의 텍스트에 취소선을 추가하려면 `line-through` 유틸리티를 사용하세요:

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="line-through">The quick brown fox...</p>
```

- 텍스트에서 줄 제거

요소의 텍스트에서 줄을 제거하려면 `no-underline` 유틸리티를 사용하세요:

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="no-underline">The quick brown fox...</p>
```

- hover에서 적용

`text-decoration-line` 유틸리티 앞에 `hover:*` 같은 variant를 붙이면 해당 상태에서만 유틸리티가 적용됩니다:

예상된 동작을 보려면 텍스트 위에 마우스를 올려보세요

[빠른 갈색 여우](https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog)가 게으른 개를 뛰어넘습니다.

```
    <p>The <a href="..." class="no-underline hover:underline ...">quick brown fox</a> jumps over the lazy dog.</p>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

- 반응형 디자인

`text-decoration-line` 유틸리티 앞에 `md:` 같은 breakpoint variant를 붙이면 중간 크기 이상의 화면에서만 유틸리티가 적용됩니다:

```
    <a class="no-underline md:underline ..." href="...">  <!-- ... --></a>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
