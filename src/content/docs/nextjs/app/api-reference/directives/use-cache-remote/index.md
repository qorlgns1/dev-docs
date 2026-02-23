---
title: '지시문: use cache: remote'
description: '소스 URL: https://nextjs.org/docs/app/api-reference/directives/use-cache-remote'
---

# 지시문: use cache: remote | Next.js
소스 URL: https://nextjs.org/docs/app/api-reference/directives/use-cache-remote

[API 참고 문서](https://nextjs.org/docs/app/api-reference)[지시문](https://nextjs.org/docs/app/api-reference/directives)use cache: remote

페이지 복사

# use cache: remote

마지막 업데이트 2026년 2월 20일

`use cache` 지시문은 대부분의 애플리케이션 요구 사항을 충족하지만, 캐시된 연산이 예상보다 자주 다시 실행되거나 업스트림 서비스(CMS, 데이터베이스, 외부 API 등)에 대한 요청이 늘어나는 경우가 있을 수 있습니다. 이는 `use cache`가 엔트리를 메모리에 저장하기 때문에 발생하며, 다음과 같은 태생적 한계가 있습니다:

  * 새로운 항목을 위해 기존 캐시 엔트리가 퇴거됨
  * 배포 환경의 메모리 제약
  * 요청 간 또는 서버 재시작 후 캐시가 유지되지 않음

`use cache`는 서버 측 캐싱 외에도 Next.js가 프리패치할 수 있는 대상과 클라이언트 측 내비게이션의 만료 시간을 정의하도록 알려 준다는 점에서 여전히 유용합니다.

`'use cache: remote'` 지시문은 캐시된 결과를 메모리 대신 원격 캐시에 저장하도록 선언적으로 지정해, 모든 서버 인스턴스가 공유하는 지속적인 캐싱을 제공합니다. 다만 인프라 비용과 캐시 조회 시 네트워크 지연이라는 트레이드오프가 따릅니다.

## 사용법[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#usage)

`'use cache: remote'`를 사용하려면 `next.config.ts` 파일에서 [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) 플래그를 활성화하세요:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      cacheComponents: true,
    }
     
    export default nextConfig
[/code]

