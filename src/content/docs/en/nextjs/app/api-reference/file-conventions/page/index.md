---
title: 'File-system conventions: page.js'
description: 'The  file allows you to define UI that is unique to a route. You can create a page by default exporting a component from the file:'
---

# File-system conventions: page.js | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/page

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)page.js

Copy page

# page.js

Last updated February 20, 2026

The `page` file allows you to define UI that is **unique** to a route. You can create a page by default exporting a component from the file:

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

## Good to know[](https://nextjs.org/docs/app/api-reference/file-conventions/page#good-to-know)

  * The `.js`, `.jsx`, or `.tsx` file extensions can be used for `page`.
  * A `page` is always the **leaf** of the route subtree.
  * A `page` file is required to make a route segment **publicly accessible**.
  * Pages are [Server Components](https://react.dev/reference/rsc/server-components) by default, but can be set to a [Client Component](https://react.dev/reference/rsc/use-client).



## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/page#reference)

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/page#props)

#### `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/page#params-optional)

A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) from the root segment down to that page.

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

Example Route| URL| `params`  
---|---|---  
`app/shop/[slug]/page.js`| `/shop/1`| `Promise<{ slug: '1' }>`  
`app/shop/[category]/[item]/page.js`| `/shop/1/2`| `Promise<{ category: '1', item: '2' }>`  
`app/shop/[...slug]/page.js`| `/shop/1/2`| `Promise<{ slug: ['1', '2'] }>`  
  
  * Since the `params` prop is a promise, you must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.



#### `searchParams` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)

A promise that resolves to an object containing the [search parameters](https://developer.mozilla.org/docs/Learn/Common_questions/What_is_a_URL#parameters) of the current URL. For example:

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

Client Component **pages** can also access `searchParams` using React’s [`use`](https://react.dev/reference/react/use) hook:

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

Example URL| `searchParams`  
---|---  
`/shop?a=1`| `Promise<{ a: '1' }>`  
`/shop?a=1&b=2`| `Promise<{ a: '1', b: '2' }>`  
`/shop?a=1&a=2`| `Promise<{ a: ['1', '2'] }>`  
  
  * Since the `searchParams` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
    * In version 14 and earlier, `searchParams` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * `searchParams` is a **[Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)** whose values cannot be known ahead of time. Using it will opt the page into **[dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)** at request time.
  * `searchParams` is a plain JavaScript object, not a `URLSearchParams` instance.



### Page Props Helper[](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)

You can type pages with `PageProps` to get strongly typed `params` and `searchParams` from the route literal. `PageProps` is a globally available helper.

app/blog/[slug]/page.tsx
[code]
    export default async function Page(props: PageProps<'/blog/[slug]'>) {
      const { slug } = await props.params
      const query = await props.searchParams
      return <h1>Blog Post: {slug}</h1>
    }
[/code]

> **Good to know**
> 
>   * Using a literal route (e.g. `'/blog/[slug]'`) enables autocomplete and strict keys for `params`.
>   * Static routes resolve `params` to `{}`.
>   * Types are generated during `next dev`, `next build`, or with `next typegen`.
>   * After type generation, the `PageProps` helper is globally available. It doesn't need to be imported.
> 


## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/page#examples)

### Displaying content based on `params`[](https://nextjs.org/docs/app/api-reference/file-conventions/page#displaying-content-based-on-params)

Using [dynamic route segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes), you can display or fetch specific content for the page based on the `params` prop.

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

### Handling filtering with `searchParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/page#handling-filtering-with-searchparams)

You can use the `searchParams` prop to handle filtering, pagination, or sorting based on the query string of the URL.

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

### Reading `searchParams` and `params` in Client Components[](https://nextjs.org/docs/app/api-reference/file-conventions/page#reading-searchparams-and-params-in-client-components)

To use `searchParams` and `params` in a Client Component (which cannot be `async`), you can use React's [`use`](https://react.dev/reference/react/use) function to read the promise:

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

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/page#version-history)

Version| Changes  
---|---  
`v15.0.0-RC`| `params` and `searchParams` are now promises. A [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150) is available.  
`v13.0.0`| `page` introduced.  
  
Was this helpful?

supported.

Send
