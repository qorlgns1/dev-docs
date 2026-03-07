---
title: "word-break - 타이포그래피 - Tailwind CSS"
description: "break-normal 유틸리티를 사용하면 일반적인 단어 분리 지점에서만 줄바꿈을 추가할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/word-break

# word-break - 타이포그래피 - Tailwind CSS

| 클래스         | 스타일                   |
| -------------- | ------------------------ |
| `break-normal` | `word-break: normal;`    |
| `break-all`    | `word-break: break-all;` |
| `break-keep`   | `word-break: keep-all;`  |

## 예제

- 일반

`break-normal` 유틸리티를 사용하면 일반적인 단어 분리 지점에서만 줄바꿈을 추가할 수 있습니다:

주요 영어 사전에 등재된 단어 중 가장 긴 단어는 pneumonoultramicroscopicsilicovolcanoconiosis이며, 이 단어는 매우 미세한 실리카 입자, 특히 화산에서 발생한 입자를 흡입해 걸리는 폐 질환을 의미합니다. 의학적으로는 규폐증(silicosis)과 동일합니다.

```
    <p class="break-normal">The longest word in any of the major...</p>
```

- 모두 분할

`break-all` 유틸리티를 사용하면 전체 단어를 보존하려고 하지 않고, 필요할 때마다 줄바꿈을 추가합니다:

주요 영어 사전에 등재된 단어 중 가장 긴 단어는 pneumonoultramicroscopicsilicovolcanoconiosis이며, 이 단어는 매우 미세한 실리카 입자, 특히 화산에서 발생한 입자를 흡입해 걸리는 폐 질환을 의미합니다. 의학적으로는 규폐증(silicosis)과 동일합니다.

```
    <p class="break-all">The longest word in any of the major...</p>
```

- 분할 유지

`break-keep` 유틸리티를 사용하면 중국어/일본어/한국어(CJK) 텍스트에 줄바꿈이 적용되지 않도록 할 수 있습니다:

抗衡不屈不挠 (kànghéng bùqū bùnáo) 这是一个长词，意思是不畏强暴，奋勇抗争，坚定不移，永不放弃。这个词通常用来描述那些在面对困难和挑战时坚持自己信念的人， 他们克服一切困难，不屈不挠地追求自己的目标。无论遇到多大的挑战，他们都能够坚持到底，不放弃，最终获得胜利。

```
    <p class="break-keep">抗衡不屈不挠...</p>
```

CJK가 아닌 텍스트에서는 `break-keep` 유틸리티가 `break-normal` 유틸리티와 동일하게 동작합니다.

- 반응형 디자인

`word-break` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <p class="break-normal md:break-all ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
