---
title: "aspect-ratio - 레이아웃 - Tailwind CSS"
description: "aspect-3/2 같은 aspect-<ratio> 유틸리티를 사용해 요소에 특정 종횡비를 적용합니다:"
---

출처 URL: https://tailwindcss.com/docs/aspect-ratio

# aspect-ratio - 레이아웃 - Tailwind CSS

| 클래스                       | 스타일                                            |
| ---------------------------- | ------------------------------------------------- |
| `aspect-<ratio>`             | `aspect-ratio: <ratio>;`                          |
| `aspect-square`              | `aspect-ratio: 1 / 1;`                            |
| `aspect-video`               | `aspect-ratio: var(--aspect-video); /* 16 / 9 */` |
| `aspect-auto`                | `aspect-ratio: auto;`                             |
| `aspect-(<custom-property>)` | `aspect-ratio: var(<custom-property>);`           |
| `aspect-[<value>]`           | `aspect-ratio: <value>;`                          |

## 예제

- 기본 예제

`aspect-3/2` 같은 `aspect-<ratio>` 유틸리티를 사용해 요소에 특정 종횡비를 적용합니다:

예제 크기를 조절해 예상 동작을 확인해 보세요.

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1200&q=80)

```
    <img class="aspect-3/2 object-cover ..." src="/img/villas.jpg" />
```

- 비디오 종횡비 사용하기

`aspect-video` 유틸리티를 사용해 비디오 요소에 16 / 9 종횡비를 적용합니다:

예제 크기를 조절해 예상 동작을 확인해 보세요.

```
    <iframe class="aspect-video ..." src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

- 사용자 정의 값 사용하기

`aspect-[<value>]` 문법을 사용해 완전히 사용자 정의한 값을 기준으로 종횡비를 설정합니다:

```
    <img class="aspect-[calc(4*3+1)/3] ..." src="/img/villas.jpg" />
```

CSS 변수의 경우 `aspect-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <img class="aspect-(--my-aspect-ratio) ..." src="/img/villas.jpg" />
```

이는 `var()` 함수를 자동으로 추가해 주는 `aspect-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형을 `aspect-ratio` 유틸리티 앞에 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <iframe class="aspect-video md:aspect-square ..." src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.

## 테마 사용자 정의

프로젝트에서 종횡비 유틸리티를 사용자 정의하려면 `--aspect-*` 테마 변수를 사용하세요:

```
    @theme {  --aspect-retro: 4 / 3; }
```

이제 마크업에서 `aspect-retro` 유틸리티를 사용할 수 있습니다:

```
    <iframe class="aspect-retro" src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

테마 사용자 정의에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
