---
title: '가이드: SPAs'
description: 'Next.js는 단일 페이지 애플리케이션(SPA) 구축을 완전히 지원합니다.'
---

# 가이드: SPAs | Next.js
Source URL: https://nextjs.org/docs/app/guides/single-page-applications

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)SPAs

Copy page

# Next.js로 단일 페이지 애플리케이션을 구축하는 방법

Last updated February 20, 2026

Next.js는 단일 페이지 애플리케이션(SPA) 구축을 완전히 지원합니다.

여기에는 프리패칭이 적용된 빠른 라우트 전환, 클라이언트 사이드 데이터 패칭, 브라우저 API 사용, 써드파티 클라이언트 라이브러리 통합, 정적 라우트 생성 등이 모두 포함됩니다.

기존 SPA가 있다면 코드에 큰 변화를 주지 않고 Next.js로 마이그레이션할 수 있으며, 이후 필요에 따라 서버 기능을 점진적으로 추가할 수 있습니다.

## 단일 페이지 애플리케이션이란?[](https://nextjs.org/docs/app/guides/single-page-applications#what-is-a-single-page-application)

SPA의 정의는 다양합니다. 여기서는 “엄격한 SPA”를 다음과 같이 정의합니다.

  * **Client-side rendering (CSR)** : 앱은 하나의 HTML 파일(예: `index.html`)로 제공됩니다. 모든 라우트, 페이지 전환, 데이터 패칭은 브라우저의 JavaScript가 처리합니다.
  * **전체 페이지 새로고침 없음** : 각 라우트마다 새 문서를 요청하는 대신, 클라이언트 사이드 JavaScript가 현재 페이지의 DOM을 조작하고 필요에 따라 데이터를 가져옵니다.



엄격한 SPA는 페이지가 상호작용 가능해지기 전에 많은 양의 JavaScript를 로드해야 하는 경우가 많습니다. 또한 클라이언트 데이터 워터폴을 관리하기도 어렵습니다. Next.js로 SPA를 구축하면 이러한 문제를 해결할 수 있습니다.

## SPA에 Next.js를 사용하는 이유?[](https://nextjs.org/docs/app/guides/single-page-applications#why-use-nextjs-for-spas)

Next.js는 JavaScript 번들을 자동으로 코드 스플리팅하고, 서로 다른 라우트용으로 여러 HTML 진입점을 생성합니다. 이를 통해 클라이언트에서 불필요한 JavaScript 로드를 피하고 번들 크기를 줄이며 더 빠른 페이지 로드를 가능하게 합니다.

