---
title: '가이드: 스크립트'
description: '모든 라우트에서 서드파티 스크립트를 로드하려면 를 임포트한 뒤 사용자 정의 에 스크립트를 직접 포함하세요:'
---

# 가이드: 스크립트 | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/scripts

# 스크립트를 로드하고 최적화하는 방법

마지막 업데이트 2026년 2월 20일

### 애플리케이션 스크립트[](https://nextjs.org/docs/pages/guides/scripts#application-scripts)

모든 라우트에서 서드파티 스크립트를 로드하려면 `next/script`를 임포트한 뒤 사용자 정의 `_app`에 스크립트를 직접 포함하세요:

pages/_app.js
```
    import Script from 'next/script'

    export default function MyApp({ Component, pageProps }) {
      return (
        <>
          <Component {...pageProps} />
          <Script src="https://example.com/script.js" />
        </>
      )
    }
```

이 스크립트는 애플리케이션의 _어떤_ 라우트를 요청하더라도 로드되고 실행됩니다. Next.js는 사용자가 여러 페이지를 오가더라도 스크립트를 **한 번만 로드**하도록 보장합니다.

> **권장 사항** : 불필요한 성능 영향을 최소화하려면 서드파티 스크립트를 특정 페이지나 레이아웃에만 포함하는 것을 권장합니다.

### 로딩 전략[](https://nextjs.org/docs/pages/guides/scripts#strategy)

기본적으로 `next/script`는 어느 페이지나 레이아웃에서든 서드파티 스크립트를 로드할 수 있지만, `strategy` 속성을 사용해 로딩 동작을 세밀하게 조정할 수 있습니다.

  * `beforeInteractive`: 어떤 Next.js 코드보다 먼저, 페이지 하이드레이션이 일어나기 전에 스크립트를 로드합니다.
  * `afterInteractive`: (**기본값**) 페이지에서 일부 하이드레이션이 진행된 후 비교적 이른 시점에 스크립트를 로드합니다.
  * `lazyOnload`: 브라우저가 유휴 상태일 때 나중에 스크립트를 로드합니다.
  * `worker`: (실험적) 웹 워커에서 스크립트를 로드합니다.

