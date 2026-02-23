---
title: '가이드: 공개 페이지'
description: '공개 페이지는 모든 사용자에게 동일한 콘텐츠를 보여줍니다. 대표적인 예로 랜딩 페이지, 마케팅 페이지, 제품 페이지가 있습니다.'
---

# 가이드: 공개 페이지 | Next.js

출처 URL: https://nextjs.org/docs/app/guides/public-static-pages

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)공개 페이지

페이지 복사

# 공개 페이지 구축하기

최종 업데이트 2026년 2월 20일

공개 페이지는 모든 사용자에게 동일한 콘텐츠를 보여줍니다. 대표적인 예로 랜딩 페이지, 마케팅 페이지, 제품 페이지가 있습니다.

데이터가 공유되므로 이러한 종류의 페이지는 미리 [prerendered](https://nextjs.org/docs/app/glossary#prerendering)해 두고 재사용할 수 있습니다. 이렇게 하면 페이지 로드가 빨라지고 서버 비용이 낮아집니다.

이 가이드는 사용자 간에 데이터를 공유하는 공개 페이지를 만드는 방법을 보여줍니다.

## 예제[](https://nextjs.org/docs/app/guides/public-static-pages#example)

예제로 제품 목록 페이지를 만들어 보겠습니다.

정적인 헤더로 시작해 비동기 외부 데이터가 있는 제품 목록을 추가하고, 응답을 막지 않고 렌더링하는 방법을 배웁니다. 마지막으로 전체 페이지를 [request-time rendering](https://nextjs.org/docs/app/glossary#request-time-rendering)으로 전환하지 않고 사용자별 프로모션 배너를 추가합니다.

이 예제에 사용된 리소스는 여기에서 확인할 수 있습니다.

  * [비디오](https://youtu.be/F6romq71KtI)
  * [데모](https://cache-components-public-pages.labs.vercel.dev/)
  * [코드](https://github.com/vercel-labs/cache-components-public-pages)



### 1단계: 간단한 헤더 추가[](https://nextjs.org/docs/app/guides/public-static-pages#step-1-add-a-simple-header)

간단한 헤더부터 시작하겠습니다.

app/products/page.tsx
[code]
    // Static component
    function Header() {
      return <h1>Shop</h1>
    }
     
    export default async function Page() {
      return (
        <>
          <Header />
        </>
      )
    }
[/code]

#### 정적 컴포넌트[](https://nextjs.org/docs/app/guides/public-static-pages#static-components)

`<Header />` 컴포넌트는 외부 데이터, 요청 헤더, 경로 매개변수, 현재 시간, 랜덤 값처럼 요청마다 달라지는 입력에 의존하지 않습니다.

출력이 변하지 않고 미리 결정될 수 있으므로 이러한 컴포넌트를 **정적** 컴포넌트라고 합니다. 대기해야 할 요청이 없으므로 Next.js는 [build time](https://nextjs.org/docs/app/glossary#build-time)에 페이지를 안전하게 **사전 렌더링**할 수 있습니다.

이는 [`next build`](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options)를 실행해 확인할 수 있습니다.

터미널
[code]
    Route (app)      Revalidate  Expire
    ┌ ○ /products           15m      1y
    └ ○ /_not-found
     
    ○  (Static)  prerendered as static content
[/code]

제품 경로에 별도 설정을 추가하지 않았어도 정적으로 표시되는 것을 확인할 수 있습니다.

### 2단계: 제품 목록 추가[](https://nextjs.org/docs/app/guides/public-static-pages#step-2-add-the-product-list)

이제 제품 목록을 가져와 렌더링해 보겠습니다.

app/products/page.tsx
[code]
    import db from '@/db'
    import { List } from '@/app/products/ui'
     
    function Header() {}
     
    // Dynamic component
    async function ProductList() {
      const products = await db.product.findMany()
      return <List items={products} />
    }
     
    export default async function Page() {
      return (
        <>
          <Header />
          <ProductList />
        </>
      )
    }
[/code]

헤더와 달리 제품 목록은 외부 데이터에 의존합니다.

#### 동적 컴포넌트[](https://nextjs.org/docs/app/guides/public-static-pages#dynamic-components)

이 데이터는 시간이 지나면서 **변할 수 있으므로**, 렌더링 결과가 더 이상 안정적이라고 보장할 수 없습니다. 따라서 제품 목록은 **동적** 컴포넌트가 됩니다.

가이드가 없다면 프레임워크는 매 사용자 요청마다 **신선한** 데이터를 가져오길 원한다고 간주합니다. 이는 새로운 서버 요청이 페이지를 렌더링하는 표준 웹 동작을 반영한 설계입니다.

그러나 이 컴포넌트를 요청 시점에 렌더링하면 데이터를 가져오는 동안 **전체** 경로의 응답이 지연됩니다. 페이지를 새로고침하면 이를 확인할 수 있습니다.

헤더가 즉시 렌더링되더라도 제품 목록이 데이터를 가져올 때까지 브라우저에 전송될 수 없습니다.

이 성능 절벽을 방지하기 위해 Next.js는 데이터를 처음 **await**할 때 [경고](https://nextjs.org/docs/messages/blocking-route)를 보여 줍니다: `Blocking data was accessed outside of Suspense`

이 시점에서 응답을 **차단 해제**하는 방법을 결정해야 합니다. 선택지는 다음과 같습니다.

  * 컴포넌트를 [**Cache**](https://nextjs.org/docs/app/glossary#cache-components)해 **안정적**으로 만든 뒤 페이지의 나머지와 함께 사전 렌더링합니다.
  * 컴포넌트를 [**Stream**](https://nextjs.org/docs/app/glossary#streaming)해 **논블로킹**으로 만들고 페이지의 나머지가 기다리지 않게 합니다.



우리 사례에서는 제품 카탈로그가 모든 사용자에게 공유되므로 캐싱이 올바른 선택입니다.

### 캐시 컴포넌트[](https://nextjs.org/docs/app/guides/public-static-pages#cache-components)

[`'use cache'`](https://nextjs.org/docs/app/api-reference/directives/use-cache) 지시문으로 함수를 캐시 가능하게 표시할 수 있습니다.

app/products/page.tsx
[code]
    import db from '@/db'
    import { List } from '@/app/products/ui'
     
    function Header() {}
     
    // Cache component
    async function ProductList() {
      'use cache'
      const products = await db.product.findMany()
      return <List items={products} />
    }
     
    export default async function Page() {
      return (
        <>
          <Header />
          <ProductList />
        </>
      )
    }
[/code]

이렇게 하면 [cache component](https://nextjs.org/docs/app/glossary#cache-components)가 됩니다. 처음 실행될 때 반환한 값이 캐시되어 재사용됩니다.

요청이 도착하기 **전**에 캐시 컴포넌트의 입력이 준비되어 있으면 정적 컴포넌트처럼 사전 렌더링할 수 있습니다.

다시 새로고침하면 캐시 컴포넌트가 응답을 차단하지 않으므로 페이지가 즉시 로드되는 것을 볼 수 있습니다. `next build`를 다시 실행하면 페이지가 여전히 정적임을 확인할 수 있습니다.

터미널
[code]
    Route (app)      Revalidate  Expire
    ┌ ○ /products           15m      1y
    └ ○ /_not-found
     
    ○  (Static)  prerendered as static content
[/code]

하지만 페이지가 영원히 정적으로 남아 있지는 않습니다.

### 3단계: 동적 프로모션 배너 추가[](https://nextjs.org/docs/app/guides/public-static-pages#step-3-add-a-dynamic-promotion-banner)

언젠가는 간단한 페이지에도 동적 콘텐츠가 필요해집니다. 이를 보여 주기 위해 프로모션 배너를 추가해 보겠습니다.

app/products/page.tsx
[code]
    import db from '@/db'
    import { List, Promotion } from '@/app/products/ui'
    import { getPromotion } from '@/app/products/data'
     
    function Header() {}
     
    async function ProductList() {}
     
    // Dynamic component
    async function PromotionContent() {
      const promotion = await getPromotion()
      return <Promotion data={promotion} />
    }
     
    export default async function Page() {
      return (
        <>
          <PromotionContent />
          <Header />
          <ProductList />
        </>
      )
    }
[/code]

다시 한 번, 이 컴포넌트는 동적으로 시작합니다. 그리고 이전과 마찬가지로 차단 동작을 도입하면 Next.js 경고가 발생합니다.

지난번에는 데이터가 공유되어 캐싱할 수 있었습니다. 이번에는 프로모션이 사용자 위치나 A/B 테스트 같은 요청별 입력에 의존하므로 캐싱만으로 차단 동작을 해결할 수 없습니다.

### 부분 사전 렌더링[](https://nextjs.org/docs/app/guides/public-static-pages#partial-prerendering)

동적 콘텐츠를 추가한다고 해서 완전히 차단되는 렌더로 돌아갈 필요는 없습니다. 스트리밍으로 응답을 차단 해제할 수 있습니다.

Next.js는 기본적으로 스트리밍을 지원합니다. [Suspense 경계](https://nextjs.org/docs/app/glossary#suspense-boundary)를 사용해 프레임워크에 스트리밍 응답을 _청크_로 나누는 지점과 콘텐츠 로딩 중에 표시할 폴백 UI를 알려줄 수 있습니다.

app/products/page.tsx
[code]
    import { Suspense } from 'react'
    import db from '@/db'
    import { List, Promotion, PromotionSkeleton } from '@/app/products/ui'
    import { getPromotion } from '@/app/products/data'
     
    function Header() {}
     
    async function ProductList() {}
     
    // Dynamic component (streamed)
    async function PromotionContent() {
      const promotion = await getPromotion()
      return <Promotion data={promotion} />
    }
     
    export default async function Page() {
      return (
        <>
          <Suspense fallback={<PromotionSkeleton />}>
            <PromotionContent />
          </Suspense>
          <Header />
          <ProductList />
        </>
      )
    }
[/code]

폴백은 정적 콘텐츠와 캐시된 콘텐츠와 함께 사전 렌더링됩니다. 내부 컴포넌트는 비동기 작업이 완료되면 나중에 스트리밍됩니다.

이 변경을 통해 Next.js는 사전 렌더링 가능한 작업과 요청 시점 작업을 분리할 수 있으며, 경로는 [부분 사전 렌더링](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr) 상태가 됩니다.

다시 `next build`를 실행해 이를 확인할 수 있습니다.

터미널
[code]
    Route (app)      Revalidate  Expire
    ┌ ◐ /products    15m      1y
    └ ◐ /_not-found
     
    ◐  (Partial Prerender)  Prerendered as static HTML with dynamic server-streamed content
[/code]

[**build time**](https://nextjs.org/docs/app/glossary#build-time)에 헤더, 제품 목록, 프로모션 폴백을 포함한 페이지 대부분이 렌더링되어 캐시되고 콘텐츠 전송 네트워크에 푸시됩니다.

[**request time**](https://nextjs.org/docs/app/glossary#request-time)에 사전 렌더된 부분이 사용자와 가까운 CDN 노드에서 즉시 제공됩니다.

동시에 사용자별 프로모션이 서버에서 렌더링되고 클라이언트로 스트리밍되어 폴백 슬롯에 교체됩니다.

마지막으로 페이지를 새로고침하면 페이지 대부분이 즉시 로드되고, 동적 부분은 준비되는 대로 스트리밍되는 것을 볼 수 있습니다.

### 다음 단계[](https://nextjs.org/docs/app/guides/public-static-pages#next-steps)

대부분 정적이지만 일부 동적 콘텐츠를 포함하는 페이지를 만드는 방법을 배웠습니다.

정적 페이지에서 시작해 비동기 작업을 추가하고, 사전 렌더링할 수 있는 부분은 캐싱하고 그렇지 않은 부분은 스트리밍하여 차단 동작을 해결했습니다.

앞으로의 가이드에서는 다음을 학습할 예정입니다.

  * 사전 렌더링된 페이지나 캐시된 데이터를 재검증하는 방법.
  * 경로 매개변수로 동일한 페이지의 변형을 만드는 방법.
  * 개인화된 사용자 데이터를 사용하는 비공개 페이지를 만드는 방법.



도움이 되었나요?

지원됨.

보내기
