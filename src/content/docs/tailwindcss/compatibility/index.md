---
title: "호환성 - 시작하기 - Tailwind CSS"
description: "Tailwind CSS v4.0은 최신 브라우저를 대상으로 설계되고 테스트되었으며, 프레임워크의 핵심 기능은 특히 다음 브라우저 버전에 의존합니다:"
---

출처 URL: https://tailwindcss.com/docs/compatibility

# 호환성 - 시작하기 - Tailwind CSS

## 브라우저 지원

Tailwind CSS v4.0은 최신 브라우저를 대상으로 설계되고 테스트되었으며, 프레임워크의 핵심 기능은 특히 다음 브라우저 버전에 의존합니다:

- **Chrome 111** _(2023년 3월 출시)_
- **Safari 16.4** _(2023년 3월 출시)_
- **Firefox 128** _(2024년 7월 출시)_

Tailwind에는 `field-sizing: content`, `@starting-style`, `text-wrap: balance` 같은 최첨단 플랫폼 기능도 많이 포함되어 있으며, 이런 기능들은 브라우저 지원이 제한적입니다. 프로젝트에서 이런 최신 기능을 사용할지는 여러분이 결정하면 됩니다. 타겟 브라우저가 지원하지 않는다면 해당 유틸리티와 variant를 사용하지 않으면 됩니다.

