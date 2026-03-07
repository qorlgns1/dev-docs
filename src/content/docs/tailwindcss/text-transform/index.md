---
title: "text-transform - 타이포그래피 - Tailwind CSS"
description: "요소의 텍스트를 대문자로 변환하려면 uppercase 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/text-transform

# text-transform - 타이포그래피 - Tailwind CSS

| 클래스        | 스타일                        |
| ------------- | ----------------------------- |
| `uppercase`   | `text-transform: uppercase;`  |
| `lowercase`   | `text-transform: lowercase;`  |
| `capitalize`  | `text-transform: capitalize;` |
| `normal-case` | `text-transform: none;`       |

## 예제

- 텍스트를 대문자로 변환하기

요소의 텍스트를 대문자로 변환하려면 `uppercase` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <p class="uppercase">The quick brown fox ...</p>
```

- 텍스트를 소문자로 변환하기

요소의 텍스트를 소문자로 변환하려면 `lowercase` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <p class="lowercase">The quick brown fox ...</p>
```

- 텍스트 첫 글자 대문자화하기

요소 텍스트의 각 단어 첫 글자를 대문자로 만들려면 `capitalize` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <p class="capitalize">The quick brown fox ...</p>
```

- 텍스트 대소문자 설정 초기화하기

요소의 원래 텍스트 대소문자를 유지하려면 `normal-case` 유틸리티를 사용하세요. 일반적으로 서로 다른 브레이크포인트에서 대문자화를 재설정할 때 사용합니다:

The quick brown fox jumps over the lazy dog.

```
    <p class="normal-case">The quick brown fox ...</p>
```

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `text-transform` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <p class="capitalize md:uppercase ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 확인하세요.
