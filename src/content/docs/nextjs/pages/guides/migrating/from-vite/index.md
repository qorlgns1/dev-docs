---
title: '마이그레이션: Vite'
description: '이 가이드는 기존 Vite 애플리케이션을 Next.js로 마이그레이션하는 과정을 안내합니다.'
---

# 마이그레이션: Vite | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/migrating/from-vite

# Vite에서 Next.js로 마이그레이션하는 방법

최종 업데이트 2026년 2월 20일

이 가이드는 기존 Vite 애플리케이션을 Next.js로 마이그레이션하는 과정을 안내합니다.

## 왜 전환하나요?[](https://nextjs.org/docs/pages/guides/migrating/from-vite#why-switch)

Vite에서 Next.js로 전환하고 싶은 이유는 여러 가지가 있습니다.

### 느린 초기 페이지 로딩 시간[](https://nextjs.org/docs/pages/guides/migrating/from-vite#slow-initial-page-loading-time)

[기본 Vite React 플러그인](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-react)으로 애플리케이션을 구축했다면, 해당 앱은 순수 클라이언트 사이드 애플리케이션입니다. 클라이언트 사이드 전용 애플리케이션(SPA라고도 함)은 종종 초기 페이지 로딩이 느립니다. 그 이유는 다음과 같습니다.

  1. 브라우저가 React 코드와 전체 애플리케이션 번들이 다운로드 및 실행될 때까지 기다려야만 코드가 데이터를 불러오기 위한 요청을 보낼 수 있습니다.
  2. 새로운 기능과 추가 의존성을 도입할수록 애플리케이션 코드가 계속 커집니다.

### 자동 코드 분할 부재[](https://nextjs.org/docs/pages/guides/migrating/from-vite#no-automatic-code-splitting)

이전의 느린 로딩 문제를 코드 분할로 어느 정도 완화할 수 있습니다. 그러나 수동으로 코드 분할을 시도하면 오히려 성능이 악화되는 경우가 많습니다. 수동 코드 분할 중 의도치 않게 네트워크 폭포 현상이 발생하기 쉽습니다. Next.js는 라우터에 자동 코드 분할을 기본 제공해 이러한 문제를 해결합니다.

### 네트워크 폭포 현상[](https://nextjs.org/docs/pages/guides/migrating/from-vite#network-waterfalls)

애플리케이션이 데이터를 가져오기 위해 클라이언트-서버 요청을 순차적으로 수행할 때 성능 저하가 흔히 발생합니다. SPA에서 일반적인 데이터 패턴은 최초에 플레이스홀더를 렌더링하고, 컴포넌트가 마운트된 후 데이터를 가져오는 방식입니다. 그러나 이 방식에서는 데이터를 가져오는 자식 컴포넌트가 부모 컴포넌트의 데이터 로딩이 끝날 때까지 요청을 시작할 수 없습니다.

Next.js에서도 클라이언트 데이터 패칭이 가능하지만, 데이터를 서버로 옮겨 패칭할 수 있는 옵션을 제공하여 클라이언트-서버 폭포를 제거할 수 있습니다.

### 빠르고 의도적인 로딩 상태[](https://nextjs.org/docs/pages/guides/migrating/from-vite#fast-and-intentional-loading-states)

[React Suspense 스트리밍](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)을 기본 지원하므로, 네트워크 폭포 없이 UI의 어느 부분을 어떤 순서로 먼저 로드할지 더 의도적으로 제어할 수 있습니다.

