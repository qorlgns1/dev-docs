---
title: '가이드: Prefetching'
description: '원본 URL: https://nextjs.org/docs/app/guides/prefetching'
---

# 가이드: Prefetching | Next.js

원본 URL: https://nextjs.org/docs/app/guides/prefetching

# Prefetching

최종 업데이트 2026년 2월 20일

프리페칭은 애플리케이션에서 서로 다른 라우트 사이를 탐색할 때 즉각적으로 반응하는 것처럼 느끼게 합니다. Next.js는 애플리케이션 코드에서 사용하는 링크를 기반으로 기본적으로 지능적인 프리페치를 시도합니다.

이 가이드는 프리페칭이 어떻게 동작하는지 설명하고 일반적인 구현 패턴을 보여 줍니다.

  * [자동 프리페치](https://nextjs.org/docs/app/guides/prefetching#automatic-prefetch)
  * [수동 프리페치](https://nextjs.org/docs/app/guides/prefetching#manual-prefetch)
  * [호버 트리거 프리페치](https://nextjs.org/docs/app/guides/prefetching#hover-triggered-prefetch)
  * [Link 확장 또는 분리](https://nextjs.org/docs/app/guides/prefetching#extending-or-ejecting-link)
  * [프리페치 비활성화](https://nextjs.org/docs/app/guides/prefetching#disabled-prefetch)

## 프리페칭은 어떻게 작동하나요?[](https://nextjs.org/docs/app/guides/prefetching#how-does-prefetching-work)

라우트 간 네비게이션 시 브라우저는 HTML 및 JavaScript 파일과 같은 페이지 자산을 요청합니다. 프리페칭은 새 라우트로 이동하기 전에 이러한 리소스를 _미리_ 가져오는 과정입니다.

Next.js는 라우트를 기준으로 애플리케이션을 더 작은 JavaScript 청크로 자동 분할합니다. 기존 SPA처럼 모든 코드를 한 번에 로드하는 대신 현재 라우트에 필요한 코드만 로드합니다. 이렇게 하면 초기 로드 시간이 줄어드는 동안 앱의 다른 부분이 백그라운드에서 로드됩니다. 사용자가 링크를 클릭할 즈음에는 새 라우트에 필요한 리소스가 이미 브라우저 캐시에 적재됩니다.

새 페이지로 이동할 때 전체 페이지 리로드나 브라우저 로딩 스피너가 없습니다. 대신 Next.js는 [클라이언트 전환](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)을 수행하여 페이지 이동이 즉각적으로 느껴지게 합니다.

## 정적 라우트 vs. 동적 라우트 프리페칭[](https://nextjs.org/docs/app/guides/prefetching#prefetching-static-vs-dynamic-routes)

| | **정적 페이지** | **동적 페이지**
|---|---|---
| **Prefetched** | 예, 전체 라우트 | [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)가 있는 경우만
| [**클라이언트 캐시 TTL**](https://nextjs.org/docs/app/guides/caching#full-route-cache) | 5분(기본값) | [활성화](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)되지 않으면 해제
| **클릭 시 서버 왕복** | 없음 | 예, [shell](https://nextjs.org/docs/app/getting-started/cache-components) 이후 스트리밍

> **알아두면 좋아요:** 초기 네비게이션 동안 브라우저는 HTML, JavaScript, React Server Components(RSC) 페이로드를 가져옵니다. 이후 네비게이션에서는 서버 컴포넌트용 RSC 페이로드와 클라이언트 컴포넌트용 JS 번들을 가져옵니다.

## 자동 프리페치[](https://nextjs.org/docs/app/guides/prefetching#automatic-prefetch)

app/ui/nav-link.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default function NavLink() {
      return <Link href="/about">About</Link>
    }
[/code]

**Context**| **Prefetched payload**| **Client Cache TTL**
---|---|---
`loading.js` 없음| 전체 페이지| 앱 리로드 시까지
`loading.js` 포함| 첫 번째 로딩 경계까지의 레이아웃| 30초 ([구성 가능](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes))

자동 프리페칭은 프로덕션에서만 실행됩니다. `prefetch={false}`를 사용해 비활성화하거나 [프리페치 비활성화](https://nextjs.org/docs/app/guides/prefetching#disabled-prefetch)에 나오는 래퍼를 활용하세요.

## 수동 프리페치[](https://nextjs.org/docs/app/guides/prefetching#manual-prefetch)

수동 프리페칭을 하려면 `next/navigation`에서 `useRouter` 훅을 가져와 뷰포트 밖의 라우트나 애널리틱스, 호버, 스크롤 등에 대응하여 `router.prefetch()`를 호출해 워밍업합니다.
[code]
    'use client'

    import { useRouter } from 'next/navigation'
    import { CustomLink } from '@components/link'

    export function PricingCard() {
      const router = useRouter()

      return (
        <div onMouseEnter={() => router.prefetch('/pricing')}>
          {/* other UI elements */}
          <CustomLink href="/pricing">View Pricing</CustomLink>
        </div>
      )
    }
[/code]

컴포넌트가 로드될 때 URL을 프리페치하려는 경우 Link를 확장하거나 분리하는 [예시]를 확인하세요.

## 호버 트리거 프리페치[](https://nextjs.org/docs/app/guides/prefetching#hover-triggered-prefetch)

> **주의:** `Link`를 확장하면 프리페칭, 캐시 무효화, 접근성 문제를 직접 관리해야 합니다. 기본 동작으로 충분하지 않을 때만 진행하세요.

Next.js는 기본적으로 적절한 프리페칭을 시도하지만, 고급 사용자는 필요에 따라 분리하여 수정할 수 있습니다. 성능과 리소스 사용 사이의 균형을 직접 제어할 수 있습니다.

예를 들어, 뷰포트에 들어올 때(기본 동작)가 아니라 호버 시에만 프리페치하도록 만들어야 할 수 있습니다.
[code]
    'use client'

    import Link from 'next/link'
    import { useState } from 'react'

    export function HoverPrefetchLink({
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

`prefetch={null}`은 사용자가 의도를 보인 이후 기본(정적) 프리페칭을 복원합니다.

## Link 확장 또는 분리[](https://nextjs.org/docs/app/guides/prefetching#extending-or-ejecting-link)

`<Link>` 컴포넌트를 확장해 자체 프리페칭 전략을 만들 수 있습니다. 예를 들어 사용자 커서 방향을 예측해 링크를 프리페치하는 [ForesightJS](https://foresightjs.com/docs/integrations/nextjs) 라이브러리를 사용할 수 있습니다.

또는 [`useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router)를 사용해 기본 `<Link>` 일부 동작을 재현할 수도 있습니다. 다만 이 경우 프리페칭과 캐시 무효화를 직접 관리해야 합니다.
[code]
    'use client'

    import { useRouter } from 'next/navigation'
    import { useEffect } from 'react'

    function ManualPrefetchLink({
      href,
      children,
    }: {
      href: string
      children: React.ReactNode
    }) {
      const router = useRouter()

      useEffect(() => {
        let cancelled = false
        const poll = () => {
          if (!cancelled) router.prefetch(href, { onInvalidate: poll })
        }
        poll()
        return () => {
          cancelled = true
        }
      }, [href, router])

      return (
        <a
          href={href}
          onClick={(event) => {
            event.preventDefault()
            router.push(href)
          }}
        >
          {children}
        </a>
      )
    }
[/code]

[`onInvalidate`](https://nextjs.org/docs/app/api-reference/functions/use-router#userouter)는 Next.js가 캐시 데이터가 오래되었다고 판단할 때 호출되어 프리페치를 새로 고칠 수 있게 합니다.

> **알아두면 좋아요:** `a` 태그를 사용하면 대상 라우트로 전체 페이지 네비게이션이 발생합니다. `onClick`에서 기본 동작을 막고 `router.push`를 호출해 대상 라우트로 이동할 수 있습니다.

## 프리페치 비활성화[](https://nextjs.org/docs/app/guides/prefetching#disabled-prefetch)

특정 라우트의 프리페칭을 완전히 비활성화해 리소스 사용을 보다 세밀하게 제어할 수 있습니다.
[code]
    'use client'

    import Link, { LinkProps } from 'next/link'

    function NoPrefetchLink({
      prefetch,
      ...rest
    }: LinkProps & { children: React.ReactNode }) {
      return <Link {...rest} prefetch={false} />
    }
[/code]

예를 들어 애플리케이션 전체에서 `<Link>`를 일관되게 사용하고 싶지만, 푸터의 링크는 뷰포트에 들어왔을 때 프리페칭할 필요가 없을 수 있습니다.

## 프리페칭 최적화[](https://nextjs.org/docs/app/guides/prefetching#prefetching-optimizations)

### 클라이언트 캐시[](https://nextjs.org/docs/app/guides/prefetching#client-cache)

Next.js는 프리페치한 React Server Component 페이로드를 경로 세그먼트를 키로 사용해 메모리에 저장합니다. 형제 라우트 간 이동(예: `/dashboard/settings` → `/dashboard/analytics`) 시 상위 레이아웃을 재사용하고 변경된 리프 페이지만 가져옵니다. 이를 통해 네트워크 트래픽이 줄고 네비게이션 속도가 개선됩니다.

### 프리페치 스케줄링[](https://nextjs.org/docs/app/guides/prefetching#prefetch-scheduling)

Next.js는 작은 작업 큐를 유지하며 다음 순서로 프리페치를 수행합니다.

  1. 뷰포트 내 링크
  2. 사용자 의도가 드러난 링크(호버 또는 터치)
  3. 최신 링크가 이전 링크를 대체
  4. 화면 밖으로 스크롤된 링크는 폐기

스케줄러는 사용 가능성이 높은 네비게이션을 우선시하면서 불필요한 다운로드를 최소화합니다.

### 부분 사전 렌더링(PPR)[](https://nextjs.org/docs/app/guides/prefetching#partial-prerendering-ppr)

PPR이 활성화되면 페이지가 정적 셸과 스트리밍되는 동적 섹션으로 나뉩니다.

  * 프리페치 가능한 셸은 즉시 스트리밍됩니다.
  * 동적 데이터는 준비되는 대로 스트리밍됩니다.
  * `revalidateTag`, `revalidatePath`와 같은 데이터 무효화는 관련 프리페치를 조용히 새로 고칩니다.

## 문제 해결[](https://nextjs.org/docs/app/guides/prefetching#troubleshooting)

### 프리페칭 중 원치 않는 부작용 발생[](https://nextjs.org/docs/app/guides/prefetching#triggering-unwanted-side-effects-during-prefetching)

레이아웃이나 페이지가 [순수](https://react.dev/learn/keeping-components-pure#purity-components-as-formulas)하지 않아 부작용(예: 애널리틱스 추적)이 있다면, 사용자가 페이지를 방문하기 전에 라우트 프리페치 단계에서 실행될 수 있습니다.

이를 피하려면 부작용을 `useEffect` 훅이나 클라이언트 컴포넌트에서 호출되는 서버 액션으로 옮겨야 합니다.

**Before** :

app/dashboard/layout.tsx

JavaScriptTypeScript
[code]
    import { trackPageView } from '@/lib/analytics'

    export default function Layout({ children }: { children: React.ReactNode }) {
      // This runs during prefetch
      trackPageView()

      return <div>{children}</div>
    }
[/code]

**After** :

app/ui/analytics-tracker.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useEffect } from 'react'
    import { trackPageView } from '@/lib/analytics'

    export function AnalyticsTracker() {
      useEffect(() => {
        trackPageView()
      }, [])

      return null
    }
[/code]

app/dashboard/layout.tsx

JavaScriptTypeScript
[code]
    import { AnalyticsTracker } from '@/app/ui/analytics-tracker'

    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <div>
          <AnalyticsTracker />
          {children}
        </div>
      )
    }
[/code]

### 너무 많은 프리페치를 방지[](https://nextjs.org/docs/app/guides/prefetching#preventing-too-many-prefetches)

Next.js는 `<Link>` 컴포넌트를 사용할 때 뷰포트에 있는 링크를 자동으로 프리페치합니다.

무한 스크롤 테이블처럼 대규모 링크 목록을 렌더링할 때 리소스 사용을 피하기 위해 이를 방지하고 싶을 수 있습니다.

`<Link>` 컴포넌트의 `prefetch` 프로퍼티를 `false`로 설정해 프리페칭을 비활성화할 수 있습니다.

app/ui/no-prefetch-link.tsx

JavaScriptTypeScript
[code]
    <Link prefetch={false} href={`/blog/${post.id}`}>
      {post.title}
    </Link>
[/code]

하지만 이렇게 하면 정적 라우트는 클릭 시에만 가져오고, 동적 라우트는 네비게이션 전에 서버 렌더링을 기다리게 됩니다.

프리페치를 완전히 비활성화하지 않고 리소스 사용을 줄이려면 사용자가 링크에 호버할 때까지 프리페칭을 지연시킬 수 있습니다. 이렇게 하면 사용자가 방문할 가능성이 높은 링크만 대상으로 삼을 수 있습니다.

app/ui/hover-prefetch-link.tsx

JavaScriptTypeScript
[code]
    'use client'

    import Link from 'next/link'
    import { useState } from 'react'

    export function HoverPrefetchLink({
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

보내기
