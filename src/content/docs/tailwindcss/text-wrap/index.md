---
title: "text-wrap - 타이포그래피 - Tailwind CSS"
description: "text-wrap 유틸리티를 사용해 넘치는 텍스트를 문맥상 자연스러운 지점에서 여러 줄로 줄바꿈하세요:"
---

출처 URL: https://tailwindcss.com/docs/text-wrap

# text-wrap - 타이포그래피 - Tailwind CSS

| 클래스         | 스타일                |
| -------------- | --------------------- |
| `text-wrap`    | `text-wrap: wrap;`    |
| `text-nowrap`  | `text-wrap: nowrap;`  |
| `text-balance` | `text-wrap: balance;` |
| `text-pretty`  | `text-wrap: pretty;`  |

## 예제

- 텍스트 줄바꿈 허용

`text-wrap` 유틸리티를 사용해 넘치는 텍스트를 문맥상 자연스러운 지점에서 여러 줄로 줄바꿈하세요:

사랑받던 맨해튼 수프 가판대 문 닫아

뉴요커들은 올해 도시에서 가장 존경받던 수프 가판대가 갑작스럽게 문을 닫으면서, 공동체를 혼란에 빠뜨린 일련의 사건 이후 겨울 추위를 예년보다 덜 따뜻하게 맞이하고 있습니다.

```
    <article class="text-wrap">  <h3>Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

- 텍스트 줄바꿈 방지

`text-nowrap` 유틸리티를 사용해 텍스트가 줄바꿈되지 않도록 하고, 필요하면 넘치도록 두세요:

사랑받던 맨해튼 수프 가판대 문 닫아

뉴요커들은 올해 도시에서 가장 존경받던 수프 가판대가 갑작스럽게 문을 닫으면서, 공동체를 혼란에 빠뜨린 일련의 사건 이후 겨울 추위를 예년보다 덜 따뜻하게 맞이하고 있습니다.

```
    <article class="text-nowrap">  <h3>Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

- 균형 잡힌 텍스트 줄바꿈

`text-balance` 유틸리티를 사용해 텍스트가 각 줄에 고르게 분배되도록 하세요:

사랑받던 맨해튼 수프 가판대 문 닫아

뉴요커들은 올해 도시에서 가장 존경받던 수프 가판대가 갑작스럽게 문을 닫으면서, 공동체를 혼란에 빠뜨린 일련의 사건 이후 겨울 추위를 예년보다 덜 따뜻하게 맞이하고 있습니다.

```
    <article>  <h3 class="text-balance">Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

성능상의 이유로 브라우저는 텍스트 균형 맞춤을 약 6줄 이하 블록으로 제한하므로, 이 기능은 제목에 가장 적합합니다.

- 보기 좋은 텍스트 줄바꿈

`text-pretty` 유틸리티를 사용하면 속도를 일부 희생하는 대신 더 나은 텍스트 줄바꿈과 레이아웃을 우선할 수 있습니다. 동작은 브라우저마다 다르지만, 텍스트 블록 끝에 고립어(한 줄에 단어 하나만 남는 경우)가 생기지 않게 하는 방식이 자주 포함됩니다:

사랑받던 맨해튼 수프 가판대 문 닫아

뉴요커들은 올해 도시에서 가장 존경받던 수프 가판대가 갑작스럽게 문을 닫으면서, 공동체를 혼란에 빠뜨린 일련의 사건 이후 겨울 추위를 예년보다 덜 따뜻하게 맞이하고 있습니다.

```
    <article>  <h3 class="text-pretty">Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

- 반응형 디자인

`text-wrap` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙여, 중간 크기 화면 이상에서만 유틸리티가 적용되도록 하세요:

```
    <h1 class="text-pretty md:text-balance ...">  <!-- ... --></h1>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
