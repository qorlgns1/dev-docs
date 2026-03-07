---
title: "text-indent - 타이포그래피 - Tailwind CSS"
description: "indent-2, indent-8 같은 indent-<number> 유틸리티를 사용해 블록 내 텍스트 앞에 표시되는 빈 공간(들여쓰기) 크기를 설정하세요:"
---

출처 URL: https://tailwindcss.com/docs/text-indent

# text-indent - 타이포그래피 - Tailwind CSS

| Class                        | Styles                                           |
| ---------------------------- | ------------------------------------------------ |
| `indent-<number>`            | `text-indent: calc(var(--spacing) * <number>);`  |
| `-indent-<number>`           | `text-indent: calc(var(--spacing) * -<number>);` |
| `indent-px`                  | `text-indent: 1px;`                              |
| `-indent-px`                 | `text-indent: -1px;`                             |
| `indent-(<custom-property>)` | `text-indent: var(<custom-property>);`           |
| `indent-[<value>]`           | `text-indent: <value>;`                          |

## 예제

- 기본 예제

`indent-2`, `indent-8` 같은 `indent-<number>` 유틸리티를 사용해 블록 내 텍스트 앞에 표시되는 빈 공간(들여쓰기) 크기를 설정하세요:

그래서 나는 물속으로 걸어 들어가기 시작했다. 솔직히 말해서 얘들아, 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 부서지는 파도를 지나가자 이상할 만큼 차분해졌다. 그게 신의 개입이었는지, 모든 생명체 사이의 유대감이었는지는 모르겠지만, 제리, 그 순간만큼은 내가 _정말로_ 해양생물학자였다고 말할 수 있다.

```
    <p class="indent-8">So I started to walk into the water...</p>
```

- 음수 값 사용하기

음수 `text-indent` 값을 사용하려면 클래스 이름 앞에 대시를 붙여 음수 값으로 변환하세요:

그래서 나는 물속으로 걸어 들어가기 시작했다. 솔직히 말해서 얘들아, 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 부서지는 파도를 지나가자 이상할 만큼 차분해졌다. 그게 신의 개입이었는지, 모든 생명체 사이의 유대감이었는지는 모르겠지만, 제리, 그 순간만큼은 내가 _정말로_ 해양생물학자였다고 말할 수 있다.

```
    <p class="-indent-8">So I started to walk into the water...</p>
```

- 사용자 지정 값 사용하기

완전히 사용자 지정한 값을 기준으로 텍스트 들여쓰기를 설정하려면 `indent-[<value>]` 문법을 사용하세요:

```
    <p class="indent-[50%] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `indent-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <p class="indent-(--my-indentation) ...">  Lorem ipsum dolor sit amet...</p>
```

이 방식은 `var()` 함수를 자동으로 추가해 주는 `indent-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `text-indent` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <p class="indent-4 md:indent-8 ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
