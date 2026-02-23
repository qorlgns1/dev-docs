---
title: '함수: useRouter'
description: '훅을 사용하면 클라이언트 컴포넌트 내부에서 라우트를 프로그래밍 방식으로 변경할 수 있습니다.'
---

# 함수: useRouter | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/use-router

# useRouter

최종 업데이트 2026년 2월 20일

`useRouter` 훅을 사용하면 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 내부에서 라우트를 프로그래밍 방식으로 변경할 수 있습니다.

> **권장 사항:** 특별히 `useRouter`를 사용해야 하는 요구 사항이 없다면 내비게이션에는 [`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)를 사용하세요.

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useRouter } from 'next/navigation'

    export default function Page() {
      const router = useRouter()

      return (
        <button type="button" onClick={() => router.push('/dashboard')}>
          Dashboard
        </button>
      )
    }
[/code]

## `useRouter()`[](https://nextjs.org/docs/app/api-reference/functions/use-router#userouter)

  * `router.push(href: string, { scroll: boolean })`: 제공된 라우트로 클라이언트 사이드 내비게이션을 수행합니다. [브라우저 기록 스택](https://developer.mozilla.org/docs/Web/API/History_API)에 새 항목을 추가합니다.
  * `router.replace(href: string, { scroll: boolean })`: 브라우저 기록 스택에 새 항목을 추가하지 않고 제공된 라우트로 클라이언트 사이드 내비게이션을 수행합니다.
  * `router.refresh()`: 현재 라우트를 새로고침합니다. 서버에 새 요청을 보내고 데이터를 다시 가져와 서버 컴포넌트를 다시 렌더링합니다. 클라이언트는 영향을 받지 않은 클라이언트 사이드 React 상태(예: `useState`)나 브라우저 상태(예: 스크롤 위치)를 잃지 않고 업데이트된 React 서버 컴포넌트 페이로드를 병합합니다.
  * `router.prefetch(href: string, options?: { onInvalidate?: () => void })`: 더 빠른 클라이언트 사이드 전환을 위해 제공된 라우트를 [프리페치](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)합니다. 선택적 `onInvalidate` 콜백은 [프리페치된 데이터가 오래될 때](https://nextjs.org/docs/app/guides/prefetching#extending-or-ejecting-link) 호출됩니다.
  * `router.back()`: 브라우저 기록 스택에서 이전 라우트로 이동합니다.
  * `router.forward()`: 브라우저 기록 스택에서 다음 페이지로 이동합니다.

> **알아두면 좋은 점** :
>
>   * 신뢰할 수 없거나 정제되지 않은 URL을 `router.push` 또는 `router.replace`에 전달하면 사이트가 XSS 취약점에 노출될 수 있으므로 절대 전달하지 마세요. 예를 들어 `router.push` 또는 `router.replace`에 전달된 `javascript:` URL은 페이지 컨텍스트에서 실행됩니다.
>   * `<Link>` 컴포넌트는 뷰포트에 보이는 즉시 라우트를 자동으로 프리페치합니다.
>   * 페치 요청이 캐시된 경우 `refresh()`는 동일한 결과를 다시 생성할 수 있습니다. `cookies`와 `headers`와 같은 다른 동적 API도 응답을 변경할 수 있습니다.
>   * `onInvalidate` 콜백은 프리페치 요청당 최대 한 번 호출됩니다. 이는 업데이트된 라우트 데이터를 위해 새 프리페치를 트리거해야 할 시점을 알리는 신호입니다.
>

### `next/router`에서 마이그레이션[](https://nextjs.org/docs/app/api-reference/functions/use-router#migrating-from-nextrouter)

  * App Router를 사용할 때는 `useRouter` 훅을 `next/router`가 아니라 `next/navigation`에서 가져와야 합니다.
  * `pathname` 문자열이 제거되었으며 [`usePathname()`](https://nextjs.org/docs/app/api-reference/functions/use-pathname)으로 대체되었습니다.
  * `query` 객체가 제거되었으며 [`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)로 대체되었습니다.
  * `router.events`가 교체되었습니다. [아래를 참고하세요.](https://nextjs.org/docs/app/api-reference/functions/use-router#router-events)

[전체 마이그레이션 가이드 보기](https://nextjs.org/docs/app/guides/migrating/app-router-migration).

## 예제[](https://nextjs.org/docs/app/api-reference/functions/use-router#examples)

### 라우터 이벤트[](https://nextjs.org/docs/app/api-reference/functions/use-router#router-events)

`usePathname`과 `useSearchParams` 같은 다른 클라이언트 컴포넌트 훅을 조합하여 페이지 변경을 감지할 수 있습니다.

app/components/navigation-events.js
[code]
    'use client'

    import { useEffect } from 'react'
    import { usePathname, useSearchParams } from 'next/navigation'

    export function NavigationEvents() {
      const pathname = usePathname()
      const searchParams = useSearchParams()

      useEffect(() => {
        const url = `${pathname}?${searchParams}`
        console.log(url)
        // You can now use the current URL
        // ...
      }, [pathname, searchParams])

      return '...'
    }
[/code]

이를 레이아웃에서 가져와 사용할 수 있습니다.

app/layout.js
[code]
    import { Suspense } from 'react'
    import { NavigationEvents } from './components/navigation-events'

    export default function Layout({ children }) {
      return (
        <html lang="en">
          <body>
            {children}

            <Suspense fallback={null}>
              <NavigationEvents />
            </Suspense>
          </body>
        </html>
      )
    }
[/code]

> **알아두면 좋은 점** : [`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)는 [정적 렌더링](https://nextjs.org/docs/app/guides/caching#static-rendering) 중 가장 가까운 `Suspense` 경계까지 클라이언트 사이드 렌더링을 유발하므로 `<NavigationEvents>`는 [`Suspense` 경계](https://nextjs.org/docs/app/api-reference/file-conventions/loading#examples)로 감싸져 있습니다. [자세히 보기](https://nextjs.org/docs/app/api-reference/functions/use-search-params#behavior).

### 맨 위로 스크롤 비활성화[](https://nextjs.org/docs/app/api-reference/functions/use-router#disabling-scroll-to-top)

기본적으로 Next.js는 새 라우트로 이동할 때 페이지 맨 위로 스크롤합니다. `router.push()` 또는 `router.replace()`에 `scroll: false`를 전달해 이 동작을 비활성화할 수 있습니다.

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useRouter } from 'next/navigation'

    export default function Page() {
      const router = useRouter()

      return (
        <button
          type="button"
          onClick={() => router.push('/dashboard', { scroll: false })}
        >
          Dashboard
        </button>
      )
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/use-router#version-history)

Version| Changes
---|---
`v15.4.0`| `router.prefetch`에 선택적 `onInvalidate` 콜백이 도입됨
`v13.0.0`| `next/navigation`의 `useRouter`가 도입됨.

보내기
