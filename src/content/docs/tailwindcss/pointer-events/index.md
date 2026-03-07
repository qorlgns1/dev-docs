---
title: "pointer-events - 인터랙티비티 - Tailwind CSS"
description: "`pointer-events-none` 유틸리티를 사용해 요소가 `:hover` 및 클릭 이벤트와 같은 포인터 이벤트를 무시하도록 설정할 수 있습니다:"
---

Source URL: https://tailwindcss.com/docs/pointer-events

# pointer-events - 인터랙티비티 - Tailwind CSS

| Class                 | Styles                  |
| --------------------- | ----------------------- |
| `pointer-events-auto` | `pointer-events: auto;` |
| `pointer-events-none` | `pointer-events: none;` |

## 예제

- 포인터 이벤트 무시하기

`pointer-events-none` 유틸리티를 사용하면 요소가 `:hover`, `click` 이벤트와 같은 포인터 이벤트를 무시하도록 설정할 수 있습니다:

예상 동작을 확인하려면 검색 아이콘을 클릭하세요

pointer-events-auto

pointer-events-none

```
    <div class="relative ...">  <div class="pointer-events-auto absolute ...">    <svg class="absolute h-5 w-5 text-gray-400">      <!-- ... -->    </svg>  </div>  <input type="text" placeholder="Search" class="..." /></div><div class="relative ...">  <div class="pointer-events-none absolute ...">    <svg class="absolute h-5 w-5 text-gray-400">      <!-- ... -->    </svg>  </div>  <input type="text" placeholder="Search" class="..." /></div>
```

포인터 이벤트는 자식 요소에서는 계속 트리거되며, 대상 요소 "아래"에 있는 요소로 통과됩니다.

- 포인터 이벤트 복원하기

`pointer-events-auto` 유틸리티를 사용하면 포인터 이벤트의 기본 브라우저 동작으로 되돌릴 수 있습니다:

```
    <div class="pointer-events-none md:pointer-events-auto ...">  <!-- ... --></div>
```
