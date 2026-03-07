---
title: "appearance - 인터랙티비티 - Tailwind CSS"
description: "요소에 적용된 브라우저 고유 스타일을 초기화하려면 appearance-none을 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/appearance

# appearance - 인터랙티비티 - Tailwind CSS

| Class             | 스타일              |
| ----------------- | ------------------- |
| `appearance-none` | `appearance: none;` |
| `appearance-auto` | `appearance: auto;` |

## 예시

- 기본 appearance 제거하기

요소에 적용된 브라우저 고유 스타일을 초기화하려면 `appearance-none`을 사용하세요:

예아니요아마도

기본 브라우저 스타일 적용됨

예아니요아마도

기본 브라우저 스타일 제거됨

```
    <select>  <option>Yes</option>  <option>No</option>  <option>Maybe</option></select><div class="grid">  <select class="col-start-1 row-start-1 appearance-none bg-gray-50 dark:bg-gray-800 ...">    <option>Yes</option>    <option>No</option>    <option>Maybe</option>  </select>  <svg class="pointer-events-none col-start-1 row-start-1 ...">    <!-- ... -->  </svg></div>
```

이 유틸리티는 커스텀 폼 컴포넌트를 만들 때 자주 사용됩니다.

- 기본 appearance 복원하기

요소에 기본 브라우저 고유 스타일을 복원하려면 `appearance-auto`를 사용하세요:

차이를 확인하려면 개발자 도구에서 `forced-colors: active`를 에뮬레이션해 보세요

기본 appearance로 대체됨

커스텀 appearance 유지됨

```
    <label>  <div>    <input type="checkbox" class="appearance-none forced-colors:appearance-auto ..." />    <svg class="invisible peer-checked:visible forced-colors:hidden ...">      <!-- ... -->    </svg>  </div>  Falls back to default appearance</label><label>  <div>    <input type="checkbox" class="appearance-none ..." />    <svg class="invisible peer-checked:visible ...">      <!-- ... -->    </svg>  </div>  Keeps custom appearance</label>
```

이는 특정 접근성 모드에서 표준 브라우저 컨트롤로 되돌릴 때 유용합니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `appearance` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <select class="appearance-auto md:appearance-none ...">  <!-- ... --></select>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
