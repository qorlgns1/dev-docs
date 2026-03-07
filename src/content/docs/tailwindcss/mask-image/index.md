---
title: "mask-image - 효과 - Tailwind CSS"
description: "요소의 마스크 이미지를 설정하려면 mask-[<value>] 구문을 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/mask-image

# mask-image - 효과 - Tailwind CSS

| 클래스                                 | 스타일                                                                                                                                                                                                                                                   |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mask-[<value>]`                       | `mask-image: <value>;`                                                                                                                                                                                                                                   |
| `mask-(<custom-property>)`             | `mask-image: var(<custom-property>);`                                                                                                                                                                                                                    |
| `mask-none`                            | `mask-image: none;`                                                                                                                                                                                                                                      |
| `mask-linear-<number>`                 | `mask-image: linear-gradient(<number>deg, black var(--tw-mask-linear-from)), transparent var(--tw-mask-linear-to));`                                                                                                                                     |
| `-mask-linear-<number>`                | `mask-image: linear-gradient(calc(<number>deg * -1), black var(--tw-mask-linear-from)), transparent var(--tw-mask-linear-to));`                                                                                                                          |
| `mask-linear-from-<number>`            | `mask-image: linear-gradient(var(--tw-mask-linear-position), black calc(var(--spacing) * <number>), transparent var(--tw-mask-linear-to));`                                                                                                              |
| `mask-linear-from-<percentage>`        | `mask-image: linear-gradient(var(--tw-mask-linear-position), black <percentage>, transparent var(--tw-mask-linear-to));`                                                                                                                                 |
| `mask-linear-from-<color>`             | `mask-image: linear-gradient(var(--tw-mask-linear-position), <color> var(--tw-mask-linear-from), transparent var(--tw-mask-linear-to));`                                                                                                                 |
| `mask-linear-from-(<custom-property>)` | `mask-image: linear-gradient(var(--tw-mask-linear-position), black <custom-property>, transparent var(--tw-mask-linear-to));`                                                                                                                            |
| `mask-linear-from-[<value>]`           | `mask-image: linear-gradient(var(--tw-mask-linear-position), black <value>, transparent var(--tw-mask-linear-to));`                                                                                                                                      |
| `mask-linear-to-<number>`              | `mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), transparent calc(var(--spacing) * <number>));`                                                                                                            |
| `mask-linear-to-<percentage>`          | `mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), transparent <percentage>);`                                                                                                                               |
| `mask-linear-to-<color>`               | `mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), <color> var(--tw-mask-linear-to));`                                                                                                                       |
| `mask-linear-to-(<custom-property>)`   | `mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), transparent var(<custom-property>));`                                                                                                                     |
| `mask-linear-to-[<value>]`             | `mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), transparent <value>);`                                                                                                                                    |
| `mask-t-from-<number>`                 | `mask-image: linear-gradient(to top, black calc(var(--spacing) * <number>), transparent var(--tw-mask-top-to));`                                                                                                                                         |
| `mask-t-from-<percentage>`             | `mask-image: linear-gradient(to top, black <percentage>, transparent var(--tw-mask-top-to));`                                                                                                                                                            |
| `mask-t-from-<color>`                  | `mask-image: linear-gradient(to top, <color> var(--tw-mask-top-from), transparent var(--tw-mask-top-to));`                                                                                                                                               |
| `mask-t-from-(<custom-property>)`      | `mask-image: linear-gradient(to top, black var(<custom-property>), transparent var(--tw-mask-top-to));`                                                                                                                                                  |
| `mask-t-from-[<value>]`                | `mask-image: linear-gradient(to top, black <value>, transparent var(--tw-mask-top-to));`                                                                                                                                                                 |
| `mask-t-to-<number>`                   | `mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent calc(var(--spacing) * <number>));`                                                                                                                                       |
| `mask-t-to-<percentage>`               | `mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent <percentage>);`                                                                                                                                                          |
| `mask-t-to-<color>`                    | `mask-image: linear-gradient(to top, black var(--tw-mask-top-from), <color> var(--tw-mask-top-to));`                                                                                                                                                     |
| `mask-t-to-(<custom-property>)`        | `mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent var(<custom-property>));`                                                                                                                                                |
| `mask-t-to-[<value>]`                  | `mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent <value>);`                                                                                                                                                               |
| `mask-r-from-<number>`                 | `mask-image: linear-gradient(to right, black calc(var(--spacing) * <number>), transparent var(--tw-mask-right-to));`                                                                                                                                     |
| `mask-r-from-<percentage>`             | `mask-image: linear-gradient(to right, black <percentage>, transparent var(--tw-mask-right-to));`                                                                                                                                                        |
| `mask-r-from-<color>`                  | `mask-image: linear-gradient(to right, <color> var(--tw-mask-right-from), transparent var(--tw-mask-right-to));`                                                                                                                                         |
| `mask-r-from-(<custom-property>)`      | `mask-image: linear-gradient(to right, black var(<custom-property>), transparent var(--tw-mask-right-to));`                                                                                                                                              |
| `mask-r-from-[<value>]`                | `mask-image: linear-gradient(to right, black <value>, transparent var(--tw-mask-right-to));`                                                                                                                                                             |
| `mask-r-to-<number>`                   | `mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent calc(var(--spacing) * <number>));`                                                                                                                                   |
| `mask-r-to-<percentage>`               | `mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent <percentage>);`                                                                                                                                                      |
| `mask-r-to-<color>`                    | `mask-image: linear-gradient(to right, black var(--tw-mask-right-from), <color> var(--tw-mask-right-to));`                                                                                                                                               |
| `mask-r-to-(<custom-property>)`        | `mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent var(<custom-property>));`                                                                                                                                            |
| `mask-r-to-[<value>]`                  | `mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent <value>);`                                                                                                                                                           |
| `mask-b-from-<number>`                 | `mask-image: linear-gradient(to bottom, black calc(var(--spacing) * <number>), transparent var(--tw-mask-bottom-to));`                                                                                                                                   |
| `mask-b-from-<percentage>`             | `mask-image: linear-gradient(to bottom, black <percentage>, transparent var(--tw-mask-bottom-to));`                                                                                                                                                      |
| `mask-b-from-<color>`                  | `mask-image: linear-gradient(to bottom, <color> var(--tw-mask-bottom-from), transparent var(--tw-mask-bottom-to));`                                                                                                                                      |
| `mask-b-from-(<custom-property>)`      | `mask-image: linear-gradient(to bottom, black var(<custom-property>), transparent var(--tw-mask-bottom-to));`                                                                                                                                            |
| `mask-b-from-[<value>]`                | `mask-image: linear-gradient(to bottom, black <value>, transparent var(--tw-mask-bottom-to));`                                                                                                                                                           |
| `mask-b-to-<number>`                   | `mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent calc(var(--spacing) * <number>));`                                                                                                                                 |
| `mask-b-to-<percentage>`               | `mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent <percentage>);`                                                                                                                                                    |
| `mask-b-to-<color>`                    | `mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), <color> var(--tw-mask-bottom-to));`                                                                                                                                            |
| `mask-b-to-(<custom-property>)`        | `mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent var(<custom-property>));`                                                                                                                                          |
| `mask-b-to-[<value>]`                  | `mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent <value>);`                                                                                                                                                         |
| `mask-l-from-<number>`                 | `mask-image: linear-gradient(to left, black calc(var(--spacing) * <number>), transparent var(--tw-mask-left-to));`                                                                                                                                       |
| `mask-l-from-<percentage>`             | `mask-image: linear-gradient(to left, black <percentage>, transparent var(--tw-mask-left-to));`                                                                                                                                                          |
| `mask-l-from-<color>`                  | `mask-image: linear-gradient(to left, <color> var(--tw-mask-left-from), transparent var(--tw-mask-left-to));`                                                                                                                                            |
| `mask-l-from-(<custom-property>)`      | `mask-image: linear-gradient(to left, black var(<custom-property>), transparent var(--tw-mask-left-to));`                                                                                                                                                |
| `mask-l-from-[<value>]`                | `mask-image: linear-gradient(to left, black <value>, transparent var(--tw-mask-left-to));`                                                                                                                                                               |
| `mask-l-to-<number>`                   | `mask-image: linear-gradient(to left, black var(--tw-mask-left-from), transparent calc(var(--spacing) * <number>));`                                                                                                                                     |
| `mask-l-to-<percentage>`               | `mask-image: linear-gradient(to bottom, black var(--tw-mask-left-from), transparent <percentage>);`                                                                                                                                                      |
| `mask-l-to-<color>`                    | `mask-image: linear-gradient(to bottom, black var(--tw-mask-left-from), <color> var(--tw-mask-left-to));`                                                                                                                                                |
| `mask-l-to-(<custom-property>)`        | `mask-image: linear-gradient(to left, black var(--tw-mask-left-from), transparent var(<custom-property>));`                                                                                                                                              |
| `mask-l-to-[<value>]`                  | `mask-image: linear-gradient(to left, black var(--tw-mask-left-from), transparent <value>);`                                                                                                                                                             |
| `mask-y-from-<number>`                 | `mask-image: linear-gradient(to top, black calc(var(--spacing) * <number>), transparent var(--tw-mask-top-to)), linear-gradient(to bottom, black calc(var(--spacing) * <number>), transparent var(--tw-mask-bottom-to)); mask-composite: intersect;`     |
| `mask-y-from-<percentage>`             | `mask-image: linear-gradient(to top, black <percentage>, transparent var(--tw-mask-top-to)), linear-gradient(to bottom, black <percentage>, transparent var(--tw-mask-bottom-to)); mask-composite: intersect;`                                           |
| `mask-y-from-<color>`                  | `mask-image: linear-gradient(to top, <color> var(--tw-mask-top-from), transparent var(--tw-mask-top-to)), linear-gradient(to bottom, <color> var(--tw-mask-bottom-from), transparent var(--tw-mask-bottom-to)); mask-composite: intersect;`              |
| `mask-y-from-(<custom-property>)`      | `mask-image: linear-gradient(to top, black var(<custom-property>), transparent var(--tw-mask-top-to)), linear-gradient(to bottom, black var(<custom-property>), transparent var(--tw-mask-bottom-to)); mask-composite: intersect;`                       |
| `mask-y-from-[<value>]`                | `mask-image: linear-gradient(to top, black <value>, transparent var(--tw-mask-top-to)), linear-gradient(to bottom, black <value>, transparent var(--tw-mask-bottom-to)); mask-composite: intersect;`                                                     |
| `mask-y-to-<number>`                   | `mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent calc(var(--spacing) * <number>)), linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent calc(var(--spacing) * <number>)); mask-composite: intersect;` |
| `mask-y-to-<percentage>`               | `mask-image: linear-gradient(to bottom, black var(--tw-mask-top-from), transparent <percentage>), linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent <percentage>); mask-composite: intersect;`                                    |
| `mask-y-to-<color>`                    | `mask-image: linear-gradient(to bottom, black var(--tw-mask-top-from), <color> var(--tw-mask-top-to)), linear-gradient(to bottom, black var(--tw-mask-bottom-from), <color> var(--tw-mask-bottom-to)); mask-composite: intersect;`                       |
| `mask-y-to-(<custom-property>)`        | `mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent var(<custom-property>)),linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent var(<custom-property>)); mask-composite: intersect;`                    |
| `mask-y-to-[<value>]`                  | `mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent <value>),linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent <value>); mask-composite: intersect;`                                                  |
| `mask-x-from-<number>`                 | `mask-image: linear-gradient(to right, black calc(var(--spacing) * <number>), transparent var(--tw-mask-right-to)), linear-gradient(to left, black calc(var(--spacing) * <number>), transparent var(--tw-mask-left-to)); mask-composite: intersect;`     |
| `mask-x-from-<percentage>`             | `mask-image: linear-gradient(to right, black <percentage>, transparent var(--tw-mask-right-to)), linear-gradient(to left, black <percentage>, transparent var(--tw-mask-left-to)); mask-composite: intersect;`                                           |
| `mask-x-from-<color>`                  | `mask-image: linear-gradient(to right, <color> var(--tw-mask-right-from), transparent var(--tw-mask-right-to)), linear-gradient(to left, <color> var(--tw-mask-left-from), transparent var(--tw-mask-left-to)); mask-composite: intersect;`              |
| `mask-x-from-(<custom-property>)`      | `mask-image: linear-gradient(to right, black var(<custom-property>), transparent var(--tw-mask-right-to)), linear-gradient(to left, black var(<custom-property>), transparent var(--tw-mask-left-to)); mask-composite: intersect;`                       |
| `mask-x-from-[<value>]`                | `mask-image: linear-gradient(to right, black <value>, transparent var(--tw-mask-right-to)), linear-gradient(to left, black <value>, transparent var(--tw-mask-left-to)); mask-composite: intersect;`                                                     |
| `mask-x-to-<number>`                   | `mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent calc(var(--spacing) * <number>)), linear-gradient(to left, black var(--tw-mask-left-from), transparent calc(var(--spacing) * <number>)); mask-composite: intersect;` |
| `mask-x-to-<percentage>`               | `mask-image: linear-gradient(to left, black var(--tw-mask-right-from), transparent <percentage>), linear-gradient(to left, black var(--tw-mask-left-from), transparent <percentage>); mask-composite: intersect;`                                        |
| `mask-x-to-<color>`                    | `mask-image: linear-gradient(to left, black var(--tw-mask-right-from), <color> var(--tw-mask-right-to)), linear-gradient(to left, black var(--tw-mask-left-from), <color> var(--tw-mask-left-to)); mask-composite: intersect;`                           |

`mask-x-to-(<custom-property>)`| `mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent var(<custom-property>)),linear-gradient(to left, black var(--tw-mask-left-from), transparent var(<custom-property>)); mask-composite: intersect;`
`mask-x-to-[<value>]`| `mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent <value>),linear-gradient(to left, black var(--tw-mask-left-from), transparent <value>); mask-composite: intersect;`
`mask-radial-[<value>]`| `mask-image: radial-gradient(<value>);`
`mask-radial-[<size>]`| `--tw-mask-radial-size: <size>;`
`mask-radial-[<size>_<size>]`| `--tw-mask-radial-size: <size> <size>;`
`mask-radial-from-<number>`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black calc(var(--spacing) * <number>), transparent var(--tw-mask-radial-to));`
`mask-radial-from-<percentage>`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black <percentage>, transparent var(--tw-mask-radial-to));`
`mask-radial-from-<color>`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), <color> var(--tw-mask-radial-from), transparent var(--tw-mask-radial-to));`
`mask-radial-from-(<custom-property>)`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(<custom-property>), transparent var(--tw-mask-radial-to));`
`mask-radial-from-[<value>]`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black <value>, transparent var(--tw-mask-radial-to));`
`mask-radial-to-<number>`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), transparent calc(var(--spacing) * <number>));`
`mask-radial-to-<percentage>`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), transparent <percentage>);`
`mask-radial-to-<color>`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), <color> var(--tw-mask-radial-to));`
`mask-radial-to-(<custom-property>)`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), transparent var(<custom-property>));`
`mask-radial-to-[<value>]`| `mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), transparent <value>);`
`mask-circle`| `--tw-mask-radial-shape: circle;`
`mask-ellipse`| `--tw-mask-radial-shape: ellipse;`
`mask-radial-closest-corner`| `--tw-mask-radial-size: closest-corner;`
`mask-radial-closest-side`| `--tw-mask-radial-size: closest-side;`
`mask-radial-farthest-corner`| `--tw-mask-radial-size: farthest-corner;`
`mask-radial-farthest-side`| `--tw-mask-radial-size: farthest-side;`
`mask-radial-at-top-left`| `--tw-mask-radial-position: top left;`
`mask-radial-at-top`| `--tw-mask-radial-position: top;`
`mask-radial-at-top-right`| `--tw-mask-radial-position: top right;`
`mask-radial-at-left`| `--tw-mask-radial-position: left;`
`mask-radial-at-center`| `--tw-mask-radial-position: center;`
`mask-radial-at-right`| `--tw-mask-radial-position: right;`
`mask-radial-at-bottom-left`| `--tw-mask-radial-position: bottom left;`
`mask-radial-at-bottom`| `--tw-mask-radial-position: bottom;`
`mask-radial-at-bottom-right`| `--tw-mask-radial-position: bottom right;`
`mask-conic-<number>`| `mask-image: conic-gradient(from <number>deg, black var(--tw-mask-conic-from), transparent var(--tw-mask-conic-to));`
`-mask-conic-<number>`| `mask-image: conic-gradient(from calc(<number>deg * -1), black var(--tw-mask-conic-from), transparent var(--tw-mask-conic-to));`
`mask-conic-from-<number>`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black calc(var(--spacing) * <number>), transparent var(--tw-mask-conic-to));`
`mask-conic-from-<percentage>`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black <percentage>, transparent var(--tw-mask-conic-to));`
`mask-conic-from-<color>`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), <color> var(--tw-mask-conic-from), transparent var(--tw-mask-conic-to));`
`mask-conic-from-(<custom-property>)`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(<custom-property>), transparent var(--tw-mask-conic-to));`
`mask-conic-from-[<value>]`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black <value>, transparent var(--tw-mask-conic-to));`
`mask-conic-to-<number>`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), transparent calc(var(--spacing) * <number>));`
`mask-conic-to-<percentage>`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), transparent <percentage>);`
`mask-conic-to-<color>`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), <color> var(--tw-mask-conic-to);`
`mask-conic-to-(<custom-property>)`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), transparent var(<custom-property>);`
`mask-conic-to-[<value>]`| `mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), transparent <value>);`

더 보기

## 예제

- 이미지 마스크 사용하기

요소의 마스크 이미지를 설정하려면 `mask-[<value>]` 구문을 사용하세요:

```
    <div class="mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ...">  <!-- ... --></div>
