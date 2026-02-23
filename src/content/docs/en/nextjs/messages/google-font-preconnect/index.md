---
title: 'Google Font Preconnect'
description: '> Note : Next.js automatically adds  after version .'
---

# Google Font Preconnect | Next.js

Source URL: https://nextjs.org/docs/messages/google-font-preconnect

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Google Font Preconnect

# Google Font Preconnect

> **Note** : Next.js automatically adds `<link rel="preconnect" />` after version `12.0.1`.

> Ensure `preconnect` is used with Google Fonts.

## Why This Error Occurred[](https://nextjs.org/docs/messages/google-font-preconnect#why-this-error-occurred)

A preconnect resource hint was not used with a request to the Google Fonts domain. Adding `preconnect` is recommended to initiate an early connection to the origin.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/google-font-preconnect#possible-ways-to-fix-it)

Add `rel="preconnect"` to the Google Font domain `<link>` tag:

pages/_document.js
[code]
    <link rel="preconnect" href="https://fonts.gstatic.com" />
[/code]

> **Note** : a **separate** link with `dns-prefetch` can be used as a fallback for browsers that don't support `preconnect` although this is not required.

## Useful Links[](https://nextjs.org/docs/messages/google-font-preconnect#useful-links)

  * [Preconnect to required origins](https://web.dev/uses-rel-preconnect/)
  * [Preconnect and dns-prefetch](https://web.dev/preconnect-and-dns-prefetch/#resolve-domain-name-early-with-reldns-prefetch)
  * [Next.js Font Optimization](https://nextjs.org/docs/pages/api-reference/components/font)



Was this helpful?

supported.

Send
