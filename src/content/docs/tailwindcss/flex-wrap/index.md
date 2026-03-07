---
title: "flex-wrap - 플렉스박스 & 그리드 - Tailwind CSS"
description: "필요한 경우 유연하지 않은 항목이 컨테이너를 넘치도록 만들면서, flex 항목이 줄바꿈되지 않게 하려면 flex-nowrap를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/flex-wrap

# flex-wrap - 플렉스박스 & 그리드 - Tailwind CSS

| Class               | 스타일                     |
| ------------------- | -------------------------- |
| `flex-nowrap`       | `flex-wrap: nowrap;`       |
| `flex-wrap`         | `flex-wrap: wrap;`         |
| `flex-wrap-reverse` | `flex-wrap: wrap-reverse;` |

## 예제

- 줄바꿈하지 않기

필요한 경우 유연하지 않은 항목이 컨테이너를 넘치도록 만들면서, flex 항목이 줄바꿈되지 않게 하려면 `flex-nowrap`를 사용하세요:

01

02

03

```
    <div class="flex flex-nowrap">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 일반 줄바꿈

flex 항목이 줄바꿈되도록 하려면 `flex-wrap`을 사용하세요:

01

02

03

```
    <div class="flex flex-wrap">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 역방향 줄바꿈

flex 항목을 반대 방향으로 줄바꿈하려면 `flex-wrap-reverse`를 사용하세요:

01

02

03

```
    <div class="flex flex-wrap-reverse">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 반응형 디자인

`flex-wrap` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="flex flex-wrap md:flex-wrap-reverse ...">  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
