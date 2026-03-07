---
title: "perspective - 변형 - Tailwind CSS"
description: "`perspective-normal` 및 `perspective-distant` 같은 유틸리티를 사용해 z-평면이 화면에서 얼마나 가깝거나 먼지 제어하세요:"
---

원문 URL: https://tailwindcss.com/docs/perspective

# perspective - 변형 - Tailwind CSS

| 클래스                            | 스타일                                                  |
| --------------------------------- | ------------------------------------------------------- |
| `perspective-dramatic`            | `perspective: var(--perspective-dramatic); /* 100px */` |
| `perspective-near`                | `perspective: var(--perspective-near); /* 300px */`     |
| `perspective-normal`              | `perspective: var(--perspective-normal); /* 500px */`   |
| `perspective-midrange`            | `perspective: var(--perspective-midrange); /* 800px */` |
| `perspective-distant`             | `perspective: var(--perspective-distant); /* 1200px */` |
| `perspective-none`                | `perspective: none;`                                    |
| `perspective-(<custom-property>)` | `perspective: var(<custom-property>);`                  |
| `perspective-[<value>]`           | `perspective: <value>;`                                 |

## 예제

- 기본 예제

`perspective-normal` 및 `perspective-distant` 같은 유틸리티를 사용해 z-평면이 화면에서 얼마나 가깝거나 먼지 제어하세요:

perspective-dramatic

1

2

3

4

5

6

perspective-normal

1

2

3

4

5

6

```
    <div class="size-20 perspective-dramatic ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div><div class="size-20 perspective-normal ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div>
```

이는 카메라를 물체에 더 가깝게 또는 더 멀게 이동하는 것과 비슷합니다.

- 원근감 제거하기

요소에서 원근 변형을 제거하려면 `perspective-none` 유틸리티를 사용하세요:

```
    <div class="perspective-none ...">  <!-- ... --></div>
```

- 사용자 지정 값 사용하기

`perspective-[<value>]` 문법을 사용하면 완전히 사용자 지정한 값으로 perspective를 설정할 수 있습니다:

```
    <div class="perspective-[750px] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `perspective-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="perspective-(--my-perspective) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `perspective-[var(<custom-property>)]`의 축약 문법입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `perspective` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="perspective-midrange md:perspective-dramatic ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.

## 테마 사용자 지정

프로젝트에서 perspective 유틸리티를 사용자 지정하려면 `--perspective-*` 테마 변수를 사용하세요:

```
    @theme {  --perspective-remote: 1800px; }
```

이제 마크업에서 `perspective-remote` 유틸리티를 사용할 수 있습니다:

```
    <div class="perspective-remote">  <!-- ... --></div>
```

테마 사용자 지정에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)를 참고하세요.
