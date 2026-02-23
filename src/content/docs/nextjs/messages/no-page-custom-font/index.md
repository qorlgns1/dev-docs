---
title: '페이지 전용 커스텀 폰트 없음'
description: '> 페이지에만 적용되는 커스텀 폰트를 방지하세요.'
---

# 페이지 전용 커스텀 폰트 없음 | Next.js

Source URL: https://nextjs.org/docs/messages/no-page-custom-font

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)페이지 전용 커스텀 폰트 없음

# 페이지 전용 커스텀 폰트 없음

> 페이지에만 적용되는 커스텀 폰트를 방지하세요.

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-page-custom-font#why-this-error-occurred)

  * 추가하려는 커스텀 폰트를 개별 페이지에만 추가했습니다. 이 경우 해당 페이지에만 폰트가 적용되고 애플리케이션 전체에는 적용되지 않습니다.
  * 추가하려는 커스텀 폰트를 `pages/_document.js` 내부의 별도 컴포넌트에 추가했습니다. 이 방식은 자동 폰트 최적화를 비활성화합니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/no-page-custom-font#possible-ways-to-fix-it)

`./pages/_document.js` 파일을 만들고 커스텀 Document에 폰트를 추가합니다:

pages/_document.js
```
    import Document, { Html, Head, Main, NextScript } from 'next/document'

    class MyDocument extends Document {
      render() {
        return (
          <Html>
            <Head>
              <link
                href="https://fonts.googleapis.com/css2?family=Inter&display=optional"
                rel="stylesheet"
              />
            </Head>
            <body>
              <Main />
              <NextScript />
            </body>
          </Html>
        )
      }
    }

    export default MyDocument
```

또는 함수 컴포넌트로 작성할 수도 있습니다:

pages/_document.js
```
    import { Html, Head, Main, NextScript } from 'next/document'

    export default function Document() {
      return (
        <Html>
          <Head>
            <link
              href="https://fonts.googleapis.com/css2?family=Inter&display=optional"
              rel="stylesheet"
            />
          </Head>
          <body>
            <Main />
            <NextScript />
          </body>
        </Html>
      )
    }
```

### 사용하지 않아도 되는 경우[](https://nextjs.org/docs/messages/no-page-custom-font#when-not-to-use-it)

특정 페이지에서만 폰트를 로드해야 하거나 폰트 최적화가 중요하지 않다면, 이 규칙을 비활성화해도 됩니다.

## 유용한 링크[](https://nextjs.org/docs/messages/no-page-custom-font#useful-links)

  * [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)
  * [Font Optimization](https://nextjs.org/docs/pages/api-reference/components/font)

Send