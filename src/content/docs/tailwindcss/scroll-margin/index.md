---
title: "scroll-margin - 인터랙티비티 - Tailwind CSS"
description: "`scroll-ml-4` 및 `scroll-mt-6` 같은 `scroll-mt-<number>`, `scroll-mr-<number>`, `scroll-mb-<number>`, `scroll-ml-<number>` 유틸리티를 사용해 스크롤 오프셋을 설정하세요..."
---

Source URL: https://tailwindcss.com/docs/scroll-margin

# scroll-margin - 인터랙티비티 - Tailwind CSS

| 클래스                           | 스타일                                                          |
| -------------------------------- | --------------------------------------------------------------- |
| `scroll-m-<number>`              | `scroll-margin: calc(var(--spacing) * <number>);`               |
| `-scroll-m-<number>`             | `scroll-margin: calc(var(--spacing) * -<number>);`              |
| `scroll-m-(<custom-property>)`   | `scroll-margin: var(<custom-property>);`                        |
| `scroll-m-[<value>]`             | `scroll-margin: <value>;`                                       |
| `scroll-mx-<number>`             | `scroll-margin-inline: calc(var(--spacing) * <number>);`        |
| `-scroll-mx-<number>`            | `scroll-margin-inline: calc(var(--spacing) * -<number>);`       |
| `scroll-mx-(<custom-property>)`  | `scroll-margin-inline: var(<custom-property>);`                 |
| `scroll-mx-[<value>]`            | `scroll-margin-inline: <value>;`                                |
| `scroll-my-<number>`             | `scroll-margin-block: calc(var(--spacing) * <number>);`         |
| `-scroll-my-<number>`            | `scroll-margin-block: calc(var(--spacing) * -<number>);`        |
| `scroll-my-(<custom-property>)`  | `scroll-margin-block: var(<custom-property>);`                  |
| `scroll-my-[<value>]`            | `scroll-margin-block: <value>;`                                 |
| `scroll-ms-<number>`             | `scroll-margin-inline-start: calc(var(--spacing) * <number>);`  |
| `-scroll-ms-<number>`            | `scroll-margin-inline-start: calc(var(--spacing) * -<number>);` |
| `scroll-ms-(<custom-property>)`  | `scroll-margin-inline-start: var(<custom-property>);`           |
| `scroll-ms-[<value>]`            | `scroll-margin-inline-start: <value>;`                          |
| `scroll-me-<number>`             | `scroll-margin-inline-end: calc(var(--spacing) * <number>);`    |
| `-scroll-me-<number>`            | `scroll-margin-inline-end: calc(var(--spacing) * -<number>);`   |
| `scroll-me-(<custom-property>)`  | `scroll-margin-inline-end: var(<custom-property>);`             |
| `scroll-me-[<value>]`            | `scroll-margin-inline-end: <value>;`                            |
| `scroll-mbs-<number>`            | `scroll-margin-block-start: calc(var(--spacing) * <number>);`   |
| `-scroll-mbs-<number>`           | `scroll-margin-block-start: calc(var(--spacing) * -<number>);`  |
| `scroll-mbs-(<custom-property>)` | `scroll-margin-block-start: var(<custom-property>);`            |
| `scroll-mbs-[<value>]`           | `scroll-margin-block-start: <value>;`                           |
| `scroll-mbe-<number>`            | `scroll-margin-block-end: calc(var(--spacing) * <number>);`     |
| `-scroll-mbe-<number>`           | `scroll-margin-block-end: calc(var(--spacing) * -<number>);`    |
| `scroll-mbe-(<custom-property>)` | `scroll-margin-block-end: var(<custom-property>);`              |
| `scroll-mbe-[<value>]`           | `scroll-margin-block-end: <value>;`                             |
| `scroll-mt-<number>`             | `scroll-margin-top: calc(var(--spacing) * <number>);`           |
| `-scroll-mt-<number>`            | `scroll-margin-top: calc(var(--spacing) * -<number>);`          |
| `scroll-mt-(<custom-property>)`  | `scroll-margin-top: var(<custom-property>);`                    |
| `scroll-mt-[<value>]`            | `scroll-margin-top: <value>;`                                   |
| `scroll-mr-<number>`             | `scroll-margin-right: calc(var(--spacing) * <number>);`         |
| `-scroll-mr-<number>`            | `scroll-margin-right: calc(var(--spacing) * -<number>);`        |
| `scroll-mr-(<custom-property>)`  | `scroll-margin-right: var(<custom-property>);`                  |
| `scroll-mr-[<value>]`            | `scroll-margin-right: <value>;`                                 |
| `scroll-mb-<number>`             | `scroll-margin-bottom: calc(var(--spacing) * <number>);`        |
| `-scroll-mb-<number>`            | `scroll-margin-bottom: calc(var(--spacing) * -<number>);`       |
| `scroll-mb-(<custom-property>)`  | `scroll-margin-bottom: var(<custom-property>);`                 |
| `scroll-mb-[<value>]`            | `scroll-margin-bottom: <value>;`                                |
| `scroll-ml-<number>`             | `scroll-margin-left: calc(var(--spacing) * <number>);`          |
| `-scroll-ml-<number>`            | `scroll-margin-left: calc(var(--spacing) * -<number>);`         |
| `scroll-ml-(<custom-property>)`  | `scroll-margin-left: var(<custom-property>);`                   |
| `scroll-ml-[<value>]`            | `scroll-margin-left: <value>;`                                  |

