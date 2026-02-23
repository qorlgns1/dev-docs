---
title: '함수: generateStaticParams'
description: '함수는 동적 라우트 세그먼트와 함께 사용해 요청 시점이 아닌 빌드 시점에 정적 생성으로 라우트를 만들 수 있습니다.'
---

# 함수: generateStaticParams | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/generate-static-params

# generateStaticParams

마지막 업데이트: 2026년 2월 20일

`generateStaticParams` 함수는 [동적 라우트 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)와 함께 사용해 요청 시점이 아닌 빌드 시점에 [**정적 생성**](https://nextjs.org/docs/app/guides/caching#static-rendering)으로 라우트를 만들 수 있습니다.

`generateStaticParams`는 다음과 함께 사용할 수 있습니다.

  * [Pages](https://nextjs.org/docs/app/api-reference/file-conventions/page) (`page.tsx`/`page.js`)
  * [Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout) (`layout.tsx`/`layout.js`)
  * [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) (`route.ts`/`route.js`)

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    // Return a list of `params` to populate the [slug] dynamic segment
    export async function generateStaticParams() {
      const posts = await fetch('https://.../posts').then((res) => res.json())

      return posts.map((post) => ({
        slug: post.slug,
      }))
    }

    // Multiple versions of this page will be statically generated
    // using the `params` returned by `generateStaticParams`
    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      // ...
    }
[/code]

> **알아두면 좋은 점** :
>
>   * [`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams) 세그먼트 구성 옵션을 사용하면 `generateStaticParams`로 생성되지 않은 동적 세그먼트를 방문했을 때의 동작을 제어할 수 있습니다.
>   * [런타임에서 경로를 재검증(ISR)](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#all-paths-at-runtime)하려면 [`generateStaticParams`에서 빈 배열을 반환](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#all-paths-at-build-time)하거나 [`export const dynamic = 'force-static'`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic)을 사용해야 합니다.
>   * `next dev` 동안에는 라우트로 이동할 때 `generateStaticParams`가 호출됩니다.
>   * `next build` 동안에는 해당 Layout 또는 Page가 생성되기 전에 `generateStaticParams`가 실행됩니다.
>   * 재검증(ISR) 중에는 `generateStaticParams`가 다시 호출되지 않습니다.
>   * `generateStaticParams`는 Pages Router의 [`getStaticPaths`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths) 함수를 대체합니다.
>

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#parameters)

`options.params` (선택 사항)

하나의 라우트에서 여러 동적 세그먼트가 `generateStaticParams`를 사용하는 경우, 부모가 생성한 각 `params` 집합마다 자식 `generateStaticParams` 함수가 한 번씩 실행됩니다.

`params` 객체는 부모 `generateStaticParams`에서 채워진 `params`를 포함하며, 이를 사용해 [자식 세그먼트에서 `params`를 생성](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#multiple-dynamic-segments-in-a-route)할 수 있습니다.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#returns)

`generateStaticParams`는 각 객체가 하나의 라우트에 대한 동적 세그먼트를 채운 값을 나타내는 객체 배열을 반환해야 합니다.

  * 객체의 각 속성은 라우트에서 채워야 할 동적 세그먼트를 의미합니다.
  * 속성 이름은 세그먼트 이름이며, 속성 값은 해당 세그먼트에 채워 넣을 값입니다.

Example Route| `generateStaticParams` 반환 타입
---|---
`/product/[id]`| `{ id: string }[]`
`/products/[category]/[product]`| `{ category: string, product: string }[]`
`/products/[...slug]`| `{ slug: string[] }[]`

## Single Dynamic Segment[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#single-dynamic-segment)

app/product/[id]/page.tsx

JavaScriptTypeScript
[code]
    export function generateStaticParams() {
      return [{ id: '1' }, { id: '2' }, { id: '3' }]
    }

    // Three versions of this page will be statically generated
    // using the `params` returned by `generateStaticParams`
    // - /product/1
    // - /product/2
    // - /product/3
    export default async function Page({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      // ...
    }
[/code]

## Multiple Dynamic Segments[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#multiple-dynamic-segments)

app/products/[category]/[product]/page.tsx

JavaScriptTypeScript
[code]
    export function generateStaticParams() {
      return [
        { category: 'a', product: '1' },
        { category: 'b', product: '2' },
        { category: 'c', product: '3' },
      ]
    }

    // Three versions of this page will be statically generated
    // using the `params` returned by `generateStaticParams`
    // - /products/a/1
    // - /products/b/2
    // - /products/c/3
    export default async function Page({
      params,
    }: {
      params: Promise<{ category: string; product: string }>
    }) {
      const { category, product } = await params
      // ...
    }
[/code]

## Catch-all Dynamic Segment[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#catch-all-dynamic-segment)

app/product/[...slug]/page.tsx

JavaScriptTypeScript
[code]
    export function generateStaticParams() {
      return [{ slug: ['a', '1'] }, { slug: ['b', '2'] }, { slug: ['c', '3'] }]
    }

    // Three versions of this page will be statically generated
    // using the `params` returned by `generateStaticParams`
    // - /product/a/1
    // - /product/b/2
    // - /product/c/3
    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string[] }>
    }) {
      const { slug } = await params
      // ...
    }
[/code]

## Examples[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#examples)

### Static Rendering[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#static-rendering)

#### 빌드 시 모든 경로[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#all-paths-at-build-time)

빌드 시 모든 경로를 정적으로 렌더링하려면 전체 경로 목록을 `generateStaticParams`에 제공하세요.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    export async function generateStaticParams() {
      const posts = await fetch('https://.../posts').then((res) => res.json())

      return posts.map((post) => ({
        slug: post.slug,
      }))
    }
[/code]

#### 빌드 시 부분 경로[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#subset-of-paths-at-build-time)

빌드 시 일부 경로만 정적으로 렌더링하고 나머지는 런타임에서 최초 방문 시 생성하려면 경로의 부분 목록을 반환하세요.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    export async function generateStaticParams() {
      const posts = await fetch('https://.../posts').then((res) => res.json())

      // Render the first 10 posts at build time
      return posts.slice(0, 10).map((post) => ({
        slug: post.slug,
      }))
    }
[/code]

그런 다음 [`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams) 세그먼트 구성 옵션을 사용해 `generateStaticParams`로 생성되지 않은 동적 세그먼트를 방문했을 때의 동작을 제어할 수 있습니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    // All posts besides the top 10 will be a 404
    export const dynamicParams = false

    export async function generateStaticParams() {
      const posts = await fetch('https://.../posts').then((res) => res.json())
      const topPosts = posts.slice(0, 10)

      return topPosts.map((post) => ({
        slug: post.slug,
      }))
    }
[/code]

#### 런타임의 모든 경로[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#all-paths-at-runtime)

모든 경로를 최초 방문 시 정적으로 렌더링하려면 빈 배열을 반환(빌드 시 렌더링되는 경로 없음)하거나 [`export const dynamic = 'force-static'`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic)을 활용하세요.

app/blog/[slug]/page.js
[code]
    export async function generateStaticParams() {
      return []
    }
[/code]

> **알아두면 좋은 점:**
>
>   * 비어 있더라도 `generateStaticParams`에서 항상 배열을 반환해야 합니다. 그렇지 않으면 라우트가 동적으로 렌더링됩니다.
>

app/changelog/[slug]/page.js
[code]
    export const dynamic = 'force-static'
[/code]

#### Cache Components와 함께[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#with-cache-components)

동적 라우트에서 [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 사용할 때 `generateStaticParams`는 **최소 한 개의 파라미터**를 반환해야 합니다. 빈 배열은 [빌드 오류](https://nextjs.org/docs/messages/empty-generate-static-params)를 일으킵니다. 이는 Cache Components가 런타임에서 `cookies()`, `headers()`, `searchParams`에 잘못 접근하지 않는지 검증할 수 있도록 합니다.

> **알아두면 좋은 점** : 빌드 시 실제 파라미터 값을 모를 경우 검증용으로 `[{ slug: '__placeholder__' }]`와 같은 플레이스홀더 파라미터를 반환하고 페이지에서 `notFound()`로 처리할 수 있습니다. 하지만 이렇게 하면 빌드 시 검증이 제대로 작동하지 않아 런타임 오류가 발생할 수 있습니다.

자세한 안내는 [동적 라우트 섹션](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components)을 참고하세요.

### With Route Handlers[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#with-route-handlers)

`generateStaticParams`는 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)와 함께 사용해 빌드 시점에 API 응답을 정적으로 생성할 수 있습니다.

app/api/posts/[id]/route.ts

JavaScriptTypeScript
[code]
    export async function generateStaticParams() {
      return [{ id: '1' }, { id: '2' }, { id: '3' }]
    }

    export async function GET(
      request: Request,
      { params }: RouteContext<'/api/posts/[id]'>
    ) {
      const { id } = await params
      // This will be statically generated for IDs 1, 2, and 3
      return Response.json({ id, title: `Post ${id}` })
    }
[/code]

### Route Handlers with Cache Components[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#route-handlers-with-cache-components)

[Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 사용할 때는 최적의 캐싱을 위해 `use cache`와 함께 사용하세요.

app/api/posts/[id]/route.ts
[code]
    export async function generateStaticParams() {
      return [{ id: '1' }, { id: '2' }, { id: '3' }]
    }

    async function getPost(id: Promise<string>) {
      'use cache'
      const resolvedId = await id
      const response = await fetch(`https://api.example.com/posts/${resolvedId}`)
      return response.json()
    }

    export async function GET(
      request: Request,
      { params }: RouteContext<'/api/posts/[id]'>
    ) {
      const post = await getPost(params.then((p) => p.id))
      return Response.json(post)
    }
[/code]

자세한 내용은 [Route Handlers 문서](https://nextjs.org/docs/app/api-reference/file-conventions/route#static-generation-with-generatestaticparams)를 참고하세요.

### 지정되지 않은 경로에 대한 렌더링 비활성화[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#disable-rendering-for-unspecified-paths)

지정되지 않은 경로가 런타임에 정적으로 렌더링되는 것을 막으려면, 라우트 세그먼트에 `export const dynamicParams = false` 옵션을 추가하세요. 이 구성 옵션을 사용하면 `generateStaticParams`가 제공한 경로만 제공되고, 지정되지 않은 경로는 404가 발생하거나 ([캐치올 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)의 경우) 매치됩니다.

### 라우트 내 여러 동적 세그먼트[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#multiple-dynamic-segments-in-a-route)

현재 레이아웃이나 페이지보다 상위에 있는 동적 세그먼트의 파라미터는 생성할 수 있지만, **하위 세그먼트는 안 됩니다**. 예를 들어 `app/products/[category]/[product]` 라우트에서는:

  * `app/products/[category]/[product]/page.js`에서 `[category]`와 `[product]` 두 세그먼트 모두의 파라미터를 생성할 수 있습니다.
  * `app/products/[category]/layout.js`에서는 `[category]`의 파라미터만 생성할 수 있습니다.

동적 세그먼트가 여러 개인 라우트의 파라미터를 생성하는 방법은 두 가지가 있습니다:

#### 하위에서 상위로 파라미터 생성[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#generate-params-from-the-bottom-up)

자식 라우트 세그먼트에서 여러 동적 세그먼트를 생성합니다.

app/products/[category]/[product]/page.tsx

JavaScriptTypeScript
[code]
    // Generate segments for both [category] and [product]
    export async function generateStaticParams() {
      const products = await fetch('https://.../products').then((res) => res.json())

      return products.map((product) => ({
        category: product.category.slug,
        product: product.id,
      }))
    }

    export default function Page({
      params,
    }: {
      params: Promise<{ category: string; product: string }>
    }) {
      // ...
    }
[/code]

#### 상위에서 하위로 파라미터 생성[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#generate-params-from-the-top-down)

부모 세그먼트를 먼저 생성한 뒤 결과를 사용해 자식 세그먼트를 생성합니다.

app/products/[category]/layout.tsx

JavaScriptTypeScript
[code]
    // Generate segments for [category]
    export async function generateStaticParams() {
      const products = await fetch('https://.../products').then((res) => res.json())

      return products.map((product) => ({
        category: product.category.slug,
      }))
    }

    export default function Layout({
      params,
    }: {
      params: Promise<{ category: string }>
    }) {
      // ...
    }
[/code]

자식 라우트 세그먼트의 `generateStaticParams` 함수는 부모 `generateStaticParams`가 생성한 각 세그먼트마다 한 번씩 실행됩니다.

자식 `generateStaticParams` 함수는 부모 `generateStaticParams` 함수에서 반환한 `params`를 사용해 자신의 세그먼트를 동적으로 생성할 수 있습니다.

app/products/[category]/[product]/page.tsx

JavaScriptTypeScript
[code]
    // Generate segments for [product] using the `params` passed from
    // the parent segment's `generateStaticParams` function
    export async function generateStaticParams({
      params: { category },
    }: {
      params: { category: string }
    }) {
      const products = await fetch(
        `https://.../products?category=${category}`
      ).then((res) => res.json())

      return products.map((product) => ({
        product: product.id,
      }))
    }

    export default function Page({
      params,
    }: {
      params: Promise<{ category: string; product: string }>
    }) {
      // ...
    }
[/code]

`params` 인수는 동기적으로 접근할 수 있으며 부모 세그먼트의 파라미터만 포함합니다.

타입 완성을 위해, TypeScript `Awaited` 헬퍼를 [`Page Props helper`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)나 [`Layout Props helper`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)와 함께 사용할 수 있습니다:

app/products/[category]/[product]/page.tsx

JavaScriptTypeScript
[code]
    export async function generateStaticParams({
      params: { category },
    }: {
      params: Awaited<LayoutProps<'/products/[category]'>['params']>
    }) {
      const products = await fetch(
        `https://.../products?category=${category}`
      ).then((res) => res.json())

      return products.map((product) => ({
        product: product.id,
      }))
    }
[/code]

> **알아두면 좋아요** : `fetch` 요청은 모든 `generate` 접두사가 붙은 함수, 레이아웃, 페이지, 서버 컴포넌트 전반에서 동일한 데이터를 대상으로 자동으로 [메모이즈](https://nextjs.org/docs/app/guides/caching#request-memoization)됩니다. `fetch`를 사용할 수 없다면 React [`cache`를 사용할 수 있습니다](https://nextjs.org/docs/app/guides/caching#react-cache-function).

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#version-history)

Version| Changes
---|---
`v13.0.0`| `generateStaticParams` 도입.
