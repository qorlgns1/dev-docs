---
title: '가이드: 스크립트'
description: '여러 경로에서 서드파티 스크립트를 로드하려면 를 import한 뒤 레이아웃 컴포넌트에 직접 포함하세요:'
---

# 가이드: 스크립트 | Next.js

Source URL: https://nextjs.org/docs/app/guides/scripts

# 스크립트를 로드하고 최적화하는 방법

마지막 업데이트 2026년 2월 20일

### 레이아웃 스크립트[](https://nextjs.org/docs/app/guides/scripts#layout-scripts)

여러 경로에서 서드파티 스크립트를 로드하려면 `next/script`를 import한 뒤 레이아웃 컴포넌트에 직접 포함하세요:

app/dashboard/layout.tsx

JavaScriptTypeScript
[code]
    import Script from 'next/script'

    export default function DashboardLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <>
          <section>{children}</section>
          <Script src="https://example.com/script.js" />
        </>
      )
    }
[/code]

폴더 라우트(예: `dashboard/page.js`)나 중첩 라우트(예: `dashboard/settings/page.js`)에 사용자가 접근하면 서드파티 스크립트가 가져와집니다. 동일한 레이아웃에서 여러 라우트를 이동하더라도 Next.js는 스크립트를 **한 번만 로드**하도록 보장합니다.

### 애플리케이션 스크립트[](https://nextjs.org/docs/app/guides/scripts#application-scripts)

모든 라우트에서 서드파티 스크립트를 로드하려면 `next/script`를 import한 뒤 루트 레이아웃에 직접 포함하세요:

app/layout.tsx

JavaScriptTypeScript
[code]
    import Script from 'next/script'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>{children}</body>
          <Script src="https://example.com/script.js" />
        </html>
      )
    }
[/code]

이 스크립트는 애플리케이션의 _모든_ 라우트에 접근할 때 로드 및 실행됩니다. 사용자가 여러 페이지를 이동하더라도 Next.js는 스크립트를 **한 번만 로드**하도록 보장합니다.

> **권장 사항**: 성능에 불필요한 영향을 줄이려면 서드파티 스크립트를 필요한 페이지나 레이아웃에만 포함하는 것이 좋습니다.

### 전략[](https://nextjs.org/docs/app/guides/scripts#strategy)

기본적으로 `next/script`는 모든 페이지나 레이아웃에서 서드파티 스크립트를 로드할 수 있지만, `strategy` 속성으로 로딩 동작을 세밀하게 조정할 수 있습니다:

  * `beforeInteractive`: 모든 Next.js 코드와 페이지 하이드레이션 이전에 스크립트를 로드합니다.
  * `afterInteractive`: (**기본값**) 일부 하이드레이션이 끝난 뒤 빠르게 스크립트를 로드합니다.
  * `lazyOnload`: 브라우저 아이들 시간 동안 나중에 스크립트를 로드합니다.
  * `worker`: (실험적) 웹 워커에서 스크립트를 로드합니다.