이를 통해 더 빠르게 로드되는 페이지를 구축하고 [레이아웃 시프트](https://vercel.com/blog/how-core-web-vitals-affect-seo)를 제거할 수 있습니다.

### 데이터 패칭 전략 선택[](https://nextjs.org/docs/pages/guides/migrating/from-vite#choose-the-data-fetching-strategy)

필요에 따라 Next.js는 페이지와 컴포넌트 단위로 데이터를 패칭하는 전략을 선택할 수 있게 합니다. 빌드 시점, 서버 요청 시점, 혹은 클라이언트에서 데이터를 가져올지 결정할 수 있습니다. 예를 들어 CMS에서 데이터를 가져와 블로그 게시물을 빌드 시 렌더링하면 CDN에 효율적으로 캐시할 수 있습니다.

### Proxy[](https://nextjs.org/docs/pages/guides/migrating/from-vite#proxy)

[Next.js Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)는 요청이 완료되기 전에 서버에서 코드를 실행할 수 있게 해줍니다. 인증이 필요한 페이지에 방문할 때 사용자에게 미인증 콘텐츠가 순간적으로 보이는 문제를 로그인 페이지 리다이렉션으로 방지하는 데 특히 유용합니다. Proxy는 실험이나 [국제화](https://nextjs.org/docs/app/guides/internationalization)에도 도움이 됩니다.

### 내장 최적화[](https://nextjs.org/docs/pages/guides/migrating/from-vite#built-in-optimizations)

[이미지](https://nextjs.org/docs/app/api-reference/components/image), [폰트](https://nextjs.org/docs/app/api-reference/components/font), [서드파티 스크립트](https://nextjs.org/docs/app/guides/scripts)는 애플리케이션 성능에 큰 영향을 미칩니다. Next.js는 이러한 요소를 자동으로 최적화하는 내장 컴포넌트를 제공합니다.

## 마이그레이션 단계[](https://nextjs.org/docs/pages/guides/migrating/from-vite#migration-steps)

이 마이그레이션의 목표는 가능한 한 빨리 작동하는 Next.js 애플리케이션을 만드는 것이며, 이후에 Next.js 기능을 점진적으로 도입하면 됩니다. 시작 단계에서는 기존 라우터를 마이그레이션하지 않고 순수 클라이언트 사이드 애플리케이션(SPA)으로 유지합니다. 이렇게 하면 마이그레이션 중 문제를 만날 가능성을 줄이고 머지 충돌도 최소화할 수 있습니다.

### 1단계: Next.js 의존성 설치[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-1-install-the-nextjs-dependency)

첫 번째 작업은 `next`를 의존성으로 설치하는 것입니다.

pnpmnpmyarnbun

Terminal
```
    pnpm add next@latest
```

### 2단계: Next.js 구성 파일 생성[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-2-create-the-nextjs-configuration-file)

프로젝트 루트에 `next.config.mjs`를 생성합니다. 이 파일은 [Next.js 구성 옵션](https://nextjs.org/docs/app/api-reference/config/next-config-js)을 담습니다.

next.config.mjs
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      output: 'export', // Outputs a Single-Page Application (SPA).
      distDir: './dist', // Changes the build output directory to `./dist/`.
    }

    export default nextConfig
```

> **알아두면 좋아요:** Next.js 구성 파일은 `.js` 또는 `.mjs` 중 원하는 확장자를 사용할 수 있습니다.

### 3단계: TypeScript 구성 업데이트[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-3-update-typescript-configuration)

TypeScript를 사용 중이라면, Next.js와 호환되도록 `tsconfig.json`을 다음과 같이 수정해야 합니다. TypeScript를 사용하지 않는다면 이 단계를 건너뛰어도 됩니다.

  1. `tsconfig.node.json`에 대한 [프로젝트 참조](https://www.typescriptlang.org/tsconfig#references)를 제거합니다.
  2. [`include` 배열](https://www.typescriptlang.org/tsconfig#include)에 `./dist/types/**/*.ts`와 `./next-env.d.ts`를 추가합니다.
  3. [`exclude` 배열](https://www.typescriptlang.org/tsconfig#exclude)에 `./node_modules`를 추가합니다.
  4. [`compilerOptions`의 `plugins` 배열](https://www.typescriptlang.org/tsconfig#plugins)에 `{ "name": "next" }`를 추가합니다: `"plugins": [{ "name": "next" }]`
  5. [`esModuleInterop`](https://www.typescriptlang.org/tsconfig#esModuleInterop)을 `true`로 설정합니다: `"esModuleInterop": true`
  6. [`jsx`](https://www.typescriptlang.org/tsconfig#jsx)를 `react-jsx`로 설정합니다: `"jsx": "react-jsx"`
  7. [`allowJs`](https://www.typescriptlang.org/tsconfig#allowJs)를 `true`로 설정합니다: `"allowJs": true`
  8. [`forceConsistentCasingInFileNames`](https://www.typescriptlang.org/tsconfig#forceConsistentCasingInFileNames)를 `true`로 설정합니다: `"forceConsistentCasingInFileNames": true`
  9. [`incremental`](https://www.typescriptlang.org/tsconfig#incremental)을 `true`로 설정합니다: `"incremental": true`

다음은 이러한 변경 사항을 적용한 `tsconfig.json` 예시입니다.

tsconfig.json
```
    {
      "compilerOptions": {
        "target": "ES2020",
        "useDefineForClassFields": true,
        "lib": ["ES2020", "DOM", "DOM.Iterable"],
        "module": "ESNext",
        "esModuleInterop": true,
        "skipLibCheck": true,
        "moduleResolution": "bundler",
        "allowImportingTsExtensions": true,
        "resolveJsonModule": true,
        "isolatedModules": true,
        "noEmit": true,
        "jsx": "react-jsx",
        "strict": true,
        "noUnusedLocals": true,
        "noUnusedParameters": true,
        "noFallthroughCasesInSwitch": true,
        "allowJs": true,
        "forceConsistentCasingInFileNames": true,
        "incremental": true,
        "plugins": [{ "name": "next" }]
      },
      "include": ["./src", "./dist/types/**/*.ts", "./next-env.d.ts"],
      "exclude": ["./node_modules"]
    }
```

TypeScript 구성에 대한 자세한 내용은 [Next.js 문서](https://nextjs.org/docs/app/api-reference/config/typescript#ide-plugin)에서 확인할 수 있습니다.

### 4단계: 루트 레이아웃 생성[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-4-create-the-root-layout)

Next.js [App Router](https://nextjs.org/docs/app) 애플리케이션은 모든 페이지를 감싸는 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout) 파일을 포함해야 하며, 이는 애플리케이션 전체를 감싸는 [React Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)입니다. 이 파일은 `app` 디렉터리 최상위에 정의합니다.

Vite 애플리케이션에서 루트 레이아웃과 가장 유사한 파일은 `<html>`, `<head>`, `<body>` 태그를 담고 있는 [`index.html`](https://vitejs.dev/guide/#index-html-and-project-root)입니다.

이 단계에서는 `index.html` 파일을 루트 레이아웃 파일로 변환합니다.

  1. `src` 폴더 안에 새로운 `app` 디렉터리를 만듭니다.
  2. 해당 `app` 디렉터리에 새 `layout.tsx` 파일을 생성합니다.

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

> **알아두면 좋아요**: 레이아웃 파일에는 `.js`, `.jsx`, `.tsx` 확장자를 사용할 수 있습니다.

  3. 생성한 `<RootLayout>` 컴포넌트에 `index.html` 파일 내용을 복사하고, `body.div#root`와 `body.script` 태그를 `<div id="root">{children}</div>`로 바꿉니다.

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
            <meta charset="UTF-8" />
            <link rel="icon" type="image/svg+xml" href="/icon.svg" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>My App</title>
            <meta name="description" content="My App is a..." />
          </head>
          <body>
            <div id="root">{children}</div>
          </body>
        </html>
      )
    }
```

  4. Next.js는 [meta charset](https://developer.mozilla.org/docs/Web/HTML/Element/meta#charset)과 [meta viewport](https://developer.mozilla.org/docs/Web/HTML/Viewport_meta_tag) 태그를 기본으로 포함하므로 `<head>`에서 제거해도 안전합니다.

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
            <link rel="icon" type="image/svg+xml" href="/icon.svg" />
            <title>My App</title>
            <meta name="description" content="My App is a..." />
          </head>
          <body>
            <div id="root">{children}</div>
          </body>
        </html>
      )
    }
```

  5. `favicon.ico`, `icon.png`, `robots.txt`와 같은 [메타데이터 파일](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#file-based-metadata)은 `app` 디렉터리 최상위에 배치하기만 하면 애플리케이션 `<head>` 태그에 자동으로 추가됩니다. [지원되는 모든 파일](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#file-based-metadata)을 `app` 디렉터리로 옮긴 후에는 `<link>` 태그를 안전하게 삭제할 수 있습니다.

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

<title>My App</title>
            <meta name="description" content="My App is a..." />
          </head>
          <body>
            <div id="root">{children}</div>
          </body>
        </html>
      )
    }
