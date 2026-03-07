---
title: "업그레이드 가이드 - 시작하기 - Tailwind CSS"
description: "Tailwind CSS v4.0은 프레임워크의 새로운 메이저 버전입니다. 호환성이 깨지는 변경 사항을 최소화하기 위해 많은 노력을 기울였지만, 일부 업데이트는 필요합니다. 이 가이드는 프로젝트를 v3에서 v4로 업그레이드할 때 필요한 모든 단계를 설명합니다."
---

출처 URL: https://tailwindcss.com/docs/upgrade-guide

# 업그레이드 가이드 - 시작하기 - Tailwind CSS

Tailwind CSS v4.0은 프레임워크의 새로운 메이저 버전입니다. 호환성이 깨지는 변경 사항을 최소화하기 위해 많은 노력을 기울였지만, 일부 업데이트는 필요합니다. 이 가이드는 프로젝트를 v3에서 v4로 업그레이드할 때 필요한 모든 단계를 설명합니다.

**Tailwind CSS v4.0은 Safari 16.4+, Chrome 111+, Firefox 128+를 대상으로 설계되었습니다.** 구형 브라우저를 지원해야 한다면 브라우저 지원 요구 사항이 바뀔 때까지 v3.4를 계속 사용하세요.

## 업그레이드 도구 사용하기

프로젝트를 v3에서 v4로 업그레이드하려면, 업그레이드 도구를 사용해 대부분의 작업을 자동으로 처리할 수 있습니다.

터미널

```
    $ npx @tailwindcss/upgrade
```

대부분의 프로젝트에서 업그레이드 도구는 의존성 업데이트, 설정 파일의 CSS 마이그레이션, 템플릿 파일 변경 처리까지 포함해 전체 마이그레이션 과정을 자동화합니다.

업그레이드 도구는 Node.js 20 이상이 필요하므로, 실행 전에 환경이 업데이트되어 있는지 확인하세요.

**새 브랜치에서 업그레이드 도구를 실행한 뒤** diff를 꼼꼼히 검토하고 브라우저에서 프로젝트를 테스트해 모든 변경 사항이 올바르게 보이는지 확인하는 것을 권장합니다. 복잡한 프로젝트에서는 일부를 수동으로 조정해야 할 수 있지만, 어떤 경우든 도구가 시간을 크게 절약해 줍니다.

