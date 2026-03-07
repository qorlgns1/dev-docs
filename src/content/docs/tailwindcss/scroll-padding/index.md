---
title: "scroll-padding - 상호작용 - Tailwind CSS"
description: "`scroll-pl-4` 및 `scroll-pt-6` 같은 `scroll-pt-<number>`, `scroll-pr-<number>`, `scroll-pb-<number>`, `scroll-pl-<number>` 유틸리티를 사용해 스크롤..."
---

Source URL: https://tailwindcss.com/docs/scroll-padding

# scroll-padding - 상호작용 - Tailwind CSS

| 클래스                           | 스타일                                                           |
| -------------------------------- | ---------------------------------------------------------------- |
| `scroll-p-<number>`              | `scroll-padding: calc(var(--spacing) * <number>);`               |
| `-scroll-p-<number>`             | `scroll-padding: calc(var(--spacing) * -<number>);`              |
| `scroll-p-(<custom-property>)`   | `scroll-padding: var(<custom-property>);`                        |
| `scroll-p-[<value>]`             | `scroll-padding: <value>;`                                       |
| `scroll-px-<number>`             | `scroll-padding-inline: calc(var(--spacing) * <number>);`        |
| `-scroll-px-<number>`            | `scroll-padding-inline: calc(var(--spacing) * -<number>);`       |
| `scroll-px-(<custom-property>)`  | `scroll-padding-inline: var(<custom-property>);`                 |
| `scroll-px-[<value>]`            | `scroll-padding-inline: <value>;`                                |
| `scroll-py-<number>`             | `scroll-padding-block: calc(var(--spacing) * <number>);`         |
| `-scroll-py-<number>`            | `scroll-padding-block: calc(var(--spacing) * -<number>);`        |
| `scroll-py-(<custom-property>)`  | `scroll-padding-block: var(<custom-property>);`                  |
| `scroll-py-[<value>]`            | `scroll-padding-block: <value>;`                                 |
| `scroll-ps-<number>`             | `scroll-padding-inline-start: calc(var(--spacing) * <number>);`  |
| `-scroll-ps-<number>`            | `scroll-padding-inline-start: calc(var(--spacing) * -<number>);` |
| `scroll-ps-(<custom-property>)`  | `scroll-padding-inline-start: var(<custom-property>);`           |
| `scroll-ps-[<value>]`            | `scroll-padding-inline-start: <value>;`                          |
| `scroll-pe-<number>`             | `scroll-padding-inline-end: calc(var(--spacing) * <number>);`    |
| `-scroll-pe-<number>`            | `scroll-padding-inline-end: calc(var(--spacing) * -<number>);`   |
| `scroll-pe-(<custom-property>)`  | `scroll-padding-inline-end: var(<custom-property>);`             |
| `scroll-pe-[<value>]`            | `scroll-padding-inline-end: <value>;`                            |
| `scroll-pbs-<number>`            | `scroll-padding-block-start: calc(var(--spacing) * <number>);`   |
| `-scroll-pbs-<number>`           | `scroll-padding-block-start: calc(var(--spacing) * -<number>);`  |
| `scroll-pbs-(<custom-property>)` | `scroll-padding-block-start: var(<custom-property>);`            |
| `scroll-pbs-[<value>]`           | `scroll-padding-block-start: <value>;`                           |
| `scroll-pbe-<number>`            | `scroll-padding-block-end: calc(var(--spacing) * <number>);`     |
| `-scroll-pbe-<number>`           | `scroll-padding-block-end: calc(var(--spacing) * -<number>);`    |
| `scroll-pbe-(<custom-property>)` | `scroll-padding-block-end: var(<custom-property>);`              |
| `scroll-pbe-[<value>]`           | `scroll-padding-block-end: <value>;`                             |
| `scroll-pt-<number>`             | `scroll-padding-top: calc(var(--spacing) * <number>);`           |
| `-scroll-pt-<number>`            | `scroll-padding-top: calc(var(--spacing) * -<number>);`          |
| `scroll-pt-(<custom-property>)`  | `scroll-padding-top: var(<custom-property>);`                    |
| `scroll-pt-[<value>]`            | `scroll-padding-top: <value>;`                                   |
| `scroll-pr-<number>`             | `scroll-padding-right: calc(var(--spacing) * <number>);`         |
| `-scroll-pr-<number>`            | `scroll-padding-right: calc(var(--spacing) * -<number>);`        |
| `scroll-pr-(<custom-property>)`  | `scroll-padding-right: var(<custom-property>);`                  |
| `scroll-pr-[<value>]`            | `scroll-padding-right: <value>;`                                 |
| `scroll-pb-<number>`             | `scroll-padding-bottom: calc(var(--spacing) * <number>);`        |
| `-scroll-pb-<number>`            | `scroll-padding-bottom: calc(var(--spacing) * -<number>);`       |
| `scroll-pb-(<custom-property>)`  | `scroll-padding-bottom: var(<custom-property>);`                 |
| `scroll-pb-[<value>]`            | `scroll-padding-bottom: <value>;`                                |
| `scroll-pl-<number>`             | `scroll-padding-left: calc(var(--spacing) * <number>);`          |
| `-scroll-pl-<number>`            | `scroll-padding-left: calc(var(--spacing) * -<number>);`         |
| `scroll-pl-(<custom-property>)`  | `scroll-padding-left: var(<custom-property>);`                   |
| `scroll-pl-[<value>]`            | `scroll-padding-left: <value>;`                                  |

