---
title: '함수: useSearchParams'
description: '는 현재 URL의 query string을 읽을 수 있게 해 주는 Client Component 훅입니다.'
---

# 함수: useSearchParams | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/use-search-params

Copy page

# useSearchParams

최종 업데이트 2026년 2월 20일

`useSearchParams`는 현재 URL의 **query string**을 읽을 수 있게 해 주는 **Client Component** 훅입니다.

`useSearchParams`는 [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) 인터페이스의 **읽기 전용** 버전을 반환합니다.

app/dashboard/search-bar.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useSearchParams } from 'next/navigation'

    export default function SearchBar() {
      const searchParams = useSearchParams()

      const search = searchParams.get('search')

      // URL -> `/dashboard?search=my-project`
      // `search` -> 'my-project'
      return <>Search: {search}</>
    }
[/code]

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#parameters)
[code]
    const searchParams = useSearchParams()
[/code]

`useSearchParams`는 어떤 매개변수도 받지 않습니다.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#returns)

`useSearchParams`는 URL의 query string을 읽기 위한 유틸리티 메서드를 포함하는 [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) 인터페이스의 **읽기 전용** 버전을 반환합니다:

  * [`URLSearchParams.get()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/get): 검색 매개변수에 연결된 첫 번째 값을 반환합니다. 예시:

URL| `searchParams.get("a")`
---|---
`/dashboard?a=1`| `'1'`
`/dashboard?a=`| `''`
`/dashboard?b=3`| `null`
`/dashboard?a=1&a=2`| `'1'` _\- 모든 값을 얻으려면 [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll)을 사용하세요_

  * [`URLSearchParams.has()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/has): 주어진 매개변수가 존재하는지 여부를 나타내는 불리언 값을 반환합니다. 예시:

