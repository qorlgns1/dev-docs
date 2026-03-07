---
title: "line-height - 타이포그래피 - Tailwind CSS"
description: "text-sm/6, text-lg/7 같은 글꼴 크기 유틸리티를 사용하면 요소의 글꼴 크기와 줄 높이를 동시에 설정할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/line-height

# line-height - 타이포그래피 - Tailwind CSS

| 클래스                            | 스타일                                                             |
| --------------------------------- | ------------------------------------------------------------------ |
| `text-<size>/<number>`            | `font-size: <size>; line-height: calc(var(--spacing) * <number>);` |
| `text-<size>/(<custom-property>)` | `font-size: <size>; line-height: var(<custom-property>);`          |
| `text-<size>/[<value>]`           | `font-size: <size>; line-height: <value>;`                         |
| `leading-none`                    | `line-height: 1;`                                                  |
| `leading-<number>`                | `line-height: calc(var(--spacing) * <number>);`                    |
| `leading-(<custom-property>)`     | `line-height: var(<custom-property>);`                             |
| `leading-[<value>]`               | `line-height: <value>;`                                            |

## 예시

- 기본 예시

`text-sm/6`, `text-lg/7` 같은 글꼴 크기 유틸리티를 사용하면 요소의 글꼴 크기와 줄 높이를 동시에 설정할 수 있습니다:

text-sm/6

그래서 나는 물속으로 걸어 들어가기 시작했다. 너희에게 거짓말은 못 하겠다, 얘들아. 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 부서지는 파도를 지나가자 이상할 만큼 평온해졌다. 그게 신의 개입이었는지 모든 생명체 사이의 유대감이었는지는 모르겠지만, 제리, 그 순간 나는 _진짜_ 해양생물학자였다.

text-sm/7

그래서 나는 물속으로 걸어 들어가기 시작했다. 너희에게 거짓말은 못 하겠다, 얘들아. 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 부서지는 파도를 지나가자 이상할 만큼 평온해졌다. 그게 신의 개입이었는지 모든 생명체 사이의 유대감이었는지는 모르겠지만, 제리, 그 순간 나는 _진짜_ 해양생물학자였다.

text-sm/8

그래서 나는 물속으로 걸어 들어가기 시작했다. 너희에게 거짓말은 못 하겠다, 얘들아. 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 부서지는 파도를 지나가자 이상할 만큼 평온해졌다. 그게 신의 개입이었는지 모든 생명체 사이의 유대감이었는지는 모르겠지만, 제리, 그 순간 나는 _진짜_ 해양생물학자였다.

```
    <p class="text-base/6 ...">So I started to walk into the water...</p><p class="text-base/7 ...">So I started to walk into the water...</p><p class="text-base/8 ...">So I started to walk into the water...</p>
```

각 글꼴 크기 유틸리티는 줄 높이를 따로 지정하지 않았을 때 기본 줄 높이도 함께 설정합니다. 이 값들과 사용자 지정 방법은 [font-size 문서](https://tailwindcss.com/docs/font-size)에서 더 자세히 확인할 수 있습니다.

- 독립적으로 설정하기

`leading-6`, `leading-7` 같은 `leading-<number>` 유틸리티를 사용하면 글꼴 크기와 독립적으로 요소의 줄 높이를 설정할 수 있습니다:

leading-6

그래서 나는 물속으로 걸어 들어가기 시작했다. 너희에게 거짓말은 못 하겠다, 얘들아. 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 부서지는 파도를 지나가자 이상할 만큼 평온해졌다. 그게 신의 개입이었는지 모든 생명체 사이의 유대감이었는지는 모르겠지만, 제리, 그 순간 나는 _진짜_ 해양생물학자였다.

leading-7

그래서 나는 물속으로 걸어 들어가기 시작했다. 너희에게 거짓말은 못 하겠다, 얘들아. 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 부서지는 파도를 지나가자 이상할 만큼 평온해졌다. 그게 신의 개입이었는지 모든 생명체 사이의 유대감이었는지는 모르겠지만, 제리, 그 순간 나는 _진짜_ 해양생물학자였다.

leading-8

그래서 나는 물속으로 걸어 들어가기 시작했다. 너희에게 거짓말은 못 하겠다, 얘들아. 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 부서지는 파도를 지나가자 이상할 만큼 평온해졌다. 그게 신의 개입이었는지 모든 생명체 사이의 유대감이었는지는 모르겠지만, 제리, 그 순간 나는 _진짜_ 해양생물학자였다.

```
    <p class="text-sm leading-6">So I started to walk into the water...</p><p class="text-sm leading-7">So I started to walk into the water...</p><p class="text-sm leading-8">So I started to walk into the water...</p>
```

- leading 제거하기

`leading-none` 유틸리티를 사용하면 요소의 줄 높이를 글꼴 크기와 같게 설정할 수 있습니다:

The quick brown fox jumps over the lazy dog.

```
    <p class="text-2xl leading-none ...">The quick brown fox...</p>
```

- 사용자 지정 값 사용하기

`leading-[<value>]` 문법을 사용하면 완전히 사용자 지정한 값을 기준으로 줄 높이를 설정할 수 있습니다:

```
    <p class="leading-[1.5] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `leading-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <p class="leading-(--my-line-height) ...">  Lorem ipsum dolor sit amet...</p>
```

이 문법은 `leading-[var(<custom-property>)]`의 단축형으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`line-height` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <p class="leading-5 md:leading-6 ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 확인할 수 있습니다.

## 테마 사용자 지정

`leading-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 구동되며, 이 변수는 사용자 테마에서 직접 사용자 지정할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 사용자 지정 방법은 [theme variable 문서](https://tailwindcss.com/docs/theme)에서 더 자세히 확인할 수 있습니다.
