---
title: "font-smoothing - 타이포그래피 - Tailwind CSS"
description: "텍스트를 그레이스케일 안티앨리어싱으로 렌더링하려면 antialiased 유틸리티를 사용하세요:"
---

# font-smoothing - 타이포그래피 - Tailwind CSS

| 클래스                 | 스타일                                                                     |
| ---------------------- | -------------------------------------------------------------------------- |
| `antialiased`          | `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;` |
| `subpixel-antialiased` | `-webkit-font-smoothing: auto; -moz-osx-font-smoothing: auto;`             |

## 예제

- 그레이스케일 안티앨리어싱

텍스트를 그레이스케일 안티앨리어싱으로 렌더링하려면 `antialiased` 유틸리티를 사용하세요:

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="antialiased ...">The quick brown fox ...</p>
```

- 서브픽셀 안티앨리어싱

텍스트를 서브픽셀 안티앨리어싱으로 렌더링하려면 `subpixel-antialiased` 유틸리티를 사용하세요:

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="subpixel-antialiased ...">The quick brown fox ...</p>
```

- 반응형 디자인

`-webkit-font-smoothing` 및 `-moz-osx-font-smoothing` 유틸리티에 `md:` 같은 브레이크포인트 변형을 접두사로 붙이면, 중간 크기 화면 이상에서만 유틸리티가 적용됩니다:

```
    <p class="antialiased md:subpixel-antialiased ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
