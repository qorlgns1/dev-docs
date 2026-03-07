---
title: "font-family - 타이포그래피 - Tailwind CSS"
description: "font-sans 및 font-mono 같은 유틸리티를 사용해 요소의 글꼴 패밀리를 설정하세요:"
---

출처 URL: https://tailwindcss.com/docs/font-family

# font-family - 타이포그래피 - Tailwind CSS

| 클래스                                 | 스타일                                                                                                                                                    |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `font-sans`                            | `font-family: var(--font-sans); /* ui-sans-serif, system-ui, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji' */` |
| `font-serif`                           | `font-family: var(--font-serif); /* ui-serif, Georgia, Cambria, 'Times New Roman', Times, serif */`                                                       |
| `font-mono`                            | `font-family: var(--font-mono); /* ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace */`                 |
| `font-(family-name:<custom-property>)` | `font-family: var(<custom-property>);`                                                                                                                    |
| `font-[<value>]`                       | `font-family: <value>;`                                                                                                                                   |

## 예제

- 기본 예제

`font-sans` 및 `font-mono` 같은 유틸리티를 사용해 요소의 글꼴 패밀리를 설정하세요:

font-sans

The quick brown fox jumps over the lazy dog.

font-serif

The quick brown fox jumps over the lazy dog.

font-mono

The quick brown fox jumps over the lazy dog.

```
    <p class="font-sans ...">The quick brown fox ...</p><p class="font-serif ...">The quick brown fox ...</p><p class="font-mono ...">The quick brown fox ...</p>
```

- 사용자 정의 값 사용하기

완전히 사용자 정의된 값을 기반으로 글꼴 패밀리를 설정하려면 `font-[<value>]` 구문을 사용하세요:

```
    <p class="font-[Open_Sans] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `font-(family-name:<custom-property>)` 구문도 사용할 수 있습니다:

```
    <p class="font-(family-name:--my-font) ...">  Lorem ipsum dolor sit amet...</p>
```

이는 자동으로 `var()` 함수를 추가해 주는 `font-[family-name:var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `font-family` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <p class="font-sans md:font-serif ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.

## 테마 커스터마이징

프로젝트에서 글꼴 패밀리 유틸리티를 커스터마이징하려면 `--font-*` 테마 변수를 사용하세요:

```
    @theme {  --font-display: "Oswald", sans-serif; }
```

이제 마크업에서 `font-display` 유틸리티를 사용할 수 있습니다:

```
    <div class="font-display">  <!-- ... --></div>
```

글꼴 패밀리에 대한 기본 `font-feature-settings` 및 `font-variation-settings` 값도 제공할 수 있습니다:

```
    @theme {  --font-display: "Oswald", sans-serif;  --font-display--font-feature-settings: "cv02", "cv03", "cv04", "cv11";   --font-display--font-variation-settings: "opsz" 32; }
```

필요한 경우 사용자 정의 글꼴을 로드하려면 [@font-face](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face) at-rule을 사용하세요:

```
    @font-face {  font-family: Oswald;  font-style: normal;  font-weight: 200 700;  font-display: swap;  src: url("/fonts/Oswald.woff2") format("woff2");}
```

[Google Fonts](https://fonts.google.com/) 같은 서비스에서 글꼴을 로드하는 경우 `@import`를 CSS 파일의 맨 위에 배치해야 합니다:

```
    @import url("https://fonts.googleapis.com/css2?family=Roboto&display=swap");@import "tailwindcss";@theme {  --font-roboto: "Roboto", sans-serif; }
```

브라우저는 `@import` 문이 다른 어떤 규칙보다 먼저 와야 하므로, URL import는 컴파일된 CSS에 인라인되는 `@import "tailwindcss"` 같은 import보다 위에 있어야 합니다.

테마 커스터마이징에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
