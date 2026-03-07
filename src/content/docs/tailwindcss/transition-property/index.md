---
title: "transition-property - 전환 및 애니메이션 - Tailwind CSS"
description: "transition 및 transition-colors 같은 유틸리티를 사용해 값이 변경될 때 어떤 속성이 전환될지 지정합니다:"
---

# transition-property - 전환 및 애니메이션 - Tailwind CSS

| 클래스                           | 스타일                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `transition`                     | `transition-property: color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */` |
| `transition-all`                 | `transition-property: all; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`                                                                                                                                                                                                                                                                                                                  |
| `transition-colors`              | `transition-property: color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`                                                                                                                                                                   |
| `transition-opacity`             | `transition-property: opacity; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`                                                                                                                                                                                                                                                                                                              |
| `transition-shadow`              | `transition-property: box-shadow; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`                                                                                                                                                                                                                                                                                                           |
| `transition-transform`           | `transition-property: transform, translate, scale, rotate; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`                                                                                                                                                                                                                                                                                  |
| `transition-none`                | `transition-property: none;`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `transition-(<custom-property>)` | `transition-property: var(<custom-property>); transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`                                                                                                                                                                                                                                                                                               |
| `transition-[<value>]`           | `transition-property: <value>; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`                                                                                                                                                                                                                                                                                                              |

## 예시

- 기본 예시

`transition` 및 `transition-colors` 같은 유틸리티를 사용해 값이 변경될 때 어떤 속성이 전환될지 지정합니다:

예상 동작을 보려면 버튼에 마우스를 올려보세요

변경 사항 저장

```
    <button class="bg-blue-500 transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 ...">  Save Changes</button>
```

- 감소된 모션 지원

사용자가 감소된 모션을 선호하도록 설정한 상황에서는 `motion-safe` 및 `motion-reduce` variant를 사용해 애니메이션과 전환을 조건부로 적용할 수 있습니다:

```
    <button class="transform transition hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none ...">  <!-- ... --></button>
```

- 사용자 정의 값 사용

`transition-[<value>]` 문법을 사용해 완전히 사용자 정의된 값을 기반으로 전환 속성을 설정합니다:

```
    <button class="transition-[height] ...">  <!-- ... --></button>
```

CSS 변수의 경우 `transition-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <button class="transition-(--my-properties) ...">  <!-- ... --></button>
```

이는 `var()` 함수를 자동으로 추가해 주는 `transition-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`transition-property` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <button class="transition-none md:transition-all ...">  <!-- ... --></button>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 알아보세요.