더 보기

## 예제

- 기본 예제

`scroll-ml-4` 및 `scroll-mt-6` 같은 `scroll-mt-<number>`, `scroll-mr-<number>`, `scroll-mb-<number>`, `scroll-ml-<number>` 유틸리티를 사용해 스냅 컨테이너 내부 항목 주변의 스크롤 오프셋을 설정하세요:

예상 동작을 확인하려면 이미지 그리드에서 스크롤하세요

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

```
    <div class="snap-x ...">  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-01.jpg"/>  </div>  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-02.jpg"/>  </div>  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-03.jpg"/>  </div>  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-04.jpg"/>  </div>  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-05.jpg"/>  </div></div>
```

- 음수 값 사용하기

음수 scroll margin 값을 사용하려면 클래스 이름 앞에 대시를 붙여 음수 값으로 변환하세요:

```
    <div class="snap-start -scroll-ml-6 ...">  <!-- ... --></div>
```

- 논리 속성 사용하기

`scroll-ms-<number>` 및 `scroll-me-<number>` 유틸리티를 사용해 `scroll-margin-inline-start` 및 `scroll-margin-inline-end` [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts)를 설정하세요. 이 속성들은 텍스트 방향에 따라 왼쪽 또는 오른쪽에 매핑됩니다:

예상 동작을 확인하려면 이미지 그리드에서 스크롤하세요

왼쪽에서 오른쪽

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

오른쪽에서 왼쪽

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

```
    <div dir="ltr">  <div class="snap-x ...">    <div class="snap-start scroll-ms-6 ...">      <img src="/img/vacation-01.jpg"/>    </div>    <!-- ... -->  </div></div><div dir="rtl">  <div class="snap-x ...">    <div class="snap-start scroll-ms-6 ...">      <img src="/img/vacation-01.jpg"/>    </div>    <!-- ... -->  </div></div>
```

더 세밀하게 제어하려면 [LTR and RTL modifiers](https://tailwindcss.com/docs/hover-focus-and-other-states#rtl-support)를 사용해 현재 텍스트 방향에 따라 특정 스타일을 조건부로 적용할 수도 있습니다.

`scroll-mbs-<number>` 및 `scroll-mbe-<number>` 유틸리티를 사용해 `scroll-margin-block-start` 및 `scroll-margin-block-end` 논리 속성을 설정하세요. 이 속성들은 writing mode에 따라 위쪽 또는 아래쪽에 매핑됩니다:

```
    <div class="snap-y ...">  <div class="snap-start scroll-mbs-6 ...">    <!-- ... -->  </div></div>
```

- 사용자 정의 값 사용하기

`scroll-ml-[<value>]` 및 `scroll-me-[<value>]` 같은 유틸리티를 사용해 완전히 사용자 정의한 값으로 scroll margin을 설정하세요:

```
    <div class="scroll-ml-[24rem] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `scroll-ml-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="scroll-ml-(--my-scroll-margin) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `scroll-ml-[var(<custom-property>)]`의 축약 표기입니다.

- 반응형 디자인

`scroll-margin` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="scroll-m-8 md:scroll-m-0 ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

`scroll-m-<number>`,`scroll-mx-<number>`,`scroll-my-<number>`,`scroll-ms-<number>`,`scroll-me-<number>`,`scroll-mbs-<number>`,`scroll-mbe-<number>`,`scroll-mt-<number>`,`scroll-mr-<number>`,`scroll-mb-<number>`, and `scroll-ml-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 동작하며, 사용자 테마에서 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징에 대한 자세한 내용은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 확인하세요.
