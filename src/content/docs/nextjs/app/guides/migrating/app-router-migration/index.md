---
title: '마이그레이션: App Router'
description: '마지막 업데이트 2026년 2월 20일'
---

# 마이그레이션: App Router | Next.js

출처 URL: https://nextjs.org/docs/app/guides/migrating/app-router-migration

[Guides](https://nextjs.org/docs/app/guides)[Migrating](https://nextjs.org/docs/app/guides/migrating)App Router

페이지 복사

# Pages에서 App Router로 마이그레이션하는 방법

마지막 업데이트 2026년 2월 20일

이 가이드를 통해 다음을 수행할 수 있습니다:

  * [Next.js 애플리케이션을 12버전에서 13버전으로 업데이트하기](https://nextjs.org/docs/app/guides/migrating/app-router-migration#nextjs-version)
  * [`pages`와 `app` 디렉터리 모두에서 동작하는 기능 업그레이드](https://nextjs.org/docs/app/guides/migrating/app-router-migration#upgrading-new-features)
  * 기존 애플리케이션을 `pages`에서 `app`으로 점진적으로 마이그레이션하기](https://nextjs.org/docs/app/guides/migrating/app-router-migration#migrating-from-pages-to-app)



## 업그레이드[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#upgrading)

### Node.js 버전[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#nodejs-version)

최소 Node.js 버전은 이제 **v18.17**입니다. 자세한 내용은 [Node.js 문서](https://nodejs.org/docs/latest-v18.x/api/)를 참고하세요.

### Next.js 버전[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#nextjs-version)

Next.js 13버전으로 업데이트하려면 선호하는 패키지 매니저로 다음 명령을 실행하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm add next@latest react@latest react-dom@latest
[/code]

### ESLint 버전[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#eslint-version)

ESLint를 사용 중이라면 ESLint 버전을 업그레이드해야 합니다:

pnpmnpmyarnbun

터미널
[code]
    pnpm add -D eslint-config-next@latest
[/code]

> **알아두면 좋아요** : ESLint 변경 사항을 적용하려면 VS Code의 ESLint 서버를 재시작해야 할 수 있습니다. 명령 팔레트(`cmd+shift+p` on Mac; `ctrl+shift+p` on Windows)를 열어 `ESLint: Restart ESLint Server`를 검색하세요.

## 다음 단계[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#next-steps)

업데이트를 마친 후 다음 섹션에서 후속 단계를 확인하세요:

  * [새 기능 업그레이드](https://nextjs.org/docs/app/guides/migrating/app-router-migration#upgrading-new-features): 개선된 Image 및 Link 컴포넌트 등 새 기능으로 업그레이드하는 방법을 안내합니다.
  * [`pages` 디렉터리에서 `app` 디렉터리로 마이그레이션](https://nextjs.org/docs/app/guides/migrating/app-router-migration#migrating-from-pages-to-app): `pages`에서 `app`으로 점진적으로 마이그레이션하는 단계별 가이드입니다.



## 새 기능 업그레이드[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#upgrading-new-features)

Next.js 13은 새로운 기능과 컨벤션을 갖춘 [App Router](https://nextjs.org/docs/app)를 도입했습니다. 새 Router는 `app` 디렉터리에서 사용할 수 있으며 `pages` 디렉터리와 공존합니다.

Next.js 13으로 업그레이드한다고 해서 반드시 App Router를 사용해야 하는 것은 아닙니다. 업데이트된 [Image 컴포넌트](https://nextjs.org/docs/app/guides/migrating/app-router-migration#image-component), [Link 컴포넌트](https://nextjs.org/docs/app/guides/migrating/app-router-migration#link-component), [Script 컴포넌트](https://nextjs.org/docs/app/guides/migrating/app-router-migration#script-component), [Font 최적화](https://nextjs.org/docs/app/guides/migrating/app-router-migration#font-optimization) 등 양쪽 디렉터리에서 작동하는 새 기능과 함께 `pages`를 계속 사용할 수 있습니다.

### `<Image/>` 컴포넌트[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#image-component)

Next.js 12에서는 임시 임포트 `next/future/image`를 통해 Image 컴포넌트의 개선 사항을 도입했습니다. 여기에는 클라이언트 측 JavaScript 감소, 이미지를 확장/스타일링하는 더 간단한 방법, 더 나은 접근성, 기본 브라우저 지연 로딩이 포함됩니다.

13버전에서는 이 새로운 동작이 `next/image`의 기본값이 되었습니다.

새 Image 컴포넌트로 마이그레이션을 돕는 두 가지 코드모드가 있습니다:

  * [**`next-image-to-legacy-image` 코드모드**](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-to-legacy-image): `next/image` 임포트를 `next/legacy/image`로 안전하게 자동 변경하여 기존 컴포넌트의 동작을 유지합니다.
  * [**`next-image-experimental` 코드모드**](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-experimental): 인라인 스타일을 위험하게 추가하고 사용되지 않는 props를 제거합니다. 기존 컴포넌트의 동작을 새로운 기본값에 맞게 변경합니다. 이 코드모드를 사용하려면 먼저 `next-image-to-legacy-image` 코드모드를 실행해야 합니다.



### `<Link>` 컴포넌트[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#link-component)

[`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)는 더 이상 자식으로 `<a>` 태그를 수동으로 추가할 필요가 없습니다. 이 동작은 [12.2버전](https://nextjs.org/blog/next-12-2)에서 실험 옵션으로 추가되었으며 이제 기본 동작입니다. Next.js 13에서 `<Link>`는 항상 `<a>`를 렌더링하며, 기본 태그로 props를 전달할 수 있습니다.

예시:
[code] 
    import Link from 'next/link'
     
    // Next.js 12: `<a>`가 중첩되지 않으면 제외됩니다.
    <Link href="/about">
      <a>About</a>
    </Link>
     
    // Next.js 13: `<Link>`는 내부적으로 항상 `<a>`를 렌더링합니다.
    <Link href="/about">
      About
    </Link>
[/code]

링크를 Next.js 13 방식으로 업그레이드하려면 [`new-link` 코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#new-link)를 사용할 수 있습니다.

### `<Script>` 컴포넌트[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#script-component)

[`next/script`](https://nextjs.org/docs/app/api-reference/components/script)의 동작이 `pages`와 `app` 모두를 지원하도록 업데이트되었지만 원활한 마이그레이션을 위해 몇 가지 변경이 필요합니다:

  * 이전에 `_document.js`에 포함했던 `beforeInteractive` 스크립트를 루트 레이아웃 파일(`app/layout.tsx`)로 이동하세요.
  * 실험적 `worker` 전략은 아직 `app`에서 작동하지 않으므로 이 전략을 사용한 스크립트는 제거하거나 다른 전략(예: `lazyOnload`)으로 수정해야 합니다.
  * `onLoad`, `onReady`, `onError` 핸들러는 Server 컴포넌트에서 동작하지 않으므로 [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)로 이동하거나 제거해야 합니다.



### 폰트 최적화[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#font-optimization)

이전에는 Next.js가 [폰트 CSS 인라인](https://nextjs.org/docs/app/api-reference/components/font)을 통해 폰트를 최적화했습니다. 13버전은 [`next/font`](https://nextjs.org/docs/app/api-reference/components/font) 모듈을 도입하여 뛰어난 성능과 개인정보 보호를 지키면서 폰트 로딩 경험을 커스터마이징할 수 있게 합니다. `next/font`는 `pages`와 `app` 디렉터리 모두에서 지원됩니다.

[CSS 인라인](https://nextjs.org/docs/app/api-reference/components/font)은 `pages`에서 계속 동작하지만 `app`에서는 동작하지 않습니다. 대신 [`next/font`](https://nextjs.org/docs/app/api-reference/components/font)를 사용해야 합니다.

`next/font` 사용 방법은 [Font Optimization](https://nextjs.org/docs/app/api-reference/components/font) 페이지에서 확인하세요.

## `pages`에서 `app`으로 마이그레이션[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#migrating-from-pages-to-app)

> **🎥 시청:** App Router를 점진적으로 도입하는 방법 → [YouTube (16 minutes)](https://www.youtube.com/watch?v=YQMSietiFm0).

App Router로 이동하는 것은 Server Components, Suspense 등 Next.js가 기반으로 하는 React 기능을 처음 사용하는 경험이 될 수 있습니다. [스페셜 파일](https://nextjs.org/docs/app/api-reference/file-conventions), [레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout) 같은 새 Next.js 기능과 결합되면 마이그레이션은 새로운 개념, 사고 모델, 동작 변화 학습이 필요합니다.

이 업데이트에 따른 복합 복잡도를 줄이기 위해 마이그레이션을 작은 단계로 나누기를 권장합니다. `app` 디렉터리는 의도적으로 `pages` 디렉터리와 동시에 작동하도록 설계되어 페이지 단위의 점진적 마이그레이션이 가능합니다.

  * `app` 디렉터리는 중첩 라우트와 레이아웃을 지원합니다. [자세히 알아보기](https://nextjs.org/docs/app/getting-started/layouts-and-pages).
  * 중첩 폴더를 사용하여 라우트를 정의하고 `page.js` 특별 파일을 통해 라우트 세그먼트를 공개합니다. [자세히 알아보기](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-4-migrating-pages).
  * 각 라우트 세그먼트의 UI는 [특별 파일 컨벤션](https://nextjs.org/docs/app/api-reference/file-conventions)을 사용해 생성합니다. 가장 일반적인 특별 파일은 `page.js`와 `layout.js`입니다.
    * `page.js`는 라우트에 고유한 UI를 정의합니다.
    * `layout.js`는 여러 라우트에서 공유되는 UI를 정의합니다.
    * 특별 파일에는 `.js`, `.jsx`, `.tsx` 확장자를 사용할 수 있습니다.
  * 컴포넌트, 스타일, 테스트 등 다른 파일을 `app` 디렉터리 안에 함께 배치할 수 있습니다. [자세히 알아보기](https://nextjs.org/docs/app).
  * `getServerSideProps`, `getStaticProps` 같은 데이터 패칭 함수는 `app` 내부의 [새 API](https://nextjs.org/docs/app/getting-started/fetching-data)로 대체되었습니다. `getStaticPaths`는 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)로 대체되었습니다.
  * `pages/_app.js`와 `pages/_document.js`는 단일 `app/layout.js` 루트 레이아웃으로 대체됩니다. [자세히 알아보기](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout).
  * `pages/_error.js`는 더 세분화된 `error.js` 특별 파일로 대체되었습니다. [자세히 알아보기](https://nextjs.org/docs/app/getting-started/error-handling).
  * `pages/404.js`는 [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) 파일로 대체되었습니다.
  * `pages/api/*` API 라우트는 [`route.js`](https://nextjs.org/docs/app/api-reference/file-conventions/route) (Route Handler) 특별 파일로 대체되었습니다.



### 1단계: `app` 디렉터리 생성[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-1-creating-the-app-directory)

최신 Next.js 버전으로 업데이트하세요(13.4 이상 필요):

pnpmnpmyarnbun

터미널
[code]
    pnpm add next@latest
[/code]

그런 다음 프로젝트 루트(또는 `src/` 디렉터리)에 새로운 `app` 디렉터리를 만드세요.

### 2단계: 루트 레이아웃 생성[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-2-creating-a-root-layout)

`app` 디렉터리 안에 새 `app/layout.tsx` 파일을 만드세요. 이는 `app` 내부 모든 라우트에 적용되는 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)입니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    export default function RootLayout({
      // Layouts must accept a children prop.
      // This will be populated with nested layouts or pages
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>{children}</body>
        </html>
      )
    }
[/code]

  * `app` 디렉터리는 반드시 루트 레이아웃을 포함해야 합니다.
  * Next.js가 `<html>`, `<body>` 태그를 자동으로 생성하지 않으므로 루트 레이아웃에서 정의해야 합니다.
  * 루트 레이아웃은 `pages/_app.tsx`와 `pages/_document.tsx` 파일을 대체합니다.
  * 레이아웃 파일에는 `.js`, `.jsx`, `.tsx` 확장자를 사용할 수 있습니다.



`<head>` HTML 요소를 관리하려면 [내장 SEO 지원](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)을 사용할 수 있습니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: 'Home',
      description: 'Welcome to Next.js',
    }
[/code]

#### `_document.js` 및 `_app.js` 마이그레이션[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#migrating-_documentjs-and-_appjs)

기존 `_app` 또는 `_document` 파일이 있다면, 그 내용(예: 전역 스타일)을 루트 레이아웃(`app/layout.tsx`)으로 복사할 수 있습니다. `app/layout.tsx`의 스타일은 `pages/*`에 적용되지 않습니다. `pages/*` 라우트가 깨지는 것을 방지하려면 마이그레이션 중에는 `_app`/`_document`를 유지해야 합니다. 완전히 마이그레이션한 후에야 안전하게 삭제할 수 있습니다.

React Context 공급자를 사용 중이라면, 이를 [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)로 옮겨야 합니다.

#### `getLayout()` 패턴을 레이아웃으로 마이그레이션(선택 사항)[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#migrating-the-getlayout-pattern-to-layouts-optional)

Next.js는 `pages` 디렉터리에서 페이지별 레이아웃을 구현하기 위해 [Page 컴포넌트에 프로퍼티를 추가](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)하는 방식을 권장했습니다. 이 패턴은 `app` 디렉터리의 [중첩 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout)에 대한 기본 지원으로 대체할 수 있습니다.

전/후 예시를 확인하세요.

**이전**

components/DashboardLayout.js
[code]
    export default function DashboardLayout({ children }) {
      return (
        <div>
          <h2>My Dashboard</h2>
          {children}
        </div>
      )
    }
[/code]

pages/dashboard/index.js
[code]
    import DashboardLayout from '../components/DashboardLayout'
     
    export default function Page() {
      return <p>My Page</p>
    }
     
    Page.getLayout = function getLayout(page) {
      return <DashboardLayout>{page}</DashboardLayout>
    }
[/code]

**이후**

  * `pages/dashboard/index.js`에서 `Page.getLayout` 속성을 제거하고, `pages`를 `app` 디렉터리로 [마이그레이션하는 단계](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-4-migrating-pages)를 따르세요.

app/dashboard/page.js
[code]export default function Page() {
          return <p>My Page</p>
        }
[/code]

  * `DashboardLayout`의 내용을 새 [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)로 옮겨 `pages` 디렉터리와 동일한 동작을 유지하세요.

app/dashboard/DashboardLayout.js
[code]'use client' // this directive should be at top of the file, before any imports.
         
        // This is a Client Component
        export default function DashboardLayout({ children }) {
          return (
            <div>
              <h2>My Dashboard</h2>
              {children}
            </div>
          )
        }
[/code]

  * `DashboardLayout`을 `app` 디렉터리 내부의 새 `layout.js` 파일로 가져오세요.

app/dashboard/layout.js
[code]import DashboardLayout from './DashboardLayout'
         
        // This is a Server Component
        export default function Layout({ children }) {
          return <DashboardLayout>{children}</DashboardLayout>
        }
[/code]

  * 클라이언트로 전송되는 컴포넌트 JavaScript 양을 줄이기 위해, `DashboardLayout.js`(Client Component)의 비대화형 부분을 점진적으로 `layout.js`(Server Component)로 옮길 수 있습니다.




### 3단계: `next/head` 마이그레이션[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-3-migrating-nexthead)

`pages` 디렉터리에서는 `next/head` React 컴포넌트를 사용해 `title`, `meta` 같은 `<head>` HTML 요소를 관리했습니다. `app` 디렉터리에서는 `next/head`가 새로운 [내장 SEO 지원](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)으로 대체됩니다.

**이전:**

pages/index.tsx

JavaScriptTypeScript
[code]
    import Head from 'next/head'
     
    export default function Page() {
      return (
        <>
          <Head>
            <title>My page title</title>
          </Head>
        </>
      )
    }
[/code]

**이후:**

app/page.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: 'My Page Title',
    }
     
    export default function Page() {
      return '...'
    }
[/code]

[모든 메타데이터 옵션 보기](https://nextjs.org/docs/app/api-reference/functions/generate-metadata).

### 4단계: 페이지 마이그레이션[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-4-migrating-pages)

  * [`app` 디렉터리](https://nextjs.org/docs/app)의 페이지는 기본적으로 [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)입니다. 이는 페이지가 [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)인 `pages` 디렉터리와 다릅니다.
  * `app`에서는 [데이터 패칭](https://nextjs.org/docs/app/getting-started/fetching-data) 방식이 변경되었습니다. `getServerSideProps`, `getStaticProps`, `getInitialProps`가 더 간결한 API로 대체되었습니다.
  * `app` 디렉터리는 중첩 폴더로 라우트를 정의하고, 공개 라우트 세그먼트를 만들기 위해 특수한 `page.js` 파일을 사용합니다.
  * `pages` 디렉터리| `app` 디렉터리| 라우트  
---|---|---  
`index.js`| `page.js`| `/`  
`about.js`| `about/page.js`| `/about`  
`blog/[slug].js`| `blog/[slug]/page.js`| `/blog/post-1`  



페이지 마이그레이션을 두 가지 주요 단계로 나누는 것을 권장합니다.

  * 1단계: 기본으로 export되는 Page Component를 새로운 Client Component로 옮깁니다.
  * 2단계: 새 Client Component를 `app` 디렉터리의 새로운 `page.js` 파일로 가져옵니다.



> **알아두면 좋아요**: 이 경로가 `pages` 디렉터리와 가장 유사한 동작을 제공하므로 마이그레이션이 가장 쉽습니다.

**1단계: 새 Client Component 만들기**

  * `app` 디렉터리 안에(`app/home-page.tsx` 등) Client Component를 export하는 별도 파일을 만듭니다. Client Component를 정의하려면 파일 최상단(모든 import 이전)에 `'use client'` 지시문을 추가하세요.
    * Pages Router와 마찬가지로, 초기 페이지 로드 시 Client Component를 정적 HTML로 사전 렌더링하는 [최적화 단계](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-client-first-load)가 있습니다.
  * `pages/index.js`에서 기본 export 페이지 컴포넌트를 `app/home-page.tsx`로 옮깁니다.



app/home-page.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    // This is a Client Component (same as components in the `pages` directory)
    // It receives data as props, has access to state and effects, and is
    // prerendered on the server during the initial page load.
    export default function HomePage({ recentPosts }) {
      return (
        <div>
          {recentPosts.map((post) => (
            <div key={post.id}>{post.title}</div>
          ))}
        </div>
      )
    }
[/code]

**2단계: 새 페이지 만들기**

  * `app` 디렉터리 안에 새 `app/page.tsx` 파일을 만듭니다. 이는 기본적으로 Server Component입니다.

  * `home-page.tsx` Client Component를 페이지에 import합니다.

  * `pages/index.js`에서 데이터를 가져왔다면, 새로운 [데이터 패칭 API](https://nextjs.org/docs/app/getting-started/fetching-data)를 사용해 서버 컴포넌트로 직접 데이터 패칭 로직을 옮기세요. 자세한 내용은 [데이터 패칭 업그레이드 가이드](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-6-migrating-data-fetching-methods)를 참고하세요.

app/page.tsx

JavaScriptTypeScript
[code]// Import your Client Component
        import HomePage from './home-page'
         
        async function getPosts() {
          const res = await fetch('https://...')
          const posts = await res.json()
          return posts
        }
         
        export default async function Page() {
          // Fetch data directly in a Server Component
          const recentPosts = await getPosts()
          // Forward fetched data to your Client Component
          return <HomePage recentPosts={recentPosts} />
        }
[/code]

  * 이전 페이지에서 `useRouter`를 사용했다면, 새로운 라우팅 훅으로 업데이트해야 합니다. [더 알아보기](https://nextjs.org/docs/app/api-reference/functions/use-router).

  * 개발 서버를 시작하고 [`http://localhost:3000`](http://localhost:3000)에 접속하세요. 기존 인덱스 라우트가 이제 app 디렉터리를 통해 제공되는 것을 확인할 수 있습니다.




### 5단계: 라우팅 훅 마이그레이션[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-5-migrating-routing-hooks)

`app` 디렉터리의 새로운 동작을 지원하기 위해 새로운 라우터가 추가되었습니다.

`app`에서는 `next/navigation`에서 import하는 세 가지 훅, 즉 [`useRouter()`](https://nextjs.org/docs/app/api-reference/functions/use-router), [`usePathname()`](https://nextjs.org/docs/app/api-reference/functions/use-pathname), [`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)를 사용해야 합니다.

  * 새로운 `useRouter` 훅은 `next/navigation`에서 import되며, `next/router`에서 import하는 `pages`용 `useRouter`와는 동작이 다릅니다.
    * [`next/router`에서 import하는 `useRouter` 훅](https://nextjs.org/docs/pages/api-reference/functions/use-router)은 `app` 디렉터리에서 지원되지 않지만 `pages` 디렉터리에서는 계속 사용할 수 있습니다.
  * 새로운 `useRouter`는 `pathname` 문자열을 반환하지 않습니다. 대신 별도의 `usePathname` 훅을 사용하세요.
  * 새로운 `useRouter`는 `query` 객체를 반환하지 않습니다. 검색 매개변수와 동적 라우트 매개변수가 분리되었으므로 `useSearchParams`와 `useParams` 훅을 사용하세요.
  * 페이지 변경 사항을 수신하려면 `useSearchParams`와 `usePathname`을 함께 사용할 수 있습니다. 자세한 내용은 [Router Events](https://nextjs.org/docs/app/api-reference/functions/use-router#router-events) 섹션을 참고하세요.
  * 이러한 새로운 훅은 Client Component에서만 지원됩니다. Server Component에서는 사용할 수 없습니다.



app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useRouter, usePathname, useSearchParams } from 'next/navigation'
     
    export default function ExampleClientComponent() {
      const router = useRouter()
      const pathname = usePathname()
      const searchParams = useSearchParams()
     
      // ...
    }
[/code]

또한 새로운 `useRouter` 훅에는 다음과 같은 변경 사항이 있습니다.

  * `fallback`이 [대체](https://nextjs.org/docs/app/guides/migrating/app-router-migration#replacing-fallback)되었기 때문에 `isFallback`이 제거되었습니다.
  * `locale`, `locales`, `defaultLocales`, `domainLocales` 값은 `app` 디렉터리에서 더 이상 내장 i18n Next.js 기능이 필요하지 않으므로 제거되었습니다. [i18n에 대해 더 알아보기](https://nextjs.org/docs/app/guides/internationalization).
  * `basePath`가 제거되었습니다. 대체 기능은 `useRouter`의 일부가 아니며 아직 구현되지 않았습니다.
  * `as` 개념이 새로운 라우터에서 제거되었으므로 `asPath`도 사라졌습니다.
  * 더 이상 필요하지 않아 `isReady`가 제거되었습니다. [정적 렌더링](https://nextjs.org/docs/app/guides/caching#static-rendering) 중에 [`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) 훅을 사용하는 컴포넌트는 프리렌더링 단계를 건너뛰고 런타임에 클라이언트에서 렌더링됩니다.
  * `route`가 제거되었습니다. 대안으로 `usePathname` 또는 `useSelectedLayoutSegments()`를 사용하세요.



[`useRouter()` API 레퍼런스 보기](https://nextjs.org/docs/app/api-reference/functions/use-router).

#### `pages`와 `app` 간 컴포넌트 공유[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#sharing-components-between-pages-and-app)

컴포넌트를 `pages` 라우터와 `app` 라우터 사이에서 호환되게 유지하려면 [`next/compat/router`의 `useRouter` 훅](https://nextjs.org/docs/pages/api-reference/functions/use-router#the-nextcompatrouter-export)을 참고하세요. 이는 `pages` 디렉터리의 `useRouter` 훅이지만 라우터 간에 컴포넌트를 공유할 때 사용하도록 만들어졌습니다. `app` 라우터에서만 사용할 준비가 되면 [`next/navigation`의 새로운 `useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router)로 업데이트하세요.

### 6단계: 데이터 패칭 방식 마이그레이션[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-6-migrating-data-fetching-methods)

`pages` 디렉터리는 페이지용 데이터를 가져오기 위해 `getServerSideProps`와 `getStaticProps`를 사용합니다. `app` 디렉터리에서는 이러한 이전 데이터 패칭 함수가 `fetch()`와 `async` React 서버 컴포넌트를 기반으로 하는 [더 간단한 API](https://nextjs.org/docs/app/getting-started/fetching-data)로 대체됩니다.

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      // This request should be cached until manually invalidated.
      // Similar to `getStaticProps`.
      // `force-cache` is the default and can be omitted.
      const staticData = await fetch(`https://...`, { cache: 'force-cache' })
     
      // This request should be refetched on every request.
      // Similar to `getServerSideProps`.
      const dynamicData = await fetch(`https://...`, { cache: 'no-store' })
     
      // This request should be cached with a lifetime of 10 seconds.
      // Similar to `getStaticProps` with the `revalidate` option.
      const revalidatedData = await fetch(`https://...`, {
        next: { revalidate: 10 },
      })
     
      return <div>...</div>
    }
[/code]

#### 서버 사이드 렌더링(`getServerSideProps`)[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#server-side-rendering-getserversideprops)

`pages` 디렉터리에서는 `getServerSideProps`를 사용해 서버에서 데이터를 가져온 뒤 해당 파일의 기본 내보낸 React 컴포넌트로 props를 전달합니다. 페이지의 초기 HTML은 서버에서 프리렌더링되고, 이후 브라우저에서 페이지를 “하이드레이션”하여 인터랙티브하게 만듭니다.

pages/dashboard.js
[code]
    // `pages` directory
     
    export async function getServerSideProps() {
      const res = await fetch(`https://...`)
      const projects = await res.json()
     
      return { props: { projects } }
    }
     
    export default function Dashboard({ projects }) {
      return (
        <ul>
          {projects.map((project) => (
            <li key={project.id}>{project.name}</li>
          ))}
        </ul>
      )
    }
[/code]

App Router에서는 [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)를 활용해 React 컴포넌트 내부에 데이터 패칭을 공존시킬 수 있습니다. 이렇게 하면 서버에서 렌더링된 HTML은 유지하면서 클라이언트로 전송되는 JavaScript 양을 줄일 수 있습니다.

`cache` 옵션을 `no-store`로 설정하면 가져온 데이터를 [캐시하지 않아야 함](https://nextjs.org/docs/app/getting-started/fetching-data)을 나타낼 수 있습니다. 이는 `pages` 디렉터리의 `getServerSideProps`와 동일한 동작입니다.

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    // `app` directory
     
    // This function can be named anything
    async function getProjects() {
      const res = await fetch(`https://...`, { cache: 'no-store' })
      const projects = await res.json()
     
      return projects
    }
     
    export default async function Dashboard() {
      const projects = await getProjects()
     
      return (
        <ul>
          {projects.map((project) => (
            <li key={project.id}>{project.name}</li>
          ))}
        </ul>
      )
    }
[/code]

#### 요청 객체에 접근하기[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#accessing-request-object)

`pages` 디렉터리에서는 Node.js HTTP API를 기반으로 요청 정보를 가져올 수 있습니다.

예를 들어 `getServerSideProps`에서 `req` 객체를 받아 요청의 쿠키와 헤더를 조회할 수 있습니다.

pages/index.js
[code]
    // `pages` directory
     
    export async function getServerSideProps({ req, query }) {
      const authHeader = req.getHeaders()['authorization'];
      const theme = req.cookies['theme'];
     
      return { props: { ... }}
    }
     
    export default function Page(props) {
      return ...
    }
[/code]

`app` 디렉터리는 요청 데이터를 읽어오기 위한 새로운 읽기 전용 함수를 제공합니다:

  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers): Web Headers API 기반이며, [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 내부에서 요청 헤더를 가져올 때 사용할 수 있습니다.
  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies): Web Cookies API 기반이며, [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 내부에서 쿠키를 가져올 때 사용할 수 있습니다.



app/page.tsx

JavaScriptTypeScript
[code]
    // `app` directory
    import { cookies, headers } from 'next/headers'
     
    async function getData() {
      const authHeader = (await headers()).get('authorization')
     
      return '...'
    }
     
    export default async function Page() {
      // You can use `cookies` or `headers` inside Server Components
      // directly or in your data fetching function
      const theme = (await cookies()).get('theme')
      const data = await getData()
      return '...'
    }
[/code]

#### 정적 사이트 생성(`getStaticProps`)[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#static-site-generation-getstaticprops)

`pages` 디렉터리에서는 `getStaticProps` 함수가 빌드 타임에 페이지를 프리렌더링하는 데 사용됩니다. 이 함수는 외부 API나 데이터베이스에서 데이터를 가져와 빌드 중에 전체 페이지로 전달할 수 있습니다.

pages/index.js
[code]
    // `pages` directory
     
    export async function getStaticProps() {
      const res = await fetch(`https://...`)
      const projects = await res.json()
     
      return { props: { projects } }
    }
     
    export default function Index({ projects }) {
      return projects.map((project) => <div>{project.name}</div>)
    }
[/code]

`app` 디렉터리에서는 [`fetch()`](https://nextjs.org/docs/app/api-reference/functions/fetch)를 사용한 데이터 패칭이 기본적으로 `cache: 'force-cache'`로 동작하며, 수동으로 무효화할 때까지 요청 데이터를 캐시합니다. 이는 `pages` 디렉터리의 `getStaticProps`와 유사합니다.

app/page.js
[code]
    // `app` directory
     
    // This function can be named anything
    async function getProjects() {
      const res = await fetch(`https://...`)
      const projects = await res.json()
     
      return projects
    }
     
    export default async function Index() {
      const projects = await getProjects()
     
      return projects.map((project) => <div>{project.name}</div>)
    }
[/code]

#### 동적 경로(`getStaticPaths`)[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#dynamic-paths-getstaticpaths)

`pages` 디렉터리에서는 `getStaticPaths` 함수로 빌드 타임에 프리렌더링해야 할 동적 경로를 정의합니다.

pages/posts/[id].js
[code]
    // `pages` directory
    import PostLayout from '@/components/post-layout'
     
    export async function getStaticPaths() {
      return {
        paths: [{ params: { id: '1' } }, { params: { id: '2' } }],
      }
    }
     
    export async function getStaticProps({ params }) {
      const res = await fetch(`https://.../posts/${params.id}`)
      const post = await res.json()
     
      return { props: { post } }
    }
     
    export default function Post({ post }) {
      return <PostLayout post={post} />
    }
[/code]

`app` 디렉터리에서는 `getStaticPaths`가 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)로 대체됩니다.

[`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)는 `getStaticPaths`와 비슷하지만, 라우트 파라미터를 반환하는 API가 더 단순화되었으며 [레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout) 내부에서도 사용할 수 있습니다. `generateStaticParams`의 반환 형태는 중첩된 `param` 객체 배열이나 해석된 경로 문자열 대신 세그먼트 배열입니다.

app/posts/[id]/page.js
[code]
    // `app` directory
    import PostLayout from '@/components/post-layout'
     
    export async function generateStaticParams() {
      return [{ id: '1' }, { id: '2' }]
    }
     
    async function getPost(params) {
      const res = await fetch(`https://.../posts/${(await params).id}`)
      const post = await res.json()
     
      return post
    }
     
    export default async function Post({ params }) {
      const post = await getPost(params)
     
      return <PostLayout post={post} />
    }
[/code]

`app` 디렉터리의 새로운 모델에서는 `generateStaticParams`라는 이름이 `getStaticPaths`보다 더 적합합니다. `getStaticProps`와 `getServerSideProps`가 더 이상 필요하지 않기 때문에 `get` 접두사는 더 설명적인 `generate`로 대체되며, 여러 동적 세그먼트를 포함하는 중첩 라우팅에 더 알맞은 `Params` 접미사가 `Paths` 대신 사용됩니다.

* * *

#### `fallback` 대체하기[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#replacing-fallback)

`pages` 디렉터리에서는 `getStaticPaths`가 반환하는 `fallback` 속성이 빌드 타임에 프리렌더링되지 않은 페이지의 동작을 정의합니다. 페이지가 생성되는 동안 대체 페이지를 보여주려면 `true`, 404 페이지를 보여주려면 `false`, 요청 시 페이지를 생성하려면 `blocking`으로 설정할 수 있습니다.

pages/posts/[id].js
[code]
    // `pages` directory
     
    export async function getStaticPaths() {
      return {
        paths: [],
        fallback: 'blocking'
      };
    }
     
    export async function getStaticProps({ params }) {
      ...
    }
     
    export default function Post({ post }) {
      return ...
    }
[/code]

`app` 디렉터리에서는 [`config.dynamicParams` 속성](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams)이 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) 외부의 파라미터를 처리하는 방식을 제어합니다:

  * **`true`** : (기본값) `generateStaticParams`에 포함되지 않은 동적 세그먼트를 온디맨드로 생성합니다.
  * **`false`** : `generateStaticParams`에 포함되지 않은 동적 세그먼트는 404를 반환합니다.



이는 `pages` 디렉터리의 `getStaticPaths`에서 사용하던 `fallback: true | false | 'blocking'` 옵션을 대체합니다. 스트리밍 환경에서는 `'blocking'`과 `true`의 차이가 미미하므로 `dynamicParams`에는 `fallback: 'blocking'` 옵션이 포함되지 않습니다.

app/posts/[id]/page.js
[code]
    // `app` directory
     
    export const dynamicParams = true;
     
    export async function generateStaticParams() {
      return [...]
    }
     
    async function getPost(params) {
      ...
    }
     
    export default async function Post({ params }) {
      const post = await getPost(params);
     
      return ...
    }
[/code]

[`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams)를 `true`(기본값)로 설정하면 아직 생성되지 않은 라우트 세그먼트가 요청될 때 서버에서 렌더링하고 캐시합니다.

#### 점진적 정적 재생성(`revalidate`가 있는 `getStaticProps`)[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#incremental-static-regeneration-getstaticprops-with-revalidate)

`pages` 디렉터리에서는 `getStaticProps` 함수로 일정 시간이 지나면 페이지를 자동으로 다시 생성하도록 `revalidate` 필드를 추가할 수 있습니다.

pages/index.js
[code]
    // `pages` directory
     
    export async function getStaticProps() {
      const res = await fetch(`https://.../posts`)
      const posts = await res.json()
     
      return {
        props: { posts },
        revalidate: 60,
      }
    }
     
    export default function Index({ posts }) {
      return (
        <Layout>
          <PostList posts={posts} />
        </Layout>
      )
    }
[/code]

`app` 디렉터리에서는 [`fetch()`](https://nextjs.org/docs/app/api-reference/functions/fetch)로 데이터를 가져올 때 `revalidate`를 사용할 수 있으며, 지정한 초 동안 요청이 캐시됩니다.

app/page.js
[code]
    // `app` directory
     
    async function getPosts() {
      const res = await fetch(`https://.../posts`, { next: { revalidate: 60 } })
      const data = await res.json()
     
      return data.posts
    }
     
    export default async function PostList() {
      const posts = await getPosts()
     
      return posts.map((post) => <div>{post.name}</div>)
    }
[/code]

#### API 라우트[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#api-routes)

API 라우트는 `pages/api` 디렉터리에서 아무 변경 없이 계속 동작하지만, `app` 디렉터리에서는 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)로 대체되었습니다.

Route Handler를 사용하면 Web [Request](https://developer.mozilla.org/docs/Web/API/Request) 및 [Response](https://developer.mozilla.org/docs/Web/API/Response) API를 활용해 특정 라우트의 사용자 지정 요청 처리기를 만들 수 있습니다.

app/api/route.ts

JavaScriptTypeScript
[code]
    export async function GET(request: Request) {}
[/code]

> **알아 두면 좋아요** : 이전에 클라이언트에서 외부 API를 호출하기 위해 API 라우트를 사용했다면, 이제는 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)를 사용해 안전하게 데이터를 가져올 수 있습니다. [데이터 패칭](https://nextjs.org/docs/app/getting-started/fetching-data)에 대해 더 알아보세요.

#### 단일 페이지 애플리케이션[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#single-page-applications)

동시에 단일 페이지 애플리케이션(SPA)에서 Next.js로 마이그레이션 중이라면, [문서](https://nextjs.org/docs/app/guides/single-page-applications)를 참고해 자세히 알아보세요.

### 7단계: 스타일링[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-7-styling)

`pages` 디렉터리에서는 전역 스타일시트가 `pages/_app.js`에만 제한되지만, `app` 디렉터리에서는 이 제한이 해제되었습니다. 전역 스타일을 어떤 레이아웃, 페이지, 컴포넌트에도 추가할 수 있습니다.

  * [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules)
  * [Tailwind CSS](https://nextjs.org/docs/app/getting-started/css#tailwind-css)
  * [Global Styles](https://nextjs.org/docs/app/getting-started/css#global-css)
  * [CSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)
  * [External Stylesheets](https://nextjs.org/docs/app/getting-started/css#external-stylesheets)
  * [Sass](https://nextjs.org/docs/app/guides/sass)

#### Tailwind CSS[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#tailwind-css)

Tailwind CSS를 사용 중이라면 `tailwind.config.js` 파일에 `app` 디렉터리를 추가해야 합니다.

tailwind.config.js
[code]
    module.exports = {
      content: [
        './app/**/*.{js,ts,jsx,tsx,mdx}', // <-- Add this line
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
      ],
    }
[/code]

또한 전역 스타일을 `app/layout.js` 파일에 import해야 합니다.

app/layout.js
[code]
    import '../styles/globals.css'
     
    export default function RootLayout({ children }) {
      return (
        <html lang="en">
          <body>{children}</body>
        </html>
      )
    }
[/code]

[Tailwind CSS로 스타일링](https://nextjs.org/docs/app/getting-started/css#tailwind-css)에 대해 더 알아보세요.

## App Router와 Pages Router를 함께 사용하기[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#using-app-router-together-with-pages-router)

서로 다른 Next.js 라우터가 제공하는 라우트 사이를 이동할 때는 하드 내비게이션이 발생하며, `next/link`의 자동 링크 사전 패칭은 라우터 간에는 동작하지 않습니다.

대신 [App Router와 Pages Router 간 내비게이션을 최적화](https://vercel.com/guides/optimizing-hard-navigations)해 사전 패칭과 빠른 페이지 전환을 유지할 수 있습니다. [자세히 알아보기](https://vercel.com/guides/optimizing-hard-navigations).

## 코드모드[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#codemods)

Next.js는 기능이 더 이상 사용되지 않을 때 코드베이스를 업그레이드하도록 돕는 Codemod 변환을 제공합니다. 자세한 내용은 [Codemods](https://nextjs.org/docs/app/guides/upgrading/codemods)를 참고하세요.

도움이 되었나요?

지원됨.

보내기
