---
title: "outline-width - 테두리 - Tailwind CSS"
description: "`outline` 또는 `outline-<number>` 유틸리티(`outline-2`, `outline-4` 등)를 사용해 요소의 아웃라인 너비를 설정합니다:"
---

원본 URL: https://tailwindcss.com/docs/outline-width

# outline-width - 테두리 - Tailwind CSS

| 클래스                               | 스타일                                   |
| ------------------------------------ | ---------------------------------------- |
| `outline`                            | `outline-width: 1px;`                    |
| `outline-<number>`                   | `outline-width: <number>px;`             |
| `outline-(length:<custom-property>)` | `outline-width: var(<custom-property>);` |
| `outline-[<value>]`                  | `outline-width: <value>;`                |

## 예제

- 기본 예제

`outline` 또는 `outline-<number>` 유틸리티(`outline-2`, `outline-4` 등)를 사용해 요소의 아웃라인 너비를 설정합니다:

outline

버튼 A

outline-2

버튼 B

outline-4

버튼 C

```
    <button class="outline outline-offset-2 ...">Button A</button><button class="outline-2 outline-offset-2 ...">Button B</button><button class="outline-4 outline-offset-2 ...">Button C</button>
```

- 포커스 시 적용

`outline-width` 유틸리티 앞에 `focus:*` 같은 variant를 붙이면 해당 상태에서만 유틸리티가 적용됩니다:

버튼에 포커스를 맞춰 아웃라인이 추가되는 것을 확인하세요

변경 사항 저장

```
    <button class="outline-offset-2 outline-sky-500 focus:outline-2 ...">Save Changes</button>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 확인하세요.

- 사용자 정의 값 사용

완전히 사용자 정의한 값으로 아웃라인 너비를 설정하려면 `outline-[<value>]` 문법을 사용하세요:

```
    <div class="outline-[2vw] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `outline-(length:<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="outline-(length:--my-outline-width) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `outline-[length:var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`outline-width` 유틸리티 앞에 `md:` 같은 breakpoint variant를 붙이면 중간 크기 화면 이상에서만 유틸리티가 적용됩니다:

```
    <div class="outline md:outline-2 ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 확인하세요.
