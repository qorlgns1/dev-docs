---
title: "clear - 레이아웃 - Tailwind CSS"
description: "앞서 있는 왼쪽 float 요소들 아래에 요소를 배치하려면 clear-left 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/clear

# clear - 레이아웃 - Tailwind CSS

| 클래스        | 스타일                 |
| ------------- | ---------------------- |
| `clear-left`  | `clear: left;`         |
| `clear-right` | `clear: right;`        |
| `clear-both`  | `clear: both;`         |
| `clear-start` | `clear: inline-start;` |
| `clear-end`   | `clear: inline-end;`   |
| `clear-none`  | `clear: none;`         |

## 예제

- 왼쪽 지우기

앞서 있는 왼쪽 float 요소들 아래에 요소를 배치하려면 `clear-left` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&h=1000&q=90)

어쩌면 우리 같은 사람들은 도서관 없이도 살 수 있을지 몰라요. 어쩌면요. 물론 우리는 세상을 바꾸기엔 너무 늙었죠. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼친 아이가 Cat in the Hat와 Five Chinese Brothers에 낙서된 음란한 그림을 보게 된다면요? 그 아이는 더 나은 것을 누릴 자격이 없나요? 보세요. 이게 연체료나 분실 도서 이야기라고 생각한다면, 다시 생각해 보는 게 좋겠어요. 이건 그 아이가 왜곡되지 않은 정신으로 책을 읽을 권리에 대한 이야기예요! 아니면, Seinfeld, 그런 게 당신을 흥분시키나요? 그런 식으로 재미를 느끼는 건가요? 당신과 당신의 흥청망청한 친구들 말이에요.

```
    <article>  <img class="float-left ..." src="/img/snow-mountains.jpg" />  <img class="float-right ..." src="/img/green-mountains.jpg" />  <p class="clear-left ...">Maybe we can live without libraries...</p></article>
```

- 오른쪽 지우기

앞서 있는 오른쪽 float 요소들 아래에 요소를 배치하려면 `clear-right` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&h=1000&q=90)![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=formathttps://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&h=1000&q=90)

어쩌면 우리 같은 사람들은 도서관 없이도 살 수 있을지 몰라요. 어쩌면요. 물론 우리는 세상을 바꾸기엔 너무 늙었죠. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼친 아이가 Cat in the Hat와 Five Chinese Brothers에 낙서된 음란한 그림을 보게 된다면요? 그 아이는 더 나은 것을 누릴 자격이 없나요? 보세요. 이게 연체료나 분실 도서 이야기라고 생각한다면, 다시 생각해 보는 게 좋겠어요. 이건 그 아이가 왜곡되지 않은 정신으로 책을 읽을 권리에 대한 이야기예요! 아니면, Seinfeld, 그런 게 당신을 흥분시키나요? 그런 식으로 재미를 느끼는 건가요? 당신과 당신의 흥청망청한 친구들 말이에요.

```
    <article>  <img class="float-left ..." src="/img/green-mountains.jpg" />  <img class="float-right ..." src="/img/snow-mountains.jpg" />  <p class="clear-right ...">Maybe we can live without libraries...</p></article>
```

- 모두 지우기

앞서 있는 모든 float 요소들 아래에 요소를 배치하려면 `clear-both` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=formathttps://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&h=1000&q=90)![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&h=1000&q=90)

어쩌면 우리 같은 사람들은 도서관 없이도 살 수 있을지 몰라요. 어쩌면요. 물론 우리는 세상을 바꾸기엔 너무 늙었죠. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼친 아이가 Cat in the Hat와 Five Chinese Brothers에 낙서된 음란한 그림을 보게 된다면요? 그 아이는 더 나은 것을 누릴 자격이 없나요? 보세요. 이게 연체료나 분실 도서 이야기라고 생각한다면, 다시 생각해 보는 게 좋겠어요. 이건 그 아이가 왜곡되지 않은 정신으로 책을 읽을 권리에 대한 이야기예요! 아니면, Seinfeld, 그런 게 당신을 흥분시키나요? 그런 식으로 재미를 느끼는 건가요? 당신과 당신의 흥청망청한 친구들 말이에요.

```
    <article>  <img class="float-left ..." src="/img/snow-mountains.jpg" />  <img class="float-right ..." src="/img/green-mountains.jpg" />  <p class="clear-both ...">Maybe we can live without libraries...</p></article>
```

- 논리 속성 사용하기

텍스트 방향에 따라 왼쪽 또는 오른쪽으로 매핑되는 [논리 속성](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts)을 사용하는 `clear-start` 및 `clear-end` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&h=1000&q=90)

ربما يمكننا العيش بدون مكتبات، أشخاص مثلي ومثلك. ربما. بالتأكيد، نحن أكبر من أن نغير العالم، ولكن ماذا عن ذلك الطفل الذي يجلس ويفتح كتابًا الآن في أحد فروع المكتبة المحلية ويجد رسومات للتبول والبول على القطة في القبعة والإخوة الصينيون الخمسة؟ ألا يستحق الأفضل؟ ينظر. إذا كنت تعتقد أن الأمر يتعلق بالغرامات المتأخرة والكتب المفقودة، فمن الأفضل أن تفكر مرة أخرى. يتعلق الأمر بحق ذلك الطفل في قراءة كتاب دون أن يتشوه عقله! أو: ربما يثيرك هذا يا سينفيلد؛ ربما هذه هي الطريقة التي تحصل بها على ركلاتك. أنت ورفاقك الطيبين.

```
    <article dir="rtl">  <img class="float-left ..." src="/img/green-mountains.jpg" />  <img class="float-right ..." src="/img/green-mountains.jpg" />  <p class="clear-end ...">...ربما يمكننا العيش بدون مكتبات،</p></article>
```

- clear 비활성화

요소에 적용된 clear를 초기화하려면 `clear-none` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&h=1000&q=90)![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=formathttps://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&h=1000&q=90)

어쩌면 우리 같은 사람들은 도서관 없이도 살 수 있을지 몰라요. 어쩌면요. 물론 우리는 세상을 바꾸기엔 너무 늙었죠. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼친 아이가 Cat in the Hat와 Five Chinese Brothers에 낙서된 음란한 그림을 보게 된다면요? 그 아이는 더 나은 것을 누릴 자격이 없나요? 보세요. 이게 연체료나 분실 도서 이야기라고 생각한다면, 다시 생각해 보는 게 좋겠어요. 이건 그 아이가 왜곡되지 않은 정신으로 책을 읽을 권리에 대한 이야기예요! 아니면, Seinfeld, 그런 게 당신을 흥분시키나요? 그런 식으로 재미를 느끼는 건가요? 당신과 당신의 흥청망청한 친구들 말이에요.

```
    <article>  <img class="float-left ..." src="/img/green-mountains.jpg" />  <img class="float-right ..." src="/img/snow-mountains.jpg" />  <p class="clear-none ...">Maybe we can live without libraries...</p></article>
```

- 반응형 디자인

`md:` 같은 브레이크포인트 변형 접두사를 `clear` 유틸리티 앞에 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <p class="clear-left md:clear-none ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
