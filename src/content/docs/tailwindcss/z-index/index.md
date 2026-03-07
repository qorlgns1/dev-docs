---
title: "z-index - 레이아웃 - Tailwind CSS"
description: "z-10, z-50 같은 z-<number> 유틸리티를 사용하면 요소가 표시된 순서와 관계없이 쌓임 순서(또는 3차원 배치)를 제어할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/z-index

# z-index - 레이아웃 - Tailwind CSS

| 클래스                  | 스타일                             |
| ----------------------- | ---------------------------------- |
| `z-<number>`            | `z-index: <number>;`               |
| `z-auto`                | `z-index: auto;`                   |
| `z-[<value>]`           | `z-index: <value>;`                |
| `z-(<custom-property>)` | `z-index: var(<custom-property>);` |

## 예제

- 기본 예제

`z-10`, `z-50` 같은 `z-<number>` 유틸리티를 사용하면 요소가 표시된 순서와 관계없이 쌓임 순서(또는 3차원 배치)를 제어할 수 있습니다:

05

04

03

02

01

```
    <div class="z-40 ...">05</div><div class="z-30 ...">04</div><div class="z-20 ...">03</div><div class="z-10 ...">02</div><div class="z-0 ...">01</div>
```

- 음수 값 사용하기

음수 z-index 값을 사용하려면 클래스 이름 앞에 대시를 붙여 음수 값으로 변환하세요:

01

02

03

04

05

```
    <div class="...">05</div><div class="...">04</div><div class="-z-10 ...">03</div><div class="...">02</div><div class="...">01</div>
```

- 사용자 지정 값 사용하기

`z-[<value>]` 문법을 사용하면 완전히 사용자 지정한 값으로 쌓임 순서를 설정할 수 있습니다:

```
    <div class="z-[calc(var(--index)+1)] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `z-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="z-(--my-z) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `z-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`z-index` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="z-0 md:z-50 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
