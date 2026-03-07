---
title: "transition-duration - 트랜지션 및 애니메이션 - Tailwind CSS"
description: "duration-150 및 duration-700 같은 유틸리티를 사용해 요소의 트랜지션 지속 시간을 밀리초 단위로 설정합니다:"
---

출처 URL: https://tailwindcss.com/docs/transition-duration

# transition-duration - 트랜지션 및 애니메이션 - Tailwind CSS

| 클래스                         | 스타일                                         |
| ------------------------------ | ---------------------------------------------- |
| `duration-<number>`            | `transition-duration: <number>ms;`             |
| `duration-initial`             | `transition-duration: initial;`                |
| `duration-(<custom-property>)` | `transition-duration: var(<custom-property>);` |
| `duration-[<value>]`           | `transition-duration: <value>;`                |

## 예제

- 기본 예제

`duration-150` 및 `duration-700` 같은 유틸리티를 사용해 요소의 트랜지션 지속 시간을 밀리초 단위로 설정합니다:

각 버튼에 마우스를 올려 예상 동작을 확인해 보세요.

duration-150

버튼 A

duration-300

버튼 B

duration-700

버튼 C

```
    <button class="transition duration-150 ease-in-out ...">Button A</button><button class="transition duration-300 ease-in-out ...">Button B</button><button class="transition duration-700 ease-in-out ...">Button C</button>
```

- 감소된 모션 지원

사용자가 감소된 모션을 선호하도록 지정한 경우, `motion-safe` 및 `motion-reduce` 변형을 사용해 애니메이션과 트랜지션을 조건부로 적용할 수 있습니다:

```
    <button type="button" class="duration-300 motion-reduce:duration-0 ...">  <!-- ... --></button>
```

- 사용자 정의 값 사용

`duration-[<value>]` 문법을 사용해 완전히 사용자 정의된 값을 기반으로 트랜지션 지속 시간을 설정할 수 있습니다:

```
    <button class="duration-[1s,15s] ...">  <!-- ... --></button>
```

CSS 변수의 경우 `duration-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <button class="duration-(--my-duration) ...">  <!-- ... --></button>
```

이는 `duration-[var(<custom-property>)]`의 단축 문법으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`transition-duration` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙여 중간 화면 크기 이상에서만 유틸리티를 적용할 수 있습니다:

```
    <button class="duration-0 md:duration-150 ...">  <!-- ... --></button>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
