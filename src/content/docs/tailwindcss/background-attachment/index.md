---
title: "background-attachment - 배경 - Tailwind CSS"
description: "bg-fixed 유틸리티를 사용하면 배경 이미지를 뷰포트 기준으로 고정할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/background-attachment

# background-attachment - 배경 - Tailwind CSS

| Class       | Styles                           |
| ----------- | -------------------------------- |
| `bg-fixed`  | `background-attachment: fixed;`  |
| `bg-local`  | `background-attachment: local;`  |
| `bg-scroll` | `background-attachment: scroll;` |

## 예제

- 배경 이미지 고정하기

`bg-fixed` 유틸리티를 사용하면 배경 이미지를 뷰포트 기준으로 고정할 수 있습니다:

콘텐츠를 스크롤해 배경 이미지가 제자리에 고정되어 있는지 확인하세요

정상까지의 나의 여행

2021년 11월 16일 · 4분 읽기

어쩌면 우리 같은 사람들, 너와 나, 도서관 없이도 살 수 있을지 몰라. 어쩌면. 그래, 우리가 세상을 바꾸기엔 너무 늙었을지도 모르지. 하지만 지금 당장 동네 도서관 한쪽에 앉아 책을 펼친 아이는 어떨까? Cat in the Hat이랑 Five Chinese Brothers 책에서 남이 낙서해 놓은 외설적인 그림을 보게 된다면? 그 아이는 더 나은 환경을 누릴 자격이 없을까?

잘 들어. 이게 연체료나 분실 도서 얘기라고 생각한다면, 다시 생각하는 게 좋겠어. 이건 그 아이가 왜곡되지 않은 상태로 책을 읽을 권리에 대한 이야기야! 아니면 뭐, 그게 네 취향일 수도 있지, Seinfeld. 그런 식으로 재미를 느끼는 걸 수도. 너랑 네 흥청망청 친구들 말이야.

```
    <div class="bg-[url(/img/mountains.jpg)] bg-fixed ...">  <!-- ... --></div>
```

- 컨테이너와 함께 스크롤하기

`bg-local` 유틸리티를 사용하면 배경 이미지가 컨테이너와 뷰포트에 맞춰 함께 스크롤됩니다:

콘텐츠를 스크롤해 배경 이미지가 컨테이너와 함께 스크롤되는지 확인하세요

우편물은 절대 멈추지 않아. 계속 오고 또 오고 또 와, 잠잠해질 틈이 없어. 정말 끈질기지. 매일매일 더 쌓이고 또 쌓여. 어떻게든 처리해야 하는데, 처리하면 할수록 또 들어와. 그러다 바코드 리더기까지 고장 나고, 하필 오늘은 Publisher's Clearing House 오는 날이지.

— Newman

```
    <div class="bg-[url(/img/mountains.jpg)] bg-local ...">  <!-- ... --></div>
```

- 뷰포트와 함께 스크롤하기

`bg-scroll` 유틸리티를 사용하면 배경 이미지는 뷰포트와 함께 스크롤되지만, 컨테이너와 함께 스크롤되지는 않습니다:

콘텐츠를 스크롤해 배경 이미지가 컨테이너에 고정되어 있는지 확인하세요

우편물은 절대 멈추지 않아. 계속 오고 또 오고 또 와, 잠잠해질 틈이 없어. 정말 끈질기지. 매일매일 더 쌓이고 또 쌓여. 어떻게든 처리해야 하는데, 처리하면 할수록 또 들어와. 그러다 바코드 리더기까지 고장 나고, 하필 오늘은 Publisher's Clearing House 오는 날이지.

— Newman

```
    <div class="bg-[url(/img/mountains.jpg)] bg-scroll ...">  <!-- ... --></div>
```

- 반응형 디자인

`background-attachment` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="bg-local md:bg-fixed ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 자세히 확인하세요.
