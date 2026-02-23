---
title: '시작하기: 폰트'
description: '마지막 업데이트: 2026년 2월 20일'
---

# 시작하기: 폰트 | Next.js

Source URL: https://nextjs.org/docs/pages/getting-started/fonts

[Pages Router](https://nextjs.org/docs/pages)[Getting Started](https://nextjs.org/docs/pages/getting-started)Fonts

Copy page

# 폰트 사용 방법

마지막 업데이트: 2026년 2월 20일

[`next/font`](https://nextjs.org/docs/app/api-reference/components/font) 모듈은 폰트를 자동으로 최적화하고 외부 네트워크 요청을 제거해 프라이버시와 성능을 향상시킵니다.

이 모듈에는 모든 폰트 파일에 대한 **내장 셀프 호스팅** 기능이 포함되어 있어, 레이아웃 시프트 없이 웹 폰트를 최적으로 로드할 수 있습니다.

`next/font` 사용을 시작하려면 [`next/font/local`](https://nextjs.org/docs/pages/getting-started/fonts#local-fonts) 또는 [`next/font/google`](https://nextjs.org/docs/pages/getting-started/fonts#google-fonts)에서 임포트한 뒤 적절한 옵션으로 함수를 호출하고, 폰트를 적용할 요소의 `className`을 설정하세요. 예를 들어 [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) (`pages/_app`)에서 전역으로 폰트를 적용할 수 있습니다.

pages/_app.tsx

JavaScriptTypeScript
[code]
    import { Geist } from 'next/font/google'
    import type { AppProps } from 'next/app'
     
    const geist = Geist({
      subsets: ['latin'],
    })
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return (
        <main className={geist.className}>
          <Component {...pageProps} />
        </main>
      )
    }
[/code]

`<html>` 요소에 폰트를 적용하려면 [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document) (`pages/_document`)를 사용할 수 있습니다.

pages/_document.tsx

JavaScriptTypeScript
[code]
    import { Html, Head, Main, NextScript } from 'next/document'
    import { Geist } from 'next/font/google'
     
    const geist = Geist({
      subsets: ['latin'],
    })
     
    export default function Document() {
      return (
        <Html lang="en" className={geist.className}>
          <Head />
          <body>
            <Main />
            <NextScript />
          </body>
        </Html>
      )
    }
[/code]

## Google 폰트[](https://nextjs.org/docs/pages/getting-started/fonts#google-fonts)

모든 Google Font를 자동으로 셀프 호스팅할 수 있습니다. 폰트는 정적 자산으로 포함되어 배포와 동일한 도메인에서 제공되므로, 사용자가 사이트를 방문해도 브라우저가 Google로 요청을 보내지 않습니다.

Google Font를 사용하려면 `next/font/google`에서 원하는 폰트를 임포트하세요.

pages/_app.tsx

JavaScriptTypeScript
[code]
    import { Geist } from 'next/font/google'
    import type { AppProps } from 'next/app'
     
    const geist = Geist({
      subsets: ['latin'],
    })
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return (
        <main className={geist.className}>
          <Component {...pageProps} />
        </main>
      )
    }
[/code]

최고의 성능과 유연성을 위해 [variable fonts](https://fonts.google.com/variablefonts)를 사용할 것을 권장합니다. variable font를 사용할 수 없는 경우 가중치를 지정해야 합니다.

pages/_app.tsx

JavaScriptTypeScript
[code]
    import { Roboto } from 'next/font/google'
    import type { AppProps } from 'next/app'
     
    const roboto = Roboto({
      weight: '400',
      subsets: ['latin'],
    })
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return (
        <main className={roboto.className}>
          <Component {...pageProps} />
        </main>
      )
    }
[/code]

## 로컬 폰트[](https://nextjs.org/docs/pages/getting-started/fonts#local-fonts)

로컬 폰트를 사용하려면 `next/font/local`에서 폰트를 임포트하고 로컬 폰트 파일의 [`src`](https://nextjs.org/docs/pages/api-reference/components/font#src)를 지정하세요. 폰트는 [`public`](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder) 폴더나 `pages` 폴더 안에 저장할 수 있습니다. 예시는 다음과 같습니다.

pages/_app.tsx

JavaScriptTypeScript
[code]
    import localFont from 'next/font/local'
    import type { AppProps } from 'next/app'
     
    const myFont = localFont({
      src: './my-font.woff2',
    })
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return (
        <main className={myFont.className}>
          <Component {...pageProps} />
        </main>
      )
    }
[/code]

하나의 폰트 패밀리에 여러 파일을 사용하려면 `src`를 배열로 지정할 수 있습니다.
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

## API Reference

Next.js Font의 전체 기능을 확인하려면 API Reference를 참고하세요.

### [Font 모듈용 FontAPI Reference](https://nextjs.org/docs/pages/api-reference/components/font)

도움이 되었나요?

supported.

Send
