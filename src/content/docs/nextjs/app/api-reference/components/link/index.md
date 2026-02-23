---
title: '컴포넌트: Link Component'
description: '는 prefetching과 경로 간 클라이언트 측 내비게이션을 제공하도록 HTML  요소를 확장한 React 컴포넌트입니다. Next.js에서 경로 간 이동을 수행하는 기본 방법입니다.'
---

# 컴포넌트: Link Component | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/components/link

[API Reference](https://nextjs.org/docs/app/api-reference)[Components](https://nextjs.org/docs/app/api-reference/components)Link Component

Copy page

# Link Component

Last updated February 20, 2026

`<Link>`는 [prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)과 경로 간 클라이언트 측 내비게이션을 제공하도록 HTML `<a>` 요소를 확장한 React 컴포넌트입니다. Next.js에서 경로 간 이동을 수행하는 기본 방법입니다.

기본 사용 예:

app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return <Link href="/dashboard">Dashboard</Link>
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/components/link#reference)

다음 props를 `<Link>` 컴포넌트에 전달할 수 있습니다:

Prop| Example| Type| Required  
---|---|---|---  
[`href`](https://nextjs.org/docs/app/api-reference/components/link#href-required)| `href="/dashboard"`| String or Object| Yes  
[`replace`](https://nextjs.org/docs/app/api-reference/components/link#replace)| `replace={false}`| Boolean| -  
[`scroll`](https://nextjs.org/docs/app/api-reference/components/link#scroll)| `scroll={false}`| Boolean| -  
[`prefetch`](https://nextjs.org/docs/app/api-reference/components/link#prefetch)| `prefetch={false}`| Boolean or null| -  
[`onNavigate`](https://nextjs.org/docs/app/api-reference/components/link#onnavigate)| `onNavigate={(e) => {}}`| Function| -  
  
> **알아두면 좋아요** : `className`이나 `target="_blank"` 같은 `<a>` 태그 속성은 `<Link>`에 props로 추가할 수 있으며, 내부 `<a>` 요소로 전달됩니다.

### `href` (required)[](https://nextjs.org/docs/app/api-reference/components/link#href-required)

이동할 경로나 URL입니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    // Navigate to /about?name=test
    export default function Page() {
      return (
        <Link
          href={{
            pathname: '/about',
            query: { name: 'test' },
          }}
        >
          About
        </Link>
      )
    }
[/code]

### `replace`[](https://nextjs.org/docs/app/api-reference/components/link#replace)

**기본값은 `false`입니다.** `true`일 때 `next/link`는 [브라우저 기록](https://developer.mozilla.org/docs/Web/API/History_API) 스택에 새 URL을 추가하는 대신 현재 히스토리 상태를 대체합니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <Link href="/dashboard" replace>
          Dashboard
        </Link>
      )
    }
[/code]

### `scroll`[](https://nextjs.org/docs/app/api-reference/components/link#scroll)

**기본값은 `true`입니다.** Next.js에서 `<Link>`의 기본 스크롤 동작은 **스크롤 위치를 유지**하는 것으로, 브라우저가 뒤로/앞으로 이동을 처리하는 방식과 유사합니다. 새 [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page)로 이동하면 페이지가 뷰포트에 보이는 동안에는 스크롤 위치가 유지됩니다. 하지만 페이지가 뷰포트에 보이지 않으면 Next.js는 첫 번째 Page 요소의 상단으로 스크롤합니다.

`scroll = {false}`이면 Next.js는 첫 번째 Page 요소로 스크롤하려 하지 않습니다.

> **알아두면 좋아요** : Next.js는 스크롤 동작을 제어하기 전에 `scroll: false`인지 확인합니다. 스크롤이 활성화되어 있으면 내비게이션에 관련된 DOM 노드를 식별하고 최상위 요소를 순회합니다. 스크롤이 불가능하거나 렌더링된 HTML이 없는 요소(예: sticky 또는 fixed 위치 요소, `getBoundingClientRect`로 계산되는 비가시 요소)는 모두 건너뜁니다. Next.js는 뷰포트에 보이는 스크롤 가능한 요소를 찾을 때까지 형제 요소를 계속 탐색합니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <Link href="/dashboard" scroll={false}>
          Dashboard
        </Link>
      )
    }
[/code]

### `prefetch`[](https://nextjs.org/docs/app/api-reference/components/link#prefetch)

`<Link />` 컴포넌트가 뷰포트에 들어오면(초기 진입 또는 스크롤 시) 프리패칭이 발생합니다. Next.js는 백그라운드에서 연결된 경로(`href`로 표시)와 해당 데이터를 미리 가져와 클라이언트 측 내비게이션 성능을 개선합니다. 사용자에게 `<Link />`를 호버할 때까지 프리패치된 데이터가 만료되면 Next.js는 다시 프리패칭을 시도합니다. **프리패칭은 프로덕션에서만 활성화됩니다.**

`prefetch` prop에 전달할 수 있는 값은 다음과 같습니다:

  * **`"auto"` 또는 `null` (기본값)**: 경로가 정적이냐 동적이냐에 따라 프리패칭 동작이 달라집니다. 정적 경로의 경우 전체 경로(모든 데이터 포함)를 프리패칭합니다. 동적 경로의 경우 [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading#instant-loading-states) 경계가 있는 가장 가까운 세그먼트까지 부분 경로를 프리패칭합니다.
  * `true`: 정적, 동적 경로 모두 전체 경로를 프리패칭합니다.
  * `false`: 뷰포트 진입 시와 호버 시 모두 프리패칭을 수행하지 않습니다.



app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <Link href="/dashboard" prefetch={false}>
          Dashboard
        </Link>
      )
    }
[/code]

### `onNavigate`[](https://nextjs.org/docs/app/api-reference/components/link#onnavigate)

클라이언트 측 내비게이션 동안 호출되는 이벤트 핸들러입니다. 핸들러는 `preventDefault()` 메서드가 포함된 이벤트 객체를 받아 필요하면 내비게이션을 취소할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <Link
          href="/dashboard"
          onNavigate={(e) => {
            // Only executes during SPA navigation
            console.log('Navigating...')
     
            // Optionally prevent navigation
            // e.preventDefault()
          }}
        >
          Dashboard
        </Link>
      )
    }