```

- 가장자리 마스킹

`mask-b-from-<value>` 및 `mask-t-to-<value>` 같은 유틸리티를 사용해 요소의 한쪽 면에 선형 그라디언트 마스크를 추가하세요:

mask-t-from-50%

mask-r-from-30%

mask-l-from-50% mask-l-to-90%

mask-b-from-20% mask-b-to-80%

```
    <div class="mask-t-from-50% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-r-from-30% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-l-from-50% mask-l-to-90% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-b-from-20% mask-b-to-80% bg-[url(/img/mountains.jpg)] ..."></div>
```

또한 `mask-x-from-70%`, `mask-y-to-90%` 같은 유틸리티를 사용하면 요소의 두 면에 동시에 마스크를 적용할 수 있습니다:

mask-x-from-70% mask-x-to-90%

mask-y-from-70% mask-y-to-90%

```
    <div class="mask-x-from-70% mask-x-to-90% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-y-from-70% mask-y-to-90% bg-[url(/img/mountains.jpg)] ..."></div>
```

기본적으로 선형 그라디언트 마스크는 black에서 transparent로 전환되지만, `mask-<side>-from-<color>` 및 `mask-<side>-to-<color>` 유틸리티를 사용해 그라디언트 색상을 사용자 지정할 수 있습니다.

- 각도가 있는 선형 마스크 추가하기

`mask-linear-<angle>`, `mask-linear-from-20`, `mask-linear-to-40` 같은 유틸리티를 사용해 요소에 사용자 지정 선형 그라디언트 마스크를 추가하세요:

mask-linear-50

-mask-linear-50

```
    <div class="mask-linear-50 mask-linear-from-60% mask-linear-to-80% bg-[url(/img/mountains.jpg)] ..."></div><div class="-mask-linear-50 mask-linear-from-60% mask-linear-to-80% bg-[url(/img/mountains.jpg)] ..."></div>
