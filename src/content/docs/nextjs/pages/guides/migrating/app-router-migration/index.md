---
title: '마이그레이션: App Router'
description: '원본 URL: https://nextjs.org/docs/pages/guides/migrating/app-router-migration'
---

# 마이그레이션: App Router | Next.js

원본 URL: https://nextjs.org/docs/pages/guides/migrating/app-router-migration

[가이드](https://nextjs.org/docs/pages/guides)[마이그레이션](https://nextjs.org/docs/pages/guides/migrating)App Router

# Pages에서 App Router로 마이그레이션하는 방법

마지막 업데이트: 2026년 2월 20일

이 가이드는 다음을 돕습니다:

  * [Next.js 애플리케이션을 버전 12에서 13으로 업데이트](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#nextjs-version)
  * [`pages`와 `app` 디렉터리 모두에서 작동하는 기능 업그레이드](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#upgrading-new-features)
  * 기존 애플리케이션을 `pages`에서 `app`으로 점진적으로 마이그레이션](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#migrating-from-pages-to-app)

## 업그레이드[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#upgrading)

### Node.js 버전[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#nodejs-version)

최소 Node.js 버전은 이제 **v18.17**입니다. 자세한 내용은 [Node.js 문서](https://nodejs.org/docs/latest-v18.x/api/)를 참고하세요.

### Next.js 버전[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#nextjs-version)

Next.js 13 버전으로 업데이트하려면 선호하는 패키지 관리자를 사용해 다음 명령을 실행하세요:

pnpmnpmyarnbun

터미널
```
    pnpm add next@latest react@latest react-dom@latest
```

### ESLint 버전[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#eslint-version)

ESLint를 사용 중이라면 ESLint 버전을 업그레이드해야 합니다:

pnpmnpmyarnbun

터미널
```
    pnpm add -D eslint-config-next@latest
```

> **알아두면 좋아요**: VS Code에서 ESLint 변경 사항을 반영하려면 ESLint 서버를 재시작해야 할 수 있습니다. 커맨드 팔레트(`cmd+shift+p` on Mac; `ctrl+shift+p` on Windows)를 열고 `ESLint: Restart ESLint Server`를 검색하세요.

## 다음 단계[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#next-steps)

업데이트가 끝났다면 다음 섹션을 참고하세요:

  * [신규 기능 업그레이드](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#upgrading-new-features): 향상된 Image 및 Link 컴포넌트 등 새로운 기능으로 업그레이드하는 방법을 안내합니다.
  * [`pages` 디렉터리에서 `app` 디렉터리로 마이그레이션](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#migrating-from-pages-to-app): `pages`에서 `app`으로 페이지 단위로 점진적으로 옮길 수 있는 단계별 가이드입니다.

## 신규 기능 업그레이드[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#upgrading-new-features)

Next.js 13은 새로운 기능과 규칙을 갖춘 [App Router](https://nextjs.org/docs/app)를 도입했습니다. 새로운 라우터는 `app` 디렉터리에서 사용할 수 있으며 `pages` 디렉터리와 함께 공존합니다.

Next.js 13으로 업그레이드한다고 해서 App Router를 반드시 사용해야 하는 것은 아닙니다. 업데이트된 [Image 컴포넌트](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#image-component), [Link 컴포넌트](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#link-component), [Script 컴포넌트](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#script-component), [폰트 최적화](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#font-optimization)처럼 두 디렉터리에서 모두 작동하는 새로운 기능은 계속 `pages`에서 사용할 수 있습니다.

### `<Image/>` 컴포넌트[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#image-component)

Next.js 12는 임시 import인 `next/future/image`를 통해 Image 컴포넌트 개선 사항을 도입했습니다. 이 개선 사항에는 클라이언트 측 JavaScript 감소, 이미지 확장 및 스타일링을 위한 더 쉬운 방법, 접근성 향상, 브라우저 기본 지연 로딩이 포함됩니다.

13버전에서는 이 새로운 동작이 `next/image`의 기본 동작이 되었습니다.

새로운 Image 컴포넌트로 마이그레이션하는 데 도움이 되는 두 가지 코드모드가 있습니다:

  * [**`next-image-to-legacy-image` codiceod**](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-to-legacy-image): `next/image` import를 `next/legacy/image`로 안전하게 자동 이름 변경합니다. 기존 컴포넌트는 동일한 동작을 유지합니다.
  * [**`next-image-experimental` codemod**](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-experimental): 인라인 스타일을 위험하게 추가하고 사용되지 않는 props를 제거합니다. 이는 기존 컴포넌트 동작을 새로운 기본 동작과 일치하도록 변경합니다. 이 codemod를 사용하려면 먼저 `next-image-to-legacy-image` codemod를 실행해야 합니다.

### `<Link>` 컴포넌트[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#link-component)

[`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)는 더 이상 자식으로 `<a>` 태그를 수동으로 추가할 필요가 없습니다. 이 동작은 [버전 12.2](https://nextjs.org/blog/next-12-2)에서 실험 옵션으로 추가되었고 이제 기본값입니다. Next.js 13에서는 `<Link>`가 항상 `<a>`를 렌더링하며 기본 태그로 props를 전달할 수 있습니다.

예:
```
    import Link from 'next/link'

    // Next.js 12: `<a>`가 중첩되지 않으면 제외됩니다
    <Link href="/about">
      <a>About</a>
    </Link>

    // Next.js 13: `<Link>`는 내부적으로 항상 `<a>`를 렌더링합니다
    <Link href="/about">
      About
    </Link>
```

Next.js 13으로 링크를 업그레이드하려면 [`new-link` codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#new-link)를 사용할 수 있습니다.

### `<Script>` 컴포넌트[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#script-component)

[`next/script`](https://nextjs.org/docs/app/api-reference/components/script)의 동작은 `pages`와 `app` 모두를 지원하도록 업데이트되었지만 원활한 마이그레이션을 위해 몇 가지 변경이 필요합니다:

  * 이전에 `_document.js`에 포함했던 모든 `beforeInteractive` 스크립트를 루트 레이아웃 파일(`app/layout.tsx`)로 이동하세요.
  * 실험적 `worker` 전략은 아직 `app`에서 작동하지 않으므로 해당 전략을 사용하는 스크립트는 제거하거나 `lazyOnload`와 같은 다른 전략을 사용하도록 수정해야 합니다.
  * `onLoad`, `onReady`, `onError` 핸들러는 Server 컴포넌트에서 작동하지 않으므로 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)로 이동하거나 완전히 제거하세요.

### 폰트 최적화[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#font-optimization)

기존에는 Next.js가 [폰트 CSS를 인라인](https://nextjs.org/docs/app/api-reference/components/font)하여 폰트를 최적화했습니다. 13버전은 새로운 [`next/font`](https://nextjs.org/docs/app/api-reference/components/font) 모듈을 도입하여 뛰어난 성능과 프라이버시를 유지하면서 폰트 로딩 경험을 사용자 정의할 수 있게 합니다. `next/font`는 `pages`와 `app` 디렉터리에서 모두 지원됩니다.

[`pages`에서 CSS 인라인](https://nextjs.org/docs/app/api-reference/components/font)은 계속 작동하지만 `app`에서는 작동하지 않습니다. 대신 [`next/font`](https://nextjs.org/docs/app/api-reference/components/font)를 사용해야 합니다.

[`next/font`](https://nextjs.org/docs/app/api-reference/components/font)를 사용하는 방법은 [폰트 최적화](https://nextjs.org/docs/app/api-reference/components/font) 페이지에서 확인하세요.

## `pages`에서 `app`으로 마이그레이션[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#migrating-from-pages-to-app)

> **🎥 시청:** App Router를 점진적으로 도입하는 방법 알아보기 → [YouTube (16분)](https://www.youtube.com/watch?v=YQMSietiFm0).

App Router로 이동하는 과정에서 Server 컴포넌트, Suspense 등 Next.js가 기반으로 하는 React 기능을 처음 사용하게 될 수 있습니다. [특수 파일](https://nextjs.org/docs/app/api-reference/file-conventions), [레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout) 같은 새로운 Next.js 기능과 결합되면 새로운 개념, 사고 모델, 동작 변화를 학습해야 하는 마이그레이션이 됩니다.

이러한 업데이트의 복잡성을 줄이기 위해 마이그레이션을 작은 단계로 나누는 것을 권장합니다. `app` 디렉터리는 `pages` 디렉터리와 동시에 작동하도록 설계되어 페이지별 점진적 마이그레이션이 가능합니다.

  * `app` 디렉터리는 중첩 라우트와 레이아웃을 모두 지원합니다. [자세히 알아보기](https://nextjs.org/docs/app/getting-started/layouts-and-pages).
  * 중첩 폴더를 사용해 라우트를 정의하고, 특별한 `page.js` 파일로 라우트 세그먼트를 공개합니다. [자세히 알아보기](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-4-migrating-pages).
  * [특수 파일 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)은 각 라우트 세그먼트의 UI를 생성하는 데 사용됩니다. 가장 일반적인 특수 파일은 `page.js`와 `layout.js`입니다.
    * `page.js`는 라우트 고유 UI를 정의합니다.
    * `layout.js`는 여러 라우트에 공유되는 UI를 정의합니다.
    * 특수 파일에는 `.js`, `.jsx`, `.tsx` 확장자를 사용할 수 있습니다.
  * 컴포넌트, 스타일, 테스트 등 다른 파일을 `app` 디렉터리 내부에 나란히 배치할 수 있습니다. [자세히 알아보기](https://nextjs.org/docs/app).
  * `getServerSideProps`와 `getStaticProps` 같은 데이터 패칭 함수는 `app` 내부의 [새 API](https://nextjs.org/docs/app/getting-started/fetching-data)로 대체되었습니다. `getStaticPaths`는 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)로 대체되었습니다.
  * `pages/_app.js`와 `pages/_document.js`는 단일 `app/layout.js` 루트 레이아웃으로 대체되었습니다. [자세히 알아보기](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout).
  * `pages/_error.js`는 더 세분된 `error.js` 특수 파일로 대체되었습니다. [자세히 알아보기](https://nextjs.org/docs/app/getting-started/error-handling).
  * `pages/404.js`는 [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) 파일로 대체되었습니다.
  * `pages/api/*` API 라우트는 [`route.js`](https://nextjs.org/docs/app/api-reference/file-conventions/route) (Route Handler) 특수 파일로 대체되었습니다.

### 1단계: `app` 디렉터리 생성[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-1-creating-the-app-directory)

최신 Next.js 버전으로 업데이트하세요(13.4 이상 필요):

pnpmnpmyarnbun

터미널
```
    pnpm add next@latest
```

그런 다음 프로젝트 루트(또는 `src/` 디렉터리)에 새 `app` 디렉터리를 만드세요.

### 2단계: 루트 레이아웃 생성[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-2-creating-a-root-layout)

`app` 디렉터리 내부에 새 `app/layout.tsx` 파일을 만드세요. 이것은 `app` 내부 모든 라우트에 적용되는 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)입니다.

app/layout.tsx

JavaScriptTypeScript
```
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
```

  * `app` 디렉터리에는 반드시 루트 레이아웃이 포함되어야 합니다.
  * Next.js가 `<html>`, `<body>` 태그를 자동으로 생성하지 않으므로 루트 레이아웃에서 반드시 정의해야 합니다.
  * 루트 레이아웃은 `pages/_app.tsx`와 `pages/_document.tsx` 파일을 대체합니다.
  * 레이아웃 파일에는 `.js`, `.jsx`, `.tsx` 확장자를 사용할 수 있습니다.

`<head>` HTML 요소를 관리하려면 [내장 SEO 지원](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)을 사용할 수 있습니다:

app/layout.tsx

JavaScriptTypeScript
```
    import type { Metadata } from 'next'

    export const metadata: Metadata = {
      title: 'Home',
      description: 'Welcome to Next.js',
    }
```

#### `_document.js` 및 `_app.js` 마이그레이션[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#migrating-_documentjs-and-_appjs)

기존 `_app` 또는 `_document` 파일이 있다면 내용(예: 전역 스타일)을 루트 레이아웃(`app/layout.tsx`)으로 복사할 수 있습니다. `app/layout.tsx`의 스타일은 `pages/*`에는 적용되지 않습니다. `pages/*` 라우트가 깨지지 않도록 마이그레이션 중에는 `_app`/`_document`를 유지해야 합니다. 전체 마이그레이션이 완료되면 안전하게 삭제할 수 있습니다.

React Context provider를 사용 중이라면 [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)로 이동해야 합니다.

#### `getLayout()` 패턴을 레이아웃으로 마이그레이션(선택 사항)[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#migrating-the-getlayout-pattern-to-layouts-optional)

Next.js는 `pages` 디렉터리에서 페이지별 레이아웃을 구현하기 위해 [페이지 컴포넌트에 속성을 추가](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)하는 방식을 권장했습니다. 이 패턴은 `app` 디렉터리의 [중첩 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout)에 대한 기본 지원으로 대체할 수 있습니다.

이전/이후 예시를 확인하세요.

**Before**

components/DashboardLayout.js
```
    export default function DashboardLayout({ children }) {
      return (
        <div>
          <h2>My Dashboard</h2>
          {children}
        </div>
      )
    }
```

pages/dashboard/index.js
```
    import DashboardLayout from '../components/DashboardLayout'

    export default function Page() {
      return <p>My Page</p>
    }

    Page.getLayout = function getLayout(page) {
      return <DashboardLayout>{page}</DashboardLayout>
    }
```

**After**

- `pages/dashboard/index.js`에서 `Page.getLayout` 속성을 제거하고, `app` 디렉터리로 [페이지를 마이그레이션하는 단계](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-4-migrating-pages)를 따르세요.

app/dashboard/page.js
```
export default function Page() {
          return <p>My Page</p>
        }
```

- `pages` 디렉터리 동작을 유지하려면 `DashboardLayout`의 내용을 새로운 [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)로 이동하세요.

app/dashboard/DashboardLayout.js
```
'use client' // this directive should be at top of the file, before any imports.

        // This is a Client Component
        export default function DashboardLayout({ children }) {
          return (
            <div>
              <h2>My Dashboard</h2>
              {children}
            </div>
          )
        }
```

- `DashboardLayout`을 `app` 디렉터리 안의 새 `layout.js` 파일로 가져옵니다.

app/dashboard/layout.js
```
import DashboardLayout from './DashboardLayout'

        // This is a Server Component
        export default function Layout({ children }) {
          return <DashboardLayout>{children}</DashboardLayout>
        }
```

- 클라이언트로 전송되는 컴포넌트 JavaScript 양을 줄이기 위해, `DashboardLayout.js`(Client Component)의 상호작용이 없는 부분을 `layout.js`(Server Component)로 점진적으로 옮길 수 있습니다.

### Step 3: `next/head` 마이그레이션[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-3-migrating-nexthead)

`pages` 디렉터리에서는 `next/head` React 컴포넌트를 사용하여 `title`, `meta` 같은 `<head>` HTML 요소를 관리합니다. `app` 디렉터리에서는 `next/head`가 새로운 [내장 SEO 지원](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)으로 대체되었습니다.

**Before:**

pages/index.tsx

JavaScriptTypeScript
```
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
```

**After:**

app/page.tsx

JavaScriptTypeScript
```
    import type { Metadata } from 'next'

    export const metadata: Metadata = {
      title: 'My Page Title',
    }

    export default function Page() {
      return '...'
    }
```

[모든 metadata 옵션 보기](https://nextjs.org/docs/app/api-reference/functions/generate-metadata).

### Step 4: 페이지 마이그레이션[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-4-migrating-pages)

- [`app` 디렉터리](https://nextjs.org/docs/app)의 페이지는 기본적으로 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)입니다. `pages` 디렉터리에서는 페이지가 [Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)였다는 점과 다릅니다.
- `app`에서는 [데이터 패칭](https://nextjs.org/docs/app/getting-started/fetching-data)이 변경되었습니다. `getServerSideProps`, `getStaticProps`, `getInitialProps`는 더 단순한 API로 대체되었습니다.
- `app` 디렉터리는 중첩 폴더를 사용해 라우트를 정의하고, 공개 라우트 세그먼트를 만들기 위해 특별한 `page.js` 파일을 사용합니다.
- `pages` Directory| `app` Directory| Route
---|---|---
`index.js`| `page.js`| `/`
`about.js`| `about/page.js`| `/about`
`blog/[slug].js`| `blog/[slug]/page.js`| `/blog/post-1`

페이지 마이그레이션은 두 가지 주요 단계로 나누는 것을 권장합니다.

- Step 1: 기본 내보내기(Page Component)를 새로운 Client Component로 이동합니다.
- Step 2: 새 Client Component를 `app` 디렉터리의 새로운 `page.js` 파일로 가져옵니다.

> **알아두면 좋아요**: 이 경로가 `pages` 디렉터리와 가장 유사한 동작을 제공하므로 가장 쉬운 마이그레이션 방법입니다.

**Step 1: 새 Client Component 만들기**

- `app` 디렉터리 안에 새 파일(예: `app/home-page.tsx`)을 만들고 Client Component를 내보냅니다. Client Component를 정의하려면 파일 맨 위(어떤 import보다 먼저)에 `'use client'` 지시문을 추가합니다.
  - Pages Router와 마찬가지로 초기 페이지 로드 시 Client Component를 정적 HTML로 사전 렌더링하는 [최적화 단계](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-client-first-load)가 있습니다.
- `pages/index.js`에서 기본 내보낸 페이지 컴포넌트를 `app/home-page.tsx`로 이동합니다.

app/home-page.tsx

JavaScriptTypeScript
```
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
```

**Step 2: 새 페이지 만들기**

- `app` 디렉터리 안에 새 `app/page.tsx` 파일을 만듭니다. 이는 기본적으로 Server Component입니다.
- 해당 페이지에 `home-page.tsx` Client Component를 import합니다.
- 기존에 `pages/index.js`에서 데이터를 패칭했다면, 새 [데이터 패칭 API](https://nextjs.org/docs/app/getting-started/fetching-data)를 사용해 Server Component로 직접 옮기세요. 자세한 내용은 [데이터 패칭 업그레이드 가이드](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-6-migrating-data-fetching-methods)를 확인하세요.

app/page.tsx

JavaScriptTypeScript
```
// Import your Client Component
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
```

- 이전 페이지에서 `useRouter`를 사용했다면 새로운 라우팅 훅으로 업데이트해야 합니다. [자세히 알아보기](https://nextjs.org/docs/app/api-reference/functions/use-router).
- 개발 서버를 시작하고 [`http://localhost:3000`](http://localhost:3000)에 접속하면 기존 인덱스 라우트가 이제 app 디렉터리를 통해 제공되는 것을 확인할 수 있습니다.

### Step 5: 라우팅 훅 마이그레이션[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-5-migrating-routing-hooks)

`app` 디렉터리의 새로운 동작을 지원하기 위해 새 라우터가 추가되었습니다.

`app`에서는 `next/navigation`에서 가져오는 세 가지 새 훅인 [`useRouter()`](https://nextjs.org/docs/app/api-reference/functions/use-router), [`usePathname()`](https://nextjs.org/docs/app/api-reference/functions/use-pathname), [`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)를 사용해야 합니다.

- 새로운 `useRouter` 훅은 `next/navigation`에서 import되며, `pages` 디렉터리에서 `next/router`로부터 가져오던 `useRouter`와 동작이 다릅니다.
  - [`next/router`에서 import한 `useRouter` 훅](https://nextjs.org/docs/pages/api-reference/functions/use-router)은 `app` 디렉터리에서는 지원되지 않지만 `pages` 디렉터리에서는 계속 사용할 수 있습니다.
- 새로운 `useRouter`는 `pathname` 문자열을 반환하지 않습니다. 대신 별도의 `usePathname` 훅을 사용하세요.
- 새로운 `useRouter`는 `query` 객체를 반환하지 않습니다. 검색 매개변수와 동적 라우트 매개변수가 분리되었으므로 `useSearchParams`와 `useParams` 훅을 사용하세요.
- 페이지 변경을 감지하려면 `useSearchParams`와 `usePathname`을 함께 사용할 수 있습니다. 자세한 내용은 [Router Events](https://nextjs.org/docs/app/api-reference/functions/use-router#router-events) 섹션을 확인하세요.
- 이러한 새 훅은 Client Component에서만 지원되며 Server Component에서는 사용할 수 없습니다.

app/example-client-component.tsx

JavaScriptTypeScript
```
    'use client'

    import { useRouter, usePathname, useSearchParams } from 'next/navigation'

    export default function ExampleClientComponent() {
      const router = useRouter()
      const pathname = usePathname()
      const searchParams = useSearchParams()

      // ...
    }
```

또한 새로운 `useRouter` 훅에는 다음과 같은 변경 사항이 있습니다.

- `fallback`이 [대체](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#replacing-fallback)되었으므로 `isFallback`이 제거되었습니다.
- built-in i18n Next.js 기능이 `app` 디렉터리에서는 더 이상 필요하지 않으므로 `locale`, `locales`, `defaultLocales`, `domainLocales` 값이 제거되었습니다. [i18n 자세히 보기](https://nextjs.org/docs/app/guides/internationalization).
- `basePath`가 제거되었습니다. 대체 기능은 `useRouter`에 포함되지 않으며 아직 구현되지 않았습니다.
- 새로운 라우터에서 `as` 개념이 제거되었으므로 `asPath`도 제거되었습니다.
- 더 이상 필요하지 않으므로 `isReady`가 제거되었습니다. [정적 렌더링](https://nextjs.org/docs/app/guides/caching#static-rendering) 중 [`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) 훅을 사용하는 컴포넌트는 프리렌더링 단계를 건너뛰고 런타임에 클라이언트에서 렌더링됩니다.
- `route`가 제거되었습니다. 대체로 `usePathname` 또는 `useSelectedLayoutSegments()`를 사용할 수 있습니다.

[`useRouter()` API 레퍼런스 보기](https://nextjs.org/docs/app/api-reference/functions/use-router).

#### `pages`와 `app` 사이에서 컴포넌트 공유[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#sharing-components-between-pages-and-app)

`pages`와 `app` 라우터 간에 컴포넌트를 호환 상태로 유지하려면 [`next/compat/router`의 `useRouter` 훅](https://nextjs.org/docs/pages/api-reference/functions/use-router#the-nextcompatrouter-export)을 참조하십시오. 이는 `pages` 디렉터리에서 사용하는 `useRouter` 훅이지만, 라우터 사이에서 컴포넌트를 공유할 때 사용하도록 설계되었습니다. `app` 라우터에서만 사용할 준비가 되면 [`next/navigation`의 새로운 `useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router)로 업데이트하십시오.

### 단계 6: 데이터 가져오기 메서드 마이그레이션[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-6-migrating-data-fetching-methods)

`pages` 디렉터리는 페이지의 데이터를 가져오기 위해 `getServerSideProps`와 `getStaticProps`를 사용합니다. `app` 디렉터리 안에서는 이러한 이전 데이터 가져오기 함수가 `fetch()`와 `async` React Server Components 위에 구축된 [더 단순한 API](https://nextjs.org/docs/app/getting-started/fetching-data)로 대체됩니다.

app/page.tsx

JavaScriptTypeScript
```
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
```

#### 서버 사이드 렌더링 (`getServerSideProps`)[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#server-side-rendering-getserversideprops)

`pages` 디렉터리에서는 `getServerSideProps`로 서버에서 데이터를 가져와 해당 파일의 기본 내보내기 React 컴포넌트에 props를 전달합니다. 페이지의 초기 HTML은 서버에서 미리 렌더링되고, 이후 브라우저에서 페이지를 "수화(hydrating)"하여 인터랙티브하게 만듭니다.

pages/dashboard.js
```
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
```

App Router에서는 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)를 사용해 React 컴포넌트 내부에 데이터 가져오기를 공존시킬 수 있습니다. 이렇게 하면 렌더링된 HTML을 서버에서 유지하면서도 클라이언트로 전송되는 JavaScript를 줄일 수 있습니다.

`cache` 옵션을 `no-store`로 설정하면 가져온 데이터가 [절대로 캐시되지 않아야 함](https://nextjs.org/docs/app/getting-started/fetching-data)을 나타낼 수 있습니다. 이는 `pages` 디렉터리의 `getServerSideProps`와 유사합니다.

app/dashboard/page.tsx

JavaScriptTypeScript
```
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
```

#### 요청 객체에 접근[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#accessing-request-object)

`pages` 디렉터리에서는 Node.js HTTP API를 기반으로 요청 관련 데이터를 가져올 수 있습니다.

예를 들어 `getServerSideProps`에서 `req` 객체를 받아 요청의 쿠키와 헤더를 읽을 수 있습니다.

pages/index.js
```
    // `pages` directory

    export async function getServerSideProps({ req, query }) {
      const authHeader = req.getHeaders()['authorization'];
      const theme = req.cookies['theme'];

      return { props: { ... }}
    }

    export default function Page(props) {
      return ...
    }
```

`app` 디렉터리는 요청 데이터를 읽어오기 위한 새 읽기 전용 함수를 제공합니다.

  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers): Web Headers API를 기반으로 하며, 요청 헤더를 가져오기 위해 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) 안에서 사용할 수 있습니다.
  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies): Web Cookies API를 기반으로 하며, 쿠키를 가져오기 위해 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) 안에서 사용할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
```
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
```

#### 정적 사이트 생성 (`getStaticProps`)[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#static-site-generation-getstaticprops)

`pages` 디렉터리에서는 `getStaticProps` 함수가 빌드 시점에 페이지를 미리 렌더링하는 데 사용됩니다. 이 함수는 외부 API나 데이터베이스에서 데이터를 가져와 빌드 중 전체 페이지에 전달할 수 있습니다.

pages/index.js
```
    // `pages` directory

    export async function getStaticProps() {
      const res = await fetch(`https://...`)
      const projects = await res.json()

      return { props: { projects } }
    }

    export default function Index({ projects }) {
      return projects.map((project) => <div>{project.name}</div>)
    }
```

`app` 디렉터리에서는 [`fetch()`](https://nextjs.org/docs/app/api-reference/functions/fetch)를 사용한 데이터 가져오기가 기본적으로 `cache: 'force-cache'`를 적용하며, 수동으로 무효화될 때까지 요청 데이터를 캐시합니다. 이는 `pages` 디렉터리의 `getStaticProps`와 유사합니다.

app/page.js
```
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
```

#### 동적 경로 (`getStaticPaths`)[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#dynamic-paths-getstaticpaths)

`pages` 디렉터리에서는 `getStaticPaths` 함수가 빌드 시점에 미리 렌더링해야 하는 동적 경로를 정의합니다.

pages/posts/[id].js
```
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
```

`app` 디렉터리에서는 `getStaticPaths`가 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)로 대체됩니다.

[`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)는 `getStaticPaths`와 유사하게 동작하지만, 라우트 매개변수를 반환하기 위한 API가 단순화되어 있으며 [레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout) 안에서도 사용할 수 있습니다. `generateStaticParams`의 반환 형태는 중첩된 `param` 객체 배열이나 해석된 경로 문자열이 아니라 세그먼트 배열입니다.

app/posts/[id]/page.js
```
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
```

`app` 디렉터리의 새로운 모델에는 `generateStaticParams`라는 이름이 `getStaticPaths`보다 더 적합합니다. `getStaticProps`와 `getServerSideProps`가 필요하지 않게 되었으므로 `get` 접두사는 더 설명적인 `generate`로 대체되었고, 다중 동적 세그먼트를 갖는 중첩 라우팅에 더 적합하도록 `Paths` 접미사는 `Params`로 바뀌었습니다.

* * *

#### `fallback` 대체[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#replacing-fallback)

`pages` 디렉터리에서 `getStaticPaths`가 반환하는 `fallback` 속성은 빌드 시점에 미리 렌더링되지 않은 페이지의 동작을 정의합니다. 이 속성은 페이지가 생성되는 동안 폴백 페이지를 보여 주도록 `true`, 404 페이지를 보여 주도록 `false`, 요청 시점에 페이지를 생성하도록 `blocking`으로 설정할 수 있습니다.

pages/posts/[id].js
```
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
```

`app` 디렉터리에서는 [`config.dynamicParams` 속성](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams)이 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)에 포함되지 않은 params를 처리하는 방식을 제어합니다.

  * **`true`**: (기본값) `generateStaticParams`에 포함되지 않은 동적 세그먼트가 필요 시 생성됩니다.
  * **`false`**: `generateStaticParams`에 포함되지 않은 동적 세그먼트는 404를 반환합니다.

이는 `pages` 디렉터리의 `getStaticPaths`에서 사용하던 `fallback: true | false | 'blocking'` 옵션을 대체합니다. 스트리밍 환경에서 `'blocking'`과 `true` 사이의 차이가 미미하므로 `dynamicParams`에는 `fallback: 'blocking'`에 해당하는 옵션이 포함되지 않았습니다.

app/posts/[id]/page.js
```
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
```

[`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams)를 `true`(기본값)로 설정하면 아직 생성되지 않은 라우트 세그먼트가 요청될 때 서버에서 렌더링되고 캐시됩니다.

#### 증분 정적 재생성 (`getStaticProps`와 `revalidate` 조합)[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#incremental-static-regeneration-getstaticprops-with-revalidate)

`pages` 디렉터리에서 `getStaticProps` 함수는 일정 시간이 지나면 페이지를 자동으로 다시 생성할 수 있도록 `revalidate` 필드를 추가할 수 있게 합니다.

pages/index.js
```
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
```

`app` 디렉터리에서는 [`fetch()`](https://nextjs.org/docs/app/api-reference/functions/fetch) 데이터 패칭에 `revalidate`를 사용할 수 있으며, 지정한 초 단위로 요청을 캐시합니다.

app/page.js
```
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
```

#### API 경로[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#api-routes)

API Routes는 `pages/api` 디렉터리에서 변경 없이 계속 동작합니다. 다만 `app` 디렉터리에서는 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)로 대체되었습니다.

Route Handlers를 사용하면 Web [Request](https://developer.mozilla.org/docs/Web/API/Request) 및 [Response](https://developer.mozilla.org/docs/Web/API/Response) API를 활용해 특정 경로에 대한 사용자 정의 요청 핸들러를 만들 수 있습니다.

app/api/route.ts

JavaScriptTypeScript
```
    export async function GET(request: Request) {}
```

> **알아두면 좋아요**: 이전에 클라이언트에서 외부 API를 호출하기 위해 API Routes를 사용했다면, 이제는 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)를 이용해 더 안전하게 데이터를 가져올 수 있습니다. [데이터 패칭](https://nextjs.org/docs/app/getting-started/fetching-data)에 대해 더 알아보세요.

#### 싱글 페이지 애플리케이션[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#single-page-applications)

동시에 싱글 페이지 애플리케이션(SPA)에서 Next.js로 마이그레이션 중이라면, 자세한 내용은 [문서](https://nextjs.org/docs/app/guides/single-page-applications)를 확인하세요.

### 7단계: 스타일링[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#step-7-styling)

`pages` 디렉터리에서는 전역 스타일시트를 `pages/_app.js`에만 제한합니다. `app` 디렉터리에서는 이 제한이 해제되었으며, 전역 스타일을 어떤 레이아웃, 페이지, 컴포넌트에도 추가할 수 있습니다.

  * [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules)
  * [Tailwind CSS](https://nextjs.org/docs/app/getting-started/css#tailwind-css)
  * [Global Styles](https://nextjs.org/docs/app/getting-started/css#global-css)
  * [CSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)
  * [External Stylesheets](https://nextjs.org/docs/app/getting-started/css#external-stylesheets)
  * [Sass](https://nextjs.org/docs/app/guides/sass)

#### Tailwind CSS[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#tailwind-css)

Tailwind CSS를 사용하는 경우 `tailwind.config.js` 파일에 `app` 디렉터리를 추가해야 합니다.

tailwind.config.js
```
    module.exports = {
      content: [
        './app/**/*.{js,ts,jsx,tsx,mdx}', // <-- Add this line
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
      ],
    }
```

또한 전역 스타일을 `app/layout.js` 파일에서 임포트해야 합니다.

app/layout.js
```
    import '../styles/globals.css'

    export default function RootLayout({ children }) {
      return (
        <html lang="en">
          <body>{children}</body>
        </html>
      )
    }
```

[Tailwind CSS 스타일링](https://nextjs.org/docs/app/getting-started/css#tailwind-css)에 대해 더 알아보세요.

## App Router와 Pages Router를 함께 사용하기[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#using-app-router-together-with-pages-router)

서로 다른 Next.js 라우터가 제공하는 경로 사이를 탐색하면 하드 내비게이션이 발생합니다. `next/link`의 자동 링크 프리패칭은 라우터 간에는 동작하지 않습니다.

대신 App Router와 Pages Router 간 내비게이션을 [최적화](https://vercel.com/guides/optimizing-hard-navigations)하여 프리패치된 빠른 페이지 전환을 유지할 수 있습니다. [자세히 알아보기](https://vercel.com/guides/optimizing-hard-navigations).

## Codemods[](https://nextjs.org/docs/pages/guides/migrating/app-router-migration#codemods)

Next.js는 기능이 더는 지원되지 않을 때 코드베이스 업그레이드를 돕는 Codemod 변환을 제공합니다. 더 자세한 정보는 [Codemods](https://nextjs.org/docs/app/guides/upgrading/codemods)를 참고하세요.

Send