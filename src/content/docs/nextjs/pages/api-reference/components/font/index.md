---
title: '컴포넌트: Font'
description: '모든 폰트 파일에 대해 자동 자체 호스팅이 내장되어 있습니다. 즉, 레이아웃 시프트 없이 웹 폰트를 최적으로 로드할 수 있습니다.'
---

# 컴포넌트: Font | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/components/font

# Font 모듈

최종 업데이트 2026년 2월 20일

[`next/font`](https://nextjs.org/docs/app/api-reference/components/font)는 글꼴(커스텀 폰트 포함)을 자동으로 최적화하고 외부 네트워크 요청을 제거하여 개인 정보 보호와 성능을 향상합니다.

모든 폰트 파일에 대해 **자동 자체 호스팅**이 내장되어 있습니다. 즉, [레이아웃 시프트](https://web.dev/articles/cls) 없이 웹 폰트를 최적으로 로드할 수 있습니다.

또한 모든 [Google Fonts](https://fonts.google.com/)를 편리하게 사용할 수 있습니다. CSS와 폰트 파일은 빌드 시 다운로드되어 다른 정적 자산과 함께 자체 호스팅됩니다. **브라우저가 Google로 요청을 보내지 않습니다.**

모든 페이지에서 폰트를 사용하려면 `/pages` 아래 [`_app.js` 파일](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)에 다음과 같이 추가하세요:

pages/_app.js
```
    import { Inter } from 'next/font/google'

    // If loading a variable font, you don't need to specify the font weight
    const inter = Inter({ subsets: ['latin'] })

    export default function MyApp({ Component, pageProps }) {
      return (
        <main className={inter.className}>
          <Component {...pageProps} />
        </main>
      )
    }
```

> **🎥 시청:** `next/font` 사용법 더 알아보기 → [YouTube (6 minutes)](https://www.youtube.com/watch?v=L8_98i_bMMA).

## Reference[](https://nextjs.org/docs/pages/api-reference/components/font#reference)

Key| `font/google`| `font/local`| Type| Required
---|---|---|---|---
[`src`](https://nextjs.org/docs/pages/api-reference/components/font#src)| | | String or Array of Objects| Yes
[`weight`](https://nextjs.org/docs/pages/api-reference/components/font#weight)| | | String or Array| Required/Optional
[`style`](https://nextjs.org/docs/pages/api-reference/components/font#style)| | | String or Array| -
[`subsets`](https://nextjs.org/docs/pages/api-reference/components/font#subsets)| | | Array of Strings| -
[`axes`](https://nextjs.org/docs/pages/api-reference/components/font#axes)| | | Array of Strings| -
[`display`](https://nextjs.org/docs/pages/api-reference/components/font#display)| | | String| -
[`preload`](https://nextjs.org/docs/pages/api-reference/components/font#preload)| | | Boolean| -
[`fallback`](https://nextjs.org/docs/pages/api-reference/components/font#fallback)| | | Array of Strings| -
[`adjustFontFallback`](https://nextjs.org/docs/pages/api-reference/components/font#adjustfontfallback)| | | Boolean or String| -
[`variable`](https://nextjs.org/docs/pages/api-reference/components/font#variable)| | | String| -
[`declarations`](https://nextjs.org/docs/pages/api-reference/components/font#declarations)| | | Array of Objects| -

### `src`[](https://nextjs.org/docs/pages/api-reference/components/font#src)

폰트 파일의 경로를 문자열 또는 `Array<{path: string, weight?: string, style?: string}>` 타입의 객체 배열로 지정하며, 폰트 로더 함수가 호출되는 디렉터리를 기준으로 합니다.

`next/font/local`에서 사용

  * 필수

예:

  * `src:'./fonts/my-font.woff2'` — `my-font.woff2`를 `app` 디렉터리 안의 `fonts` 디렉터리에 둘 때
  * `src:[{path: './inter/Inter-Thin.ttf', weight: '100',},{path: './inter/Inter-Regular.ttf',weight: '400',},{path: './inter/Inter-Bold-Italic.ttf', weight: '700',style: 'italic',},]`
  * 폰트 로더 함수를 `app/page.tsx`에서 호출하면서 `src:'../styles/fonts/my-font.ttf'`로 지정했다면, `my-font.ttf`는 프로젝트 루트의 `styles/fonts`에 위치함

### `weight`[](https://nextjs.org/docs/pages/api-reference/components/font#weight)

다음과 같은 경우의 폰트 [`weight`](https://fonts.google.com/knowledge/glossary/weight):

  * 특정 폰트에서 사용 가능한 굵기 값 또는 [variable](https://fonts.google.com/variablefonts) 폰트일 때 값 범위를 담은 문자열
  * 폰트가 [variable google font](https://fonts.google.com/variablefonts)가 아닐 때 여러 굵기 값을 담은 배열로 지정 (`next/font/google`에만 적용)

`next/font/google` 및 `next/font/local`에서 사용

  * 사용 중인 폰트가 [variable](https://fonts.google.com/variablefonts)이 **아닐 때 필수**

예:

  * `weight: '400'`: 단일 굵기 값을 나타내는 문자열 – [`Inter`](https://fonts.google.com/specimen/Inter?query=inter)의 경우 가능한 값은 `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'`, `'variable'`이며 기본값은 `'variable'`
  * `weight: '100 900'`: variable 폰트에서 `100`부터 `900` 사이 범위를 나타내는 문자열
  * `weight: ['100','400','900']`: variable 폰트가 아닐 때 3개의 가능한 값을 담은 배열

### `style`[](https://nextjs.org/docs/pages/api-reference/components/font#style)

다음과 같은 경우의 폰트 [`style`](https://developer.mozilla.org/docs/Web/CSS/font-style):

  * 기본값이 `'normal'`인 문자열 [값](https://developer.mozilla.org/docs/Web/CSS/font-style#values)
  * 폰트가 [variable google font](https://fonts.google.com/variablefonts)가 아닐 때 여러 스타일 값을 담은 배열 (`next/font/google`에만 적용)

`next/font/google` 및 `next/font/local`에서 사용

  * 선택 사항

예:

  * `style: 'italic'`: 문자열 – `next/font/google`에서는 `normal` 또는 `italic`
  * `style: 'oblique'`: 문자열 – `next/font/local`에서는 [표준 폰트 스타일](https://developer.mozilla.org/docs/Web/CSS/font-style)에 포함된 값이면 모두 가능
  * `style: ['italic','normal']`: `next/font/google`에서 사용할 2개의 값 배열 (`normal`, `italic` 중 선택)

### `subsets`[](https://nextjs.org/docs/pages/api-reference/components/font#subsets)

프리로드할 [서브셋](https://nextjs.org/docs/app/api-reference/components/font#specifying-a-subset)의 이름을 문자열 배열로 정의합니다. `subsets`로 지정한 폰트는 [`preload`](https://nextjs.org/docs/pages/api-reference/components/font#preload) 옵션이 기본값 `true`일 때 head에 link preload 태그가 추가됩니다.

`next/font/google`에서 사용

  * 선택 사항

예:

  * `subsets: ['latin']`: `latin` 서브셋을 담은 배열

Google Fonts에서 사용하는 폰트의 서브셋 목록을 확인할 수 있습니다.

### `axes`[](https://nextjs.org/docs/pages/api-reference/components/font#axes)

일부 variable 폰트는 추가 `axes`를 포함할 수 있습니다. 기본적으로 파일 크기를 줄이기 위해 폰트 weight만 포함됩니다. 가능한 `axes` 값은 폰트에 따라 다릅니다.

`next/font/google`에서 사용

  * 선택 사항

예:

  * `axes: ['slnt']`: `Inter` variable 폰트의 `slnt` 값을 담은 배열입니다. [여기](https://fonts.google.com/variablefonts?vfquery=inter#font-families)에서 추가 `axes`를 확인할 수 있습니다. 자신의 폰트에 사용할 수 있는 `axes` 값은 [Google variable fonts 페이지](https://fonts.google.com/variablefonts#font-families)에서 필터를 적용해 `wght` 이외의 축을 찾으면 됩니다.

### `display`[](https://nextjs.org/docs/pages/api-reference/components/font#display)

기본값이 `'swap'`인 폰트 [`display`](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display)로, 가능한 문자열 [값](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display#values)은 `'auto'`, `'block'`, `'swap'`, `'fallback'`, `'optional'`입니다.

`next/font/google` 및 `next/font/local`에서 사용

  * 선택 사항

예:

  * `display: 'optional'`: `optional` 값으로 지정한 문자열

### `preload`[](https://nextjs.org/docs/pages/api-reference/components/font#preload)

폰트를 [프리로드](https://nextjs.org/docs/app/api-reference/components/font#preloading)할지 여부를 지정하는 불리언 값으로 기본값은 `true`입니다.

`next/font/google` 및 `next/font/local`에서 사용

  * 선택 사항

예:

  * `preload: false`

### `fallback`[](https://nextjs.org/docs/pages/api-reference/components/font#fallback)

폰트를 로드할 수 없을 때 사용할 폴백 폰트입니다. 기본값 없이 폴백 폰트 이름을 담은 문자열 배열로 지정합니다.

  * 선택 사항

`next/font/google` 및 `next/font/local`에서 사용

예:

  * `fallback: ['system-ui', 'arial']`: `system-ui` 또는 `arial`을 폴백으로 설정하는 배열

### `adjustFontFallback`[](https://nextjs.org/docs/pages/api-reference/components/font#adjustfontfallback)

  * `next/font/google`: [Cumulative Layout Shift](https://web.dev/cls/)를 줄이기 위해 자동 폴백 폰트 사용 여부를 설정하는 불리언 값으로 기본값은 `true`
  * `next/font/local`: 자동 폴백 폰트 사용 여부를 설정하는 문자열 또는 불리언 `false` 값으로, 가능한 값은 `'Arial'`, `'Times New Roman'`, `false`이며 기본값은 `'Arial'`

`next/font/google` 및 `next/font/local`에서 사용

  * 선택 사항

예:

  * `adjustFontFallback: false`: `next/font/google`용
  * `adjustFontFallback: 'Times New Roman'`: `next/font/local`용

### `variable`[](https://nextjs.org/docs/pages/api-reference/components/font#variable)

[CSS 변수 방식](https://nextjs.org/docs/pages/api-reference/components/font#css-variables)으로 스타일을 적용할 때 사용할 CSS 변수 이름을 정의하는 문자열 값입니다.

`next/font/google` 및 `next/font/local`에서 사용

  * 선택 사항

예:

  * `variable: '--my-font'`: CSS 변수 `--my-font`를 선언

### `declarations`[](https://nextjs.org/docs/pages/api-reference/components/font#declarations)

생성된 `@font-face`를 더욱 정의하는 폰트 페이스 [descriptor](https://developer.mozilla.org/docs/Web/CSS/@font-face#descriptors) 키-값 쌍 배열입니다.

`next/font/local`에서 사용

  * 선택 사항

예:

  * `declarations: [{ prop: 'ascent-override', value: '90%' }]`

## 예제[](https://nextjs.org/docs/pages/api-reference/components/font#examples)

## Google Fonts[](https://nextjs.org/docs/pages/api-reference/components/font#google-fonts)

Google 폰트를 사용하려면 `next/font/google`에서 함수를 import하세요. 최적의 성능과 유연성을 위해 [variable fonts](https://fonts.google.com/variablefonts)를 권장합니다.

모든 페이지에서 폰트를 사용하려면 `/pages` 아래 [`_app.js` 파일](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)에 다음과 같이 추가하세요:

pages/_app.js
```
    import { Inter } from 'next/font/google'

    // If loading a variable font, you don't need to specify the font weight
    const inter = Inter({ subsets: ['latin'] })

    export default function MyApp({ Component, pageProps }) {
      return (
        <main className={inter.className}>
          <Component {...pageProps} />
        </main>
      )
    }
```

variable 폰트를 사용할 수 없다면 **반드시 weight를 지정해야 합니다**:

pages/_app.js
```
    import { Roboto } from 'next/font/google'

    const roboto = Roboto({
      weight: '400',
      subsets: ['latin'],
    })

    export default function MyApp({ Component, pageProps }) {
      return (
        <main className={roboto.className}>
          <Component {...pageProps} />
        </main>
      )
    }
```

배열을 사용해 여러 weight와/또는 스타일을 지정할 수 있습니다:

app/layout.js
```
    const roboto = Roboto({
      weight: ['400', '700'],
      style: ['normal', 'italic'],
      subsets: ['latin'],
      display: 'swap',
    })
```

> **알아두면 좋아요**: 여러 단어로 된 폰트 이름에는 밑줄(_)을 사용하세요. 예를 들어 `Roboto Mono`는 `Roboto_Mono`로 import해야 합니다.

### `<head>`에 폰트 적용하기[](https://nextjs.org/docs/pages/api-reference/components/font#apply-the-font-in-head)

다음과 같이 `<head>` 내부에 폰트를 주입하면 래퍼나 `className` 없이도 폰트를 사용할 수 있습니다:

pages/_app.js
```
    import { Inter } from 'next/font/google'

    const inter = Inter({ subsets: ['latin'] })

    export default function MyApp({ Component, pageProps }) {
      return (
        <>
          <style jsx global>{`
            html {
              font-family: ${inter.style.fontFamily};
            }
          `}</style>
          <Component {...pageProps} />
        </>
      )
    }
```

### 단일 페이지 사용[](https://nextjs.org/docs/pages/api-reference/components/font#single-page-usage)

아래와 같이 특정 페이지에 추가하여 단일 페이지에서 폰트를 사용할 수 있습니다:

pages/index.js
```
    import { Inter } from 'next/font/google'

    const inter = Inter({ subsets: ['latin'] })

    export default function Home() {
      return (
        <div className={inter.className}>
          <p>Hello World</p>
        </div>
      )
    }
```

### 서브셋 지정하기[](https://nextjs.org/docs/pages/api-reference/components/font#specifying-a-subset)

Google Fonts는 자동으로 [subset](https://fonts.google.com/knowledge/glossary/subsetting) 처리되어 폰트 파일 크기를 줄이고 성능을 개선합니다. 미리 로드하려는 서브셋을 정의해야 하며, [`preload`](https://nextjs.org/docs/app/api-reference/components/font#preload)가 `true`인데 서브셋을 지정하지 않으면 경고가 발생합니다.

함수 호출에 서브셋을 추가하면 됩니다:

pages/_app.js
```
    const inter = Inter({ subsets: ['latin'] })
```

자세한 내용은 [Font API Reference](https://nextjs.org/docs/app/api-reference/components/font)를 참고하세요.

## 여러 폰트 사용하기[](https://nextjs.org/docs/pages/api-reference/components/font#using-multiple-fonts)

애플리케이션에서 여러 폰트를 가져와 사용할 수 있으며, 두 가지 접근 방식이 있습니다.

첫 번째 방법은 폰트를 내보내는 유틸리티 함수를 만들고, 필요한 곳에서 가져와 `className`을 적용하는 것입니다. 이렇게 하면 실제로 렌더링될 때만 폰트가 미리 로드됩니다:

app/fonts.ts

JavaScriptTypeScript
```
    import { Inter, Roboto_Mono } from 'next/font/google'

    export const inter = Inter({
      subsets: ['latin'],
      display: 'swap',
    })

    export const roboto_mono = Roboto_Mono({
      subsets: ['latin'],
      display: 'swap',
    })
```

위 예제에서는 `Inter`가 전역에 적용되고, `Roboto Mono`는 필요한 곳에서 가져와 사용할 수 있습니다.

또는 [CSS 변수](https://nextjs.org/docs/app/api-reference/components/font#variable)를 만들어 선호하는 CSS 솔루션과 함께 사용할 수도 있습니다:

app/global.css
```
    html {
      font-family: var(--font-inter);
    }

    h1 {
      font-family: var(--font-roboto-mono);
    }
```

이 예제에서는 `Inter`가 전역에 적용되고 모든 `<h1>` 태그는 `Roboto Mono` 스타일을 사용합니다.

> **Recommendation** : 각 폰트는 추가로 다운로드해야 하는 리소스이므로 여러 폰트 사용은 신중하게 결정하세요.

### 로컬 폰트[](https://nextjs.org/docs/pages/api-reference/components/font#local-fonts)

`next/font/local`을 가져오고 로컬 폰트 파일의 `src`를 지정하세요. 최고의 성능과 유연성을 위해 [variable fonts](https://fonts.google.com/variablefonts) 사용을 권장합니다.

pages/_app.js
```
    import localFont from 'next/font/local'

    // Font files can be colocated inside of `pages`
    const myFont = localFont({ src: './my-font.woff2' })

    export default function MyApp({ Component, pageProps }) {
      return (
        <main className={myFont.className}>
          <Component {...pageProps} />
        </main>
      )
    }
```

하나의 폰트 패밀리에 여러 파일을 사용하려면 `src`를 배열로 지정할 수 있습니다:
```
    const roboto = localFont({
      src: [
        {
          path: './Roboto-Regular.woff2',
          weight: '400',
          style: 'normal',
        },
        {
          path: './Roboto-Italic.woff2',
          weight: '400',
          style: 'italic',
        },
        {
          path: './Roboto-Bold.woff2',
          weight: '700',
          style: 'normal',
        },
        {
          path: './Roboto-BoldItalic.woff2',
          weight: '700',
          style: 'italic',
        },
      ],
    })
```

자세한 내용은 [Font API Reference](https://nextjs.org/docs/app/api-reference/components/font)를 참고하세요.

### Tailwind CSS와 함께 사용하기[](https://nextjs.org/docs/pages/api-reference/components/font#with-tailwind-css)

`next/font`는 [CSS 변수](https://nextjs.org/docs/app/api-reference/components/font#css-variables)를 사용하여 [Tailwind CSS](https://tailwindcss.com/)와 자연스럽게 통합됩니다.

아래 예제에서는 `next/font/google`의 `Inter`와 `Roboto_Mono` 폰트를 사용합니다(어떤 Google Font나 로컬 폰트도 사용할 수 있습니다). `variable` 옵션으로 각각의 CSS 변수 이름(예: `inter`, `roboto_mono`)을 정의한 뒤, `inter.variable`과 `roboto_mono.variable`을 HTML 문서에 적용하여 CSS 변수를 포함시킵니다.

> **Good to know** : 프로젝트 요구, 스타일 선호도에 따라 `<html>` 또는 `<body>` 태그에 이 변수를 추가할 수 있습니다.

pages/_app.js
```
    import { Inter } from 'next/font/google'

    const inter = Inter({
      subsets: ['latin'],
      variable: '--font-inter',
    })

    const roboto_mono = Roboto_Mono({
      subsets: ['latin'],
      display: 'swap',
      variable: '--font-roboto-mono',
    })

    export default function MyApp({ Component, pageProps }) {
      return (
        <main className={`${inter.variable} ${roboto_mono.variable} font-sans`}>
          <Component {...pageProps} />
        </main>
      )
    }
```

마지막으로 [Tailwind CSS config](https://nextjs.org/docs/app/getting-started/css#tailwind-css)에 CSS 변수를 추가합니다:

global.css
```
    @import 'tailwindcss';

    @theme inline {
      --font-sans: var(--font-inter);
      --font-mono: var(--font-roboto-mono);
    }
```

### Tailwind CSS v3[](https://nextjs.org/docs/pages/api-reference/components/font#tailwind-css-v3)

tailwind.config.js
```
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: [
        './pages/**/*.{js,ts,jsx,tsx}',
        './components/**/*.{js,ts,jsx,tsx}',
        './app/**/*.{js,ts,jsx,tsx}',
      ],
      theme: {
        extend: {
          fontFamily: {
            sans: ['var(--font-inter)'],
            mono: ['var(--font-roboto-mono)'],
          },
        },
      },
      plugins: [],
    }
```

이제 `font-sans`와 `font-mono` 유틸리티 클래스로 요소에 폰트를 적용할 수 있습니다.
```
    <p class="font-sans ...">The quick brown fox ...</p>
    <p class="font-mono ...">The quick brown fox ...</p>
```

### 스타일 적용하기[](https://nextjs.org/docs/pages/api-reference/components/font#applying-styles)

폰트 스타일은 다음 세 가지 방법으로 적용할 수 있습니다:

  * [`className`](https://nextjs.org/docs/pages/api-reference/components/font#classname)
  * [`style`](https://nextjs.org/docs/pages/api-reference/components/font#style-1)
  * [CSS Variables](https://nextjs.org/docs/pages/api-reference/components/font#css-variables)

#### `className`[](https://nextjs.org/docs/pages/api-reference/components/font#classname)

로딩된 폰트에 대한 읽기 전용 CSS `className`을 반환하므로 이를 HTML 요소에 전달할 수 있습니다.
```
    <p className={inter.className}>Hello, Next.js!</p>
```

#### `style`[](https://nextjs.org/docs/pages/api-reference/components/font#style-1)

로딩된 폰트에 대한 읽기 전용 CSS `style` 객체를 반환하며, `style.fontFamily`를 통해 폰트 패밀리 이름과 폴백 폰트에 접근할 수 있습니다.
```
    <p style={inter.style}>Hello World</p>
```

#### CSS Variables[](https://nextjs.org/docs/pages/api-reference/components/font#css-variables)

스타일을 외부 스타일시트에서 정의하고 추가 옵션을 지정하려면 CSS 변수 방식을 사용하세요.

폰트를 가져오는 것과 더불어 CSS 변수가 정의된 CSS 파일도 가져오고, 폰트 로더 객체에 `variable` 옵션을 다음과 같이 설정합니다:

app/page.tsx

JavaScriptTypeScript
```
    import { Inter } from 'next/font/google'
    import styles from '../styles/component.module.css'

    const inter = Inter({
      variable: '--font-inter',
    })
```

폰트를 사용하려면 스타일링하려는 텍스트의 부모 컨테이너 `className`을 폰트 로더의 `variable` 값으로 설정하고, 텍스트의 `className`을 외부 CSS 파일의 `styles` 속성으로 지정합니다.

app/page.tsx

JavaScriptTypeScript
```
    <main className={inter.variable}>
      <p className={styles.text}>Hello World</p>
    </main>
```

`component.module.css` 파일에서 `text` 선택자 클래스를 다음과 같이 정의합니다:

styles/component.module.css
```
    .text {
      font-family: var(--font-inter);
      font-weight: 200;
      font-style: italic;
    }
```

위 예제에서는 `Hello World` 텍스트가 `Inter` 폰트와 생성된 폴백 폰트로 `font-weight: 200`, `font-style: italic` 스타일을 적용받습니다.

### 폰트 정의 파일 사용하기[](https://nextjs.org/docs/pages/api-reference/components/font#using-a-font-definitions-file)

`localFont` 또는 Google 폰트 함수를 호출할 때마다 해당 폰트는 애플리케이션 내에서 하나의 인스턴스로 호스팅됩니다. 따라서 동일한 폰트를 여러 곳에서 사용할 필요가 있다면, 한 곳에서 로드하고 필요한 위치에서 해당 폰트 객체를 가져와야 합니다. 이를 위해 폰트 정의 파일을 사용합니다.

예를 들어, 앱 디렉터리 루트의 `styles` 폴더에 `fonts.ts` 파일을 만듭니다.

그런 다음 폰트 정의를 다음과 같이 지정합니다:

styles/fonts.ts

JavaScriptTypeScript
```
    import { Inter, Lora, Source_Sans_3 } from 'next/font/google'
    import localFont from 'next/font/local'

    // define your variable fonts
    const inter = Inter()
    const lora = Lora()
    // define 2 weights of a non-variable font
    const sourceCodePro400 = Source_Sans_3({ weight: '400' })
    const sourceCodePro700 = Source_Sans_3({ weight: '700' })
    // define a custom local font where GreatVibes-Regular.ttf is stored in the styles folder
    const greatVibes = localFont({ src: './GreatVibes-Regular.ttf' })

    export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }
```

이제 코드에서 다음과 같이 정의를 사용할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
```
    import { inter, lora, sourceCodePro700, greatVibes } from '../styles/fonts'

    export default function Page() {
      return (
        <div>
          <p className={inter.className}>Hello world using Inter font</p>
          <p style={lora.style}>Hello world using Lora font</p>
          <p className={sourceCodePro700.className}>
            Hello world using Source_Sans_3 font with weight 700
          </p>
          <p className={greatVibes.className}>My title in Great Vibes font</p>
        </div>
      )
    }
```

코드에서 폰트 정의를 더 쉽게 가져오려면 `tsconfig.json` 또는 `jsconfig.json`에 경로 별칭을 다음과 같이 정의할 수 있습니다:

tsconfig.json
```
    {
      "compilerOptions": {
        "paths": {
          "@/fonts": ["./styles/fonts"]
        }
      }
    }
```

이제 다음과 같이 폰트 정의를 가져올 수 있습니다:

app/about/page.tsx

JavaScriptTypeScript
```
    import { greatVibes, sourceCodePro400 } from '@/fonts'
```

### 사전 로딩[](https://nextjs.org/docs/pages/api-reference/components/font#preloading)

사이트의 페이지에서 폰트 함수를 호출해도 모든 라우트에서 전역으로 사용할 수 있도록 선로딩되는 것은 아닙니다. 대신, 해당 폰트가 사용된 파일 유형을 기준으로 관련 라우트에서만 선로딩됩니다.

  * [고유 페이지](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)에 있으면 그 페이지의 고유 라우트에서만 선로딩됩니다.
  * [커스텀 App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)에 있으면 `/pages` 아래 사이트의 모든 라우트에서 선로딩됩니다.

## 버전 변경사항[](https://nextjs.org/docs/pages/api-reference/components/font#version-changes)

Version| Changes
---|---
`v13.2.0`| `@next/font`가 `next/font`로 이름이 변경되었습니다. 별도 설치가 더 이상 필요하지 않습니다.
`v13.0.0`| `@next/font`가 추가되었습니다.

supported.

Send