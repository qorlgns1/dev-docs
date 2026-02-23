---
title: '아키텍처: 지원되는 브라우저'
description: 'Next.js는 모던 브라우저를 추가 설정 없이 지원합니다.'
---

# 아키텍처: 지원되는 브라우저 | Next.js

Source URL: https://nextjs.org/docs/architecture/supported-browsers

[Next.js Docs](https://nextjs.org/docs)[Architecture](https://nextjs.org/docs/architecture)Supported Browsers

Copy page

# 지원되는 브라우저

마지막 업데이트 2026년 2월 20일

Next.js는 **모던 브라우저**를 추가 설정 없이 지원합니다.

  * Chrome 111+
  * Edge 111+
  * Firefox 111+
  * Safari 16.4+

## Browserslist[](https://nextjs.org/docs/architecture/supported-browsers#browserslist)

특정 브라우저나 기능을 타깃팅하고 싶다면, Next.js에서는 `package.json` 파일에서 [Browserslist](https://browsersl.ist) 구성을 지원합니다. Next.js는 기본적으로 다음 Browserslist 구성을 사용합니다:

package.json
[code]
    {
      "browserslist": ["chrome 111", "edge 111", "firefox 111", "safari 16.4"]
    }
[/code]

## 폴리필[](https://nextjs.org/docs/architecture/supported-browsers#polyfills)

다음과 같은 [널리 사용되는 폴리필](https://github.com/vercel/next.js/blob/canary/packages/next-polyfill-nomodule/src/index.js)을 주입합니다:

  * [**fetch()**](https://developer.mozilla.org/docs/Web/API/Fetch_API) — 대체 대상: `whatwg-fetch`, `unfetch`.
  * [**URL**](https://developer.mozilla.org/docs/Web/API/URL) — 대체 대상: [`url` 패키지 (Node.js API)](https://nodejs.org/api/url.html).
  * [**Object.assign()**](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) — 대체 대상: `object-assign`, `object.assign`, `core-js/object/assign`.

이러한 폴리필이 의존성에 포함되어 있다면, 생산 빌드에서 자동으로 제거되어 중복을 방지합니다.

또한 번들 크기를 줄이기 위해, Next.js는 해당 폴리필이 필요한 브라우저에서만 이를 로드합니다. 전 세계 웹 트래픽의 대부분은 이 폴리필을 다운로드하지 않습니다.

### 사용자 정의 폴리필[](https://nextjs.org/docs/architecture/supported-browsers#custom-polyfills)

자체 코드나 외부 npm 의존성이 타깃 브라우저에서 지원되지 않는 기능(예: IE 11)을 요구하는 경우, 직접 폴리필을 추가해야 합니다.

#### App Router에서[](https://nextjs.org/docs/architecture/supported-browsers#in-app-router)

폴리필을 포함하려면 [`instrumentation-client.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client)에 임포트할 수 있습니다.

instrumentation-client.ts
[code]
    import './polyfills'
[/code]

#### Pages Router에서[](https://nextjs.org/docs/architecture/supported-browsers#in-pages-router)

이 경우 [Custom `<App>`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) 또는 개별 컴포넌트에서 필요한 **특정 폴리필**에 대한 최상위 임포트를 추가해야 합니다.

pages/_app.tsx

JavaScriptTypeScript
[code]
    import './polyfills'

    import type { AppProps } from 'next/app'

    export default function MyApp({ Component, pageProps }: AppProps) {
      return <Component {...pageProps} />
    }
[/code]

#### 조건부 폴리필 로딩[](https://nextjs.org/docs/architecture/supported-browsers#conditionally-loading-polyfills)

가장 좋은 접근 방식은 지원되지 않는 기능을 특정 UI 섹션에 격리하고 필요할 때 폴리필을 조건부로 로드하는 것입니다.

hooks/analytics.ts

JavaScriptTypeScript
[code]
    import { useCallback } from 'react'

    export const useAnalytics = () => {
      const tracker = useCallback(async (data: unknown) => {
        if (!('structuredClone' in globalThis)) {
          import('polyfills/structured-clone').then((mod) => {
            globalThis.structuredClone = mod.default
          })
        }

        /* Do some work that uses structured clone */
      }, [])

      return tracker
    }
[/code]

## JavaScript 언어 기능[](https://nextjs.org/docs/architecture/supported-browsers#javascript-language-features)

Next.js는 최신 JavaScript 기능을 기본적으로 사용할 수 있도록 해줍니다. [ES6 기능](https://github.com/lukehoban/es6features) 외에도 다음을 지원합니다:

  * [Async/await](https://github.com/tc39/ecmascript-asyncawait) (ES2017)
  * [Object Rest/Spread Properties](https://github.com/tc39/proposal-object-rest-spread) (ES2018)
  * [Dynamic `import()`](https://github.com/tc39/proposal-dynamic-import) (ES2020)
  * [Optional Chaining](https://github.com/tc39/proposal-optional-chaining) (ES2020)
  * [Nullish Coalescing](https://github.com/tc39/proposal-nullish-coalescing) (ES2020)
  * [Class Fields](https://github.com/tc39/proposal-class-fields) 및 [Static Properties](https://github.com/tc39/proposal-static-class-features) (ES2022)
  * 기타 등등!

### TypeScript 기능[](https://nextjs.org/docs/architecture/supported-browsers#typescript-features)

Next.js는 기본적으로 TypeScript를 지원합니다. [여기에서 자세히 알아보세요](https://nextjs.org/docs/pages/api-reference/config/typescript).

### Babel 구성 커스터마이징(고급)[](https://nextjs.org/docs/architecture/supported-browsers#customizing-babel-config-advanced)

Babel 구성을 커스터마이즈할 수 있습니다. [여기에서 자세히 알아보세요](https://nextjs.org/docs/pages/guides/babel).

Was this helpful?

supported.

Send
