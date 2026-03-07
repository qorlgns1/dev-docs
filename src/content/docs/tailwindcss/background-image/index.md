---
title: "background-image - 배경 - Tailwind CSS"
description: "bg-[<value>] 문법을 사용해 요소의 배경 이미지를 설정하세요:"
---

출처 URL: https://tailwindcss.com/docs/background-image

# background-image - 배경 - Tailwind CSS

| 클래스                          | 스타일                                                                                 |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| `bg-[<value>]`                  | `background-image: <value>;`                                                           |
| `bg-(image:<custom-property>)`  | `background-image: var(<custom-property>);`                                            |
| `bg-none`                       | `background-image: none;`                                                              |
| `bg-linear-to-t`                | `background-image: linear-gradient(to top, var(--tw-gradient-stops));`                 |
| `bg-linear-to-tr`               | `background-image: linear-gradient(to top right, var(--tw-gradient-stops));`           |
| `bg-linear-to-r`                | `background-image: linear-gradient(to right, var(--tw-gradient-stops));`               |
| `bg-linear-to-br`               | `background-image: linear-gradient(to bottom right, var(--tw-gradient-stops));`        |
| `bg-linear-to-b`                | `background-image: linear-gradient(to bottom, var(--tw-gradient-stops));`              |
| `bg-linear-to-bl`               | `background-image: linear-gradient(to bottom left, var(--tw-gradient-stops));`         |
| `bg-linear-to-l`                | `background-image: linear-gradient(to left, var(--tw-gradient-stops));`                |
| `bg-linear-to-tl`               | `background-image: linear-gradient(to top left, var(--tw-gradient-stops));`            |
| `bg-linear-<angle>`             | `background-image: linear-gradient(<angle> in oklab, var(--tw-gradient-stops));`       |
| `-bg-linear-<angle>`            | `background-image: linear-gradient(-<angle> in oklab, var(--tw-gradient-stops));`      |
| `bg-linear-(<custom-property>)` | `background-image: linear-gradient(var(--tw-gradient-stops, var(<custom-property>)));` |
| `bg-linear-[<value>]`           | `background-image: linear-gradient(var(--tw-gradient-stops, <value>));`                |
| `bg-radial`                     | `background-image: radial-gradient(in oklab, var(--tw-gradient-stops));`               |
| `bg-radial-(<custom-property>)` | `background-image: radial-gradient(var(--tw-gradient-stops, var(<custom-property>)));` |
| `bg-radial-[<value>]`           | `background-image: radial-gradient(var(--tw-gradient-stops, <value>));`                |
| `bg-conic-<angle>`              | `background-image: conic-gradient(from <angle> in oklab, var(--tw-gradient-stops));`   |
| `-bg-conic-<angle>`             | `background-image: conic-gradient(from -<angle> in oklab, var(--tw-gradient-stops));`  |
| `bg-conic-(<custom-property>)`  | `background-image: var(<custom-property>);`                                            |
| `bg-conic-[<value>]`            | `background-image: <value>;`                                                           |
| `from-<color>`                  | `--tw-gradient-from: <color>;`                                                         |
| `from-<percentage>`             | `--tw-gradient-from-position: <percentage>;`                                           |
| `from-(<custom-property>)`      | `--tw-gradient-from: var(<custom-property>);`                                          |
| `from-[<value>]`                | `--tw-gradient-from: <value>;`                                                         |
| `via-<color>`                   | `--tw-gradient-via: <color>;`                                                          |
| `via-<percentage>`              | `--tw-gradient-via-position: <percentage>;`                                            |
| `via-(<custom-property>)`       | `--tw-gradient-via: var(<custom-property>);`                                           |
| `via-[<value>]`                 | `--tw-gradient-via: <value>;`                                                          |
| `to-<color>`                    | `--tw-gradient-to: <color>;`                                                           |
| `to-<percentage>`               | `--tw-gradient-to-position: <percentage>;`                                             |
| `to-(<custom-property>)`        | `--tw-gradient-to: var(<custom-property>);`                                            |
| `to-[<value>]`                  | `--tw-gradient-to: <value>;`                                                           |

더 보기

## 예시

- 기본 예시

`bg-[<value>]` 문법을 사용해 요소의 배경 이미지를 설정하세요:

```
    <div class="bg-[url(/img/mountains.jpg)] ..."></div>
```

- 선형 그라디언트 추가

