---
title: '지원되는 브라우저 | Sentry for Next.js'
description: 'Sentry의 최신 JavaScript SDK는 ES2020 호환성을 요구합니다. 최소 지원 브라우저 버전은 다음과 같습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers

# 지원되는 브라우저 | Sentry for Next.js

Sentry의 최신 JavaScript SDK는 ES2020 호환성을 요구합니다. 최소 지원 브라우저 버전은 다음과 같습니다.

* Chrome 80
* Edge 80
* Safari 14, iOS Safari 14.4
* Firefox 74
* Opera 67
* Samsung Internet 13.0

또한 Sentry JavaScript SDK는 `fetch` API를 사용할 수 있어야 합니다. `fetch`를 사용할 수 없는 브라우저 유사 환경을 지원해야 한다면, fetch API용 polyfill을 포함해야 합니다.

## [이전 JavaScript 버전 지원](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers.md#supporting-earlier-javascript-versions)

Sentry JavaScript SDK는 최상의 사용자 경험과 가장 작은 번들 크기를 제공하기 위해 ES2020 문법과 기능을 사용합니다. 이전 버전을 지원하려면 Babel, SWC, TypeScript 같은 transpiler로 코드를 트랜스파일하고 polyfill을 추가해야 합니다.

## [8.x 브라우저 지원](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers.md#8x-browser-support)

Sentry의 JavaScript SDK는 ES2018 호환성과 [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis) 지원을 요구합니다. 최소 지원 브라우저 버전은 다음과 같습니다.

* Chrome 71
* Edge 79
* Safari 12.1, iOS Safari 12.2
* Firefox 65
* Opera 58
* Samsung Internet 10

## [7.x 브라우저 지원](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers.md#7x-browser-support)

Sentry JavaScript SDK의 `7.x`는 ES6 문법과 object spread 같은 일부 ES6+ 언어 기능을 사용합니다. 이러한 문법을 지원하지 않는 구형 브라우저를 대상으로 코드를 다운컴파일하고 있다면, 그 과정에 Sentry SDK도 포함해야 합니다.

