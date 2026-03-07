---
title: "stroke-width - SVG - Tailwind CSS"
description: "`stroke-1` 및 `stroke-2` 같은 `stroke-<number>` 유틸리티를 사용해 SVG의 스트로크 너비를 설정합니다:"
---

Source URL: https://tailwindcss.com/docs/stroke-width

# stroke-width - SVG - Tailwind CSS

| Class                               | Styles                                  |
| ----------------------------------- | --------------------------------------- |
| `stroke-<number>`                   | `stroke-width: <number>;`               |
| `stroke-(length:<custom-property>)` | `stroke-width: var(<custom-property>);` |
| `stroke-[<value>]`                  | `stroke-width: <value>;`                |

## 예제

- 기본 예제

`stroke-1`, `stroke-2` 같은 `stroke-<number>` 유틸리티를 사용해 SVG의 스트로크 너비를 설정합니다:

```
    <svg class="stroke-1 ..."></svg><svg class="stroke-2 ..."></svg>
```

이는 [Heroicons](https://heroicons.com) 같은 아이콘 세트를 스타일링할 때 유용합니다.

- 사용자 정의 값 사용하기

완전히 사용자 정의한 값을 기준으로 스트로크 너비를 설정하려면 `stroke-[<value>]` 문법을 사용하세요:

```
    <div class="stroke-[1.5] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `stroke-(length:<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="stroke-(length:--my-stroke-width) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `stroke-[length:var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`stroke-width` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="stroke-1 md:stroke-2 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
