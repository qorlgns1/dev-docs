---
title: "transform - 변환 - Tailwind CSS"
description: "전환이 CPU 대신 GPU에서 렌더링될 때 성능이 더 좋다면, transform-gpu 유틸리티를 추가해 하드웨어 가속을 강제할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/transform

# transform - 변환 - Tailwind CSS

| 클래스                          | 스타일                                                                                                                 |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `transform-(<custom-property>)` | `transform: var(<custom-property>);`                                                                                   |
| `transform-[<value>]`           | `transform: <value>;`                                                                                                  |
| `transform-none`                | `transform: none;`                                                                                                     |
| `transform-gpu`                 | `transform: translateZ(0) var(--tw-rotate-x) var(--tw-rotate-y) var(--tw-rotate-z) var(--tw-skew-x) var(--tw-skew-y);` |
| `transform-cpu`                 | `transform: var(--tw-rotate-x) var(--tw-rotate-y) var(--tw-rotate-z) var(--tw-skew-x) var(--tw-skew-y);`               |

## 예제

- 하드웨어 가속

전환이 CPU 대신 GPU에서 렌더링될 때 성능이 더 좋다면, `transform-gpu` 유틸리티를 추가해 하드웨어 가속을 강제할 수 있습니다:

```
    <div class="scale-150 transform-gpu">  <!-- ... --></div>
```

이 조건을 상황에 따라 되돌려야 한다면 `transform-cpu` 유틸리티를 사용해 다시 CPU로 강제할 수 있습니다.

- 변환 제거하기

`transform-none` 유틸리티를 사용하면 요소에 적용된 모든 변환을 한 번에 제거할 수 있습니다:

```
    <div class="skew-y-3 md:transform-none">  <!-- ... --></div>
```

- 사용자 정의 값 사용하기

`transform-[<value>]` 문법을 사용하면 완전히 사용자 정의한 값을 기준으로 변환을 설정할 수 있습니다:

```
    <div class="transform-[matrix(1,2,3,4,5,6)] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `transform-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="transform-(--my-transform) ...">  <!-- ... --></div>
```

이것은 `var()` 함수를 자동으로 추가해 주는 `transform-[var(<custom-property>)]`의 단축 문법입니다.
