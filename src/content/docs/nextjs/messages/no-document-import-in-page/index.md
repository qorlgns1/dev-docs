---
title: '페이지에서 Document 가져오기 금지'
description: '를 (TypeScript를 사용하는 경우 ) 외부의 페이지에서 가져왔습니다. 이는 애플리케이션에서 예기치 않은 문제를 유발할 수 있습니다.'
---

# 페이지에서 Document 가져오기 금지 | Next.js

Source URL: https://nextjs.org/docs/messages/no-document-import-in-page

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)페이지에서 Document 가져오기 금지

# 페이지에서 Document 가져오기 금지

> `pages/_document.js` 밖에서 `next/document`를 가져오지 마세요.

## 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-document-import-in-page#why-this-error-occurred)

`next/document`를 `pages/_document.js`(TypeScript를 사용하는 경우 `pages/_document.tsx`) 외부의 페이지에서 가져왔습니다. 이는 애플리케이션에서 예기치 않은 문제를 유발할 수 있습니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-document-import-in-page#possible-ways-to-fix-it)

기본 `Document` 컴포넌트를 재정의하려면 `next/document`를 `pages/_document.js`(또는 `pages/_document.tsx`) 내부에서만 가져와 사용하세요:

pages/_document.js
```
    import Document, { Html, Head, Main, NextScript } from 'next/document'

    class MyDocument extends Document {
      //...
    }

    export default MyDocument
```

## 유용한 링크[](https://nextjs.org/docs/messages/no-document-import-in-page#useful-links)

  * [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)

이 정보가 도움이 되었나요?

supported.

Send