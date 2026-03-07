---
title: "함수와 지시어 - 핵심 개념 - Tailwind CSS"
description: "지시어는 Tailwind CSS 프로젝트에서 특별한 기능을 제공하는, CSS에서 사용할 수 있는 Tailwind 전용 사용자 정의 at-rules입니다."
---

출처 URL: https://tailwindcss.com/docs/functions-and-directives

# 함수와 지시어 - 핵심 개념 - Tailwind CSS

## 지시어

지시어는 Tailwind CSS 프로젝트에서 특별한 기능을 제공하는, CSS에서 사용할 수 있는 Tailwind 전용 사용자 정의 [at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/At-rule)입니다.

- @import

`@import` 지시어를 사용하면 Tailwind 자체를 포함한 CSS 파일을 인라인으로 가져올 수 있습니다:

CSS

```
    @import "tailwindcss";
```

- @theme

`@theme` 지시어를 사용해 폰트, 색상, 브레이크포인트 같은 프로젝트의 사용자 정의 디자인 토큰을 정의할 수 있습니다:

CSS

```
    @theme {  --font-display: "Satoshi", "sans-serif";  --breakpoint-3xl: 120rem;  --color-avocado-100: oklch(0.99 0 0);  --color-avocado-200: oklch(0.98 0.04 113.22);  --color-avocado-300: oklch(0.94 0.11 115.03);  --color-avocado-400: oklch(0.92 0.19 114.08);  --color-avocado-500: oklch(0.84 0.18 117.33);  --color-avocado-600: oklch(0.53 0.12 118.34);  --ease-fluid: cubic-bezier(0.3, 0, 0, 1);  --ease-snappy: cubic-bezier(0.2, 0, 0, 1);  /* ... */}
```