[/code]

> **알아두면 좋아요** : `onClick`과 `onNavigate`는 비슷해 보이지만 목적이 다릅니다. `onClick`은 모든 클릭 이벤트에서 실행되지만, `onNavigate`는 클라이언트 측 내비게이션 중에만 실행됩니다. 주요 차이점:
> 
>   * 보조 키(`Ctrl`/`Cmd` + 클릭)를 사용할 때 `onClick`은 실행되지만, Next.js가 새 탭용 기본 내비게이션을 막기 때문에 `onNavigate`는 실행되지 않습니다.
>   * 외부 URL은 클라이언트 측 및 동일 출처 내비게이션에만 해당하므로 `onNavigate`를 트리거하지 않습니다.
>   * `download` 속성이 있는 링크는 브라우저가 해당 URL을 다운로드로 처리하므로 `onClick`에서는 동작하지만 `onNavigate`에서는 동작하지 않습니다.
> 


## Examples[](https://nextjs.org/docs/app/api-reference/components/link#examples)

아래 예시는 다양한 시나리오에서 `<Link>` 컴포넌트를 사용하는 방법을 보여줍니다.

### 동적 경로 세그먼트에 연결하기[](https://nextjs.org/docs/app/api-reference/components/link#linking-to-dynamic-route-segments)

[동적 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)에 연결할 때는 [템플릿 리터럴과 보간](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Template_literals)을 사용해 링크 목록을 생성할 수 있습니다. 예를 들어, 블로그 게시물 목록을 생성하려면 다음과 같습니다:

app/blog/post-list.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    interface Post {
      id: number
      title: string
      slug: string
    }
     
    export default function PostList({ posts }: { posts: Post[] }) {
      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>
              <Link href={`/blog/${post.slug}`}>{post.title}</Link>
            </li>
          ))}
        </ul>
      )
    }
[/code]

### 활성 링크 확인하기[](https://nextjs.org/docs/app/api-reference/components/link#checking-active-links)

