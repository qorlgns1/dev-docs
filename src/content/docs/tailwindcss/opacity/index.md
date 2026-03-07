---
title: "opacity - 효과 - Tailwind CSS"
description: "opacity-25, opacity-100 같은 opacity-<number> 유틸리티를 사용해 요소의 투명도를 설정하세요:"
---

출처 URL: https://tailwindcss.com/docs/opacity

# opacity - 효과 - Tailwind CSS

| 클래스                        | 스타일                             |
| ----------------------------- | ---------------------------------- |
| `opacity-<number>`            | `opacity: <number>%;`              |
| `opacity-(<custom-property>)` | `opacity: var(<custom-property>);` |
| `opacity-[<value>]`           | `opacity: <value>;`                |

## 예제

- 기본 예제

`opacity-25`, `opacity-100` 같은 `opacity-<number>` 유틸리티를 사용해 요소의 투명도를 설정하세요:

opacity-100

버튼 A

opacity-75

버튼 B

opacity-50

버튼 C

opacity-25

버튼 D

```
    <button class="bg-indigo-500 opacity-100 ..."></button><button class="bg-indigo-500 opacity-75 ..."></button><button class="bg-indigo-500 opacity-50 ..."></button><button class="bg-indigo-500 opacity-25 ..."></button>
```

- 조건부 적용

`disabled:*` 같은 variant를 `opacity` 유틸리티 앞에 붙여 해당 상태에서만 유틸리티가 적용되도록 하세요:

```
    <input class="opacity-100 disabled:opacity-75 ..." type="text" />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

- 사용자 정의 값 사용

완전히 사용자 정의한 값으로 투명도를 설정하려면 `opacity-[<value>]` 문법을 사용하세요:

```
    <button class="opacity-[.67] ...">  <!-- ... --></button>
```

CSS 변수의 경우 `opacity-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <button class="opacity-(--my-opacity) ...">  <!-- ... --></button>
```

이는 `var()` 함수를 자동으로 추가해 주는 `opacity-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`md:` 같은 breakpoint variant를 `opacity` 유틸리티 앞에 붙여 중간 크기 이상의 화면에서만 유틸리티가 적용되도록 하세요:

```
    <button class="opacity-50 md:opacity-100 ...">  <!-- ... --></button>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
