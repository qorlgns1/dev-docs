---
title: "font-feature-settings - 타이포그래피 - Tailwind CSS"
description: "font-features-[<value>] 유틸리티를 사용해 이를 지원하는 글꼴에서 OpenType 기능을 활성화할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/font-feature-settings

# font-feature-settings - 타이포그래피 - Tailwind CSS

| 클래스                              | 스타일                                           |
| ----------------------------------- | ------------------------------------------------ |
| `font-features-[<value>]`           | `font-feature-settings: <value>;`                |
| `font-features-(<custom-property>)` | `font-feature-settings: var(<custom-property>);` |

## 예제

- 기본 예제

`font-features-[<value>]` 유틸리티를 사용해 이를 지원하는 글꼴에서 OpenType 기능을 활성화할 수 있습니다:

```
    <p class="font-features-['smcp'] ...">This text uses small caps.</p>
```

- 여러 기능 활성화

쉼표로 구분하면 여러 OpenType 기능을 활성화할 수 있습니다:

```
    <p class="font-features-['smcp','onum'] ...">This text uses small caps and oldstyle numbers.</p>
```

- CSS 변수 사용

`font-features-(<custom-property>)` 문법을 사용해 CSS 변수에서 글꼴 기능 설정을 적용할 수 있습니다:

```
    <p class="font-features-(--my-features) ...">  <!-- ... --></p>
```

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `font-feature-settings` 유틸리티 앞에 붙이면 중간 크기 화면 이상에서만 유틸리티가 적용됩니다:

```
    <p class="font-features-['tnum'] md:font-features-['smcp'] ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용법은 [variant 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
