---
title: "transition-delay - 전환 및 애니메이션 - Tailwind CSS"
description: "delay-150, delay-700 같은 유틸리티를 사용해 요소의 전환 지연 시간을 밀리초 단위로 설정하세요:"
---

# transition-delay - 전환 및 애니메이션 - Tailwind CSS

| 클래스                      | 스타일                                      |
| --------------------------- | ------------------------------------------- |
| `delay-<number>`            | `transition-delay: <number>ms;`             |
| `delay-(<custom-property>)` | `transition-delay: var(<custom-property>);` |
| `delay-[<value>]`           | `transition-delay: <value>;`                |

## 예제

- 기본 예제

`delay-150`, `delay-700` 같은 유틸리티를 사용해 요소의 전환 지연 시간을 밀리초 단위로 설정하세요:

예상 동작을 보려면 각 버튼에 마우스를 올려보세요

delay-150

버튼 A

delay-300

버튼 B

delay-700

버튼 C

```
    <button class="transition delay-150 duration-300 ease-in-out ...">Button A</button><button class="transition delay-300 duration-300 ease-in-out ...">Button B</button><button class="transition delay-700 duration-300 ease-in-out ...">Button C</button>
```

- 축소된 모션 지원

사용자가 축소된 모션을 선호하도록 설정한 경우, `motion-safe` 및 `motion-reduce` 변형을 사용해 애니메이션과 전환을 조건부로 적용할 수 있습니다:

```
    <button type="button" class="delay-300 motion-reduce:delay-0 ...">  <!-- ... --></button>
```

- 사용자 정의 값 사용

완전히 사용자 정의된 값을 기준으로 전환 지연 시간을 설정하려면 `delay-[<value>]` 문법을 사용하세요:

```
    <button class="delay-[1s,250ms] ...">  <!-- ... --></button>
```

CSS 변수의 경우 `delay-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <button class="delay-(--my-delay) ...">  <!-- ... --></button>
```

이는 `var()` 함수를 자동으로 추가해 주는 `delay-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `transition-delay` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <button class="delay-150 md:delay-300 ...">  <!-- ... --></button>
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