그다음 원격 캐싱이 타당하다고 판단한 함수나 컴포넌트에 `'use cache: remote'`를 추가합니다. 핸들러 구현은 [`cacheHandlers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)를 통해 구성하며, 대부분의 호스팅 제공자는 이를 자동으로 제공해야 합니다. 셀프 호스팅 중이라면 `cacheHandlers` 구성 참조를 확인해 캐시 스토리지를 설정하세요.

### 원격 캐싱을 피해야 할 때[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#when-to-avoid-remote-caching)

  * 이미 서버 측 캐시 키-값 저장소로 데이터 레이어를 감싸고 있다면, 추가 캐싱 계층 없이 정적 셸에 데이터를 포함하기에 `use cache`로 충분할 수 있습니다
  * 연산이 근접성 또는 로컬 액세스로 이미 빠른 경우(< 50ms) 원격 캐시 조회가 성능 향상에 도움이 되지 않을 수 있습니다
  * 캐시 키가 요청마다 대부분 고유 값(검색 필터, 가격 범위, 사용자별 매개변수 등)을 갖는다면 캐시 활용률이 0에 가까워집니다
  * 데이터가 자주 변경된다면(수 초~수 분) 캐시 적중분이 빠르게 오래되어 미스와 업스트림 재검증 대기가 잦아집니다

### 원격 캐싱이 적합한 경우[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#when-remote-caching-makes-sense)

원격 캐싱은 콘텐츠가 정적 셸 밖에서 요청 시점으로 연기될 때 가장 큰 가치를 제공합니다. 이는 컴포넌트가 [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies), [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers), [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) 같은 요청 값을 참조하며 Suspense 경계 안에 배치될 때 흔히 나타납니다. 이 상황에서는:

  * 각 요청이 컴포넌트를 실행하고 캐시를 조회합니다
  * 서버리스 환경에서는 인스턴스마다 고유한 휘발성 메모리를 가지므로 캐시 적중률이 낮습니다
  * 원격 캐싱이 모든 인스턴스가 공유하는 캐시를 제공해 적중률을 높이고 백엔드 부하를 줄입니다

`'use cache: remote'`가 특히 설득력 있는 시나리오:

  * **레이트 리밋이 있는 API**: 업스트림 서비스에 레이트 리밋이나 쿼터가 있어 초과 위험이 있는 경우
  * **느린 백엔드 보호**: 트래픽 급증 시 데이터베이스나 API가 병목이 되는 경우
  * **비용이 큰 연산**: 반복 실행하기 부담스러운 데이터베이스 쿼리나 연산
  * **불안정하거나 신뢰도 낮은 서비스**: 간헐적으로 실패하거나 가용성 문제가 있는 외부 서비스

이러한 상황에서는 원격 캐싱의 비용과 지연이 레이트 리밋 오류, 백엔드 과부하, 높은 컴퓨팅 비용, 열화된 사용자 경험 같은 더 심각한 결과를 피하는 데 정당화됩니다.

정적 셸 콘텐츠의 경우 `use cache`로 충분한 편입니다. 업스트림 소스가 동시 재검증 요청을 처리할 수 없다면(예: 레이트 리밋된 CMS) `use cache: remote`가 공유 캐시 계층 역할을 합니다. 이는 데이터베이스 앞에 키-값 저장소를 두는 것과 동일한 패턴이지만, 코드로 선언합니다.

### `use cache`, `use cache: private`와의 차이점[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#how-use-cache-remote-differs-from-use-cache-and-use-cache-private)

Next.js는 각기 다른 사용 사례를 위한 세 가지 캐싱 지시문을 제공합니다:

Feature| `use cache`| `'use cache: remote'`| `'use cache: private'`  
---|---|---|---  
**서버 측 캐싱**| In-memory 또는 cache handler| Remote cache handler| 없음  
**캐시 범위**| 모든 사용자 간 공유| 모든 사용자 간 공유| 클라이언트별(브라우저)  
**cookies/headers 직접 접근**| 불가(인수로 전달 필요)| 불가(인수로 전달 필요)| 가능  
**서버 캐시 활용률**| 정적 셸 밖에서는 낮을 수 있음| 높음(인스턴스 간 공유)| 해당 없음  
**추가 비용**| 없음| 인프라(스토리지, 네트워크)| 없음  
**지연 영향**| 없음| Cache handler 조회| 없음  

### 런타임 데이터와 캐싱[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#caching-with-runtime-data)

`use cache`와 `'use cache: remote'`는 cookies나 search params 같은 런타임 값을 직접 접근할 수 없습니다. 이러한 값을 추출해 캐시된 함수에 인수로 전달할 수 있습니다. 이 패턴은 [with runtime data](https://nextjs.org/docs/app/getting-started/cache-components#with-runtime-data)를 참고하세요.

> **알아두면 좋습니다** : `use cache`는 엔트리를 메모리에 저장합니다. 서버리스 환경에서는 인스턴스 간 메모리가 공유되지 않고 요청 처리 후 삭제되므로 런타임 캐싱에서 캐시 미스가 잦습니다.

### 캐시 키 고려 사항[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#cache-key-considerations)

캐시 키에 포함할 값을 신중히 선택하세요. 고유 값이 늘어날수록 별도의 캐시 엔트리가 생성되어 활용률이 떨어집니다. 다음은 검색 필터를 포함한 예시입니다:

app/products/[category]/page.tsx
[code]
    import { Suspense } from 'react'
     
    export default async function ProductsPage({
      params,
      searchParams,
    }: {
      params: Promise<{ category: string }>
      searchParams: Promise<{ minPrice?: string }>
    }) {
      return (
        <Suspense fallback={<div>Loading...</div>}>
          <ProductList params={params} searchParams={searchParams} />
        </Suspense>
      )
    }
     
    async function ProductList({
      params,
      searchParams,
    }: {
      params: Promise<{ category: string }>
      searchParams: Promise<{ minPrice?: string }>
    }) {
      const { category } = await params
     
      const { minPrice } = await searchParams
     
      // Cache only on category (few unique values)
      // Don't include price filter (many unique values)
      const products = await getProductsByCategory(category)
     
      // Filter price in memory instead of creating cache entries
      // for every price value
      const filtered = minPrice
        ? products.filter((p) => p.price >= parseFloat(minPrice))
        : products
     
      return <div>{/* render filtered products */}</div>
    }
     
    async function getProductsByCategory(category: string) {
      'use cache: remote'
      // Only category is part of the cache key
      // Much better utilization than caching every price filter value
      return db.products.findByCategory(category)
    }
[/code]

이 예에서 원격 핸들러는 캐시 엔트리당 더 많은 데이터(카테고리 내 모든 상품)를 저장해 캐시 적중률을 높입니다. 캐시 미스 시 백엔드 호출 비용이 더 크다면, 더 큰 엔트리를 저장하는 비용을 감수할 가치가 있습니다.

동일한 원칙이 사용자별 데이터에도 적용됩니다. 사용자별 데이터를 그대로 캐싱하기보다 사용자 선호도를 활용해 공유 데이터를 캐싱하세요.

예를 들어 사용자 세션에 언어 선호도가 있다면 이를 추출해 공유 콘텐츠를 캐싱합니다:

  * 사용자별 엔트리를 생성하는 `getUserProfile(sessionID)` 원격 캐싱 대신
  * 언어별 엔트리를 생성하는 `getCMSContent(language)`를 원격 캐싱

app/components/welcome-message.tsx
[code]
    import { cookies } from 'next/headers'
    import { cacheLife } from 'next/cache'
     
    export async function WelcomeMessage() {
      // Extract the language preference (not unique per user)
      const language = (await cookies()).get('language')?.value || 'en'
     
      // Cache based on language (few unique values: en, es, fr, de, etc.)
      // All users who prefer 'en' share the same cache entry
      const content = await getCMSContent(language)
     
      return <div>{content.welcomeMessage}</div>
    }
     
    async function getCMSContent(language: string) {
      'use cache: remote'
      cacheLife({ expire: 3600 })
      // Creates ~10-50 cache entries (one per language)
      // instead of thousands (one per user)
      return cms.getHomeContent(language)
    }
[/code]

이렇게 하면 동일한 언어를 선호하는 모든 사용자가 하나의 캐시 엔트리를 공유해 캐시 활용률을 높이고 CMS 부하를 줄입니다.

두 예 모두 동일한 패턴을 따릅니다: 고유 값이 적은 차원을 찾고(카테고리 vs. 가격, 언어 vs. 사용자 ID) 해당 차원으로 캐싱하며, 나머지는 메모리에서 필터링하거나 선택합니다.

`getUserProfile`이 사용하는 서비스가 프런트엔드 부하를 감당하지 못하더라도, 짧은 `cacheLife`를 설정한 `use cache` 지시문으로 메모리 캐싱을 사용할 수 있습니다. 그러나 대부분의 사용자 데이터는 위 가이드라인처럼 이미 키-값 저장소로 감싼 소스에서 직접 가져오는 것이 일반적입니다.

[`'use cache: private'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)는 컴플라이언스 요구사항이 있거나 런타임 데이터를 인수로 전달하도록 리팩터링할 수 없을 때만 사용하세요.

