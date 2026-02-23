---
title: '라우팅: Custom Document'
description: '커스텀 는 Page를 렌더링할 때 사용되는  및  태그를 업데이트할 수 있습니다.'
---

# 라우팅: Custom Document | Next.js

소스 URL: https://nextjs.org/docs/pages/building-your-application/routing/custom-document

[Building Your Application](https://nextjs.org/docs/pages/building-your-application/routing) [Routing](https://nextjs.org/docs/pages/building-your-application/routing) Custom Document

# Custom Document

2026년 2월 20일 업데이트

커스텀 `Document`는 [Page](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)를 렌더링할 때 사용되는 `<html>` 및 `<body>` 태그를 업데이트할 수 있습니다.

기본 `Document`를 재정의하려면 아래와 같이 `pages/_document` 파일을 생성하세요:

pages/_document.tsx

JavaScriptTypeScript
```
    import { Html, Head, Main, NextScript } from 'next/document'

    export default function Document() {
      return (
        <Html lang="en">
          <Head />
          <body>
            <Main />
            <NextScript />
          </body>
        </Html>
      )
    }
```

> **알아두면 좋아요** :
>
>   * `_document`는 서버에서만 렌더링되므로 `onClick`과 같은 이벤트 핸들러는 이 파일에서 사용할 수 없습니다.
>   * `<Html>`, `<Head />`, `<Main />`, `<NextScript />`는 페이지가 올바르게 렌더링되도록 필수입니다.
>

## 주의 사항[](https://nextjs.org/docs/pages/building-your-application/routing/custom-document#caveats)

  * `_document`에서 사용하는 `<Head />` 컴포넌트는 [`next/head`](https://nextjs.org/docs/pages/api-reference/components/head)와 동일하지 않습니다. 여기서 사용하는 `<Head />`는 모든 페이지에 공통으로 들어가는 `<head>` 코드를 위해서만 사용해야 합니다. `<title>` 태그와 같은 다른 경우에는 페이지나 컴포넌트에서 [`next/head`](https://nextjs.org/docs/pages/api-reference/components/head)를 사용하는 것이 좋습니다.
  * `<Main />` 외부의 React 컴포넌트는 브라우저에서 초기화되지 않습니다. 이 영역에 애플리케이션 로직이나 커스텀 CSS(`styled-jsx` 등)를 추가하지 마세요. 모든 페이지에서 공유되는 컴포넌트(예: 메뉴, 툴바)가 필요하다면 [Layouts](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)를 참고하세요.
  * 현재 `Document`는 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)나 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) 같은 Next.js [데이터 패칭 메서드](https://nextjs.org/docs/pages/building-your-application/data-fetching)를 지원하지 않습니다.

## `renderPage` 커스터마이징[](https://nextjs.org/docs/pages/building-your-application/routing/custom-document#customizing-renderpage)

`renderPage`를 커스터마이징하는 작업은 고급 사용 사례이며, 서버 사이드 렌더링을 지원해야 하는 CSS-in-JS 같은 라이브러리에서만 필요합니다. 기본 제공 `styled-jsx` 지원에는 필요하지 않습니다.

**이 패턴 사용은 권장하지 않습니다.** 대신 페이지와 레이아웃에서 데이터를 보다 쉽게 가져올 수 있는 App Router를 [점진적으로 도입](https://nextjs.org/docs/app/guides/migrating/app-router-migration)하는 방안을 고려하세요.

pages/_document.tsx

JavaScriptTypeScript
```
    import Document, {
      Html,
      Head,
      Main,
      NextScript,
      DocumentContext,
      DocumentInitialProps,
    } from 'next/document'

    class MyDocument extends Document {
      static async getInitialProps(
        ctx: DocumentContext
      ): Promise<DocumentInitialProps> {
        const originalRenderPage = ctx.renderPage

        // Run the React rendering logic synchronously
        ctx.renderPage = () =>
          originalRenderPage({
            // Useful for wrapping the whole react tree
            enhanceApp: (App) => App,
            // Useful for wrapping in a per-page basis
            enhanceComponent: (Component) => Component,
          })

        // Run the parent `getInitialProps`, it now includes the custom `renderPage`
        const initialProps = await Document.getInitialProps(ctx)

        return initialProps
      }

      render() {
        return (
          <Html lang="en">
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
```

> **알아두면 좋아요** :
>
>   * `_document`의 `getInitialProps`는 클라이언트 사이드 전환 동안 호출되지 않습니다.
>   * `_document`용 `ctx` 객체는 [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props#context-object)에서 받는 것과 동일하지만, `renderPage`가 추가됩니다.
>

보내기