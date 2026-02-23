---
title: '문서 밖에서 Before Interactive Script 사용 금지'
description: '>  또는  외부에서 의  전략 사용을 방지합니다.'
---

# 문서 밖에서 Before Interactive Script 사용 금지 | Next.js

출처 URL: https://nextjs.org/docs/messages/no-before-interactive-script-outside-document

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)문서 밖에서 Before Interactive Script 사용 금지

# 문서 밖에서 Before Interactive Script 사용 금지

> `app/layout.jsx` 또는 `pages/_document.js` 외부에서 `next/script`의 `beforeInteractive` 전략 사용을 방지합니다.

## 왜 이 오류가 발생했나요[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#why-this-error-occurred)

`beforeInteractive` 전략의 `next/script` 컴포넌트는 `app/layout.jsx` 또는 `pages/_document.js` 밖에서 사용할 수 없습니다. 이는 `beforeInteractive` 전략이 **`app/layout.jsx`** 또는 **`pages/_document.js`** 내부에서만 작동하며, 전체 사이트에 필요한 스크립트를 로드하도록 설계되었기 때문입니다(즉, 애플리케이션의 어떤 페이지라도 서버 측에서 로드되면 스크립트가 로드됩니다).

## 가능한 해결 방법[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#possible-ways-to-fix-it)

### App Router[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#app-router)

글로벌 스크립트가 필요하고 App Router를 사용 중이라면, 스크립트를 `app/layout.jsx` 내부로 이동하세요.

app/layout.jsx
```
    import Script from 'next/script'

    export default function RootLayout({ children }) {
      return (
        <html lang="en">
          <body>{children}</body>
          <Script
            src="https://example.com/script.js"
            strategy="beforeInteractive"
          />
        </html>
      )
    }
```

### Pages Router[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#pages-router)

글로벌 스크립트가 필요하고 Pages Router를 사용 중이라면, 스크립트를 `pages/_document.js` 내부로 이동하세요.

pages/_document.js
```
    import { Html, Head, Main, NextScript } from 'next/document'
    import Script from 'next/script'

    export default function Document() {
      return (
        <Html>
          <Head />
          <body>
            <Main />
            <NextScript />
            <Script
              src="https://example.com/script.js"
              strategy="beforeInteractive"
            ></Script>
          </body>
        </Html>
      )
    }
```

## 유용한 링크[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#useful-links)

  * [App Router 스크립트 최적화](https://nextjs.org/docs/app/guides/scripts)
  * [Pages Router 스크립트 최적화](https://nextjs.org/docs/pages/guides/scripts)

보내기
