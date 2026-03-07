---
title: "white-space - 타이포그래피 - Tailwind CSS"
description: "요소 안에서 텍스트가 일반적으로 줄바꿈되도록 하려면 whitespace-normal 유틸리티를 사용하세요. 줄바꿈과 공백은 축약됩니다:"
---

출처 URL: https://tailwindcss.com/docs/white-space

# white-space - 타이포그래피 - Tailwind CSS

| Class                     | Styles                       |
| ------------------------- | ---------------------------- |
| `whitespace-normal`       | `white-space: normal;`       |
| `whitespace-nowrap`       | `white-space: nowrap;`       |
| `whitespace-pre`          | `white-space: pre;`          |
| `whitespace-pre-line`     | `white-space: pre-line;`     |
| `whitespace-pre-wrap`     | `white-space: pre-wrap;`     |
| `whitespace-break-spaces` | `white-space: break-spaces;` |

## 예제

- 기본

요소 안에서 텍스트가 일반적으로 줄바꿈되도록 하려면 `whitespace-normal` 유틸리티를 사용하세요. 줄바꿈과 공백은 축약됩니다:

안녕하세요 여러분! 이제 거의 2022년인데도 우리 사이에 외계인이 살고 있는지 아직 모르고 있죠, 아니면 알고 있을까요? 어쩌면 이 글을 쓰고 있는 사람이 외계인일지도 모릅니다. 절대 알 수 없을 거예요.

```
    <p class="whitespace-normal">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

- 줄바꿈 없음

요소 안에서 텍스트 줄바꿈을 막으려면 `whitespace-nowrap` 유틸리티를 사용하세요. 줄바꿈과 공백은 축약됩니다:

안녕하세요 여러분! 이제 거의 2022년인데도 우리 사이에 외계인이 살고 있는지 아직 모르고 있죠, 아니면 알고 있을까요? 어쩌면 이 글을 쓰고 있는 사람이 외계인일지도 모릅니다. 절대 알 수 없을 거예요.

```
    <p class="overflow-auto whitespace-nowrap">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

- Pre

요소 안에서 줄바꿈과 공백을 유지하려면 `whitespace-pre` 유틸리티를 사용하세요. 텍스트는 줄바꿈되지 않습니다:

안녕하세요 여러분! 이제 거의 2022년인데도 우리 사이에 외계인이 살고 있는지 아직 모르고 있죠, 아니면 알고 있을까요? 어쩌면 이 글을 쓰고 있는 사람이 외계인일지도 모릅니다. 절대 알 수 없을 거예요.

```
    <p class="overflow-auto whitespace-pre">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

- Pre Line

요소 안에서 공백은 유지하지 않고 줄바꿈만 유지하려면 `whitespace-pre-line` 유틸리티를 사용하세요. 텍스트는 일반적으로 줄바꿈됩니다:

안녕하세요 여러분! 이제 거의 2022년인데도 우리 사이에 외계인이 살고 있는지 아직 모르고 있죠, 아니면 알고 있을까요? 어쩌면 이 글을 쓰고 있는 사람이 외계인일지도 모릅니다. 절대 알 수 없을 거예요.

```
    <p class="whitespace-pre-line">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

- Pre Wrap

요소 안에서 줄바꿈과 공백을 유지하려면 `whitespace-pre-wrap` 유틸리티를 사용하세요. 텍스트는 일반적으로 줄바꿈됩니다:

안녕하세요 여러분! 이제 거의 2022년인데도 우리 사이에 외계인이 살고 있는지 아직 모르고 있죠, 아니면 알고 있을까요? 어쩌면 이 글을 쓰고 있는 사람이 외계인일지도 모릅니다. 절대 알 수 없을 거예요.

```
    <p class="whitespace-pre-wrap">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

- Break Spaces

요소 안에서 줄바꿈과 공백을 유지하려면 `whitespace-break-spaces` 유틸리티를 사용하세요. 줄 끝의 공백이 걸쳐 매달리지 않고 다음 줄로 줄바꿈됩니다:

안녕하세요 여러분! 이제 거의 2022년인데도 우리 사이에 외계인이 살고 있는지 아직 모르고 있죠, 아니면 알고 있을까요? 어쩌면 이 글을 쓰고 있는 사람이 외계인일지도 모릅니다. 절대 알 수 없을 거예요.

```
    <p class="whitespace-break-spaces">Hey everyone!It's almost 2022       and we still don't know if there             are aliens living among us, or do we? Maybe the person writing this is an alien.You will never know.</p>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `white-space` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <p class="whitespace-pre md:whitespace-normal ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
