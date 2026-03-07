---
title: "mask-position - 효과 - Tailwind CSS"
description: "요소의 마스크 이미지 위치를 제어하려면 mask-center, mask-right, mask-left-top 같은 유틸리티를 사용하세요:"
---

# mask-position - 효과 - Tailwind CSS

| 클래스                              | 스타일                                   |
| ----------------------------------- | ---------------------------------------- |
| `mask-top-left`                     | `mask-position: top left;`               |
| `mask-top`                          | `mask-position: top;`                    |
| `mask-top-right`                    | `mask-position: top right;`              |
| `mask-left`                         | `mask-position: left;`                   |
| `mask-center`                       | `mask-position: center;`                 |
| `mask-right`                        | `mask-position: right;`                  |
| `mask-bottom-left`                  | `mask-position: bottom left;`            |
| `mask-bottom`                       | `mask-position: bottom;`                 |
| `mask-bottom-right`                 | `mask-position: bottom right;`           |
| `mask-position-(<custom-property>)` | `mask-position: var(<custom-property>);` |
| `mask-position-[<value>]`           | `mask-position: <value>;`                |

## 예제

- 기본 예제

요소의 마스크 이미지 위치를 제어하려면 `mask-center`, `mask-right`, `mask-left-top` 같은 유틸리티를 사용하세요:

mask-top-left

mask-top

mask-top-right

mask-left

mask-center

mask-right

mask-bottom-left

mask-bottom

mask-bottom-right

```
    <div class="mask-top-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-top mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-top-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-center mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값으로 마스크 위치를 설정하려면 `mask-position-[<value>]` 구문을 사용하세요:

```
    <div class="mask-position-[center_top_1rem] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `mask-position-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="mask-position-(--my-mask-position) ...">  <!-- ... --></div>
```

이것은 `mask-position-[var(<custom-property>)]`의 단축 표기이며, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`mask-position` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="mask-center md:mask-top ...">  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
