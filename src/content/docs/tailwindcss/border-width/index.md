---
title: "border-width - 테두리 - Tailwind CSS"
description: "요소의 모든 면에 테두리 너비를 설정하려면 border-2, border-4 같은 border 또는 border-<number> 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/border-width

# border-width - 테두리 - Tailwind CSS

| 클래스                                 | 스타일                                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `border`                               | `border-width: 1px;`                                                                                         |
| `border-<number>`                      | `border-width: <number>px;`                                                                                  |
| `border-(length:<custom-property>)`    | `border-width: var(<custom-property>);`                                                                      |
| `border-[<value>]`                     | `border-width: <value>;`                                                                                     |
| `border-x`                             | `border-inline-width: 1px;`                                                                                  |
| `border-x-<number>`                    | `border-inline-width: <number>px;`                                                                           |
| `border-x-(length:<custom-property>)`  | `border-inline-width: var(<custom-property>);`                                                               |
| `border-x-[<value>]`                   | `border-inline-width: <value>;`                                                                              |
| `border-y`                             | `border-block-width: 1px;`                                                                                   |
| `border-y-<number>`                    | `border-block-width: <number>px;`                                                                            |
| `border-y-(length:<custom-property>)`  | `border-block-width: var(<custom-property>);`                                                                |
| `border-y-[<value>]`                   | `border-block-width: <value>;`                                                                               |
| `border-s`                             | `border-inline-start-width: 1px;`                                                                            |
| `border-s-<number>`                    | `border-inline-start-width: <number>px;`                                                                     |
| `border-s-(length:<custom-property>)`  | `border-inline-start-width: var(<custom-property>);`                                                         |
| `border-s-[<value>]`                   | `border-inline-start-width: <value>;`                                                                        |
| `border-e`                             | `border-inline-end-width: 1px;`                                                                              |
| `border-e-<number>`                    | `border-inline-end-width: <number>px;`                                                                       |
| `border-e-(length:<custom-property>)`  | `border-inline-end-width: var(<custom-property>);`                                                           |
| `border-e-[<value>]`                   | `border-inline-end-width: <value>;`                                                                          |
| `border-bs`                            | `border-block-start-width: 1px;`                                                                             |
| `border-bs-<number>`                   | `border-block-start-width: <number>px;`                                                                      |
| `border-bs-(length:<custom-property>)` | `border-block-start-width: var(<custom-property>);`                                                          |
| `border-bs-[<value>]`                  | `border-block-start-width: <value>;`                                                                         |
| `border-be`                            | `border-block-end-width: 1px;`                                                                               |
| `border-be-<number>`                   | `border-block-end-width: <number>px;`                                                                        |
| `border-be-(length:<custom-property>)` | `border-block-end-width: var(<custom-property>);`                                                            |
| `border-be-[<value>]`                  | `border-block-end-width: <value>;`                                                                           |
| `border-t`                             | `border-top-width: 1px;`                                                                                     |
| `border-t-<number>`                    | `border-top-width: <number>px;`                                                                              |
| `border-t-(length:<custom-property>)`  | `border-top-width: var(<custom-property>);`                                                                  |
| `border-t-[<value>]`                   | `border-top-width: <value>;`                                                                                 |
| `border-r`                             | `border-right-width: 1px;`                                                                                   |
| `border-r-<number>`                    | `border-right-width: <number>px;`                                                                            |
| `border-r-(length:<custom-property>)`  | `border-right-width: var(<custom-property>);`                                                                |
| `border-r-[<value>]`                   | `border-right-width: <value>;`                                                                               |
| `border-b`                             | `border-bottom-width: 1px;`                                                                                  |
| `border-b-<number>`                    | `border-bottom-width: <number>px;`                                                                           |
| `border-b-(length:<custom-property>)`  | `border-bottom-width: var(<custom-property>);`                                                               |
| `border-b-[<value>]`                   | `border-bottom-width: <value>;`                                                                              |
| `border-l`                             | `border-left-width: 1px;`                                                                                    |
| `border-l-<number>`                    | `border-left-width: <number>px;`                                                                             |
| `border-l-(length:<custom-property>)`  | `border-left-width: var(<custom-property>);`                                                                 |
| `border-l-[<value>]`                   | `border-left-width: <value>;`                                                                                |
| `divide-x`                             | `& > :not(:last-child) { border-inline-start-width: 0px; border-inline-end-width: 1px; }`                    |
| `divide-x-<number>`                    | `& > :not(:last-child) { border-inline-start-width: 0px; border-inline-end-width: <number>px; }`             |
| `divide-x-(length:<custom-property>)`  | `& > :not(:last-child) { border-inline-start-width: 0px; border-inline-end-width: var(<custom-property>); }` |
| `divide-x-[<value>]`                   | `& > :not(:last-child) { border-inline-start-width: 0px; border-inline-end-width: <value>; }`                |
| `divide-y`                             | `& > :not(:last-child) { border-top-width: 0px; border-bottom-width: 1px; }`                                 |
| `divide-y-<number>`                    | `& > :not(:last-child) { border-top-width: 0px; border-bottom-width: <number>px; }`                          |
| `divide-y-(length:<custom-property>)`  | `& > :not(:last-child) { border-top-width: 0px; border-bottom-width: var(<custom-property>); }`              |
| `divide-y-[<value>]`                   | `& > :not(:last-child) { border-top-width: 0px; border-bottom-width: <value>; }`                             |
| `divide-x-reverse`                     | `--tw-divide-x-reverse: 1;`                                                                                  |
| `divide-y-reverse`                     | `--tw-divide-y-reverse: 1;`                                                                                  |

