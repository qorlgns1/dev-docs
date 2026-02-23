---
title: '인라인 스크립트 ID'
description: '> 인라인 콘텐츠가 있는  컴포넌트에는  속성을 강제합니다.'
---

# 인라인 스크립트 ID | Next.js

출처 URL: https://nextjs.org/docs/messages/inline-script-id

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)인라인 스크립트 ID

# 인라인 스크립트 ID

> 인라인 콘텐츠가 있는 `next/script` 컴포넌트에는 `id` 속성을 강제합니다.

## 왜 이 오류가 발생했나요?[](https://nextjs.org/docs/messages/inline-script-id#why-this-error-occurred)

인라인 콘텐츠를 포함한 `next/script` 컴포넌트는 스크립트를 추적하고 최적화하기 위해 `id` 속성을 정의해야 합니다.

## 해결 방법[](https://nextjs.org/docs/messages/inline-script-id#possible-ways-to-fix-it)

`next/script` 컴포넌트에 `id` 속성을 추가하세요.

pages/_app.js
```
    import Script from 'next/script'

    export default function App({ Component, pageProps }) {
      return (
        <>
          <Script id="my-script">{`console.log('Hello world!');`}</Script>
          <Component {...pageProps} />
        </>
      )
    }
```

## 유용한 링크[](https://nextjs.org/docs/messages/inline-script-id#useful-links)

  * [Next.js Script 컴포넌트 문서](https://nextjs.org/docs/pages/guides/scripts)