---
title: "filter: blur() - 필터 - Tailwind CSS"
description: "blur-sm, blur-lg 같은 유틸리티를 사용해 요소를 흐리게 처리합니다:"
---

# filter: blur() - 필터 - Tailwind CSS

| Class                      | 스타일                                      |
| -------------------------- | ------------------------------------------- |
| `blur-xs`                  | `filter: blur(var(--blur-xs)); /* 4px */`   |
| `blur-sm`                  | `filter: blur(var(--blur-sm)); /* 8px */`   |
| `blur-md`                  | `filter: blur(var(--blur-md)); /* 12px */`  |
| `blur-lg`                  | `filter: blur(var(--blur-lg)); /* 16px */`  |
| `blur-xl`                  | `filter: blur(var(--blur-xl)); /* 24px */`  |
| `blur-2xl`                 | `filter: blur(var(--blur-2xl)); /* 40px */` |
| `blur-3xl`                 | `filter: blur(var(--blur-3xl)); /* 64px */` |
| `blur-none`                | `filter: ;`                                 |
| `blur-(<custom-property>)` | `filter: blur(var(<custom-property>));`     |
| `blur-[<value>]`           | `filter: blur(<value>);`                    |

## 예제

- 기본 예제

`blur-sm`, `blur-lg` 같은 유틸리티를 사용해 요소를 흐리게 처리합니다:

blur-none

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

blur-sm

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

blur-lg

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

blur-2xl

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="blur-none" src="/img/mountains.jpg" /><img class="blur-sm" src="/img/mountains.jpg" /><img class="blur-lg" src="/img/mountains.jpg" /><img class="blur-2xl" src="/img/mountains.jpg" />
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값으로 블러를 설정하려면 `blur-[<value>]` 문법을 사용합니다:

```
    <img class="blur-[2px] ..." src="/img/mountains.jpg" />
```

CSS 변수의 경우 `blur-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="blur-(--my-blur) ..." src="/img/mountains.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `blur-[var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`filter: blur()` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <img class="blur-none md:blur-lg ..." src="/img/mountains.jpg" />
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 확인하세요.

## 테마 사용자 지정

프로젝트에서 블러 유틸리티를 사용자 지정하려면 `--blur-*` 테마 변수를 사용하세요:

```
    @theme {  --blur-2xs: 2px; }
```

이제 마크업에서 `blur-2xs` 유틸리티를 사용할 수 있습니다:

```
    <img class="blur-2xs" src="/img/mountains.jpg" />
```

테마 사용자 지정에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
