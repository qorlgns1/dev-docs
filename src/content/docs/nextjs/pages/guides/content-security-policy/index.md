---
title: '가이드: Content Security Policy'
description: '최종 업데이트: 2026년 2월 20일'
---

# 가이드: Content Security Policy | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/content-security-policy

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)콘텐츠 보안 정책

# Next.js 애플리케이션에 Content Security Policy (CSP)를 설정하는 방법

최종 업데이트: 2026년 2월 20일

[Content Security Policy (CSP)](https://developer.mozilla.org/docs/Web/HTTP/CSP)는 Next.js 애플리케이션을 교차 사이트 스크립팅(XSS), 클릭재킹, 기타 코드 주입 공격과 같은 다양한 보안 위협으로부터 보호하는 데 중요합니다.

CSP를 사용하면 개발자가 콘텐츠 소스, 스크립트, 스타일시트, 이미지, 폰트, 오브젝트, 미디어(오디오, 비디오), iframe 등에서 허용되는 출처를 지정할 수 있습니다.

예시

  * [Strict CSP](https://github.com/vercel/next.js/tree/canary/examples/with-strict-csp)

## 논스[](https://nextjs.org/docs/pages/guides/content-security-policy#nonces)

[nonce](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce)는 한 번만 사용하도록 생성되는 고유한 무작위 문자열입니다. CSP와 함께 사용되어 엄격한 CSP 지시문을 우회하면서 특정 인라인 스크립트나 스타일을 선택적으로 허용합니다.

### 논스를 사용하는 이유?[](https://nextjs.org/docs/pages/guides/content-security-policy#why-use-a-nonce)

CSP는 공격을 방지하기 위해 인라인 스크립트와 외부 스크립트 모두를 차단할 수 있습니다. 논스를 사용하면 일치하는 논스 값이 포함된 경우에만 특정 스크립트를 안전하게 실행할 수 있습니다.

공격자가 페이지에 스크립트를 로드하려면 논스 값을 추측해야 합니다. 그렇기 때문에 논스는 요청마다 예측 불가능하고 고유해야 합니다.

### Proxy로 논스 추가하기[](https://nextjs.org/docs/pages/guides/content-security-policy#adding-a-nonce-with-proxy)

[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)는 페이지가 렌더링되기 전에 헤더를 추가하고 논스를 생성할 수 있게 해줍니다.

페이지가 조회될 때마다 새 논스를 생성해야 합니다. 따라서 논스를 추가하려면 **반드시 [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)을 사용해야 합니다**.

예를 들어:

> **알아두면 좋아요**: 개발 환경에서는 React가 브라우저에서 서버 측 오류 스택을 복원하는 등 향상된 디버깅 정보를 제공하기 위해 `eval`을 사용하므로 `'unsafe-eval'`이 필요합니다. `unsafe-eval`은 프로덕션에서는 필요하지 않습니다. React와 Next.js는 기본적으로 프로덕션에서 `eval`을 사용하지 않습니다.

proxy.ts

JavaScriptTypeScript
[code]
    import { NextRequest, NextResponse } from 'next/server'

    export function proxy(request: NextRequest) {
      const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
      const isDev = process.env.NODE_ENV === 'development'
      const cspHeader = `
        default-src 'self';
        script-src 'self' 'nonce-${nonce}' 'strict-dynamic'${isDev ? " 'unsafe-eval'" : ''};
        style-src 'self' 'nonce-${nonce}';
        img-src 'self' blob: data:;
        font-src 'self';
        object-src 'none';
        base-uri 'self';
        form-action 'self';
        frame-ancestors 'none';
        upgrade-insecure-requests;
    `
      // Replace newline characters and spaces
      const contentSecurityPolicyHeaderValue = cspHeader
        .replace(/\s{2,}/g, ' ')
        .trim()

      const requestHeaders = new Headers(request.headers)
      requestHeaders.set('x-nonce', nonce)

      requestHeaders.set(
        'Content-Security-Policy',
        contentSecurityPolicyHeaderValue
      )

      const response = NextResponse.next({
        request: {
          headers: requestHeaders,
        },
      })
      response.headers.set(
        'Content-Security-Policy',
        contentSecurityPolicyHeaderValue
      )

      return response
    }
[/code]

기본적으로 Proxy는 모든 요청에서 실행됩니다. [`matcher`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher)를 사용하여 특정 경로에서만 Proxy가 실행되도록 필터링할 수 있습니다.

`next/link`의 프리패치와 CSP 헤더가 필요 없는 정적 자산은 매칭 대상에서 제외하는 것을 권장합니다.

proxy.ts

JavaScriptTypeScript
[code]
    export const config = {
      matcher: [
        /*
         * Match all request paths except for the ones starting with:
         * - api (API routes)
         * - _next/static (static files)
         * - _next/image (image optimization files)
         * - favicon.ico (favicon file)
         */
        {
          source: '/((?!api|_next/static|_next/image|favicon.ico).*)',
          missing: [
            { type: 'header', key: 'next-router-prefetch' },
            { type: 'header', key: 'purpose', value: 'prefetch' },
          ],
        },
      ],
    }
[/code]

### Next.js에서 논스가 동작하는 방식[](https://nextjs.org/docs/pages/guides/content-security-policy#how-nonces-work-in-nextjs)

논스를 사용하려면 페이지가 **동적으로 렌더링**되어야 합니다. Next.js는 요청에 포함된 CSP 헤더를 기반으로 **서버 측 렌더링** 중에 논스를 적용하기 때문입니다. 정적 페이지는 빌드 시점에 생성되므로 요청 또는 응답 헤더가 존재하지 않아 논스를 주입할 수 없습니다.

동적으로 렌더링되는 페이지에서 논스 지원은 다음과 같이 작동합니다.

  1. **Proxy가 논스를 생성함**: Proxy가 요청에 대한 고유한 논스를 생성하고, 이를 `Content-Security-Policy` 헤더에 추가하며, 동시에 사용자 정의 `x-nonce` 헤더로 설정합니다.
  2. **Next.js가 논스를 추출함**: 렌더링 중에 Next.js는 `Content-Security-Policy` 헤더를 파싱하고 `'nonce-{value}'` 패턴을 사용해 논스를 추출합니다.
  3. **논스가 자동으로 적용됨**: Next.js는 다음에 논스를 자동으로 부여합니다:
     * 프레임워크 스크립트(React, Next.js 런타임)
     * 페이지별 JavaScript 번들
     * Next.js가 생성한 인라인 스타일 및 스크립트
     * `nonce` prop을 사용하는 모든 `<Script>` 컴포넌트

이 자동 동작 덕분에 각 태그에 논스를 수동으로 추가할 필요가 없습니다.

### 동적 렌더링 강제하기[](https://nextjs.org/docs/pages/guides/content-security-policy#forcing-dynamic-rendering)

논스를 사용 중이라면 페이지가 동적 렌더링을 명시적으로 선택하도록 설정해야 할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    import { connection } from 'next/server'

    export default async function Page() {
      // wait for an incoming request to render this page
      await connection()
      // Your page content
    }
[/code]

### 논스 읽어오기[](https://nextjs.org/docs/pages/guides/content-security-policy#reading-the-nonce)

[`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)를 사용해 페이지에 논스를 전달할 수 있습니다:

pages/index.tsx

JavaScriptTypeScript
[code]
    import Script from 'next/script'

    import type { GetServerSideProps } from 'next'

    export default function Page({ nonce }) {
      return (
        <Script
          src="https://www.googletagmanager.com/gtag/js"
          strategy="afterInteractive"
          nonce={nonce}
        />
      )
    }

    export const getServerSideProps: GetServerSideProps = async ({ req }) => {
      const nonce = req.headers['x-nonce']
      return { props: { nonce } }
    }
[/code]

Pages Router 애플리케이션에서는 `_document.tsx`에서도 논스를 조회할 수 있습니다:

pages/_document.tsx

JavaScriptTypeScript
[code]
    import Document, {
      Html,
      Head,
      Main,
      NextScript,
      DocumentContext,
      DocumentInitialProps,
    } from 'next/document'

    interface ExtendedDocumentProps extends DocumentInitialProps {
      nonce?: string
    }

    class MyDocument extends Document<ExtendedDocumentProps> {
      static async getInitialProps(
        ctx: DocumentContext
      ): Promise<ExtendedDocumentProps> {
        const initialProps = await Document.getInitialProps(ctx)
        const nonce = ctx.req?.headers?.['x-nonce'] as string | undefined

        return {
          ...initialProps,
          nonce,
        }
      }

      render() {
        const { nonce } = this.props

        return (
          <Html lang="en">
            <Head nonce={nonce} />
            <body>
              <Main />
              <NextScript nonce={nonce} />
            </body>
          </Html>
        )
      }
    }

    export default MyDocument
[/code]

## CSP와 함께하는 정적 렌더링 vs 동적 렌더링[](https://nextjs.org/docs/pages/guides/content-security-policy#static-vs-dynamic-rendering-with-csp)

논스를 사용하면 Next.js 애플리케이션의 렌더링 방식에 중요한 영향을 줍니다:

### 동적 렌더링 요구 사항[](https://nextjs.org/docs/pages/guides/content-security-policy#dynamic-rendering-requirement)

CSP에 논스를 사용하면 **모든 페이지가 동적으로 렌더링**되어야 합니다. 이는 다음을 의미합니다.

  * 페이지는 빌드에는 성공하지만 동적 렌더링을 제대로 구성하지 않으면 런타임 오류가 발생할 수 있습니다
  * 각 요청마다 새로운 논스가 적용된 새 페이지가 생성됩니다
  * 정적 최적화와 Incremental Static Regeneration(ISR)이 비활성화됩니다
  * 추가 구성이 없다면 CDN이 페이지를 캐시할 수 없습니다
  * 정적 셸 스크립트가 논스에 접근할 수 없으므로 **Partial Prerendering(PPR)은 논스 기반 CSP와 호환되지 않습니다**

### 성능 영향[](https://nextjs.org/docs/pages/guides/content-security-policy#performance-implications)

정적 렌더링에서 동적 렌더링으로 전환하면 성능에 영향을 줍니다.

  * **초기 페이지 로드가 느려짐**: 각 요청마다 페이지를 생성해야 합니다
  * **서버 부하 증가**: 모든 요청이 서버 측 렌더링을 필요로 합니다
  * **CDN 캐시 불가**: 기본적으로 동적 페이지는 엣지에서 캐시할 수 없습니다
  * **호스팅 비용 증가**: 동적 렌더링에는 더 많은 서버 리소스가 필요합니다

### 논스를 사용할 시점[](https://nextjs.org/docs/pages/guides/content-security-policy#when-to-use-nonces)

다음 상황에서는 논스를 고려하세요.

  * `'unsafe-inline'`을 금지하는 엄격한 보안 요구 사항이 있는 경우
  * 애플리케이션이 민감한 데이터를 다루는 경우
  * 특정 인라인 스크립트만 허용하고 나머지는 차단해야 하는 경우
  * 준수 요구 사항이 엄격한 CSP를 명시하는 경우

## 논스를 사용하지 않는 경우[](https://nextjs.org/docs/pages/guides/content-security-policy#without-nonces)

논스가 필요 없는 애플리케이션은 [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js) 파일에서 CSP 헤더를 직접 설정할 수 있습니다:

next.config.js
[code]
    const isDev = process.env.NODE_ENV === 'development'

    const cspHeader = `
        default-src 'self';
        script-src 'self' 'unsafe-inline'${isDev ? " 'unsafe-eval'" : ''};
        style-src 'self' 'unsafe-inline';
        img-src 'self' blob: data:;
        font-src 'self';
        object-src 'none';
        base-uri 'self';
        form-action 'self';
        frame-ancestors 'none';
        upgrade-insecure-requests;
    `

    module.exports = {
      async headers() {
        return [
          {
            source: '/(.*)',
            headers: [
              {
                key: 'Content-Security-Policy',
                value: cspHeader.replace(/\n/g, ''),
              },
            ],
          },
        ]
      },
    }
[/code]

## 개발 vs 프로덕션 고려 사항[](https://nextjs.org/docs/pages/guides/content-security-policy#development-vs-production-considerations)

CSP 구현은 개발 환경과 프로덕션 환경에서 다릅니다.

### 개발 환경[](https://nextjs.org/docs/pages/guides/content-security-policy#development-environment)

개발 환경에서는 React가 브라우저에서 서버 측 오류 스택이 어디에서 발생했는지 보여주기 위해 `eval`을 사용하므로 `'unsafe-eval'`을 활성화해야 합니다.

proxy.ts

JavaScriptTypeScript
[code]
    export function proxy(request: NextRequest) {
      const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
      const isDev = process.env.NODE_ENV === 'development'

      const cspHeader = `
[/code]

default-src 'self';
        script-src 'self' 'nonce-${nonce}' 'strict-dynamic' ${isDev ? "'unsafe-eval'" : ''};
        style-src 'self' ${isDev ? "'unsafe-inline'" : `'nonce-${nonce}'`};
        img-src 'self' blob: data:;
        font-src 'self';
        object-src 'none';
        base-uri 'self';
        form-action 'self';
        frame-ancestors 'none';
        upgrade-insecure-requests;
    `

      // Rest of proxy implementation
    }
[/code]

### 프로덕션 배포[](https://nextjs.org/docs/pages/guides/content-security-policy#production-deployment)

프로덕션에서 자주 발생하는 문제:

  * **Nonce가 적용되지 않음**: 프록시가 필요한 모든 라우트에서 동작하는지 확인하세요
  * **정적 자산이 차단됨**: CSP가 Next.js 정적 자산을 허용하는지 검증하세요
  * **서드파티 스크립트**: 필요한 도메인을 CSP 정책에 추가하세요

## 문제 해결[](https://nextjs.org/docs/pages/guides/content-security-policy#troubleshooting)

### 서드파티 스크립트[](https://nextjs.org/docs/pages/guides/content-security-policy#third-party-scripts)

CSP와 함께 서드파티 스크립트를 사용할 때는 필요한 도메인을 추가하고 nonce를 전달해야 합니다:

pages/_app.tsx

JavaScriptTypeScript
[code]
    import type { AppProps } from 'next/app'
    import Script from 'next/script'

    export default function App({ Component, pageProps }: AppProps) {
      const nonce = pageProps.nonce

      return (
        <>
          <Component {...pageProps} />
          <Script
            src="https://www.googletagmanager.com/gtag/js"
            strategy="afterInteractive"
            nonce={nonce}
          />
        </>
      )
    }
[/code]

CSP를 업데이트하여 서드파티 도메인을 허용하세요:

proxy.ts

JavaScriptTypeScript
[code]
    const cspHeader = `
      default-src 'self';
      script-src 'self' 'nonce-${nonce}' 'strict-dynamic' https://www.googletagmanager.com;
      connect-src 'self' https://www.google-analytics.com;
      img-src 'self' data: https://www.google-analytics.com;
    `
[/code]

### 흔한 CSP 위반[](https://nextjs.org/docs/pages/guides/content-security-policy#common-csp-violations)

  1. **인라인 스타일**: nonce를 지원하는 CSS-in-JS 라이브러리를 사용하거나 스타일을 외부 파일로 이동하세요
  2. **동적 import**: script-src 정책에서 동적 import를 허용하는지 확인하세요
  3. **WebAssembly**: WebAssembly를 사용하는 경우 `'wasm-unsafe-eval'`을 추가하세요
  4. **서비스 워커**: 서비스 워커 스크립트에 적절한 정책을 추가하세요

## 버전 기록[](https://nextjs.org/docs/pages/guides/content-security-policy#version-history)

Version| Changes
---|---
`v14.0.0`| 해시 기반 CSP를 위한 실험적 SRI 지원이 추가됨
`v13.4.20`| 올바른 nonce 처리와 CSP 헤더 파싱을 위해 권장됨.

보내기
