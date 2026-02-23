---
title: '<Suspense> 외부에서 캐시되지 않은 데이터에 접근했습니다'
description: '기능을 활성화하면 Next.js는 모든 사용자 요청마다 접근해야 하는 데이터를 기다리는 컴포넌트를 부모  경계 안에 둘 것으로 예상합니다. 이 요구 사항의 목적은 Next.js가 해당 데이터를 접근하고 렌더링하는 동안 유용한 폴백 UI를 제공하려는 것입니다.'
---

# `<Suspense>` 외부에서 캐시되지 않은 데이터에 접근했습니다 | Next.js

출처 URL: https://nextjs.org/docs/messages/blocking-route

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)`<Suspense>` 외부에서 캐시되지 않은 데이터에 접근했습니다

# `<Suspense>` 외부에서 캐시되지 않은 데이터에 접근했습니다

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/blocking-route#why-this-error-occurred)

`cacheComponents` 기능을 활성화하면 Next.js는 모든 사용자 요청마다 접근해야 하는 데이터를 기다리는 컴포넌트를 부모 `Suspense` 경계 안에 둘 것으로 예상합니다. 이 요구 사항의 목적은 Next.js가 해당 데이터를 접근하고 렌더링하는 동안 유용한 폴백 UI를 제공하려는 것입니다.

요청 헤더처럼 사용자 요청을 처리할 때만 본질적으로 사용할 수 있는 데이터도 있지만, Next.js는 기본적으로 모든 비동기 데이터가 사용자 요청을 처리할 때마다 접근된다고 가정하며, `"use cache"`로 명시적으로 캐시하지 않는 한 그렇습니다.

이 오류를 해결하는 정확한 방법은 어떤 데이터를 접근하는지와 Next.js 앱이 어떻게 동작하길 원하는지에 따라 달라집니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/blocking-route#possible-ways-to-fix-it)

### 데이터에 접근하기[](https://nextjs.org/docs/messages/blocking-route#accessing-data)

`fetch`, 데이터베이스 클라이언트, 기타 비동기 IO를 수행하는 모듈을 사용해 데이터를 가져오면 Next.js는 해당 데이터를 모든 사용자 요청 시마다 로드하려는 의도로 해석합니다.

이 데이터를 페이지를 완전 혹은 부분적으로 프리렌더링하는 동안 사용하려면 `"use cache"`를 사용해 캐시해야 합니다.

이전:

app/page.js
[code]
    async function getRecentArticles() {
      return db.query(...)
    }
     
    export default async function Page() {
      const articles = await getRecentArticles(token);
      return <ArticleList articles={articles}>
    }
[/code]

이후:

app/page.js
[code]
    import { cacheTag, cacheLife } from 'next/cache'
     
    async function getRecentArticles() {
      "use cache"
      // This cache can be revalidated by webhook or server action
      // when you call revalidateTag("articles")
      cacheTag("articles")
      // This cache will revalidate after an hour even if no explicit
      // revalidate instruction was received
      cacheLife('hours')
      return db.query(...)
    }
     
    export default async function Page() {
      const articles = await getRecentArticles(token);
      return <ArticleList articles={articles}>
    }
[/code]

이 데이터가 모든 사용자 요청마다 접근되어야 한다면 React의 `Suspense`를 사용해 폴백 UI를 제공해야 합니다. `Suspense` 경계를 어디에 배치할지는 렌더링하려는 폴백 UI의 종류에 따라 결정하면 됩니다. 데이터를 접근하는 컴포넌트 바로 상위나 루트 레이아웃에 둘 수도 있습니다.

이전:

app/page.js
[code]
    async function getLatestTransactions() {
      return db.query(...)
    }
     
    export default async function Page() {
      const transactions = await getLatestTransactions(token);
      return <TransactionList transactions={transactions}>
    }
[/code]

이후:

app/page.js
[code]
    import { Suspense } from 'react'
     
    async function TransactionList() {
      const transactions = await db.query(...)
      return ...
    }
     
    function TransactionSkeleton() {
      return <ul>...</ul>
    }
     
    export default async function Page() {
      return (
        <Suspense fallback={<TransactionSkeleton />}>
          <TransactionList/>
        </Suspense>
      )
    }
[/code]

### Headers[](https://nextjs.org/docs/messages/blocking-route#headers)

`headers()`, `cookies()`, `draftMode()`로 요청 헤더에 접근하고 있다면, 이러한 API 사용 위치를 기존 컴포넌트 트리의 더 깊은 곳으로 옮길 수 있는지 검토하세요.

이전:

app/inbox.js
[code]
    export async function Inbox({ token }) {
      const email = await getEmail(token)
      return (
        <ul>
          {email.map((e) => (
            <EmailRow key={e.id} />
          ))}
        </ul>
      )
    }
[/code]

app/page.js
[code]
    import { cookies } from 'next/headers'
     
    import { Inbox } from './inbox'
     
    export default async function Page() {
      const token = (await cookies()).get('token')
      return (
        <Suspense fallback="loading your inbox...">
          <Inbox token={token}>
        </Suspense>
      )
    }
[/code]

이후:

app/inbox.js
[code]
    import { cookies } from 'next/headers'
     
    export async function Inbox() {
      const token = (await cookies()).get('token')
      const email = await getEmail(token)
      return (
        <ul>
          {email.map((e) => (
            <EmailRow key={e.id} />
          ))}
        </ul>
      )
    }
[/code]

app/page.js
[code]
    import { Inbox } from './inbox'
     
    export default async function Page() {
      return (
        <Suspense fallback="loading your inbox...">
          <Inbox>
        </Suspense>
      )
    }
