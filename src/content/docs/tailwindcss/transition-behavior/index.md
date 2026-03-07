---
title: "transition-behavior - 전환 및 애니메이션 - Tailwind CSS"
description: "hidden에서 block으로 변경되는 요소처럼, 값 집합이 이산적인 속성을 변경할 때 전환을 시작하려면 transition-discrete 유틸리티를 사용하세요:"
---

# transition-behavior - 전환 및 애니메이션 - Tailwind CSS

| 클래스                | 스타일                                 |
| --------------------- | -------------------------------------- |
| `transition-normal`   | `transition-behavior: normal;`         |
| `transition-discrete` | `transition-behavior: allow-discrete;` |

## 예제

- 기본 예제

`hidden`에서 `block`으로 변경되는 요소처럼, 값 집합이 이산적인 속성을 변경할 때 전환을 시작하려면 `transition-discrete` 유틸리티를 사용하세요:

예상 동작을 확인하려면 체크박스와 상호작용해 보세요

transition-normalI 숨기기

transition-discreteI 페이드 아웃

```
    <label class="peer ...">  <input type="checkbox" checked /></label><button class="hidden transition-all not-peer-has-checked:opacity-0 peer-has-checked:block ...">  I hide</button><label class="peer ...">  <input type="checkbox" checked /></label><button class="hidden transition-all transition-discrete not-peer-has-checked:opacity-0 peer-has-checked:block ...">  I fade out</button>
```

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `transition-behavior` 유틸리티 앞에 붙이면 중간 화면 크기 이상에서만 유틸리티가 적용됩니다:

```
    <button class="transition-discrete md:transition-normal ...">  <!-- ... --></button>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
