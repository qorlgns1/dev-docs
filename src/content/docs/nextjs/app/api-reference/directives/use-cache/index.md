---
title: '지시문: use cache'
description: '지시문은 라우트, React 컴포넌트, 함수가 캐시될 수 있도록 표시합니다. 파일 상단에 선언하면 해당 파일의 모든 export가 캐시되고, 함수나 컴포넌트 상단에 인라인으로 선언하면 반환값을 캐시합니다.'
---

# 지시문: use cache | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/directives/use-cache

[API Reference](https://nextjs.org/docs/app/api-reference)[Directives](https://nextjs.org/docs/app/api-reference/directives)use cache

# use cache

마지막 업데이트 2026년 2월 20일

`use cache` 지시문은 라우트, React 컴포넌트, 함수가 캐시될 수 있도록 표시합니다. 파일 상단에 선언하면 해당 파일의 모든 export가 캐시되고, 함수나 컴포넌트 상단에 인라인으로 선언하면 반환값을 캐시합니다.

> **알아 두면 좋아요:**
>
>   * 쿠키나 헤더를 사용해야 한다면 캐시 범위 밖에서 읽고 값을 인자로 전달하세요. 이 패턴이 권장됩니다.
>   * 인메모리 캐시가 런타임 데이터에 충분하지 않다면 [`'use cache: remote'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote)가 전용 캐시 핸들러를 제공하도록 플랫폼을 허용하지만, 캐시 확인을 위한 네트워크 왕복이 필요하고 일반적으로 플랫폼 비용이 발생합니다.
>   * 규정 준수 요구 사항이 있거나 런타임 데이터를 `use cache` 범위로 인자로 전달하도록 리팩터링할 수 없다면 [`'use cache: private'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)를 확인하세요.
>

## 사용법[](https://nextjs.org/docs/app/api-reference/directives/use-cache#usage)

`use cache`는 Cache Components 기능입니다. 이를 활성화하려면 `next.config.ts` 파일에 [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) 옵션을 추가하세요:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      cacheComponents: true,
    }

    export default nextConfig
[/code]

그런 다음 파일, 컴포넌트, 함수 단위로 `use cache`를 추가합니다:
[code]
    // File level
    'use cache'

    export default async function Page() {
      // ...
    }

    // Component level
    export async function MyComponent() {
      'use cache'
      return <></>
    }

    // Function level
    export async function getData() {
      'use cache'
      const data = await fetch('/api/data')
      return data
    }
[/code]

> **알아 두면 좋아요**: 파일 단위로 사용하면 모든 함수 export가 async 함수여야 합니다.

## `use cache` 동작 방식[](https://nextjs.org/docs/app/api-reference/directives/use-cache#how-use-cache-works)

### 캐시 키[](https://nextjs.org/docs/app/api-reference/directives/use-cache#cache-keys)

캐시 항목 키는 입력값의 직렬화 버전으로 생성되며, 여기에는 다음이 포함됩니다:

  1. **Build ID** - 빌드마다 고유하며 변경 시 모든 캐시 항목이 무효화됩니다.
  2. **Function ID** - 코드베이스에서 함수 위치와 시그니처를 기반으로 한 보안 해시입니다.
  3. **직렬화 가능한 인자** - 컴포넌트의 props 또는 함수 인자입니다.
  4. **HMR refresh hash** (개발 환경 전용) - 핫 모듈 교체 시 캐시를 무효화합니다.

캐시된 함수가 외부 스코프의 변수를 참조하면 해당 변수가 자동으로 캡처되어 인자로 바인딩되며, 캐시 키의 일부가 됩니다.

lib/data.ts
[code]
    async function Component({ userId }: { userId: string }) {
      const getData = async (filter: string) => {
        'use cache'
        // Cache key includes both userId (from closure) and filter (argument)
        return fetch(`/api/users/${userId}/data?filter=${filter}`)
      }

      return getData('active')
    }
[/code]