[/code]

또는 요청 헤더에 접근하는 컴포넌트 상단에 `Suspense` 경계를 추가할 수도 있습니다.

### Params 및 SearchParams[](https://nextjs.org/docs/messages/blocking-route#params-and-searchparams)

레이아웃 `params`, 페이지 `params`, `searchParams` props는 Promise입니다. 레이아웃이나 페이지 컴포넌트에서 바로 await하면 실제로 필요한 위치보다 더 상위에서 props에 접근하게 될 수 있습니다. 이 props를 Promise 형태로 더 깊은 컴포넌트로 전달하고, 실제 param이나 searchParam이 필요한 곳에 가까운 위치에서 await해 보세요.

이전:

app/map.js
[code]
    export async function Map({ lat, lng }) {
      const mapData = await fetch(`https://...?lat=${lat}&lng=${lng}`)
      return drawMap(mapData)
    }
[/code]

app/page.js
[code]
    import { cookies } from 'next/headers'
     
    import { Map } from './map'
     
    export default async function Page({ searchParams }) {
      const { lat, lng } = await searchParams;
      return (
        <Suspense fallback="loading your inbox...">
          <Map lat={lat} lng={lng}>
        </Suspense>
      )
    }
[/code]

이후:

app/map.js
[code]
    export async function Map({ coords }) {
      const { lat, lng } = await coords
      const mapData = await fetch(`https://...?lat=${lat}&lng=${lng}`)
      return drawMap(mapData)
    }
[/code]

app/page.js
[code]
    import { cookies } from 'next/headers'
     
    import { Map } from './map'
     
    export default async function Page({ searchParams }) {
      const coords = searchParams.then(sp => ({ lat: sp.lat, lng: sp.lng }))
      return (
        <Suspense fallback="loading your inbox...">
          <Map coord={coords}>
        </Suspense>
      )
    }
[/code]

또는 `params`나 `searchParams`에 접근하는 컴포넌트 상단에 `Suspense` 경계를 추가해 Next.js가 이 요청 데이터를 기다리는 동안 어떤 UI를 사용할지 알 수 있게 할 수 있습니다.

#### `generateStaticParams`[](https://nextjs.org/docs/messages/blocking-route#generatestaticparams)

레이아웃과 페이지 `params`의 경우 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)를 사용해 빌드 타임 검증용 샘플 값을 제공하면 `Suspense` 없이도 `params`를 직접 await할 수 있습니다.

app/blog/[slug]/page.js
[code]
    export async function generateStaticParams() {
      return [{ slug: 'hello-world' }]
    }
     
    export default async function Page({ params }) {
      const { slug } = await params //  Valid with generateStaticParams
      return <div>Blog post: {slug}</div>
    }
[/code]

검증은 경로에 따라 달라집니다. 런타임 파라미터는 `Suspense` 없이 런타임 API에 접근하거나, `Suspense`나 `use cache` 없이 동적 콘텐츠를 트리거해 오류가 발생할 수 있는 조건부 분기를 실행할 수 있습니다. [Dynamic Routes with Cache Components](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components)를 참고하세요.

### 짧은 수명의 캐시[](https://nextjs.org/docs/messages/blocking-route#short-lived-caches)

`"use cache"`를 사용하면 프리렌더링하기엔 너무 짧을 수 있는 [`cacheLife()`](https://nextjs.org/docs/app/api-reference/functions/cacheLife)를 지정할 수 있습니다. 이렇게 해두면 브라우저의 클라이언트 라우터 캐시가 해당 항목을 재사용할 수 있도록 0이 아닌 캐시 시간을 명시할 수 있고, 높은 요청 트래픽 중에 업스트림 API를 보호하는 데도 유용합니다.

`"use cache"` 항목을 프리렌더링할 수 있으리라 예상했다면 `cacheLife()`를 조금 더 길게 설정해 보세요.

이전:

app/page.js
[code]
    import { cacheLife } from 'next/cache'
     
    async function getDashboard() {
      "use cache"
      // This cache will revalidate after 1 second. It is so short
      // Next.js won't prerender it on the server but the client router
      // can reuse the result for up to 30 seconds unless the user manually refreshes
      cacheLife('seconds')
      return db.query(...)
    }
     
    export default async function Page() {
      const data = await getDashboard(token);
      return <Dashboard data={data}>
    }
[/code]

이후:

app/page.js
[code]
    import { cacheLife } from 'next/cache'
     
    async function getDashboard() {
      "use cache"
      // This cache will revalidate after 1 minute. It's long enough that
      // Next.js will still produce a fully or partially prerendered page
      cacheLife('minutes')
      return db.query(...)
    }
     
    export default async function Page() {
      const data = await getDashboard(token);
      return <Dashboard data={data}>
    }
[/code]

또는 이 짧은 수명의 캐시에 접근하는 컴포넌트 상단에 `Suspense` 경계를 추가해 Next.js가 사용자 요청 동안 데이터를 가져올 때 사용할 UI를 알 수 있도록 할 수 있습니다.

## 유용한 링크[](https://nextjs.org/docs/messages/blocking-route#useful-links)

  * [`Suspense` React API](https://react.dev/reference/react/Suspense)
  * [`headers` 함수](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`cookies` 함수](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`draftMode` 함수](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * [`connection` 함수](https://nextjs.org/docs/app/api-reference/functions/connection)
  * [`cacheLife` 함수](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
  * [`cacheTag` 함수](https://nextjs.org/docs/app/api-reference/functions/cacheTag)



도움이 되었나요?

지원됨.

보내기
