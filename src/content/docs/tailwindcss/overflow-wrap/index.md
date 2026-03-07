---
title: "overflow-wrap - 타이포그래피 - Tailwind CSS"
description: "필요한 경우 단어의 글자 사이에서 줄바꿈을 허용하려면 wrap-break-word 유틸리티를 사용하세요:"
---

소스 URL: https://tailwindcss.com/docs/overflow-wrap

# overflow-wrap - 타이포그래피 - Tailwind CSS

| 클래스            | 스타일                       |
| ----------------- | ---------------------------- |
| `wrap-break-word` | `overflow-wrap: break-word;` |
| `wrap-anywhere`   | `overflow-wrap: anywhere;`   |
| `wrap-normal`     | `overflow-wrap: normal;`     |

## 예제

- 단어 중간 줄바꿈

필요한 경우 단어의 글자 사이에서 줄바꿈을 허용하려면 `wrap-break-word` 유틸리티를 사용하세요:

주요 영어 사전에 수록된 가장 긴 단어는 pneumonoultramicroscopicsilicovolcanoconiosis로, 매우 미세한 실리카 입자를 흡입해 발생하는 폐 질환을 뜻하며, 특히 화산에서 비롯된 경우를 가리킵니다. 의학적으로는 규폐증(silicosis)과 동일합니다.

```
    <p class="wrap-break-word">The longest word in any of the major...</p>
```

- 어디서나 줄바꿈

`wrap-anywhere` 유틸리티는 `wrap-break-word`와 비슷하게 동작하지만, 브라우저가 요소의 고유 크기를 계산할 때 단어 중간 줄바꿈도 함께 고려한다는 점이 다릅니다:

wrap-break-word

![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Jay Riemenschneider

jason.riemenschneider@vandelayindustries.com

wrap-anywhere

![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Jay Riemenschneider

jason.riemenschneider@vandelayindustries.com

```
    <div class="flex max-w-sm">  <img class="size-16 rounded-full" src="/img/profile.jpg" />  <div class="wrap-break-word">    <p class="font-medium">Jay Riemenschneider</p>    <p>jason.riemenschneider@vandelayindustries.com</p>  </div></div><div class="flex max-w-sm">  <img class="size-16 rounded-full" src="/img/profile.jpg" />  <div class="wrap-anywhere">    <p class="font-medium">Jay Riemenschneider</p>    <p>jason.riemenschneider@vandelayindustries.com</p>  </div></div>
```

이 방식은 `flex` 컨테이너 내부에서 텍스트를 줄바꿈할 때 유용합니다. 보통은 자식 요소가 콘텐츠 크기보다 더 작게 줄어들 수 있도록 `min-width: 0`을 설정해야 합니다.

- 일반 줄바꿈

공백, 하이픈, 구두점 같은 자연스러운 줄바꿈 지점에서만 줄바꿈을 허용하려면 `wrap-normal` 유틸리티를 사용하세요:

주요 영어 사전에 수록된 가장 긴 단어는 pneumonoultramicroscopicsilicovolcanoconiosis로, 매우 미세한 실리카 입자를 흡입해 발생하는 폐 질환을 뜻하며, 특히 화산에서 비롯된 경우를 가리킵니다. 의학적으로는 규폐증(silicosis)과 동일합니다.

```
    <p class="wrap-normal">The longest word in any of the major...</p>
```

- 반응형 디자인

`overflow-wrap` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <p class="wrap-normal md:wrap-break-word ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