```

- 방사형 마스크 추가하기

`mask-radial-from-<value>` 및 `mask-radial-to-<value>` 유틸리티를 사용해 요소에 방사형 그라디언트 마스크를 추가하세요:

![](https://tailwindcss.com/_next/static/media/keyboard-light.fbe8285c.png)![](https://tailwindcss.com/_next/static/media/keyboard-dark.8bd29bbf.png)

속도

파워 유저를 위해 설계됨

키보드 단축키로 그 어느 때보다 빠르게 작업하세요

```
    <div class="flex items-center gap-4">  <img class="mask-radial-[100%_100%] mask-radial-from-75% mask-radial-at-left ..." src="/img/keyboard.png" />  <div class="font-medium">    <p class="font-mono text-xs text-blue-500 uppercase dark:text-blue-400">Speed</p>    <p class="mt-2 text-base text-gray-700 dark:text-gray-300">Built for power users</p>    <p class="mt-1 text-sm leading-relaxed text-balance text-gray-500">      Work faster than ever with customizable keyboard shortcuts    </p>  </div></div>
```

기본적으로 방사형 그라디언트 마스크는 black에서 transparent로 전환되지만, `mask-radial-from-<color>` 및 `mask-radial-to-<color>` 유틸리티를 사용해 그라디언트 색상을 사용자 지정할 수 있습니다.

#

- 방사형 위치 설정하기

`mask-radial-at-bottom-left`, `mask-radial-at-[35%_35%]` 같은 유틸리티를 사용해 방사형 그라디언트 마스크 중심의 위치를 설정하세요:

mask-radial-at-top-left

mask-radial-at-top

mask-radial-at-top-right

mask-radial-at-left

mask-radial-at-center

mask-radial-at-right

mask-radial-at-bottom-left

mask-radial-at-bottom

mask-radial-at-bottom-right

```
    <div class="mask-radial-at-top-left mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-at-top mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-at-top-right mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-at-left mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-at-center mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-at-right mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-at-bottom-left mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-at-bottom mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-at-bottom-right mask-radial-from-100% bg-[url(/img/mountains.jpg)] ..."></div>
