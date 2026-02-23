---
title: 'Document에서 Head 임포트 금지'
description: '원본 URL: https://nextjs.org/docs/messages/no-head-import-in-document'
---

# Document에서 Head 임포트 금지 | Next.js

원본 URL: https://nextjs.org/docs/messages/no-head-import-in-document

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)Document에서 Head 임포트 금지

# Document에서 Head 임포트 금지

> `pages/_document.js`에서 `next/head` 사용을 방지합니다.

## 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-head-import-in-document#why-this-error-occurred)

`pages/_document.js`에서 `next/head`를 임포트했습니다. 이로 인해 애플리케이션에서 예상치 못한 문제가 발생할 수 있습니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-head-import-in-document#possible-ways-to-fix-it)

기본 `Document` 컴포넌트를 오버라이드하려면 `pages/_document.js`에서 `next/document`만 임포트하고 사용하세요. 모든 페이지에서 `<head>` 코드를 수정하려고 `Head` 컴포넌트를 사용하기 위해 `next/head`를 임포트하고 있다면, 대신 `next/document`에서 임포트하세요.

pages/_document.js
```js
import Document, { Html, Head, Main, NextScript } from 'next/document'
 
class MyDocument extends Document {
  static async getInitialProps(ctx) {
    //...
  }
 
  render() {
    return (
      <Html>
        <Head></Head>
      </Html>
    )
  }
}
 
export default MyDocument
```

## 유용한 링크[](https://nextjs.org/docs/messages/no-head-import-in-document#useful-links)

- [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)

도움이 되었나요?

지원됨.

보내기