### 중첩 규칙[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#nesting-rules)

원격 캐시는 다음과 같은 중첩 규칙을 가집니다:

  * 원격 캐시는 다른 원격 캐시(`'use cache: remote'`) 안에 중첩될 수 있습니다
  * 원격 캐시는 일반 캐시(`'use cache'`) 안에 중첩될 수 있습니다
  * 원격 캐시는 프라이빗 캐시(`'use cache: private'`) 안에 중첩될 수 없습니다
  * 프라이빗 캐시는 원격 캐시 안에 중첩될 수 없습니다

[code] 
    // VALID: Remote inside remote
    async function outerRemote() {
      'use cache: remote'
      const result = await innerRemote()
      return result
    }
     
    async function innerRemote() {
      'use cache: remote'
      return getData()
    }
     
    // VALID: Remote inside regular cache
    async function outerCache() {
      'use cache'
      // The inner remote cache will work when deferred to request time
      const result = await innerRemote()
      return result
    }
     
    async function innerRemote() {
      'use cache: remote'
      return getData()
    }
     
    // INVALID: Remote inside private
    async function outerPrivate() {
      'use cache: private'
      const result = await innerRemote() // Error!
      return result
    }
     
    async function innerRemote() {
      'use cache: remote'
      return getData()
    }
[/code]

