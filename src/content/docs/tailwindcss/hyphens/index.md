---
title: "hyphens - 타이포그래피 - Tailwind CSS"
description: "줄바꿈 제안 &shy;를 사용하더라도 단어가 하이픈으로 분할되지 않게 하려면 hyphens-none 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/hyphens

# hyphens - 타이포그래피 - Tailwind CSS

| 클래스           | 스타일             |
| ---------------- | ------------------ |
| `hyphens-none`   | `hyphens: none;`   |
| `hyphens-manual` | `hyphens: manual;` |
| `hyphens-auto`   | `hyphens: auto;`   |

## 예제

- 하이픈 분할 방지

줄바꿈 제안 `&shy;`를 사용하더라도 단어가 하이픈으로 분할되지 않게 하려면 `hyphens-none` 유틸리티를 사용하세요:

독일어에서 가장 긴 단어로 Duden 사전에 공식 등재된 Kraftfahrzeug­haftpflichtversicherung는 자동차 책임 보험을 뜻하는 36글자 단어입니다.

```
    <p class="hyphens-none">  ... Kraftfahrzeug&shy;haftpflichtversicherung is a ...</p>
```

- 수동 하이픈 분할

줄바꿈 제안 `&shy;`를 사용한 위치에만 하이픈 분할 지점을 설정하려면 `hyphens-manual` 유틸리티를 사용하세요:

독일어에서 가장 긴 단어로 Duden 사전에 공식 등재된 Kraftfahrzeug­haftpflichtversicherung는 자동차 책임 보험을 뜻하는 36글자 단어입니다.

```
    <p class="hyphens-manual">  ... Kraftfahrzeug&shy;haftpflichtversicherung is a ...</p>
```

이것이 브라우저의 기본 동작입니다.

- 자동 하이픈 분할

언어를 기준으로 브라우저가 하이픈 분할 지점을 자동으로 선택하도록 하려면 `hyphens-auto` 유틸리티를 사용하세요:

독일어에서 가장 긴 단어로 Duden 사전에 공식 등재된 Kraftfahrzeughaftpflichtversicherung는 자동차 책임 보험을 뜻하는 36글자 단어입니다.

```
    <p class="hyphens-auto" lang="de">  ... Kraftfahrzeughaftpflichtversicherung is a ...</p>
```

줄바꿈 제안 `&shy;`는 자동 하이픈 분할 지점보다 우선 적용됩니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `hyphens` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <p class="hyphens-none md:hyphens-auto ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