위 스니펫에서 `userId`는 외부 스코프에서 캡처되고 `filter`는 인자로 전달되므로 둘 다 `getData` 함수의 캐시 키에 포함됩니다. 즉, 사용자와 필터 조합마다 별도의 캐시 항목이 생성됩니다.

## 직렬화[](https://nextjs.org/docs/app/api-reference/directives/use-cache#serialization)

캐시된 함수의 인자와 반환값은 직렬화 가능해야 합니다.

전체 참조는 아래를 확인하세요:

  * [Serializable arguments](https://react.dev/reference/rsc/use-server#serializable-parameters-and-return-values) - **React Server Components** 직렬화를 사용합니다.
  * [Serializable return types](https://react.dev/reference/rsc/use-client#serializable-types) - **React Client Components** 직렬화를 사용합니다.

> **알아 두면 좋아요:** 인자와 반환값은 서로 다른 직렬화 시스템을 사용합니다. 서버 컴포넌트 직렬화(인자용)는 클라이언트 컴포넌트 직렬화(반환값용)보다 제한이 더 엄격합니다. 따라서 JSX 요소를 반환할 수는 있지만 패스스루 패턴을 사용하지 않으면 인자로 받을 수 없습니다.

### 지원 타입[](https://nextjs.org/docs/app/api-reference/directives/use-cache#supported-types)

**인자:**

  * 원시 값: `string`, `number`, `boolean`, `null`, `undefined`
  * 평범한 객체: `{ key: value }`
  * 배열: `[1, 2, 3]`
  * Dates, Maps, Sets, TypedArrays, ArrayBuffers
  * React elements (패스스루 전용)

**반환값:**

  * 인자와 동일하며, 여기에 JSX 요소가 추가됩니다.

### 미지원 타입[](https://nextjs.org/docs/app/api-reference/directives/use-cache#unsupported-types)

  * 클래스 인스턴스
  * 함수(패스스루 제외)
  * Symbols, WeakMaps, WeakSets
  * URL 인스턴스

app/components/user-card.tsx
[code]
    // Valid - primitives and plain objects
    async function UserCard({
      id,
      config,
    }: {
      id: string
      config: { theme: string }
    }) {
      'use cache'
      return <div>{id}</div>
    }

    // Invalid - class instance
    async function UserProfile({ user }: { user: UserClass }) {
      'use cache'
      // Error: Cannot serialize class instance
      return <div>{user.name}</div>
    }
[/code]

### 패스스루(직렬화할 수 없는 인자)[](https://nextjs.org/docs/app/api-reference/directives/use-cache#pass-through-non-serializable-arguments)

값을 **읽지만 않으면** 직렬화할 수 없는 값을 받을 수 있습니다. 이를 통해 `children`과 Server Actions를 활용한 구성 패턴이 가능합니다:

app/components/cached-wrapper.tsx
[code]
    async function CachedWrapper({ children }: { children: ReactNode }) {
      'use cache'
      // Don't read or modify children - just pass it through
      return (
        <div className="wrapper">
          <header>Cached Header</header>
          {children}
        </div>
      )
    }

    // Usage: children can be dynamic
    export default function Page() {
      return (
        <CachedWrapper>
          <DynamicComponent /> {/* Not cached, passed through */}
        </CachedWrapper>
      )
    }
[/code]

캐시된 컴포넌트를 통해 Server Actions도 전달할 수 있습니다:

app/components/cached-form.tsx
[code]
    async function CachedForm({ action }: { action: () => Promise<void> }) {
      'use cache'
      // Don't call action here - just pass it through
      return <form action={action}>{/* ... */}</form>
    }
[/code]

## 제약사항[](https://nextjs.org/docs/app/api-reference/directives/use-cache#constraints)

캐시된 함수는 격리된 환경에서 실행됩니다. 다음 제약을 통해 캐시 동작의 예측 가능성과 보안을 보장합니다.

### 런타임 API[](https://nextjs.org/docs/app/api-reference/directives/use-cache#runtime-apis)

캐시된 함수와 컴포넌트는 `cookies()`, `headers()`, `searchParams` 같은 런타임 API에 직접 접근할 수 **없습니다**. 대신 캐시 범위 밖에서 값을 읽고 인자로 전달하세요.

### 런타임 캐싱 고려 사항[](https://nextjs.org/docs/app/api-reference/directives/use-cache#runtime-caching-considerations)

`use cache`는 주로 정적 셸에 동적 데이터를 포함하도록 설계되었지만, 인메모리 LRU(Least Recently Used) 스토리지를 사용해 런타임 데이터도 캐시할 수 있습니다.

런타임 캐시 동작은 호스팅 환경에 따라 달라집니다:

Environment| Runtime Caching Behavior
---|---
**Serverless**|  캐시 항목이 요청 간에 유지되지 않는 것이 일반적입니다(요청마다 인스턴스가 다를 수 있음). 빌드 타임 캐싱은 정상적으로 동작합니다.
**Self-hosted**|  캐시 항목이 요청 간에 유지됩니다. [`cacheMaxMemorySize`](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)로 캐시 크기를 제어하세요.

기본 인메모리 캐시로 충분하지 않다면 플랫폼이 전용 캐시 핸들러(예: Redis, KV 데이터베이스)를 제공할 수 있는 **[`use cache: remote`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote)**를 고려하세요. 이는 전체 트래픽에 맞게 확장되지 않은 데이터 소스에 대한 접근 횟수를 줄이는 데 도움이 되지만, 스토리지, 네트워크 지연, 플랫폼 비용이 발생합니다.

매우 드물게, 규정 준수 요구 사항이 있거나 런타임 데이터를 `use cache` 범위에 인자로 전달하도록 코드를 리팩터링할 수 없는 경우 [`use cache: private`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)가 필요할 수 있습니다.

### React.cache 격리[](https://nextjs.org/docs/app/api-reference/directives/use-cache#reactcache-isolation)

[`React.cache`](https://react.dev/reference/react/cache)는 `use cache` 경계 내부에서 격리된 스코프로 동작합니다. `use cache` 함수 밖에서 `React.cache`로 저장한 값은 안쪽에서 보이지 않습니다.

따라서 `React.cache`를 사용해 데이터를 `use cache` 범위 안으로 전달할 수 없습니다:
[code]
    import { cache } from 'react'

    const store = cache(() => ({ current: null as string | null }))

    function Parent() {
      const shared = store()
      shared.current = 'value from parent'
      return <Child />
    }

    async function Child() {
      'use cache'
      const shared = store()
      // shared.current is null, not 'value from parent'
      // use cache has its own isolated React.cache scope
      return <div>{shared.current}</div>
    }
[/code]

이 격리는 캐시된 함수가 예측 가능한 자체 포함형 동작을 유지하도록 보장합니다. 데이터를 `use cache` 범위에 전달하려면 함수 인자를 사용하세요.

## 런타임에서의 `use cache`[](https://nextjs.org/docs/app/api-reference/directives/use-cache#use-cache-at-runtime)

**서버**에서는 캐시 항목이 인메모리에 저장되며 `cacheLife` 구성의 `revalidate`, `expire` 시간 설정을 따릅니다. `next.config.js`에서 [`cacheHandlers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)를 설정해 캐시 스토리지를 커스터마이즈할 수 있습니다.

**클라이언트**에서는 서버 캐시 콘텐츠가 브라우저 메모리에 저장되며 `stale` 시간 동안 유지됩니다. 클라이언트 라우터는 구성과 상관없이 **최소 30초의 stale 시간**을 강제합니다.

`x-nextjs-stale-time` 응답 헤더는 서버와 클라이언트 간 캐시 수명을 전달해 일관된 동작을 보장합니다.

## 재검증[](https://nextjs.org/docs/app/api-reference/directives/use-cache#revalidation)

기본적으로 `use cache`는 다음 설정을 가진 `default` 프로필을 사용합니다:

  * **stale**: 5분(클라이언트 측)
  * **revalidate**: 15분(서버 측)
  * **expire**: 시간 기반 만료 없음

lib/data.ts
[code]
    async function getData() {
      'use cache'
      // Implicitly uses default profile
      return fetch('/api/data')
    }
[/code]

### 캐시 수명 커스터마이징[](https://nextjs.org/docs/app/api-reference/directives/use-cache#customizing-cache-lifetime)

[`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) 함수를 사용해 캐시 지속 시간을 커스터마이즈하세요:

lib/data.ts
[code]
    import { cacheLife } from 'next/cache'

    async function getData() {
      'use cache'
      cacheLife('hours') // Use built-in 'hours' profile
      return fetch('/api/data')
    }
[/code]

### 온디맨드 재검증[](https://nextjs.org/docs/app/api-reference/directives/use-cache#on-demand-revalidation)

온디맨드 캐시 무효화를 위해 [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag), [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag), [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 사용하세요:

lib/data.ts
[code]
    import { cacheTag } from 'next/cache'
[/code]

async function getProducts() {
      'use cache'
      cacheTag('products')
      return fetch('/api/products')
    }
[/code]

app/actions.ts
[code]
    'use server'

    import { updateTag } from 'next/cache'

    export async function updateProduct() {
      await db.products.update(...)
      updateTag('products') // Invalidates all 'products' caches
    }
[/code]

`cacheLife`와 `cacheTag`는 클라이언트와 서버 캐싱 계층 전반에 통합되어, 한 곳에서 캐싱 의미를 정의하면 어디서든 적용됩니다.

## 예시[](https://nextjs.org/docs/app/api-reference/directives/use-cache#examples)

### `use cache`로 전체 라우트 캐싱[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-an-entire-route-with-use-cache)

전체 라우트를 사전 렌더링하려면 `layout`과 `page` 파일 **모두** 상단에 `use cache`를 추가하세요. 각 세그먼트는 애플리케이션의 개별 진입점으로 간주되며 독립적으로 캐시됩니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    'use cache'

    export default async function Layout({ children }: { children: ReactNode }) {
      return <div>{children}</div>
    }
[/code]

`page` 파일에 임포트되어 중첩된 모든 컴포넌트는 해당 `page`와 연결된 캐시 출력의 일부가 됩니다.

app/page.tsx

JavaScriptTypeScript
[code]
    'use cache'

    async function Users() {
      const users = await fetch('/api/users')
      // loop through users
    }

    export default async function Page() {
      return (
        <main>
          <Users />
        </main>
      )
    }
[/code]

> **알아두면 좋아요** :
>
> * `use cache`를 `layout`이나 `page` 중 하나에만 추가하면, 그 라우트 세그먼트와 그 안으로 임포트된 컴포넌트만 캐시됩니다.

### `use cache`로 컴포넌트 출력 캐싱[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-a-components-output-with-use-cache)

컴포넌트 수준에서 `use cache`를 사용해 해당 컴포넌트 안에서 수행되는 fetch나 연산을 캐시할 수 있습니다. 직렬화된 props가 동일한 값을 생성하는 한 동일한 캐시 엔트리가 재사용됩니다.

app/components/bookings.tsx

JavaScriptTypeScript
[code]
    export async function Bookings({ type = 'haircut' }: BookingsProps) {
      'use cache'
      async function getBookingsData() {
        const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
        return data
      }
      return //...
    }

    interface BookingsProps {
      type: string
    }
[/code]

### `use cache`로 함수 출력 캐싱[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-function-output-with-use-cache)

`use cache`는 모든 비동기 함수에 추가할 수 있으므로, 컴포넌트나 라우트에만 국한되지 않습니다. 네트워크 요청, 데이터베이스 쿼리, 느린 연산 등을 캐싱할 수 있습니다.

app/actions.ts

JavaScriptTypeScript
[code]
    export async function getData() {
      'use cache'

      const data = await fetch('/api/data')
      return data
    }
[/code]

### 인터리빙[](https://nextjs.org/docs/app/api-reference/directives/use-cache#interleaving)

React에서는 `children` 또는 슬롯을 활용한 컴포지션이 유연한 컴포넌트를 만드는 잘 알려진 패턴입니다. `use cache`를 사용할 때도 동일하게 UI를 구성할 수 있습니다. 반환된 JSX에 `children`이나 다른 컴포지션 슬롯으로 포함된 내용은 캐시 가능한 컴포넌트를 통과하되 캐시 엔트리에 영향을 주지 않습니다.

캐시 가능한 함수 본문 내부에서 JSX 슬롯을 직접 참조하지 않는 한, 반환된 출력에 슬롯이 존재해도 캐시 엔트리에 영향이 없습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const uncachedData = await getData()
      return (
        // Pass compositional slots as props, e.g. header and children
        <CacheComponent header={<h1>Home</h1>}>
          {/* DynamicComponent is provided as the children slot */}
          <DynamicComponent data={uncachedData} />
        </CacheComponent>
      )
    }

    async function CacheComponent({
      header, // header: a compositional slot, injected as a prop
      children, // children: another slot for nested composition
    }: {
      header: ReactNode
      children: ReactNode
    }) {
      'use cache'
      const cachedData = await fetch('/api/cached-data')
      return (
        <div>
          {header}
          <PrerenderedComponent data={cachedData} />
          {children}
        </div>
      )
    }
[/code]

또한 캐시 가능한 함수 안에서 호출하지 않고도, 캐시된 컴포넌트를 거쳐 Server Action을 Client Component로 전달할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import ClientComponent from './ClientComponent'

    export default async function Page() {
      const performUpdate = async () => {
        'use server'
        // Perform some server-side update
        await db.update(...)
      }

      return <CachedComponent performUpdate={performUpdate} />
    }

    async function CachedComponent({
      performUpdate,
    }: {
      performUpdate: () => Promise<void>
    }) {
      'use cache'
      // Do not call performUpdate here
      return <ClientComponent action={performUpdate} />
    }
[/code]

app/ClientComponent.tsx

JavaScriptTypeScript
[code]
    'use client'

    export default function ClientComponent({
      action,
    }: {
      action: () => Promise<void>
    }) {
      return <button onClick={action}>Update</button>
    }
[/code]

## 문제 해결[](https://nextjs.org/docs/app/api-reference/directives/use-cache#troubleshooting)

### 캐시 동작 디버깅[](https://nextjs.org/docs/app/api-reference/directives/use-cache#debugging-cache-behavior)

#### 상세 로깅[](https://nextjs.org/docs/app/api-reference/directives/use-cache#verbose-logging)

상세한 캐시 로그를 보려면 `NEXT_PRIVATE_DEBUG_CACHE=1`을 설정하세요:
[code]
    NEXT_PRIVATE_DEBUG_CACHE=1 npm run dev
    # or for production
    NEXT_PRIVATE_DEBUG_CACHE=1 npm run start
[/code]

> **알아두면 좋아요:** 이 환경 변수는 ISR 및 기타 캐싱 메커니즘도 로깅합니다. 자세한 내용은 [Verifying correct production behavior](https://nextjs.org/docs/app/guides/incremental-static-regeneration#verifying-correct-production-behavior)를 참고하세요.

#### 콘솔 로그 재생[](https://nextjs.org/docs/app/api-reference/directives/use-cache#console-log-replays)

개발 환경에서 캐시된 함수의 콘솔 로그에는 `Cache` 접두사가 붙습니다.

### 빌드 중단(Cache Timeout)[](https://nextjs.org/docs/app/api-reference/directives/use-cache#build-hangs-cache-timeout)

빌드가 중단된다면 `use cache` 경계 밖에서 생성된 동적 또는 런타임 데이터로 해결되는 Promise에 접근하고 있는 것입니다. 캐시된 함수가 빌드 중에 해결될 수 없는 데이터를 기다리며, 50초 후 타임아웃이 발생합니다.

빌드가 타임아웃되면 다음 오류 메시지가 표시됩니다:

> Error: Filling a cache during prerender timed out, likely because request-specific arguments such as params, searchParams, cookies() or dynamic data were used inside "use cache".

이 상황은 Promise를 props로 전달하거나, 클로저로 접근하거나, 공유 저장소(Map)에 보관할 때 자주 발생합니다.

> **알아두면 좋아요:** `use cache` 내부에서 `cookies()`나 `headers()`를 직접 호출하면 [다른 오류](https://nextjs.org/docs/messages/next-request-in-use-cache)가 즉시 발생하며, 타임아웃이 아닙니다.

**런타임 데이터 Promise를 props로 전달하는 경우:**

app/page.tsx
[code]
    import { cookies } from 'next/headers'
    import { Suspense } from 'react'

    export default function Page() {
      return (
        <Suspense fallback={<div>Loading...</div>}>
          <Dynamic />
        </Suspense>
      )
    }

    async function Dynamic() {
      const cookieStore = cookies()
      return <Cached promise={cookieStore} /> // Build hangs
    }

    async function Cached({ promise }: { promise: Promise<unknown> }) {
      'use cache'
      const data = await promise // Waits for runtime data during build
      return <p>..</p>
    }
[/code]

`Dynamic` 컴포넌트에서 `cookies` 스토어를 기다린 뒤, 쿠키 값을 `Cached` 컴포넌트에 전달하세요.

**공유 중복 제거 저장소:**

app/page.tsx
[code]
    // Problem: Map stores dynamic Promises, accessed by cached code
    import { Suspense } from 'react'

    const cache = new Map<string, Promise<string>>()

    export default function Page() {
      return (
        <>
          <Suspense fallback={<div>Loading...</div>}>
            <Dynamic id="data" />
          </Suspense>
          <Cached id="data" />
        </>
      )
    }

    async function Dynamic({ id }: { id: string }) {
      // Stores dynamic Promise in shared Map
      cache.set(
        id,
        fetch(`https://api.example.com/${id}`).then((r) => r.text())
      )
      return <p>Dynamic</p>
    }

    async function Cached({ id }: { id: string }) {
      'use cache'
      return <p>{await cache.get(id)}</p> // Build hangs - retrieves dynamic Promise
    }
[/code]

Next.js의 내장 `fetch()` 중복 제거를 사용하거나 캐시 컨텍스트와 비캐시 컨텍스트에 대해 별도의 Map을 사용하세요.

## 플랫폼 지원[](https://nextjs.org/docs/app/api-reference/directives/use-cache#platform-support)

Deployment Option| Supported
---|---
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| 예
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| 예
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| 아니오
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| 플랫폼별

Next.js를 셀프 호스팅할 때 [캐싱을 구성](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr)하는 방법을 알아보세요.

## 버전 기록[](https://nextjs.org/docs/app/api-reference/directives/use-cache#version-history)

Version| Changes
---|---
`v16.0.0`| `"use cache"`가 Cache Components 기능과 함께 활성화됩니다.
`v15.0.0`| `"use cache"`가 실험적 기능으로 도입됩니다.

## 관련 항목

관련 API 레퍼런스를 확인하세요.

- [use cache: private](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)
  - 런타임 요청 API에 접근하는 함수를 캐싱하기 위해 "use cache: private" 지시어를 사용하는 방법을 알아보세요.

- [cacheComponents](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
  - Next.js에서 cacheComponents 플래그를 활성화하는 방법을 알아보세요.

- [cacheLife](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)
  - Next.js에서 cacheLife 구성을 설정하는 방법을 알아보세요.

- [cacheHandlers](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)
  - Next.js에서 use cache 지시어용 사용자 정의 캐시 핸들러를 구성하세요.

- [cacheTag](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
  - Next.js 애플리케이션에서 cacheTag 함수를 사용해 캐시 무효화를 관리하는 방법을 알아보세요.

- [cacheLife](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
  - 캐시된 함수나 컴포넌트의 만료 시간을 설정하기 위해 cacheLife 함수를 사용하는 방법을 알아보세요.

- [revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
  - revalidateTag 함수의 API 레퍼런스입니다.
