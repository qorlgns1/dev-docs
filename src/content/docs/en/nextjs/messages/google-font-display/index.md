---
title: 'Google Font Display'
description: '> Enforce font-display behavior with Google Fonts.'
---

# Google Font Display | Next.js

Source URL: https://nextjs.org/docs/messages/google-font-display

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Google Font Display

# Google Font Display

> Enforce font-display behavior with Google Fonts.

## Why This Error Occurred[](https://nextjs.org/docs/messages/google-font-display#why-this-error-occurred)

For a Google Font, the font-display descriptor was either missing or set to `auto`, `block`, or `fallback`, which are not recommended.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/google-font-display#possible-ways-to-fix-it)

For most cases, the best font display strategy for custom fonts is `optional`.

pages/index.js
[code]
    import Head from 'next/head'
     
    export default function IndexPage() {
      return (
        <div>
          <Head>
            <link
              href="https://fonts.googleapis.com/css2?family=Krona+One&display=optional"
              rel="stylesheet"
            />
          </Head>
        </div>
      )
    }
[/code]

Specifying `display=optional` minimizes the risk of invisible text or layout shift. If swapping to the custom font after it has loaded is important to you, then use `display=swap` instead.

### When Not To Use It[](https://nextjs.org/docs/messages/google-font-display#when-not-to-use-it)

If you want to specifically display a font using an `auto`, `block`, or `fallback` strategy, then you can disable this rule.

## Useful Links[](https://nextjs.org/docs/messages/google-font-display#useful-links)

  * [Controlling Font Performance with font-display](https://developer.chrome.com/blog/font-display/)
  * [Google Fonts API Docs](https://developers.google.com/fonts/docs/css2#use_font-display)
  * [CSS `font-display` property](https://www.w3.org/TR/css-fonts-4/#font-display-desc)



Was this helpful?

supported.

Send