[`usePathname()`](https://nextjs.org/docs/app/api-reference/functions/use-pathname)을 사용해 링크가 활성 상태인지 확인할 수 있습니다. 예를 들어, 활성 링크에 클래스를 추가하려면 현재 `pathname`이 링크의 `href`와 일치하는지 확인하면 됩니다:

app/ui/nav-links.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { usePathname } from 'next/navigation'
    import Link from 'next/link'
     
    export function Links() {
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

### `id`로 스크롤하기[](https://nextjs.org/docs/app/api-reference/components/link#scrolling-to-an-id)

내비게이션 시 특정 `id`로 스크롤하려면 URL에 `#` 해시 링크를 추가하거나 해시 링크만 `href` prop에 전달하면 됩니다. `<Link>`가 `<a>` 요소로 렌더링되기 때문에 가능합니다.
[code] 
    <Link href="/dashboard#settings">Settings</Link>
     
    // Output
    <a href="/dashboard#settings">Settings</a>
[/code]

> **알아두면 좋아요** :
> 
>   * 내비게이션 시 페이지가 뷰포트에 보이지 않으면 Next.js가 [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page)로 스크롤합니다.
> 


### push 대신 URL 교체하기[](https://nextjs.org/docs/app/api-reference/components/link#replace-the-url-instead-of-push)

`Link` 컴포넌트의 기본 동작은 `history` 스택에 새 URL을 `push`하는 것입니다. 새 항목 추가를 방지하려면 다음 예시처럼 `replace` prop을 사용하세요:

app/page.js

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <Link href="/about" replace>
          About us
        </Link>
      )
    }
[/code]

### 페이지 상단으로 스크롤하는 동작 비활성화[](https://nextjs.org/docs/app/api-reference/components/link#disable-scrolling-to-the-top-of-the-page)

Next.js에서 `<Link>`의 기본 스크롤 동작은 **스크롤 위치를 유지**하는 것으로, 브라우저의 뒤로/앞으로 내비게이션 처리 방식과 유사합니다. 새 [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page)로 이동할 때 페이지가 뷰포트에 보이면 스크롤 위치가 그대로 유지됩니다.

하지만 페이지가 뷰포트에 보이지 않으면 Next.js는 첫 번째 Page 요소의 상단으로 스크롤합니다. 이 동작을 비활성화하려면 `<Link>` 컴포넌트에 `scroll={false}`를 전달하거나, `router.push()` 또는 `router.replace()`에 `scroll: false`를 전달하면 됩니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <Link href="/#hashid" scroll={false}>
          Disables scrolling to the top
        </Link>
      )
    }
[/code]

`router.push()` 또는 `router.replace()` 사용:
[code]
    // useRouter
    import { useRouter } from 'next/navigation'
     
    const router = useRouter()
     
    router.push('/dashboard', { scroll: false })
[/code]

### Proxy에서 링크 프리패칭하기[](https://nextjs.org/docs/app/api-reference/components/link#prefetching-links-in-proxy)

[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)는 인증이나 사용자를 다른 페이지로 리라이팅하는 기타 목적에 자주 사용됩니다. Proxy를 통한 리라이팅으로 `<Link />` 컴포넌트가 링크를 올바르게 프리패칭하도록 하려면, 보여줄 URL과 프리패칭할 URL을 모두 Next.js에 알려야 합니다. 이는 프록시를 거쳐 올바른 프리패칭 경로를 알아내기 위한 불필요한 요청을 방지하는 데 필요합니다.

예를 들어 인증 사용자와 방문자 뷰가 있는 `/dashboard` 라우트를 제공하려면, Proxy에 다음 코드를 추가해 사용자를 올바른 페이지로 리다이렉션할 수 있습니다:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'
     
    export function proxy(request: Request) {
      const nextUrl = request.nextUrl
      if (nextUrl.pathname === '/dashboard') {
        if (request.cookies.authToken) {
          return NextResponse.rewrite(new URL('/auth/dashboard', request.url))
        } else {
          return NextResponse.rewrite(new URL('/public/dashboard', request.url))
        }
      }
    }
[/code]

이 경우 `<Link />` 컴포넌트에서 다음 코드를 사용하면 됩니다:

app/page.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import Link from 'next/link'
    import useIsAuthed from './hooks/useIsAuthed' // Your auth hook
     
    export default function Page() {
      const isAuthed = useIsAuthed()
      const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
      return (
        <Link as="/dashboard" href={path}>
          Dashboard
        </Link>
      )
    }
[/code]

### 탐색 차단[](https://nextjs.org/docs/app/api-reference/components/link#blocking-navigation)

`onNavigate` prop을 사용하면 폼에 저장되지 않은 변경 사항이 있을 때처럼 특정 조건이 충족될 때 탐색을 차단할 수 있습니다. 앱 전반의 여러 컴포넌트에서 탐색을 차단해야 할 때(예: 폼 편집 중에는 모든 링크 이동을 막고 싶을 때) React Context를 사용하면 이 차단 상태를 깔끔하게 공유할 수 있습니다. 먼저 탐색 차단 상태를 추적할 컨텍스트를 만듭니다:

