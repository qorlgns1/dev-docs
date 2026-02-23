---
title: '파일 시스템 규칙: page.js'
description: '파일을 사용하면 경로에 고유한 UI를 정의할 수 있습니다. 파일에서 컴포넌트를 기본 내보내기(default export)하면 페이지를 만들 수 있습니다:'
---

# 파일 시스템 규칙: page.js | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/file-conventions/page

# page.js

마지막 업데이트: 2026년 2월 20일

`page` 파일을 사용하면 경로에 **고유한** UI를 정의할 수 있습니다. 파일에서 컴포넌트를 기본 내보내기(default export)하면 페이지를 만들 수 있습니다:

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    export default function Page({
      params,
      searchParams,
    }: {
      params: Promise<{ slug: string }>
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }) {
      return <h1>My Page</h1>
    }
[/code]

## 알아두면 좋은 내용[](https://nextjs.org/docs/app/api-reference/file-conventions/page#good-to-know)

  * `page`에는 `.js`, `.jsx`, `.tsx` 파일 확장자를 사용할 수 있습니다.
  * `page`는 항상 라우트 서브트리의 **리프**입니다.
  * `page` 파일이 있어야 라우트 세그먼트를 **공개적으로 접근 가능**하게 만들 수 있습니다.
  * 페이지는 기본적으로 [Server Components](https://react.dev/reference/rsc/server-components)이지만, [Client Component](https://react.dev/reference/rsc/use-client)로 설정할 수 있습니다.

## 참고[](https://nextjs.org/docs/app/api-reference/file-conventions/page#reference)

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/page#props)

#### `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/page#params-optional)

루트 세그먼트부터 해당 페이지까지의 [동적 라우트 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 포함하는 객체로 해석되는 프로미스입니다.

app/shop/[slug]/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
    }
[/code]

예시 경로| URL| `params`
---|---|---
`app/shop/[slug]/page.js`| `/shop/1`| `Promise<{ slug: '1' }>`
`app/shop/[category]/[item]/page.js`| `/shop/1/2`| `Promise<{ category: '1', item: '2' }>`
`app/shop/[...slug]/page.js`| `/shop/1/2`| `Promise<{ slug: ['1', '2'] }>`

  * `params` prop이 프로미스이므로 값을 읽으려면 `async/await` 또는 React의 [`use`](https://react.dev/reference/react/use) 함수를 사용해야 합니다.
    * 버전 14 및 이전에서는 `params`가 동기 prop이었습니다. 하위 호환을 돕기 위해 Next.js 15에서도 동기적으로 접근할 수 있지만, 이 동작은 추후 폐기될 예정입니다.

#### `searchParams` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)

현재 URL의 [검색 매개변수](https://developer.mozilla.org/docs/Learn/Common_questions/What_is_a_URL#parameters)를 포함하는 객체로 해석되는 프로미스입니다. 예:

app/shop/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page({
      searchParams,
    }: {
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }) {
      const filters = (await searchParams).filters
    }
[/code]

클라이언트 컴포넌트 **페이지**에서도 React의 [`use`](https://react.dev/reference/react/use) 훅으로 `searchParams`를 사용할 수 있습니다:

app/shop/page.tsx

JavaScriptTypeScript
[code]
    'use client'
    import { use } from 'react'

    export default function Page({
      searchParams,
    }: {
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }) {
      const filters = use(searchParams).filters
    }
[/code]

예시 URL| `searchParams`
---|---
`/shop?a=1`| `Promise<{ a: '1' }>`
`/shop?a=1&b=2`| `Promise<{ a: '1', b: '2' }>`
`/shop?a=1&a=2`| `Promise<{ a: ['1', '2'] }>`

  * `searchParams` prop이 프로미스이므로 값을 읽을 때 `async/await` 또는 React의 [`use`](https://react.dev/reference/react/use) 함수를 사용해야 합니다.
    * 버전 14 및 이전에서는 `searchParams`가 동기 prop이었습니다. 하위 호환을 돕기 위해 Next.js 15에서도 동기적으로 접근할 수 있지만, 이 동작은 추후 폐기될 예정입니다.
  * `searchParams`는 값이 미리 결정될 수 없는 **[동적 API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)**입니다. 이를 사용하면 페이지가 요청 시점의 **[동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)**으로 전환됩니다.
  * `searchParams`는 `URLSearchParams` 인스턴스가 아닌 일반 JavaScript 객체입니다.

### Page Props Helper[](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)

페이지를 `PageProps`로 타이핑하면 라우트 리터럴에서 강력하게 타입 지정된 `params`와 `searchParams`를 사용할 수 있습니다. `PageProps`는 전역적으로 사용할 수 있는 헬퍼입니다.

app/blog/[slug]/page.tsx
[code]
    export default async function Page(props: PageProps<'/blog/[slug]'>) {
      const { slug } = await props.params
      const query = await props.searchParams
      return <h1>Blog Post: {slug}</h1>
    }
[/code]

> **알아두면 좋은 내용**
>
>   * 리터럴 라우트(예: `'/blog/[slug]'`)를 사용하면 `params`에 대한 자동 완성과 엄격한 키를 활용할 수 있습니다.
>   * 정적 라우트의 `params`는 `{}`로 해석됩니다.
>   * 타입은 `next dev`, `next build`, 또는 `next typegen` 중에 생성됩니다.
>   * 타입 생성 후에는 `PageProps` 헬퍼가 전역적으로 제공되므로 import할 필요가 없습니다.
>

## 예시[](https://nextjs.org/docs/app/api-reference/file-conventions/page#examples)

### `params` 기준으로 콘텐츠 표시[](https://nextjs.org/docs/app/api-reference/file-conventions/page#displaying-content-based-on-params)

[동적 라우트 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 사용하면 `params` prop을 기반으로 페이지에 특정 콘텐츠를 표시하거나 가져올 수 있습니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      return <h1>Blog Post: {slug}</h1>
    }
[/code]

### `searchParams`로 필터링 처리[](https://nextjs.org/docs/app/api-reference/file-conventions/page#handling-filtering-with-searchparams)

`searchParams` prop을 사용하면 URL의 쿼리 문자열을 기반으로 필터링, 페이지네이션 또는 정렬을 처리할 수 있습니다.

app/shop/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page({
      searchParams,
    }: {
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }) {
      const { page = '1', sort = 'asc', query = '' } = await searchParams

      return (
        <div>
          <h1>Product Listing</h1>
          <p>Search query: {query}</p>
          <p>Current page: {page}</p>
          <p>Sort order: {sort}</p>
        </div>
      )
    }
[/code]

### 클라이언트 컴포넌트에서 `searchParams`와 `params` 읽기[](https://nextjs.org/docs/app/api-reference/file-conventions/page#reading-searchparams-and-params-in-client-components)

`searchParams`와 `params`를 `async`로 만들 수 없는 클라이언트 컴포넌트에서 사용하려면 React의 [`use`](https://react.dev/reference/react/use) 함수를 통해 프로미스를 읽을 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { use } from 'react'

    export default function Page({
      params,
      searchParams,
    }: {
      params: Promise<{ slug: string }>
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }) {
      const { slug } = use(params)
      const { query } = use(searchParams)
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/page#version-history)

버전| 변경 사항
---|---
`v15.0.0-RC`| `params`와 `searchParams`가 이제 프로미스입니다. [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150)가 제공됩니다.
`v13.0.0`| `page` 도입.

보내기
