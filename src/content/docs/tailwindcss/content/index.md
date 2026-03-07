---
title: "content - 타이포그래피 - Tailwind CSS"
description: "content-[<value>] 문법을 before 및 after 변형과 함께 사용해 ::before 및 ::after 가상 요소의 내용을 설정하세요:"
---

출처 URL: https://tailwindcss.com/docs/content

# content - 타이포그래피 - Tailwind CSS

| 클래스                        | 스타일                             |
| ----------------------------- | ---------------------------------- |
| `content-[<value>]`           | `content: <value>;`                |
| `content-(<custom-property>)` | `content: var(<custom-property>);` |
| `content-none`                | `content: none;`                   |

## 예제

- 기본 예제

`content-[<value>]` 문법을 `before` 및 `after` 변형과 함께 사용해 `::before` 및 `::after` 가상 요소의 내용을 설정하세요:

해상도가 더 높다는 것은 단순히 더 좋은 품질의 이미지를 의미하는 것만은 아닙니다. Retina 6K 디스플레이를 탑재한 [Pro Display XDR](https://www.apple.com/pro-display-xdr/)은 5K 디스플레이보다 화면 작업 공간을 거의 40% 더 제공합니다.

```
    <p>Higher resolution means more than just a better-quality image. With aRetina 6K display, <a class="text-blue-600 after:content-['_↗']" href="...">Pro Display XDR</a> gives you nearly 40 percent more screen real estate thana 5K display.</p>
```

- 속성 값 참조

`content-[attr(<name>)]` 문법을 사용하면 `attr()` CSS 함수를 통해 속성에 저장된 값을 참조할 수 있습니다:

```
    <p before="Hello World" class="before:content-[attr(before)] ...">  <!-- ... --></p>
```

- 공백과 밑줄 사용

HTML에서는 공백이 클래스의 끝을 나타내므로, 임의 값의 공백은 밑줄로 바꿔야 합니다:

```
    <p class="before:content-['Hello_World'] ..."></p>
```

실제 밑줄을 포함해야 한다면, 백슬래시로 이스케이프하여 사용할 수 있습니다:

```
    <p class="before:content-['Hello\_World']"></p>
```

- CSS 변수 사용

`content-(<custom-property>)` 문법을 사용하면 CSS 변수를 통해 `::before` 및 `::after` 가상 요소의 내용을 제어할 수 있습니다:

```
    <p class="content-(--my-content)"></p>
```

이는 `var()` 함수를 자동으로 추가해 주는 `content-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`content` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <p class="before:content-['Mobile'] md:before:content-['Desktop'] ..."></p>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 알아보세요.
