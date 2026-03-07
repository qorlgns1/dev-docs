---
title: "outline-offset - 테두리 - Tailwind CSS"
description: "outline-offset-<number>| outline-offset: <number>px;"
---

원문 URL: https://tailwindcss.com/docs/outline-offset

# outline-offset - 테두리 - Tailwind CSS

| 클래스                               | 스타일                                    |
| ------------------------------------ | ----------------------------------------- |
| `outline-offset-<number>`            | `outline-offset: <number>px;`             |
| `-outline-offset-<number>`           | `outline-offset: calc(<number>px * -1);`  |
| `outline-offset-(<custom-property>)` | `outline-offset: var(<custom-property>);` |
| `outline-offset-[<value>]`           | `outline-offset: <value>;`                |

## 예시

- 기본 예시

`outline-offset-2`, `outline-offset-4` 같은 유틸리티를 사용해 요소의 outline 오프셋을 변경합니다:

outline-offset-0

버튼 A

outline-offset-2

버튼 B

outline-offset-4

버튼 C

```
    <button class="outline-2 outline-offset-0 ...">Button A</button><button class="outline-2 outline-offset-2 ...">Button B</button><button class="outline-2 outline-offset-4 ...">Button C</button>
```

- 사용자 정의 값 사용하기

`outline-offset-[<value>]` 문법을 사용하면 완전히 사용자 정의한 값을 기준으로 outline 오프셋을 설정할 수 있습니다:

```
    <div class="outline-offset-[2vw] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `outline-offset-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="outline-offset-(--my-outline-offset) ...">  <!-- ... --></div>
```

이 문법은 `var()` 함수를 자동으로 추가해 주는 `outline-offset-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`outline-offset` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 화면 크기 이상에서만 유틸리티가 적용됩니다:

```
    <div class="outline md:outline-offset-2 ...">  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
