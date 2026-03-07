---
title: "text-underline-offset - 타이포그래피 - Tailwind CSS"
description: "underline-offset-2, underline-offset-4 같은 underline-offset-<number> 유틸리티를 사용해 텍스트 밑줄의 오프셋을 변경할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/text-underline-offset

# text-underline-offset - 타이포그래피 - Tailwind CSS

| 클래스                                 | 스타일                                           |
| -------------------------------------- | ------------------------------------------------ |
| `underline-offset-<number>`            | `text-underline-offset: <number>px;`             |
| `-underline-offset-<number>`           | `text-underline-offset: calc(<number>px * -1);`  |
| `underline-offset-auto`                | `text-underline-offset: auto;`                   |
| `underline-offset-(<custom-property>)` | `text-underline-offset: var(<custom-property>);` |
| `underline-offset-[<value>]`           | `text-underline-offset: <value>;`                |

## 예제

- 기본 예제

`underline-offset-2`, `underline-offset-4` 같은 `underline-offset-<number>` 유틸리티를 사용해 텍스트 밑줄의 오프셋을 변경할 수 있습니다:

underline-offset-1

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

underline-offset-2

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

underline-offset-4

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

underline-offset-8

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="underline underline-offset-1">The quick brown fox...</p><p class="underline underline-offset-2">The quick brown fox...</p><p class="underline underline-offset-4">The quick brown fox...</p><p class="underline underline-offset-8">The quick brown fox...</p>
```

- 커스텀 값 사용하기

완전히 사용자 지정한 값으로 텍스트 밑줄 오프셋을 설정하려면 `underline-offset-[<value>]` 구문을 사용하세요:

```
    <p class="underline-offset-[3px] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `underline-offset-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <p class="underline-offset-(--my-underline-offset) ...">  Lorem ipsum dolor sit amet...</p>
```

이 구문은 `var()` 함수를 자동으로 추가해 주는 `underline-offset-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`text-underline-offset` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <p class="underline md:underline-offset-4 ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
