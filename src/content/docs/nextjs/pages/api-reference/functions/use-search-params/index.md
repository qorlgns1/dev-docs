---
title: '함수: useSearchParams'
description: '는 현재 URL의 쿼리 문자열을 읽을 수 있게 해 주는 훅입니다.'
---

# 함수: useSearchParams | Next.js

소스 URL: https://nextjs.org/docs/pages/api-reference/functions/use-search-params

# useSearchParams

마지막 업데이트 2026년 2월 20일

`useSearchParams`는 현재 URL의 **쿼리 문자열**을 읽을 수 있게 해 주는 훅입니다.

`useSearchParams`는 [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) 인터페이스의 **읽기 전용** 버전을 반환합니다.

pages/dashboard.tsx

JavaScriptTypeScript
[code]
    import { useSearchParams } from 'next/navigation'

    export default function Dashboard() {
      const searchParams = useSearchParams()

      if (!searchParams) {
        // Render fallback UI while search params are not yet available
        return null
      }

      const search = searchParams.get('search')

      // URL -> `/dashboard?search=my-project`
      // `search` -> 'my-project'
      return <>Search: {search}</>
    }
[/code]

## 매개변수[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#parameters)
[code]
    const searchParams = useSearchParams()
[/code]

`useSearchParams`는 어떠한 매개변수도 받지 않습니다.

## 반환값[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#returns)

`useSearchParams`는 [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) 인터페이스의 **읽기 전용** 버전 또는 [사전 렌더링](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#behavior-during-pre-rendering) 중에는 `null`을 반환합니다.

이 인터페이스에는 URL의 쿼리 문자열을 읽기 위한 유틸리티 메서드가 포함되어 있습니다.

  * [`URLSearchParams.get()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/get): 검색 매개변수와 연결된 첫 번째 값을 반환합니다. 예:

URL| `searchParams.get("a")`
---|---
`/dashboard?a=1`| `'1'`
`/dashboard?a=`| `''`
`/dashboard?b=3`| `null`
`/dashboard?a=1&a=2`| `'1'` _\- 모든 값을 가져오려면 [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll) 사용_

  * [`URLSearchParams.has()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/has): 주어진 매개변수가 존재하는지 나타내는 불리언 값을 반환합니다. 예:

URL| `searchParams.has("a")`
---|---
`/dashboard?a=1`| `true`
`/dashboard?b=3`| `false`

  * [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll), [`keys()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/keys), [`values()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/values), [`entries()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/entries), [`forEach()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/forEach), [`toString()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/toString) 등을 포함한 [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams)의 다른 **읽기 전용** 메서드에 대해 자세히 알아보세요.

> **알아두면 좋아요** : `useSearchParams`는 [React Hook](https://react.dev/learn#using-hooks)이므로 클래스에서는 사용할 수 없습니다.

## 동작[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#behavior)

### 사전 렌더링 중 동작[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#behavior-during-pre-rendering)

[`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)를 사용하지 않는 [정적으로 최적화된](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) 페이지의 경우, `useSearchParams`는 사전 렌더링 중에 `null`을 반환합니다. 하이드레이션 후 실제 검색 매개변수 값으로 업데이트됩니다.

이는 검색 매개변수가 요청에 따라 달라지므로 정적 생성 동안에는 알 수 없기 때문입니다.

pages/dashboard.tsx

JavaScriptTypeScript
[code]
    import { useSearchParams } from 'next/navigation'

    export default function Dashboard() {
      const searchParams = useSearchParams()

      if (!searchParams) {
        // Return a fallback UI while search params are loading
        // This prevents hydration mismatches
        return <DashboardSkeleton />
      }

      const search = searchParams.get('search')

      return <>Search: {search}</>
    }
[/code]

### `getServerSideProps`와 함께 사용[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#using-with-getserversideprops)

[`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)를 사용할 때 페이지는 각 요청마다 서버 렌더링되며 `useSearchParams`가 즉시 실제 검색 매개변수를 반환합니다.

pages/dashboard.tsx

JavaScriptTypeScript
[code]
    import { useSearchParams } from 'next/navigation'

    export default function Dashboard() {
      const searchParams = useSearchParams()

      // With getServerSideProps, this fallback is never rendered because
      // searchParams is always available on the server. However, keeping
      // the fallback allows this component to be reused on other pages
      // that may not use getServerSideProps.
      if (!searchParams) {
        return null
      }

      const search = searchParams.get('search')

      return <>Search: {search}</>
    }

    export async function getServerSideProps() {
      return { props: {} }
    }
[/code]

## 예시[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#examples)

### 검색 매개변수 업데이트[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#updating-search-params)

[`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router) 훅을 사용해 검색 매개변수를 업데이트할 수 있습니다.

pages/dashboard.tsx

JavaScriptTypeScript
[code]
    import { useRouter } from 'next/router'
    import { useSearchParams } from 'next/navigation'
    import { useCallback } from 'react'

    export default function Dashboard() {
      const router = useRouter()
      const searchParams = useSearchParams()

      const createQueryString = useCallback(
        (name: string, value: string) => {
          const params = new URLSearchParams(searchParams?.toString())
          params.set(name, value)
          return params.toString()
        },
        [searchParams]
      )

      if (!searchParams) {
        return null
      }

      return (
        <>
          <p>Sort By</p>
          <button
            onClick={() => {
              router.push(router.pathname + '?' + createQueryString('sort', 'asc'))
            }}
          >
            ASC
          </button>
          <button
            onClick={() => {
              router.push(router.pathname + '?' + createQueryString('sort', 'desc'))
            }}
          >
            DESC
          </button>
        </>
      )
    }
[/code]

### App Router와 컴포넌트 공유[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#sharing-components-with-app-router)

`next/navigation`의 `useSearchParams`는 Pages Router와 App Router 모두에서 작동합니다. 덕분에 어느 컨텍스트에서도 동작하는 공유 컴포넌트를 만들 수 있습니다.

components/search-bar.tsx

JavaScriptTypeScript
[code]
    import { useSearchParams } from 'next/navigation'

    // This component works in both pages/ and app/
    export function SearchBar() {
      const searchParams = useSearchParams()

      if (!searchParams) {
        // Fallback for Pages Router during pre-rendering
        return <input defaultValue="" placeholder="Search..." />
      }

      const search = searchParams.get('search') ?? ''

      return <input defaultValue={search} placeholder="Search..." />
    }
[/code]

> **알아두면 좋아요** : App Router에서 이 컴포넌트를 사용할 때는 [정적 렌더링](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering)을 지원하려면 `<Suspense>` 경계로 감싸세요.

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#version-history)

버전| 변경 사항
---|---
`v13.0.0`| `useSearchParams` 도입.

보내기
