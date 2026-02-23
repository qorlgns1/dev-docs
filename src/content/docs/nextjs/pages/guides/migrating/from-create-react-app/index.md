---
title: '마이그레이션: Create React App'
description: '이 가이드는 기존 Create React App(CRA) 사이트를 Next.js로 마이그레이션하는 방법을 설명합니다.'
---

# 마이그레이션: Create React App | Next.js

소스 URL: https://nextjs.org/docs/pages/guides/migrating/from-create-react-app

[가이드](https://nextjs.org/docs/pages/guides)[마이그레이션](https://nextjs.org/docs/pages/guides/migrating)Create React App

# Create React App에서 Next.js로 마이그레이션하는 방법

최종 업데이트 2026년 2월 20일

이 가이드는 기존 Create React App(CRA) 사이트를 Next.js로 마이그레이션하는 방법을 설명합니다.

## 왜 전환하나요?[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#why-switch)

Create React App에서 Next.js로 전환하고 싶은 이유는 여러 가지가 있습니다.

### 초기 페이지 로딩 시간이 느림[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#slow-initial-page-loading-time)

Create React App은 순수한 클라이언트 사이드 렌더링을 사용합니다. [싱글 페이지 애플리케이션(SPA)](https://nextjs.org/docs/app/guides/single-page-applications)으로 알려진 클라이언트 사이드 전용 애플리케이션은 종종 초기 페이지 로딩 시간이 느립니다. 이는 다음과 같은 이유 때문입니다.

  1. 브라우저가 React 코드와 전체 애플리케이션 번들을 다운로드해 실행해야만, 코드가 데이터를 로드하기 위한 요청을 보낼 수 있습니다.
  2. 새로운 기능과 의존성을 추가할 때마다 애플리케이션 코드가 커집니다.

### 자동 코드 분할 없음[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#no-automatic-code-splitting)

앞서 언급한 느린 로딩 문제는 코드 분할로 어느 정도 완화할 수 있습니다. 그러나 코드 분할을 수동으로 시도하면 네트워크 워터폴을 의도치 않게 유발할 수 있습니다. Next.js는 라우터와 빌드 파이프라인에 자동 코드 분할과 트리 셰이킹을 기본 제공하여 이 문제를 해결합니다.

### 네트워크 워터폴[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#network-waterfalls)

애플리케이션이 데이터를 가져오기 위해 클라이언트-서버 요청을 순차적으로 수행할 때 성능 저하가 자주 발생합니다. [SPA](https://nextjs.org/docs/app/guides/single-page-applications)에서 데이터 페칭 패턴은 플레이스홀더를 렌더링한 뒤 컴포넌트가 마운트된 후에 데이터를 가져오는 방식입니다. 문제는 자식 컴포넌트가 부모 컴포넌트의 데이터 로딩이 끝난 뒤에야 데이터를 가져오기 시작할 수 있어, “워터폴” 형태의 요청이 발생한다는 점입니다.

Next.js는 클라이언트 사이드 데이터 페칭을 지원하면서도 데이터를 서버에서 가져오도록 옮길 수 있게 해줍니다. 이는 클라이언트-서버 워터폴을 완전히 제거하는 경우가 많습니다.

### 빠르고 의도적인 로딩 상태[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#fast-and-intentional-loading-states)

[React Suspense를 통한 스트리밍](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)을 기본 지원하므로, 네트워크 워터폴을 만들지 않고도 어떤 UI 조각을 어떤 순서로 먼저 로드할지 정의할 수 있습니다.

이를 통해 더 빠르게 로드되는 페이지를 만들고 [레이아웃 시프트](https://vercel.com/blog/how-core-web-vitals-affect-seo)를 제거할 수 있습니다.

### 데이터 페칭 전략 선택[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#choose-the-data-fetching-strategy)

필요에 따라 Next.js에서는 페이지나 컴포넌트 단위로 데이터 페칭 전략을 선택할 수 있습니다. 예를 들어, CMS에서 데이터를 가져와 게시글을 빌드 시점(SSG)에 렌더링해 빠른 로드 속도를 얻거나, 필요한 경우 요청 시점(SSR)에 데이터를 가져올 수 있습니다.

### Proxy[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#proxy)

[Next.js Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 사용하면 요청이 완료되기 전에 서버에서 코드를 실행할 수 있습니다. 예를 들어, 인증이 필요한 페이지에서 프록시를 통해 사용자를 로그인 페이지로 리디렉션하여 인증되지 않은 콘텐츠가 깜빡 보이는 현상을 방지할 수 있습니다. 또한 A/B 테스트, 실험, [국제화](https://nextjs.org/docs/app/guides/internationalization)와 같은 기능에도 활용할 수 있습니다.

### 내장 최적화[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#built-in-optimizations)

[이미지](https://nextjs.org/docs/app/api-reference/components/image), [폰트](https://nextjs.org/docs/app/api-reference/components/font), [서드파티 스크립트](https://nextjs.org/docs/app/guides/scripts)는 애플리케이션 성능에 큰 영향을 줍니다. Next.js는 이러한 요소를 자동으로 최적화하는 특화된 컴포넌트와 API를 제공합니다.

## 마이그레이션 단계[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#migration-steps)

목표는 작동하는 Next.js 애플리케이션을 가능한 한 빨리 구축해, 이후 Next.js 기능을 점진적으로 도입할 수 있게 하는 것입니다. 우선 기존 라우터를 즉시 대체하지 않고 애플리케이션을 순수 클라이언트 사이드 애플리케이션([SPA](https://nextjs.org/docs/app/guides/single-page-applications))으로 취급합니다. 이렇게 하면 복잡성과 머지 충돌을 줄일 수 있습니다.

> **참고** : `package.json`의 사용자 지정 `homepage` 필드, 커스텀 서비스 워커, 특정 Babel/webpack 조정 등 고급 CRA 구성을 사용 중이라면, 가이드 마지막의 **추가 고려 사항** 섹션에서 이러한 기능을 Next.js에서 복제하거나 적응시키는 팁을 확인하세요.

### 1단계: Next.js 의존성 설치[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-1-install-the-nextjs-dependency)

기존 프로젝트에 Next.js를 설치하세요.

pnpmnpmyarnbun

터미널
```
    pnpm add next@latest
```

### 2단계: Next.js 구성 파일 생성[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-2-create-the-nextjs-configuration-file)

프로젝트 루트(`package.json`과 같은 수준)에 `next.config.ts`를 생성하세요. 이 파일에는 [Next.js 구성 옵션](https://nextjs.org/docs/app/api-reference/config/next-config-js)이 들어갑니다.

next.config.ts
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      output: 'export', // Outputs a Single-Page Application (SPA)
      distDir: 'build', // Changes the build output directory to `build`
    }

    export default nextConfig
```

> **참고** : `output: 'export'`를 사용하면 정적 내보내기를 수행하는 것이며, SSR이나 API 같은 서버 사이드 기능을 사용할 수 **없습니다**. Next.js 서버 기능을 활용하려면 이 줄을 제거하세요.

### 3단계: 루트 레이아웃 생성[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-3-create-the-root-layout)

Next.js [App Router](https://nextjs.org/docs/app) 애플리케이션에는 모든 페이지를 감싸는 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout) 파일이 필요하며, 이는 [React Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)입니다.

CRA 애플리케이션에서 루트 레이아웃 파일과 가장 유사한 것은 `<html>`, `<head>`, `<body>` 태그가 들어 있는 `public/index.html`입니다.

  1. `src` 폴더 안(또는 루트에 `app`을 두고 싶다면 프로젝트 루트)에 새 `app` 디렉터리를 만듭니다.
  2. `app` 디렉터리 안에 `layout.tsx`(또는 `layout.js`) 파일을 생성합니다.

app/layout.tsx

JavaScriptTypeScript
```
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return '...'
    }
```

이제 이전 `index.html`의 내용을 `<RootLayout>` 컴포넌트로 복사하세요. `body div#root`(및 `body noscript`)를 `<div id="root">{children}</div>`로 바꿉니다.

app/layout.tsx

JavaScriptTypeScript
```
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <head>
            <meta charSet="UTF-8" />
            <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>React App</title>
            <meta name="description" content="Web site created..." />
          </head>
          <body>
            <div id="root">{children}</div>
          </body>
        </html>
      )
    }
```

> **알아두면 좋아요** : Next.js는 기본적으로 CRA의 `public/manifest.json`, 추가 아이콘, [테스트 구성](https://nextjs.org/docs/app/guides/testing)을 무시합니다. 이러한 요소가 필요하다면 Next.js의 [Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)와 [테스트](https://nextjs.org/docs/app/guides/testing) 설정을 사용하세요.

### 4단계: 메타데이터[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-4-metadata)

Next.js는 `<meta charset="UTF-8" />`와 `<meta name="viewport" content="width=device-width, initial-scale=1" />` 태그를 자동으로 포함하므로 `<head>`에서 제거할 수 있습니다.

app/layout.tsx

JavaScriptTypeScript
```
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <head>
            <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
            <title>React App</title>
            <meta name="description" content="Web site created..." />
          </head>
          <body>
            <div id="root">{children}</div>
          </body>
        </html>
      )
    }
```

`favicon.ico`, `icon.png`, `robots.txt` 같은 [메타데이터 파일](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#file-based-metadata)은 `app` 디렉터리 최상위에 배치하기만 하면 애플리케이션 `<head>` 태그에 자동으로 추가됩니다. [지원되는 모든 파일](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#file-based-metadata)을 `app` 디렉터리로 옮긴 후에는 해당 `<link>` 태그를 안전하게 삭제할 수 있습니다.

app/layout.tsx

JavaScriptTypeScript
```
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <head>
            <title>React App</title>
            <meta name="description" content="Web site created..." />
          </head>
          <body>
            <div id="root">{children}</div>
          </body>
        </html>
      )
    }
```

마지막으로 Next.js는 [Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)를 통해 남은 `<head>` 태그를 관리할 수 있습니다. 최종 메타데이터 정보를 내보낸 [`metadata` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-object)로 옮기세요.

app/layout.tsx

JavaScriptTypeScript
```
    import type { Metadata } from 'next'

    export const metadata: Metadata = {
      title: 'React App',
      description: 'Web site created with Next.js.',
    }

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>
            <div id="root">{children}</div>
          </body>
        </html>
      )
    }
```

위 변경을 통해 `index.html`에서 모든 것을 선언하던 방식에서, 프레임워크에 내장된 Next.js의 규칙 기반 접근 방식([Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images))으로 전환했습니다. 이 방식은 페이지의 SEO와 공유 성능을 더 쉽게 개선하도록 도와줍니다.

### 5단계: 스타일[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-5-styles)

CRA와 마찬가지로 Next.js는 [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules)을 기본 지원합니다. 또한 [전역 CSS import](https://nextjs.org/docs/app/getting-started/css#global-css)도 지원합니다.

전역 CSS 파일이 있다면 `app/layout.tsx`에 import 하세요.

app/layout.tsx

JavaScriptTypeScript
```
    import '../index.css'

    export const metadata = {
      title: 'React App',
      description: 'Web site created with Next.js.',
```

}

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>
            <div id="root">{children}</div>
          </body>
        </html>
      )
    }
[/code]

Tailwind CSS를 사용 중이라면 [설치 문서](https://nextjs.org/docs/app/getting-started/css#tailwind-css)를 확인하세요.

### 6단계: 엔트리포인트 페이지 만들기[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-6-create-the-entrypoint-page)

Create React App은 엔트리 포인트로 `src/index.tsx`(또는 `index.js`)를 사용합니다. Next.js(App Router)에서는 `app` 디렉터리의 각 폴더가 하나의 라우트에 대응하며, 각 폴더에는 `page.tsx`가 있어야 합니다.

현재는 앱을 SPA로 유지하며 **모든** 라우트를 가로채고 싶으므로 [선택적 캐치올 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#optional-catch-all-segments)를 사용합니다.

  1. **`app` 내부에 `[[...slug]]` 디렉터리를 만듭니다.**

[code]
    app
     ┣ [[...slug]]
     ┃ ┗ page.tsx
     ┣ layout.tsx
[/code]

  2. **다음 내용을 `page.tsx`에 추가합니다.**

app/[[...slug]]/page.tsx

JavaScriptTypeScript
[code]
    export function generateStaticParams() {
      return [{ slug: [''] }]
    }

    export default function Page() {
      return '...' // We'll update this
    }
[/code]

이 설정은 비어 있는 슬러그(`/`)에 대해 단일 라우트를 생성하도록 Next.js에 지시하여 사실상 **모든** 라우트를 동일한 페이지에 매핑합니다. 이 페이지는 정적 HTML로 사전 렌더링되는 [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)입니다.

### 7단계: 클라이언트 전용 엔트리포인트 추가[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-7-add-a-client-only-entrypoint)

다음으로 CRA의 루트 App 컴포넌트를 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 안에 삽입하여 모든 로직을 클라이언트 측에 유지합니다. 처음 Next.js를 사용한다면, 클라이언트 컴포넌트도 기본적으로 서버에서 사전 렌더링된다는 점을 알아두세요. 즉, 추가로 클라이언트 사이드 JavaScript를 실행할 수 있는 능력이 있다고 생각하면 됩니다.

`app/[[...slug]]/`에 `client.tsx`(또는 `client.js`)를 생성하세요:

app/[[...slug]]/client.tsx

JavaScriptTypeScript
[code]
    'use client'

    import dynamic from 'next/dynamic'

    const App = dynamic(() => import('../../App'), { ssr: false })

    export function ClientOnly() {
      return <App />
    }
[/code]

  * `'use client'` 지시문은 이 파일을 **클라이언트 컴포넌트**로 지정합니다.
  * `ssr: false`가 포함된 `dynamic` import는 `<App />` 컴포넌트의 서버 사이드 렌더링을 비활성화하여 진정한 클라이언트 전용(SPA)으로 만듭니다.

이제 새 컴포넌트를 사용하도록 `page.tsx`(또는 `page.js`)를 업데이트합니다:

app/[[...slug]]/page.tsx

JavaScriptTypeScript
[code]
    import { ClientOnly } from './client'

    export function generateStaticParams() {
      return [{ slug: [''] }]
    }

    export default function Page() {
      return <ClientOnly />
    }
[/code]

### 8단계: 정적 이미지 import 업데이트[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-8-update-static-image-imports)

CRA에서 이미지 파일을 import하면 해당 파일의 공개 URL이 문자열로 반환됩니다:
[code]
    import image from './img.png'

    export default function App() {
      return <img src={image} />
    }
[/code]

Next.js에서는 정적 이미지 import가 객체를 반환합니다. 이 객체를 Next.js의 [`<Image>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/image)에 직접 전달하거나, 기존 `<img>` 태그와 함께 객체의 `src` 속성을 사용할 수 있습니다.

`<Image>` 컴포넌트는 [자동 이미지 최적화](https://nextjs.org/docs/app/api-reference/components/image)를 제공하며, 이미지의 실제 크기를 기반으로 결과 `<img>`의 `width`와 `height` 속성을 자동으로 설정해 로딩 시 레이아웃 시프트를 방지합니다. 그러나 이미지의 한쪽 차원만 스타일링되고 다른 쪽이 `auto`로 설정되지 않은 경우에는 `<img>`의 차원 속성 값으로 고정되어 이미지가 찌그러질 수 있습니다.

`<img>` 태그를 유지하면 애플리케이션의 변경량을 줄이고 위 문제를 예방할 수 있습니다. 이후 필요할 때 [로더를 구성](https://nextjs.org/docs/app/api-reference/components/image#loader)하거나 자동 이미지 최적화를 제공하는 기본 Next.js 서버로 이전하여 `<Image>` 컴포넌트로 점진적으로 전환할 수 있습니다.

**`/public`에서 import한 이미지의 절대 경로를 상대 import로 변환하세요:**
[code]
    // Before
    import logo from '/logo.png'

    // After
    import logo from '../public/logo.png'
[/code]

**`<img>` 태그에는 이미지 객체 전체 대신 `src` 속성을 전달하세요:**
[code]
    // Before
    <img src={logo} />

    // After
    <img src={logo.src} />
[/code]

또는 파일명을 기준으로 이미지 자산의 공개 URL을 참조할 수도 있습니다. 예를 들어 `public/logo.png`는 애플리케이션에서 `/logo.png`로 제공되며, 이는 `src` 값이 됩니다.

> **경고:** TypeScript를 사용 중이라면 `src` 속성에 접근할 때 타입 오류가 발생할 수 있습니다. 이를 해결하려면 `tsconfig.json`의 [`include` 배열](https://www.typescriptlang.org/tsconfig#include)에 `next-env.d.ts`를 추가해야 합니다. Next.js는 9단계에서 애플리케이션을 실행할 때 이 파일을 자동으로 생성합니다.

### 9단계: 환경 변수 마이그레이션[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-9-migrate-environment-variables)

Next.js는 CRA와 유사한 방식으로 [환경 변수](https://nextjs.org/docs/app/guides/environment-variables)를 지원하지만, 브라우저에서 노출하려는 변수에는 반드시 `NEXT_PUBLIC_` 접두사가 필요합니다.

주요 차이는 클라이언트 측에서 환경 변수를 노출할 때 사용하는 접두사입니다. `REACT_APP_` 접두사를 사용하는 모든 환경 변수를 `NEXT_PUBLIC_`으로 변경하세요.

### 10단계: `package.json` 스크립트 업데이트[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-10-update-scripts-in-packagejson)

`package.json` 스크립트를 Next.js 명령으로 업데이트하세요. 또한 `.gitignore`에 `.next`와 `next-env.d.ts`를 추가합니다:

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "npx serve@latest ./build"
      }
    }
[/code]

.gitignore
[code]
    # ...
    .next
    next-env.d.ts
[/code]

이제 다음 명령을 실행할 수 있습니다:

pnpmnpmyarnbun

Terminal
[code]
    pnpm dev
[/code]

<http://localhost:3000>을 열면 Next.js(SPA 모드)에서 애플리케이션이 실행되는 것을 확인할 수 있습니다.

### 11단계: 정리[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#step-11-clean-up)

이제 Create React App에만 필요한 아티팩트를 제거할 수 있습니다:

  * `public/index.html`
  * `src/index.tsx`
  * `src/react-app-env.d.ts`
  * `reportWebVitals` 설정
  * `react-scripts` 의존성(`package.json`에서 제거)

## 추가 고려사항[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#additional-considerations)

### CRA에서 커스텀 `homepage` 사용[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#using-a-custom-homepage-in-cra)

CRA의 `package.json`에서 `homepage` 필드를 사용하여 특정 하위 경로 아래에 앱을 제공했다면, Next.js에서는 `next.config.ts`의 [`basePath` 설정](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)으로 동일하게 구성할 수 있습니다:

next.config.ts
[code]
    import { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      basePath: '/my-subpath',
      // ...
    }

    export default nextConfig
[/code]

### 커스텀 `Service Worker` 처리[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#handling-a-custom-service-worker)

CRA의 서비스 워커(예: `create-react-app`의 `serviceWorker.js`)를 사용했다면, Next.js에서 [PWA(Progressive Web Applications)](https://nextjs.org/docs/app/guides/progressive-web-apps)를 만드는 방법을 참고하세요.

### API 요청 프록시 [](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#proxying-api-requests)

CRA 앱에서 `package.json`의 `proxy` 필드로 백엔드 서버에 요청을 전달했다면, Next.js에서는 `next.config.ts`의 [rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)로 동일하게 구성할 수 있습니다:

next.config.ts
[code]
    import { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      async rewrites() {
        return [
          {
            source: '/api/:path*',
            destination: 'https://your-backend.com/:path*',
          },
        ]
      },
    }
[/code]

### 커스텀 Webpack[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#custom-webpack)

CRA에서 커스텀 webpack 또는 Babel 구성을 사용했다면, `next.config.ts`에서 Next.js 구성을 확장할 수 있습니다:

next.config.ts
[code]
    import { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      webpack: (config, { isServer }) => {
        // Modify the webpack config here
        return config
      },
    }

    export default nextConfig
[/code]

> **참고** : 이렇게 하려면 `dev` 스크립트에 `--webpack`을 추가하여 Webpack을 사용해야 합니다.

### TypeScript 설정[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#typescript-setup)

`tsconfig.json`이 있으면 Next.js가 자동으로 TypeScript를 설정합니다. `tsconfig.json`의 `include` 배열에 `next-env.d.ts`가 포함되어 있는지 확인하세요:
[code]
    {
      "include": ["next-env.d.ts", "app/**/*", "src/**/*"]
    }
[/code]

## 번들러 호환성[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#bundler-compatibility)

Create React App은 번들링에 webpack을 사용합니다. Next.js는 이제 더 빠른 로컬 개발을 위해 [Turbopack](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)을 기본값으로 사용합니다:
[code]
    next dev  # Uses Turbopack by default
[/code]

CRA와 유사하게 Webpack을 사용하려면:
[code]
    next dev --webpack
[/code]

고급 webpack 설정을 마이그레이션해야 한다면 여전히 [커스텀 webpack 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack)을 제공할 수 있습니다.

## 다음 단계[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#next-steps)

모든 작업이 정상적으로 끝났다면, 이제 Next.js에서 단일 페이지 애플리케이션으로 작동하는 앱을 갖게 됩니다. 아직 서버 사이드 렌더링이나 파일 기반 라우팅 같은 Next.js 기능을 활용하고 있지는 않지만, 이제 점진적으로 도입할 수 있습니다:

  * **React Router에서** [Next.js App Router](https://nextjs.org/docs/app)로 마이그레이션하여 다음을 활용하세요:
    * 자동 코드 분할
    * [스트리밍 서버 렌더링](https://nextjs.org/docs/app/api-reference/file-conventions/loading)
    * [React 서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)
  * [`<Image>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/image)로 **이미지를 최적화**하세요.
  * [`next/font`](https://nextjs.org/docs/app/api-reference/components/font)로 **폰트를 최적화**하세요.
  * [`<Script>` 컴포넌트](https://nextjs.org/docs/app/guides/scripts)로 **서드파티 스크립트를 최적화**하세요.
  * Next.js [권장 규칙](https://nextjs.org/docs/app/api-reference/config/eslint#setup-eslint)과 함께 **ESLint를 활성화**하세요.

> **참고** : 정적 내보내기(`output: 'export'`)는 `useParams` 훅이나 다른 서버 기능을 [현재 지원하지 않습니다](https://github.com/vercel/next.js/issues/54393). 모든 Next.js 기능을 사용하려면 `next.config.ts`에서 `output: 'export'`를 제거하세요.

보내기
