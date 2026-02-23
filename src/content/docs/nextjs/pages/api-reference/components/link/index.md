---
title: '컴포넌트: Link'
description: '은 HTML  요소를 확장하여 prefetching과 라우트 간 클라이언트 내비게이션을 제공하는 React 컴포넌트입니다. Next.js에서 라우트 간 이동을 수행하는 기본 수단입니다.'
---

# 컴포넌트: Link | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/components/link

# Link

마지막 업데이트: 2026년 2월 20일

`<Link>`은 HTML `<a>` 요소를 확장하여 [prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)과 라우트 간 클라이언트 내비게이션을 제공하는 React 컴포넌트입니다. Next.js에서 라우트 간 이동을 수행하는 기본 수단입니다.

기본 사용법:

pages/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function Home() {
      return <Link href="/dashboard">Dashboard</Link>
    }
[/code]

## Reference[](https://nextjs.org/docs/pages/api-reference/components/link#reference)

다음 프로퍼티를 `<Link>` 컴포넌트에 전달할 수 있습니다.

Prop| Example| Type| Required
---|---|---|---
[`href`](https://nextjs.org/docs/pages/api-reference/components/link#href-required)| `href="/dashboard"`| String or Object| Yes
[`as`](https://nextjs.org/docs/pages/api-reference/components/link#as)| `as="/post/abc"`| String or Object| -
[`replace`](https://nextjs.org/docs/pages/api-reference/components/link#replace)| `replace={false}`| Boolean| -
[`scroll`](https://nextjs.org/docs/pages/api-reference/components/link#scroll)| `scroll={false}`| Boolean| -
[`prefetch`](https://nextjs.org/docs/pages/api-reference/components/link#prefetch)| `prefetch={false}`| Boolean| -
[`shallow`](https://nextjs.org/docs/pages/api-reference/components/link#shallow)| `shallow={false}`| Boolean| -
[`locale`](https://nextjs.org/docs/pages/api-reference/components/link#locale)| `locale="fr"`| String or Boolean| -
[`onNavigate`](https://nextjs.org/docs/pages/api-reference/components/link#onnavigate)| `onNavigate={(e) => {}}`| Function| -

> **알아두면 좋은 사항** : `className` 또는 `target="_blank"`와 같은 `<a>` 태그 속성을 `<Link>`에 프로퍼티로 추가하면 기본 `<a>` 요소로 전달됩니다.

### `href` (required)[](https://nextjs.org/docs/pages/api-reference/components/link#href-required)

이동할 경로나 URL입니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    // Navigate to /about?name=test
    export default function Home() {
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

### `replace`[](https://nextjs.org/docs/pages/api-reference/components/link#replace)

**기본값은`false`입니다.** `true`이면 `next/link`가 [브라우저 기록](https://developer.mozilla.org/docs/Web/API/History_API) 스택에 새 URL을 추가하는 대신 현재 기록 상태를 교체합니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function Home() {
      return (
        <Link href="/dashboard" replace>
          Dashboard
        </Link>
      )
    }
[/code]

### `scroll`[](https://nextjs.org/docs/pages/api-reference/components/link#scroll)

**기본값은`true`입니다.** Next.js의 `<Link>` 기본 스크롤 동작은 브라우저의 뒤로/앞으로 이동과 비슷하게 **스크롤 위치를 유지**하는 것입니다. 새 [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page)로 이동할 때 Page가 뷰포트에 보이는 한 스크롤 위치가 유지됩니다. 그러나 Page가 뷰포트에 보이지 않으면 Next.js는 첫 번째 Page 요소의 최상단으로 스크롤합니다.

`scroll = {false}`이면 Next.js는 첫 번째 Page 요소로 스크롤하지 않습니다.

> **알아두면 좋은 사항** : Next.js는 스크롤 동작을 제어하기 전에 `scroll: false`인지 확인합니다. 스크롤이 활성화되어 있으면 탐색 대상 DOM 노드를 식별한 뒤 최상위 요소를 검사합니다. 스크롤할 수 없거나 렌더링된 HTML이 없는 요소(스티키/고정 위치 요소, `getBoundingClientRect`로 계산되는 비가시 요소 등)는 건너뛰며, 뷰포트에 보이는 스크롤 가능한 요소를 찾을 때까지 형제 요소를 계속 탐색합니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function Home() {
      return (
        <Link href="/dashboard" scroll={false}>
          Dashboard
        </Link>
      )
    }
[/code]

### `prefetch`[](https://nextjs.org/docs/pages/api-reference/components/link#prefetch)

`<Link />` 컴포넌트가 사용자 뷰포트에 들어오면(최초 렌더 또는 스크롤로) 프리패칭이 발생합니다. Next.js는 `href`가 가리키는 라우트와 데이터를 백그라운드에서 미리 로드하여 클라이언트 내비게이션 성능을 향상시킵니다. **프리패칭은 프로덕션에서만 활성화됩니다.**

`prefetch` 프로퍼티에는 다음 값을 전달할 수 있습니다.

  * **`true` (default)**: 라우트 전체와 해당 데이터가 프리패칭됩니다.
  * `false`: 뷰포트에 진입할 때는 프리패칭하지 않지만, 호버 시에는 진행됩니다. 호버 시에도 완전히 비활성화하려면 `<a>` 태그를 사용하거나 프리패칭을 호버에서도 끌 수 있는 App Router를 [점진적으로 도입](https://nextjs.org/docs/app/guides/migrating/app-router-migration)하는 것을 고려하세요.

pages/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function Home() {
      return (
        <Link href="/dashboard" prefetch={false}>
          Dashboard
        </Link>
      )
    }
[/code]

### `shallow`[](https://nextjs.org/docs/pages/api-reference/components/link#shallow)

[`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props), [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props), [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props)를 다시 실행하지 않고 현재 페이지의 경로만 갱신합니다. 기본값은 `false`입니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function Home() {
      return (
        <Link href="/dashboard" shallow={false}>
          Dashboard
        </Link>
      )
    }
[/code]

### `locale`[](https://nextjs.org/docs/pages/api-reference/components/link#locale)

활성 로케일이 자동으로 접두사로 붙습니다. `locale`은 다른 로케일을 지정할 수 있습니다. `false`이면 기본 동작이 비활성화되므로 `href`에 로케일을 포함해야 합니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function Home() {
      return (
        <>
          {/* Default behavior: locale is prepended */}
          <Link href="/dashboard">Dashboard (with locale)</Link>

          {/* Disable locale prepending */}
          <Link href="/dashboard" locale={false}>
            Dashboard (without locale)
          </Link>

          {/* Specify a different locale */}
          <Link href="/dashboard" locale="fr">
            Dashboard (French)
          </Link>
        </>
      )
    }
[/code]

### `as`[](https://nextjs.org/docs/pages/api-reference/components/link#as)

브라우저 URL 바에 표시할 경로를 위한 선택적 데코레이터입니다. Next.js 9.5.3 이전에는 동적 라우트를 위해 사용되었으니, 동작 방식은 [이전 문서](https://github.com/vercel/next.js/blob/v9.5.2/docs/api-reference/next/link.md#dynamic-routes)를 참고하세요.

이 경로가 `href`와 다르면 [이전 문서](https://github.com/vercel/next.js/blob/v9.5.2/docs/api-reference/next/link.md#dynamic-routes)에 나온 것처럼 기존 `href`/`as` 동작이 사용됩니다.

### `onNavigate`[](https://nextjs.org/docs/pages/api-reference/components/link#onnavigate)

클라이언트 내비게이션 중 호출되는 이벤트 핸들러입니다. `preventDefault()` 메서드가 포함된 이벤트 객체를 받아 필요할 때 내비게이션을 취소할 수 있습니다.

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

> **알아두면 좋은 사항** : `onClick`과 `onNavigate`는 비슷해 보이지만 용도가 다릅니다. `onClick`은 모든 클릭 이벤트에서 실행되지만 `onNavigate`는 클라이언트 측 내비게이션에서만 실행됩니다. 주요 차이점은 다음과 같습니다.
>
>   * 수정 키(`Ctrl`/`Cmd` + 클릭)를 사용할 때 새 탭 내비게이션을 막기 때문에 `onClick`은 실행되지만 `onNavigate`는 실행되지 않습니다.
>   * 외부 URL은 클라이언트 측/동일 출처 내비게이션이 아니므로 `onNavigate`를 트리거하지 않습니다.
>   * `download` 속성이 있는 링크는 브라우저가 다운로드로 처리하므로 `onClick`과는 동작하지만 `onNavigate`와는 동작하지 않습니다.
>

## Examples[](https://nextjs.org/docs/pages/api-reference/components/link#examples)

다음 예제는 다양한 시나리오에서 `<Link>` 컴포넌트를 사용하는 방법을 보여줍니다.

### Linking to dynamic route segments[](https://nextjs.org/docs/pages/api-reference/components/link#linking-to-dynamic-route-segments-1)

[동적 라우트 세그먼트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention)에는 템플릿 리터럴로 링크 경로를 생성하는 것이 편리합니다.

예를 들어 동적 라우트 `pages/blog/[slug].js`에 대한 링크 목록을 생성할 수 있습니다.

pages/blog/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    function Posts({ posts }) {
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

### Scrolling to an `id`[](https://nextjs.org/docs/pages/api-reference/components/link#scrolling-to-an-id)

내비게이션 시 특정 `id`로 스크롤하려면 URL에 `#` 해시 링크를 추가하거나 `href` 프로퍼티에 해시 링크만 전달하면 됩니다. `<Link>`가 `<a>` 요소로 렌더링되기 때문에 가능합니다.
[code]
    <Link href="/dashboard#settings">Settings</Link>

    // Output
    <a href="/dashboard#settings">Settings</a>
[/code]

### Passing a URL Object[](https://nextjs.org/docs/pages/api-reference/components/link#passing-a-url-object)

`Link`는 URL 객체를 받을 수 있으며, 이를 자동으로 포맷해 URL 문자열을 생성합니다.

pages/index.ts

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    function Home() {
      return (
        <ul>
          <li>
            <Link
              href={{
                pathname: '/about',
                query: { name: 'test' },
              }}
            >
              About us
            </Link>
          </li>
          <li>
            <Link
              href={{
                pathname: '/blog/[slug]',
                query: { slug: 'my-post' },
              }}
            >
              Blog Post
            </Link>
          </li>
        </ul>
      )
    }

    export default Home
[/code]

위 예제에는 다음 링크가 포함되어 있습니다.

  * 미리 정의된 라우트: `/about?name=test`
  * [동적 라우트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention): `/blog/my-post`

[Node.js URL 모듈 문서](https://nodejs.org/api/url.html#url_url_strings_and_url_objects)에 정의된 모든 속성을 사용할 수 있습니다.

### Replace the URL instead of push[](https://nextjs.org/docs/pages/api-reference/components/link#replace-the-url-instead-of-push)

`Link` 컴포넌트의 기본 동작은 새 URL을 `history` 스택에 `push`하는 것입니다. 아래 예시처럼 `replace` prop을 사용하면 새 항목이 추가되지 않도록 할 수 있습니다:

pages/index.js

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function Home() {
      return (
        <Link href="/about" replace>
          About us
        </Link>
      )
    }
[/code]

### 페이지 맨 위로 스크롤되는 동작 비활성화[](https://nextjs.org/docs/pages/api-reference/components/link#disable-scrolling-to-the-top-of-the-page)

`Link`의 기본 동작은 페이지 맨 위로 스크롤하는 것입니다. 해시가 정의되어 있으면 일반 `<a>` 태그처럼 특정 id로 스크롤합니다. 페이지 상단/해시로 스크롤되지 않도록 하려면 `Link`에 `scroll={false}`를 추가하면 됩니다:

pages/index.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function Home() {
      return (
        <Link href="/#hashid" scroll={false}>
          Disables scrolling to the top
        </Link>
      )
    }
[/code]

### Proxy에서 링크 미리 가져오기[](https://nextjs.org/docs/pages/api-reference/components/link#prefetching-links-in-proxy)

사용자를 다른 페이지로 리라이트해야 하는 인증 등 목적을 위해 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 사용하는 것이 흔합니다. Proxy를 통한 리라이트와 함께 `<Link />` 컴포넌트가 링크를 제대로 미리 가져오게 하려면, Next.js에 표시할 URL과 미리 가져올 URL을 모두 알려야 합니다. 이렇게 해야 올바른 프리페치 경로를 알기 위해 Proxy로 불필요한 페치를 보내지 않습니다.

예를 들어, 인증 사용자와 방문자용 뷰를 모두 제공하는 `/dashboard` 라우트를 서비스하려면 Proxy에 다음 코드를 추가하여 사용자를 올바른 페이지로 리디렉션할 수 있습니다:

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

pages/index.tsx

JavaScriptTypeScript
[code]
    'use client'

    import Link from 'next/link'
    import useIsAuthed from './hooks/useIsAuthed' // Your auth hook

    export default function Home() {
      const isAuthed = useIsAuthed()
      const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
      return (
        <Link as="/dashboard" href={path}>
          Dashboard
        </Link>
      )
    }
[/code]

> **알아두면 좋아요**: [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention)를 사용하는 경우 `as`와 `href` props를 조정해야 합니다. 예를 들어 `/dashboard/authed/[user]`처럼 Proxy를 통해 다르게 보여주고 싶은 Dynamic Route가 있다면 `<Link href={{ pathname: '/dashboard/authed/[user]', query: { user: username } }} as="/dashboard/[user]">Profile</Link>`처럼 작성합니다.

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/components/link#version-history)

Version| Changes
---|---
`v15.4.0`| 기본 `prefetch` 동작에 대한 `auto` 별칭 추가.
`v15.3.0`| `onNavigate` API 추가
`v13.0.0`| 더 이상 자식 `<a>` 태그가 필요하지 않음. 코드베이스를 자동으로 업데이트할 수 있는 [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#remove-a-tags-from-link-components)가 제공됨.
`v10.0.0`| 동적 라우트를 가리키는 `href` props가 자동으로 해석되어 `as` prop이 더는 필요하지 않음.
`v8.0.0`| 프리페치 성능 향상.
`v1.0.0`| `next/link` 도입.

보내기
