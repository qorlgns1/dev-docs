---
title: "transition-timing-function - 트랜지션 및 애니메이션 - Tailwind CSS"
description: "ease-in, ease-out 같은 유틸리티를 사용해 요소 트랜지션의 easing 곡선을 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/transition-timing-function

# transition-timing-function - 트랜지션 및 애니메이션 - Tailwind CSS

| Class                      | Styles                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------ |
| `ease-linear`              | `transition-timing-function: linear;`                                                |
| `ease-in`                  | `transition-timing-function: var(--ease-in); /* cubic-bezier(0.4, 0, 1, 1) */`       |
| `ease-out`                 | `transition-timing-function: var(--ease-out); /* cubic-bezier(0, 0, 0.2, 1) */`      |
| `ease-in-out`              | `transition-timing-function: var(--ease-in-out); /* cubic-bezier(0.4, 0, 0.2, 1) */` |
| `ease-initial`             | `transition-timing-function: initial;`                                               |
| `ease-(<custom-property>)` | `transition-timing-function: var(<custom-property>);`                                |
| `ease-[<value>]`           | `transition-timing-function: <value>;`                                               |

## 예제

- 기본 예제

`ease-in`, `ease-out` 같은 유틸리티를 사용해 요소 트랜지션의 easing 곡선을 제어하세요:

각 버튼에 마우스를 올려 예상 동작을 확인해 보세요.

ease-in

버튼 A

ease-out

버튼 B

ease-in-out

버튼 C

```
    <button class="duration-300 ease-in ...">Button A</button><button class="duration-300 ease-out ...">Button B</button><button class="duration-300 ease-in-out ...">Button C</button>
```

- 사용자 지정 값 사용하기

`ease-[<value>]` 문법을 사용해 완전히 사용자 지정한 값으로 transition timing function을 설정할 수 있습니다:

```
    <button class="ease-[cubic-bezier(0.95,0.05,0.795,0.035)] ...">  <!-- ... --></button>
```

CSS 변수의 경우 `ease-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <button class="ease-(--my-ease) ...">  <!-- ... --></button>
```

이는 `var()` 함수를 자동으로 추가해 주는 `ease-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`transition-timing-function` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 크기 이상의 화면에서만 유틸리티가 적용됩니다:

```
    <button class="ease-out md:ease-in ...">  <!-- ... --></button>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 사용자 지정

프로젝트에서 transition timing function 유틸리티를 사용자 지정하려면 `--ease-*` 테마 변수를 사용하세요:

```
    @theme {  --ease-in-expo: cubic-bezier(0.95, 0.05, 0.795, 0.035); }
```

이제 마크업에서 `ease-in-expo` 유틸리티를 사용할 수 있습니다:

```
    <button class="ease-in-expo">  <!-- ... --></button>
```

테마 사용자 지정에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
