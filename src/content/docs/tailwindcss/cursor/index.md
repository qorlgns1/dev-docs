---
title: "cursor - 인터랙티비티 - Tailwind CSS"
description: "cursor-pointer 및 cursor-grab 같은 유틸리티를 사용해 요소 위에 마우스를 올렸을 때 표시되는 커서를 제어할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/cursor

# cursor - 인터랙티비티 - Tailwind CSS

| Class                        | 스타일                            |
| ---------------------------- | --------------------------------- |
| `cursor-auto`                | `cursor: auto;`                   |
| `cursor-default`             | `cursor: default;`                |
| `cursor-pointer`             | `cursor: pointer;`                |
| `cursor-wait`                | `cursor: wait;`                   |
| `cursor-text`                | `cursor: text;`                   |
| `cursor-move`                | `cursor: move;`                   |
| `cursor-help`                | `cursor: help;`                   |
| `cursor-not-allowed`         | `cursor: not-allowed;`            |
| `cursor-none`                | `cursor: none;`                   |
| `cursor-context-menu`        | `cursor: context-menu;`           |
| `cursor-progress`            | `cursor: progress;`               |
| `cursor-cell`                | `cursor: cell;`                   |
| `cursor-crosshair`           | `cursor: crosshair;`              |
| `cursor-vertical-text`       | `cursor: vertical-text;`          |
| `cursor-alias`               | `cursor: alias;`                  |
| `cursor-copy`                | `cursor: copy;`                   |
| `cursor-no-drop`             | `cursor: no-drop;`                |
| `cursor-grab`                | `cursor: grab;`                   |
| `cursor-grabbing`            | `cursor: grabbing;`               |
| `cursor-all-scroll`          | `cursor: all-scroll;`             |
| `cursor-col-resize`          | `cursor: col-resize;`             |
| `cursor-row-resize`          | `cursor: row-resize;`             |
| `cursor-n-resize`            | `cursor: n-resize;`               |
| `cursor-e-resize`            | `cursor: e-resize;`               |
| `cursor-s-resize`            | `cursor: s-resize;`               |
| `cursor-w-resize`            | `cursor: w-resize;`               |
| `cursor-ne-resize`           | `cursor: ne-resize;`              |
| `cursor-nw-resize`           | `cursor: nw-resize;`              |
| `cursor-se-resize`           | `cursor: se-resize;`              |
| `cursor-sw-resize`           | `cursor: sw-resize;`              |
| `cursor-ew-resize`           | `cursor: ew-resize;`              |
| `cursor-ns-resize`           | `cursor: ns-resize;`              |
| `cursor-nesw-resize`         | `cursor: nesw-resize;`            |
| `cursor-nwse-resize`         | `cursor: nwse-resize;`            |
| `cursor-zoom-in`             | `cursor: zoom-in;`                |
| `cursor-zoom-out`            | `cursor: zoom-out;`               |
| `cursor-(<custom-property>)` | `cursor: var(<custom-property>);` |
| `cursor-[<value>]`           | `cursor: <value>;`                |

더 보기

## 예시

- 기본 예시

`cursor-pointer` 및 `cursor-grab` 같은 유틸리티를 사용해 요소 위에 마우스를 올렸을 때 표시되는 커서를 제어할 수 있습니다:

각 버튼 위에 마우스를 올려 커서가 바뀌는 것을 확인해 보세요

SubmitSaving...Confirm

```
    <button class="cursor-pointer ...">Submit</button><button class="cursor-progress ...">Saving...</button><button class="cursor-not-allowed ..." disabled>Confirm</button>
```

- 사용자 지정 값 사용하기

`cursor-[<value>]` 구문을 사용해 완전히 사용자 지정한 값으로 커서를 설정할 수 있습니다:

```
    <button class="cursor-[url(hand.cur),_pointer] ...">  <!-- ... --></button>
```

CSS 변수의 경우 `cursor-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <button class="cursor-(--my-cursor) ...">  <!-- ... --></button>
```

이는 `var()` 함수를 자동으로 추가해 주는 `cursor-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`cursor` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <button class="cursor-not-allowed md:cursor-auto ...">  <!-- ... --></button>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
