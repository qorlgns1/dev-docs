---
title: "field-sizing - 인터랙티비티 - Tailwind CSS"
description: "field-sizing-content 유틸리티를 사용하면 폼 컨트롤이 콘텐츠에 따라 크기를 조정할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/field-sizing

# field-sizing - 인터랙티비티 - Tailwind CSS

| 클래스                 | 스타일                   |
| ---------------------- | ------------------------ |
| `field-sizing-fixed`   | `field-sizing: fixed;`   |
| `field-sizing-content` | `field-sizing: content;` |

## 예시

- 콘텐츠 기반 크기 조정

`field-sizing-content` 유틸리티를 사용하면 폼 컨트롤이 콘텐츠에 따라 크기를 조정할 수 있습니다:

아래 입력창에 입력해 크기가 변하는지 확인해 보세요

라텍스 영업사원, Vanderlay Industries

```
    <textarea class="field-sizing-content ..." rows="2">  Latex Salesman, Vanderlay Industries</textarea>
```

- 고정 크기 사용

`field-sizing-fixed` 유틸리티를 사용하면 폼 컨트롤이 고정된 크기를 사용합니다:

아래 입력창에 입력해도 크기가 동일하게 유지되는지 확인해 보세요

라텍스 영업사원, Vanderlay Industries

```
    <textarea class="field-sizing-fixed w-80 ..." rows="2">  Latex Salesman, Vanderlay Industries</textarea>
```

- 반응형 디자인

`field-sizing` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 크기 화면 이상에서만 유틸리티가 적용됩니다:

```
    <input class="field-sizing-content md:field-sizing-fixed ..." />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