```

이는 마스크 이미지 자체의 위치를 설정하는 [`mask-position`](https://tailwindcss.com/docs/mask-position)과는 다르며, 방사형 그라디언트를 설정하는 것입니다.

#

- 방사형 크기 설정하기

`mask-radial-closest-corner`, `mask-radial-farthest-side` 같은 유틸리티를 사용해 방사형 그라디언트 마스크의 크기를 설정하세요:

mask-radial-closest-side

mask-radial-closest-corner

mask-radial-farthest-side

mask-radial-farthest-corner

```
    <div class="mask-radial-closest-side mask-radial-from-100% mask-radial-at-[30%_30%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-closest-corner mask-radial-from-100% mask-radial-at-[30%_30%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-farthest-side mask-radial-from-100% mask-radial-at-[30%_30%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-radial-farthest-corner mask-radial-from-100% mask-radial-at-[30%_30%] bg-[url(/img/mountains.jpg)] ..."></div>
```

사용자 지정 방사형 그라디언트 크기를 설정할 때 사용할 수 있는 단위는 그라디언트의 `<ending-shape>`에 따라 달라지며, 기본값은 `ellipse`입니다.

`mask-circle`에서는 `mask-radial-[5rem]`처럼 하나의 고정 길이만 사용할 수 있습니다. 반면 `mask-ellipse`에서는 `mask-radial-[40%_80%]`처럼 각 축을 고정 길이 또는 백분율로 지정할 수 있습니다.

- 원뿔형 마스크 추가하기

`mask-conic-from-<value>`, `mask-conic-to-<value>`, `mask-conic-<angle>` 유틸리티를 사용해 요소에 원뿔형 그라디언트 마스크를 추가하세요:

사용된 저장 공간: 75%

2 GB 중 0.48 GB 남음

```
    <div class="flex items-center gap-5 rounded-xl bg-white p-4 shadow-lg ring-1 ring-black/5 dark:bg-gray-800">  <div class="grid grid-cols-1 grid-rows-1">    <div class="border-4 border-gray-100 dark:border-gray-700 ..."></div>    <div class="border-4 border-amber-500 mask-conic-from-75% mask-conic-to-75% dark:border-amber-400 ..."></div>  </div>  <div class="w-0 flex-1 text-sm text-gray-950 dark:text-white">    <p class="font-medium">Storage used: 75%</p>    <p class="mt-1 text-gray-500 dark:text-gray-400"><span class="font-medium">0.48 GB</span> out of 2 GB remaining</p>  </div></div>
