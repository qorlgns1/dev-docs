---
title: '시작하기: Cache Components'
description: '마지막 업데이트 2026년 2월 20일'
---

# 시작하기: Cache Components | Next.js

출처 URL: https://nextjs.org/docs/app/getting-started/cache-components

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Cache Components

페이지 복사

# Cache Components

마지막 업데이트 2026년 2월 20일

> **알아두면 좋아요:** Cache Components는 선택 사항입니다. Next 구성 파일에서 `cacheComponents` 플래그를 `true`로 설정해 활성화하세요. 자세한 내용은 [Cache Components 활성화](https://nextjs.org/docs/app/getting-started/cache-components#enabling-cache-components)를 참조하세요.

Cache Components를 사용하면 하나의 라우트 안에서 정적, 캐시된, 동적 콘텐츠를 섞을 수 있어 정적 사이트의 속도와 동적 렌더링의 유연성을 동시에 얻을 수 있습니다.

서버 렌더링 애플리케이션은 보통 정적 페이지(빠르지만 오래된 콘텐츠)와 동적 페이지(신선하지만 느림) 사이에서 선택을 강요합니다. 작업을 클라이언트로 옮기면 서버 부하는 줄지만 번들이 커지고 초기 렌더링이 느려집니다.

Cache Components는 경로를 미리 렌더링해 즉시 브라우저로 전송되는 **정적 HTML 셸**을 만들고, 동적 콘텐츠는 준비되는 대로 UI를 업데이트하여 이러한 트레이드오프를 제거합니다.

## Cache Components에서 렌더링이 작동하는 방식[](https://nextjs.org/docs/app/getting-started/cache-components#how-rendering-works-with-cache-components)

빌드 시점에 Next.js는 라우트의 컴포넌트 트리를 렌더링합니다. 컴포넌트가 네트워크 리소스, 특정 시스템 API에 접근하지 않거나 렌더링에 요청 정보가 필요하지 않으면, 해당 출력은 **자동으로 정적 셸에 포함**됩니다. 그렇지 않다면 다음 중 하나를 선택해야 합니다:

  * 컴포넌트를 React [`<Suspense>`](https://react.dev/reference/react/Suspense)로 감싸 [내용이 준비될 때까지 대체 UI](https://nextjs.org/docs/app/getting-started/cache-components#defer-rendering-to-request-time)를 표시하며 렌더링을 요청 시점으로 연기하기
  * 또는 [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) 지시어로 결과를 캐시해 [정적 셸에 포함](https://nextjs.org/docs/app/getting-started/cache-components#using-use-cache)하기(요청 데이터가 필요 없는 경우)



이 작업은 요청이 도착하기 전에 미리 수행되므로 사전 렌더링이라고 부릅니다. 이렇게 하면 초기 페이지 로드용 HTML과 클라이언트 내비게이션용 직렬화된 [RSC Payload](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-server)로 구성된 정적 셸이 생성되어, 사용자가 URL에 직접 접근하든 다른 페이지에서 이동하든 브라우저가 즉시 완전한 렌더링 결과를 받습니다.

Next.js는 사전 렌더링 중 완료할 수 없는 컴포넌트를 명시적으로 처리하도록 요구합니다. `<Suspense>`로 감싸거나 `use cache`로 표시하지 않으면 개발 및 빌드 시 [`Uncached data was accessed outside of <Suspense>`](https://nextjs.org/docs/messages/blocking-route) 오류가 발생합니다.

> **알아두면 좋아요**: 캐싱은 컴포넌트 또는 함수 단위로 적용할 수 있으며, 대체 UI는 어떤 서브트리에도 정의할 수 있으므로 하나의 라우트 안에서 정적, 캐시된, 동적 콘텐츠를 조합할 수 있습니다.

이 렌더링 접근 방식은 **Partial Prerendering**이라 부르며, Cache Components 사용 시 기본 동작입니다. 나머지 문서에서는 부분 또는 전체 출력을 생성할 수 있는 "사전 렌더링"으로 통칭합니다.

> **🎥 시청:** 왜 Partial Prerendering이 필요한지와 동작 방식 → [YouTube (10분)](https://www.youtube.com/watch?v=MTcPrTIBkpA).

## 자동으로 사전 렌더링되는 콘텐츠[](https://nextjs.org/docs/app/getting-started/cache-components#automatically-prerendered-content)

동기 I/O, 모듈 import, 순수 계산 같은 작업은 사전 렌더링 동안 완료될 수 있습니다. 이러한 작업만 사용하는 컴포넌트는 렌더링 결과가 정적 HTML 셸에 포함됩니다.

아래 `Page` 컴포넌트의 모든 작업이 렌더링 중에 완료되므로 렌더링 결과는 자동으로 정적 셸에 포함됩니다. 레이아웃과 페이지가 모두 사전 렌더링에 성공하면 전체 라우트가 정적 셸이 됩니다.

page.tsx
[code]
    import fs from 'node:fs'
     
    export default async function Page() {
      // Synchronous file system read
      const content = fs.readFileSync('./config.json', 'utf-8')
     
      // Module imports
      const constants = await import('./constants.json')
     
      // Pure computations
      const processed = JSON.parse(content).items.map((item) => item.value * 2)
     
      return (
        <div>
          <h1>{constants.appName}</h1>
          <ul>
            {processed.map((value, i) => (
              <li key={i}>{value}</li>
            ))}
          </ul>
        </div>
      )
    }
[/code]

> **알아두면 좋아요**: 빌드 출력 요약을 확인해 라우트가 완전히 사전 렌더링되었는지 검증할 수 있습니다. 또는 브라우저에서 페이지 소스를 열어 어떤 콘텐츠가 정적 셸에 추가되었는지 확인할 수 있습니다.

## 렌더링을 요청 시점으로 미루기[](https://nextjs.org/docs/app/getting-started/cache-components#defer-rendering-to-request-time)

사전 렌더링 중 Next.js가 완료할 수 없는 작업(네트워크 요청, 요청 데이터 접근, 비동기 작업 등)을 만나면 이를 명시적으로 처리해야 합니다. 렌더링을 요청 시점으로 미루려면 상위 컴포넌트가 Suspense 경계를 사용해 대체 UI를 제공해야 합니다. 대체 UI는 정적 셸의 일부가 되고, 실제 콘텐츠는 요청 시점에 해결됩니다.

Suspense 경계는 필요한 컴포넌트에 최대한 가깝게 배치하세요. 이렇게 하면 경계 밖의 모든 콘텐츠가 정상적으로 사전 렌더링될 수 있어 정적 셸에 포함되는 양이 극대화됩니다.

> **알아두면 좋아요**: Suspense 경계를 사용하면 여러 동적 섹션이 서로를 블로킹하지 않고 병렬로 렌더링되어 총 로드 시간이 줄어듭니다.

### 동적 콘텐츠[](https://nextjs.org/docs/app/getting-started/cache-components#dynamic-content)

외부 시스템은 콘텐츠를 비동기적으로 제공하므로 해결까지 예측하기 어렵고 실패할 수도 있습니다. 그래서 사전 렌더링은 이를 자동으로 실행하지 않습니다.

일반적으로 매 요청마다 최신 데이터를 받아야 하는 경우(실시간 피드나 개인화 콘텐츠 등) Suspense 경계로 대체 UI를 제공해 렌더링을 미루세요.

예를 들어 아래 `DynamicContent` 컴포넌트는 자동으로 사전 렌더링되지 않는 여러 작업을 사용합니다.

page.tsx
[code]
    import { Suspense } from 'react'
    import fs from 'node:fs/promises'
     
    async function DynamicContent() {
      // Network request
      const data = await fetch('https://api.example.com/data')
     
      // Database query
      const users = await db.query('SELECT * FROM users')
     
      // Async file system operation
      const file = await fs.readFile('..', 'utf-8')
     
      // Simulating external system delay
      await new Promise((resolve) => setTimeout(resolve, 100))
     
      return <div>Not in the static shell</div>
    }
[/code]

페이지에서 `DynamicContent`를 사용하려면 `<Suspense>`로 감싸 대체 UI를 정의하세요:

page.tsx
[code]
    export default async function Page(props) {
      return (
        <>
          <h1>Part of the static shell</h1>
          {/* <p>Loading..</p> is part of the static shell */}
          <Suspense fallback={<p>Loading..</p>}>
            <DynamicContent />
            <div>Sibling excluded from static shell</div>
          </Suspense>
        </>
      )
    }
[/code]

사전 렌더링은 `fetch` 요청에서 중단됩니다. 요청 자체는 시작되지 않으며 이후 코드는 실행되지 않습니다.

대체 UI(`<p>Loading...</p>`)는 정적 셸에 포함되고, 컴포넌트 콘텐츠는 요청 시점에 스트리밍됩니다.

이 예시에서 네트워크 요청, 데이터베이스 쿼리, 파일 읽기, 타임아웃이 모두 동일한 컴포넌트 내부에서 순차적으로 실행되므로 모든 작업이 완료될 때까지 콘텐츠가 나타나지 않습니다.

> **알아두면 좋아요**: 자주 변경되지 않는 동적 콘텐츠라면 `use cache`를 사용해 데이터를 스트리밍 대신 정적 셸에 포함할 수 있습니다. 예시는 [during prerendering](https://nextjs.org/docs/app/getting-started/cache-components#during-prerendering) 섹션을 참고하세요.

### 런타임 데이터[](https://nextjs.org/docs/app/getting-started/cache-components#runtime-data)

요청이 들어올 때만 사용할 수 있는, 요청 컨텍스트가 필요한 특정 유형의 동적 데이터입니다.

  * [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies) \- 사용자 쿠키 데이터
  * [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers) \- 요청 헤더
  * [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) \- URL 쿼리 매개변수
  * [`params`](https://nextjs.org/docs/app/api-reference/file-conventions/page#params-optional) \- 동적 라우트 매개변수(최소 하나의 샘플을 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)로 제공하지 않는 한). 자세한 패턴은 [Cache Components와 동적 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components)를 참고하세요.



page.tsx
[code]
    import { cookies, headers } from 'next/headers'
    import { Suspense } from 'react'
     
    async function RuntimeData({ searchParams }) {
      // Accessing request data
      const cookieStore = await cookies()
      const headerStore = await headers()
      const search = await searchParams
     
      return <div>Not in the static shell</div>
    }
[/code]

`RuntimeData` 컴포넌트를 사용하려면 `<Suspense>` 경계로 감싸세요:

page.tsx
[code]
    export default async function Page(props) {
      return (
        <>
          <h1>Part of the static shell</h1>
          {/* <p>Loading..</p> is part of the static shell */}
          <Suspense fallback={<p>Loading..</p>}>
            <RuntimeData searchParams={props.searchParams} />
            <div>Sibling excluded from static shell</div>
          </Suspense>
        </>
      )
    }
[/code]

위의 런타임 API에 접근하지 않고 요청 시점으로 미루고 싶다면 [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection)을 사용하세요.

> **알아두면 좋아요**: 런타임 데이터는 요청 컨텍스트가 필요하므로 `use cache`로 캐싱할 수 없습니다. 런타임 API에 접근하는 컴포넌트는 항상 `<Suspense>`로 감싸야 합니다. 다만 런타임 데이터에서 값을 추출해 캐시된 함수에 인자로 전달할 수 있습니다. 예시는 [런타임 데이터 사용](https://nextjs.org/docs/app/getting-started/cache-components#with-runtime-data) 섹션을 참고하세요.

쿠키 같은 런타임 데이터를 정적 셸을 막지 않고 읽는 방법 중 하나는 client context provider에 promise를 전달하는 것입니다. 예시는 [컨텍스트와 React.cache로 데이터 공유하기](https://nextjs.org/docs/app/getting-started/server-and-client-components#sharing-data-with-context-and-reactcache)를 참고하세요.

> **알아두면 좋아요:** `React.cache`는 `use cache` 경계 내부의 격리된 스코프에서 동작합니다. 자세한 내용은 [React.cache 격리](https://nextjs.org/docs/app/api-reference/directives/use-cache#reactcache-isolation)를 참고하세요.

### 비결정적 연산[](https://nextjs.org/docs/app/getting-started/cache-components#non-deterministic-operations)

`Math.random()`, `Date.now()`, `crypto.randomUUID()` 같은 연산은 실행될 때마다 다른 값을 생성합니다. 요청마다 고유한 값을 생성하도록 요청 시점에 실행되게 하려면, Cache Components는 이러한 연산을 동적 또는 런타임 데이터 접근 이후에 호출해 의도를 명시하도록 요구합니다.
[code] 
    import { connection } from 'next/server'
    import { Suspense } from 'react'
     
    async function UniqueContent() {
      // Explicitly defer to request time
      await connection()
     
      // Non-deterministic operations
      const random = Math.random()
      const now = Date.now()

const date = new Date()
      const uuid = crypto.randomUUID()
      const bytes = crypto.getRandomValues(new Uint8Array(16))
     
      return (
        <div>
          <p>{random}</p>
          <p>{now}</p>
          <p>{date.getTime()}</p>
          <p>{uuid}</p>
          <p>{bytes}</p>
        </div>
      )
    }
[/code]

`UniqueContent` 컴포넌트는 요청 시점까지 실행을 지연하므로 라우트에서 사용하려면 `<Suspense>` 로 감싸야 합니다:

page.tsx
[code]
    export default async function Page() {
      return (
        // <p>Loading..</p> is part of the static shell
        <Suspense fallback={<p>Loading..</p>}>
          <UniqueContent />
        </Suspense>
      )
    }
[/code]

들어오는 모든 요청은 서로 다른 난수, 날짜 등을 보게 됩니다.

> **알아두면 좋은 점** : `use cache` 로 비결정적 연산을 캐싱할 수 있습니다. 예시는 [with non-deterministic operations](https://nextjs.org/docs/app/getting-started/cache-components#with-non-deterministic-operations) 섹션을 확인하세요.

## `use cache` 사용하기[](https://nextjs.org/docs/app/getting-started/cache-components#using-use-cache)

[`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) 지시문은 비동기 함수와 컴포넌트의 반환 값을 캐싱합니다. 함수, 컴포넌트, 파일 단위 어디에나 적용할 수 있습니다.

인수와 상위 스코프에서 클로저로 포획된 값은 자동으로 [cache key](https://nextjs.org/docs/app/api-reference/directives/use-cache#cache-keys)에 포함되므로 서로 다른 입력마다 별도의 캐시 항목이 생성됩니다. 이를 통해 개인화 또는 매개변수화된 캐시 콘텐츠를 제공할 수 있습니다.

[동적 콘텐츠](https://nextjs.org/docs/app/getting-started/cache-components#dynamic-content)를 매 요청마다 원본에서 새로 가져올 필요가 없다면, 캐싱을 통해 프리렌더링 시 정적 셸에 포함하거나 런타임에서 여러 요청 간 결과를 재사용할 수 있습니다.

캐시된 콘텐츠는 캐시 수명에 기반한 자동 재검증 또는 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag), [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag)를 사용한 태그 기반 온디맨드 재검증 두 가지 방식으로 최신 상태를 유지할 수 있습니다.

> **알아두면 좋은 점** : 캐싱 가능한 항목과 인수 동작에 대한 자세한 내용은 [serialization requirements and constraints](https://nextjs.org/docs/app/api-reference/directives/use-cache#constraints)를 참조하세요.

### 프리렌더링 중[](https://nextjs.org/docs/app/getting-started/cache-components#during-prerendering)

[동적 콘텐츠](https://nextjs.org/docs/app/getting-started/cache-components#dynamic-content)가 외부 소스에서 가져오더라도 접근 사이에 변경될 가능성이 낮은 경우가 많습니다. 예를 들어 재고 변경 시에만 갱신되는 상품 카탈로그, 발행 후 거의 변하지 않는 블로그 글, 과거 날짜의 분석 보고서 등이 있습니다.

이 데이터가 [런타임 데이터](https://nextjs.org/docs/app/getting-started/cache-components#runtime-data)에 의존하지 않는다면 `use cache` 지시문으로 정적 HTML 셸에 포함할 수 있습니다. 캐시 사용 기간은 [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) 로 정의하세요.

재검증이 발생하면 정적 셸이 새 콘텐츠로 업데이트됩니다. 온디맨드 재검증에 대한 자세한 내용은 [Tagging and revalidating](https://nextjs.org/docs/app/getting-started/cache-components#tagging-and-revalidating)을 참고하세요.

app/page.tsx
[code]
    import { cacheLife } from 'next/cache'
     
    export default async function Page() {
      'use cache'
      cacheLife('hours')
     
      const users = await db.query('SELECT * FROM users')
     
      return (
        <ul>
          {users.map((user) => (
            <li key={user.id}>{user.name}</li>
          ))}
        </ul>
      )
    }
[/code]

`cacheLife` 함수는 캐시 동작을 제어하는 캐시 프로파일 이름(예: `'hours'`, `'days'`, `'weeks'`) 또는 사용자 정의 구성 객체를 받습니다:

app/page.tsx
[code]
    import { cacheLife } from 'next/cache'
     
    export default async function Page() {
      'use cache'
      cacheLife({
        stale: 3600, // 1 hour until considered stale
        revalidate: 7200, // 2 hours until revalidated
        expire: 86400, // 1 day until expired
      })
     
      const users = await db.query('SELECT * FROM users')
     
      return (
        <ul>
          {users.map((user) => (
            <li key={user.id}>{user.name}</li>
          ))}
        </ul>
      )
    }
[/code]

사용 가능한 프로파일과 사용자 정의 구성 옵션은 [`cacheLife` API reference](https://nextjs.org/docs/app/api-reference/functions/cacheLife)에서 확인할 수 있습니다.

### 런타임 데이터와 함께[](https://nextjs.org/docs/app/getting-started/cache-components#with-runtime-data)

런타임 데이터와 [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache)는 동일한 스코프에서 함께 사용할 수 없습니다. 대신 런타임 API에서 값을 추출하여 캐시된 함수의 인수로 전달하세요.

app/profile/page.tsx
[code]
    import { cookies } from 'next/headers'
    import { Suspense } from 'react'
     
    export default function Page() {
      // Page itself creates the dynamic boundary
      return (
        <Suspense fallback={<div>Loading...</div>}>
          <ProfileContent />
        </Suspense>
      )
    }
     
    // Component (not cached) reads runtime data
    async function ProfileContent() {
      const session = (await cookies()).get('session')?.value
     
      return <CachedContent sessionId={session} />
    }
     
    // Cached component/function receives data as props
    async function CachedContent({ sessionId }: { sessionId: string }) {
      'use cache'
      // sessionId becomes part of cache key
      const data = await fetchUserData(sessionId)
      return <div>{data}</div>
    }
[/code]

요청 시점에 일치하는 캐시 항목이 없다면 `CachedContent` 가 실행되고, 그 결과가 이후 요청을 위해 저장됩니다.

### 비결정적 연산과 함께[](https://nextjs.org/docs/app/getting-started/cache-components#with-non-deterministic-operations)

`use cache` 스코프 안에서는 비결정적 연산이 프리렌더링 동안 실행됩니다. 이는 모든 사용자에게 동일한 렌더링 결과를 제공하고 싶을 때 유용합니다:
[code] 
    export default async function Page() {
      'use cache'
     
      // Execute once, then cached for all requests
      const random = Math.random()
      const random2 = Math.random()
      const now = Date.now()
      const date = new Date()
      const uuid = crypto.randomUUID()
      const bytes = crypto.getRandomValues(new Uint8Array(16))
     
      return (
        <div>
          <p>
            {random} and {random2}
          </p>
          <p>{now}</p>
          <p>{date.getTime()}</p>
          <p>{uuid}</p>
          <p>{bytes}</p>
        </div>
      )
    }
[/code]

캐시가 재검증될 때까지 모든 요청은 동일한 난수, 타임스탬프, UUID를 포함한 라우트를 받게 됩니다.

### 태깅 및 재검증[](https://nextjs.org/docs/app/getting-started/cache-components#tagging-and-revalidating)

[`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) 로 캐시된 데이터를 태깅한 뒤, Server Actions에서 [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) 로 즉시 업데이트하거나, 허용 가능한 지연이 있다면 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) 로 온디맨드로 재검증하세요.

#### `updateTag` 사용 시[](https://nextjs.org/docs/app/getting-started/cache-components#with-updatetag)

동일한 요청 내에서 캐시 데이터를 만료시키고 즉시 새로 고쳐야 한다면 `updateTag` 를 사용하세요:

app/actions.ts
[code]
    import { cacheTag, updateTag } from 'next/cache'
     
    export async function getCart() {
      'use cache'
      cacheTag('cart')
      // fetch data
    }
     
    export async function updateCart(itemId: string) {
      'use server'
      // write data using the itemId
      // update the user cart
      updateTag('cart')
    }
[/code]

#### `revalidateTag` 사용 시[](https://nextjs.org/docs/app/getting-started/cache-components#with-revalidatetag)

`revalidateTag` 는 적절히 태깅된 캐시 항목만 stale-while-revalidate 방식으로 무효화하고 싶을 때 사용합니다. 이는 최종적 일관성을 허용할 수 있는 정적 콘텐츠에 적합합니다.

app/actions.ts
[code]
    import { cacheTag, revalidateTag } from 'next/cache'
     
    export async function getPosts() {
      'use cache'
      cacheTag('posts')
      // fetch data
    }
     
    export async function createPost(post: FormData) {
      'use server'
      // write data using the FormData
      revalidateTag('posts', 'max')
    }
[/code]

더 자세한 설명과 사용 예시는 [`use cache` API reference](https://nextjs.org/docs/app/api-reference/directives/use-cache)에서 확인하세요.

### 무엇을 캐시해야 할까요?[](https://nextjs.org/docs/app/getting-started/cache-components#what-should-i-cache)

캐시할 대상을 결정할 때는 원하는 UI 로딩 상태를 기준으로 생각하세요. 데이터가 런타임 데이터에 의존하지 않고 일정 기간 동안 여러 요청에 같은 값을 제공해도 괜찮다면, `cacheLife` 와 함께 `use cache` 로 그 동작을 서술하세요.

업데이트 메커니즘이 있는 CMS라면 더 긴 캐시 기간과 태그를 조합하고, `revalidateTag` 로 정적인 초기 UI를 재검증 대상으로 표시하는 방식을 고려하세요. 이 패턴을 사용하면 실제로 콘텐츠가 변경될 때만 업데이트하여 빠른 캐시 응답을 유지하면서도 불필요하게 캐시를 미리 만료시키지 않을 수 있습니다.

## 모두 종합하기[](https://nextjs.org/docs/app/getting-started/cache-components#putting-it-all-together)

다음은 정적 콘텐츠, 캐시된 동적 콘텐츠, 스트리밍 동적 콘텐츠가 단일 페이지에서 함께 작동하는 전체 예시입니다:

app/blog/page.tsx
[code]
    import { Suspense } from 'react'
    import { cookies } from 'next/headers'
    import { cacheLife } from 'next/cache'
    import Link from 'next/link'
     
    export default function BlogPage() {
      return (
        <>
          {/* Static content - prerendered automatically */}
          <header>
            <h1>Our Blog</h1>
            <nav>
              <Link href="/">Home</Link> | <Link href="/about">About</Link>
            </nav>
          </header>
     
          {/* Cached dynamic content - included in the static shell */}
          <BlogPosts />
     
          {/* Runtime dynamic content - streams at request time */}
          <Suspense fallback={<p>Loading your preferences...</p>}>
            <UserPreferences />
          </Suspense>
        </>
      )
    }
     
    // Everyone sees the same blog posts (revalidated every hour)
    async function BlogPosts() {
      'use cache'
      cacheLife('hours')
     
      const res = await fetch('https://api.vercel.app/blog')
      const posts = await res.json()
     
      return (
        <section>
          <h2>Latest Posts</h2>
          <ul>
            {posts.slice(0, 5).map((post: any) => (
              <li key={post.id}>
                <h3>{post.title}</h3>
                <p>
                  By {post.author} on {post.date}
                </p>
              </li>
            ))}
          </ul>
        </section>
      )
    }
     
    // Personalized per user based on their cookie
    async function UserPreferences() {
      const theme = (await cookies()).get('theme')?.value || 'light'
      const favoriteCategory = (await cookies()).get('category')?.value
     
      return (
        <aside>
          <p>Your theme: {theme}</p>
          {favoriteCategory && <p>Favorite category: {favoriteCategory}</p>}
        </aside>
      )
    }
[/code]

프리렌더링 중에는 헤더(정적)와 API에서 가져와 `use cache` 로 캐시된 블로그 글이 사용자 환경설정 대체 UI와 함께 정적 셸에 포함됩니다.

사용자가 페이지를 방문하면 헤더와 블로그 게시물이 포함된 이 프리렌더된 셸이 즉시 표시됩니다. 개인화된 기본 설정은 사용자의 쿠키에 의존하므로 요청 시점에만 스트리밍하면 됩니다. 이렇게 하면 초기 페이지 로드를 빠르게 유지하면서도 개인화된 콘텐츠를 제공할 수 있습니다.

## 메타데이터와 뷰포트[](https://nextjs.org/docs/app/getting-started/cache-components#metadata-and-viewport)

`generateMetadata`와 `generateViewport`는 페이지나 레이아웃을 렌더링하는 과정의 일부입니다. 프리렌더링 중에는 이 함수들의 런타임 데이터 또는 캐시되지 않은 동적 데이터 접근이 페이지의 나머지 부분과 별도로 추적됩니다.

페이지나 레이아웃을 프리렌더할 수 있지만 메타데이터나 뷰포트만 캐시되지 않은 동적 데이터나 런타임 데이터에 접근한다면 Next.js는 명시적인 선택을 요구합니다. 가능하면 데이터를 캐시하거나, 지연 렌더링이 의도적이라는 신호를 보내야 합니다. 처리 방법은 [Metadata with Cache Components](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#with-cache-components)와 [Viewport with Cache Components](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#with-cache-components)를 참조하세요.

## Cache Components 활성화[](https://nextjs.org/docs/app/getting-started/cache-components#enabling-cache-components)

Next 구성 파일에 [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) 옵션을 추가하면 Cache Components(PPR 포함)를 활성화할 수 있습니다:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      cacheComponents: true,
    }
     
    export default nextConfig
[/code]

> **알아두면 좋은 점:** Cache Components가 활성화되면 `GET` 라우트 핸들러는 페이지와 동일한 프리렌더링 모델을 따릅니다. 자세한 내용은 [Route Handlers with Cache Components](https://nextjs.org/docs/app/getting-started/route-handlers#with-cache-components)를 참조하세요.

## 내비게이션은 Activity 사용[](https://nextjs.org/docs/app/getting-started/cache-components#navigation-uses-activity)

[`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) 플래그가 활성화되면 Next.js는 클라이언트 측 내비게이션 중 컴포넌트 상태를 유지하기 위해 React의 [`<Activity>`](https://react.dev/reference/react/Activity) 컴포넌트를 사용합니다.

다른 경로로 이동할 때 이전 경로를 언마운트하는 대신 Next.js는 Activity 모드를 [`"hidden"`](https://react.dev/reference/react/Activity#activity)으로 설정합니다. 이는 다음을 의미합니다:

  * 경로 간 이동 시 컴포넌트 상태가 유지됩니다
  * 뒤로 이동하면 이전 경로가 상태를 그대로 유지한 채 다시 나타납니다
  * 경로가 숨겨지면 이펙트가 정리되고, 다시 표시될 때 재생성됩니다

이 동작은 사용자가 경로를 오가더라도 UI 상태(폼 입력, 확장된 섹션 등)를 유지하여 내비게이션 경험을 개선합니다.

> **알아두면 좋은 점**: Next.js는 휴리스틱을 사용해 최근에 방문한 일부 경로만 `"hidden"` 상태로 유지하고, 오래된 경로는 DOM에서 제거하여 과도한 증가를 방지합니다.

## 라우트 세그먼트 구성 마이그레이션[](https://nextjs.org/docs/app/getting-started/cache-components#migrating-route-segment-configs)

Cache Components를 활성화하면 여러 라우트 세그먼트 구성 옵션이 더 이상 필요하거나 지원되지 않습니다.

### `dynamic = "force-dynamic"`[](https://nextjs.org/docs/app/getting-started/cache-components#dynamic--force-dynamic)

**필요 없습니다.** 모든 페이지는 기본적으로 동적입니다.

app/page.tsx
[code]
    // Before - No longer needed
    export const dynamic = 'force-dynamic'
     
    export default function Page() {
      return <div>...</div>
    }
[/code]

app/page.tsx
[code]
    // After - Just remove it
    export default function Page() {
      return <div>...</div>
    }
[/code]

### `dynamic = "force-static"`[](https://nextjs.org/docs/app/getting-started/cache-components#dynamic--force-static)

먼저 해당 설정을 제거하세요. 개발 및 빌드 단계에서 처리되지 않은 동적 또는 런타임 데이터 접근이 감지되면 Next.js는 오류를 발생시킵니다. 그렇지 않으면 [프리렌더링](https://nextjs.org/docs/app/getting-started/cache-components#automatically-prerendered-content) 단계가 자동으로 정적 HTML 셸을 추출합니다.

동적 데이터 접근에는 [`use cache`](https://nextjs.org/docs/app/getting-started/cache-components#using-use-cache)를 데이터 접근 지점에 최대한 가깝게 추가하고 `'max'`와 같은 긴 [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife)를 지정하여 캐시된 동작을 유지하세요. 필요하면 페이지나 레이아웃의 상단에 추가할 수 있습니다.

런타임 데이터 접근(`cookies()`, `headers()` 등)의 경우 오류 메시지가 [이를 `Suspense`로 감싸](https://nextjs.org/docs/app/getting-started/cache-components#runtime-data)도록 안내합니다. 처음에 `force-static`을 사용했다면 요청 시 작업을 방지하기 위해 런타임 데이터 접근을 제거해야 합니다.

app/page.tsx
[code]
    // Before
    export const dynamic = 'force-static'
     
    export default async function Page() {
      const data = await fetch('https://api.example.com/data')
      return <div>...</div>
    }
[/code]

app/page.tsx
[code]
    import { cacheLife } from 'next/cache'
     
    // After - Use 'use cache' instead
    export default async function Page() {
      'use cache'
      cacheLife('max')
      const data = await fetch('https://api.example.com/data')
      return <div>...</div>
    }
[/code]

### `revalidate`[](https://nextjs.org/docs/app/getting-started/cache-components#revalidate)

**`cacheLife`로 대체하세요.** 라우트 세그먼트 구성 대신 `cacheLife` 함수를 사용해 캐시 기간을 정의하세요.
[code] 
    // Before
    export const revalidate = 3600 // 1 hour
     
    export default async function Page() {
      return <div>...</div>
    }
[/code]

app/page.tsx
[code]
    // After - Use cacheLife
    import { cacheLife } from 'next/cache'
     
    export default async function Page() {
      'use cache'
      cacheLife('hours')
      return <div>...</div>
    }
[/code]

### `fetchCache`[](https://nextjs.org/docs/app/getting-started/cache-components#fetchcache)

**필요 없습니다.** `use cache`가 활성화된 범위 내의 모든 데이터 페칭은 자동으로 캐시되므로 `fetchCache`는 더 이상 필요하지 않습니다.

app/page.tsx
[code]
    // Before
    export const fetchCache = 'force-cache'
[/code]

app/page.tsx
[code]
    // After - Use 'use cache' to control caching behavior
    export default async function Page() {
      'use cache'
      // All fetches here are cached
      return <div>...</div>
    }
[/code]

### `runtime = 'edge'`[](https://nextjs.org/docs/app/getting-started/cache-components#runtime--edge)

**지원되지 않습니다.** Cache Components는 Node.js 런타임이 필요하며 [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)에서는 오류가 발생합니다.

## 다음 단계

Cache Components용 구성 옵션에 대해 자세히 알아보세요.

### [cacheComponentsNext.js에서 cacheComponents 플래그를 활성화하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)### [use cacheNext.js 애플리케이션에서 "use cache" 지시문을 사용해 데이터를 캐시하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/directives/use-cache)### [cacheLife캐시된 함수나 컴포넌트의 만료 시간을 설정하는 cacheLife 함수를 사용하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/functions/cacheLife)### [cacheTagNext.js 애플리케이션에서 캐시 무효화를 관리하는 cacheTag 함수 사용 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/functions/cacheTag)### [revalidateTagrevalidateTag 함수의 API 레퍼런스입니다.](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)### [updateTagupdateTag 함수의 API 레퍼런스입니다.](https://nextjs.org/docs/app/api-reference/functions/updateTag)

도움이 되었나요?

지원됨.

보내기
