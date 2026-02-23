---
title: '시작하기: 링크 및 탐색'
description: 'Next.js에서는 기본적으로 서버에서 라우트를 렌더링합니다. 이는 새 라우트를 보여 주기 전에 클라이언트가 서버 응답을 기다려야 함을 의미합니다. Next.js는 탐색이 빠르고 반응성을 유지하도록 사전 가져오기, 스트리밍, 클라이언트 측 전환을 기본으로 제공합니다.'
---

# 시작하기: 링크 및 탐색 | Next.js

출처 URL: https://nextjs.org/docs/app/getting-started/linking-and-navigating

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)링크 및 탐색

페이지 복사

# 링크 및 탐색

마지막 업데이트: 2026년 2월 20일

Next.js에서는 기본적으로 서버에서 라우트를 렌더링합니다. 이는 새 라우트를 보여 주기 전에 클라이언트가 서버 응답을 기다려야 함을 의미합니다. Next.js는 탐색이 빠르고 반응성을 유지하도록 [사전 가져오기](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching), [스트리밍](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming), [클라이언트 측 전환](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)을 기본으로 제공합니다.

이 가이드는 Next.js에서 탐색이 어떻게 동작하는지, 그리고 [동적 라우트](https://nextjs.org/docs/app/getting-started/linking-and-navigating#dynamic-routes-without-loadingtsx)와 [느린 네트워크](https://nextjs.org/docs/app/getting-started/linking-and-navigating#slow-networks)에 맞춰 이를 최적화하는 방법을 설명합니다.

## 탐색 방식[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#how-navigation-works)

Next.js의 탐색 방식을 이해하려면 다음 개념을 알고 있으면 도움이 됩니다.

  * [서버 렌더링](https://nextjs.org/docs/app/getting-started/linking-and-navigating#server-rendering)
  * [사전 가져오기](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)
  * [스트리밍](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)
  * [클라이언트 측 전환](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)

### 서버 렌더링[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#server-rendering)

Next.js에서 [레이아웃과 페이지](https://nextjs.org/docs/app/getting-started/layouts-and-pages)는 기본적으로 [React Server Components](https://react.dev/reference/rsc/server-components)입니다. 초기 및 이후 탐색 모두에서 [Server Component Payload](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs)는 클라이언트로 전송되기 전에 서버에서 생성됩니다.

서버 렌더링은 시점에 따라 두 가지 유형이 있습니다.

  * **정적 렌더링(또는 사전 렌더링)** 은 빌드 타임 또는 [재검증](https://nextjs.org/docs/app/getting-started/caching-and-revalidating) 중에 수행되며 결과가 캐시됩니다.
  * **동적 렌더링** 은 클라이언트 요청에 응답하여 요청 시점에 수행됩니다.

서버 렌더링의 트레이드오프는 새 라우트를 보여 주기 전에 클라이언트가 서버 응답을 기다려야 한다는 점입니다. Next.js는 사용자가 방문할 가능성이 높은 라우트를 [사전 가져오기](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)하고 [클라이언트 측 전환](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)을 수행하여 이 지연을 완화합니다.

> **알아두면 좋아요**: 초기 방문을 위한 HTML도 생성됩니다.

### 사전 가져오기[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)

사전 가져오기는 사용자가 실제로 이동하기 전에 백그라운드에서 라우트를 로드하는 과정입니다. 사용자가 링크를 클릭할 때쯤이면 다음 라우트를 렌더링할 데이터가 이미 클라이언트에 있으므로 라우트 간 탐색이 즉시 발생하는 것처럼 느껴집니다.

Next.js는 [`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)로 연결된 라우트가 사용자 뷰포트에 들어오면 자동으로 사전 가져옵니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <html>
          <body>
            <nav>
              {/* Prefetched when the link is hovered or enters the viewport */}
              <Link href="/blog">Blog</Link>
              {/* No prefetching */}
              <a href="/contact">Contact</a>
            </nav>
            {children}
          </body>
        </html>
      )
    }
[/code]

사전 가져오는 범위는 라우트가 정적인지 동적인지에 따라 달라집니다.

  * **정적 라우트**: 전체 라우트를 사전 가져옵니다.
  * **동적 라우트**: [`loading.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)가 있으면 라우트를 건너뛰거나 일부만 사전 가져옵니다.

동적 라우트를 건너뛰거나 일부만 사전 가져오면 사용자가 방문하지 않을 라우트에 대해 불필요한 서버 작업을 방지할 수 있습니다. 그러나 탐색 전 서버 응답을 기다리면 앱이 응답하지 않는 것처럼 보일 수 있습니다.

동적 라우트 탐색 경험을 개선하려면 [스트리밍](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)을 사용할 수 있습니다.

### 스트리밍[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)

스트리밍은 전체 라우트가 렌더링될 때까지 기다리지 않고 준비되는 대로 동적 라우트의 일부를 서버에서 클라이언트로 전송하도록 합니다. 따라서 페이지 일부가 로딩 중이더라도 사용자는 더 빨리 화면을 볼 수 있습니다.

동적 라우트에서는 **부분 사전 가져오기**가 가능하다는 뜻입니다. 즉, 공유 레이아웃과 로딩 스켈레톤을 미리 요청할 수 있습니다.

스트리밍을 사용하려면 라우트 폴더에 `loading.tsx`를 생성하세요.

app/dashboard/loading.tsx

JavaScriptTypeScript
[code]
    export default function Loading() {
      // Add fallback UI that will be shown while the route is loading.
      return <LoadingSkeleton />
    }
[/code]

백그라운드에서 Next.js는 `page.tsx` 내용을 자동으로 `<Suspense>` 경계로 감쌉니다. 사전 가져온 폴백 UI는 라우트가 로딩되는 동안 표시되고, 준비되면 실제 콘텐츠로 교체됩니다.

> **알아두면 좋아요**: 중첩 컴포넌트의 로딩 UI를 만들기 위해 [`<Suspense>`](https://react.dev/reference/react/Suspense)를 직접 사용할 수도 있습니다.

`loading.tsx`의 이점:

  * 즉각적인 탐색과 시각적 피드백 제공
  * 공유 레이아웃은 상호작용 가능 상태를 유지하고 탐색을 중단할 수 있음
  * [TTFB](https://web.dev/articles/ttfb), [FCP](https://web.dev/articles/fcp), [TTI](https://web.dev/articles/tti) 등 핵심 웹 바이탈 개선

탐색 경험을 더욱 높이기 위해 Next.js는 `<Link>` 컴포넌트로 [클라이언트 측 전환](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)을 수행합니다.

### 클라이언트 측 전환[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)

전통적으로 서버 렌더링 페이지로 이동하면 전체 페이지가 다시 로드됩니다. 이 과정에서 상태가 초기화되고 스크롤 위치가 리셋되며 상호작용이 차단됩니다.

Next.js는 `<Link>` 컴포넌트를 이용한 클라이언트 측 전환으로 이를 피합니다. 페이지를 다시 로드하는 대신 다음과 같이 콘텐츠를 동적으로 업데이트합니다.

  * 공유 레이아웃과 UI 유지
  * 현재 페이지를 사전 가져온 로딩 상태 또는 사용 가능한 새 페이지로 교체

클라이언트 측 전환 덕분에 서버 렌더링 앱이 클라이언트 렌더링 앱처럼 _느껴집니다_. 이를 [사전 가져오기](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) 및 [스트리밍](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)과 결합하면 동적 라우트에서도 빠른 전환이 가능합니다.

## 전환이 느려질 수 있는 원인[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#what-can-make-transitions-slow)

이러한 Next.js 최적화 덕분에 탐색은 빠르고 반응성이 좋습니다. 그러나 특정 상황에서는 전환이 여전히 느리게 _느껴질_ 수 있습니다. 흔한 원인과 사용자 경험 개선 방법은 다음과 같습니다.

### `loading.tsx`가 없는 동적 라우트[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#dynamic-routes-without-loadingtsx)

동적 라우트로 이동할 때 클라이언트는 결과를 보여 주기 전에 서버 응답을 기다려야 합니다. 이 때문에 앱이 응답하지 않는 것처럼 느껴질 수 있습니다.

동적 라우트에 `loading.tsx`를 추가하여 부분 사전 가져오기를 활성화하고 즉각적인 탐색을 트리거하며 라우트 렌더링 중 로딩 UI를 표시하는 것을 권장합니다.

app/blog/[slug]/loading.tsx

JavaScriptTypeScript
[code]
    export default function Loading() {
      return <LoadingSkeleton />
    }
[/code]

> **알아두면 좋아요**: 개발 모드에서는 Next.js Devtools를 사용해 라우트가 정적인지 동적인지 확인할 수 있습니다. 자세한 내용은 [`devIndicators`](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators)를 참조하세요.

### `generateStaticParams`가 없는 동적 세그먼트[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#dynamic-segments-without-generatestaticparams)

[동적 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)가 사전 렌더링될 수 있음에도 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)가 없어 빌드 타임에 렌더링되지 않으면, 해당 라우트는 요청 시점의 동적 렌더링으로 폴백합니다.

`generateStaticParams`를 추가하여 라우트를 빌드 타임에 정적으로 생성하도록 하세요.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    export async function generateStaticParams() {
      const posts = await fetch('https://.../posts').then((res) => res.json())
     
      return posts.map((post) => ({
        slug: post.slug,
      }))
    }
     
    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      // ...
    }
[/code]

### 느린 네트워크[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#slow-networks)

느리거나 불안정한 네트워크에서는 사용자가 링크를 클릭하기 전에 사전 가져오기가 완료되지 않을 수 있습니다. 이는 정적 라우트와 동적 라우트 모두에 영향을 줄 수 있습니다. 이런 경우 `loading.js` 폴백이 아직 사전 가져오기되지 않아 즉시 나타나지 않을 수 있습니다.

인지된 성능을 개선하려면 [`useLinkStatus` 훅](https://nextjs.org/docs/app/api-reference/functions/use-link-status)을 사용하여 전환이 진행 중일 때 즉각적인 피드백을 표시할 수 있습니다.

app/ui/loading-indicator.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useLinkStatus } from 'next/link'
     
    export default function LoadingIndicator() {
      const { pending } = useLinkStatus()
      return (
        <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
      )
    }
[/code]

초기 애니메이션 지연(예: 100ms)을 추가하고 처음에는 보이지 않게(`opacity: 0`) 설정하여 힌트를 "디바운스"할 수 있습니다. 그러면 지정한 지연보다 탐색이 오래 걸리는 경우에만 로딩 인디케이터가 표시됩니다. CSS 예시는 [`useLinkStatus` 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/use-link-status#gracefully-handling-fast-navigation)에서 확인하세요.

> **알아두면 좋아요**: 진행률 표시줄처럼 다른 시각적 피드백 패턴도 사용할 수 있습니다. 예시는 [여기](https://github.com/vercel/react-transition-progress)를 참고하세요.

### 사전 가져오기 비활성화[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#disabling-prefetching)

`<Link>` 컴포넌트의 `prefetch` prop을 `false`로 설정하면 사전 가져오기를 옵트아웃할 수 있습니다. 이는 (무한 스크롤 테이블처럼) 링크가 많은 목록을 렌더링할 때 리소스 사용을 최소화하는 데 유용합니다.
[code] 
    <Link prefetch={false} href="/blog">
      Blog
    </Link>
[/code]

그러나 사전 가져오기 비활성화에는 다음과 같은 트레이드오프가 있습니다.

  * **정적 라우트** 는 사용자가 링크를 클릭해야만 가져옵니다.
  * **동적 라우트** 는 클라이언트가 탐색하기 전에 먼저 서버에서 렌더링해야 합니다.

리소스 사용량을 완전히 비활성화하지 않고 줄이려면 호버 시에만 프리페치하도록 설정할 수 있습니다. 이렇게 하면 뷰포트의 모든 링크가 아니라 사용자가 방문할 가능성이 더 _높은_ 경로로 프리페치를 제한할 수 있습니다.

app/ui/hover-prefetch-link.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import Link from 'next/link'
    import { useState } from 'react'
     
    function HoverPrefetchLink({
      href,
      children,
    }: {
      href: string
      children: React.ReactNode
    }) {
      const [active, setActive] = useState(false)
     
      return (
        <Link
          href={href}
          prefetch={active ? null : false}
          onMouseEnter={() => setActive(true)}
        >
          {children}
        </Link>
      )
    }
[/code]

### 하이드레이션이 완료되지 않음[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#hydration-not-completed)

`<Link>` 는 클라이언트 컴포넌트이므로 라우트를 프리페치하려면 먼저 하이드레이션을 완료해야 합니다. 초기 방문 시에는 JavaScript 번들이 크면 하이드레이션이 지연되어 프리페치가 즉시 시작되지 않을 수 있습니다.

React는 Selective Hydration으로 이를 완화하며, 다음과 같은 방법으로 더 개선할 수 있습니다.

  * [`@next/bundle-analyzer`](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack) 플러그인을 사용해 큰 의존성을 제거하여 번들 크기를 파악하고 줄입니다.
  * 가능한 경우 클라이언트 로직을 서버로 이동합니다. 자세한 내용은 [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) 문서를 참고하세요.



## 예시[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#examples)

### 네이티브 History API[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#native-history-api)

Next.js에서는 페이지를 다시 로드하지 않고도 브라우저의 히스토리 스택을 업데이트하기 위해 네이티브 [`window.history.pushState`](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState) 및 [`window.history.replaceState`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState) 메서드를 사용할 수 있습니다.

`pushState` 와 `replaceState` 호출은 Next.js Router와 통합되어 [`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname)과 [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)와 동기화할 수 있습니다.

#### `window.history.pushState`[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#windowhistorypushstate)

브라우저 히스토리 스택에 새 항목을 추가할 때 사용하세요. 사용자는 이전 상태로 되돌아갈 수 있습니다. 예를 들어 제품 목록을 정렬하려면 다음과 같이 합니다:
[code] 
    'use client'
     
    import { useSearchParams } from 'next/navigation'
     
    export default function SortProducts() {
      const searchParams = useSearchParams()
     
      function updateSorting(sortOrder: string) {
        const params = new URLSearchParams(searchParams.toString())
        params.set('sort', sortOrder)
        window.history.pushState(null, '', `?${params.toString()}`)
      }
     
      return (
        <>
          <button onClick={() => updateSorting('asc')}>Sort Ascending</button>
          <button onClick={() => updateSorting('desc')}>Sort Descending</button>
        </>
      )
    }
[/code]

#### `window.history.replaceState`[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#windowhistoryreplacestate)

브라우저 히스토리 스택의 현재 항목을 교체할 때 사용하세요. 사용자는 이전 상태로 돌아갈 수 없습니다. 예를 들어 애플리케이션 로케일을 전환하려면 다음과 같이 합니다:
[code] 
    'use client'
     
    import { usePathname } from 'next/navigation'
     
    export function LocaleSwitcher() {
      const pathname = usePathname()
     
      function switchLocale(locale: string) {
        // e.g. '/en/about' or '/fr/contact'
        const newPath = `/${locale}${pathname}`
        window.history.replaceState(null, '', newPath)
      }
     
      return (
        <>
          <button onClick={() => switchLocale('en')}>English</button>
          <button onClick={() => switchLocale('fr')}>French</button>
        </>
      )
    }
[/code]

##

### [Link Component내장 `next/link` 컴포넌트로 빠른 클라이언트 측 내비게이션을 활성화하세요.](https://nextjs.org/docs/app/api-reference/components/link)### [loading.js`loading.js` 파일에 대한 API 레퍼런스.](https://nextjs.org/docs/app/api-reference/file-conventions/loading)### [PrefetchingNext.js에서 프리페치를 구성하는 방법을 알아보세요.](https://nextjs.org/docs/app/guides/prefetching)

도움이 되었나요?

지원됨.

전송
