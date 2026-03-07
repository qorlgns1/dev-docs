---
title: "Preflight - 기본 스타일 - Tailwind CSS"
description: "modern-normalize를 기반으로 구축된 Preflight는 브라우저 간 불일치를 완화하고 디자인 시스템의 제약 안에서 더 쉽게 작업할 수 있도록 설계된 Tailwind 프로젝트용 기본 스타일 세트입니다..."
---

Source URL: https://tailwindcss.com/docs/preflight

# Preflight - 기본 스타일 - Tailwind CSS

## 개요

[modern-normalize](https://github.com/sindresorhus/modern-normalize)를 기반으로 구축된 Preflight는 브라우저 간 불일치를 완화하고 디자인 시스템의 제약 안에서 더 쉽게 작업할 수 있도록 설계된 Tailwind 프로젝트용 기본 스타일 세트입니다.

프로젝트에 `tailwindcss`를 import하면 Preflight가 `base` 레이어에 자동으로 주입됩니다:

CSS

```
    @layer theme, base, components, utilities;@import "tailwindcss/theme.css" layer(theme);@import "tailwindcss/preflight.css" layer(base);@import "tailwindcss/utilities.css" layer(utilities);
```

Preflight의 대부분 스타일은 눈에 띄지 않도록 설계되어 있습니다. 기대한 대로 동작하게 만들어 줄 뿐입니다. 하지만 일부는 더 강한 의견이 반영되어 있어 처음 접하면 의외로 느껴질 수 있습니다.

Preflight가 적용하는 모든 스타일의 전체 참조는 [stylesheet](https://github.com/tailwindlabs/tailwindcss/blob/main/packages/tailwindcss/preflight.css)를 확인하세요.

- 마진이 제거됩니다

Preflight는 heading, blockquote, paragraph 등을 포함한 모든 요소의 기본 마진을 제거합니다:

CSS

```
    *,::after,::before,::backdrop,::file-selector-button {  margin: 0;  padding: 0;}
```

이렇게 하면 spacing scale에 포함되지 않은 user-agent stylesheet의 마진 값에 실수로 의존하기가 더 어려워집니다.

- 보더 스타일이 초기화됩니다

`border` 클래스를 추가하는 것만으로 보더를 쉽게 적용할 수 있도록, Tailwind는 다음 규칙으로 모든 요소의 기본 보더 스타일을 재정의합니다:

CSS

```
    *,::after,::before,::backdrop,::file-selector-button {  box-sizing: border-box;  border: 0 solid;}
```

`border` 클래스는 `border-width` 속성만 설정하므로, 이 초기화는 해당 클래스를 추가할 때 항상 `currentColor`를 사용하는 단색 `1px` 보더가 적용되도록 보장합니다.

이로 인해 특정 서드파티 라이브러리(예: [Google maps](https://github.com/tailwindlabs/tailwindcss/issues/484))를 통합할 때 예상치 못한 결과가 발생할 수 있습니다.

이런 상황에서는 사용자 정의 CSS로 Preflight 스타일을 재정의해 우회할 수 있습니다:

CSS

```
    @layer base {  .google-map * {    border-style: none;  }}
```

- 헤딩은 스타일이 없습니다

모든 heading 요소는 기본적으로 완전히 스타일이 제거되며, 일반 텍스트와 같은 font size와 weight를 가집니다:

CSS

```
    h1,h2,h3,h4,h5,h6 {  font-size: inherit;  font-weight: inherit;}
```

이유는 두 가지입니다:

- **type scale에서 의도치 않게 벗어나는 일을 방지합니다**. 기본적으로 브라우저는 Tailwind의 기본 type scale에 없고, 사용자 type scale에도 존재한다는 보장이 없는 크기를 heading에 할당합니다.
- **UI 개발에서는 heading을 시각적으로 덜 강조해야 하는 경우가 많습니다**. heading이 기본적으로 unstyled이면, heading에 적용하는 모든 스타일링이 의식적이고 의도적으로 이루어집니다.

프로젝트에 기본 header 스타일을 추가하려면 [adding your own base styles](https://tailwindcss.com/docs/adding-custom-styles#adding-base-styles)를 참고하세요.

- 목록은 스타일이 없습니다

순서 있는 목록과 순서 없는 목록은 기본적으로 스타일이 없으며, 글머리표나 번호가 표시되지 않습니다:

CSS

```
    ol,ul,menu {  list-style: none;}
```

목록에 스타일을 적용하려면 [list-style-type](https://tailwindcss.com/docs/list-style-type) 및 [list-style-position](https://tailwindcss.com/docs/list-style-position) 유틸리티를 사용할 수 있습니다:

HTML

```
    <ul class="list-inside list-disc">  <li>One</li>  <li>Two</li>  <li>Three</li></ul>
```

프로젝트에 기본 목록 스타일을 추가하려면 [adding your own base styles](https://tailwindcss.com/docs/adding-custom-styles#adding-base-styles)를 참고하세요.

#

- 접근성 고려 사항

스타일이 없는 목록은 [VoiceOver에서 목록으로 안내되지 않습니다](https://unfetteredthoughts.net/2017/09/26/voiceover-and-list-style-type-none/). 콘텐츠가 실제로 목록이지만 스타일 없이 유지하고 싶다면 요소에 [`"list"` role을 추가](https://www.scottohara.me/blog/2019/01/12/lists-and-safari.html)하세요:

HTML

```
    <ul role="list">  <li>One</li>  <li>Two</li>  <li>Three</li></ul>
```

- 이미지는 블록 레벨입니다

이미지 및 기타 대체 요소(`svg`, `video`, `canvas` 등)는 기본적으로 `display: block`입니다:

CSS

```
    img,svg,video,canvas,audio,iframe,embed,object {  display: block;  vertical-align: middle;}
```

이렇게 하면 브라우저 기본값인 `display: inline`을 사용할 때 자주 발생하는 예기치 않은 정렬 문제를 피하는 데 도움이 됩니다.

이 요소들 중 하나를 `block` 대신 `inline`으로 만들어야 한다면 `inline` 유틸리티를 사용하세요:

HTML

```
    <img class="inline" src="..." alt="..." />
```

- 이미지는 크기가 제한됩니다

이미지와 비디오는 고유 종횡비를 유지하는 방식으로 부모 너비에 맞게 제한됩니다:

CSS

```
    img,video {  max-width: 100%;  height: auto;}
```

이렇게 하면 컨테이너를 넘쳐흐르는 것을 방지하고 기본적으로 반응형이 되도록 합니다. 이 동작을 재정의해야 한다면 `max-w-none` 유틸리티를 사용하세요:

HTML

```
    <img class="max-w-none" src="..." alt="..." />
```

#

- `hidden` 속성이 있는 요소는 숨김 상태를 유지합니다

CSS

```
    [hidden]:where(:not([hidden="until-found"])) {  display: none !important;}
```

이는 `hidden="until-found"`를 사용하는 경우를 제외하고 `hidden` 속성이 있는 요소가 보이지 않도록 강제합니다. 사용자에게 요소를 보이게 하려면 `hidden` 속성을 제거하세요.

## Preflight 확장하기

Preflight 위에 사용자 정의 기본 스타일을 추가하려면 CSS에서 `@layer base`를 사용해 `base` CSS 레이어에 추가하세요:

CSS

```
    @layer base {  h1 {    font-size: var(--text-2xl);  }  h2 {    font-size: var(--text-xl);  }  h3 {    font-size: var(--text-lg);  }  a {    color: var(--color-blue-600);    text-decoration-line: underline;  }}
```

자세한 내용은 [adding base styles documentation](https://tailwindcss.com/docs/adding-custom-styles#adding-base-styles)에서 확인할 수 있습니다.

## Preflight 비활성화하기

Preflight를 완전히 비활성화하려면(예: 기존 프로젝트에 Tailwind를 통합하는 경우 또는 자체 기본 스타일을 정의하고 싶은 경우), 필요한 Tailwind 부분만 import하면 됩니다.

기본적으로 `@import "tailwindcss";`는 다음을 주입합니다:

CSS

```
    @layer theme, base, components, utilities;@import "tailwindcss/theme.css" layer(theme);@import "tailwindcss/preflight.css" layer(base);@import "tailwindcss/utilities.css" layer(utilities);
```

Preflight를 비활성화하려면 다른 항목은 유지한 채 해당 import만 생략하면 됩니다:

CSS

```
    @layer theme, base, components, utilities;@import "tailwindcss/theme.css" layer(theme);@import "tailwindcss/preflight.css" layer(base);@import "tailwindcss/utilities.css" layer(utilities);
```

Tailwind CSS 파일을 개별적으로 import할 때 `source()`, `theme()`, `prefix()` 같은 기능은 각 기능이 적용되는 import에 지정해야 합니다.

예를 들어 source detection은 생성되는 유틸리티에 영향을 주므로 `source(…)`는 `utilities.css` import에 추가해야 합니다:

CSS

```
    @layer theme, base, components, utilities;@import "tailwindcss/theme.css" layer(theme);@import "tailwindcss/utilities.css" layer(utilities);@import "tailwindcss/utilities.css" layer(utilities) source(none);
```

`important`도 유틸리티에 영향을 주므로 동일합니다:

CSS

```
    @layer theme, base, components, utilities;@import "tailwindcss/theme.css" layer(theme);@import "tailwindcss/utilities.css" layer(utilities);@import "tailwindcss/utilities.css" layer(utilities) important;
```

마찬가지로 `theme(static)`와 `theme(inline)`은 생성되는 theme 변수를 변경하므로 `theme.css` import에 배치해야 합니다:

CSS

```
    @layer theme, base, components, utilities;@import "tailwindcss/theme.css" layer(theme);@import "tailwindcss/theme.css" layer(theme) theme(static);@import "tailwindcss/utilities.css" layer(utilities);
```

마지막으로 `prefix(tw)`로 prefix를 사용하면 유틸리티와 변수 모두에 영향을 주므로 두 import 모두에 지정해야 합니다:

CSS

```
    @layer theme, base, components, utilities;@import "tailwindcss/theme.css" layer(theme);@import "tailwindcss/utilities.css" layer(utilities);@import "tailwindcss/theme.css" layer(theme) prefix(tw);@import "tailwindcss/utilities.css" layer(utilities) prefix(tw);
```