더 보기

## 예제

- 기본 예제

요소의 모든 면에 테두리 너비를 설정하려면 `border-2`, `border-4` 같은 `border` 또는 `border-<number>` 유틸리티를 사용하세요:

border

border-2

border-4

border-8

```
    <div class="border border-indigo-600 ..."></div><div class="border-2 border-indigo-600 ..."></div><div class="border-4 border-indigo-600 ..."></div><div class="border-8 border-indigo-600 ..."></div>
```

- 개별 면

요소의 한 면에 테두리 너비를 설정하려면 `border-r`, `border-t-4` 같은 유틸리티를 사용하세요:

border-t-4

border-r-4

border-b-4

border-l-4

```
    <div class="border-t-4 border-indigo-500 ..."></div><div class="border-r-4 border-indigo-500 ..."></div><div class="border-b-4 border-indigo-500 ..."></div><div class="border-l-4 border-indigo-500 ..."></div>
```

- 가로 및 세로 면

요소의 두 면에 동시에 테두리 너비를 설정하려면 `border-x`, `border-y-4` 같은 유틸리티를 사용하세요:

border-x-4

border-y-4

```
    <div class="border-x-4 border-indigo-500 ..."></div><div class="border-y-4 border-indigo-500 ..."></div>
```

- 논리 속성 사용하기

`border-inline-start-width`와 `border-inline-end-width` [논리 속성](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts)을 설정하려면 `border-s`, `border-e-4` 같은 유틸리티를 사용하세요. 이 속성들은 텍스트 방향에 따라 왼쪽 또는 오른쪽 테두리에 매핑됩니다:

왼쪽에서 오른쪽

오른쪽에서 왼쪽

```
    <div dir="ltr">  <div class="border-s-4 ..."></div></div><div dir="rtl">  <div class="border-s-4 ..."></div></div>
```

`border-block-start-width`와 `border-block-end-width` 논리 속성을 설정하려면 `border-bs-<number>`, `border-be-<number>` 유틸리티를 사용하세요. 이 속성들은 쓰기 모드에 따라 위쪽 또는 아래쪽 테두리에 매핑됩니다:

```
    <div class="border-bs-4 ..."></div>
```

- 자식 요소 사이

자식 요소 사이에 테두리를 추가하려면 `divide-x`, `divide-y-4` 같은 유틸리티를 사용하세요:

01

02

03

```
    <div class="grid grid-cols-3 divide-x-4">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

#

- 자식 요소 순서 뒤집기

요소가 역순일 때(`flex-row-reverse` 또는 `flex-col-reverse` 사용) 각 요소의 올바른 면에 테두리가 추가되도록 `divide-x-reverse` 또는 `divide-y-reverse` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex flex-col-reverse divide-y-4 divide-y-reverse divide-gray-200">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 사용자 정의 값 사용하기

완전히 사용자 정의한 값을 기준으로 테두리 너비를 설정하려면 `border-[<value>]` 구문을 사용하세요:

```
    <div class="border-[2vw] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `border-(length:<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="border-(length:--my-border-width) ...">  <!-- ... --></div>
```

이 구문은 `border-[length:var(<custom-property>)]`의 단축형으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `border-width` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <div class="border-2 md:border-t-4 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
