---
title: "display - 레이아웃 - Tailwind CSS"
description: "텍스트와 요소의 흐름을 제어하려면 inline, inline-block, block 유틸리티를 사용하세요:"
---

# display - 레이아웃 - Tailwind CSS

| 클래스               | 스타일                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inline`             | `display: inline;`                                                                                                                                      |
| `block`              | `display: block;`                                                                                                                                       |
| `inline-block`       | `display: inline-block;`                                                                                                                                |
| `flow-root`          | `display: flow-root;`                                                                                                                                   |
| `flex`               | `display: flex;`                                                                                                                                        |
| `inline-flex`        | `display: inline-flex;`                                                                                                                                 |
| `grid`               | `display: grid;`                                                                                                                                        |
| `inline-grid`        | `display: inline-grid;`                                                                                                                                 |
| `contents`           | `display: contents;`                                                                                                                                    |
| `table`              | `display: table;`                                                                                                                                       |
| `inline-table`       | `display: inline-table;`                                                                                                                                |
| `table-caption`      | `display: table-caption;`                                                                                                                               |
| `table-cell`         | `display: table-cell;`                                                                                                                                  |
| `table-column`       | `display: table-column;`                                                                                                                                |
| `table-column-group` | `display: table-column-group;`                                                                                                                          |
| `table-footer-group` | `display: table-footer-group;`                                                                                                                          |
| `table-header-group` | `display: table-header-group;`                                                                                                                          |
| `table-row-group`    | `display: table-row-group;`                                                                                                                             |
| `table-row`          | `display: table-row;`                                                                                                                                   |
| `list-item`          | `display: list-item;`                                                                                                                                   |
| `hidden`             | `display: none;`                                                                                                                                        |
| `sr-only`            | `position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; border-width: 0;` |
| `not-sr-only`        | `position: static; width: auto; height: auto; padding: 0; margin: 0; overflow: visible; clip-path: none; white-space: normal;`                          |

더 보기

## 예제

- 블록과 인라인

텍스트와 요소의 흐름을 제어하려면 `inline`, `inline-block`, `block` 유틸리티를 사용하세요:

텍스트 흐름을 제어할 때 CSS 속성 display: inline을 사용하면 요소 내부 텍스트가 일반적으로 줄바꿈됩니다.

반면 display: inline-block 속성을 사용하면 요소가 감싸져서 내부 텍스트가 부모 요소를 넘어 확장되지 않도록 합니다.

마지막으로 display: block 속성을 사용하면 요소가 자체 줄을 차지하고 부모 너비를 채웁니다.

```
    <p>  When controlling the flow of text, using the CSS property <span class="inline">display: inline</span> will cause the  text inside the element to wrap normally.</p><p>  While using the property <span class="inline-block">display: inline-block</span> will wrap the element to prevent the  text inside from extending beyond its parent.</p><p>  Lastly, using the property <span class="block">display: block</span> will put the element on its own line and fill its  parent.</p>
```

- Flow Root

`flow-root` 유틸리티를 사용해 자체 [block formatting context](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Block_formatting_context)를 갖는 블록 레벨 요소를 만드세요:

좋아, 내가 한마디 해주지, 웃긴 친구야. "New York Public Library"라고 적힌 그 작은 도장 있잖아? 너한테는 별 의미 없을지 몰라도, 나한테는 엄청난 의미가 있어. 정말 엄청나게.

그래, 원하면 웃어도 좋아. 너 같은 부류는 전에 많이 봤어. 번지르르하고, 사람들 앞에서 튀고, 관습을 과시하듯 무시하지. 그래, 네가 무슨 생각하는지 알아. 이 사람이 왜 오래된 도서관 책 때문에 이렇게 난리를 치는 거냐고? 힌트 하나 주지, 친구.

```
    <div class="p-4">  <div class="flow-root ...">    <div class="my-4 ...">Well, let me tell you something, ...</div>  </div>  <div class="flow-root ...">    <div class="my-4 ...">Sure, go ahead, laugh if you want...</div>  </div></div>
```

- Flex

`flex` 유틸리티를 사용해 블록 레벨 flex 컨테이너를 만드세요:

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Andrew Alfred** 기술 고문

```
    <div class="flex items-center">  <img src="path/to/image.jpg" />  <div>    <strong>Andrew Alfred</strong>    <span>Technical advisor</span>  </div></div>
