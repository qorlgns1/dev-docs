---
title: '구성 요소: Font'
description: '모든 폰트 파일에 대해 내장 자동 셀프 호스팅을 포함합니다. 이는 layout shift 없이 웹 폰트를 최적으로 로드할 수 있음을 의미합니다.'
---

# 구성 요소: Font | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/components/font

# Font 모듈

마지막 업데이트 2026년 2월 20일

[`next/font`](https://nextjs.org/docs/app/api-reference/components/font)는 커스텀 폰트를 포함한 폰트를 자동으로 최적화하고 외부 네트워크 요청을 제거하여 개인 정보 보호와 성능을 향상합니다.

모든 폰트 파일에 대해 **내장 자동 셀프 호스팅**을 포함합니다. 이는 [layout shift](https://web.dev/articles/cls) 없이 웹 폰트를 최적으로 로드할 수 있음을 의미합니다.

또한 모든 [Google Fonts](https://fonts.google.com/)를 편리하게 사용할 수 있습니다. CSS와 폰트 파일은 빌드 시 다운로드되어 나머지 정적 자산과 함께 셀프 호스팅됩니다. **브라우저가 Google로 요청을 보내지 않습니다.**

app/layout.tsx

JavaScriptTypeScript
[code]
    import { Inter } from 'next/font/google'

    // If loading a variable font, you don't need to specify the font weight
    const inter = Inter({
      subsets: ['latin'],
      display: 'swap',
    })

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en" className={inter.className}>
          <body>{children}</body>
        </html>
      )
    }
[/code]

> **🎥 시청:** `next/font` 사용법 자세히 알아보기 → [YouTube (6분)](https://www.youtube.com/watch?v=L8_98i_bMMA).

## Reference[](https://nextjs.org/docs/app/api-reference/components/font#reference)

Key| `font/google`| `font/local`| Type| Required
---|---|---|---|---
[`src`](https://nextjs.org/docs/app/api-reference/components/font#src)| | | String or Array of Objects| Yes
[`weight`](https://nextjs.org/docs/app/api-reference/components/font#weight)| | | String or Array| Required/Optional
[`style`](https://nextjs.org/docs/app/api-reference/components/font#style)| | | String or Array| -
[`subsets`](https://nextjs.org/docs/app/api-reference/components/font#subsets)| | | Array of Strings| -
[`axes`](https://nextjs.org/docs/app/api-reference/components/font#axes)| | | Array of Strings| -
[`display`](https://nextjs.org/docs/app/api-reference/components/font#display)| | | String| -
[`preload`](https://nextjs.org/docs/app/api-reference/components/font#preload)| | | Boolean| -
[`fallback`](https://nextjs.org/docs/app/api-reference/components/font#fallback)| | | Array of Strings| -
[`adjustFontFallback`](https://nextjs.org/docs/app/api-reference/components/font#adjustfontfallback)| | | Boolean or String| -
[`variable`](https://nextjs.org/docs/app/api-reference/components/font#variable)| | | String| -
[`declarations`](https://nextjs.org/docs/app/api-reference/components/font#declarations)| | | Array of Objects| -

### `src`[](https://nextjs.org/docs/app/api-reference/components/font#src)

폰트 파일 경로를 문자열 또는 객체 배열(type: `Array<{path: string, weight?: string, style?: string}>`)로 지정하며, 경로는 폰트 로더 함수가 호출되는 디렉터리를 기준으로 합니다.

`next/font/local`에서 사용합니다.

  * 필수

예시:

  * `src:'./fonts/my-font.woff2'`: `my-font.woff2`를 `app` 디렉터리 내부의 `fonts` 디렉터리에 배치
  * `src:[{path: './inter/Inter-Thin.ttf', weight: '100',},{path: './inter/Inter-Regular.ttf',weight: '400',},{path: './inter/Inter-Bold-Italic.ttf', weight: '700',style: 'italic',},]`
  * `app/page.tsx`에서 `src:'../styles/fonts/my-font.ttf'`로 폰트 로더 함수를 호출한다면, `my-font.ttf`는 프로젝트 루트의 `styles/fonts`에 위치

### `weight`[](https://nextjs.org/docs/app/api-reference/components/font#weight)

폰트의 [`weight`](https://fonts.google.com/knowledge/glossary/weight)를 다음과 같이 지정합니다.

  * 특정 폰트에서 사용 가능한 굵기 값 또는 [variable](https://fonts.google.com/variablefonts) 폰트인 경우 범위를 나타내는 문자열
  * 폰트가 [variable google font](https://fonts.google.com/variablefonts)가 아닐 때 굵기 값들의 배열. `next/font/google`에만 적용됩니다.

`next/font/google` 및 `next/font/local`에서 사용합니다.

  * 사용하는 폰트가 [variable](https://fonts.google.com/variablefonts)이 **아닐 때** 필수

예시:

  * `weight: '400'`: 단일 굵기를 나타내는 문자열. [`Inter`](https://fonts.google.com/specimen/Inter?query=inter)의 가능한 값은 `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'`, `'variable'`이며 기본값은 `'variable'`
  * `weight: '100 900'`: variable 폰트에서 `100`부터 `900`까지 범위를 나타내는 문자열
  * `weight: ['100','400','900']`: variable 폰트가 아닌 경우 가능한 3개의 값을 갖는 배열

### `style`[](https://nextjs.org/docs/app/api-reference/components/font#style)

폰트 [`style`](https://developer.mozilla.org/docs/Web/CSS/font-style)을 다음과 같이 지정합니다.

  * 기본값이 `'normal'`인 문자열 [value](https://developer.mozilla.org/docs/Web/CSS/font-style#values)
  * 폰트가 [variable google font](https://fonts.google.com/variablefonts)가 아닐 때 스타일 값 배열. `next/font/google`에만 적용됩니다.

`next/font/google` 및 `next/font/local`에서 사용합니다.

  * 선택 사항

예시:

  * `style: 'italic'`: 문자열. `next/font/google`에서는 `normal` 또는 `italic`
  * `style: 'oblique'`: 문자열. `next/font/local`에서는 어떤 값이든 사용할 수 있지만 [표준 폰트 스타일](https://developer.mozilla.org/docs/Web/CSS/font-style)에서 가져오는 것이 기대됩니다.
  * `style: ['italic','normal']`: `next/font/google`용 2개 값의 배열로, 값은 `normal`, `italic`

### `subsets`[](https://nextjs.org/docs/app/api-reference/components/font#subsets)

로드하려는 각 서브셋 이름을 문자열 배열로 정의한 폰트 [`subsets`](https://fonts.google.com/knowledge/glossary/subsetting)입니다. `subsets`로 지정된 폰트는 [`preload`](https://nextjs.org/docs/app/api-reference/components/font#preload) 옵션이 기본값 `true`일 때 head에 link preload 태그가 주입됩니다.

`next/font/google`에서 사용합니다.

  * 선택 사항

예시:

  * `subsets: ['latin']`: `latin` 서브셋 하나를 포함한 배열

Google Fonts의 해당 폰트 페이지에서 모든 서브셋 목록을 확인할 수 있습니다.

### `axes`[](https://nextjs.org/docs/app/api-reference/components/font#axes)

일부 variable 폰트에는 포함할 수 있는 추가 `axes`가 있습니다. 기본적으로는 파일 크기를 줄이기 위해 폰트 weight만 포함됩니다. 가능한 `axes` 값은 폰트별로 다릅니다.

`next/font/google`에서 사용합니다.

  * 선택 사항

예시:

  * `axes: ['slnt']`: `Inter` variable 폰트의 추가 `axes` 값인 `slnt`를 포함하는 배열. 가능한 `axes` 값은 [Google variable fonts 페이지](https://fonts.google.com/variablefonts#font-families)의 필터를 사용해 `wght` 외의 축을 확인할 수 있습니다.

### `display`[](https://nextjs.org/docs/app/api-reference/components/font#display)

폰트 [`display`](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display)를 `'auto'`, `'block'`, `'swap'`, `'fallback'`, `'optional'` 중 하나의 문자열 [values](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display#values)로 지정하며 기본값은 `'swap'`입니다.

`next/font/google` 및 `next/font/local`에서 사용합니다.

  * 선택 사항

예시:

  * `display: 'optional'`: `optional` 값으로 지정한 문자열

### `preload`[](https://nextjs.org/docs/app/api-reference/components/font#preload)

폰트를 [preload](https://nextjs.org/docs/app/api-reference/components/font#preloading)할지 여부를 지정하는 불리언 값입니다. 기본값은 `true`입니다.

`next/font/google` 및 `next/font/local`에서 사용합니다.

  * 선택 사항

예시:

  * `preload: false`

### `fallback`[](https://nextjs.org/docs/app/api-reference/components/font#fallback)

폰트를 로드할 수 없을 때 사용할 폰트입니다. 기본값 없이 폴백 폰트 문자열 배열로 지정합니다.

  * 선택 사항

`next/font/google` 및 `next/font/local`에서 사용합니다.

예시:

  * `fallback: ['system-ui', 'arial']`: 폴백 폰트를 `system-ui` 또는 `arial`로 설정하는 배열

### `adjustFontFallback`[](https://nextjs.org/docs/app/api-reference/components/font#adjustfontfallback)

  * `next/font/google`: 자동 폴백 폰트를 사용해 [Cumulative Layout Shift](https://web.dev/cls/)를 줄일지 여부를 설정하는 불리언 값. 기본값은 `true`.
  * `next/font/local`: 자동 폴백 폰트를 사용할지 여부를 설정하는 문자열 또는 불리언 `false`. 가능한 값은 `'Arial'`, `'Times New Roman'`, `false`. 기본값은 `'Arial'`.

`next/font/google` 및 `next/font/local`에서 사용합니다.

  * 선택 사항

예시:

  * `adjustFontFallback: false`: `next/font/google`용
  * `adjustFontFallback: 'Times New Roman'`: `next/font/local`용

### `variable`[](https://nextjs.org/docs/app/api-reference/components/font#variable)

[CSS 변수 방식](https://nextjs.org/docs/app/api-reference/components/font#css-variables)으로 스타일을 적용할 때 사용할 CSS 변수 이름을 정의하는 문자열 값입니다.

`next/font/google` 및 `next/font/local`에서 사용합니다.

  * 선택 사항

예시:

  * `variable: '--my-font'`: CSS 변수 `--my-font`를 선언

### `declarations`[](https://nextjs.org/docs/app/api-reference/components/font#declarations)

생성되는 `@font-face`를 추가로 정의하는 폰트 페이스 [descriptor](https://developer.mozilla.org/docs/Web/CSS/@font-face#descriptors) 키-값 쌍의 배열입니다.

`next/font/local`에서 사용합니다.

  * 선택 사항

예시:

  * `declarations: [{ prop: 'ascent-override', value: '90%' }]`

## Examples[](https://nextjs.org/docs/app/api-reference/components/font#examples)

## Google Fonts[](https://nextjs.org/docs/app/api-reference/components/font#google-fonts)

Google 폰트를 사용하려면 `next/font/google`에서 함수로 import하세요. 최고의 성능과 유연성을 위해 [variable fonts](https://fonts.google.com/variablefonts) 사용을 권장합니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import { Inter } from 'next/font/google'

    // If loading a variable font, you don't need to specify the font weight
    const inter = Inter({
      subsets: ['latin'],
      display: 'swap',
    })

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en" className={inter.className}>
          <body>{children}</body>
        </html>
      )
    }
[/code]

variable 폰트를 사용할 수 없다면 **weight를 지정해야 합니다**:

app/layout.tsx

JavaScriptTypeScript
[code]
    import { Roboto } from 'next/font/google'

    const roboto = Roboto({
      weight: '400',
      subsets: ['latin'],
      display: 'swap',
    })

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en" className={roboto.className}>
          <body>{children}</body>
        </html>
      )
    }
[/code]

배열을 사용해 여러 weight와/또는 style을 지정할 수도 있습니다.

app/layout.js
[code]
    const roboto = Roboto({
      weight: ['400', '700'],
      style: ['normal', 'italic'],
      subsets: ['latin'],
      display: 'swap',
    })
[/code]

> **알아두면 좋아요**: 여러 단어로 구성된 폰트 이름에는 밑줄(_)을 사용하세요. 예: `Roboto Mono`는 `Roboto_Mono`로 import해야 합니다.

### 서브셋 지정하기[](https://nextjs.org/docs/app/api-reference/components/font#specifying-a-subset)

Google Fonts는 자동으로 [서브셋](https://fonts.google.com/knowledge/glossary/subsetting) 처리됩니다. 이렇게 하면 폰트 파일 크기가 줄고 성능이 향상됩니다. 어떤 서브셋을 프리로드할지 직접 정의해야 하며, [`preload`](https://nextjs.org/docs/app/api-reference/components/font#preload)가 `true`인데 서브셋을 지정하지 않으면 경고가 발생합니다.

함수 호출에 다음과 같이 추가하면 됩니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    const inter = Inter({ subsets: ['latin'] })
[/code]

자세한 내용은 [Font API Reference](https://nextjs.org/docs/app/api-reference/components/font)를 확인하세요.

## 여러 폰트 사용하기[](https://nextjs.org/docs/app/api-reference/components/font#using-multiple-fonts)

애플리케이션에서 여러 폰트를 가져와 사용할 수 있습니다. 접근 방식은 두 가지입니다.

첫 번째 방법은 폰트를 내보내는 유틸리티 함수를 만든 뒤 필요한 곳에서 임포트하고 해당 `className`을 적용하는 것입니다. 이렇게 하면 렌더링될 때만 폰트가 프리로드됩니다.

app/fonts.ts

JavaScriptTypeScript
[code]
    import { Inter, Roboto_Mono } from 'next/font/google'

    export const inter = Inter({
      subsets: ['latin'],
      display: 'swap',
    })

    export const roboto_mono = Roboto_Mono({
      subsets: ['latin'],
      display: 'swap',
    })
[/code]

app/layout.tsx

JavaScriptTypeScript
[code]
    import { inter } from './fonts'

    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="en" className={inter.className}>
          <body>
            <div>{children}</div>
          </body>
        </html>
      )
    }
[/code]

app/page.tsx

JavaScriptTypeScript
[code]
    import { roboto_mono } from './fonts'

    export default function Page() {
      return (
        <>
          <h1 className={roboto_mono.className}>My page</h1>
        </>
      )
    }
[/code]

위 예제에서 `Inter`는 전역으로 적용되고, `Roboto Mono`는 필요한 곳에 임포트해 적용할 수 있습니다.

또는 [CSS 변수](https://nextjs.org/docs/app/api-reference/components/font#variable)를 만들어 선호하는 CSS 솔루션과 함께 사용할 수도 있습니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import { Inter, Roboto_Mono } from 'next/font/google'
    import styles from './global.css'

    const inter = Inter({
      subsets: ['latin'],
      variable: '--font-inter',
      display: 'swap',
    })

    const roboto_mono = Roboto_Mono({
      subsets: ['latin'],
      variable: '--font-roboto-mono',
      display: 'swap',
    })

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en" className={`${inter.variable} ${roboto_mono.variable}`}>
          <body>
            <h1>My App</h1>
            <div>{children}</div>
          </body>
        </html>
      )
    }
[/code]

app/global.css
[code]
    html {
      font-family: var(--font-inter);
    }

    h1 {
      font-family: var(--font-roboto-mono);
    }
[/code]

위 예제에서 `Inter`는 전역에 적용되고, 모든 `<h1>` 태그는 `Roboto Mono`로 스타일링됩니다.

> **Recommendation** : 여러 폰트를 사용할수록 클라이언트가 내려받아야 하는 리소스가 늘어나므로 신중하게 추가하는 것이 좋습니다.

### 로컬 폰트[](https://nextjs.org/docs/app/api-reference/components/font#local-fonts)

`next/font/local`을 임포트하고 로컬 폰트 파일의 `src`를 지정하세요. 최고의 성능과 유연성을 위해 [가변 폰트](https://fonts.google.com/variablefonts)를 권장합니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import localFont from 'next/font/local'

    // Font files can be colocated inside of `app`
    const myFont = localFont({
      src: './my-font.woff2',
      display: 'swap',
    })

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en" className={myFont.className}>
          <body>{children}</body>
        </html>
      )
    }
[/code]

단일 폰트 패밀리에 여러 파일을 사용하려면 `src`를 배열로 지정할 수 있습니다:
[code]
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
[/code]

자세한 내용은 [Font API Reference](https://nextjs.org/docs/app/api-reference/components/font)를 참고하세요.

### Tailwind CSS와 함께 사용하기[](https://nextjs.org/docs/app/api-reference/components/font#with-tailwind-css)

`next/font`는 [CSS 변수](https://nextjs.org/docs/app/api-reference/components/font#css-variables)를 사용해 [Tailwind CSS](https://tailwindcss.com/)와 매끄럽게 통합됩니다.

아래 예제에서는 `next/font/google`의 `Inter`와 `Roboto_Mono`를 사용하지만, 어떤 Google Font나 로컬 폰트도 사용할 수 있습니다. `variable` 옵션으로 CSS 변수 이름(예: `inter`, `roboto_mono`)을 정의한 후, `inter.variable`과 `roboto_mono.variable`을 HTML 문서에 적용해 CSS 변수를 포함시킵니다.

> **Good to know** : 필요와 선호도에 따라 이 변수들을 `<html>` 또는 `<body>` 태그에 추가할 수 있습니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import { Inter, Roboto_Mono } from 'next/font/google'

    const inter = Inter({
      subsets: ['latin'],
      display: 'swap',
      variable: '--font-inter',
    })

    const roboto_mono = Roboto_Mono({
      subsets: ['latin'],
      display: 'swap',
      variable: '--font-roboto-mono',
    })

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html
          lang="en"
          className={`${inter.variable} ${roboto_mono.variable} antialiased`}
        >
          <body>{children}</body>
        </html>
      )
    }
[/code]

마지막으로 [Tailwind CSS 설정](https://nextjs.org/docs/app/getting-started/css#tailwind-css)에 CSS 변수를 추가합니다:

global.css
[code]
    @import 'tailwindcss';

    @theme inline {
      --font-sans: var(--font-inter);
      --font-mono: var(--font-roboto-mono);
    }
[/code]

### Tailwind CSS v3[](https://nextjs.org/docs/app/api-reference/components/font#tailwind-css-v3)

tailwind.config.js
[code]
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
[/code]

이제 `font-sans`, `font-mono` 유틸리티 클래스를 사용해 요소에 폰트를 적용할 수 있습니다.
[code]
    <p class="font-sans ...">The quick brown fox ...</p>
    <p class="font-mono ...">The quick brown fox ...</p>
[/code]

### 스타일 적용하기[](https://nextjs.org/docs/app/api-reference/components/font#applying-styles)

폰트 스타일은 세 가지 방식으로 적용할 수 있습니다.

  * [`className`](https://nextjs.org/docs/app/api-reference/components/font#classname)
  * [`style`](https://nextjs.org/docs/app/api-reference/components/font#style-1)
  * [CSS Variables](https://nextjs.org/docs/app/api-reference/components/font#css-variables)

#### `className`[](https://nextjs.org/docs/app/api-reference/components/font#classname)

로드된 폰트를 HTML 요소에 전달할 수 있는 읽기 전용 CSS `className`을 반환합니다.
[code]
    <p className={inter.className}>Hello, Next.js!</p>
[/code]

#### `style`[](https://nextjs.org/docs/app/api-reference/components/font#style-1)

로드된 폰트를 HTML 요소에 전달할 수 있는 읽기 전용 CSS `style` 객체를 반환하며, `style.fontFamily`를 통해 폰트 패밀리 이름과 폴백 폰트에 접근할 수 있습니다.
[code]
    <p style={inter.style}>Hello World</p>
[/code]

#### CSS Variables[](https://nextjs.org/docs/app/api-reference/components/font#css-variables)

외부 스타일시트에서 스타일을 설정하고 추가 옵션을 지정하려면 CSS 변수 방식을 사용하세요.

폰트를 임포트하는 것과 함께, CSS 변수가 정의된 CSS 파일도 임포트하고 폰트 로더 객체의 variable 옵션을 다음과 같이 설정합니다:

app/page.tsx

JavaScriptTypeScript
[code]
    import { Inter } from 'next/font/google'
    import styles from '../styles/component.module.css'

    const inter = Inter({
      variable: '--font-inter',
    })
[/code]

폰트를 사용하려면 스타일링하려는 텍스트의 부모 컨테이너 `className`을 폰트 로더의 `variable` 값으로 지정하고, 텍스트의 `className`을 외부 CSS 파일의 `styles` 속성으로 설정합니다.

app/page.tsx

JavaScriptTypeScript
[code]
    <main className={inter.variable}>
      <p className={styles.text}>Hello World</p>
    </main>
[/code]

`component.module.css` CSS 파일에서 `text` 셀렉터 클래스를 다음과 같이 정의합니다:

styles/component.module.css
[code]
    .text {
      font-family: var(--font-inter);
      font-weight: 200;
      font-style: italic;
    }
[/code]

이 예제에서는 `Hello World` 텍스트가 `Inter` 폰트와 생성된 폰트 폴백을 사용하여 `font-weight: 200`, `font-style: italic`으로 스타일링됩니다.

### 폰트 정의 파일 사용하기[](https://nextjs.org/docs/app/api-reference/components/font#using-a-font-definitions-file)

`localFont`나 Google 폰트 함수를 호출할 때마다 해당 폰트는 애플리케이션 내 하나의 인스턴스로 호스팅됩니다. 따라서 동일한 폰트를 여러 곳에서 사용해야 한다면 한 곳에서 로드하고 필요한 곳에서 관련 폰트 객체를 임포트해야 합니다. 이를 위해 폰트 정의 파일을 사용합니다.

예를 들어 앱 디렉터리 루트의 `styles` 폴더에 `fonts.ts` 파일을 만듭니다.

그런 다음 폰트 정의를 아래와 같이 지정합니다:

styles/fonts.ts

JavaScriptTypeScript
[code]
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
[/code]

이제 코드에서 다음과 같이 정의를 사용할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
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
[/code]

코드에서 폰트 정의에 쉽게 접근하려면 `tsconfig.json` 또는 `jsconfig.json` 파일에 다음과 같이 경로 별칭을 정의할 수 있습니다:

tsconfig.json
[code]
    {
      "compilerOptions": {
        "paths": {
          "@/fonts": ["./styles/fonts"]
        }
      }
    }
[/code]

You can now import any font definition as follows:

app/about/page.tsx

JavaScriptTypeScript
[code]
    import { greatVibes, sourceCodePro400 } from '@/fonts'
[/code]

### 프리로딩[](https://nextjs.org/docs/app/api-reference/components/font#preloading)

사이트의 페이지에서 폰트 함수를 호출하면, 해당 폰트는 모든 라우트에서 전역으로 사용 가능하거나 프리로딩되지 않습니다. 대신, 사용된 파일 유형에 따라 관련 라우트에서만 프리로딩됩니다:

  * [고유 페이지](https://nextjs.org/docs/app/api-reference/file-conventions/page)라면, 그 페이지의 고유 라우트에서 프리로딩됩니다.
  * [레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout)이라면, 해당 레이아웃이 감싸는 모든 라우트에서 프리로딩됩니다.
  * [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)이라면, 모든 라우트에서 프리로딩됩니다.

## 버전 변경 사항[](https://nextjs.org/docs/app/api-reference/components/font#version-changes)

Version| Changes
---|---
`v13.2.0`| `@next/font`가 `next/font`로 이름이 변경되었습니다. 설치가 더 이상 필요하지 않습니다.
`v13.0.0`| `@next/font`가 추가되었습니다.

Send
