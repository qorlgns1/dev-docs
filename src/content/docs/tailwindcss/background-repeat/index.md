---
title: "background-repeat - 배경 - Tailwind CSS"
description: "배경 이미지를 세로와 가로 모두 반복하려면 bg-repeat 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/background-repeat

# background-repeat - 배경 - Tailwind CSS

| Class             | Styles                          |
| ----------------- | ------------------------------- |
| `bg-repeat`       | `background-repeat: repeat;`    |
| `bg-repeat-x`     | `background-repeat: repeat-x;`  |
| `bg-repeat-y`     | `background-repeat: repeat-y;`  |
| `bg-repeat-space` | `background-repeat: space;`     |
| `bg-repeat-round` | `background-repeat: round;`     |
| `bg-no-repeat`    | `background-repeat: no-repeat;` |

## 예제

- 기본 예제

배경 이미지를 세로와 가로 모두 반복하려면 `bg-repeat` 유틸리티를 사용하세요:

```
    <div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat ..."></div>
```

- 가로로 반복

배경 이미지를 가로로만 반복하려면 `bg-repeat-x` 유틸리티를 사용하세요:

```
    <div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-x ..."></div>
```

- 세로로 반복

배경 이미지를 세로로만 반복하려면 `bg-repeat-y` 유틸리티를 사용하세요:

```
    <div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-y ..."></div>
```

- 잘림 방지

배경 이미지가 잘리지 않도록 반복하려면 `bg-repeat-space` 유틸리티를 사용하세요:

```
    <div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-space ..."></div>
```

- 잘림 및 간격 방지

배경 이미지가 잘리지 않게 반복하고, 간격이 생기지 않도록 필요 시 늘리려면 `bg-repeat-round` 유틸리티를 사용하세요:

```
    <div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-round ..."></div>
```

- 반복 비활성화

배경 이미지가 반복되지 않도록 하려면 `bg-no-repeat` 유틸리티를 사용하세요:

```
    <div class="bg-[url(/img/clouds.svg)] bg-center bg-no-repeat ..."></div>
```

- 반응형 디자인

`background-repeat` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 크기 이상의 화면에서만 유틸리티가 적용됩니다:

```
    <div class="bg-repeat md:bg-repeat-x ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
