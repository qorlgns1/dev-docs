---
title: "mask-size - 효과 - Tailwind CSS"
description: "mask-cover 유틸리티를 사용해 마스크 이미지가 마스크 레이어를 꽉 채울 때까지 크기를 조정하고, 필요하면 이미지를 잘라냅니다:"
---

출처 URL: https://tailwindcss.com/docs/mask-size

# mask-size - 효과 - Tailwind CSS

| 클래스                          | 스타일                               |
| ------------------------------- | ------------------------------------ |
| `mask-auto`                     | `mask-size: auto;`                   |
| `mask-cover`                    | `mask-size: cover;`                  |
| `mask-contain`                  | `mask-size: contain;`                |
| `mask-size-(<custom-property>)` | `mask-size: var(<custom-property>);` |
| `mask-size-[<value>]`           | `mask-size: <value>;`                |

## 예제

- 컨테이너 채우기

`mask-cover` 유틸리티를 사용해 마스크 이미지가 마스크 레이어를 꽉 채울 때까지 크기를 조정하고, 필요하면 이미지를 잘라냅니다:

```
    <div class="mask-cover mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 자르지 않고 채우기

`mask-contain` 유틸리티를 사용해 마스크 이미지를 자르거나 늘리지 않고 바깥 경계까지 크기를 조정합니다:

```
    <div class="mask-contain mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 기본 크기 사용하기

`mask-auto` 유틸리티를 사용해 마스크 이미지를 기본 크기로 표시합니다:

```
    <div class="mask-auto mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 사용자 지정 값 사용하기

완전히 사용자 지정한 값을 기준으로 마스크 이미지 크기를 설정하려면 `mask-size-[<value>]` 구문을 사용합니다:

```
    <div class="mask-size-[auto_100px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `mask-size-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="mask-size-(--my-mask-size) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `mask-size-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`mask-size` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="mask-auto md:mask-contain ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
