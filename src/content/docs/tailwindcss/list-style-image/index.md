---
title: "list-style-image - 타이포그래피 - Tailwind CSS"
description: "list-image-[<value>] 구문을 사용해 목록 항목의 마커 이미지를 제어합니다:"
---

출처 URL: https://tailwindcss.com/docs/list-style-image

# list-style-image - 타이포그래피 - Tailwind CSS

| 클래스                           | 스타일                                      |
| -------------------------------- | ------------------------------------------- |
| `list-image-[<value>]`           | `list-style-image: <value>;`                |
| `list-image-(<custom-property>)` | `list-style-image: var(<custom-property>);` |
| `list-image-none`                | `list-style-image: none;`                   |

## 예제

- 기본 예제

`list-image-[<value>]` 구문을 사용해 목록 항목의 마커 이미지를 제어합니다:

- 다진 포르치니 버섯 5컵
- 올리브 오일 1/2컵
- 셀러리 3lb

```
    <ul class="list-image-[url(/img/checkmark.png)]">  <li>5 cups chopped Porcini mushrooms</li>  <!-- ... --></ul>
```

- CSS 변수 사용

`list-image-(<custom-property>)` 구문을 사용해 CSS 변수로 목록 항목의 마커 이미지를 제어합니다:

```
    <ul class="list-image-(--my-list-image)">  <!-- ... --></ul>
```

이것은 `var()` 함수를 자동으로 추가해 주는 `list-image-[var(<custom-property>)]`의 축약형일 뿐입니다.

- 마커 이미지 제거

`list-image-none` 유틸리티를 사용해 목록 항목에서 기존 마커 이미지를 제거합니다:

```
    <ul class="list-image-none">  <!-- ... --></ul>
```

- 반응형 디자인

`md:` 같은 breakpoint variant를 `list-style-image` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 유틸리티가 적용됩니다:

```
    <ul class="list-image-none md:list-image-[url(/img/checkmark.png)] ...">  <!-- ... --></ul>
```

variants 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
