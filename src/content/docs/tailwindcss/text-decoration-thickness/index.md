---
title: "text-decoration-thickness - 타이포그래피 - Tailwind CSS"
description: "decoration-2, decoration-4 같은 decoration-<number> 유틸리티를 사용해 요소의 텍스트 장식 두께를 변경할 수 있습니다:"
---

# text-decoration-thickness - 타이포그래피 - Tailwind CSS

| 클래스                                  | 스타일                                               |
| --------------------------------------- | ---------------------------------------------------- |
| `decoration-<number>`                   | `text-decoration-thickness: <number>px;`             |
| `decoration-from-font`                  | `text-decoration-thickness: from-font;`              |
| `decoration-auto`                       | `text-decoration-thickness: auto;`                   |
| `decoration-(length:<custom-property>)` | `text-decoration-thickness: var(<custom-property>);` |
| `decoration-[<value>]`                  | `text-decoration-thickness: <value>;`                |

## 예시

- 기본 예시

`decoration-2`, `decoration-4` 같은 `decoration-<number>` 유틸리티를 사용해 요소의 [텍스트 장식](https://tailwindcss.com/docs/text-decoration-line) 두께를 변경할 수 있습니다:

decoration-1

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

decoration-2

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

decoration-4

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="underline decoration-1">The quick brown fox...</p><p class="underline decoration-2">The quick brown fox...</p><p class="underline decoration-4">The quick brown fox...</p>
```

- 사용자 지정 값 사용하기

완전히 사용자 지정한 값을 기준으로 텍스트 장식 두께를 설정하려면 `decoration-[<value>]` 문법을 사용하세요:

```
    <p class="decoration-[0.25rem] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `decoration-(length:<custom-property>)` 문법도 사용할 수 있습니다:

```
    <p class="decoration-(length:--my-decoration-thickness) ...">  Lorem ipsum dolor sit amet...</p>
```

이는 `var()` 함수를 자동으로 추가해 주는 `decoration-[length:var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `text-decoration-thickness` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <p class="underline md:decoration-4 ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용법은 [variant 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 알아보세요.