URL| `searchParams.has("a")`
---|---
`/dashboard?a=1`| `true`
`/dashboard?b=3`| `false`

  * [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams)의 다른 **읽기 전용** 메서드인 [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll), [`keys()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/keys), [`values()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/values), [`entries()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/entries), [`forEach()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/forEach), [`toString()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/toString)에 대해 더 알아보세요.

> **알아 두면 좋은 점** :
>
>   * `useSearchParams`는 [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) 훅이며 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서는 [부분 렌더링](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) 중 오래된 값을 방지하기 위해 **지원되지 않습니다**.
>   * 검색 매개변수를 기준으로 Server Component에서 데이터를 가져오고 싶다면 해당 페이지의 [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)을 읽는 편이 더 좋습니다. 그런 다음 그 값을 페이지 내의 모든 컴포넌트(서버 또는 클라이언트)에 props로 전달할 수 있습니다.
>   * 애플리케이션에 `/pages` 디렉터리가 포함된 경우 `useSearchParams`는 `ReadonlyURLSearchParams | null`을 반환합니다. `null` 값은 마이그레이션 중 호환성을 위한 것으로, `getServerSideProps`를 사용하지 않는 페이지의 사전 렌더링 동안 검색 매개변수를 알 수 없기 때문입니다.
>

## Behavior[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#behavior)

### Static Rendering[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering)

경로가 [정적으로 렌더링](https://nextjs.org/docs/app/guides/caching#static-rendering)되는 경우 `useSearchParams`를 호출하면 가장 가까운 [`Suspense` 경계](https://nextjs.org/docs/app/api-reference/file-conventions/loading#examples)까지의 Client Component 트리가 클라이언트 사이드 렌더링됩니다.

이를 통해 경로의 일부는 정적으로 렌더링하면서 `useSearchParams`를 사용하는 동적 부분은 클라이언트 사이드로 렌더링할 수 있습니다.

`useSearchParams`를 사용하는 Client Component를 `<Suspense/>` 경계로 감싸는 것을 권장합니다. 이렇게 하면 그 위에 있는 Client Component는 정적으로 렌더링되어 초기 HTML의 일부로 전송됩니다. [예시](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering).

예를 들어:

app/dashboard/search-bar.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useSearchParams } from 'next/navigation'

    export default function SearchBar() {
      const searchParams = useSearchParams()

      const search = searchParams.get('search')

      // This will not be logged on the server when using static rendering
      console.log(search)

      return <>Search: {search}</>
    }
[/code]

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { Suspense } from 'react'
    import SearchBar from './search-bar'

    // This component passed as a fallback to the Suspense boundary
    // will be rendered in place of the search bar in the initial HTML.
    // When the value is available during React hydration the fallback
    // will be replaced with the `<SearchBar>` component.
    function SearchBarFallback() {
      return <>placeholder</>
    }

    export default function Page() {
      return (
        <>
          <nav>
            <Suspense fallback={<SearchBarFallback />}>
              <SearchBar />
            </Suspense>
          </nav>
          <h1>Dashboard</h1>
        </>
      )
    }
[/code]

> **알아 두면 좋은 점** :
>
>   * 개발 중에는 경로가 온디맨드로 렌더링되므로 `useSearchParams`가 suspend되지 않으며 `Suspense` 없이도 동작하는 것처럼 보일 수 있습니다.
>   * 프로덕션 빌드에서는 Client Component에서 `useSearchParams`를 호출하는 [정적 페이지](https://nextjs.org/docs/app/guides/caching#static-rendering)가 반드시 `Suspense` 경계로 감싸져 있어야 하며, 그렇지 않으면 [Missing Suspense boundary with useSearchParams](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout) 오류로 빌드가 실패합니다.
>   * 경로를 동적으로 렌더링할 계획이라면 먼저 Server Component에서 [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection) 함수를 사용하여 들어오는 요청을 기다리는 것이 좋습니다. 이렇게 하면 그 아래 모든 항목이 사전 렌더링에서 제외됩니다. 경로를 동적으로 만드는 요소는 [Dynamic Rendering 가이드](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)에서 확인하세요.
>   * 이미 Server Component Page에 있다면 [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)을 사용하고 값을 Client Component에 전달하는 것을 고려하세요.
>   * Page [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)을 Client Component에 직접 전달하고 React의 `use()`로 풀 수도 있습니다. 이 경우 suspend되므로 Client Component를 `Suspense` 경계로 감싸야 합니다.
>

### Dynamic Rendering[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#dynamic-rendering)

경로가 [동적으로 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)되는 경우 Client Component의 초기 서버 렌더링 동안 서버에서 `useSearchParams`를 사용할 수 있습니다.

예를 들어:

app/dashboard/search-bar.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useSearchParams } from 'next/navigation'

    export default function SearchBar() {
      const searchParams = useSearchParams()

      const search = searchParams.get('search')

      // This will be logged on the server during the initial render
      // and on the client on subsequent navigations.
      console.log(search)

      return <>Search: {search}</>
    }
[/code]

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { connection } from 'next/server'
    import SearchBar from './search-bar'

    export default async function Page() {
      await connection()
      return (
        <>
          <nav>
            <SearchBar />
          </nav>
          <h1>Dashboard</h1>
        </>
      )
    }
[/code]

> **알아 두면 좋은 점** :
>
>   * 이전에는 페이지에서 `export const dynamic = 'force-dynamic'`을 설정하여 동적 렌더링을 강제했습니다. 이제는 동적 렌더링을 들어오는 요청과 의미적으로 연결해 주는 [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection)을 사용하는 것이 좋습니다.
>

### Server Components[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#server-components)

#### Pages[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#pages)

[Pages](https://nextjs.org/docs/app/api-reference/file-conventions/page) (Server Components)에서 검색 매개변수에 접근하려면 [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) prop을 사용하세요.

#### Layouts[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#layouts)

Pages와 달리 [Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout) (Server Components)은 `searchParams` prop을 **받지 않습니다**. 공유 레이아웃은 [내비게이션 중 다시 렌더링되지](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) 않기 때문에 내비게이션 사이에 오래된 `searchParams`가 남을 수 있습니다. [자세한 설명](https://nextjs.org/docs/app/api-reference/file-conventions/layout#query-params)을 확인하세요.

대신 Page [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page) prop이나 최신 `searchParams`로 클라이언트에서 다시 렌더링되는 Client Component의 [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) 훅을 사용하세요.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#examples)

### Updating `searchParams`[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#updating-searchparams)

[`useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router) 또는 [`Link`](https://nextjs.org/docs/app/api-reference/components/link)를 사용하여 새로운 `searchParams`를 설정할 수 있습니다. 내비게이션이 수행된 후 현재 [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page)는 업데이트된 [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)을 받게 됩니다.

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'

    export default function ExampleClientComponent() {
      const router = useRouter()
      const pathname = usePathname()
      const searchParams = useSearchParams()

      // Get a new searchParams string by merging the current
      // searchParams with a provided key/value pair
      const createQueryString = useCallback(
        (name: string, value: string) => {
          const params = new URLSearchParams(searchParams.toString())
          params.set(name, value)

          return params.toString()
        },
        [searchParams]
      )

      return (
        <>
          <p>Sort By</p>

          {/* using useRouter */}
          <button
            onClick={() => {
              // <pathname>?sort=asc
              router.push(pathname + '?' + createQueryString('sort', 'asc'))
            }}
          >
            ASC

</button>

          {/* using <Link> */}
          <Link
            href={
              // <pathname>?sort=desc
              pathname + '?' + createQueryString('sort', 'desc')
            }
          >
            DESC
          </Link>
        </>
      )
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#version-history)

Version| 변경 사항
---|---
`v13.0.0`| `useSearchParams` 도입.
