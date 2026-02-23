---
title: '함수: useParams'
description: '는 현재 URL이 채운 라우트의 동적 매개변수를 읽을 수 있는 훅입니다.'
---

# 함수: useParams | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/functions/use-params

[API Reference](https://nextjs.org/docs/pages/api-reference) [Functions](https://nextjs.org/docs/pages/api-reference/functions) useParams

# useParams

마지막 업데이트: 2026년 2월 20일

`useParams`는 현재 URL이 채운 라우트의 [동적 매개변수](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 읽을 수 있는 훅입니다.

pages/shop/[slug].tsx

JavaScript / TypeScript
```
    import { useParams } from 'next/navigation'

    export default function ShopPage() {
      const params = useParams<{ slug: string }>()

      if (!params) {
        // Render fallback UI while params are not yet available
        return null
      }

      // Route -> /shop/[slug]
      // URL -> /shop/shoes
      // `params` -> { slug: 'shoes' }
      return <>Shop: {params.slug}</>
    }
```

## 매개변수[](https://nextjs.org/docs/pages/api-reference/functions/use-params#parameters)
```
    const params = useParams()
```

`useParams`는 어떤 매개변수도 받지 않습니다.

## 반환값[](https://nextjs.org/docs/pages/api-reference/functions/use-params#returns)

`useParams`는 현재 라우트의 [동적 매개변수](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)가 채워진 객체를 반환하며, [사전 렌더링](https://nextjs.org/docs/pages/api-reference/functions/use-params#behavior-during-pre-rendering) 중에는 `null`을 반환합니다.

  * 객체의 각 속성은 활성 동적 세그먼트입니다.
  * 속성 이름은 세그먼트 이름이고, 속성 값은 세그먼트에 채워진 실제 값입니다.
  * 속성 값은 [동적 세그먼트 유형](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)에 따라 `string` 또는 `string` 배열 중 하나입니다.
  * 라우트에 동적 매개변수가 없으면 `useParams`는 빈 객체를 반환합니다.

예를 들면 다음과 같습니다:

Route| URL| `useParams()`
---|---|---
`pages/shop/page.js`| `/shop`| `{}`
`pages/shop/[slug].js`| `/shop/1`| `{ slug: '1' }`
`pages/shop/[tag]/[item].js`| `/shop/1/2`| `{ tag: '1', item: '2' }`
`pages/shop/[...slug].js`| `/shop/1/2`| `{ slug: ['1', '2'] }`

> **알아두면 좋아요**: `useParams`는 [React 훅](https://react.dev/learn#using-hooks)이므로 클래스에서는 사용할 수 없습니다.

## 동작[](https://nextjs.org/docs/pages/api-reference/functions/use-params#behavior)

### 사전 렌더링 중 동작[](https://nextjs.org/docs/pages/api-reference/functions/use-params#behavior-during-pre-rendering)

[정적으로 최적화된](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) 페이지에서는 `useParams`가 초기 렌더에서 `null`을 반환합니다. 하이드레이션 이후 라우터가 준비되면 값이 실제 매개변수로 업데이트됩니다.

이는 동적 라우트의 경우 정적 생성 시점에는 매개변수를 알 수 없기 때문입니다.

pages/shop/[slug].tsx

JavaScript / TypeScript
```
    import { useParams } from 'next/navigation'

    export default function ShopPage() {
      const params = useParams<{ slug: string }>()

      if (!params) {
        // Return a fallback UI while params are loading
        // This prevents hydration mismatches
        return <ShopPageSkeleton />
      }

      return <>Shop: {params.slug}</>
    }
```

### `getServerSideProps`와 함께 사용[](https://nextjs.org/docs/pages/api-reference/functions/use-params#using-with-getserversideprops)

[`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)를 사용할 때는 페이지가 매 요청마다 서버 렌더링되므로 `useParams`가 실제 매개변수를 즉시 반환합니다.

pages/shop/[slug].tsx

JavaScript / TypeScript
```
    import { useParams } from 'next/navigation'

    export default function ShopPage() {
      const params = useParams<{ slug: string }>()

      // With getServerSideProps, this fallback is never rendered because
      // params is always available on the server. However, keeping
      // the fallback allows this component to be reused on other pages
      // that may not use getServerSideProps.
      if (!params) {
        return null
      }

      return <>Shop: {params.slug}</>
    }

    export async function getServerSideProps() {
      return { props: {} }
    }
```

### `router.query`와의 비교[](https://nextjs.org/docs/pages/api-reference/functions/use-params#comparison-with-routerquery)

`useParams`는 동적 라우트 매개변수만 반환하는 반면, `useRouter`에서 가져오는 [`router.query`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)는 동적 매개변수와 쿼리 문자열 매개변수를 모두 포함합니다.

pages/shop/[slug].tsx

JavaScript / TypeScript
```
    import { useRouter } from 'next/router'
    import { useParams } from 'next/navigation'

    export default function ShopPage() {
      const router = useRouter()
      const params = useParams()

      // URL -> /shop/shoes?color=red

      // router.query -> { slug: 'shoes', color: 'red' }
      // params -> { slug: 'shoes' }

      // ...
    }
```

## 예시[](https://nextjs.org/docs/pages/api-reference/functions/use-params#examples)

### App Router와 컴포넌트 공유[](https://nextjs.org/docs/pages/api-reference/functions/use-params#sharing-components-with-app-router)

`next/navigation`의 `useParams`는 Pages Router와 App Router 모두에서 동작합니다. 이를 통해 두 컨텍스트에서 모두 동작하는 공유 컴포넌트를 만들 수 있습니다.

components/breadcrumb.tsx

JavaScript / TypeScript
```
    import { useParams } from 'next/navigation'

    // This component works in both pages/ and app/
    export function Breadcrumb() {
      const params = useParams<{ slug: string }>()

      if (!params) {
        // Fallback for Pages Router during pre-rendering
        return <nav>Home / ...</nav>
      }

      return <nav>Home / {params.slug}</nav>
    }
```

> **알아두면 좋아요**: App Router에서 이 컴포넌트를 사용할 때 `useParams`는 `null`을 반환하지 않으므로 폴백 분기가 렌더링되지 않습니다.

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/functions/use-params#version-history)

Version| Changes
---|---
`v13.3.0`| `useParams` 도입.