또한 v4의 [호환성 깨짐 변경 사항](https://tailwindcss.com/docs/upgrade-guide#changes-from-v3)을 모두 확인해 무엇이 바뀌었는지 충분히 이해해 두는 것이 좋습니다. 업그레이드 도구가 놓치는 항목이 프로젝트에 있을 수 있기 때문입니다.

## 수동으로 업그레이드하기

- PostCSS 사용 시

v3에서는 `tailwindcss` 패키지가 PostCSS 플러그인이었지만, v4에서는 PostCSS 플러그인이 전용 `@tailwindcss/postcss` 패키지로 분리되었습니다.

또한 v4에서는 import와 vendor prefix 처리가 자동으로 이루어지므로, 프로젝트에 `postcss-import`와 `autoprefixer`가 있다면 제거할 수 있습니다.

postcss.config.mjs

```
    export default {  plugins: {    "postcss-import": {},    tailwindcss: {},    autoprefixer: {},    "@tailwindcss/postcss": {},  },};
```

- Vite 사용 시

Vite를 사용 중이라면 성능 향상과 최적의 개발자 경험을 위해 PostCSS 플러그인에서 새로운 전용 Vite 플러그인으로 마이그레이션하는 것을 권장합니다.

vite.config.ts

```
    import { defineConfig } from "vite";import tailwindcss from "@tailwindcss/vite";export default defineConfig({  plugins: [    tailwindcss(),  ],});
```

- Tailwind CLI 사용 시

v4에서는 Tailwind CLI가 전용 `@tailwindcss/cli` 패키지로 분리되었습니다. 빌드 명령을 새 패키지를 사용하도록 업데이트하세요.

터미널

```
    npx tailwindcss -i input.css -o output.cssnpx @tailwindcss/cli -i input.css -o output.css
```

## v3에서 변경된 사항

다음은 Tailwind CSS v4.0의 모든 호환성 깨짐 변경 사항을 종합한 목록입니다.

[업그레이드 도구](https://tailwindcss.com/docs/upgrade-guide#using-the-upgrade-tool)가 이 변경 사항 대부분을 자동으로 처리하므로, 가능하다면 사용하는 것을 강력히 권장합니다.

- 브라우저 요구 사항

Tailwind CSS v4.0은 최신 브라우저를 대상으로 하며 Safari 16.4, Chrome 111, Firefox 128을 타깃으로 합니다. 핵심 프레임워크 기능을 위해 `@property`, `color-mix()` 같은 최신 CSS 기능에 의존하므로, Tailwind CSS v4.0은 구형 브라우저에서 동작하지 않습니다.

구형 브라우저 지원이 필요하다면 당분간 v3.4를 계속 사용하는 것을 권장합니다. 더 빠른 업그레이드를 돕기 위한 호환 모드를 적극적으로 검토 중이며, 앞으로 더 많은 소식을 공유할 예정입니다.

- @tailwind 지시어 제거

v4에서는 v3에서 사용하던 `@tailwind` 지시어 대신 일반 CSS `@import` 문으로 Tailwind를 가져옵니다.

CSS

```
    @tailwind base;@tailwind components;@tailwind utilities;@import "tailwindcss";
```

- 사용 중단된 유틸리티 제거

v3에서 이미 사용 중단되었고 수년간 문서화되지 않았던 유틸리티를 제거했습니다. 아래는 제거된 항목과 최신 대체안입니다.

| 사용 중단               | 대체                                              |
| ----------------------- | ------------------------------------------------- |
| `bg-opacity-*`          | `bg-black/50` 같은 opacity modifier 사용          |
| `text-opacity-*`        | `text-black/50` 같은 opacity modifier 사용        |
| `border-opacity-*`      | `border-black/50` 같은 opacity modifier 사용      |
| `divide-opacity-*`      | `divide-black/50` 같은 opacity modifier 사용      |
| `ring-opacity-*`        | `ring-black/50` 같은 opacity modifier 사용        |
| `placeholder-opacity-*` | `placeholder-black/50` 같은 opacity modifier 사용 |
| `flex-shrink-*`         | `shrink-*`                                        |
| `flex-grow-*`           | `grow-*`                                          |
| `overflow-ellipsis`     | `text-ellipsis`                                   |
| `decoration-slice`      | `box-decoration-slice`                            |
| `decoration-clone`      | `box-decoration-clone`                            |

- 유틸리티 이름 변경

v4에서는 일관성과 예측 가능성을 높이기 위해 다음 유틸리티 이름을 변경했습니다.

| v3                 | v4                 |
| ------------------ | ------------------ |
| `shadow-sm`        | `shadow-xs`        |
| `shadow`           | `shadow-sm`        |
| `drop-shadow-sm`   | `drop-shadow-xs`   |
| `drop-shadow`      | `drop-shadow-sm`   |
| `blur-sm`          | `blur-xs`          |
| `blur`             | `blur-sm`          |
| `backdrop-blur-sm` | `backdrop-blur-xs` |
| `backdrop-blur`    | `backdrop-blur-sm` |
| `rounded-sm`       | `rounded-xs`       |
| `rounded`          | `rounded-sm`       |
| `outline-none`     | `outline-hidden`   |
| `ring`             | `ring-3`           |

#

- 그림자, 반경, 블러 스케일 업데이트

모든 유틸리티에 명명된 값을 가지도록 기본 그림자, 반경, 블러 스케일의 이름을 변경했습니다. 이전 버전 호환을 위해 "bare" 버전도 여전히 동작하지만, 해당 `_< utility>_-sm` 유틸리티를 각 `_< utility>_-xs` 버전으로 바꾸지 않으면 모양이 달라집니다.

이 변경에 맞게 프로젝트를 업데이트하려면 모든 v3 유틸리티를 v4 버전으로 교체하세요.

HTML

```
    <input class="shadow-sm" /><input class="shadow-xs" /><input class="shadow" /><input class="shadow-sm" />
```

#

- `outline` 유틸리티 이름 변경

이제 `outline` 유틸리티는 border 및 ring 유틸리티와의 일관성을 위해 기본적으로 `outline-width: 1px`를 설정합니다. 또한 모든 `outline-<number>` 유틸리티는 기본 `outline-style`을 `solid`로 설정하므로 `outline`과 함께 조합할 필요가 없습니다.

HTML

```
    <input class="outline outline-2" /><input class="outline-2" />
```

기존 `outline-none` 유틸리티는 실제로 `outline-style: none`을 설정하지 않았고, 접근성을 위해 강제 색상 모드에서 여전히 보이는 보이지 않는 outline을 설정했습니다.

이를 더 명확히 하기 위해 이 유틸리티 이름을 `outline-hidden`으로 변경했고, 실제로 `outline-style: none`을 설정하는 새로운 `outline-none` 유틸리티를 추가했습니다.

이 변경에 맞게 프로젝트를 업데이트하려면 `outline-none` 사용을 모두 `outline-hidden`으로 교체하세요.

HTML

```
    <input class="focus:outline-none" /><input class="focus:outline-hidden" />
```

#

- 기본 ring 너비 변경

v3에서 `ring` 유틸리티는 `3px` ring을 추가했습니다. v4에서는 border 및 outline과 일관되도록 이를 `1px`로 변경했습니다.

이 변경에 맞게 프로젝트를 업데이트하려면 `ring` 사용을 모두 `ring-3`로 교체하세요.

HTML

```
    <input class="ring ring-blue-500" /><input class="ring-3 ring-blue-500" />
```

- 요소 간 간격 선택자

대규모 페이지에서의 심각한 성능 문제를 해결하기 위해 [`space-x-*` 및 `space-y-*` 유틸리티](https://tailwindcss.com/docs/margin#adding-space-between-children)에 사용되는 선택자를 변경했습니다.

CSS

```
    /* Before */.space-y-4 > :not([hidden]) ~ :not([hidden]) {  margin-top: 1rem;}/* Now */.space-y-4 > :not(:last-child) {  margin-bottom: 1rem;}
```

프로젝트에서 이 유틸리티를 인라인 요소와 함께 사용했거나, 자식 요소 간격을 조정하려고 다른 margin을 추가했다면 변화가 보일 수 있습니다.

이 변경으로 문제가 생기면 flex 또는 grid 레이아웃으로 마이그레이션하고 `gap`을 사용하는 것을 권장합니다.

HTML

```
    <div class="space-y-4 p-4"><div class="flex flex-col gap-4 p-4">  <label for="name">Name</label>  <input type="text" name="name" /></div>
```

- Divide 선택자

대규모 페이지에서의 심각한 성능 문제를 해결하기 위해 [`divide-x-*` 및 `divide-y-*` 유틸리티](https://tailwindcss.com/docs/border-width#between-children)에 사용되는 선택자를 변경했습니다.

CSS

```
    /* Before */.divide-y-4 > :not([hidden]) ~ :not([hidden]) {  border-top-width: 4px;}/* Now */.divide-y-4 > :not(:last-child) {  border-bottom-width: 4px;}
```

이 유틸리티를 인라인 요소와 함께 사용했거나, 자식 요소의 간격을 조정하려고 다른 margin/padding을 추가했거나, 특정 자식 요소의 border를 조정했다면 프로젝트에서 변화가 보일 수 있습니다.

- 그라디언트에서 variant 사용

v3에서는 variant로 그라디언트의 일부를 재정의하면 전체 그라디언트가 "리셋"되어, 아래 예시에서는 다크 모드에서 `to-*` 색상이 노란색이 아닌 투명색이 되었습니다.

HTML

```
    <div class="bg-gradient-to-r from-red-500 to-yellow-400 dark:from-blue-500">  <!-- ... --></div>
```

v4에서는 이 값들이 유지되며, 이는 Tailwind의 다른 유틸리티 동작 방식과 더 일관됩니다.

즉, 특정 상태에서 3단계 그라디언트를 다시 2단계로 "해제"하려면 `via-none`을 명시적으로 사용해야 할 수 있습니다.

HTML

```
    <div class="bg-linear-to-r from-red-500 via-orange-400 to-yellow-400 dark:via-none dark:from-blue-500 dark:to-teal-400">  <!-- ... --></div>
```

- Container 설정

v3의 `container` 유틸리티에는 `center`, `padding` 같은 여러 설정 옵션이 있었지만 v4에서는 더 이상 존재하지 않습니다.

v4에서 `container` 유틸리티를 커스터마이즈하려면 `@utility` 지시어로 확장하세요.

CSS

```
    @utility container {  margin-inline: auto;  padding-inline: 2rem;}
```

- 기본 border 색상

v3에서 `border-*`, `divide-*` 유틸리티는 기본적으로 설정된 `gray-200` 색상을 사용했습니다. v4에서는 Tailwind의 기본 의견을 줄이고 브라우저 기본값과 맞추기 위해 이를 `currentColor`로 변경했습니다.

이 변경에 맞게 프로젝트를 업데이트하려면 `border-*` 또는 `divide-*` 유틸리티를 사용하는 모든 곳에서 색상을 명시하세요.

```
    <div class="border border-gray-200 px-2 py-3 ...">  <!-- ... --></div>
```

또는 v3 동작을 유지하려면 다음 base 스타일을 프로젝트에 추가하세요.

CSS

```
    @layer base {  *,  ::after,  ::before,  ::backdrop,  ::file-selector-button {    border-color: var(--color-gray-200, currentColor);  }}
```

- 기본 ring 너비 및 색상

`border-*`, `divide-*`, `outline-*` 유틸리티와 더 일관되도록 `ring` 유틸리티의 너비를 3px에서 1px로, 기본 색상을 `blue-500`에서 `currentColor`로 변경했습니다.

이 변경에 맞게 프로젝트를 업데이트하려면 `ring` 사용을 모두 `ring-3`로 교체하세요.

```
    <button class="focus:ring ..."><button class="focus:ring-3 ...">  <!-- ... --></button>
```

그다음 기본 ring 색상에 의존하던 모든 위치에 `ring-blue-500`을 추가하세요.

```
    <button class="focus:ring-3 focus:ring-blue-500 ...">  <!-- ... --></button>
```

또는 v3 동작을 유지하려면 다음 테마 변수를 CSS에 추가하세요.

CSS

```
    @theme {  --default-ring-width: 3px;  --default-ring-color: var(--color-blue-500);}
```

다만 이 변수들은 호환성 목적으로만 지원되며, Tailwind CSS v4.0의 관용적인 사용 방식으로 간주되지는 않습니다.

- Preflight 변경 사항

v4의 Preflight base 스타일에 몇 가지 작은 변경이 있습니다.

#

- 새로운 기본 placeholder 색상

v3에서 placeholder 텍스트는 기본적으로 설정된 `gray-400` 색상을 사용했습니다. v4에서는 이를 단순화해 현재 텍스트 색상을 50% 불투명도로 사용합니다.

대부분 이 변경을 거의 알아차리지 못할 가능성이 높고(오히려 더 보기 좋아질 수도 있습니다), v3 동작을 유지하고 싶다면 다음 CSS를 프로젝트에 추가하세요.

CSS

```
    @layer base {  input::placeholder,  textarea::placeholder {    color: var(--color-gray-400);  }}
```

#

- 버튼이 기본 커서 사용

이제 버튼은 기본 브라우저 동작과 맞추기 위해 `cursor: pointer` 대신 `cursor: default`를 사용합니다.

기본적으로 `cursor: pointer`를 계속 사용하고 싶다면 다음 base 스타일을 CSS에 추가하세요.

CSS

```
    @layer base {  button:not(:disabled),  [role="button"]:not(:disabled) {    cursor: pointer;  }}
```

#

- Dialog margin 제거

이제 Preflight는 다른 요소 reset과 일관되도록 `<dialog>` 요소의 margin도 reset합니다.

여전히 dialog를 기본적으로 가운데 정렬하고 싶다면 다음 CSS를 프로젝트에 추가하세요.

CSS

```
    @layer base {  dialog {    margin: auto;  }}
```

#

- `hidden` attribute 우선 적용

`block`, `flex` 같은 display 클래스는 더 이상 요소의 `hidden` attribute보다 우선하지 않습니다. 사용자에게 요소를 보이게 하려면 `hidden` attribute를 제거하세요. 이는 `hidden="until-found"`에는 적용되지 않습니다.

- prefix 사용

이제 prefix는 variant처럼 보이며 항상 클래스 이름의 맨 앞에 옵니다.

```
    <div class="tw:flex tw:bg-red-500 tw:hover:bg-red-600">  <!-- ... --></div>
```

prefix를 사용할 때도, prefix를 사용하지 않는 것처럼 테마 변수를 설정해야 합니다.

```
    @import "tailwindcss" prefix(tw);@theme {  --font-display: "Satoshi", "sans-serif";  --breakpoint-3xl: 120rem;  --color-avocado-100: oklch(0.99 0 0);  --color-avocado-200: oklch(0.98 0.04 113.22);  --color-avocado-300: oklch(0.94 0.11 115.03);  /* ... */}
```

생성된 CSS 변수에는 프로젝트의 기존 변수와 충돌을 피하기 위해 prefix가 _포함됩니다_.

```
    :root {  --tw-font-display: "Satoshi", "sans-serif";  --tw-breakpoint-3xl: 120rem;  --tw-color-avocado-100: oklch(0.99 0 0);  --tw-color-avocado-200: oklch(0.98 0.04 113.22);  --tw-color-avocado-300: oklch(0.94 0.11 115.03);  /* ... */}
```

- 중요도 modifier

v3에서는 유틸리티 이름 앞(variant 뒤)에 `!`를 두어 중요도를 지정할 수 있었습니다. v4에서는 `!`를 클래스 이름의 맨 끝에 두어야 합니다.

```
    <div class="flex! bg-red-500! hover:bg-red-600/50!">  <!-- ... --></div>
```

이전 방식도 호환성을 위해 여전히 지원되지만 사용 중단 예정입니다.

- 커스텀 유틸리티 추가

v3에서는 `@layer utilities` 또는 `@layer components` 안에서 정의한 커스텀 클래스가 Tailwind에서 실제 유틸리티 클래스로 인식되어 `hover`, `focus`, `lg` 같은 variant와 자동으로 동작했습니다. 차이는 `@layer components`가 생성된 스타일시트에서 항상 먼저 온다는 점이었습니다.

v4에서는 네이티브 cascade layer를 사용하고 더 이상 `@layer` at-rule을 가로채지 않으므로, 대체로 `@utility` API를 도입했습니다.

CSS

```
    @layer utilities {  .tab-4 {    tab-size: 4;  }}@utility tab-4 {  tab-size: 4;}
```

이제 커스텀 유틸리티도 정의한 속성 수를 기준으로 정렬됩니다. 즉, 이런 `.btn` 같은 컴포넌트 유틸리티는 추가 설정 없이 다른 Tailwind 유틸리티로 덮어쓸 수 있습니다.

CSS

```
    @layer components {  .btn {    border-radius: 0.5rem;    padding: 0.5rem 1rem;    background-color: ButtonFace;  }}@utility btn {  border-radius: 0.5rem;  padding: 0.5rem 1rem;  background-color: ButtonFace;}
```

[사용자 정의 유틸리티 추가 문서](https://tailwindcss.com/docs/adding-custom-styles#adding-custom-utilities)에서 사용자 정의 유틸리티 등록에 대해 더 알아보세요.

- Variant 스태킹 순서

v3에서는 스택된 variant가 오른쪽에서 왼쪽으로 적용되었지만, v4에서는 CSS 문법과 더 유사하게 보이도록 왼쪽에서 오른쪽으로 적용되도록 변경되었습니다.

이 변경에 맞게 프로젝트를 업데이트하려면, 순서에 민감한 스택 variant의 순서를 반대로 바꾸세요:

HTML

```
    <ul class="py-4 first:*:pt-0 last:*:pb-0"><ul class="py-4 *:first:pt-0 *:last:pb-0">  <li>One</li>  <li>Two</li>  <li>Three</li></ul>
```

해당 경우는 거의 없거나 아주 적을 가능성이 큽니다. 직접 자식 variant(`*`)와 타이포그래피 플러그인 variant(`prose-headings`)가 가장 가능성이 높고, 그마저도 다른 variant와 함께 스택해서 사용한 경우에만 해당됩니다.

- 임의 값(arbitrary values)에서의 변수

v3에서는 `var()` 없이도 CSS 변수를 임의 값으로 사용할 수 있었지만, 최근 CSS 업데이트로 인해 이 방식은 종종 모호해질 수 있습니다. 그래서 v4에서는 대괄호 대신 소괄호를 사용하는 문법으로 변경되었습니다.

이 변경에 맞게 프로젝트를 업데이트하려면, 기존 변수 축약 문법 사용을 새 변수 축약 문법으로 바꾸세요:

HTML

```
    <div class="bg-[--brand-color]"></div><div class="bg-(--brand-color)"></div>
```

- `grid` 및 `object-position` 유틸리티의 임의 값

이전에는 임의 값 내부의 `grid-cols-*`, `grid-rows-*`, `object-*` 유틸리티에서 쉼표가 공백으로 치환되었습니다. 이 특수 동작은 v2와의 호환성을 위해 Tailwind CSS v3에 존재했습니다. v4.0에서는 이 호환성이 제거되었으며, 공백을 나타내기 위해 밑줄을 사용해야 합니다.

이 변경에 맞게 프로젝트를 업데이트하려면, 공백 의미로 사용하던 쉼표를 밑줄로 바꾸세요:

HTML

```
    <div class="grid-cols-[max-content,auto]"></div><div class="grid-cols-[max-content_auto]"></div>
```

- 모바일에서의 hover 스타일

v4에서는 기본 입력 장치가 hover를 지원할 때만 `hover` variant가 적용되도록 변경되었습니다:

CSS

```
    @media (hover: hover) {  .hover\:underline:hover {    text-decoration: underline;  }}
```

탭 시 hover가 트리거되는 터치 디바이스 동작에 의존하도록 사이트를 구성했다면 문제가 생길 수 있습니다. 이게 문제라면, 기존 구현을 사용하는 사용자 정의 variant로 `hover` variant를 재정의할 수 있습니다:

CSS

```
    @custom-variant hover (&:hover);
```

다만 일반적으로는 hover 기능을 보조적 향상(enhancement)으로 취급하고, 사이트 동작이 이에 의존하지 않도록 권장합니다. 터치 디바이스는 실제 hover 기능을 갖고 있지 않기 때문입니다.

- `outline-color` 전환(transition)

이제 `transition` 및 `transition-colors` 유틸리티에 `outline-color` 속성이 포함됩니다.

즉, 포커스 시 사용자 정의 색상 outline을 추가하고 있었다면 기본 색상에서 해당 색상으로 전환되는 효과가 보일 수 있습니다. 이를 피하려면 outline 색상을 항상 설정하거나, 두 상태 모두에 명시적으로 설정하세요:

HTML

```
    <button class="transition hover:outline-2 hover:outline-cyan-500"></button><button class="outline-cyan-500 transition hover:outline-2"></button>
```

- 개별 transform 속성

이제 `rotate-*`, `scale-*`, `translate-*` 유틸리티는 CSS의 개별 `rotate`, `scale`, `translate` 속성을 기반으로 합니다. 일반적으로 동작에는 영향이 없지만, 주의할 몇 가지 경우가 있습니다:

#

- Transform 초기화

기존에는 `transform-none`으로 `rotate`, `scale`, `translate` 유틸리티를 “초기화”할 수 있었습니다. 이제는 더 이상 동작하지 않으며, 개별 속성을 각각 초기화해야 합니다:

HTML

```
    <button class="scale-150 focus:transform-none"></button><button class="scale-150 focus:scale-none"></button>
```

#

- Transition

전환 대상 속성 목록을 커스터마이즈하면서 `transform`을 포함한 경우(예: `transition-[opacity,transform]`) 이제 이러한 유틸리티는 전환되지 않습니다. 해결하려면 목록에 개별 속성을 포함하세요. 예를 들어 `opacity-*`와 `scale-*` 유틸리티를 사용할 때 변경 사항을 전환하려면 `transition-[opacity,scale]`를 사용해야 합니다.

HTML

```
    <button class="transition-[opacity,transform] hover:scale-150"></button><button class="transition-[opacity,scale] hover:scale-150"></button>
```

- 코어 플러그인 비활성화

v3에는 프레임워크 내 특정 유틸리티를 완전히 비활성화할 수 있는 `corePlugins` 옵션이 있었습니다. v4에서는 더 이상 지원되지 않습니다.

- `theme()` 함수 사용

v4에서는 모든 테마 값에 대해 CSS 변수를 제공하므로, 가능하다면 `theme()` 함수 대신 해당 변수를 사용하는 것을 권장합니다:

CSS

```
    .my-class {  background-color: theme(colors.red.500);  background-color: var(--color-red-500);}
```

여전히 `theme()` 함수를 사용해야 하는 경우(예: CSS 변수가 지원되지 않는 미디어 쿼리)에는 기존 점 표기법 대신 CSS 변수 이름을 사용해야 합니다:

CSS

```
    @media (width >= theme(screens.xl)) {@media (width >= theme(--breakpoint-xl)) {  /* ... */}
```

- JavaScript config 파일 사용

JavaScript config 파일은 하위 호환성을 위해 여전히 지원되지만, v4에서는 더 이상 자동으로 감지되지 않습니다.

여전히 JavaScript config 파일을 사용해야 한다면 `@config` 지시어를 사용해 명시적으로 로드할 수 있습니다:

CSS

```
    @config "../../tailwind.config.js";
```

JavaScript 기반 config의 `corePlugins`, `safelist`, `separator` 옵션은 v4.0에서 지원되지 않습니다. v4에서 유틸리티를 safelist 처리하려면 [`@source inline()`](https://tailwindcss.com/docs/detecting-classes-in-source-files#safelisting-specific-utilities)을 사용하세요.

- JavaScript에서의 테마 값

v3에서는 JavaScript 기반 config를 다른 JavaScript에서 사용할 수 있는 평탄한 객체로 변환하는 `resolveConfig` 함수를 내보냈습니다.

v4에서는 대신 우리가 생성하는 CSS 변수를 직접 사용하길 바라는 취지에서 이를 제거했습니다. 이 방식이 훨씬 단순하며 번들 크기도 크게 줄여줍니다.

예를 들어 React의 인기 라이브러리 [Motion](https://motion.dev/docs/react-quick-start)은 CSS 변수 값을 기준으로 애니메이션의 시작/종료를 지정할 수 있습니다:

JSX

```
    <motion.div animate={{ backgroundColor: "var(--color-blue-500)" }} />
```

JS에서 해석된 CSS 변수 값이 필요하다면 `getComputedStyle`을 사용해 문서 루트의 테마 변수 값을 가져올 수 있습니다:

spaghetti.js

```
    let styles = getComputedStyle(document.documentElement);let shadow = styles.getPropertyValue("--shadow-xl");
```

- Vue, Svelte, CSS modules에서 `@apply` 사용

v4에서는 메인 CSS 파일과 별도로 번들되는 스타일시트(예: CSS modules 파일, Vue/Svelte/Astro의 `<style>` 블록 등)가 다른 파일에 정의된 테마 변수, 사용자 정의 유틸리티, 사용자 정의 variant에 접근할 수 없습니다.

이런 컨텍스트에서 해당 정의를 사용할 수 있게 하려면, [`@reference`](https://tailwindcss.com/docs/functions-and-directives#reference-directive)를 사용해 번들에 CSS를 중복 추가하지 않고 가져오세요:

Vue

```
    <template>  <h1>Hello world!</h1></template><style>  @reference "../../app.css";  h1 {    @apply text-2xl font-bold text-red-500;  }</style>
```

또는 `@apply`를 전혀 사용하지 않고 CSS 테마 변수를 직접 사용할 수도 있습니다. 이 경우 Tailwind가 해당 스타일을 처리할 필요가 없어 성능도 향상됩니다:

Vue

```
    <template>  <h1>Hello world!</h1></template><style>  h1 {    color: var(--text-red-500);  }</style>
```

[CSS modules와 함께 Tailwind 사용하기](https://tailwindcss.com/docs/compatibility#css-modules) 문서에서 더 자세히 확인할 수 있습니다.

- Sass, Less, Stylus 사용

Tailwind CSS v4.0은 Sass, Less, Stylus 같은 CSS 전처리기와 함께 사용하도록 설계되지 않았습니다. Tailwind CSS 자체를 전처리기라고 생각하면 됩니다. Sass와 Stylus를 함께 쓰지 않는 것과 같은 이유로 Tailwind와 Sass를 함께 쓰지 않아야 합니다. 따라서 스타일시트나 Vue/Svelte/Astro 등의 `<style>` 블록에서 Sass, Less, Stylus를 사용하는 것은 불가능합니다.

[호환성 문서](https://tailwindcss.com/docs/compatibility#sass-less-and-stylus)에서 더 알아보세요.