더 보기

## 예제

- 기본 예제

`scroll-pl-4` 및 `scroll-pt-6` 같은 `scroll-pt-<number>`, `scroll-pr-<number>`, `scroll-pb-<number>`, `scroll-pl-<number>` 유틸리티를 사용해 스냅 컨테이너 내 요소의 스크롤 오프셋을 설정합니다:

예상되는 동작을 확인하려면 이미지 그리드에서 스크롤하세요

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

```
    <div class="snap-x scroll-pl-6 ...">  <div class="snap-start ...">    <img src="/img/vacation-01.jpg" />  </div>  <div class="snap-start ...">    <img src="/img/vacation-02.jpg" />  </div>  <div class="snap-start ...">    <img src="/img/vacation-03.jpg" />  </div>  <div class="snap-start ...">    <img src="/img/vacation-04.jpg" />  </div>  <div class="snap-start ...">    <img src="/img/vacation-05.jpg" />  </div></div>
```

- 논리 속성 사용

`scroll-ps-<number>` 및 `scroll-pe-<number>` 유틸리티를 사용해 `scroll-padding-inline-start` 및 `scroll-padding-inline-end` 논리 속성을 설정합니다. 이 속성은 텍스트 방향에 따라 왼쪽 또는 오른쪽에 매핑됩니다:

예상되는 동작을 확인하려면 이미지 그리드에서 스크롤하세요

왼쪽에서 오른쪽

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

오른쪽에서 왼쪽

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGV8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

```
    <div dir="ltr">  <div class="snap-x scroll-ps-6 ...">    <!-- ... -->  </div></div><div dir="rtl">  <div class="snap-x scroll-ps-6 ...">    <!-- ... -->  </div></div>
```

`scroll-pbs-<number>` 및 `scroll-pbe-<number>` 유틸리티를 사용해 `scroll-padding-block-start` 및 `scroll-padding-block-end` 논리 속성을 설정합니다. 이 속성은 작성 모드에 따라 위쪽 또는 아래쪽에 매핑됩니다:

```
    <div class="snap-y scroll-pbs-6 ...">  <!-- ... --></div>
```

- 음수 값 사용

음수 scroll padding 값을 사용하려면 클래스 이름 앞에 대시를 붙여 음수 값으로 변환하세요:

```
    <div class="-scroll-ps-6 snap-x ...">  <!-- ... --></div>
```

- 사용자 지정 값 사용

`scroll-pl-[<value>]` 및 `scroll-pe-[<value>]` 같은 유틸리티를 사용해 완전히 사용자 지정한 값으로 scroll padding을 설정할 수 있습니다:

```
    <div class="scroll-pl-[24rem] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `scroll-pl-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="scroll-pl-(--my-scroll-padding) ...">  <!-- ... --></div>
```

이 문법은 `scroll-pl-[var(<custom-property>)]`의 단축형일 뿐이며, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`scroll-padding` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="scroll-p-8 md:scroll-p-0 ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

`scroll-p-<number>`,`scroll-px-<number>`,`scroll-py-<number>`,`scroll-ps-<number>`,`scroll-pe-<number>`,`scroll-pbs-<number>`,`scroll-pbe-<number>`,`scroll-pt-<number>`,`scroll-pr-<number>`,`scroll-pb-<number>`, 그리고 `scroll-pl-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 구동되며, 이 변수는 사용자 테마에서 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징은 [theme variable documentation](https://tailwindcss.com/docs/theme)에서 자세히 알아보세요.
