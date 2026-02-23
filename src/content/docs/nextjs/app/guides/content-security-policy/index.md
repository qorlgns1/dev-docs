---
title: '가이드: Content Security Policy'
description: 'CSP를 사용하면 개발자는 콘텐츠 소스, 스크립트, 스타일시트, 이미지, 폰트, 객체, 미디어(오디오, 비디오), iframe 등에서 허용되는 출처를 지정할 수 있습니다.'
---

# 가이드: Content Security Policy | Next.js

Source URL: https://nextjs.org/docs/app/guides/content-security-policy

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)Content Security Policy

Copy page

# Next.js 애플리케이션에 Content Security Policy(CSP)를 설정하는 방법

최종 업데이트 2026년 2월 20일

[Content Security Policy(CSP)](https://developer.mozilla.org/docs/Web/HTTP/CSP)는 교차 사이트 스크립팅(XSS), 클릭재킹, 기타 코드 삽입 공격 등 다양한 보안 위협으로부터 Next.js 애플리케이션을 보호하는 데 중요합니다.

CSP를 사용하면 개발자는 콘텐츠 소스, 스크립트, 스타일시트, 이미지, 폰트, 객체, 미디어(오디오, 비디오), iframe 등에서 허용되는 출처를 지정할 수 있습니다.

Examples

  * [Strict CSP](https://github.com/vercel/next.js/tree/canary/examples/with-strict-csp)

## Nonces[](https://nextjs.org/docs/app/guides/content-security-policy#nonces)

[nonce](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce)는 일회용으로 생성되는 고유하고 무작위 문자열입니다. CSP와 함께 사용되어 특정 인라인 스크립트나 스타일을 선택적으로 허용해 엄격한 CSP 지시문을 우회할 수 있습니다.

### 왜 nonce를 사용해야 하나요?[](https://nextjs.org/docs/app/guides/content-security-policy#why-use-a-nonce)

CSP는 공격을 막기 위해 인라인 및 외부 스크립트를 모두 차단할 수 있습니다. nonce는 일치하는 값이 포함된 특정 스크립트만 안전하게 실행하도록 허용합니다.

공격자가 페이지에 스크립트를 로드하려면 nonce 값을 추측해야 합니다. 따라서 nonce는 예측 불가능하고 요청마다 고유해야 합니다.

### Proxy로 nonce 추가하기[](https://nextjs.org/docs/app/guides/content-security-policy#adding-a-nonce-with-proxy)

[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 사용하면 페이지가 렌더링되기 전에 헤더를 추가하고 nonce를 생성할 수 있습니다.

페이지가 표시될 때마다 새로운 nonce를 생성해야 합니다. 즉, nonce를 추가하려면 **반드시 [dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)을 사용해야 합니다**.

예시:

> **알아 두면 좋아요**: 개발 환경에서는 React가 브라우저에서 서버 측 오류 스택을 재구성하는 등 향상된 디버깅 정보를 제공하기 위해 `eval`을 사용하므로 `'unsafe-eval'`이 필요합니다. `unsafe-eval`은 프로덕션에서는 필요하지 않습니다. React와 Next.js는 기본적으로 프로덕션에서 `eval`을 사용하지 않습니다.

proxy.ts

JavaScriptTypeScript
```
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
```

기본적으로 Proxy는 모든 요청에서 실행됩니다. [`matcher`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher)를 사용해 특정 경로에서만 Proxy가 실행되도록 필터링할 수 있습니다.

CSP 헤더가 필요 없는 `next/link` 프리페치와 정적 자산은 매칭에서 제외하는 것이 좋습니다.

proxy.ts

JavaScriptTypeScript
```
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
```

### Next.js에서 nonce가 동작하는 방식[](https://nextjs.org/docs/app/guides/content-security-policy#how-nonces-work-in-nextjs)

nonce를 사용하려면 페이지가 **동적 렌더링**되어야 합니다. Next.js는 요청에 포함된 CSP 헤더를 기반으로 **서버 측 렌더링** 중에 nonce를 적용합니다. 정적 페이지는 빌드 시점에 생성되므로 요청/응답 헤더가 존재하지 않아 nonce를 삽입할 수 없습니다.

동적으로 렌더링되는 페이지에서 nonce 지원이 동작하는 방식은 다음과 같습니다.

  1. **Proxy가 nonce를 생성**: proxy가 요청에 대한 고유 nonce를 만들고 이를 `Content-Security-Policy` 헤더에 추가하며 사용자 정의 `x-nonce` 헤더에도 설정합니다.
  2. **Next.js가 nonce를 추출**: 렌더링 중 Next.js는 `Content-Security-Policy` 헤더를 파싱하여 `'nonce-{value}'` 패턴으로 nonce를 추출합니다.
  3. **nonce 자동 적용**: Next.js는 nonce를 다음에 자동으로 첨부합니다.
     * 프레임워크 스크립트(React, Next.js 런타임)
     * 페이지별 JavaScript 번들
     * Next.js가 생성하는 인라인 스타일과 스크립트
     * `nonce` prop을 사용하는 `<Script>` 컴포넌트

이 자동 동작 덕분에 각 태그에 nonce를 수동으로 추가할 필요가 없습니다.

### 동적 렌더링 강제하기[](https://nextjs.org/docs/app/guides/content-security-policy#forcing-dynamic-rendering)

nonce를 사용한다면 페이지를 명시적으로 동적 렌더링으로 전환해야 할 수도 있습니다.

app/page.tsx

JavaScriptTypeScript
```
    import { connection } from 'next/server'

    export default async function Page() {
      // wait for an incoming request to render this page
      await connection()
      // Your page content
    }
```

### nonce 읽기[](https://nextjs.org/docs/app/guides/content-security-policy#reading-the-nonce)

[`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)를 사용해 [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서 nonce를 읽을 수 있습니다.

app/page.tsx

JavaScriptTypeScript
```
    import { headers } from 'next/headers'
    import Script from 'next/script'

    export default async function Page() {
      const nonce = (await headers()).get('x-nonce')

      return (
        <Script
          src="https://www.googletagmanager.com/gtag/js"
          strategy="afterInteractive"
          nonce={nonce}
        />
      )
    }
```

## CSP와 정적/동적 렌더링 비교[](https://nextjs.org/docs/app/guides/content-security-policy#static-vs-dynamic-rendering-with-csp)

nonce를 사용하면 Next.js 애플리케이션 렌더링 방식에 중요한 영향을 줍니다.

### 동적 렌더링 요구사항[](https://nextjs.org/docs/app/guides/content-security-policy#dynamic-rendering-requirement)

CSP에서 nonce를 사용하면 **모든 페이지가 동적 렌더링**되어야 합니다. 이는 다음을 의미합니다.

  * 페이지는 빌드에 성공하더라도 동적 렌더링 구성이 올바르지 않으면 런타임 오류가 발생할 수 있습니다.
  * 각 요청마다 새로운 nonce로 새 페이지가 생성됩니다.
  * 정적 최적화와 Incremental Static Regeneration(ISR)이 비활성화됩니다.
  * 추가 구성이 없다면 CDN이 페이지를 캐시할 수 없습니다.
  * 정적 셸 스크립트가 nonce에 접근할 수 없으므로 **Partial Prerendering(PPR)은 nonce 기반 CSP와 호환되지 않습니다**.

### 성능 영향[](https://nextjs.org/docs/app/guides/content-security-policy#performance-implications)

정적 렌더링에서 동적 렌더링으로 전환하면 성능에 다음과 같은 영향이 있습니다.

  * **초기 페이지 로드가 느려짐**: 요청마다 페이지를 생성해야 합니다.
  * **서버 부하 증가**: 모든 요청이 서버 측 렌더링을 요구합니다.
  * **CDN 캐싱 불가**: 기본적으로 동적 페이지는 엣지에서 캐시할 수 없습니다.
  * **호스팅 비용 증가**: 동적 렌더링에는 더 많은 서버 리소스가 필요합니다.

### nonce 사용 시기[](https://nextjs.org/docs/app/guides/content-security-policy#when-to-use-nonces)

다음 상황에서 nonce 사용을 고려하세요.

  * `'unsafe-inline'`을 허용하지 않는 엄격한 보안 요건이 있는 경우
  * 애플리케이션이 민감한 데이터를 처리하는 경우
  * 특정 인라인 스크립트만 허용하고 나머지를 차단해야 하는 경우
  * 규정 준수 요구사항이 엄격한 CSP를 요구하는 경우

## Nonce 없이 사용하기[](https://nextjs.org/docs/app/guides/content-security-policy#without-nonces)

nonce가 필요하지 않은 애플리케이션은 [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js)에서 직접 CSP 헤더를 설정할 수 있습니다.

next.config.js
```
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
```

## Subresource Integrity(실험적)[](https://nextjs.org/docs/app/guides/content-security-policy#subresource-integrity-experimental)

nonce의 대안으로 Next.js는 Subresource Integrity(SRI)를 사용한 해시 기반 CSP에 대한 실험적 지원을 제공합니다. 이 방식은 엄격한 CSP를 유지하면서도 정적 생성을 계속 사용할 수 있게 해 줍니다.

> **알아 두면 좋아요**: 이 기능은 실험적이며 App Router 애플리케이션에서 webpack 번들러를 사용할 때만 가능합니다.

### SRI 동작 방식[](https://nextjs.org/docs/app/guides/content-security-policy#how-sri-works)

nonce 대신 SRI는 빌드 시 JavaScript 파일의 암호화 해시를 생성합니다. 이 해시는 `integrity` 속성으로 스크립트 태그에 추가되어 브라우저가 전송 중 파일이 수정되지 않았는지 검증할 수 있게 합니다.

### SRI 활성화[](https://nextjs.org/docs/app/guides/content-security-policy#enabling-sri)

`next.config.js`에 실험적 SRI 구성을 추가하세요.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        sri: {
          algorithm: 'sha256', // or 'sha384' or 'sha512'
        },
      },
    }

    module.exports = nextConfig
```

### SRI와 함께하는 CSP 구성[](https://nextjs.org/docs/app/guides/content-security-policy#csp-configuration-with-sri)

SRI를 활성화해도 기존 CSP 정책을 계속 사용할 수 있습니다. SRI는 자산에 `integrity` 속성을 추가하여 독립적으로 동작합니다.

> **알아 두면 좋아요**: 동적 렌더링 시나리오에서는 필요하다면 proxy로 nonce를 계속 생성해 SRI 무결성 속성과 nonce 기반 CSP를 결합할 수 있습니다.

next.config.js
```
    const isDev = process.env.NODE_ENV === 'development'

    const cspHeader = `
        default-src 'self';
        script-src 'self'${isDev ? " 'unsafe-eval'" : ''};
        style-src 'self';
        img-src 'self' blob: data:;
        font-src 'self';
        object-src 'none';
        base-uri 'self';
        form-action 'self';
        frame-ancestors 'none';
```

upgrade-insecure-requests;
    `

    module.exports = {
      experimental: {
        sri: {
          algorithm: 'sha256',
        },
      },
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

### 넌스 대비 SRI의 이점[](https://nextjs.org/docs/app/guides/content-security-policy#benefits-of-sri-over-nonces)

  * **정적 생성** : 페이지를 정적으로 생성하고 캐시할 수 있음
  * **CDN 호환성** : 정적 페이지가 CDN 캐싱과 함께 동작함
  * **향상된 성능** : 요청마다 서버 사이드 렌더링이 필요 없음
  * **빌드 타임 보안** : 해시가 빌드 시점에 생성되어 무결성을 보장함

### SRI의 제한 사항[](https://nextjs.org/docs/app/guides/content-security-policy#limitations-of-sri)

  * **실험적 기능** : 향후 변경되거나 제거될 수 있음
  * **Webpack 한정** : Turbopack에서는 사용할 수 없음
  * **App Router 전용** : Pages Router에서는 지원되지 않음
  * **빌드 타임 한정** : 동적으로 생성되는 스크립트를 처리할 수 없음

## 개발 vs 프로덕션 고려 사항[](https://nextjs.org/docs/app/guides/content-security-policy#development-vs-production-considerations)

CSP 구현은 개발 환경과 프로덕션 환경에서 다르게 동작합니다.

### 개발 환경[](https://nextjs.org/docs/app/guides/content-security-policy#development-environment)

개발 환경에서는 React가 `eval`을 사용해 서버 오류 스택을 브라우저에서 재구성하는 등 향상된 디버깅 정보를 제공하므로 `'unsafe-eval'`을 활성화해야 합니다. 이를 통해 서버에서 오류가 어디에서 발생했는지 확인할 수 있습니다:

proxy.ts

JavaScriptTypeScript
```
    export function proxy(request: NextRequest) {
      const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
      const isDev = process.env.NODE_ENV === 'development'

      const cspHeader = `
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
```

### 프로덕션 배포[](https://nextjs.org/docs/app/guides/content-security-policy#production-deployment)

프로덕션에서 발생하는 일반적인 문제:

  * **넌스 미적용** : 필요한 모든 라우트에서 프록시가 실행되는지 확인
  * **정적 자산 차단** : CSP가 Next.js 정적 자산을 허용하는지 검증
  * **서드파티 스크립트** : 필요한 도메인을 CSP 정책에 추가

## 문제 해결[](https://nextjs.org/docs/app/guides/content-security-policy#troubleshooting)

### 서드파티 스크립트[](https://nextjs.org/docs/app/guides/content-security-policy#third-party-scripts)

CSP와 함께 서드파티 스크립트를 사용할 때:

app/layout.tsx

JavaScriptTypeScript
```
    import { GoogleTagManager } from '@next/third-parties/google'
    import { headers } from 'next/headers'

    export default async function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      const nonce = (await headers()).get('x-nonce')

      return (
        <html lang="en">
          <body>
            {children}
            <GoogleTagManager gtmId="GTM-XYZ" nonce={nonce} />
          </body>
        </html>
      )
    }
```

CSP를 업데이트해 서드파티 도메인을 허용하세요:

proxy.ts

JavaScriptTypeScript
```
    const cspHeader = `
      default-src 'self';
      script-src 'self' 'nonce-${nonce}' 'strict-dynamic' https://www.googletagmanager.com;
      connect-src 'self' https://www.google-analytics.com;
      img-src 'self' data: https://www.google-analytics.com;
    `
```

### 일반적인 CSP 위반[](https://nextjs.org/docs/app/guides/content-security-policy#common-csp-violations)

  1. **인라인 스타일** : 넌스를 지원하는 CSS-in-JS 라이브러리를 사용하거나 스타일을 외부 파일로 이동
  2. **동적 import** : script-src 정책에서 동적 import가 허용되는지 확인
  3. **WebAssembly** : WebAssembly를 사용한다면 `'wasm-unsafe-eval'`을 추가
  4. **서비스 워커** : 서비스 워커 스크립트에 맞는 정책을 추가

## 버전 기록[](https://nextjs.org/docs/app/guides/content-security-policy#version-history)

Version| Changes
---|---
`v14.0.0`| 해시 기반 CSP를 위한 실험적 SRI 지원 추가
`v13.4.20`| 적절한 넌스 처리 및 CSP 헤더 파싱을 위한 권장 버전.

##

- [proxy.js](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  - 프록시 파일 `proxy.js`의 API 레퍼런스.

- [headers](https://nextjs.org/docs/app/api-reference/functions/headers)
  - `headers` 함수의 API 레퍼런스.

Send