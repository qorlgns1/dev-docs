---
title: "사용자 정의 스타일 추가 - 핵심 개념 - Tailwind CSS"
description: "프레임워크로 작업할 때 가장 큰 과제는, 프레임워크가 처리해 주지 않는 것이 필요할 때 무엇을 해야 하는지 파악하는 경우가 많다는 점입니다."
---

# 사용자 정의 스타일 추가 - 핵심 개념 - Tailwind CSS

프레임워크로 작업할 때 가장 큰 과제는, 프레임워크가 처리해 주지 않는 것이 필요할 때 무엇을 해야 하는지 파악하는 경우가 많다는 점입니다.

Tailwind는 처음부터 확장 가능하고 사용자 정의 가능하도록 설계되어, 무엇을 만들든 프레임워크와 씨름하고 있다는 느낌이 들지 않게 합니다.

이 가이드에서는 디자인 토큰 사용자 정의, 필요할 때 그 제약에서 벗어나는 방법, 자체 사용자 정의 CSS 추가, 플러그인으로 프레임워크 확장 같은 주제를 다룹니다.

## 테마 사용자 정의

색상 팔레트, 간격 스케일, 타이포그래피 스케일, 브레이크포인트 같은 항목을 변경하고 싶다면, CSS에서 `@theme` 지시어를 사용해 사용자 정의를 추가하세요:

CSS

```
    @theme {  --font-display: "Satoshi", "sans-serif";  --breakpoint-3xl: 120rem;  --color-avocado-100: oklch(0.99 0 0);  --color-avocado-200: oklch(0.98 0.04 113.22);  --color-avocado-300: oklch(0.94 0.11 115.03);  --color-avocado-400: oklch(0.92 0.19 114.08);  --color-avocado-500: oklch(0.84 0.18 117.33);  --color-avocado-600: oklch(0.53 0.12 118.34);  --ease-fluid: cubic-bezier(0.3, 0, 0, 1);  --ease-snappy: cubic-bezier(0.2, 0, 0, 1);  /* ... */}
```

