---
title: "list-style-type - 타이포그래피 - Tailwind CSS"
description: "list-disc, list-decimal 같은 유틸리티를 사용해 목록 마커의 스타일을 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/list-style-type

# list-style-type - 타이포그래피 - Tailwind CSS

| 클래스                     | 스타일                                     |
| -------------------------- | ------------------------------------------ |
| `list-disc`                | `list-style-type: disc;`                   |
| `list-decimal`             | `list-style-type: decimal;`                |
| `list-none`                | `list-style-type: none;`                   |
| `list-(<custom-property>)` | `list-style-type: var(<custom-property>);` |
| `list-[<value>]`           | `list-style-type: <value>;`                |

## 예제

- 기본 예제

`list-disc`, `list-decimal` 같은 유틸리티를 사용해 목록 마커의 스타일을 제어하세요:

list-disc

- 이제부터 내 인생이 어떻게 완전히 뒤집혔는지에 대한 이야기야
- 잠깐만 시간 내서 바로 거기 앉아 봐
- Bel-Air라는 마을의 왕자가 된 사연을 들려줄게

list-decimal

- 이제부터 내 인생이 어떻게 완전히 뒤집혔는지에 대한 이야기야
- 잠깐만 시간 내서 바로 거기 앉아 봐
- Bel-Air라는 마을의 왕자가 된 사연을 들려줄게

list-none

- 이제부터 내 인생이 어떻게 완전히 뒤집혔는지에 대한 이야기야
- 잠깐만 시간 내서 바로 거기 앉아 봐
- Bel-Air라는 마을의 왕자가 된 사연을 들려줄게

```
    <ul class="list-disc">  <li>Now this is a story all about how, my life got flipped-turned upside down</li>  <!-- ... --></ul><ol class="list-decimal">  <li>Now this is a story all about how, my life got flipped-turned upside down</li>  <!-- ... --></ol><ul class="list-none">  <li>Now this is a story all about how, my life got flipped-turned upside down</li>  <!-- ... --></ul>
```

- 사용자 지정 값 사용

`list-[<value>]` 문법을 사용하면 완전히 사용자 지정한 값으로 마커를 설정할 수 있습니다:

```
    <ol class="list-[upper-roman] ...">  <!-- ... --></ol>
```

CSS 변수의 경우 `list-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <ol class="list-(--my-marker) ...">  <!-- ... --></ol>
```

이는 `list-[var(<custom-property>)]`의 축약형으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `list-style-type` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <ul class="list-none md:list-disc ...">  <!-- ... --></ul>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
