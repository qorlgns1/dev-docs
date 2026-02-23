---
title: '구성 요소: Script'
description: '마지막 업데이트 2026년 2월 20일'
---

# 구성 요소: Script | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/components/script

[API Reference](https://nextjs.org/docs/pages/api-reference)[Components](https://nextjs.org/docs/pages/api-reference/components)Script

Copy page

# Script

마지막 업데이트 2026년 2월 20일

이 API 레퍼런스는 Script 컴포넌트에서 사용할 수 있는 [props](https://nextjs.org/docs/pages/api-reference/components/script#props)를 이해하는 데 도움을 줍니다. 기능과 사용법은 [Optimizing Scripts](https://nextjs.org/docs/app/guides/scripts) 페이지를 참고하세요.

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import Script from 'next/script'
     
    export default function Dashboard() {
      return (
        <>
          <Script src="https://example.com/script.js" />
        </>
      )
    }
[/code]

## Props[](https://nextjs.org/docs/pages/api-reference/components/script#props)

다음은 Script 컴포넌트에서 사용할 수 있는 props 요약입니다:

Prop| Example| Type| Required  
---|---|---|---  
[`src`](https://nextjs.org/docs/pages/api-reference/components/script#src)| `src="http://example.com/script"`| String| 인라인 스크립트를 사용하지 않는 한 필수  
[`strategy`](https://nextjs.org/docs/pages/api-reference/components/script#strategy)| `strategy="lazyOnload"`| String| -  
[`onLoad`](https://nextjs.org/docs/pages/api-reference/components/script#onload)| `onLoad={onLoadFunc}`| Function| -  
[`onReady`](https://nextjs.org/docs/pages/api-reference/components/script#onready)| `onReady={onReadyFunc}`| Function| -  
[`onError`](https://nextjs.org/docs/pages/api-reference/components/script#onerror)| `onError={onErrorFunc}`| Function| -  
  
## Required Props[](https://nextjs.org/docs/pages/api-reference/components/script#required-props)

`<Script />` 컴포넌트는 다음 속성을 필요로 합니다.

### `src`[](https://nextjs.org/docs/pages/api-reference/components/script#src)

외부 스크립트의 URL을 지정하는 경로 문자열입니다. 절대 경로의 외부 URL 또는 내부 경로 모두 사용할 수 있습니다. 인라인 스크립트를 사용하지 않는 한 `src` 속성은 필수입니다.

## Optional Props[](https://nextjs.org/docs/pages/api-reference/components/script#optional-props)

`<Script />` 컴포넌트는 필수 항목 외에도 다양한 속성을 받을 수 있습니다.

### `strategy`[](https://nextjs.org/docs/pages/api-reference/components/script#strategy)

스크립트의 로딩 전략입니다. 사용할 수 있는 전략은 네 가지입니다:

  * `beforeInteractive`: 모든 Next.js 코드와 페이지 하이드레이션 전에 로드합니다.
  * `afterInteractive`: (**기본값**) 페이지에서 일부 하이드레이션이 발생한 후 빠르게 로드합니다.
  * `lazyOnload`: 브라우저 유휴 시간 동안 로드합니다.
  * `worker`: (실험적) 웹 워커에서 로드합니다.



### `beforeInteractive`[](https://nextjs.org/docs/pages/api-reference/components/script#beforeinteractive)

`beforeInteractive` 전략으로 로드되는 스크립트는 서버에서 초기 HTML에 주입되고, 모든 Next.js 모듈 전에 다운로드되며, 배치된 순서대로 실행됩니다.

이 전략으로 지정된 스크립트는 사전 로드되어 모든 1st-party 코드보다 먼저 페치되지만, 실행이 **페이지 하이드레이션을 차단하지 않습니다**.

`beforeInteractive` 스크립트는 `Document` 컴포넌트(`pages/_document.js`) 내부에 배치해야 하며, 사이트 전체에서 필요한 스크립트를 로드하도록 설계되었습니다(즉, 애플리케이션의 어떤 페이지든 서버 측에서 로드될 때 해당 스크립트가 로드됨).

**이 전략은 가능한 한 빨리 페치해야 하는 중요한 스크립트에만 사용하세요.**

pages/_document.js
[code]
    import { Html, Head, Main, NextScript } from 'next/document'
    import Script from 'next/script'
     
    export default function Document() {
      return (
        <Html>
          <Head />
          <body>
            <Main />
            <NextScript />
            <Script
              src="https://example.com/script.js"
              strategy="beforeInteractive"
            />
          </body>
        </Html>
      )
    }
[/code]

> **알아두면 좋아요** : `beforeInteractive` 스크립트는 컴포넌트 어디에 배치하든 항상 HTML 문서의 `head` 내부에 주입됩니다.

`beforeInteractive`로 가능한 한 빨리 페치해야 하는 스크립트 예시는 다음과 같습니다:

  * 봇 감지기
  * 쿠키 동의 매니저



### `afterInteractive`[](https://nextjs.org/docs/pages/api-reference/components/script#afterinteractive)

`afterInteractive` 전략을 사용하는 스크립트는 클라이언트 측 HTML에 주입되며 페이지에서 일부(또는 전체) 하이드레이션이 발생한 후 로드됩니다. **이것이 Script 컴포넌트의 기본 전략**이며, 가능한 빨리 로드해야 하지만 1st-party Next.js 코드보다 먼저 로드할 필요는 없는 스크립트에 사용해야 합니다.

`afterInteractive` 스크립트는 어떤 페이지나 레이아웃에든 배치할 수 있고, 해당 페이지(또는 페이지 그룹)가 브라우저에서 열릴 때만 로드 및 실행됩니다.

app/page.js
[code]
    import Script from 'next/script'
     
    export default function Page() {
      return (
        <>
          <Script src="https://example.com/script.js" strategy="afterInteractive" />
        </>
      )
    }
[/code]

`afterInteractive`에 적합한 스크립트 예시는 다음과 같습니다:

  * 태그 매니저
  * 분석 도구



### `lazyOnload`[](https://nextjs.org/docs/pages/api-reference/components/script#lazyonload)

`lazyOnload` 전략을 사용하는 스크립트는 브라우저 유휴 시간 동안 클라이언트 측 HTML에 주입되고, 페이지의 모든 리소스가 페치된 후 로드됩니다. 이 전략은 일찍 로드할 필요가 없는 백그라운드 또는 저우선순위 스크립트에 사용해야 합니다.

`lazyOnload` 스크립트는 어떤 페이지나 레이아웃에도 배치할 수 있으며, 해당 페이지(또는 페이지 그룹)가 브라우저에서 열릴 때만 로드 및 실행됩니다.

app/page.js
[code]
    import Script from 'next/script'
     
    export default function Page() {
      return (
        <>
          <Script src="https://example.com/script.js" strategy="lazyOnload" />
        </>
      )
    }
[/code]

즉시 로드할 필요가 없고 `lazyOnload`로 페치해도 되는 스크립트 예시는 다음과 같습니다:

  * 채팅 지원 플러그인
  * 소셜 미디어 위젯



### `worker`[](https://nextjs.org/docs/pages/api-reference/components/script#worker)

> **경고:** `worker` 전략은 아직 안정적이지 않으며 App Router에서 작동하지 않습니다. 주의해서 사용하세요.

`worker` 전략을 사용하는 스크립트는 웹 워커로 오프로드되어 메인 스레드를 확보하고, 메인 스레드에서 중요한 1st-party 리소스만 처리되도록 합니다. 이 전략은 어떤 스크립트에든 사용할 수 있지만 모든 서드파티 스크립트를 지원한다고 보장되지 않는 고급 사용 사례입니다.

`worker` 전략을 사용하려면 `next.config.js`에서 `nextScriptWorkers` 플래그를 활성화해야 합니다:

next.config.js
[code]
    module.exports = {
      experimental: {
        nextScriptWorkers: true,
      },
    }
[/code]

`worker` 스크립트는 **현재 `pages/` 디렉터리에서만 사용할 수 있습니다**:

pages/home.tsx

JavaScriptTypeScript
[code]
    import Script from 'next/script'
     
    export default function Home() {
      return (
        <>
          <Script src="https://example.com/script.js" strategy="worker" />
        </>
      )
    }
[/code]

### `onLoad`[](https://nextjs.org/docs/pages/api-reference/components/script#onload)

> **경고:** `onLoad`는 아직 Server Components에서 작동하지 않으며 Client Components에서만 사용할 수 있습니다. 또한 `onLoad`는 `beforeInteractive`와 함께 사용할 수 없습니다. 대신 `onReady` 사용을 고려하세요.

일부 서드파티 스크립트는 스크립트 로드가 완료된 후 JavaScript 코드를 실행해야 콘텐츠를 초기화하거나 함수를 호출합니다. 스크립트를 `afterInteractive` 또는 `lazyOnload` 전략으로 로드하는 경우 `onLoad` 속성을 사용해 로드 완료 후 코드를 실행할 수 있습니다.

다음은 라이브러리가 로드된 후에만 lodash 메서드를 실행하는 예시입니다.

app/page.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import Script from 'next/script'
     
    export default function Page() {
      return (
        <>
          <Script
            src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js"
            onLoad={() => {
              console.log(_.sample([1, 2, 3, 4]))
            }}
          />
        </>
      )
    }
[/code]

### `onReady`[](https://nextjs.org/docs/pages/api-reference/components/script#onready)

> **경고:** `onReady`는 아직 Server Components에서 작동하지 않으며 Client Components에서만 사용할 수 있습니다.

일부 서드파티 스크립트는 스크립트 로드가 끝난 후와 컴포넌트가 매번 마운트될 때(예: 라우트 이동 후) JavaScript 코드를 실행해야 합니다. `onReady` 속성을 사용하면 스크립트가 최초로 로드될 때와 이후 컴포넌트가 다시 마운트될 때마다 스크립트의 load 이벤트 직후 코드를 실행할 수 있습니다.

다음은 컴포넌트가 마운트될 때마다 Google Maps JS 임베드를 다시 초기화하는 예시입니다:
[code] 
    import { useRef } from 'react'
    import Script from 'next/script'
     
    export default function Page() {
      const mapRef = useRef()
     
      return (
        <>
          <div ref={mapRef}></div>
          <Script
            id="google-maps"
            src="https://maps.googleapis.com/maps/api/js"
            onReady={() => {
              new google.maps.Map(mapRef.current, {
                center: { lat: -34.397, lng: 150.644 },
                zoom: 8,
              })
            }}
          />
        </>
      )
    }
[/code]

### `onError`[](https://nextjs.org/docs/pages/api-reference/components/script#onerror)

> **경고:** `onError`는 아직 Server Components에서 작동하지 않으며 Client Components에서만 사용할 수 있습니다. 또한 `onError`는 `beforeInteractive` 로딩 전략과 함께 사용할 수 없습니다.

스크립트 로드 실패를 감지하면 도움이 되는 경우가 있습니다. 이러한 오류는 `onError` 속성으로 처리할 수 있습니다:
[code] 
    import Script from 'next/script'
     
    export default function Page() {
      return (
        <>
          <Script
            src="https://example.com/script.js"
            onError={(e: Error) => {
              console.error('Script failed to load', e)
            }}
          />
        </>
      )
    }
[/code]

## Version History[](https://nextjs.org/docs/pages/api-reference/components/script#version-history)

Version| Changes  
---|---  
`v13.0.0`| `beforeInteractive`와 `afterInteractive`가 `app`을 지원하도록 수정되었습니다.  
`v12.2.4`| `onReady` prop이 추가되었습니다.  
`v12.2.2`| `_document`에서 `beforeInteractive`와 함께 `next/script` 사용을 허용했습니다.  
`v11.0.0`| `next/script`가 도입되었습니다.  
  
이 정보가 도움이 되었나요?

supported.

Send
