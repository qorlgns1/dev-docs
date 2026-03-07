---
title: "will-change - 인터랙티비티 - Tailwind CSS"
description: "will-change-scroll, will-change-contents, will-change-transform 유틸리티를 사용하면, 가까운 시점에 변경될 것으로 예상되는 요소에 대해 브라우저가 실제 애니메이션이 시작되기 전에 필요한 준비를 하도록 지시하여 최적화할 ..."
---

출처 URL: https://tailwindcss.com/docs/will-change

# will-change - 인터랙티비티 - Tailwind CSS

| Class                           | Styles                                 |
| ------------------------------- | -------------------------------------- |
| `will-change-auto`              | `will-change: auto;`                   |
| `will-change-scroll`            | `will-change: scroll-position;`        |
| `will-change-contents`          | `will-change: contents;`               |
| `will-change-transform`         | `will-change: transform;`              |
| `will-change-<custom-property>` | `will-change: var(<custom-property>);` |
| `will-change-[<value>]`         | `will-change: <value>;`                |

## 예제

- will change로 최적화하기

`will-change-scroll`, `will-change-contents`, `will-change-transform` 유틸리티를 사용하면, 가까운 시점에 변경될 것으로 예상되는 요소에 대해 브라우저가 실제 애니메이션이 시작되기 전에 필요한 준비를 하도록 지시하여 최적화할 수 있습니다:

```
    <div class="overflow-auto will-change-scroll">  <!-- ... --></div>
```

이 유틸리티들은 요소가 변경되기 직전에 적용하고, 완료된 직후 `will-change-auto`를 사용해 제거하는 것을 권장합니다.

`will-change` 속성은 **이미 알려진 성능 문제**를 다룰 때 최후의 수단으로 사용하는 것이 목적입니다. 이 유틸리티를 과도하게 사용하거나, 단순히 성능 문제를 예상해서 사용하는 것은 피하세요. 오히려 페이지 성능이 더 저하될 수 있습니다.

- 사용자 정의 값 사용하기

`will-change-[<value>]` 구문을 사용하면 완전히 사용자 정의한 값을 기반으로 `will-change` 속성을 설정할 수 있습니다:

```
    <div class="will-change-[top,left] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `will-change-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="will-change-(--my-properties) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `will-change-[var(<custom-property>)]`의 단축 표기입니다.
