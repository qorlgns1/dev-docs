---
title: 'No Unwanted Polyfill.io'
description: '> Prevent duplicate polyfills from Polyfill.io.'
---

Source URL: https://nextjs.org/docs/messages/no-unwanted-polyfillio

# No Unwanted Polyfill.io

> Prevent duplicate polyfills from Polyfill.io.

## Why This Error Occurred

You are using polyfills from Polyfill.io and including polyfills already shipped with Next.js. This unnecessarily increases page weight which can affect loading performance.

## Possible Ways to Fix It

Remove all duplicate polyfills. If you need to add polyfills but are not sure if Next.js already includes it, take a look at the list of [supported browsers and features](https://nextjs.org/docs/architecture/supported-browsers).

## Useful Links

- [Supported Browsers and Features](https://nextjs.org/docs/architecture/supported-browsers)

