---
title: '파일 시스템 규칙: layout.js'
description: '파일은 Next.js 애플리케이션에서 레이아웃을 정의하는 데 사용됩니다.'
---

# 파일 시스템 규칙: layout.js | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/layout

[API Reference](https://nextjs.org/docs/app/api-reference)[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)layout.js

페이지 복사

# layout.js

최종 업데이트 2026년 2월 20일

`layout` 파일은 Next.js 애플리케이션에서 레이아웃을 정의하는 데 사용됩니다.

app/dashboard/layout.tsx

JavaScriptTypeScript
[code]
    export default function DashboardLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return <section>{children}</section>
    }
[/code]

**루트 레이아웃** 은 루트 `app` 디렉터리에서 가장 상위에 있는 레이아웃입니다. `<html>` 및 `<body>` 태그와 전역으로 공유되는 UI를 정의하는 데 사용합니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    export default function RootLayout({
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

## 참고[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#reference)

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#props)

#### `children` (필수)[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#children-required)

레이아웃 컴포넌트는 `children` prop을 받아서 사용해야 합니다. 렌더링 중에 `children` 은 레이아웃이 감싸고 있는 경로 세그먼트로 채워집니다. 주로 하위 [Layout](https://nextjs.org/docs/app/api-reference/file-conventions/page) (존재한다면) 또는 [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page) 컴포넌트가 되지만, 상황에 따라 [Loading](https://nextjs.org/docs/app/api-reference/file-conventions/loading)이나 [Error](https://nextjs.org/docs/app/getting-started/error-handling) 같은 다른 특수 파일일 수도 있습니다.

#### `params` (선택)[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#params-optional)

루트 세그먼트에서 해당 레이아웃까지의 [동적 경로 파라미터](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) 객체로 해결되는 프로미스입니다.

app/dashboard/[team]/layout.tsx

JavaScriptTypeScript
[code]
    export default async function Layout({
      children,
      params,
    }: {
      children: React.ReactNode
      params: Promise<{ team: string }>
    }) {
      const { team } = await params
    }
[/code]

예시 경로| URL| `params`  
---|---|---  
`app/dashboard/[team]/layout.js`| `/dashboard/1`| `Promise<{ team: '1' }>`  
`app/shop/[tag]/[item]/layout.js`| `/shop/1/2`| `Promise<{ tag: '1', item: '2' }>`  
`app/blog/[...slug]/layout.js`| `/blog/1/2`| `Promise<{ slug: ['1', '2'] }>`  
  
  * `params` prop은 프로미스이므로 값을 읽으려면 `async/await` 또는 React의 [`use`](https://react.dev/reference/react/use) 함수를 사용해야 합니다.
    * 버전 14 및 이전 버전에서는 `params` 가 동기 prop이었습니다. 하위 호환을 위해 Next.js 15에서도 동기적으로 접근할 수 있지만, 이 동작은 앞으로 제거될 예정입니다.



### Layout Props Helper[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)

디렉터리 구조에서 유추되는 강한 타입의 `params` 와 이름 있는 슬롯을 얻기 위해 레이아웃을 `LayoutProps` 로 타입 지정할 수 있습니다. `LayoutProps` 는 전역에서 사용할 수 있는 헬퍼입니다.

app/dashboard/layout.tsx
[code]
    export default function Layout(props: LayoutProps<'/dashboard'>) {
      return (
        <section>
          {props.children}
          {/* If you have app/dashboard/@analytics, it appears as a typed slot: */}
          {/* {props.analytics} */}
        </section>
      )
    }
[/code]

> **알아두면 좋아요** :
> 
>   * `next dev`, `next build`, `next typegen` 중 하나를 실행할 때 타입이 생성됩니다.
>   * 타입 생성 이후에는 `LayoutProps` 헬퍼가 전역에서 제공되므로 import 할 필요가 없습니다.
> 


### Root Layout[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)

`app` 디렉터리에는 루트 `app` 디렉터리에서 가장 상위에 위치한 **루트 레이아웃** 이 반드시 포함되어야 합니다. 일반적으로 루트 레이아웃은 `app/layout.js` 입니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html>
          <body>{children}</body>
        </html>
      )
    }
[/code]

  * 루트 레이아웃은 `<html>` 및 `<body>` 태그를 반드시 정의해야 합니다.
    * `<title>` 또는 `<meta>` 와 같은 `<head>` 태그를 루트 레이아웃에 수동으로 추가해서는 안 됩니다. 대신 [Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)를 사용하면 스트리밍이나 `<head>` 요소 중복 제거 같은 고급 요구 사항을 자동으로 처리할 수 있습니다.
  * **여러 개의 루트 레이아웃** 을 만들 수 있습니다. 위쪽에 `layout.js` 가 없는 레이아웃은 모두 루트 레이아웃입니다. 대표적인 두 가지 방식:
    * `app/(shop)/layout.js`, `app/(marketing)/layout.js`처럼 [route group](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups)을 사용
    * `app/layout.js` 를 생략하여 `app/dashboard/layout.js`, `app/blog/layout.js` 등의 하위 디렉터리 레이아웃이 각 디렉터리의 루트 레이아웃이 되도록 함
    * **여러 루트 레이아웃 사이** 를 탐색하면 클라이언트 측 전환이 아닌 **페이지 전체 새로고침** 이 발생합니다.
  * 루트 레이아웃은 [internationalization](https://nextjs.org/docs/app/guides/internationalization)을 구현할 때처럼 `app/[lang]/layout.js` 같이 **동적 세그먼트** 아래 위치시킬 수도 있습니다.



## 주의사항[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#caveats)

### Request Object[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#request-object)

레이아웃은 탐색 중 불필요한 서버 요청을 피하기 위해 클라이언트 측에 캐시됩니다.

[Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout)는 다시 렌더링되지 않습니다. 페이지 간 탐색 시 레이아웃을 캐시하고 재사용하여 불필요한 연산을 줄일 수 있습니다. 레이아웃에서 원시 요청 객체 접근을 제한하면, Next.js는 잠재적으로 느리거나 비용이 큰 사용자 코드를 레이아웃에서 실행하는 것을 방지해 성능 저하를 막을 수 있습니다.

요청 객체가 필요하다면 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) 및 함수에서 [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)와 [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API를 사용할 수 있습니다.

app/shop/layout.tsx

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'
     
    export default async function Layout({ children }) {
      const cookieStore = await cookies()
      const theme = cookieStore.get('theme')
      return '...'
    }
[/code]

### Query params[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#query-params)

레이아웃은 탐색 시 다시 렌더링되지 않으므로, 그렇지 않으면 오래될 검색 파라미터(search params)에 접근할 수 없습니다.

최신 쿼리 파라미터를 읽으려면 Page의 [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) prop을 사용하거나, Client Component 안에서 [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) 훅으로 읽으면 됩니다. Client Component는 탐색 시 다시 렌더링되므로 최신 쿼리 파라미터를 사용할 수 있습니다.

app/ui/search.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useSearchParams } from 'next/navigation'
     
    export default function Search() {
      const searchParams = useSearchParams()
     
      const search = searchParams.get('search')
     
      return '...'
    }
[/code]

app/shop/layout.tsx

JavaScriptTypeScript
[code]
    import Search from '@/app/ui/search'
     
    export default function Layout({ children }) {
      return (
        <>
          <Search />
          {children}
        </>
      )
    }
[/code]

### Pathname[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#pathname)

레이아웃은 탐색 시 다시 렌더링되지 않으므로, 그렇지 않으면 오래될 pathname에 접근할 수 없습니다.

현재 pathname이 필요하다면 Client Component 안에서 [`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) 훅으로 읽으면 됩니다. Client Component는 탐색 중 다시 렌더링되므로 최신 pathname에 접근할 수 있습니다.

app/ui/breadcrumbs.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { usePathname } from 'next/navigation'
     
    // Simplified breadcrumbs logic
    export default function Breadcrumbs() {
      const pathname = usePathname()
      const segments = pathname.split('/')
     
      return (
        <nav>
          {segments.map((segment, index) => (
            <span key={index}>
              {' > '}
              {segment}
            </span>
          ))}
        </nav>
      )
    }
[/code]

app/docs/layout.tsx

JavaScriptTypeScript
[code]
    import { Breadcrumbs } from '@/app/ui/Breadcrumbs'
     
    export default function Layout({ children }) {
      return (
        <>
          <Breadcrumbs />
          <main>{children}</main>
        </>
      )
    }
[/code]

### Fetching Data[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#fetching-data)

레이아웃은 `children` 에 데이터를 전달할 수 없습니다. 그러나 하나의 경로에서 같은 데이터를 여러 번 가져오고 React [`cache`](https://react.dev/reference/react/cache)를 사용해 요청을 중복 제거해도 성능에는 영향을 주지 않습니다.

또는 Next.js에서 [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch)를 사용할 때는 요청이 자동으로 중복 제거됩니다.

app/lib/data.ts

JavaScriptTypeScript
[code]
    export async function getUser(id: string) {
      const res = await fetch(`https://.../users/${id}`)
      return res.json()
    }
[/code]

app/dashboard/layout.tsx

JavaScriptTypeScript
[code]
    import { getUser } from '@/app/lib/data'
    import { UserName } from '@/app/ui/user-name'
     
    export default async function Layout({ children }) {
      const user = await getUser('1')
     
      return (
        <>
          <nav>
            {/* ... */}
            <UserName user={user.name} />
          </nav>
          {children}
        </>
      )
    }
[/code]

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { getUser } from '@/app/lib/data'
    import { UserName } from '@/app/ui/user-name'
     
    export default async function Page() {
      const user = await getUser('1')
     
      return (
        <div>
          <h1>Welcome {user.name}</h1>
        </div>
      )
    }
[/code]

### Accessing child segments[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#accessing-child-segments)

레이아웃은 자신 아래 경로 세그먼트에 접근할 수 없습니다. 모든 경로 세그먼트가 필요하다면 Client Component 안에서 [`useSelectedLayoutSegment`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment) 또는 [`useSelectedLayoutSegments`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)를 사용할 수 있습니다.

app/ui/nav-link.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import Link from 'next/link'
    import { useSelectedLayoutSegment } from 'next/navigation'
     
    export default function NavLink({
      slug,
      children,
    }: {
      slug: string
      children: React.ReactNode
    }) {
      const segment = useSelectedLayoutSegment()
      const isActive = slug === segment
     
      return (
        <Link
          href={`/blog/${slug}`}
          // Change style depending on whether the link is active
          style={{ fontWeight: isActive ? 'bold' : 'normal' }}
        >
          {children}
        </Link>
      )
    }
[/code]

app/blog/layout.tsx

JavaScriptTypeScript
[code]
    import { NavLink } from './nav-link'
    import getPosts from './get-posts'
     
    export default async function Layout({
      children,
    }: {
      children: React.ReactNode
    }) {
      const featuredPosts = await getPosts()
      return (
        <div>
          {featuredPosts.map((post) => (
            <div key={post.id}>
              <NavLink slug={post.slug}>{post.title}</NavLink>
            </div>
          ))}
          <div>{children}</div>
        </div>
      )
    }
[/code]

## 예시[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#examples)

### 메타데이터[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#metadata)

[`metadata` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#the-metadata-object)나 [`generateMetadata` 함수](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#generatemetadata-function)를 사용하면 `title`, `meta` 등의 `<head>` HTML 요소를 수정할 수 있습니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: 'Next.js',
    }
     
    export default function Layout({ children }: { children: React.ReactNode }) {
      return '...'
    }
[/code]

> **알아두면 좋아요** : 루트 레이아웃에 `<title>` 및 `<meta>` 같은 `<head>` 태그를 직접 추가하면 **안 됩니다**. 대신 스트리밍 및 `<head>` 요소 중복 제거 같은 고급 요구 사항을 자동으로 처리하는 [Metadata API](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)를 사용하세요.

### 활성 내비게이션 링크[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#active-nav-links)

[`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) 훅을 사용해 내비게이션 링크가 활성 상태인지 판단할 수 있습니다.

`usePathname` 는 클라이언트 훅이므로 내비게이션 링크를 Client Component로 분리한 뒤 레이아웃에서 가져와야 합니다:

app/ui/nav-links.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { usePathname } from 'next/navigation'
    import Link from 'next/link'
     
    export function NavLinks() {
      const pathname = usePathname()
     
      return (
        <nav>
          <Link className={`link ${pathname === '/' ? 'active' : ''}`} href="/">
            Home
          </Link>
     
          <Link
            className={`link ${pathname === '/about' ? 'active' : ''}`}
            href="/about"
          >
            About
          </Link>
        </nav>
      )
    }
[/code]

app/layout.tsx

JavaScriptTypeScript
[code]
    import { NavLinks } from '@/app/ui/nav-links'
     
    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="en">
          <body>
            <NavLinks />
            <main>{children}</main>
          </body>
        </html>
      )
    }
[/code]

### `params` 기반 콘텐츠 표시[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#displaying-content-based-on-params)

[동적 라우트 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 사용하면 `params` prop에 따라 특정 콘텐츠를 표시하거나 가져올 수 있습니다.

app/dashboard/layout.tsx

JavaScriptTypeScript
[code]
    export default async function DashboardLayout({
      children,
      params,
    }: {
      children: React.ReactNode
      params: Promise<{ team: string }>
    }) {
      const { team } = await params
     
      return (
        <section>
          <header>
            <h1>Welcome to {team}'s Dashboard</h1>
          </header>
          <main>{children}</main>
        </section>
      )
    }
[/code]

### 클라이언트 컴포넌트에서 `params` 읽기[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#reading-params-in-client-components)

`params` 를 Client Component( `async` 가 될 수 없음)에서 사용하려면 React의 [`use`](https://react.dev/reference/react/use) 함수를 사용해 promise를 읽을 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { use } from 'react'
     
    export default function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = use(params)
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#version-history)

Version| Changes  
---|---  
`v15.0.0-RC`| `params` 가 이제 Promise입니다. [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150)을 사용할 수 있습니다.  
`v13.0.0`| `layout` 이 도입되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