테마 사용자 정의에 대한 자세한 내용은 [테마 변수 문서](https://tailwindcss.com/docs/theme)를 참고하세요.

## 임의 값 사용하기

제약된 디자인 토큰 집합만으로도 잘 다듬어진 디자인의 대부분을 보통 구성할 수 있지만, 가끔은 픽셀 단위로 정확히 맞추기 위해 그 제약을 벗어나야 할 때가 있습니다.

배경 이미지를 정확한 위치에 맞추기 위해 `top: 117px` 같은 값이 정말 필요하다면, Tailwind의 대괄호 표기법을 사용해 임의 값으로 클래스를 즉석에서 생성하세요:

HTML

```
    <div class="top-[117px]">  <!-- ... --></div>
```

이는 사실상 인라인 스타일과 비슷하지만, `hover` 같은 인터랙티브 modifier나 `lg` 같은 반응형 modifier와 결합할 수 있다는 큰 장점이 있습니다:

HTML

```
    <div class="top-[117px] lg:top-[344px]">  <!-- ... --></div>
```

이 방식은 배경색, 글꼴 크기, 의사 요소 콘텐츠 등 프레임워크의 모든 항목에 적용됩니다:

HTML

```
    <div class="bg-[#bada55] text-[22px] before:content-['Festivus']">  <!-- ... --></div>
```

CSS 변수를 임의 값으로 참조하는 경우에는 사용자 정의 속성 문법을 사용할 수 있습니다:

HTML

```
    <div class="fill-(--my-brand-color) ...">  <!-- ... --></div>
```

이는 `fill-[var(--my-brand-color)]`의 축약형으로, `var()` 함수를 자동으로 추가해 줍니다.

- 임의 속성

기본 제공되는 유틸리티에 Tailwind가 포함하지 않은 CSS 속성을 사용해야 한다면, 대괄호 표기법으로 완전히 임의의 CSS를 작성할 수도 있습니다:

HTML

```
    <div class="[mask-type:luminance]">  <!-- ... --></div>
```

이건 정말로 인라인 스타일과 같지만, 다시 말해 modifier를 사용할 수 있다는 장점이 있습니다:

HTML

```
    <div class="[mask-type:luminance] hover:[mask-type:alpha]">  <!-- ... --></div>
```

이는 CSS 변수처럼, 특히 조건에 따라 값이 달라져야 하는 경우에도 유용합니다:

HTML

```
    <div class="[--scroll-offset:56px] lg:[--scroll-offset:44px]">  <!-- ... --></div>
```

- 임의 variant

임의 `variant`는 임의 값과 비슷하지만, 선택자를 즉석에서 수정할 때 사용합니다. `hover:{utility}` 같은 내장 의사 클래스 variant나 `md:{utility}` 같은 반응형 variant처럼, HTML에서 대괄호 표기법으로 직접 사용할 수 있습니다.

HTML

```
    <ul role="list">  {#each items as item}  <li class="lg:[&:nth-child(-n+3)]:hover:underline">{item}</li>  {/each}</ul>
```

자세한 내용은 [임의 variant](https://tailwindcss.com/docs/hover-focus-and-other-states#using-arbitrary-variants) 문서를 참고하세요.

- 공백 처리

임의 값에 공백이 포함되어야 할 때는 대신 밑줄(`_`)을 사용하면, Tailwind가 빌드 시점에 자동으로 공백으로 변환합니다:

HTML

```
    <div class="grid grid-cols-[1fr_500px_2fr]">  <!-- ... --></div>
```

밑줄이 흔하지만 공백이 유효하지 않은 상황에서는, 예를 들어 URL처럼 Tailwind가 밑줄을 공백으로 바꾸지 않고 그대로 유지합니다:

HTML

```
    <div class="bg-[url('/what_a_rush.png')]">  <!-- ... --></div>
```

드물게 밑줄을 실제로 써야 하는데 공백도 유효해서 모호한 경우에는, 밑줄 앞에 백슬래시를 넣어 이스케이프하면 Tailwind가 공백으로 변환하지 않습니다:

HTML

```
    <div class="before:content-['hello\_world']">  <!-- ... --></div>
```

렌더링된 HTML에서 백슬래시가 제거되는 JSX 같은 환경을 사용한다면, 백슬래시가 JavaScript 이스케이프 문자로 처리되지 않도록 [String.raw()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw)를 사용하세요:

```
    <div className={String.raw`before:content-['hello\_world']`}>  <!-- ... --></div>
```

- 모호성 해결

Tailwind의 많은 유틸리티는 공통 네임스페이스를 공유하지만 서로 다른 CSS 속성에 매핑됩니다. 예를 들어 `text-lg`와 `text-black`은 모두 `text-` 네임스페이스를 공유하지만, 하나는 `font-size`, 다른 하나는 `color`에 해당합니다.

임의 값을 사용할 때 Tailwind는 일반적으로 전달한 값을 기준으로 이런 모호성을 자동으로 처리할 수 있습니다:

HTML

```
    <!-- Will generate a font-size utility --><div class="text-[22px]">...</div><!-- Will generate a color utility --><div class="text-[#bada55]">...</div>
```

하지만 CSS 변수를 사용할 때처럼 실제로 모호한 경우도 있습니다:

HTML

```
    <div class="text-(--my-var)">...</div>
```

이런 상황에서는 값 앞에 [CSS 데이터 타입](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Types)을 추가해 Tailwind에 기본 타입을 "힌트"로 줄 수 있습니다:

HTML

```
    <!-- Will generate a font-size utility --><div class="text-(length:--my-var)">...</div><!-- Will generate a color utility --><div class="text-(color:--my-var)">...</div>
```

## 사용자 정의 CSS 사용하기

Tailwind는 대부분의 스타일링 요구를 처리하도록 설계되었지만, 필요하다면 일반 CSS를 직접 작성하는 데 아무 제약이 없습니다:

CSS

```
    @import "tailwindcss";.my-custom-style {  /* ... */}
```

- 기본 스타일 추가

페이지의 기본값(텍스트 색상, 배경색, 글꼴 패밀리 등)만 설정하고 싶다면, 가장 쉬운 방법은 `html` 또는 `body` 요소에 클래스를 추가하는 것입니다:

HTML

```
    <!doctype html><html lang="en" class="bg-gray-100 font-serif text-gray-900">  <!-- ... --></html>
```

이렇게 하면 기본 스타일링 결정을 별도 파일에 숨기지 않고, 다른 스타일과 함께 마크업에 둘 수 있습니다.

특정 HTML 요소에 대한 기본 스타일을 직접 추가하고 싶다면 `@layer` 지시어를 사용해 해당 스타일을 Tailwind의 `base` 레이어에 추가하세요:

CSS

```
    @layer base {  h1 {    font-size: var(--text-2xl);  }  h2 {    font-size: var(--text-xl);  }}
```

- 컴포넌트 클래스 추가

프로젝트에 더 복잡한 클래스를 추가하면서도 유틸리티 클래스로 재정의할 수 있게 하고 싶다면 `components` 레이어를 사용하세요.

전통적으로는 `card`, `btn`, `badge` 같은 클래스가 여기에 해당합니다.

CSS

```
    @layer components {  .card {    background-color: var(--color-white);    border-radius: var(--radius-lg);    padding: --spacing(6);    box-shadow: var(--shadow-xl);  }}
```

컴포넌트 클래스를 `components` 레이어에 정의하면, 필요할 때 유틸리티 클래스로 계속 재정의할 수 있습니다:

HTML

```
    <!-- Will look like a card, but with square corners --><div class="card rounded-none">  <!-- ... --></div>
```

Tailwind를 사용하면 이런 종류의 클래스가 생각보다 자주 필요하지 않을 수 있습니다. 권장 사항은 [중복 관리](https://tailwindcss.com/docs/styling-with-utility-classes#managing-duplication) 가이드를 참고하세요.

`components` 레이어는 사용 중인 서드파티 컴포넌트의 사용자 정의 스타일을 넣기에도 좋은 위치입니다:

CSS

```
    @layer components {  .select2-dropdown {    /* ... */  }}
```

- variant 사용하기

사용자 정의 CSS 안에서 Tailwind variant를 적용하려면 `@variant` 지시어를 사용하세요:

app.css

```
    .my-element {  background: white;  @variant dark {    background: black;  }}
```

Compiled CSS

```
    .my-element {  background: white;  @media (prefers-color-scheme: dark) {    background: black;  }}
```

여러 variant를 동시에 적용해야 한다면 중첩을 사용하세요:

app.css

```
    .my-element {  background: white;  @variant dark {    @variant hover {      background: black;    }  }}
```

Compiled CSS

```
    .my-element {  background: white;  @media (prefers-color-scheme: dark) {    &:hover {      @media (hover: hover) {        background: black;      }    }  }}
```

## 사용자 정의 유틸리티 추가

- 단순 유틸리티

Tailwind에 기본 포함된 유틸리티 외에도, 직접 사용자 정의 유틸리티를 추가할 수 있습니다. 이는 프로젝트에서 사용하고 싶은 CSS 기능이 있지만 Tailwind가 기본 유틸리티로 제공하지 않을 때 유용합니다.

`@utility` 지시어를 사용해 프로젝트에 사용자 정의 유틸리티를 추가하세요:

CSS

```
    @utility content-auto {  content-visibility: auto;}
```

이제 HTML에서 이 유틸리티를 사용할 수 있습니다:

HTML

```
    <div class="content-auto">  <!-- ... --></div>
```

또한 `hover`, `focus`, `lg` 같은 variant와도 함께 동작합니다:

HTML

```
    <div class="hover:content-auto">  <!-- ... --></div>
```

사용자 정의 유틸리티는 프레임워크의 내장 유틸리티와 함께 `utilities` 레이어에 자동으로 삽입됩니다.

- 복합 유틸리티

사용자 정의 유틸리티가 단일 클래스 이름보다 복잡하다면, 중첩을 사용해 유틸리티를 정의하세요:

CSS

```
    @utility scrollbar-hidden {  &::-webkit-scrollbar {    display: none;  }}
```

- 함수형 유틸리티

`@utility` 지시어로 단순 유틸리티를 등록하는 것 외에도, 인수를 받는 함수형 유틸리티를 등록할 수 있습니다:

CSS

```
    @utility tab-* {  tab-size: --value(--tab-size-*);}
```

특수 함수 `--value()`는 유틸리티 값을 해석하는 데 사용됩니다.

#

- 테마 값 매칭

`--value(--theme-key-*)` 문법을 사용하면 유틸리티 값을 테마 키 집합에 대해 해석할 수 있습니다:

CSS

```
    @theme {  --tab-size-2: 2;  --tab-size-4: 4;  --tab-size-github: 8;}@utility tab-* {  tab-size: --value(--tab-size-*);}
```

이렇게 하면 `tab-2`, `tab-4`, `tab-github` 같은 유틸리티와 매칭됩니다.

#

- 순수 값

값을 순수 값으로 해석하려면 `--value({type})` 문법을 사용하세요. 여기서 `{type}`은 순수 값으로 검증하려는 데이터 타입입니다:

CSS

```
    @utility tab-* {  tab-size: --value(integer);}
```

이렇게 하면 `tab-1`, `tab-76` 같은 유틸리티와 매칭됩니다.

사용 가능한 순수 값 데이터 타입은 `number`, `integer`, `ratio`, `percentage`입니다.

#

- 리터럴 값

리터럴 값을 지원하려면 `--value('literal')` 문법을 사용하세요(따옴표에 주의):

CSS

```
    @utility tab-* {  tab-size: --value("inherit", "initial", "unset");}
```

이렇게 하면 `tab-inherit`, `tab-initial`, `tab-unset` 같은 유틸리티와 매칭됩니다.

#

- 임의 값

임의 값을 지원하려면 `--value([{type}])` 문법을 사용하세요(대괄호에 주의). 이렇게 하면 Tailwind에 임의 값으로 지원할 타입을 알려줄 수 있습니다:

CSS

```
    @utility tab-* {  tab-size: --value([integer]);}
```

이렇게 하면 `tab-[1]`, `tab-[76]` 같은 유틸리티와 매칭됩니다.

사용 가능한 임의 값 데이터 타입은 `absolute-size`, `angle`, `bg-size`, `color`, `family-name`, `generic-name`, `image`, `integer`, `length`, `line-width`, `number`, `percentage`, `position`, `ratio`, `relative-size`, `url`, `vector`, `*`입니다.

#

- 테마 값, 순수 값, 임의 값 함께 지원

`--value()` 함수의 세 가지 형태는 하나의 규칙 안에서 여러 선언으로 함께 사용할 수 있으며, 해석에 실패한 선언은 출력에서 생략됩니다:

CSS

```
    @theme {  --tab-size-github: 8;}@utility tab-* {  tab-size: --value([integer]);  tab-size: --value(integer);  tab-size: --value(--tab-size-*);}
```

덕분에 필요할 경우 각 케이스에서 값을 다르게 처리할 수 있습니다. 예를 들어 순수 정수를 백분율로 변환할 수 있습니다:

CSS

```
    @utility opacity-* {  opacity: --value([percentage]);  opacity: calc(--value(integer) * 1%);  opacity: --value(--opacity-*);}
```

여러 케이스에서 반환 값을 다르게 처리할 필요가 없다면, `--value()` 함수는 여러 인수를 받아 왼쪽에서 오른쪽 순서로 해석할 수도 있습니다:

CSS

```
    @theme {  --tab-size-github: 8;}@utility tab-* {  tab-size: --value(--tab-size-*, integer, [integer]);}@utility opacity-* {  opacity: calc(--value(integer) * 1%);  opacity: --value(--opacity-*, [percentage]);}
```

#

- 음수 값

음수 값을 지원하려면, 양수 유틸리티와 음수 유틸리티를 각각 별도 선언으로 등록하세요:

CSS

```
    @utility inset-* {  inset: --spacing(--value(integer));  inset: --value([percentage], [length]);}@utility -inset-* {  inset: --spacing(--value(integer) * -1);  inset: calc(--value([percentage], [length]) * -1);}
```

#

- Modifier

Modifier는 `--modifier()` 함수를 사용해 처리합니다. 이 함수는 `--value()` 함수와 완전히 동일하게 동작하지만, modifier가 있을 때 해당 modifier를 대상으로 동작합니다:

CSS

```
    @utility text-* {  font-size: --value(--text-*, [length]);  line-height: --modifier(--leading-*, [length], [*]);}
```

modifier가 없으면 modifier에 의존하는 선언은 출력에 포함되지 않습니다.

#

- 분수

분수를 처리하기 위해 CSS `ratio` 데이터 타입을 사용합니다. 이를 `--value()`와 함께 사용하면, Tailwind는 값과 modifier를 하나의 값으로 처리하라는 신호로 인식합니다:

CSS

```
    @utility aspect-* {  aspect-ratio: --value(--aspect-ratio-*, ratio, [ratio]);}
```

이렇게 하면 `aspect-square`, `aspect-3/4`, `aspect-[7/9]` 같은 유틸리티와 매칭됩니다.

## 사용자 정의 variant 추가

Tailwind에 기본 포함된 variant 외에도, `@custom-variant` 지시어를 사용해 사용자 정의 variant를 추가할 수 있습니다:

```
    @custom-variant theme-midnight {  &:where([data-theme="midnight"] *) {    @slot;  }}
```

이제 HTML에서 `theme-midnight:<utility>` variant를 사용할 수 있습니다:

```
    <html data-theme="midnight">  <button class="theme-midnight:bg-black ..."></button></html>
```

중첩이 필요하지 않은 경우에는 축약 문법으로 variant를 만들 수 있습니다:

```
    @custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

사용자 정의 variant가 여러 규칙을 가질 때는 서로 중첩할 수 있습니다:

```
    @custom-variant any-hover {  @media (any-hover: hover) {    &:hover {      @slot;    }  }}
```
