---
title: "mask-repeat - 효과 - Tailwind CSS"
description: "mask-repeat 유틸리티를 사용해 마스크 이미지를 세로와 가로로 모두 반복합니다:"
---

출처 URL: https://tailwindcss.com/docs/mask-repeat

# mask-repeat - 효과 - Tailwind CSS

| 클래스              | 스타일                    |
| ------------------- | ------------------------- |
| `mask-repeat`       | `mask-repeat: repeat;`    |
| `mask-no-repeat`    | `mask-repeat: no-repeat;` |
| `mask-repeat-x`     | `mask-repeat: repeat-x;`  |
| `mask-repeat-y`     | `mask-repeat: repeat-y;`  |
| `mask-repeat-space` | `mask-repeat: space;`     |
| `mask-repeat-round` | `mask-repeat: round;`     |

## 예제

- 기본 예제

`mask-repeat` 유틸리티를 사용해 마스크 이미지를 세로와 가로로 모두 반복합니다:

```
    <div class="mask-repeat mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 가로로 반복

`mask-repeat-x` 유틸리티를 사용해 마스크 이미지를 가로 방향으로만 반복합니다:

```
    <div class="mask-repeat-x mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)]..."></div>
```

- 세로로 반복

`mask-repeat-y` 유틸리티를 사용해 마스크 이미지를 세로 방향으로만 반복합니다:

```
    <div class="mask-repeat-y mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)]..."></div>
```

- 잘림 방지

`mask-repeat-space` 유틸리티를 사용해 마스크 이미지를 잘리지 않게 반복합니다:

```
    <div class="mask-repeat-space mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 잘림과 간격 방지

`mask-repeat-round` 유틸리티를 사용해 마스크 이미지를 잘리지 않게 반복하며, 필요하면 간격이 생기지 않도록 늘립니다:

```
    <div class="mask-repeat-round mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 반복 비활성화

`mask-no-repeat` 유틸리티를 사용해 마스크 이미지가 반복되지 않도록 합니다:

```
    <div class="mask-no-repeat mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

- 반응형 디자인

`mask-repeat` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙여 중간 크기 이상의 화면에서만 유틸리티가 적용되도록 할 수 있습니다:

```
    <div class="mask-repeat md:mask-repeat-x ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
