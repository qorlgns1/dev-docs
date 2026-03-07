---
title: "overscroll-behavior - 레이아웃 - Tailwind CSS"
description: '대상 영역의 스크롤이 부모 요소의 스크롤을 유발하지 않도록 하면서, 이를 지원하는 운영체제에서는 컨테이너 끝을 넘어 스크롤할 때의 "bounce" effe...를 유지하려면 overscroll-contain 유틸리티를 사용하세요.'
---

Source URL: https://tailwindcss.com/docs/overscroll-behavior

# overscroll-behavior - 레이아웃 - Tailwind CSS

| 클래스                 | 스타일                            |
| ---------------------- | --------------------------------- |
| `overscroll-auto`      | `overscroll-behavior: auto;`      |
| `overscroll-contain`   | `overscroll-behavior: contain;`   |
| `overscroll-none`      | `overscroll-behavior: none;`      |
| `overscroll-x-auto`    | `overscroll-behavior-x: auto;`    |
| `overscroll-x-contain` | `overscroll-behavior-x: contain;` |
| `overscroll-x-none`    | `overscroll-behavior-x: none;`    |
| `overscroll-y-auto`    | `overscroll-behavior-y: auto;`    |
| `overscroll-y-contain` | `overscroll-behavior-y: contain;` |
| `overscroll-y-none`    | `overscroll-behavior-y: none;`    |

## 예제

- 부모 오버스크롤 방지

대상 영역에서의 스크롤이 부모 요소의 스크롤을 유발하지 않도록 하려면 `overscroll-contain` 유틸리티를 사용하세요. 또한 이를 지원하는 운영체제에서는 컨테이너 끝을 넘어 스크롤할 때 "bounce" 효과를 유지합니다:

동작을 보려면 스크롤하세요

자, 내가 한마디 해줄게, 웃기는 친구야. "뉴욕 공립 도서관"이라고 적힌 그 작은 도장 알지? 너한테는 별거 아닐지 몰라도, 나한테는 큰 의미가 있어. 정말 엄청나게 말이야.

그래, 원하면 실컷 웃어. 너 같은 부류는 전에도 많이 봤어. 화려하게 눈에 띄고, 관습을 과시하듯 무시하는 타입. 맞아, 네가 무슨 생각하는지 알아. 이 사람이 낡은 도서관 책 때문에 왜 이렇게 호들갑일까 싶겠지? 힌트를 하나 주지, 친구.

어쩌면 너와 나 같은 사람은 도서관 없이도 살 수 있을지 몰라. 어쩌면. 그래, 우리는 세상을 바꾸기엔 너무 나이가 들었지. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼친 아이는 어떨까? The Cat in the Hat이랑 The Five Chinese Brothers에 낙서된 음란한 그림을 발견한다면? 그 아이도 더 나은 걸 누릴 자격이 있지 않겠어?

```
    <div class="overscroll-contain ...">Well, let me tell you something, ...</div>
```

- 오버스크롤 bounce 방지

대상 영역에서의 스크롤이 부모 요소의 스크롤을 유발하지 않도록 하고, 컨테이너 끝을 넘어 스크롤할 때의 "bounce" 효과도 막으려면 `overscroll-none` 유틸리티를 사용하세요:

동작을 보려면 스크롤하세요

자, 내가 한마디 해줄게, 웃기는 친구야. "뉴욕 공립 도서관"이라고 적힌 그 작은 도장 알지? 너한테는 별거 아닐지 몰라도, 나한테는 큰 의미가 있어. 정말 엄청나게 말이야.

그래, 원하면 실컷 웃어. 너 같은 부류는 전에도 많이 봤어. 화려하게 눈에 띄고, 관습을 과시하듯 무시하는 타입. 맞아, 네가 무슨 생각하는지 알아. 이 사람이 낡은 도서관 책 때문에 왜 이렇게 호들갑일까 싶겠지? 힌트를 하나 주지, 친구.

어쩌면 너와 나 같은 사람은 도서관 없이도 살 수 있을지 몰라. 어쩌면. 그래, 우리는 세상을 바꾸기엔 너무 나이가 들었지. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼친 아이는 어떨까? The Cat in the Hat이랑 The Five Chinese Brothers에 낙서된 음란한 그림을 발견한다면? 그 아이도 더 나은 걸 누릴 자격이 있지 않겠어?

```
    <div class="overscroll-none ...">Well, let me tell you something, ...</div>
```

- 기본 오버스크롤 동작 사용

기본 스크롤 영역의 경계에 도달했을 때 사용자가 부모 스크롤 영역을 계속 스크롤할 수 있게 하려면 `overscroll-auto` 유틸리티를 사용하세요:

동작을 보려면 스크롤하세요

자, 내가 한마디 해줄게, 웃기는 친구야. "뉴욕 공립 도서관"이라고 적힌 그 작은 도장 알지? 너한테는 별거 아닐지 몰라도, 나한테는 큰 의미가 있어. 정말 엄청나게 말이야.

그래, 원하면 실컷 웃어. 너 같은 부류는 전에도 많이 봤어. 화려하게 눈에 띄고, 관습을 과시하듯 무시하는 타입. 맞아, 네가 무슨 생각하는지 알아. 이 사람이 낡은 도서관 책 때문에 왜 이렇게 호들갑일까 싶겠지? 힌트를 하나 주지, 친구.

어쩌면 너와 나 같은 사람은 도서관 없이도 살 수 있을지 몰라. 어쩌면. 그래, 우리는 세상을 바꾸기엔 너무 나이가 들었지. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼친 아이는 어떨까? The Cat in the Hat이랑 The Five Chinese Brothers에 낙서된 음란한 그림을 발견한다면? 그 아이도 더 나은 걸 누릴 자격이 있지 않겠어?

```
    <div class="overscroll-auto ...">Well, let me tell you something, ...</div>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `overscroll-behavior` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <div class="overscroll-auto md:overscroll-contain ...">  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
