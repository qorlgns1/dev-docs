---
title: "background-size - 배경 - Tailwind CSS"
description: "bg-cover 유틸리티를 사용해 배경 이미지가 배경 레이어를 가득 채울 때까지 크기를 조정하며, 필요하면 이미지를 잘라냅니다:"
---

출처 URL: https://tailwindcss.com/docs/background-size

# background-size - 배경 - Tailwind CSS

| 클래스                        | 스타일                                     |
| ----------------------------- | ------------------------------------------ |
| `bg-auto`                     | `background-size: auto;`                   |
| `bg-cover`                    | `background-size: cover;`                  |
| `bg-contain`                  | `background-size: contain;`                |
| `bg-size-(<custom-property>)` | `background-size: var(<custom-property>);` |
| `bg-size-[<value>]`           | `background-size: <value>;`                |

## 예제

- 컨테이너를 채우기

`bg-cover` 유틸리티를 사용해 배경 이미지가 배경 레이어를 가득 채울 때까지 크기를 조정하며, 필요하면 이미지를 잘라냅니다:

```
    <div class="bg-[url(/img/mountains.jpg)] bg-cover bg-center"></div>
```

- 잘라내기 없이 채우기

`bg-contain` 유틸리티를 사용해 배경 이미지를 잘라내거나 늘리지 않고 바깥 경계에 맞게 크기를 조정합니다:

```
    <div class="bg-[url(/img/mountains.jpg)] bg-contain bg-center"></div>
```

- 기본 크기 사용하기

`bg-auto` 유틸리티를 사용해 배경 이미지를 기본 크기로 표시합니다:

```
    <div class="bg-[url(/img/mountains.jpg)] bg-auto bg-center bg-no-repeat"></div>
```

- 사용자 지정 값 사용하기

`bg-size-[<value>]` 문법을 사용해 완전히 사용자 지정한 값으로 배경 크기를 설정합니다:

```
    <div class="bg-size-[auto_100px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `bg-size-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="bg-size-(--my-image-size) ...">  <!-- ... --></div>
```

이것은 `var()` 함수를 자동으로 추가해 주는 `bg-size-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`background-size` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="bg-auto md:bg-contain ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
