---
title: '중복된 Head 없음'
description: '사용자 정의 문서에서  컴포넌트를 두 번 이상 사용했습니다. 이는 애플리케이션에서 예상치 못한 동작을 일으킬 수 있습니다.'
---

# 중복된 Head 없음 | Next.js

출처 URL: https://nextjs.org/docs/messages/no-duplicate-head

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)중복된 Head 없음

# 중복된 Head 없음

> `pages/_document.js`에서 `<Head>`의 중복 사용을 방지하세요.

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-duplicate-head#why-this-error-occurred)

사용자 정의 문서에서 `<Head />` 컴포넌트를 두 번 이상 사용했습니다. 이는 애플리케이션에서 예상치 못한 동작을 일으킬 수 있습니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-duplicate-head#possible-ways-to-fix-it)

`pages/_document.js`의 사용자 정의 문서에서 `<Head />` 컴포넌트를 하나만 사용하세요.

pages/_document.js
[code]
    import Document, { Html, Head, Main, NextScript } from 'next/document'

    class MyDocument extends Document {
      static async getInitialProps(ctx) {
        //...
      }

      render() {
        return (
          <Html>
            <Head />
            <body>
              <Main />
              <NextScript />
            </body>
          </Html>
        )
      }
    }

    export default MyDocument
[/code]

## 유용한 링크[](https://nextjs.org/docs/messages/no-duplicate-head#useful-links)

  * [사용자 정의 Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)

보내기
