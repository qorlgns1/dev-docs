---
title: "resize - 인터랙티비티 - Tailwind CSS"
description: "요소를 가로 및 세로로 크기 조절 가능하게 만들려면 resize를 사용하세요:"
---

Source URL: https://tailwindcss.com/docs/resize

# resize - 인터랙티비티 - Tailwind CSS

| 클래스        | 스타일                |
| ------------- | --------------------- |
| `resize-none` | `resize: none;`       |
| `resize`      | `resize: both;`       |
| `resize-y`    | `resize: vertical;`   |
| `resize-x`    | `resize: horizontal;` |

## 예제

- 모든 방향으로 크기 조절

요소를 가로와 세로 모두 크기 조절 가능하게 만들려면 `resize`를 사용하세요:

예상 동작을 확인하려면 데모에서 textarea 핸들을 드래그하세요

```
    <textarea class="resize rounded-md ..."></textarea>
```

- 세로 크기 조절

요소를 세로로 크기 조절 가능하게 만들려면 `resize-y`를 사용하세요:

예상 동작을 확인하려면 데모에서 textarea 핸들을 드래그하세요

```
    <textarea class="resize-y rounded-md ..."></textarea>
```

- 가로 크기 조절

요소를 가로로 크기 조절 가능하게 만들려면 `resize-x`를 사용하세요:

예상 동작을 확인하려면 데모에서 textarea 핸들을 드래그하세요

```
    <textarea class="resize-x rounded-md ..."></textarea>
```

- 크기 조절 방지

요소의 크기 조절을 막으려면 `resize-none`을 사용하세요:

textarea 핸들이 사라진 것을 확인하세요

```
    <textarea class="resize-none rounded-md"></textarea>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `resize` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="resize-none md:resize ...">  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