```

기본적으로 원뿔형 그라디언트 마스크는 black에서 transparent로 전환되지만, `mask-conic-from-<color>` 및 `mask-conic-to-<color>` 유틸리티를 사용해 그라디언트 색상을 사용자 지정할 수 있습니다.

- 마스크 결합하기

`mask-radial-from-<value>`, `mask-conic-to-<value>`, `mask-l-from-<value>` 같은 그라디언트 마스크 유틸리티를 결합해 더 복잡한 그라디언트 마스크를 만들 수 있습니다:

```
    <div class="mask-b-from-50% mask-radial-[50%_90%] mask-radial-from-80% bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-r-from-80% mask-b-from-80% mask-radial-from-70% mask-radial-to-85% bg-[url(/img/mountains.jpg)] ..."></div>
```

이 동작은 Tailwind가 기본적으로 [`mask-composite` property](https://tailwindcss.com/docs/mask-composite)를 `intersect`로 설정한다는 점에 의존합니다. 이 속성을 변경하면 그라디언트 마스크가 결합되는 방식에 영향을 줍니다.

- 마스크 이미지 제거하기

요소에서 기존 마스크 이미지를 제거하려면 `mask-none` 유틸리티를 사용하세요:

```
    <div class="mask-none">  <!-- ... --></div>
```

- 사용자 지정 값 사용하기

`mask-linear-[<value>]`, `mask-radial-[<value>]` 같은 유틸리티를 사용해 완전히 사용자 지정한 값을 기반으로 마스크 이미지를 설정하세요:

```
    <div class="mask-linear-[70deg,transparent_10%,black,transparent_80%] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `mask-linear-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="mask-linear-(--my-mask) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `mask-linear-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`mask-image` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 이상의 화면에서만 유틸리티가 적용됩니다:

```
    <div class="mask-radial-from-70% md:mask-radial-from-50% ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 지정

프로젝트의 색상 유틸리티를 사용자 지정하려면 `--color-*` 테마 변수를 사용하세요:

```
    @theme {  --color-regal-blue: #243c5a; }
```

이제 마크업에서 `mask-radial-from-regal-blue`,`mask-conic-to-regal-blue`, `mask-b-from-regal-blue` 같은 유틸리티를 사용할 수 있습니다:

```
    <div class="mask-radial-from-regal-blue">  <!-- ... --></div>
```

테마 사용자 지정에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
