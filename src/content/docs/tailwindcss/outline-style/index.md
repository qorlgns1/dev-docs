---
title: "outline-style - 테두리 - Tailwind CSS"
description: "`outline-solid` 및 `outline-dashed` 같은 유틸리티를 사용해 요소의 외곽선 스타일을 설정합니다:"
---

원본 URL: https://tailwindcss.com/docs/outline-style

# outline-style - 테두리 - Tailwind CSS

| 클래스           | 스타일                                                 |
| ---------------- | ------------------------------------------------------ |
| `outline-solid`  | `outline-style: solid;`                                |
| `outline-dashed` | `outline-style: dashed;`                               |
| `outline-dotted` | `outline-style: dotted;`                               |
| `outline-double` | `outline-style: double;`                               |
| `outline-none`   | `outline-style: none;`                                 |
| `outline-hidden` | `outline: 2px solid transparent; outline-offset: 2px;` |

## 예제

- 기본 예제

`outline-solid`, `outline-dashed` 같은 유틸리티를 사용해 요소의 외곽선 스타일을 설정합니다:

outline-solid

버튼 A

outline-dashed

버튼 B

outline-dotted

버튼 C

outline-double

버튼 D

```
    <button class="outline-2 outline-offset-2 outline-solid ...">Button A</button><button class="outline-2 outline-offset-2 outline-dashed ...">Button B</button><button class="outline-2 outline-offset-2 outline-dotted ...">Button C</button><button class="outline-3 outline-offset-2 outline-double ...">Button D</button>
```

- 외곽선 숨기기

`outline-hidden` 유틸리티를 사용하면 포커스된 요소의 기본 브라우저 외곽선을 숨기면서도, 강제 색상 모드에서는 외곽선을 유지할 수 있습니다:

동작을 확인하려면 개발자 도구에서 `forced-colors: active`를 에뮬레이션해 보세요.

```
    <input class="focus:border-indigo-600 focus:outline-hidden ..." type="text" />
```

이 유틸리티를 사용할 때는 접근성을 위해 사용자 정의 포커스 스타일을 직접 적용하는 것을 강력히 권장합니다.

- 외곽선 제거

`outline-none` 유틸리티를 사용하면 포커스된 요소의 기본 브라우저 외곽선을 완전히 제거할 수 있습니다:

게시

```
    <div class="focus-within:outline-2 focus-within:outline-indigo-600 ...">  <textarea class="outline-none ..." placeholder="Leave a comment..." />  <button class="..." type="button">Post</button></div>
```

이 유틸리티를 사용할 때는 접근성을 위해 사용자 정의 포커스 스타일을 직접 적용하는 것을 강력히 권장합니다.

- 반응형 디자인

`outline-style` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="outline md:outline-dashed ...">  <!-- ... --></div>
```

변형 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