```

  6. 마지막으로 Next.js는 [Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)를 통해 마지막 `<head>` 태그를 관리할 수 있습니다. 최종 메타데이터 정보를 내보낸 [`metadata` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-object)로 옮기세요.

app/layout.tsx

JavaScriptTypeScript
```
    import type { Metadata } from 'next'

    export const metadata: Metadata = {
      title: 'My App',
      description: 'My App is a...',
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

위 변경으로 `index.html`에서 모든 것을 선언하던 방식에서 프레임워크에 내장된 Next.js의 관례 기반 접근 방식([Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images))으로 전환했습니다. 이 접근 방식은 페이지의 SEO와 웹 공유성을 더욱 쉽게 개선할 수 있게 해 줍니다.

### Step 5: Create the Entrypoint Page[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-5-create-the-entrypoint-page)

Next.js에서는 `page.tsx` 파일을 생성해 애플리케이션의 엔트리포인트를 선언합니다. Vite에서 이 파일과 가장 가까운 대응은 `main.tsx` 파일입니다. 이 단계에서는 애플리케이션의 엔트리포인트를 설정합니다.

  1. **`app` 디렉터리에 `[[...slug]]` 디렉터리를 만듭니다.**

이 가이드에서는 먼저 Next.js를 SPA(Single Page Application)로 설정하는 것이 목표이므로, 페이지 엔트리포인트가 애플리케이션의 모든 가능한 라우트를 포착해야 합니다. 이를 위해 `app` 디렉터리에 새로운 `[[...slug]]` 디렉터리를 만드세요.

이 디렉터리는 [선택적 캐치올 라우트 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#optional-catch-all-segments)라고 합니다. Next.js는 폴더를 사용해 라우트를 정의하는 파일 시스템 기반 라우터를 사용합니다. 이 특수 디렉터리는 애플리케이션의 모든 라우트가 그 안의 `page.tsx` 파일로 전달되도록 해 줍니다.

  2. **`app/[[...slug]]` 디렉터리 안에 다음 내용을 가진 새 `page.tsx` 파일을 만듭니다.**

app/[[...slug]]/page.tsx

JavaScriptTypeScript
```
    import '../../index.css'

    export function generateStaticParams() {
      return [{ slug: [''] }]
    }

    export default function Page() {
      return '...' // We'll update this
    }
```

> **알아두면 좋아요**: Page 파일에는 `.js`, `.jsx`, `.tsx` 확장자를 모두 사용할 수 있습니다.

이 파일은 [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)입니다. `next build`를 실행하면 이 파일은 정적 자산으로 프리렌더링됩니다. 동적 코드가 필요하지 않습니다.

이 파일은 전역 CSS를 가져오고 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)가 `/`의 인덱스 라우트 하나만 생성하도록 지정합니다.

이제 클라이언트 전용으로 실행될 Vite 애플리케이션의 나머지를 이동해 봅시다.

app/[[...slug]]/client.tsx

JavaScriptTypeScript
```
    'use client'

    import React from 'react'
    import dynamic from 'next/dynamic'

    const App = dynamic(() => import('../../App'), { ssr: false })

    export function ClientOnly() {
      return <App />
    }
```

이 파일은 `'use client'` 지시문으로 정의된 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)입니다. 클라이언트 컴포넌트는 클라이언트로 전송되기 전에 서버에서 [HTML로 프리렌더링](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs)됩니다.

