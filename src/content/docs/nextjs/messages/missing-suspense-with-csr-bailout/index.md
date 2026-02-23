---
title: 'useSearchParams에서 Suspense 경계 누락'
description: '원본 URL: https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout'
---

# useSearchParams에서 Suspense 경계 누락 | Next.js

원본 URL: https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)useSearchParams에서 Suspense 경계 누락

# useSearchParams에서 Suspense 경계 누락

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#why-this-error-occurred)

Suspense 경계 없이 `useSearchParams()`를 통해 검색 매개변수를 읽으면 전체 페이지가 클라이언트 측 렌더링으로 전환됩니다. 이로 인해 클라이언트 측 JavaScript가 로드될 때까지 페이지가 비어 보일 수 있습니다.

## 해결할 수 있는 방법[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#possible-ways-to-fix-it)

의도에 따라 다음과 같은 선택지가 있습니다.

  * 라우트를 정적으로 생성된 상태로 유지하려면 `useSearchParams()`를 호출하는 가장 작은 서브트리를 `Suspense`로 감싸세요. 예를 들어 해당 훅 사용을 자식 클라이언트 컴포넌트로 옮기고 그 컴포넌트를 `Suspense`로 감싸 렌더링할 수 있습니다. 이렇게 하면 정적 셸을 유지하고 전체 CSR 포기를 피할 수 있습니다.
  * 라우트를 동적으로 렌더링하려면 서버 컴포넌트(예: 페이지 또는 래핑 레이아웃)에서 [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection) 함수를 사용하세요. 이는 들어오는 요청을 기다리고 그 아래의 모든 내용을 사전 렌더링에서 제외합니다.



app/page.tsx

JavaScriptTypeScript
[code]
    import { connection } from 'next/server'
     
    export default async function Page() {
      await connection()
      return <div>...</div>
    }
[/code]

  * `connection` API가 제공되기 전에는 서버 컴포넌트 `page.tsx` 또는 `layout.tsx`에서 `export const dynamic = 'force-dynamic'`을 설정해 라우트를 온디맨드 렌더링으로 전환했습니다. `'use client'`가 선언된 클라이언트 컴포넌트 `page.tsx`에서 `dynamic`을 설정해도 효과가 없다는 점에 유의하세요.



app/layout.tsx

JavaScriptTypeScript
[code]
    export const dynamic = 'force-dynamic'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return children
    }
[/code]

  * 또는 서버 컴포넌트 페이지에서 `searchParams` 값을 클라이언트 컴포넌트로 내려보낼 수 있습니다. 클라이언트 컴포넌트에서는 React의 `use()`로 이를 풀어낼 수 있으며, 이때 주변에 `Suspense` 경계를 둬야 합니다. [사용 시점 안내](https://nextjs.org/docs/app/getting-started/layouts-and-pages#what-to-use-and-when)를 확인하세요.



app/page.tsx

JavaScriptTypeScript
[code]
    import { Suspense } from 'react'
    import ClientSearch from './client-search'
     
    export default function Page({
      searchParams,
    }: {
      searchParams: Promise<{ q?: string }>
    }) {
      return (
        <Suspense fallback={<>...</>}>
          <ClientSearch searchParams={searchParams} />
        </Suspense>
      )
    }
[/code]

app/client-search.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { use } from 'react'
     
    export default function ClientSearch({
      searchParams,
    }: {
      searchParams: Promise<{ q?: string }>
    }) {
      const params = use(searchParams)
      return <div>Query: {params.q}</div>
    }
[/code]

  * 페이지를 다시 서버 컴포넌트로 만들고 `useSearchParams`를 사용하는 클라이언트 전용 코드를 자식 클라이언트 컴포넌트로 분리하는 방법도 고려하세요.



app/search.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useSearchParams } from 'next/navigation'
    import { Suspense } from 'react'
     
    function Search() {
      const searchParams = useSearchParams()
     
      return <input placeholder="Search..." />
    }
     
    export function Searchbar() {
      return (
        // You could have a loading skeleton as the `fallback` too
        <Suspense>
          <Search />
        </Suspense>
      )
    }
[/code]

## 비활성화[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#disabling)

> **참고**: 이는 Next.js 14.x 버전에서만 사용할 수 있습니다. 14보다 높은 버전을 사용 중이라면 위의 방법으로 문제를 해결하세요.

이 규칙을 비활성화하는 것은 권장하지 않습니다. 그러나 꼭 필요하다면 `next.config.js`에서 `missingSuspenseWithCSRBailout` 옵션을 `false`로 설정해 비활성화할 수 있습니다.

next.config.js
[code]
    module.exports = {
      experimental: {
        missingSuspenseWithCSRBailout: false,
      },
    }
[/code]

이 구성 옵션은 향후 메이저 버전에서 제거될 예정입니다.

## 디버깅[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#debugging)

Suspense 경계 없이 `useSearchParams()`가 사용되는 위치를 찾는 데 어려움이 있다면 다음 명령을 실행해 더 자세한 스택 트레이스를 확인하세요.
[code] 
    next build --debug-prerender
[/code]

그러면 소스 맵이 포함된 난독화되지 않은 스택 트레이스가 제공되어 어떤 컴포넌트와 라우트가 문제를 일으키는지 더 쉽게 파악할 수 있습니다.

## 유용한 링크[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#useful-links)

  * [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)
  * [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection)
  * [동적 렌더링 가이드](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)
  * [사전 렌더링 오류 디버깅](https://nextjs.org/docs/app/api-reference/cli/next#debugging-prerender-errors)



도움이 되었나요?

지원됨.

보내기
