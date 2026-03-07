---
title: "float - 레이아웃 - Tailwind CSS"
description: "float-right 유틸리티를 사용해 요소를 컨테이너의 오른쪽으로 띄웁니다:"
---

# float - 레이아웃 - Tailwind CSS

| Class         | Styles                 |
| ------------- | ---------------------- |
| `float-right` | `float: right;`        |
| `float-left`  | `float: left;`         |
| `float-start` | `float: inline-start;` |
| `float-end`   | `float: inline-end;`   |
| `float-none`  | `float: none;`         |

## 예제

- 요소를 오른쪽으로 띄우기

`float-right` 유틸리티를 사용해 요소를 컨테이너의 오른쪽으로 띄웁니다:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

어쩌면 우리 같은 사람들은 도서관 없이도 살 수 있을지 모릅니다. 어쩌면요. 물론 우리는 세상을 바꾸기엔 너무 늙었죠. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼쳤다가 Cat in the Hat과 Five Chinese Brothers에 성적인 낙서를 발견하는 그 아이는요? 그 아이는 더 나은 걸 누릴 자격이 없나요? 보세요. 이게 연체료나 분실 도서 이야기라고 생각한다면 다시 생각하는 게 좋습니다. 이건 아이가 왜곡되지 않은 마음으로 책을 읽을 권리에 대한 이야기입니다! 아니면, Seinfeld, 그런 게 당신 취향인가요? 그런 식으로 즐거움을 찾는 건가요. 당신과 당신의 흥청망청 친구들 말입니다.

```
    <article>  <img class="float-right ..." src="/img/mountains.jpg" />  <p>Maybe we can live without libraries, people like you and me. ...</p></article>
```

- 요소를 왼쪽으로 띄우기

`float-left` 유틸리티를 사용해 요소를 컨테이너의 왼쪽으로 띄웁니다:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

어쩌면 우리 같은 사람들은 도서관 없이도 살 수 있을지 모릅니다. 어쩌면요. 물론 우리는 세상을 바꾸기엔 너무 늙었죠. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼쳤다가 Cat in the Hat과 Five Chinese Brothers에 성적인 낙서를 발견하는 그 아이는요? 그 아이는 더 나은 걸 누릴 자격이 없나요? 보세요. 이게 연체료나 분실 도서 이야기라고 생각한다면 다시 생각하는 게 좋습니다. 이건 아이가 왜곡되지 않은 마음으로 책을 읽을 권리에 대한 이야기입니다! 아니면, Seinfeld, 그런 게 당신 취향인가요? 그런 식으로 즐거움을 찾는 건가요. 당신과 당신의 흥청망청 친구들 말입니다.

```
    <article>  <img class="float-left ..." src="/img/mountains.jpg" />  <p>Maybe we can live without libraries, people like you and me. ...</p></article>
```

- 논리 속성 사용하기

텍스트 방향에 따라 왼쪽 또는 오른쪽에 매핑되도록 [논리 속성](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts)을 사용하는 `float-start` 및 `float-end` 유틸리티를 사용하세요:

왼쪽에서 오른쪽

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

어쩌면 우리 같은 사람들은 도서관 없이도 살 수 있을지 모릅니다. 어쩌면요. 물론 우리는 세상을 바꾸기엔 너무 늙었죠. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼쳤다가 Cat in the Hat과 Five Chinese Brothers에 성적인 낙서를 발견하는 그 아이는요? 그 아이는 더 나은 걸 누릴 자격이 없나요? 보세요. 이게 연체료나 분실 도서 이야기라고 생각한다면 다시 생각하는 게 좋습니다. 이건 아이가 왜곡되지 않은 마음으로 책을 읽을 권리에 대한 이야기입니다! 아니면, Seinfeld, 그런 게 당신 취향인가요? 그런 식으로 즐거움을 찾는 건가요. 당신과 당신의 흥청망청 친구들 말입니다.

오른쪽에서 왼쪽

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

ربما يمكننا العيش بدون مكتبات، أشخاص مثلي ومثلك. ربما. بالتأكيد، نحن أكبر من أن نغير العالم، ولكن ماذا عن ذلك الطفل الذي يجلس ويفتح كتابًا الآن في أحد فروع المكتبة المحلية ويجد رسومات للتبول والبول على القطة في القبعة والإخوة الصينيون الخمسة؟ ألا يستحق الأفضل؟ ينظر. إذا كنت تعتقد أن الأمر يتعلق بالغرامات المتأخرة والكتب المفقودة، فمن الأفضل أن تفكر مرة أخرى. يتعلق الأمر بحق ذلك الطفل في قراءة كتاب دون أن يتشوه عقله! أو: ربما يثيرك هذا يا سينفيلد؛ ربما هذه هي الطريقة التي تحصل بها على ركلاتك. أنت ورفاقك الطيبين.

```
    <article>  <img class="float-start ..." src="/img/mountains.jpg" />  <p>Maybe we can live without libraries, people like you and me. ...</p></article><article dir="rtl">  <img class="float-start ..." src="/img/mountains.jpg" />  <p>... ربما يمكننا العيش بدون مكتبات، أشخاص مثلي ومثلك. ربما. بالتأكيد</p></article>
```

- float 비활성화하기

`float-none` 유틸리티를 사용해 요소에 적용된 모든 float를 초기화합니다:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

어쩌면 우리 같은 사람들은 도서관 없이도 살 수 있을지 모릅니다. 어쩌면요. 물론 우리는 세상을 바꾸기엔 너무 늙었죠. 하지만 지금 이 순간 동네 도서관 분관에 앉아 책을 펼쳤다가 Cat in the Hat과 Five Chinese Brothers에 성적인 낙서를 발견하는 그 아이는요? 그 아이는 더 나은 걸 누릴 자격이 없나요? 보세요. 이게 연체료나 분실 도서 이야기라고 생각한다면 다시 생각하는 게 좋습니다. 이건 아이가 왜곡되지 않은 마음으로 책을 읽을 권리에 대한 이야기입니다! 아니면, Seinfeld, 그런 게 당신 취향인가요? 그런 식으로 즐거움을 찾는 건가요. 당신과 당신의 흥청망청 친구들 말입니다.

```
    <article>  <img class="float-none ..." src="/img/mountains.jpg" />  <p>Maybe we can live without libraries, people like you and me. ...</p></article>
```

- 반응형 디자인

`float` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 유틸리티가 적용됩니다:

```
    <img class="float-right md:float-left" src="/img/mountains.jpg" />
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
