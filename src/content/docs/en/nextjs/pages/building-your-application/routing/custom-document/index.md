---
title: 'Routing: Custom Document'
description: 'A custom  can update the  and  tags used to render a Page.'
---

# Routing: Custom Document | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/routing/custom-document

[Building Your Application](https://nextjs.org/docs/pages/building-your-application)[Routing](https://nextjs.org/docs/pages/building-your-application/routing)Custom Document

Copy page

# Custom Document

Last updated February 20, 2026

A custom `Document` can update the `<html>` and `<body>` tags used to render a [Page](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts).

To override the default `Document`, create the file `pages/_document` as shown below:

pages/_document.tsx

JavaScriptTypeScript
[code]
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
[/code]

> **Good to know** :
> 
>   * `_document` is only rendered on the server, so event handlers like `onClick` cannot be used in this file.
>   * `<Html>`, `<Head />`, `<Main />` and `<NextScript />` are required for the page to be properly rendered.
> 


## Caveats[](https://nextjs.org/docs/pages/building-your-application/routing/custom-document#caveats)

  * The `<Head />` component used in `_document` is not the same as [`next/head`](https://nextjs.org/docs/pages/api-reference/components/head). The `<Head />` component used here should only be used for any `<head>` code that is common for all pages. For all other cases, such as `<title>` tags, we recommend using [`next/head`](https://nextjs.org/docs/pages/api-reference/components/head) in your pages or components.
  * React components outside of `<Main />` will not be initialized by the browser. Do _not_ add application logic here or custom CSS (like `styled-jsx`). If you need shared components in all your pages (like a menu or a toolbar), read [Layouts](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern) instead.
  * `Document` currently does not support Next.js [Data Fetching methods](https://nextjs.org/docs/pages/building-your-application/data-fetching) like [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) or [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props).



## Customizing `renderPage`[](https://nextjs.org/docs/pages/building-your-application/routing/custom-document#customizing-renderpage)

Customizing `renderPage` is advanced and only needed for libraries like CSS-in-JS to support server-side rendering. This is not needed for built-in `styled-jsx` support.

**We do not recommend using this pattern.** Instead, consider [incrementally adopting](https://nextjs.org/docs/app/guides/migrating/app-router-migration) the App Router, which allows you to more easily fetch data for pages and layouts.

pages/_document.tsx

JavaScriptTypeScript
[code]
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
[/code]

> **Good to know** :
> 
>   * `getInitialProps` in `_document` is not called during client-side transitions.
>   * The `ctx` object for `_document` is equivalent to the one received in [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props#context-object), with the addition of `renderPage`.
> 


Was this helpful?

supported.

Send