```

- Inline Flex

`inline-flex` 유틸리티를 사용해 텍스트와 함께 흐르는 인라인 flex 컨테이너를 만드세요:

오늘은 병을 미시간에서는 10센트에 반환할 수 있지만 여기서는 5센트뿐이라는 점을 활용할 방법을 찾느라 하루 대부분을 보냈다. ![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)Kramer는 계속 이게 성립할 방법이 없다고, 가능한 모든 접근법으로 계산해 봤다고 말하지만, 나는 이걸 가능하게 만들 방법이 있다고 믿을 수밖에 없다. 여기에는 기회가 너무 크다.

```
    <p>  Today I spent most of the day researching ways to ...  <span class="inline-flex items-baseline">    <img src="/img/kramer.jpg" class="mx-1 size-5 self-center rounded-full" />    <span>Kramer</span>  </span>  keeps telling me there is no way to make it work, that ...</p>
```

- Grid

`grid` 유틸리티를 사용해 그리드 컨테이너를 만드세요:

01

02

03

04

05

06

07

08

09

```
    <div class="grid grid-cols-3 grid-rows-3 gap-4">  <!-- ... --></div>
```

- Inline Grid

`inline-grid` 유틸리티를 사용해 인라인 그리드 컨테이너를 만드세요:

01

02

03

04

05

06

01

02

03

04

05

06

```
    <span class="inline-grid grid-cols-3 gap-4">  <span>01</span>  <span>02</span>  <span>03</span>  <span>04</span>  <span>05</span>  <span>06</span></span><span class="inline-grid grid-cols-3 gap-4">  <span>01</span>  <span>02</span>  <span>03</span>  <span>04</span>  <span>05</span>  <span>06</span></span>
```

- Contents

`contents` 유틸리티를 사용해 자식 요소가 부모의 직계 자식처럼 동작하는 "유령" 컨테이너를 만드세요:

01

02

03

04

```
    <div class="flex ...">  <div class="flex-1 ...">01</div>  <div class="contents">    <div class="flex-1 ...">02</div>    <div class="flex-1 ...">03</div>  </div>  <div class="flex-1 ...">04</div></div>
```

- Table

`table`, `table-row`, `table-cell`, `table-caption`, `table-column`, `table-column-group`, `table-header-group`, `table-row-group`, `table-footer-group` 유틸리티를 사용해 각각의 테이블 요소처럼 동작하는 요소를 만드세요:

노래

아티스트

연도

The Sliding Mr. Bones (Next Stop, Pottersville)

Malcolm Lockyer

1961

Witchy Woman

The Eagles

1972

Shining Star

Earth, Wind, and Fire

1975

```
    <div class="table w-full ...">  <div class="table-header-group ...">    <div class="table-row">      <div class="table-cell text-left ...">Song</div>      <div class="table-cell text-left ...">Artist</div>      <div class="table-cell text-left ...">Year</div>    </div>  </div>  <div class="table-row-group">    <div class="table-row">      <div class="table-cell ...">The Sliding Mr. Bones (Next Stop, Pottersville)</div>      <div class="table-cell ...">Malcolm Lockyer</div>      <div class="table-cell ...">1961</div>    </div>    <div class="table-row">      <div class="table-cell ...">Witchy Woman</div>      <div class="table-cell ...">The Eagles</div>      <div class="table-cell ...">1972</div>    </div>    <div class="table-row">      <div class="table-cell ...">Shining Star</div>      <div class="table-cell ...">Earth, Wind, and Fire</div>      <div class="table-cell ...">1975</div>    </div>  </div></div>
```

- Hidden

`hidden` 유틸리티를 사용해 문서에서 요소를 제거하세요:

01

02

03

```
    <div class="flex ...">  <div class="hidden ...">01</div>  <div>02</div>  <div>03</div></div>
```

요소를 시각적으로만 숨기고 문서에는 유지하려면 대신 [visibility](https://tailwindcss.com/docs/visibility#making-elements-invisible) 속성을 사용하세요.

- 스크린 리더 전용

스크린 리더에서는 숨기지 않고 시각적으로만 요소를 숨기려면 `sr-only`를 사용하세요:

```
    <a href="#">  <svg><!-- ... --></svg>  <span class="sr-only">Settings</span></a>
```

`sr-only`를 되돌려 시각 사용자와 스크린 리더 모두에게 요소를 보이게 하려면 `not-sr-only`를 사용하세요:

```
    <a href="#">  <svg><!-- ... --></svg>  <span class="sr-only sm:not-sr-only">Settings</span></a>
```

예를 들어 작은 화면에서는 시각적으로 숨기고 큰 화면에서는 표시하고 싶을 때 유용합니다.

- 반응형 디자인

`display` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 화면 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="flex md:inline-flex ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
