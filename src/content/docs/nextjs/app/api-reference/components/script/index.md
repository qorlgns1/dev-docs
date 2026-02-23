---
title: '컴포넌트: Script 컴포넌트'
description: '이 API 레퍼런스는 Script 컴포넌트에 사용할 수 있는 props의 동작을 이해하는 데 도움을 줍니다. 기능과 사용 예시는 Optimizing Scripts 페이지를 참고하세요.'
---

# 컴포넌트: Script 컴포넌트 | Next.js
Source URL: https://nextjs.org/docs/app/api-reference/components/script

[API 레퍼런스](https://nextjs.org/docs/app/api-reference)[컴포넌트](https://nextjs.org/docs/app/api-reference/components)Script 컴포넌트

# Script 컴포넌트

최종 업데이트 2026년 2월 20일

이 API 레퍼런스는 Script 컴포넌트에 사용할 수 있는 [props](https://nextjs.org/docs/app/api-reference/components/script#props)의 동작을 이해하는 데 도움을 줍니다. 기능과 사용 예시는 [Optimizing Scripts](https://nextjs.org/docs/app/guides/scripts) 페이지를 참고하세요.

app/dashboard/page.tsx

JavaScriptTypeScript
```
    import Script from 'next/script'

    export default function Dashboard() {
      return (
        <>
          <Script src="https://example.com/script.js" />
        </>
      )
    }
```

## Props[](https://nextjs.org/docs/app/api-reference/components/script#props)

Script 컴포넌트에서 사용할 수 있는 props 요약은 다음과 같습니다.

Prop| 예시| 타입| 필수
---|---|---|---
[`src`](https://nextjs.org/docs/app/api-reference/components/script#src)| `src="http://example.com/script"`| String| 인라인 스크립트를 사용하지 않는 한 필수
[`strategy`](https://nextjs.org/docs/app/api-reference/components/script#strategy)| `strategy="lazyOnload"`| String| -
[`onLoad`](https://nextjs.org/docs/app/api-reference/components/script#onload)| `onLoad={onLoadFunc}`| Function| -
[`onReady`](https://nextjs.org/docs/app/api-reference/components/script#onready)| `onReady={onReadyFunc}`| Function| -
[`onError`](https://nextjs.org/docs/app/api-reference/components/script#onerror)| `onError={onErrorFunc}`| Function| -

## 필수 Props[](https://nextjs.org/docs/app/api-reference/components/script#required-props)

`<Script />` 컴포넌트에는 다음 속성이 필요합니다.

### `src`[](https://nextjs.org/docs/app/api-reference/components/script#src)

외부 스크립트의 URL을 지정하는 경로 문자열입니다. 절대 외부 URL이거나 내부 경로일 수 있습니다. 인라인 스크립트를 사용하지 않는 한 `src` 속성은 필수입니다.

## 선택 Props[](https://nextjs.org/docs/app/api-reference/components/script#optional-props)

`<Script />` 컴포넌트는 필수 속성 외에도 여러 추가 속성을 허용합니다.

### `strategy`[](https://nextjs.org/docs/app/api-reference/components/script#strategy)

스크립트의 로딩 전략입니다. 사용할 수 있는 네 가지 전략이 있습니다.

  * `beforeInteractive`: 모든 Next.js 코드와 페이지 하이드레이션 전에 로드합니다.
  * `afterInteractive`: (**기본값**) 페이지에서 일부 하이드레이션이 진행된 이후 일찍 로드합니다.
  * `lazyOnload`: 브라우저 유휴 시간 동안 로드합니다.
  * `worker`: (실험적) 웹 워커에서 로드합니다.

### `beforeInteractive`[](https://nextjs.org/docs/app/api-reference/components/script#beforeinteractive)

`beforeInteractive` 전략으로 로드되는 스크립트는 서버에서 초기 HTML에 삽입되고, 어떤 Next.js 모듈보다 먼저 다운로드되며, 배치된 순서대로 실행됩니다.

이 전략이 지정된 스크립트는 모든 1st-party 코드보다 먼저 프리로드 및 페치되지만, 실행은 **페이지 하이드레이션을 차단하지 않습니다**.

`beforeInteractive` 스크립트는 루트 레이아웃(`app/layout.tsx`) 안에 배치해야 하며, 사이트 전체에서 필요한 스크립트를 로드하도록 설계되었습니다(즉, 애플리케이션의 어떤 페이지든 서버 사이드로 로드될 때 스크립트가 로드됨).

**이 전략은 가능한 한 빨리 가져와야 하는 중요 스크립트에만 사용해야 합니다.**

app/layout.tsx

JavaScriptTypeScript
```
    import Script from 'next/script'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>
            {children}
            <Script
              src="https://example.com/script.js"
              strategy="beforeInteractive"
            />
          </body>
        </html>
      )
    }
```

> **알아 두세요**: `beforeInteractive` 스크립트는 컴포넌트 내 위치와 관계없이 항상 HTML 문서의 `head` 안에 삽입됩니다.

`beforeInteractive`로 가능한 한 빨리 가져와야 하는 스크립트 예시는 다음과 같습니다.

  * 봇 감지기
  * 쿠키 동의 관리자

### `afterInteractive`[](https://nextjs.org/docs/app/api-reference/components/script#afterinteractive)

`afterInteractive` 전략을 사용하는 스크립트는 클라이언트 측 HTML에 삽입되며, 페이지에서 일부(또는 전체) 하이드레이션이 발생한 이후에 로드됩니다. **이 전략은 Script 컴포넌트의 기본값**이며, 1st-party Next.js 코드보다 먼저 로드할 필요는 없지만 가능한 한 빨리 로드해야 하는 스크립트에 사용하세요.

`afterInteractive` 스크립트는 모든 페이지 또는 레이아웃 안에 배치할 수 있으며, 해당 페이지(또는 페이지 그룹)가 브라우저에서 열릴 때만 로드 및 실행됩니다.

app/page.js
```
    import Script from 'next/script'

    export default function Page() {
      return (
        <>
          <Script src="https://example.com/script.js" strategy="afterInteractive" />
        </>
      )
    }
```

`afterInteractive`에 적합한 스크립트 예시는 다음과 같습니다.

  * 태그 관리자
  * 애널리틱스

### `lazyOnload`[](https://nextjs.org/docs/app/api-reference/components/script#lazyonload)

`lazyOnload` 전략을 사용하는 스크립트는 브라우저 유휴 시간 동안 클라이언트 측 HTML에 삽입되며, 페이지의 모든 리소스가 페치된 후 로드됩니다. 이 전략은 일찍 로드할 필요가 없는 백그라운드 또는 낮은 우선순위 스크립트에 사용하세요.

`lazyOnload` 스크립트는 모든 페이지 또는 레이아웃 안에 배치할 수 있으며, 해당 페이지(또는 페이지 그룹)가 브라우저에서 열릴 때만 로드 및 실행됩니다.

app/page.js
```
    import Script from 'next/script'

    export default function Page() {
      return (
        <>
          <Script src="https://example.com/script.js" strategy="lazyOnload" />
        </>
      )
    }
```

즉시 로드할 필요가 없고 `lazyOnload`로 페치해도 되는 스크립트 예시는 다음과 같습니다.

  * 채팅 지원 플러그인
  * 소셜 미디어 위젯

### `worker`[](https://nextjs.org/docs/app/api-reference/components/script#worker)

> **경고:** `worker` 전략은 아직 안정적이지 않으며 App Router에서는 작동하지 않습니다. 사용 시 주의하세요.

`worker` 전략을 사용하는 스크립트는 메인 스레드를 확보하고 중요한 1st-party 리소스만 메인 스레드에서 처리되도록 웹 워커로 오프로드됩니다. 이 전략은 모든 스크립트에 사용할 수 있지만, 모든 서드파티 스크립트를 지원한다고 보장되지 않는 고급 사용 사례입니다.

`worker` 전략을 사용하려면 `next.config.js`에서 `nextScriptWorkers` 플래그를 활성화해야 합니다.

next.config.js
```
    module.exports = {
      experimental: {
        nextScriptWorkers: true,
      },
    }
```

`worker` 스크립트는 **현재 `pages/` 디렉터리에서만 사용할 수 있습니다**.

pages/home.tsx

JavaScriptTypeScript
```
    import Script from 'next/script'

    export default function Home() {
      return (
        <>
          <Script src="https://example.com/script.js" strategy="worker" />
        </>
      )
    }
```

### `onLoad`[](https://nextjs.org/docs/app/api-reference/components/script#onload)

> **경고:** `onLoad`는 아직 서버 컴포넌트에서 동작하지 않으며 클라이언트 컴포넌트에서만 사용할 수 있습니다. 또한 `beforeInteractive`와 함께 사용할 수 없습니다. 대신 `onReady`를 고려하세요.

일부 서드파티 스크립트는 스크립트가 로드된 직후 JavaScript 코드를 실행해 콘텐츠를 초기화하거나 함수를 호출해야 합니다. `afterInteractive` 또는 `lazyOnload` 로딩 전략으로 스크립트를 로드한다면, `onLoad` 속성을 사용해 스크립트 로드 이후 코드를 실행할 수 있습니다.

다음은 라이브러리가 로드된 이후에만 lodash 메서드를 실행하는 예시입니다.

app/page.tsx

JavaScriptTypeScript
```
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
```

### `onReady`[](https://nextjs.org/docs/app/api-reference/components/script#onready)

> **경고:** `onReady`는 아직 서버 컴포넌트에서 동작하지 않으며 클라이언트 컴포넌트에서만 사용할 수 있습니다.

일부 서드파티 스크립트는 스크립트가 처음 로드된 후뿐 아니라 컴포넌트가 마운트될 때마다(예: 라우트 네비게이션 이후) JavaScript 코드를 실행해야 합니다. `onReady` 속성을 사용하면 첫 로드 시 스크립트의 load 이벤트 이후, 그리고 이후 컴포넌트가 다시 마운트될 때마다 코드를 실행할 수 있습니다.

다음은 컴포넌트가 마운트될 때마다 Google Maps JS 임베드를 다시 초기화하는 예시입니다.

app/page.tsx

JavaScriptTypeScript
```
    'use client'

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
```

### `onError`[](https://nextjs.org/docs/app/api-reference/components/script#onerror)

> **경고:** `onError`는 아직 서버 컴포넌트에서 동작하지 않으며 클라이언트 컴포넌트에서만 사용할 수 있습니다. 또한 `beforeInteractive` 로딩 전략과는 함께 사용할 수 없습니다.

스크립트 로드 실패를 포착하면 도움이 될 때가 있습니다. 이러한 오류는 `onError` 속성으로 처리할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
```
    'use client'

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
```

## 버전 기록[](https://nextjs.org/docs/app/api-reference/components/script#version-history)

버전| 변경 사항
---|---
`v13.0.0`| `beforeInteractive` 및 `afterInteractive`가 `app`을 지원하도록 수정됨.
`v12.2.4`| `onReady` prop 추가.
`v12.2.2`| `_document`에서도 `beforeInteractive`와 함께 `next/script` 사용 허용.
`v11.0.0`| `next/script` 도입.

보내기