[`next/link`](https://nextjs.org/docs/app/api-reference/components/link) 컴포넌트는 라우트를 자동으로 [프리패칭](https://nextjs.org/docs/app/api-reference/components/link#prefetch)하여, 엄격한 SPA 수준의 빠른 페이지 전환을 제공하면서도 URL에 애플리케이션 라우팅 상태를 유지해 링크와 공유에 유리합니다.

Next.js는 정적 사이트나 모든 것이 클라이언트 사이드에서 렌더링되는 엄격한 SPA로 시작할 수 있습니다. 프로젝트가 성장하면 [React Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) 등 필요한 서버 기능을 점진적으로 추가할 수 있습니다.

## 예시[](https://nextjs.org/docs/app/guides/single-page-applications#examples)

SPA를 구축할 때 흔히 사용하는 패턴과 Next.js가 이를 해결하는 방법을 살펴보겠습니다.

### Context Provider 내에서 React의 `use` 사용[](https://nextjs.org/docs/app/guides/single-page-applications#using-reacts-use-within-a-context-provider)

상위 컴포넌트(또는 레이아웃)에서 데이터를 패칭해 Promise를 반환하고, 클라이언트 컴포넌트에서 React의 [`use` API](https://react.dev/reference/react/use)로 값을 언랩하는 방식을 권장합니다.

Next.js는 서버에서 일찍 데이터 패칭을 시작할 수 있습니다. 이 예시에서는 루트 레이아웃이 애플리케이션의 진입점이며, 서버는 즉시 클라이언트로 스트리밍 응답을 시작할 수 있습니다.

데이터 패칭을 루트 레이아웃으로 “호이스팅”하면, 애플리케이션의 다른 컴포넌트보다 앞서 서버에서 요청을 시작합니다. 이렇게 하면 클라이언트 워터폴을 제거하고 클라이언트-서버 간 여러 왕복을 방지할 수 있습니다. 또한 서버가 데이터베이스와 더 가깝거나 이상적으로 공동 배치되어 있다면 성능을 크게 향상할 수 있습니다.

예를 들어 루트 레이아웃에서 Promise를 호출하되, _await 하지 마십시오._

app/layout.tsx

JavaScriptTypeScript
[code]
    import { UserProvider } from './user-provider'
    import { getUser } from './user' // some server-side function
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      let userPromise = getUser() // do NOT await
     
      return (
        <html lang="en">
          <body>
            <UserProvider userPromise={userPromise}>{children}</UserProvider>
          </body>
        </html>
      )
    }
[/code]

단일 Promise를 [지연시켜 Client Component의 prop으로 전달](https://nextjs.org/docs/app/getting-started/fetching-data#streaming-data-with-the-use-api)할 수 있지만, 일반적으로 React 컨텍스트 프로바이더와 함께 사용하는 패턴을 권장합니다. 이렇게 하면 맞춤형 React 훅을 통해 클라이언트 컴포넌트에서 더 쉽게 접근할 수 있습니다.

Promise를 React 컨텍스트 프로바이더로 전달할 수 있습니다.

app/user-provider.ts

JavaScriptTypeScript
[code]
    'use client';
     
    import { createContext, useContext, ReactNode } from 'react';
     
    type User = any;
    type UserContextType = {
      userPromise: Promise<User | null>;
    };
     
    const UserContext = createContext<UserContextType | null>(null);
     
    export function useUser(): UserContextType {
      let context = useContext(UserContext);
      if (context === null) {
        throw new Error('useUser must be used within a UserProvider');
      }
      return context;
    }
     
    export function UserProvider({
      children,
      userPromise
    }: {
      children: ReactNode;
      userPromise: Promise<User | null>;
    }) {
      return (
        <UserContext.Provider value={{ userPromise }}>
          {children}
        </UserContext.Provider>
      );
    }
[/code]

마지막으로 임의의 클라이언트 컴포넌트에서 `useUser()` 커스텀 훅을 호출해 Promise를 언랩할 수 있습니다.

app/profile.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { use } from 'react'
    import { useUser } from './user-provider'
     
    export function Profile() {
      const { userPromise } = useUser()
      const user = use(userPromise)
     
      return '...'
    }
[/code]

Promise를 소비하는 컴포넌트(예: 위의 `Profile`)는 서스펜드됩니다. 이를 통해 부분 하이드레이션이 가능하며, JavaScript 로딩이 완료되기 전에 스트리밍 및 프리렌더된 HTML을 볼 수 있습니다.

### SWR을 사용하는 SPA[](https://nextjs.org/docs/app/guides/single-page-applications#spas-with-swr)

[SWR](https://swr.vercel.app)은 데이터 패칭을 위한 인기 있는 React 라이브러리입니다.

SWR 2.3.0(및 React 19+)에서는 기존 SWR 기반 클라이언트 데이터 패칭 코드와 함께 서버 기능을 점진적으로 도입할 수 있습니다. 이는 앞서 설명한 `use()` 패턴의 추상화입니다. 즉, 데이터 패칭을 클라이언트와 서버 사이에서 이동하거나 둘 다 사용할 수 있습니다.

  * **클라이언트 전용:** `useSWR(key, fetcher)`
  * **서버 전용:** `useSWR(key)` \+ RSC가 제공하는 데이터
  * **혼합:** `useSWR(key, fetcher)` \+ RSC가 제공하는 데이터



예를 들어 애플리케이션을 `<SWRConfig>`와 `fallback`으로 감쌀 수 있습니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import { SWRConfig } from 'swr'
    import { getUser } from './user' // some server-side function
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <SWRConfig
          value={{
            fallback: {
              // We do NOT await getUser() here
              // Only components that read this data will suspend
              '/api/user': getUser(),
            },
          }}
        >
          {children}
        </SWRConfig>
      )
    }
[/code]

이것이 서버 컴포넌트이므로 `getUser()`는 쿠키, 헤더를 안전하게 읽거나 데이터베이스와 통신할 수 있습니다. 별도의 API 라우트가 필요하지 않습니다. `<SWRConfig>` 아래의 클라이언트 컴포넌트는 동일한 키로 `useSWR()`를 호출해 사용자 데이터를 가져올 수 있습니다. `useSWR`를 사용하는 컴포넌트 코드는 기존 클라이언트 패칭 방식에서 **아무런 변경도 필요 없습니다.**

app/profile.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import useSWR from 'swr'
     
    export function Profile() {
      const fetcher = (url) => fetch(url).then((res) => res.json())
      // The same SWR pattern you already know
      const { data, error } = useSWR('/api/user', fetcher)
     
      return '...'
    }
[/code]

`fallback` 데이터는 프리렌더되어 초기 HTML 응답에 포함될 수 있으며, 이후 자식 컴포넌트에서 `useSWR`를 사용해 즉시 읽을 수 있습니다. SWR의 폴링, 재검증, 캐싱은 여전히 **클라이언트 사이드에서만** 실행되므로 SPA에서 의존하던 모든 상호작용성을 그대로 유지합니다.

초기 `fallback` 데이터를 Next.js가 자동 처리하므로, 이전에 `data`가 `undefined`인지 확인하던 조건부 로직을 삭제해도 됩니다. 데이터가 로딩 중이면 가장 가까운 `<Suspense>` 경계가 서스펜드됩니다.

| SWR| RSC| RSC + SWR  
---|---|---|---  
SSR data| | |   
Streaming while SSR| | |   
Deduplicate requests| | |   
Client-side features| | |   
  
### React Query를 사용하는 SPA[](https://nextjs.org/docs/app/guides/single-page-applications#spas-with-react-query)

React Query를 Next.js에서 클라이언트와 서버 모두와 함께 사용할 수 있습니다. 이를 통해 엄격한 SPA를 구축하는 동시에 React Query와 함께 Next.js 서버 기능을 활용할 수 있습니다.

자세한 내용은 [React Query 문서](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr)에서 확인하세요.

### 브라우저에서만 컴포넌트 렌더링[](https://nextjs.org/docs/app/guides/single-page-applications#rendering-components-only-in-the-browser)

클라이언트 컴포넌트는 `next build` 중에 [프리렌더](https://github.com/reactwg/server-components/discussions/4)됩니다. 클라이언트 컴포넌트의 프리렌더링을 비활성화하고 브라우저 환경에서만 로드하려면 [`next/dynamic`](https://nextjs.org/docs/app/guides/lazy-loading#nextdynamic)을 사용할 수 있습니다.
[code] 
    import dynamic from 'next/dynamic'
     
    const ClientOnlyComponent = dynamic(() => import('./component'), {
      ssr: false,
    })
[/code]

이는 `window`나 `document` 같은 브라우저 API에 의존하는 써드파티 라이브러리에 유용합니다. 이러한 API 존재 여부를 확인하는 `useEffect`를 추가하고, 존재하지 않으면 `null`이나 프리렌더될 로딩 상태를 반환하도록 할 수도 있습니다.

### 클라이언트에서 얕은 라우팅[](https://nextjs.org/docs/app/guides/single-page-applications#shallow-routing-on-the-client)

[Create React App](https://nextjs.org/docs/app/guides/migrating/from-create-react-app)이나 [Vite](https://nextjs.org/docs/app/guides/migrating/from-vite) 같은 엄격한 SPA에서 마이그레이션하는 경우, URL 상태를 업데이트하기 위해 얕은 라우팅을 수행하는 기존 코드가 있을 수 있습니다. 이는 Next.js 기본 파일 시스템 라우팅을 사용하지 않고도 애플리케이션 내 뷰 사이를 수동으로 전환할 때 유용합니다.

Next.js에서는 페이지를 새로고침하지 않고 브라우저의 히스토리 스택을 업데이트하기 위해 네이티브 [`window.history.pushState`](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState)와 [`window.history.replaceState`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState) 메서드를 사용할 수 있습니다.

`pushState`와 `replaceState` 호출은 Next.js Router와 통합되어 [`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) 및 [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)와 동기화됩니다.
[code] 
    'use client'
     
    import { useSearchParams } from 'next/navigation'
     
    export default function SortProducts() {
      const searchParams = useSearchParams()
     
      function updateSorting(sortOrder: string) {
        const urlSearchParams = new URLSearchParams(searchParams.toString())
        urlSearchParams.set('sort', sortOrder)
        window.history.pushState(null, '', `?${urlSearchParams.toString()}`)
      }
     
      return (
        <>
          <button onClick={() => updateSorting('asc')}>Sort Ascending</button>
          <button onClick={() => updateSorting('desc')}>Sort Descending</button>
        </>
      )
    }
[/code]

Next.js에서 [routing and navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating#how-navigation-works)이 어떻게 작동하는지 더 알아보세요.

### 클라이언트 컴포넌트에서 서버 액션 사용하기[](https://nextjs.org/docs/app/guides/single-page-applications#using-server-actions-in-client-components)

클라이언트 컴포넌트를 계속 사용하면서도 서버 액션을 점진적으로 도입할 수 있습니다. 이를 통해 API 라우트를 호출하는 보일러플레이트 코드를 제거하고, 대신 로딩 및 오류 상태를 처리하기 위해 `useActionState`와 같은 React 기능을 사용할 수 있습니다.

예를 들어, 첫 번째 서버 액션을 만들어 보세요:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    export async function create() {}
[/code]

서버 액션은 클라이언트에서 일반 자바스크립트 함수를 호출하듯 가져와 사용할 수 있습니다. API 엔드포인트를 수동으로 만들 필요가 없습니다:

app/button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { create } from './actions'
     
    export function Button() {
      return <button onClick={() => create()}>Create</button>
    }
[/code]

[서버 액션으로 데이터 변경](https://nextjs.org/docs/app/getting-started/updating-data)에 대해 더 알아보세요.

## 정적 내보내기(선택 사항)[](https://nextjs.org/docs/app/guides/single-page-applications#static-export-optional)

Next.js는 완전한 [정적 사이트](https://nextjs.org/docs/app/guides/static-exports) 생성을 지원합니다. 이는 엄격한 SPA보다 몇 가지 이점이 있습니다:

  * **자동 코드 분할:** 단일 `index.html`을 제공하는 대신, Next.js는 라우트마다 HTML 파일을 생성하므로 방문자가 클라이언트 자바스크립트 번들을 기다리지 않고 더 빠르게 콘텐츠를 볼 수 있습니다.
  * **향상된 사용자 경험:** 모든 라우트에 동일한 최소 스켈레톤을 제공하는 대신 각 라우트에 완전히 렌더링된 페이지를 제공합니다. 사용자가 클라이언트 측에서 탐색할 때 전환은 여전히 즉각적이며 SPA와 유사합니다.



정적 내보내기를 활성화하려면 구성을 업데이트하세요:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      output: 'export',
    }
     
    export default nextConfig
[/code]

`next build`를 실행하면 Next.js가 애플리케이션의 HTML/CSS/JS 에셋이 포함된 `out` 폴더를 생성합니다.

> **Note:** Next.js 서버 기능은 정적 내보내기에서 지원되지 않습니다. [자세히 보기](https://nextjs.org/docs/app/guides/static-exports#unsupported-features).

## 기존 프로젝트를 Next.js로 마이그레이션하기[](https://nextjs.org/docs/app/guides/single-page-applications#migrating-existing-projects-to-nextjs)

다음 가이드를 따라 Next.js로 점진적으로 마이그레이션할 수 있습니다:

  * [Create React App에서 마이그레이션](https://nextjs.org/docs/app/guides/migrating/from-create-react-app)
  * [Vite에서 마이그레이션](https://nextjs.org/docs/app/guides/migrating/from-vite)



이미 Pages Router를 사용하는 SPA라면 [App Router를 점진적으로 도입](https://nextjs.org/docs/app/guides/migrating/app-router-migration)하는 방법을 확인하세요.

도움이 되었나요?

supported.

Send
