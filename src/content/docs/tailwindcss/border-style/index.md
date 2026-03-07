---
title: "border-style - 테두리 - Tailwind CSS"
description: "border-solid, border-dotted 같은 유틸리티를 사용해 요소의 테두리 스타일을 제어할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/border-style

# border-style - 테두리 - Tailwind CSS

| 클래스          | 스타일                                            |
| --------------- | ------------------------------------------------- |
| `border-solid`  | `border-style: solid;`                            |
| `border-dashed` | `border-style: dashed;`                           |
| `border-dotted` | `border-style: dotted;`                           |
| `border-double` | `border-style: double;`                           |
| `border-hidden` | `border-style: hidden;`                           |
| `border-none`   | `border-style: none;`                             |
| `divide-solid`  | `& > :not(:last-child) { border-style: solid; }`  |
| `divide-dashed` | `& > :not(:last-child) { border-style: dashed; }` |
| `divide-dotted` | `& > :not(:last-child) { border-style: dotted; }` |
| `divide-double` | `& > :not(:last-child) { border-style: double; }` |
| `divide-hidden` | `& > :not(:last-child) { border-style: hidden; }` |
| `divide-none`   | `& > :not(:last-child) { border-style: none; }`   |

## 예시

- 기본 예시

`border-solid`, `border-dotted` 같은 유틸리티를 사용해 요소의 테두리 스타일을 제어할 수 있습니다:

border-solid

버튼 A

border-dashed

버튼 A

border-dotted

버튼 A

border-double

버튼 A

```
    <div class="border-2 border-solid ..."></div><div class="border-2 border-dashed ..."></div><div class="border-2 border-dotted ..."></div><div class="border-4 border-double ..."></div>
```

- 테두리 제거하기

`border-none` 유틸리티를 사용해 요소에 기존에 적용된 테두리를 제거할 수 있습니다:

변경 사항 저장

```
    <button class="border-none ...">Save Changes</button>
```

이 방식은 보통 더 작은 breakpoint에서 적용된 테두리 스타일을 제거할 때 가장 자주 사용됩니다.

- 구분선 스타일 설정하기

`divide-dashed`, `divide-dotted` 같은 유틸리티를 사용해 자식 요소 사이의 테두리 스타일을 제어할 수 있습니다:

01

02

03

```
    <div class="grid grid-cols-3 divide-x-3 divide-dashed divide-indigo-500">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- 반응형 디자인

`border-style` 유틸리티 앞에 `md:` 같은 breakpoint variant를 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="border-solid md:border-dotted ...">  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