`bg-linear-to-r`, `bg-linear-<angle>` 같은 유틸리티를 [color stop utilities](https://tailwindcss.com/docs/background-image#setting-gradient-color-stops)와 함께 사용해 요소에 선형 그라디언트를 추가하세요:

```
    <div class="h-14 bg-linear-to-r from-cyan-500 to-blue-500"></div><div class="h-14 bg-linear-to-t from-sky-500 to-indigo-500"></div><div class="h-14 bg-linear-to-bl from-violet-500 to-fuchsia-500"></div><div class="h-14 bg-linear-65 from-purple-500 to-pink-500"></div>
```

- 방사형 그라디언트 추가

`bg-radial`, `bg-radial-[<position>]` 유틸리티를 [color stop utilities](https://tailwindcss.com/docs/background-image#setting-gradient-color-stops)와 함께 사용해 요소에 방사형 그라디언트를 추가하세요:

```
    <div class="size-18 rounded-full bg-radial from-pink-400 from-40% to-fuchsia-700"></div><div class="size-18 rounded-full bg-radial-[at_50%_75%] from-sky-200 via-blue-400 to-indigo-900 to-90%"></div><div class="size-18 rounded-full bg-radial-[at_25%_25%] from-white to-zinc-900 to-75%"></div>
```

- 원뿔형 그라디언트 추가

`bg-conic`, `bg-conic-<angle>` 유틸리티를 [color stop utilities](https://tailwindcss.com/docs/background-image#setting-gradient-color-stops)와 함께 사용해 요소에 원뿔형 그라디언트를 추가하세요:

```
    <div class="size-24 rounded-full bg-conic from-blue-600 to-sky-400 to-50%"></div><div class="size-24 rounded-full bg-conic-180 from-indigo-600 via-indigo-50 to-indigo-600"></div><div class="size-24 rounded-full bg-conic/decreasing from-violet-700 via-lime-300 to-violet-700"></div>
```

- 그라디언트 색상 스톱 설정

`from-indigo-500`, `via-purple-500`, `to-pink-500` 같은 유틸리티를 사용해 그라디언트 스톱의 색상을 설정하세요:

```
    <div class="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 ..."></div>
```

- 그라디언트 스톱 위치 설정

`from-10%`, `via-30%`, `to-90%` 같은 유틸리티를 사용해 그라디언트 색상 스톱의 위치를 더 정밀하게 설정하세요:

10%

30%

90%

```
    <div class="bg-gradient-to-r from-indigo-500 from-10% via-sky-500 via-30% to-emerald-500 to-90% ..."></div>
```

- 보간 모드 변경

보간 모디파이어를 사용해 그라디언트의 보간 모드를 제어하세요:

srgb

hsl

oklab

oklch

longer

shorter

increasing

decreasing

```
    <div class="bg-linear-to-r/srgb from-indigo-500 to-teal-400"></div><div class="bg-linear-to-r/hsl from-indigo-500 to-teal-400"></div><div class="bg-linear-to-r/oklab from-indigo-500 to-teal-400"></div><div class="bg-linear-to-r/oklch from-indigo-500 to-teal-400"></div><div class="bg-linear-to-r/longer from-indigo-500 to-teal-400"></div><div class="bg-linear-to-r/shorter from-indigo-500 to-teal-400"></div><div class="bg-linear-to-r/increasing from-indigo-500 to-teal-400"></div><div class="bg-linear-to-r/decreasing from-indigo-500 to-teal-400"></div>
```

기본적으로 그라디언트는 `oklab` 색 공간에서 보간됩니다.

- 배경 이미지 제거

`bg-none` 유틸리티를 사용해 요소의 기존 배경 이미지를 제거하세요:

```
    <div class="bg-none"></div>
```

- 사용자 정의 값 사용

`bg-linear-[<value>]`, `from-[<value>]` 같은 유틸리티를 사용해 완전히 사용자 정의한 값을 기반으로 그라디언트를 설정하세요:

```
    <div class="bg-linear-[25deg,red_5%,yellow_60%,lime_90%,teal] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `bg-linear-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="bg-linear-(--my-gradient) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `bg-linear-[var(<custom-property>)]`의 축약 문법입니다.

- 반응형 디자인

`background-image` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙여, 중간 화면 크기 이상에서만 해당 유틸리티가 적용되게 하세요:

```
    <div class="from-purple-400 md:from-yellow-500 ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 정의

프로젝트의 색상 유틸리티를 사용자 정의하려면 `--color-*` 테마 변수를 사용하세요:

```
    @theme {  --color-regal-blue: #243c5a; }
```

이제 `from-regal-blue`, `via-regal-blue`, `to-regal-blue` 같은 유틸리티를 마크업에서 사용할 수 있습니다:

```
    <div class="from-regal-blue">  <!-- ... --></div>
```

테마 사용자 정의에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
