---
title: '_document에서 styled-jsx 사용 금지'
description: '> 에서 를 사용하는 것을 방지하세요.'
---

# `_document`에서 `styled-jsx` 사용 금지 | Next.js

출처 URL: https://nextjs.org/docs/messages/no-styled-jsx-in-document

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)`_document`에서 `styled-jsx` 사용 금지

# `_document`에서 `styled-jsx` 사용 금지

> `pages/_document.js`에서 `styled-jsx`를 사용하는 것을 방지하세요.

## 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-styled-jsx-in-document#why-this-error-occurred)

[Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)에서는 `styled-jsx`와 같은 커스텀 CSS를 사용할 수 없습니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-styled-jsx-in-document#possible-ways-to-fix-it)

모든 페이지에서 공유할 CSS가 필요하다면 [Custom `App`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) 파일을 참고하거나 커스텀 레이아웃을 정의하세요.

예를 들어 `styles.css`라는 다음 스타일시트를 살펴보세요:

styles.css
[code]
    body {
      font-family:
        'SF Pro Text', 'SF Pro Icons', 'Helvetica Neue', 'Helvetica', 'Arial',
        sans-serif;
      padding: 20px 20px 60px;
      max-width: 680px;
      margin: 0 auto;
    }
[/code]

아직 없다면 `pages/_app.{js,tsx}` 파일을 생성한 뒤 `styles.css` 파일을 import하세요.

pages/_app.js
[code]
    import '../styles.css'
     
    // This default export is required in a new `pages/_app.js` file.
    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

이 스타일(`styles.css`)은 애플리케이션의 모든 페이지와 컴포넌트에 적용됩니다.

## 유용한 링크[](https://nextjs.org/docs/messages/no-styled-jsx-in-document#useful-links)

  * [Custom Document 주의 사항](https://nextjs.org/docs/pages/building-your-application/routing/custom-document#caveats)
  * [레이아웃](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)
  * [내장 CSS 지원](https://nextjs.org/docs/app/getting-started/css)
  * [Custom `App`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)



도움이 되었나요?

지원됨.

보내기
