---
title: "list-style-position - 타이포그래피 - Tailwind CSS"
description: "list-inside 및 list-outside 같은 유틸리티를 사용해 목록에서 마커 위치와 텍스트 들여쓰기를 제어하세요:"
---

출처 URL: https://tailwindcss.com/docs/list-style-position

# list-style-position - 타이포그래피 - Tailwind CSS

| 클래스         | 스타일                          |
| -------------- | ------------------------------- |
| `list-inside`  | `list-style-position: inside;`  |
| `list-outside` | `list-style-position: outside;` |

## 예제

- 기본 예제

`list-inside` 및 `list-outside` 같은 유틸리티를 사용해 목록에서 마커 위치와 텍스트 들여쓰기를 제어하세요:

list-inside

- 다진 포르치니 버섯 5컵
- 올리브 오일 1/2컵
- 셀러리 3lb

list-outside

- 다진 포르치니 버섯 5컵
- 올리브 오일 1/2컵
- 셀러리 3lb

```
    <ul class="list-inside">  <li>5 cups chopped Porcini mushrooms</li>  <!-- ... --></ul><ul class="list-outside">  <li>5 cups chopped Porcini mushrooms</li>  <!-- ... --></ul>
```

- 반응형 디자인

`list-style-position` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <ul class="list-outside md:list-inside ...">  <!-- ... --></ul>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