각 전략과 사용 사례에 대한 자세한 내용은 [`next/script`](https://nextjs.org/docs/app/api-reference/components/script#strategy) API 레퍼런스를 참고하세요.

### 스크립트를 웹 워커로 오프로드하기(실험적)[](https://nextjs.org/docs/pages/guides/scripts#offloading-scripts-to-a-web-worker-experimental)

> **경고:** `worker` 전략은 아직 안정적이지 않으며 App Router에서는 동작하지 않습니다. 주의해서 사용하세요.

`worker` 전략을 사용하는 스크립트는 [Partytown](https://partytown.qwik.dev/)을 통해 웹 워커에서 실행됩니다. 이렇게 하면 메인 스레드를 애플리케이션 코드에 집중할 수 있어 사이트 성능을 개선할 수 있습니다.

이 전략은 아직 실험 단계이므로 `next.config.js`에서 `nextScriptWorkers` 플래그를 활성화해야만 사용할 수 있습니다:

next.config.js
```
    module.exports = {
      experimental: {
        nextScriptWorkers: true,
      },
    }
```

그다음 개발 서버를 실행하면 Next.js가 필요한 패키지를 설치하는 과정을 안내해 설정을 마칠 수 있습니다:

pnpmnpmyarnbun

터미널
```
    pnpm dev
```

예를 들어 `npm install @qwik.dev/partytown`을 실행해 Partytown을 설치하라는 메시지를 볼 수 있습니다.

설정이 완료되면 `strategy="worker"`를 지정하는 것만으로 Partytown이 자동으로 초기화되고 스크립트가 웹 워커로 오프로드됩니다.

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

웹 워커에 서드파티 스크립트를 로드할 때 고려해야 할 트레이드오프가 여러 가지 있습니다. 자세한 내용은 Partytown의 [tradeoffs](https://partytown.qwik.dev/trade-offs) 문서를 확인하세요.

#### 사용자 지정 Partytown 구성 사용하기[](https://nextjs.org/docs/pages/guides/scripts#using-custom-partytown-configuration)

`worker` 전략은 추가 구성이 없어도 동작하지만, Partytown은 `debug` 모드 활성화나 이벤트 전달처럼 일부 설정을 바꾸기 위한 구성 객체를 지원합니다.

추가 구성 옵션을 넣고 싶다면 [사용자 정의 `_document.js`](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)에 사용하는 `<Head />` 컴포넌트 안에 포함할 수 있습니다:

_pages/document.jsx
```
    import { Html, Head, Main, NextScript } from 'next/document'

    export default function Document() {
      return (
        <Html>
          <Head>
            <script
              data-partytown-config
              dangerouslySetInnerHTML={{
                __html: `
                  partytown = {
                    lib: "/_next/static/~partytown/",
                    debug: true
                  };
                `,
              }}
            />
          </Head>
          <body>
            <Main />
            <NextScript />
          </body>
        </Html>
      )
    }
```

Partytown 구성을 수정하려면 다음 조건을 충족해야 합니다.

  1. Next.js가 사용하는 기본 구성을 덮어쓰려면 반드시 `data-partytown-config` 속성을 사용해야 합니다.
  2. Partytown 라이브러리 파일을 별도 디렉터리에 저장하지 않는 한, Next.js가 필요한 정적 파일을 어디에 두는지 알 수 있도록 구성 객체에 `lib: "/_next/static/~partytown/"` 속성-값을 포함해야 합니다.

> **참고** : [asset prefix](https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix)를 사용하면서 Partytown의 기본 구성을 수정하려면 해당 prefix를 `lib` 경로에 포함해야 합니다.

추가할 수 있는 다른 속성 전체 목록은 Partytown의 [configuration options](https://partytown.qwik.dev/configuration)을 살펴보세요.

### 인라인 스크립트[](https://nextjs.org/docs/pages/guides/scripts#inline-scripts)

외부 파일에서 로드하지 않는 인라인 스크립트도 Script 컴포넌트에서 지원합니다. 중괄호 안에 JavaScript를 넣어 작성할 수 있습니다.
```
    <Script id="show-banner">
      {`document.getElementById('banner').classList.remove('hidden')`}
    </Script>
```

또는 `dangerouslySetInnerHTML` 속성을 사용할 수 있습니다.
```
    <Script
      id="show-banner"
      dangerouslySetInnerHTML={{
        __html: `document.getElementById('banner').classList.remove('hidden')`,
      }}
    />
```

> **경고** : Next.js가 스크립트를 추적하고 최적화하려면 인라인 스크립트에 반드시 `id` 속성을 지정해야 합니다.

### 추가 코드를 실행하기[](https://nextjs.org/docs/pages/guides/scripts#executing-additional-code)

이벤트 핸들러를 Script 컴포넌트와 함께 사용해 특정 이벤트 발생 후 추가 코드를 실행할 수 있습니다.

  * `onLoad`: 스크립트 로드가 끝난 뒤 코드를 실행합니다.
  * `onReady`: 스크립트 로드가 끝난 뒤와 컴포넌트가 마운트될 때마다 코드를 실행합니다.
  * `onError`: 스크립트를 로드하지 못했을 때 코드를 실행합니다.

이 핸들러는 `next/script`를 임포트해 `"use client"`가 코드 첫 줄에 선언된 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 안에서만 동작합니다.

pages/index.tsx

JavaScriptTypeScript
```
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
```

각 이벤트 핸들러에 대한 자세한 설명과 예시는 [`next/script`](https://nextjs.org/docs/pages/api-reference/components/script#onload) API 레퍼런스를 참고하세요.

### 추가 속성[](https://nextjs.org/docs/pages/guides/scripts#additional-attributes)

[`nonce`](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce)나 [커스텀 데이터 속성](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/data-*)처럼 Script 컴포넌트가 사용하지 않는 `<script>` 요소용 DOM 속성을 여러 개 지정할 수 있습니다. 추가 속성을 포함하면 HTML에 포함되는 최종 최적화 `<script>` 요소로 자동 전달됩니다.

pages/index.tsx

JavaScriptTypeScript
```
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
```

supported.

Send