최신 플랫폼 기능의 지원 여부가 확실하지 않다면 [Can I use](https://caniuse.com/mdn-css_at-rules_starting-style) 데이터베이스가 매우 유용한 참고 자료입니다.

## Sass, Less, Stylus

Tailwind CSS v4.0은 특정 워크플로를 위해 설계된 완전한 CSS 빌드 도구이며, Sass, Less, Stylus 같은 CSS 전처리기와 함께 사용하도록 설계되지 않았습니다.

**Tailwind CSS 자체를 전처리기로 생각하세요**. Sass를 Stylus와 함께 쓰지 않는 것과 같은 이유로, Tailwind를 Sass와 함께 사용할 필요가 없습니다.

Tailwind는 최신 브라우저를 기준으로 설계되어 있어서 nesting이나 변수 같은 기능을 위해 별도의 전처리기가 실제로 필요하지 않으며, import 번들링이나 vendor prefix 추가 같은 작업도 Tailwind 자체가 처리합니다.

- 빌드 타임 import

Tailwind는 `@import`로 포함한 다른 CSS 파일을 별도의 전처리 도구 없이 자동으로 번들링합니다.

app.css

```
    @import "tailwindcss";@import "./typography.css";
```

이 예시에서는 `typography.css` 파일이 Sass나 `postcss-import` 같은 추가 도구 없이 Tailwind에 의해 컴파일된 CSS에 번들링됩니다.

- 변수

모든 최신 브라우저는 어떤 전처리기 없이도 [native CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)를 지원합니다:

typography.css

```
    .typography {  font-size: var(--text-base);  color: var(--color-gray-700);}
```

Tailwind는 내부적으로 CSS 변수를 매우 많이 사용하므로, 프로젝트에서 Tailwind를 쓸 수 있다면 native CSS 변수도 사용할 수 있습니다.

- Nesting

Tailwind는 내부적으로 [Lightning CSS](https://lightningcss.dev/)를 사용해 이런 중첩 CSS를 처리합니다:

typography.css

```
    .typography {  p {    font-size: var(--text-base);  }  img {    border-radius: var(--radius-lg);  }}
```

Tailwind가 해당 중첩 CSS를 평탄화해 모든 최신 브라우저가 이해할 수 있도록 만들어 줍니다:

output.css

```
    .typography p {  font-size: var(--text-base);}.typography img {  border-radius: var(--radius-lg);}
```

요즘은 native CSS nesting 지원도 매우 좋아졌기 때문에, Tailwind를 사용하지 않더라도 nesting을 위해 전처리기가 꼭 필요하지는 않습니다.

- 반복문

Tailwind에서는 과거에 반복문으로 만들었던 클래스들(예: `col-span-1`, `col-span-2` 등)을 미리 정의할 필요 없이, 사용할 때마다 Tailwind가 온디맨드로 생성합니다.

게다가 Tailwind CSS로 작업할 때는 대부분의 스타일링을 CSS 파일이 아니라 HTML에서 처리합니다. 처음부터 많은 양의 CSS를 작성하지 않기 때문에, 대량의 커스텀 CSS 규칙을 프로그래밍 방식으로 생성하기 위한 반복문 같은 기능이 굳이 필요하지 않습니다.

- 색상 및 수학 함수

Sass나 Less 같은 전처리기를 사용할 때는 `darken`, `lighten` 같은 함수로 색상을 조정했을 수 있습니다.

Tailwind를 사용할 때 권장되는 워크플로는, 프레임워크에 포함된 전문적으로 설계된 [default color palette](https://tailwindcss.com/docs/colors)처럼 각 색상의 밝고 어두운 음영이 포함된 사전 정의 팔레트를 사용하는 것입니다.

```
    <button class="bg-indigo-500 hover:bg-indigo-600 ...">  <!-- ... --></button>
```

또한 [color-mix()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix) 같은 최신 CSS 기능을 사용하면 브라우저에서 런타임에 직접 색상을 조정할 수 있습니다. 이 방식은 CSS 변수나 `currentcolor` 키워드로 정의된 색상도 조정할 수 있는데, 이는 전처리기로는 불가능합니다.

마찬가지로 브라우저는 이제 `min()`, `max()`, `round()` 같은 수학 함수도 기본 지원하므로, 이런 기능을 위해 전처리기에 의존할 필요도 없습니다.

## CSS 모듈

Tailwind는 CSS 모듈과 호환되며, 이미 CSS 모듈을 사용 중인 프로젝트에 Tailwind를 도입할 때 함께 사용할 수 있습니다. 하지만 **가능하다면 CSS 모듈과 Tailwind를 함께 사용하는 것은 권장하지 않습니다**.

- 스코프 관련 문제

CSS 모듈은 커스텀 CSS를 작성할 때 발생하는 스코프 문제를 해결하기 위해 만들어졌지만, HTML에서 유틸리티 클래스를 조합하는 방식에서는 그런 문제가 거의 발생하지 않습니다.

Tailwind에서는 각 유틸리티 클래스가 어디서 사용되든 항상 같은 동작을 하므로 스타일 스코프가 자연스럽게 유지됩니다. UI의 한 부분에 유틸리티 클래스를 추가했을 때 다른 곳에 예상치 못한 부작용이 생길 위험이 없습니다.

- 성능

CSS 모듈을 사용할 때 Vite, Parcel, Turbopack 같은 빌드 도구는 각 CSS 모듈을 개별적으로 처리합니다. 즉, 프로젝트에 CSS 모듈이 50개라면 **Tailwind도 50번 별도로 실행되어야 하며** , 그 결과 빌드 시간이 훨씬 느려지고 개발자 경험도 나빠집니다.

- 명시적인 컨텍스트 공유

CSS 모듈은 각각 별도로 처리되므로, import하지 않으면 `@theme`가 없습니다.

즉, `@apply` 같은 기능은 전역 스타일을 reference로 명시적으로 import하지 않으면 기대한 대로 동작하지 않습니다:

theme 변수가 정의되도록 전역 스타일을 reference로 import하세요

Button.module.css

```
    @reference "../app.css";button {  @apply bg-blue-500;}
```

또는 `@apply` 대신 CSS 변수를 사용할 수도 있습니다. 이 방법은 Tailwind가 해당 파일 처리를 건너뛸 수 있어 빌드 성능이 개선되는 추가 이점도 있습니다:

Button.module.css

```
    button {  background: var(--color-blue-500);}
```

## Vue, Svelte, Astro

Vue, Svelte, Astro는 컴포넌트 파일 내 `<style>` 블록을 지원하며, 이 방식은 [CSS modules](https://tailwindcss.com/docs/compatibility#css-modules)와 매우 유사하게 동작합니다. 즉, 각 블록이 빌드 도구에서 완전히 별도로 처리되고 동일한 단점이 모두 존재합니다.

이 도구들과 Tailwind를 함께 쓴다면, **컴포넌트에서 `<style>` 블록 사용을 피하고** Tailwind가 의도한 방식대로 마크업에서 유틸리티 클래스로 직접 스타일링하는 것을 권장합니다.

`<style>` 블록을 사용한다면, `@apply` 같은 기능이 기대대로 동작하도록 전역 스타일을 reference로 import해야 합니다:

theme 변수가 정의되도록 전역 스타일을 reference로 import하세요

Button.vue

```
    <template>  <button><slot /></button></template><style scoped>  @reference "../app.css";  button {    @apply bg-blue-500;  }</style>
```

또는 `@apply` 같은 기능 대신 전역으로 정의한 CSS 변수를 사용하세요. 이 방식은 Tailwind가 컴포넌트 CSS를 전혀 처리할 필요가 없습니다:

Button.vue

```
    <template>  <button><slot /></button></template><style scoped>  button {    background-color: var(--color-blue-500);  }</style>
```
