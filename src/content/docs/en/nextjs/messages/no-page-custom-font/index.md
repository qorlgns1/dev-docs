---
title: 'No Page Custom Font'
description: '> Prevent page-only custom fonts.'
---

# No Page Custom Font | Next.js

Source URL: https://nextjs.org/docs/messages/no-page-custom-font

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Page Custom Font

# No Page Custom Font

> Prevent page-only custom fonts.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-page-custom-font#why-this-error-occurred)

  * The custom font you're adding was added to a page - this only adds the font to the specific page and not the entire application.
  * The custom font you're adding was added to a separate component within `pages/_document.js` \- this disables automatic font optimization.



## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-page-custom-font#possible-ways-to-fix-it)

Create the file `./pages/_document.js` and add the font to a custom Document:

pages/_document.js
[code]
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
[/code]

Or as a function component:

pages/_document.js
[code]
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
[/code]

### When Not To Use It[](https://nextjs.org/docs/messages/no-page-custom-font#when-not-to-use-it)

If you have a reason to only load a font for a particular page or don't care about font optimization, then you can disable this rule.

## Useful Links[](https://nextjs.org/docs/messages/no-page-custom-font#useful-links)

  * [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)
  * [Font Optimization](https://nextjs.org/docs/pages/api-reference/components/font)



Was this helpful?

supported.

Send
