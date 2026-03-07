---
title: "text-overflow - 타이포그래피 - Tailwind CSS"
description: "truncate 유틸리티를 사용하면 텍스트 줄바꿈을 방지하고, 필요할 경우 넘치는 텍스트를 말줄임표(…)로 잘라낼 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/text-overflow

# text-overflow - 타이포그래피 - Tailwind CSS

| Class           | Styles                                                            |
| --------------- | ----------------------------------------------------------------- |
| `truncate`      | `overflow: hidden; text-overflow: ellipsis; white-space: nowrap;` |
| `text-ellipsis` | `text-overflow: ellipsis;`                                        |
| `text-clip`     | `text-overflow: clip;`                                            |

## 예제

- 텍스트 자르기

`truncate` 유틸리티를 사용하면 텍스트 줄바꿈을 방지하고, 필요할 경우 넘치는 텍스트를 말줄임표(…)로 잘라낼 수 있습니다:

주요 영어 사전에 등재된 단어 중 가장 긴 단어는 pneumonoultramicroscopicsilicovolcanoconiosis이며, 이는 매우 미세한 실리카 입자(특히 화산에서 발생한 입자)를 흡입해 생기는 폐 질환을 가리키는 단어입니다. 의학적으로는 규폐증(silicosis)과 동일합니다.

```
    <p class="truncate">The longest word in any of the major...</p>
```

- 말줄임표 추가하기

`text-ellipsis` 유틸리티를 사용하면 필요할 경우 넘치는 텍스트를 말줄임표(…)로 잘라낼 수 있습니다:

주요 영어 사전에 등재된 단어 중 가장 긴 단어는 pneumonoultramicroscopicsilicovolcanoconiosis이며, 이는 매우 미세한 실리카 입자(특히 화산에서 발생한 입자)를 흡입해 생기는 폐 질환을 가리키는 단어입니다. 의학적으로는 규폐증(silicosis)과 동일합니다.

```
    <p class="overflow-hidden text-ellipsis">The longest word in any of the major...</p>
```

- 텍스트 클리핑

`text-clip` 유틸리티를 사용하면 콘텐츠 영역의 경계에서 텍스트를 잘라낼 수 있습니다:

주요 영어 사전에 등재된 단어 중 가장 긴 단어는 pneumonoultramicroscopicsilicovolcanoconiosis이며, 이는 매우 미세한 실리카 입자(특히 화산에서 발생한 입자)를 흡입해 생기는 폐 질환을 가리키는 단어입니다. 의학적으로는 규폐증(silicosis)과 동일합니다.

```
    <p class="overflow-hidden text-clip">The longest word in any of the major...</p>
```

이것이 브라우저의 기본 동작입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `text-overflow` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <p class="text-ellipsis md:text-clip ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