[테마 변수 문서](https://tailwindcss.com/docs/theme)에서 테마 커스터마이징에 대해 더 알아보세요.

- @source

`@source` 지시어를 사용하면 Tailwind의 자동 콘텐츠 감지에서 잡아내지 못하는 소스 파일을 명시적으로 지정할 수 있습니다:

CSS

```
    @source "../node_modules/@my-company/ui-lib";
```

[소스 파일에서 클래스 감지 문서](https://tailwindcss.com/docs/detecting-classes-in-source-files)에서 자동 콘텐츠 감지에 대해 더 알아보세요.

- @utility

`@utility` 지시어를 사용하면 `hover`, `focus`, `lg` 같은 variant와 함께 동작하는 사용자 정의 유틸리티를 프로젝트에 추가할 수 있습니다:

CSS

```
    @utility tab-4 {  tab-size: 4;}
```

[사용자 정의 유틸리티 추가 문서](https://tailwindcss.com/docs/adding-custom-styles#adding-custom-utilities)에서 사용자 정의 유틸리티 등록에 대해 더 알아보세요.

- @variant

`@variant` 지시어를 사용해 CSS의 스타일에 Tailwind variant를 적용할 수 있습니다:

CSS

```
    .my-element {  background: white;  @variant dark {    background: black;  }}
```

[variant 사용 문서](https://tailwindcss.com/docs/adding-custom-styles#using-variants)에서 variant 사용법을 더 알아보세요.

- @custom-variant

`@custom-variant` 지시어를 사용하면 프로젝트에 사용자 정의 variant를 추가할 수 있습니다:

CSS

```
    @custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

이를 통해 `theme-midnight:bg-black`, `theme-midnight:text-white` 같은 유틸리티를 작성할 수 있습니다.

[사용자 정의 variant 추가 문서](https://tailwindcss.com/docs/adding-custom-styles#adding-custom-variants)에서 자세히 알아보세요.

- @apply

`@apply` 지시어를 사용하면 기존 유틸리티 클래스를 사용자 정의 CSS에 인라인으로 적용할 수 있습니다:

CSS

```
    .select2-dropdown {  @apply rounded-b-lg shadow-md;}.select2-search {  @apply rounded border border-gray-300;}.select2-results__group {  @apply text-lg font-bold text-gray-900;}
```

이 기능은 사용자 정의 CSS(예: 서드파티 라이브러리의 스타일 오버라이드)를 작성해야 하지만, 디자인 토큰을 계속 활용하고 HTML에서 익숙하게 쓰던 동일한 문법을 유지하고 싶을 때 유용합니다.

- @reference

Vue 또는 Svelte 컴포넌트의 `<style>` 블록이나 CSS 모듈 안에서 `@apply` 또는 `@variant`를 사용하려면, 해당 컨텍스트에서 값을 사용할 수 있도록 테마 변수, 사용자 정의 유틸리티, 사용자 정의 variant를 가져와야 합니다.

출력 CSS를 중복시키지 않고 이를 수행하려면, 스타일을 실제로 포함하지 않고 참조만 하도록 `@reference` 지시어로 메인 스타일시트를 가져오세요:

Vue

```
    <template>  <h1>Hello world!</h1></template><style>  @reference "../../app.css";  h1 {    @apply text-2xl font-bold text-red-500;  }</style>
```

사용자 정의 없이 기본 테마만 사용하는 경우(예: `@theme`, `@custom-variant`, `@plugin` 등을 사용하지 않는 경우), `tailwindcss`를 직접 가져올 수 있습니다:

Vue

```
    <template>  <h1>Hello world!</h1></template><style>  @reference "tailwindcss";  h1 {    @apply text-2xl font-bold text-red-500;  }</style>
```

- 서브패스 Import

CLI, Vite, PostCSS를 사용할 때 `@import`, `@reference`, `@plugin`, `@config` 지시어는 모두 번들러 및 TypeScript 경로 별칭과 유사하게 동작하는 [서브패스 import](https://nodejs.org/api/packages.html#subpath-imports)를 지원합니다:

package.json

```
    {  // ...  "imports": {    "#app.css": "./src/css/app.css"  }}
```

Vue

```
    <template>  <h1>Hello world!</h1></template><style>  @reference "#app.css";  h1 {    @apply text-2xl font-bold text-red-500;  }</style>
```

## 함수

Tailwind는 색상 및 간격 스케일을 더 쉽게 다룰 수 있도록 다음과 같은 빌드 타임 함수를 제공합니다.

- --alpha()

`--alpha()` 함수를 사용해 색상의 불투명도를 조정할 수 있습니다:

Input CSS

```
    .my-element {  color: --alpha(var(--color-lime-300) / 50%);}
```

Compiled CSS

```
    .my-element {  color: color-mix(in oklab, var(--color-lime-300) 50%, transparent);}
```

- --spacing()

`--spacing()` 함수를 사용하면 테마를 기반으로 간격 값을 생성할 수 있습니다:

Input CSS

```
    .my-element {  margin: --spacing(4);}
```

Compiled CSS

```
    .my-element {  margin: calc(var(--spacing) * 4);}
```

이는 임의 값에서도 유용하며, 특히 `calc()`와 함께 사용할 때 더욱 유용합니다:

HTML

```
    <div class="py-[calc(--spacing(4)-1px)]">  <!-- ... --></div>
```

## 호환성

아래 지시어와 함수는 Tailwind CSS v3.x와의 호환성을 위해서만 존재합니다.

`@config` 및 `@plugin` 지시어는 `@theme`, `@utility` 및 기타 CSS 기반 기능과 함께 사용할 수 있습니다. 이를 통해 테마, 사용자 정의 설정, 유틸리티, variant, preset을 CSS로 점진적으로 이전할 수 있습니다. CSS에 정의된 항목은 가능한 경우 병합되고, 그렇지 않으면 config, preset, plugin에 정의된 항목보다 우선 적용됩니다.

- @config

`@config` 지시어를 사용해 레거시 JavaScript 기반 설정 파일을 로드할 수 있습니다:

CSS

```
    @config "../../tailwind.config.js";
```

JavaScript 기반 config의 `corePlugins`, `safelist`, `separator` 옵션은 v4.0에서 지원되지 않습니다. v4에서 유틸리티를 safelist 하려면 [`@source inline()`](https://tailwindcss.com/docs/detecting-classes-in-source-files#safelisting-specific-utilities)을 사용하세요.

- @plugin

`@plugin` 지시어를 사용해 레거시 JavaScript 기반 plugin을 로드할 수 있습니다:

CSS

```
    @plugin "@tailwindcss/typography";
```

`@plugin` 지시어는 패키지 이름 또는 로컬 경로를 받을 수 있습니다.

- theme()

`theme()` 함수를 사용하면 점 표기법으로 Tailwind 테마 값에 접근할 수 있습니다:

CSS

```
    .my-element {  margin: theme(spacing.12);}
```

이 함수는 더 이상 권장되지 않으며, 대신 [CSS 테마 변수 사용](https://tailwindcss.com/docs/theme#using-your-theme-variables)을 권장합니다.