클라이언트 전용 애플리케이션으로 시작하려는 경우, `App` 컴포넌트 이하에서 프리렌더링을 비활성화하도록 Next.js를 구성할 수 있습니다.
```
    const App = dynamic(() => import('../../App'), { ssr: false })
```

이제 엔트리포인트 페이지를 새 컴포넌트를 사용하도록 업데이트하세요.

app/[[...slug]]/page.tsx

JavaScriptTypeScript
```
    import '../../index.css'
    import { ClientOnly } from './client'

    export function generateStaticParams() {
      return [{ slug: [''] }]
    }

    export default function Page() {
      return <ClientOnly />
    }
```

### Step 6: Update Static Image Imports[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-6-update-static-image-imports)

Next.js는 Vite와 약간 다르게 정적 이미지 import를 처리합니다. Vite에서는 이미지 파일을 import하면 공개 URL을 문자열로 반환합니다.

App.tsx
```
    import image from './img.png' // `image` will be '/assets/img.2d8efhg.png' in production

    export default function App() {
      return <img src={image} />
    }
```

Next.js에서는 정적 이미지 import가 객체를 반환합니다. 이 객체는 Next.js [`<Image>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/image)와 바로 사용할 수 있고, 기존 `<img>` 태그에 객체의 `src` 속성을 전달할 수도 있습니다.

`<Image>` 컴포넌트에는 [자동 이미지 최적화](https://nextjs.org/docs/app/api-reference/components/image)의 장점이 있습니다. `<Image>`는 이미지의 크기를 기준으로 결과 `<img>`의 `width`와 `height` 속성을 자동으로 설정합니다. 이는 이미지가 로드될 때 레이아웃 시프트를 방지합니다. 그러나 앱에 하나의 차원만 스타일링되고 다른 차원이 `auto`로 스타일링되지 않은 이미지가 있는 경우 문제가 발생할 수 있습니다. `auto`로 스타일링되지 않으면 해당 차원은 `<img>` 차원 속성 값으로 기본 설정되어 이미지가 찌그러져 보일 수 있습니다.

`<img>` 태그를 유지하면 애플리케이션의 변경량을 줄이고 위 문제를 방지할 수 있습니다. 이후 [로더 구성](https://nextjs.org/docs/app/api-reference/components/image#loader)이나 자동 이미지 최적화를 제공하는 기본 Next.js 서버로 이전해 `<Image>` 컴포넌트로 이미지를 최적화하도록 선택적으로 마이그레이션할 수 있습니다.

  1. **`/public`에서 import한 이미지의 절대 import 경로를 상대 import로 변환하세요.**

```
    // Before
    import logo from '/logo.png'

    // After
    import logo from '../public/logo.png'
```

  2. **전체 이미지 객체 대신 이미지의 `src` 속성을 `<img>` 태그에 전달하세요.**

```
    // Before
    <img src={logo} />

    // After
    <img src={logo.src} />
```

또는 파일 이름을 기준으로 이미지 자산의 공개 URL을 참조할 수도 있습니다. 예를 들어 `public/logo.png`는 애플리케이션에서 `/logo.png`로 이미지를 제공하므로 해당 값을 `src`로 사용할 수 있습니다.

> **경고:** TypeScript를 사용하는 경우 `src` 속성에 접근할 때 타입 오류가 발생할 수 있습니다. 지금은 무시해도 괜찮으며, 이 가이드 끝에서 해결됩니다.

### Step 7: Migrate the Environment Variables[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-7-migrate-the-environment-variables)

Next.js는 Vite와 유사하게 `.env` [환경 변수](https://nextjs.org/docs/app/guides/environment-variables)를 지원합니다. 주요 차이는 클라이언트 측에 환경 변수를 노출하는 접두사입니다.

  * `VITE_` 접두사가 있는 모든 환경 변수를 `NEXT_PUBLIC_`로 바꾸세요.

Vite는 Next.js에서 지원하지 않는 몇 가지 내장 환경 변수를 특수 객체 `import.meta.env`에 노출합니다. 사용 방법을 다음과 같이 업데이트해야 합니다.

  * `import.meta.env.MODE` ⇒ `process.env.NODE_ENV`
  * `import.meta.env.PROD` ⇒ `process.env.NODE_ENV === 'production'`
  * `import.meta.env.DEV` ⇒ `process.env.NODE_ENV !== 'production'`
  * `import.meta.env.SSR` ⇒ `typeof window !== 'undefined'`

Next.js는 내장 `BASE_URL` 환경 변수를 제공하지 않습니다. 하지만 필요하다면 여전히 설정할 수 있습니다.

  1. **`.env` 파일에 다음을 추가하세요.**

.env
```
    # ...
    NEXT_PUBLIC_BASE_PATH="/some-base-path"
```

  2. **`next.config.mjs` 파일에서 [`basePath`](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)를 `process.env.NEXT_PUBLIC_BASE_PATH`로 설정하세요.**

next.config.mjs
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      output: 'export', // Outputs a Single-Page Application (SPA).
      distDir: './dist', // Changes the build output directory to `./dist/`.
      basePath: process.env.NEXT_PUBLIC_BASE_PATH, // Sets the base path to `/some-base-path`.
    }

    export default nextConfig
```

  3. **`import.meta.env.BASE_URL` 사용을 `process.env.NEXT_PUBLIC_BASE_PATH`로 업데이트하세요.**

### Step 8: Update Scripts in `package.json`[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-8-update-scripts-in-packagejson)

이제 애플리케이션을 실행해 Next.js로 성공적으로 마이그레이션했는지 테스트할 수 있습니다. 그 전에 `package.json`의 `scripts`를 Next.js 관련 명령으로 업데이트하고, `.gitignore`에 `.next`와 `next-env.d.ts`를 추가하세요.

package.json
```
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start"
      }
    }
```

.gitignore
```
    # ...
    .next
    next-env.d.ts
    dist
```

이제 `npm run dev`를 실행하고 [`http://localhost:3000`](http://localhost:3000)을 열어 보세요. Next.js에서 실행 중인 애플리케이션을 확인할 수 있습니다.

> **예시:** Vite 애플리케이션을 Next.js로 마이그레이션한 작동 예시는 [이 풀 리퀘스트](https://github.com/inngest/vite-to-nextjs/pull/1)를 참고하세요.

### Step 9: Clean Up[](https://nextjs.org/docs/pages/guides/migrating/from-vite#step-9-clean-up)

이제 코드베이스에서 Vite 관련 아티팩트를 정리할 수 있습니다.

  * `main.tsx` 삭제
  * `index.html` 삭제
  * `vite-env.d.ts` 삭제
  * `tsconfig.node.json` 삭제
  * `vite.config.ts` 삭제
  * Vite 의존성 제거

## Next Steps[](https://nextjs.org/docs/pages/guides/migrating/from-vite#next-steps)

모든 것이 계획대로 진행되었다면 이제 단일 페이지 애플리케이션으로 실행되는 Next.js 애플리케이션을 갖게 됩니다. 아직 Next.js의 대부분 이점을 활용하고 있지는 않지만, 이제 점진적으로 변경해 모든 이점을 누릴 수 있습니다. 다음과 같은 작업을 고려해 보세요.

  * [Next.js App Router](https://nextjs.org/docs/app)로 React Router를 마이그레이션하여 다음을 얻기:
    * 자동 코드 분할
    * [스트리밍 서버 렌더링](https://nextjs.org/docs/app/api-reference/file-conventions/loading)
    * [React 서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)
  * [`<Image>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/image)로 이미지 최적화
  * [`next/font`](https://nextjs.org/docs/app/api-reference/components/font)로 폰트 최적화
  * [`<Script>` 컴포넌트](https://nextjs.org/docs/app/guides/scripts)로 서드파티 스크립트 최적화
  * [Next.js 규칙을 지원하도록 ESLint 구성 업데이트](https://nextjs.org/docs/app/api-reference/config/eslint)

Send