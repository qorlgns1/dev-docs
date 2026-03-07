---
title: "user-select - 상호작용 - Tailwind CSS"
description: "select-none 유틸리티를 사용하면 요소와 그 자식 요소에서 텍스트를 선택하지 못하게 할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/user-select

# user-select - 상호작용 - Tailwind CSS

| 클래스        | 스타일               |
| ------------- | -------------------- |
| `select-none` | `user-select: none;` |
| `select-text` | `user-select: text;` |
| `select-all`  | `user-select: all;`  |
| `select-auto` | `user-select: auto;` |

## 예제

- 텍스트 선택 비활성화

`select-none` 유틸리티를 사용하면 요소와 그 자식 요소에서 텍스트를 선택하지 못하게 할 수 있습니다:

예상되는 동작을 확인하려면 텍스트를 선택해 보세요.

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <div class="select-none ...">The quick brown fox jumps over the lazy dog.</div>
```

- 텍스트 선택 허용

`select-text` 유틸리티를 사용하면 요소와 그 자식 요소에서 텍스트를 선택할 수 있습니다:

예상되는 동작을 확인하려면 텍스트를 선택해 보세요.

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <div class="select-text ...">The quick brown fox jumps over the lazy dog.</div>
```

- 한 번의 클릭으로 모든 텍스트 선택

`select-all` 유틸리티를 사용하면 사용자가 클릭할 때 요소 안의 모든 텍스트가 자동으로 선택됩니다:

예상되는 동작을 확인하려면 텍스트를 클릭해 보세요.

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <div class="select-all ...">The quick brown fox jumps over the lazy dog.</div>
```

- 자동 선택 동작 사용

`select-auto` 유틸리티를 사용하면 텍스트 선택에 브라우저 기본 동작을 사용할 수 있습니다:

예상되는 동작을 확인하려면 텍스트를 선택해 보세요.

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <div class="select-auto ...">The quick brown fox jumps over the lazy dog.</div>
```

- 반응형 디자인

`user-select` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 유틸리티가 적용됩니다:

```
    <div class="select-none md:select-all ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
