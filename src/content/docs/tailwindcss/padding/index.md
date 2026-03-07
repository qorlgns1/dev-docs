---
title: "padding - 간격 - Tailwind CSS"
description: "요소의 모든 면에 패딩을 제어하려면 `p-4`, `p-8` 같은 `p-<number>` 유틸리티를 사용하세요:"
---

Source URL: https://tailwindcss.com/docs/padding

# padding - 간격 - Tailwind CSS

| 클래스                    | 스타일                                                   |
| ------------------------- | -------------------------------------------------------- |
| `p-<number>`              | `padding: calc(var(--spacing) * <number>);`              |
| `p-px`                    | `padding: 1px;`                                          |
| `p-(<custom-property>)`   | `padding: var(<custom-property>);`                       |
| `p-[<value>]`             | `padding: <value>;`                                      |
| `px-<number>`             | `padding-inline: calc(var(--spacing) * <number>);`       |
| `px-px`                   | `padding-inline: 1px;`                                   |
| `px-(<custom-property>)`  | `padding-inline: var(<custom-property>);`                |
| `px-[<value>]`            | `padding-inline: <value>;`                               |
| `py-<number>`             | `padding-block: calc(var(--spacing) * <number>);`        |
| `py-px`                   | `padding-block: 1px;`                                    |
| `py-(<custom-property>)`  | `padding-block: var(<custom-property>);`                 |
| `py-[<value>]`            | `padding-block: <value>;`                                |
| `ps-<number>`             | `padding-inline-start: calc(var(--spacing) * <number>);` |
| `ps-px`                   | `padding-inline-start: 1px;`                             |
| `ps-(<custom-property>)`  | `padding-inline-start: var(<custom-property>);`          |
| `ps-[<value>]`            | `padding-inline-start: <value>;`                         |
| `pe-<number>`             | `padding-inline-end: calc(var(--spacing) * <number>);`   |
| `pe-px`                   | `padding-inline-end: 1px;`                               |
| `pe-(<custom-property>)`  | `padding-inline-end: var(<custom-property>);`            |
| `pe-[<value>]`            | `padding-inline-end: <value>;`                           |
| `pbs-<number>`            | `padding-block-start: calc(var(--spacing) * <number>);`  |
| `pbs-px`                  | `padding-block-start: 1px;`                              |
| `pbs-(<custom-property>)` | `padding-block-start: var(<custom-property>);`           |
| `pbs-[<value>]`           | `padding-block-start: <value>;`                          |
| `pbe-<number>`            | `padding-block-end: calc(var(--spacing) * <number>);`    |
| `pbe-px`                  | `padding-block-end: 1px;`                                |
| `pbe-(<custom-property>)` | `padding-block-end: var(<custom-property>);`             |
| `pbe-[<value>]`           | `padding-block-end: <value>;`                            |
| `pt-<number>`             | `padding-top: calc(var(--spacing) * <number>);`          |
| `pt-px`                   | `padding-top: 1px;`                                      |
| `pt-(<custom-property>)`  | `padding-top: var(<custom-property>);`                   |
| `pt-[<value>]`            | `padding-top: <value>;`                                  |
| `pr-<number>`             | `padding-right: calc(var(--spacing) * <number>);`        |
| `pr-px`                   | `padding-right: 1px;`                                    |
| `pr-(<custom-property>)`  | `padding-right: var(<custom-property>);`                 |
| `pr-[<value>]`            | `padding-right: <value>;`                                |
| `pb-<number>`             | `padding-bottom: calc(var(--spacing) * <number>);`       |
| `pb-px`                   | `padding-bottom: 1px;`                                   |
| `pb-(<custom-property>)`  | `padding-bottom: var(<custom-property>);`                |
| `pb-[<value>]`            | `padding-bottom: <value>;`                               |
| `pl-<number>`             | `padding-left: calc(var(--spacing) * <number>);`         |
| `pl-px`                   | `padding-left: 1px;`                                     |
| `pl-(<custom-property>)`  | `padding-left: var(<custom-property>);`                  |
| `pl-[<value>]`            | `padding-left: <value>;`                                 |

더 보기

## 예제

- 기본 예제

요소의 모든 면에 패딩을 제어하려면 `p-4`, `p-8` 같은 `p-<number>` 유틸리티를 사용하세요:

p-8

```
    <div class="p-8 ...">p-8</div>
```

- 한쪽에 패딩 추가

요소의 한쪽 패딩을 제어하려면 `pt-6`, `pr-4` 같은 `pt-<number>`, `pr-<number>`, `pb-<number>`, `pl-<number>` 유틸리티를 사용하세요:

pt-6

pr-4

pb-8

pl-2

```
    <div class="pt-6 ...">pt-6</div><div class="pr-4 ...">pr-4</div><div class="pb-8 ...">pb-8</div><div class="pl-2 ...">pl-2</div>
```

- 가로 패딩 추가

요소의 가로 패딩을 제어하려면 `px-4`, `px-8` 같은 `px-<number>` 유틸리티를 사용하세요:

px-8

```
    <div class="px-8 ...">px-8</div>
```

- 세로 패딩 추가

요소의 세로 패딩을 제어하려면 `py-4`, `py-8` 같은 `py-<number>` 유틸리티를 사용하세요:

py-8

```
    <div class="py-8 ...">py-8</div>
```

- 논리 속성 사용

텍스트 방향에 따라 왼쪽 또는 오른쪽에 매핑되는 `padding-inline-start` 및 `padding-inline-end` 논리 속성을 설정하려면 `ps-4`, `pe-8` 같은 `ps-<number>` 또는 `pe-<number>` 유틸리티를 사용하세요:

왼쪽에서 오른쪽

ps-8

pe-8

오른쪽에서 왼쪽

ps-8

pe-8

```
    <div>  <div dir="ltr">    <div class="ps-8 ...">ps-8</div>    <div class="pe-8 ...">pe-8</div>  </div>  <div dir="rtl">    <div class="ps-8 ...">ps-8</div>    <div class="pe-8 ...">pe-8</div>  </div></div>
```

더 세밀하게 제어하려면 [LTR and RTL modifiers](https://tailwindcss.com/docs/hover-focus-and-other-states#rtl-support)도 사용해 현재 텍스트 방향에 따라 특정 스타일을 조건부로 적용할 수 있습니다.

쓰기 모드에 따라 위쪽 또는 아래쪽에 매핑되는 `padding-block-start` 및 `padding-block-end` 논리 속성을 설정하려면 `pbs-<number>` 및 `pbe-<number>` 유틸리티를 사용하세요:

```
    <div class="pbs-8 ...">pbs-8</div>
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값을 기준으로 패딩을 설정하려면 `p-[<value>]`,`px-[<value>]`, `pb-[<value>]` 같은 유틸리티를 사용하세요:

```
    <div class="p-[5px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `p-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="p-(--my-padding) ...">  <!-- ... --></div>
```

이 구문은 `var()` 함수를 자동으로 추가해 주는 `p-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`padding` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="py-4 md:py-8 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.

## 테마 사용자 지정

`p-<number>`,`px-<number>`,`py-<number>`,`ps-<number>`,`pe-<number>`,`pbs-<number>`,`pbe-<number>`,`pt-<number>`,`pr-<number>`,`pb-<number>`, `pl-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 동작하며, 이 변수는 사용자 테마에서 사용자 지정할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 사용자 지정에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