각 전략과 사용 사례에 대한 자세한 내용은 [`next/script`](https://nextjs.org/docs/app/api-reference/components/script#strategy) API 레퍼런스를 참조하세요.

### 스크립트를 웹 워커로 오프로딩하기(실험적)[](https://nextjs.org/docs/app/guides/scripts#offloading-scripts-to-a-web-worker-experimental)

> **경고:** `worker` 전략은 아직 안정적이지 않으며 App Router와 함께 작동하지 않습니다. 주의해서 사용하세요.

`worker` 전략을 사용하는 스크립트는 [Partytown](https://partytown.qwik.dev/)을 통해 웹 워커에서 실행됩니다. 이렇게 하면 메인 스레드를 나머지 애플리케이션 코드에 전용으로 사용할 수 있어 사이트 성능이 향상될 수 있습니다.

이 전략은 아직 실험 단계이므로 `next.config.js`에서 `nextScriptWorkers` 플래그를 활성화해야만 사용할 수 있습니다:

next.config.js
[code]
    module.exports = {
      experimental: {
        nextScriptWorkers: true,
      },
    }
[/code]

그런 다음 개발 서버를 실행하면 Next.js가 필요한 패키지 설치 과정을 안내합니다:

pnpmnpmyarnbun

Terminal
[code]
    pnpm dev
[/code]

`npm install @qwik.dev/partytown`을 실행해 Partytown을 설치하라는 안내를 확인하게 됩니다.

설치가 끝나면 `strategy="worker"`를 정의하는 것만으로 Partytown이 애플리케이션에 자동으로 초기화되고 스크립트가 웹 워커로 오프로딩됩니다.

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

서드파티 스크립트를 웹 워커에서 로드할 때 고려해야 할 트레이드오프가 여러 가지 있습니다. 자세한 내용은 Partytown의 [tradeoffs](https://partytown.qwik.dev/trade-offs) 문서를 참고하세요.

### 인라인 스크립트[](https://nextjs.org/docs/app/guides/scripts#inline-scripts)

외부 파일에서 로드되지 않는 인라인 스크립트도 Script 컴포넌트에서 지원합니다. 중괄호 안에 JavaScript를 작성하면 됩니다:
[code]
    <Script id="show-banner">
      {`document.getElementById('banner').classList.remove('hidden')`}
    </Script>
[/code]

또는 `dangerouslySetInnerHTML` 속성을 사용할 수 있습니다:
[code]
    <Script
      id="show-banner"
      dangerouslySetInnerHTML={{
        __html: `document.getElementById('banner').classList.remove('hidden')`,
      }}
    />
[/code]

> **경고**: Next.js가 스크립트를 추적하고 최적화하려면 인라인 스크립트에 `id` 속성을 반드시 지정해야 합니다.

### 추가 코드를 실행하기[](https://nextjs.org/docs/app/guides/scripts#executing-additional-code)

Script 컴포넌트에 이벤트 핸들러를 사용해 특정 이벤트 이후에 추가 코드를 실행할 수 있습니다:

  * `onLoad`: 스크립트 로딩이 완료된 후 코드를 실행합니다.
  * `onReady`: 스크립트 로딩이 끝난 뒤, 그리고 컴포넌트가 마운트될 때마다 코드를 실행합니다.
  * `onError`: 스크립트 로딩에 실패했을 때 코드를 실행합니다.

이 핸들러들은 `next/script`를 import하고 `"use client"`가 코드 첫 줄에 정의된 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 내부에서만 동작합니다:

app/page.tsx

JavaScriptTypeScript
[code]
    'use client'

    import Script from 'next/script'

    export default function Page() {
      return (
        <>
          <Script
            src="https://example.com/script.js"
            onLoad={() => {
              console.log('Script has loaded')
            }}
          />
        </>
      )
    }
[/code]

각 이벤트 핸들러에 대한 자세한 설명과 예시는 [`next/script`](https://nextjs.org/docs/app/api-reference/components/script#onload) API 레퍼런스를 참고하세요.

### 추가 속성[](https://nextjs.org/docs/app/guides/scripts#additional-attributes)

[`nonce`](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce)나 [커스텀 데이터 속성](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/data-*)처럼 Script 컴포넌트가 사용하지 않는 다양한 DOM 속성을 `<script>` 요소에 지정할 수 있습니다. 이러한 추가 속성을 포함하면 HTML에 삽입되는 최종 최적화 `<script>` 요소로 자동 전달됩니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Script from 'next/script'

    export default function Page() {
      return (
        <>
          <Script
            src="https://example.com/script.js"
            id="example-script"
            nonce="XUENAJFW"
            data-test="script"
          />
        </>
      )
    }
[/code]

## API 레퍼런스

next/script API에 대해 더 알아보세요.

- [스크립트 컴포넌트](https://nextjs.org/docs/app/api-reference/components/script)
  - Script 컴포넌트Next.js 애플리케이션에서 기본 제공 `next/script` 컴포넌트를 사용해 서드파티 스크립트를 최적화합니다.

보내기