// INVALID: Private inside remote
    async function outerRemote() {
      'use cache: remote'
      const result = await innerPrivate() // Error!
      return result
    }
     
    async function innerPrivate() {
      'use cache: private'
      return getData()
    }
[/code]

## 예시[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#examples)

다음 예시는 `'use cache: remote'`를 사용하는 일반적인 패턴을 보여 줍니다. `cacheLife` 매개변수(`stale`, `revalidate`, `expire`)에 대한 자세한 내용은 [`cacheLife` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/cacheLife)를 참고하세요.

### 사용자 선호도 기반[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#with-user-preferences)

사용자의 통화 선호도를 기준으로 제품 가격을 캐싱합니다. 통화 정보가 쿠키에 저장되므로 이 컴포넌트는 요청 시점에 렌더링됩니다. 동일한 통화를 사용하는 모든 사용자가 캐시된 가격을 공유하고, 서버리스 환경에서는 모든 인스턴스가 동일한 원격 캐시를 공유하기 때문에 원격 캐싱이 유용합니다.

app/product/[id]/page.tsx

JavaScriptTypeScript
[code]
    import { Suspense } from 'react'
    import { cookies } from 'next/headers'
    import { cacheTag, cacheLife } from 'next/cache'
     
    export async function generateStaticParams() {
      return [{ id: '1' }, { id: '2' }, { id: '3' }]
    }
     
    export default async function ProductPage({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
     
      return (
        <div>
          <ProductDetails id={id} />
          <Suspense fallback={<div>Loading price...</div>}>
            <ProductPrice productId={id} />
          </Suspense>
        </div>
      )
    }
     
    function ProductDetails({ id }: { id: string }) {
      return <div>Product: {id}</div>
    }
     
    async function ProductPrice({ productId }: { productId: string }) {
      // Reading cookies defers this component to request time
      const currency = (await cookies()).get('currency')?.value ?? 'USD'
     
      // Cache the price per product and currency combination
      // All users with the same currency share this cache entry
      const price = await getProductPrice(productId, currency)
     
      return (
        <div>
          Price: {price} {currency}
        </div>
      )
    }
     
    async function getProductPrice(productId: string, currency: string) {
      'use cache: remote'
      cacheTag(`product-price-${productId}`)
      cacheLife({ expire: 3600 }) // 1 hour
     
      // Cached per (productId, currency) - few currencies means high cache utilization
      return db.products.getPrice(productId, currency)
    }
[/code]

### 데이터베이스 부하 감소[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#reducing-database-load)

비용이 큰 데이터베이스 쿼리를 캐싱하여 데이터베이스 부하를 줄입니다. 이 예제에서는 `cookies()`, `headers()`, `searchParams`에 접근하지 않습니다. 통계 정보를 정적 셸에 포함하지 말아야 한다면 [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection)을 사용해 명시적으로 요청 시점으로 연기할 수 있습니다.

app/dashboard/page.tsx
[code]
    import { Suspense } from 'react'
    import { connection } from 'next/server'
    import { cacheLife, cacheTag } from 'next/cache'
     
    export default function DashboardPage() {
      return (
        <Suspense fallback={<div>Loading stats...</div>}>
          <DashboardStats />
        </Suspense>
      )
    }
     
    async function DashboardStats() {
      // Defer to request time
      await connection()
     
      const stats = await getGlobalStats()
     
      return <StatsDisplay stats={stats} />
    }
     
    async function getGlobalStats() {
      'use cache: remote'
      cacheTag('global-stats')
      cacheLife({ expire: 60 }) // 1 minute
     
      // This expensive database query is cached and shared across all users,
      // reducing load on your database
      const stats = await db.analytics.aggregate({
        total_users: 'count',
        active_sessions: 'count',
        revenue: 'sum',
      })
     
      return stats
    }
[/code]

이 설정이면 대시보드를 방문하는 사용자가 얼마나 많든 상관없이 업스트림 데이터베이스는 최대 분당 한 번만 요청을 받습니다.

### 스트리밍 컨텍스트의 API 응답[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#api-responses-in-streaming-contexts)

스트리밍 중이거나 동적 작업 이후에 가져오는 API 응답을 캐싱합니다.

app/feed/page.tsx
[code]
    import { Suspense } from 'react'
    import { connection } from 'next/server'
    import { cacheLife, cacheTag } from 'next/cache'
     
    export default async function FeedPage() {
      return (
        <div>
          <Suspense fallback={<Skeleton />}>
            <FeedItems />
          </Suspense>
        </div>
      )
    }
     
    async function FeedItems() {
      // Defer to request time
      await connection()
     
      const items = await getFeedItems()
     
      return items.map((item) => <FeedItem key={item.id} item={item} />)
    }
     
    async function getFeedItems() {
      'use cache: remote'
      cacheTag('feed-items')
      cacheLife({ expire: 120 }) // 2 minutes
     
      // This API call is cached, reducing requests to your external service
      const response = await fetch('https://api.example.com/feed')
      return response.json()
    }
[/code]

### 동적 검사 이후의 계산된 데이터[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#computed-data-after-dynamic-checks)

동적 보안 또는 기능 검사 뒤에 수행되는 비용이 큰 계산을 캐싱합니다.

app/reports/page.tsx
[code]
    import { connection } from 'next/server'
    import { cacheLife } from 'next/cache'
     
    export default async function ReportsPage() {
      // Defer to request time (for security check)
      await connection()
     
      const report = await generateReport()
     
      return <ReportViewer report={report} />
    }
     
    async function generateReport() {
      'use cache: remote'
      cacheLife({ expire: 3600 }) // 1 hour
     
      // This expensive computation is cached and shared across all authorized users,
      // avoiding repeated calculations
      const data = await db.transactions.findMany()
     
      return {
        totalRevenue: calculateRevenue(data),
        topProducts: analyzeProducts(data),
        trends: calculateTrends(data),
      }
    }
[/code]

### 혼합 캐싱 전략[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#mixed-caching-strategies)

최적의 성능을 위해 정적, 원격, 프라이빗 캐싱을 조합합니다.

app/product/[id]/page.tsx
[code]
    import { Suspense } from 'react'
    import { connection } from 'next/server'
    import { cookies } from 'next/headers'
    import { cacheLife, cacheTag } from 'next/cache'
     
    // Static product data - prerendered at build time
    async function getProduct(id: string) {
      'use cache'
      cacheTag(`product-${id}`)
     
      // This is cached at build time and shared across all users
      return db.products.find({ where: { id } })
    }
     
    // Shared pricing data - cached at runtime in remote handler
    async function getProductPrice(id: string) {
      'use cache: remote'
      cacheTag(`product-price-${id}`)
      cacheLife({ expire: 300 }) // 5 minutes
     
      // This is cached at runtime and shared across all users
      return db.products.getPrice({ where: { id } })
    }
     
    // User-specific recommendations - private cache per user
    async function getRecommendations(productId: string) {
      'use cache: private'
      cacheLife({ expire: 60 }) // 1 minute
     
      const sessionId = (await cookies()).get('session-id')?.value
     
      // This is cached per-user and never shared
      return db.recommendations.findMany({
        where: { productId, sessionId },
      })
    }
     
    export default async function ProductPage({ params }) {
      const { id } = await params
     
      // Static product data
      const product = await getProduct(id)
     
      return (
        <div>
          <ProductDetails product={product} />
     
          {/* Dynamic shared price */}
          <Suspense fallback={<PriceSkeleton />}>
            <ProductPriceComponent productId={id} />
          </Suspense>
     
          {/* Dynamic personalized recommendations */}
          <Suspense fallback={<RecommendationsSkeleton />}>
            <ProductRecommendations productId={id} />
          </Suspense>
        </div>
      )
    }
     
    function ProductDetails({ product }) {
      return (
        <div>
          <h1>{product.name}</h1>
          <p>{product.description}</p>
        </div>
      )
    }
     
    async function ProductPriceComponent({ productId }) {
      // Defer to request time
      await connection()
     
      const price = await getProductPrice(productId)
      return <div>Price: ${price}</div>
    }
     
    async function ProductRecommendations({ productId }) {
      const recommendations = await getRecommendations(productId)
      return <RecommendationsList items={recommendations} />
    }
     
    function PriceSkeleton() {
      return <div>Loading price...</div>
    }
     
    function RecommendationsSkeleton() {
      return <div>Loading recommendations...</div>
    }
     
    function RecommendationsList({ items }) {
      return (
        <ul>
          {items.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      )
    }
[/code]

> **알아두면 좋아요** :
> 
>   * 원격 캐시는 서버 측 캐시 핸들러에 저장되며 모든 사용자가 공유합니다.
>   * `'use cache: remote'`는 [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache)가 서버 측 캐시 적중을 제공하지 못할 수 있는 정적 셸 외부에서도 작동합니다.
>   * [`cacheTag()`](https://nextjs.org/docs/app/api-reference/functions/cacheTag)와 [`revalidateTag()`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 사용하면 원격 캐시를 온디맨드로 무효화할 수 있습니다.
>   * [`cacheLife()`](https://nextjs.org/docs/app/api-reference/functions/cacheLife)를 사용해 캐시 만료를 구성하세요.
>   * 사용자별 데이터에는 `'use cache: remote'` 대신 [`'use cache: private'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)를 사용하세요.
>   * 원격 캐시는 계산하거나 가져온 데이터를 서버 측에 저장해 오리진 부하를 줄입니다.
> 

## 플랫폼 지원[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#platform-support)

Deployment Option| Supported  
---|---  
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| Yes  
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| Yes  
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| No  
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| Yes  
  
## 버전 기록[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#version-history)

Version| Changes  
---|---  
`v16.0.0`| `"use cache: remote"`가 Cache Components 기능과 함께 활성화되었습니다.  
  
## 관련

관련 API 레퍼런스를 확인하세요.

### [use cache Next.js 애플리케이션에서 데이터를 캐시하기 위해 "use cache" 지시어를 사용하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/directives/use-cache)
### [use cache: private 런타임 요청 API에 접근하는 함수를 캐시하기 위해 "use cache: private" 지시어를 사용하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)
### [cacheComponents Next.js에서 cacheComponents 플래그를 활성화하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
### [cacheHandlers Next.js의 use cache 지시어에 사용할 사용자 지정 캐시 핸들러를 구성하세요.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)
### [cacheLife 캐시된 함수나 컴포넌트의 만료 시간을 설정하기 위해 cacheLife 함수를 사용하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
### [cacheTag Next.js 애플리케이션에서 캐시 무효화를 관리하기 위해 cacheTag 함수를 사용하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
### [connection connection 함수에 대한 API 참조입니다.](https://nextjs.org/docs/app/api-reference/functions/connection)

도움이 되었나요?

지원됨.

보내기