app/contexts/navigation-blocker.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { createContext, useState, useContext } from 'react'
     
    interface NavigationBlockerContextType {
      isBlocked: boolean
      setIsBlocked: (isBlocked: boolean) => void
    }
     
    export const NavigationBlockerContext =
      createContext<NavigationBlockerContextType>({
        isBlocked: false,
        setIsBlocked: () => {},
      })
     
    export function NavigationBlockerProvider({
      children,
    }: {
      children: React.ReactNode
    }) {
      const [isBlocked, setIsBlocked] = useState(false)
     
      return (
        <NavigationBlockerContext.Provider value={{ isBlocked, setIsBlocked }}>
          {children}
        </NavigationBlockerContext.Provider>
      )
    }
     
    export function useNavigationBlocker() {
      return useContext(NavigationBlockerContext)
    }
[/code]

컨텍스트를 사용하는 폼 컴포넌트를 만듭니다:

app/components/form.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useNavigationBlocker } from '../contexts/navigation-blocker'
     
    export default function Form() {
      const { setIsBlocked } = useNavigationBlocker()
     
      return (
        <form
          onSubmit={(e) => {
            e.preventDefault()
            setIsBlocked(false)
          }}
          onChange={() => setIsBlocked(true)}
        >
          <input type="text" name="name" />
          <button type="submit">Save</button>
        </form>
      )
    }
[/code]

탐색을 차단하는 커스텀 Link 컴포넌트를 만듭니다:

app/components/custom-link.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import Link from 'next/link'
    import { useNavigationBlocker } from '../contexts/navigation-blocker'
     
    interface CustomLinkProps extends React.ComponentProps<typeof Link> {
      children: React.ReactNode
    }
     
    export function CustomLink({ children, ...props }: CustomLinkProps) {
      const { isBlocked } = useNavigationBlocker()
     
      return (
        <Link
          onNavigate={(e) => {
            if (
              isBlocked &&
              !window.confirm('You have unsaved changes. Leave anyway?')
            ) {
              e.preventDefault()
            }
          }}
          {...props}
        >
          {children}
        </Link>
      )
    }
[/code]

탐색 컴포넌트를 만듭니다:

app/components/nav.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { CustomLink as Link } from './custom-link'
     
    export default function Nav() {
      return (
        <nav>
          <Link href="/">Home</Link>
          <Link href="/about">About</Link>
        </nav>
      )
    }
[/code]

마지막으로 루트 레이아웃에서 `NavigationBlockerProvider`로 앱을 감싸고 페이지에서 컴포넌트를 사용합니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import { NavigationBlockerProvider } from './contexts/navigation-blocker'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>
            <NavigationBlockerProvider>{children}</NavigationBlockerProvider>
          </body>
        </html>
      )
    }
[/code]

그런 다음 페이지에서 `Nav`와 `Form` 컴포넌트를 사용합니다:

app/page.tsx

JavaScriptTypeScript
[code]
    import Nav from './components/nav'
    import Form from './components/form'
     
    export default function Page() {
      return (
        <div>
          <Nav />
          <main>
            <h1>Welcome to the Dashboard</h1>
            <Form />
          </main>
        </div>
      )
    }
[/code]

사용자가 폼에 저장되지 않은 변경 사항이 있는 상태에서 `CustomLink`를 통해 다른 페이지로 이동하려고 하면, 떠나기 전에 확인하라는 메시지가 표시됩니다.

## 버전 기록[](https://nextjs.org/docs/app/api-reference/components/link#version-history)

Version| Changes  
---|---  
`v15.4.0`| 기본 `prefetch` 동작의 별칭으로 `auto`를 추가했습니다.  
`v15.3.0`| `onNavigate` API를 추가했습니다.  
`v13.0.0`| 더 이상 자식 `<a>` 태그가 필요하지 않습니다. 코드베이스를 자동으로 업데이트하는 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#remove-a-tags-from-link-components)가 제공됩니다.  
`v10.0.0`| 동적 라우트를 가리키는 `href` prop이 자동으로 해석되며 더 이상 `as` prop이 필요하지 않습니다.  
`v8.0.0`| 프리페치 성능이 향상되었습니다.  
`v1.0.0`| `next/link`가 도입되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
