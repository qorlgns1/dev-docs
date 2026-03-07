---
title: "perspective-origin - 변환 - Tailwind CSS"
description: "perspective-origin-top 및 perspective-origin-bottom-left 같은 유틸리티를 사용해 원근감의 소실점 위치를 제어하세요:"
---

소스 URL: https://tailwindcss.com/docs/perspective-origin

# perspective-origin - 변환 - Tailwind CSS

| 클래스                                   | 스타일                                        |
| ---------------------------------------- | --------------------------------------------- |
| `perspective-origin-center`              | `perspective-origin: center;`                 |
| `perspective-origin-top`                 | `perspective-origin: top;`                    |
| `perspective-origin-top-right`           | `perspective-origin: top right;`              |
| `perspective-origin-right`               | `perspective-origin: right;`                  |
| `perspective-origin-bottom-right`        | `perspective-origin: bottom right;`           |
| `perspective-origin-bottom`              | `perspective-origin: bottom;`                 |
| `perspective-origin-bottom-left`         | `perspective-origin: bottom left;`            |
| `perspective-origin-left`                | `perspective-origin: left;`                   |
| `perspective-origin-top-left`            | `perspective-origin: top left;`               |
| `perspective-origin-(<custom-property>)` | `perspective-origin: var(<custom-property>);` |
| `perspective-origin-[<value>]`           | `perspective-origin: <value>;`                |

## 예제

- 기본 예제

`perspective-origin-top` 및 `perspective-origin-bottom-left` 같은 유틸리티를 사용해 원근감의 소실점 위치를 제어하세요:

perspective-origin-top-left

1

2

3

4

5

6

perspective-origin-bottom-right

1

2

3

4

5

6

```
    <div class="size-20 perspective-near perspective-origin-top-left ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div><div class="size-20 perspective-near perspective-origin-bottom-right …">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div>
```

- 사용자 정의 값 사용하기

완전히 사용자 정의된 값을 기반으로 원근 기준점을 설정하려면 `perspective-origin-[<value>]` 구문을 사용하세요:

```
    <div class="perspective-origin-[200%_150%] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `perspective-origin-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="perspective-origin-(--my-perspective-origin) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `perspective-origin-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `perspective-origin` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 접두사로 붙이세요:

```
    <div class="perspective-origin-center md:perspective-origin-bottom-left ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
