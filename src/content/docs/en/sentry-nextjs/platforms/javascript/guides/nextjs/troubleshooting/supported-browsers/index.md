---
title: 'Supported Browsers | Sentry for Next.js'
description: "Sentry's latest JavaScript SDKs require ES2020 compatibility. The minimum supported browser versions are:"
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers

# Supported Browsers | Sentry for Next.js

Sentry's latest JavaScript SDKs require ES2020 compatibility. The minimum supported browser versions are:

* Chrome 80
* Edge 80
* Safari 14, iOS Safari 14.4
* Firefox 74
* Opera 67
* Samsung Internet 13.0

In addition, the Sentry JavaScript SDKs require the `fetch` API to be available. If you need to support browser-like environments that do not have `fetch` available, you should include a polyfill for the fetch API.

## [Supporting earlier JavaScript versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers.md#supporting-earlier-javascript-versions)

The Sentry JavaScript SDK uses ES2020 syntax and functionality to provide the best possible user experience and lowest bundle size. If you want to support earlier versions, you need to transpile your code using a transpiler like Babel, SWC, or TypeScript, and add polyfills.

## [8.x Browser support](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers.md#8x-browser-support)

Sentry's JavaScript SDKs require ES2018 compatibility plus support for [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis). The minimum supported browser versions are:

* Chrome 71
* Edge 79
* Safari 12.1, iOS Safari 12.2
* Firefox 65
* Opera 58
* Samsung Internet 10

## [7.x Browser support](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers.md#7x-browser-support)

`7.x` of the Sentry JavaScript SDKs use ES6 syntax, along with a few other ES6+ language features, such as object spread. If you are down-compiling your code in order to target older browsers that don't support such syntax, you'll need to include the Sentry SDK in that process.

