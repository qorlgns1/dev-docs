---
title: '시작하기: 폰트 최적화'
description: '마지막 업데이트 2026년 2월 20일'
---

# 시작하기: 폰트 최적화 | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/fonts

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Font Optimization

Copy page

# 폰트 최적화

마지막 업데이트 2026년 2월 20일

[`next/font`](https://nextjs.org/docs/app/api-reference/components/font) 모듈은 폰트를 자동으로 최적화하고 외부 네트워크 요청을 제거하여 개인정보 보호와 성능을 향상합니다.

이 모듈은 모든 폰트 파일에 대한 **내장형 자체 호스팅**을 포함합니다. 즉, 레이아웃 시프트 없이 웹 폰트를 최적으로 로드할 수 있습니다.

`next/font`를 사용하려면 [`next/font/local`](https://nextjs.org/docs/app/getting-started/fonts#local-fonts) 또는 [`next/font/google`](https://nextjs.org/docs/app/getting-started/fonts#google-fonts)에서 임포트하고, 적절한 옵션으로 함수처럼 호출한 다음 폰트를 적용할 요소의 `className`을 설정하면 됩니다. 예시는 다음과 같습니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import { Geist } from 'next/font/google'
     
    const geist = Geist({
      subsets: ['latin'],
    })
     
    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="en" className={geist.className}>
          <body>{children}</body>
        </html>
      )
    }
[/code]

폰트는 사용되는 컴포넌트 범위에만 적용됩니다. 전체 애플리케이션에 폰트를 적용하려면 [Root Layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)에 추가하세요.

## Google 폰트[](https://nextjs.org/docs/app/getting-started/fonts#google-fonts)

모든 Google Font를 자동으로 자체 호스팅할 수 있습니다. 폰트는 정적 자산으로 포함되어 배포 도메인과 동일한 도메인에서 제공되므로, 사용자가 사이트를 방문할 때 브라우저가 Google로 요청을 보내지 않습니다.

Google Font 사용을 시작하려면 `next/font/google`에서 원하는 폰트를 임포트하세요:

app/layout.tsx

JavaScriptTypeScript
[code]
    import { Geist } from 'next/font/google'
     
    const geist = Geist({
      subsets: ['latin'],
    })
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en" className={geist.className}>
          <body>{children}</body>
        </html>
      )
    }
[/code]

최상의 성능과 유연성을 위해 [variable fonts](https://fonts.google.com/variablefonts) 사용을 권장합니다. variable font를 사용할 수 없다면 `weight`를 지정해야 합니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import { Roboto } from 'next/font/google'
     
    const roboto = Roboto({
      weight: '400',
      subsets: ['latin'],
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

## 로컬 폰트[](https://nextjs.org/docs/app/getting-started/fonts#local-fonts)

로컬 폰트를 사용하려면 `next/font/local`에서 폰트를 임포트하고 로컬 폰트 파일의 [`src`](https://nextjs.org/docs/app/api-reference/components/font#src)를 지정하세요. 폰트는 [`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) 폴더 또는 `app` 폴더 내부에 함께 둘 수 있습니다. 예시는 다음과 같습니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import localFont from 'next/font/local'
     
    const myFont = localFont({
      src: './my-font.woff2',
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

## API Reference

Next.js Font의 전체 기능 세트는 API Reference를 확인하세요.

### [FontOptimizing loading web fonts with the built-in `next/font` loaders.](https://nextjs.org/docs/app/api-reference/components/font)

Was this helpful?

supported.

Send
