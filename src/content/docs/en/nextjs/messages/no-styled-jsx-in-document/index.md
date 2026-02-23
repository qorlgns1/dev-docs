---
title: 'No styled-jsx in _document'
description: '> Prevent usage of  in .'
---

# No `styled-jsx` in `_document` | Next.js

Source URL: https://nextjs.org/docs/messages/no-styled-jsx-in-document

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No `styled-jsx` in `_document`

# No `styled-jsx` in `_document`

> Prevent usage of `styled-jsx` in `pages/_document.js`.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-styled-jsx-in-document#why-this-error-occurred)

Custom CSS like `styled-jsx` is not allowed in a [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document).

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-styled-jsx-in-document#possible-ways-to-fix-it)

If you need shared CSS for all of your pages, take a look at the [Custom `App`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) file or define a custom layout.

For example, consider the following stylesheet named `styles.css`:

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

Create a `pages/_app.{js,tsx}` file if not already present. Then, import the `styles.css` file.

pages/_app.js
[code]
    import '../styles.css'
     
    // This default export is required in a new `pages/_app.js` file.
    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

These styles (`styles.css`) will apply to all pages and components in your application.

## Useful Links[](https://nextjs.org/docs/messages/no-styled-jsx-in-document#useful-links)

  * [Custom Document Caveats](https://nextjs.org/docs/pages/building-your-application/routing/custom-document#caveats)
  * [Layouts](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)
  * [Built in CSS Support](https://nextjs.org/docs/app/getting-started/css)
  * [Custom `App`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)



Was this helpful?

supported.

Send
