---
title: "columns - 레이아웃 - Tailwind CSS"
description: "요소 내부 콘텐츠에 생성할 열 개수를 설정하려면 columns-3 같은 columns-<number> 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/columns

# columns - 레이아웃 - Tailwind CSS

| 클래스                        | 스타일                                                |
| ----------------------------- | ----------------------------------------------------- |
| `columns-<number>`            | `columns: <number>;`                                  |
| `columns-3xs`                 | `columns: var(--container-3xs); /* 16rem (256px) */`  |
| `columns-2xs`                 | `columns: var(--container-2xs); /* 18rem (288px) */`  |
| `columns-xs`                  | `columns: var(--container-xs); /* 20rem (320px) */`   |
| `columns-sm`                  | `columns: var(--container-sm); /* 24rem (384px) */`   |
| `columns-md`                  | `columns: var(--container-md); /* 28rem (448px) */`   |
| `columns-lg`                  | `columns: var(--container-lg); /* 32rem (512px) */`   |
| `columns-xl`                  | `columns: var(--container-xl); /* 36rem (576px) */`   |
| `columns-2xl`                 | `columns: var(--container-2xl); /* 42rem (672px) */`  |
| `columns-3xl`                 | `columns: var(--container-3xl); /* 48rem (768px) */`  |
| `columns-4xl`                 | `columns: var(--container-4xl); /* 56rem (896px) */`  |
| `columns-5xl`                 | `columns: var(--container-5xl); /* 64rem (1024px) */` |
| `columns-6xl`                 | `columns: var(--container-6xl); /* 72rem (1152px) */` |
| `columns-7xl`                 | `columns: var(--container-7xl); /* 80rem (1280px) */` |
| `columns-auto`                | `columns: auto;`                                      |
| `columns-(<custom-property>)` | `columns: var(<custom-property>);`                    |
| `columns-[<value>]`           | `columns: <value>;`                                   |

더 보기

## 예제

- 숫자로 설정하기

요소 내부 콘텐츠에 생성할 열 개수를 설정하려면 `columns-3` 같은 `columns-<number>` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2952&q=80)![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2902&q=80)![](https://images.unsplash.com/photo-1491904768633-2b7e3e7fede5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3131&q=80)![](https://images.unsplash.com/photo-1463288889890-a56b2853c40f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3132&q=80)![](https://images.unsplash.com/photo-1611605645802-c21be743c321?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)![](https://images.unsplash.com/photo-1498603993951-8a027a8a8f84?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2936&q=80)![](https://images.unsplash.com/photo-1526400473556-aac12354f3db?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)![](https://images.unsplash.com/photo-1617369120004-4fc70312c5e6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1587&q=80)![](https://images.unsplash.com/photo-1518892096458-a169843d7f7f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)

```
    <div class="columns-3 ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

열 너비는 지정한 열 개수에 맞게 자동으로 조정됩니다.

- 너비로 설정하기

요소 내부 콘텐츠에 대한 이상적인 열 너비를 설정하려면 `columns-xs`, `columns-sm` 같은 유틸리티를 사용하세요:

예시 크기를 조절해 예상 동작을 확인하세요

![](https://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2952&q=80)![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2902&q=80)![](https://images.unsplash.com/photo-1491904768633-2b7e3e7fede5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3131&q=80)![](https://images.unsplash.com/photo-1463288889890-a56b2853c40f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3132&q=80)

```
    <div class="columns-3xs ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

열 너비를 설정하면 열이 너무 좁아지지 않도록 열 개수가 자동으로 조정됩니다.

- 열 간격 설정하기

열 사이 너비를 지정하려면 `gap-<width>` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2952&q=80)![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2902&q=80)![](https://images.unsplash.com/photo-1491904768633-2b7e3e7fede5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3131&q=80)![](https://images.unsplash.com/photo-1463288889890-a56b2853c40f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3132&q=80)![](https://images.unsplash.com/photo-1611605645802-c21be743c321?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)![](https://images.unsplash.com/photo-1498603993951-8a027a8a8f84?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2936&q=80)![](https://images.unsplash.com/photo-1526400473556-aac12354f3db?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)![](https://images.unsplash.com/photo-1617369120004-4fc70312c5e6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1587&q=80)![](https://images.unsplash.com/photo-1518892096458-a169843d7f7f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)

```
    <div class="columns-3 gap-8 ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

`gap` 유틸리티에 대한 자세한 내용은 [gap documentation](https://tailwindcss.com/docs/gap)에서 확인하세요.

- 사용자 지정 값 사용하기

완전히 사용자 지정한 값으로 열을 설정하려면 `columns-[<value>]` 구문을 사용하세요:

```
    <div class="columns-[30vw] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `columns-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="columns-(--my-columns) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `columns-[var(<custom-property>)]`의 단축 표기일 뿐입니다.

- 반응형 디자인

작은 화면 크기 이상에서만 유틸리티를 적용하려면 `columns` 유틸리티 앞에 `sm:` 같은 브레이크포인트 variant를 붙이세요:

예시 크기를 조절해 예상 동작을 확인하세요

![](https://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2952&q=80)![](https://images.unsplash.com/photo-1434394354979-a235cd36269d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2902&q=80)![](https://images.unsplash.com/photo-1491904768633-2b7e3e7fede5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3131&q=80)![](https://images.unsplash.com/photo-1463288889890-a56b2853c40f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3132&q=80)![](https://images.unsplash.com/photo-1611605645802-c21be743c321?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)![](https://images.unsplash.com/photo-1498603993951-8a027a8a8f84?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2936&q=80)![](https://images.unsplash.com/photo-1526400473556-aac12354f3db?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)![](https://images.unsplash.com/photo-1617369120004-4fc70312c5e6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1587&q=80)![](https://images.unsplash.com/photo-1518892096458-a169843d7f7f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80)

```
    <div class="columns-2 gap-4 sm:columns-3 sm:gap-8 ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.

## 테마 커스터마이징

프로젝트에서 고정 너비 열 유틸리티를 커스터마이징하려면 `--container-*` 테마 변수를 사용하세요:

```
    @theme {  --container-4xs: 14rem; }
```

이제 마크업에서 `columns-4xs` 유틸리티를 사용할 수 있습니다:

```
    <div class="columns-4xs">  <!-- ... --></div>
```

테마 커스터마이징에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
