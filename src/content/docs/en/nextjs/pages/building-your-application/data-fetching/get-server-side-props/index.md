---
title: 'Data Fetching: getServerSideProps'
description: 'is a Next.js function that can be used to fetch data and render the contents of a page at request time.'
---

# Data Fetching: getServerSideProps | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props

[Building Your Application](https://nextjs.org/docs/pages/building-your-application)[Data Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching)getServerSideProps

Copy page

# getServerSideProps

Last updated February 20, 2026

`getServerSideProps` is a Next.js function that can be used to fetch data and render the contents of a page at request time.

## Example[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#example)

You can use `getServerSideProps` by exporting it from a Page Component. The example below shows how you can fetch data from a 3rd party API in `getServerSideProps`, and pass the data to the page as props:

pages/index.tsx

JavaScriptTypeScript
[code]
    import type { InferGetServerSidePropsType, GetServerSideProps } from 'next'
     
    type Repo = {
      name: string
      stargazers_count: number
    }
     
    export const getServerSideProps = (async () => {
      // Fetch data from external API
      const res = await fetch('https://api.github.com/repos/vercel/next.js')
      const repo: Repo = await res.json()
      // Pass data to the page via props
      return { props: { repo } }
    }) satisfies GetServerSideProps<{ repo: Repo }>
     
    export default function Page({
      repo,
    }: InferGetServerSidePropsType<typeof getServerSideProps>) {
      return (
        <main>
          <p>{repo.stargazers_count}</p>
        </main>
      )
    }
[/code]

## When should I use `getServerSideProps`?[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#when-should-i-use-getserversideprops)

You should use `getServerSideProps` if you need to render a page that relies on personalized user data, or information that can only be known at request time. For example, `authorization` headers or a geolocation.

If you do not need to fetch the data at request time, or would prefer to cache the data and pre-rendered HTML, we recommend using [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props).

## Behavior[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#behavior)

  * `getServerSideProps` runs on the server.
  * `getServerSideProps` can only be exported from a **page**.
  * `getServerSideProps` returns JSON.
  * When a user visits a page, `getServerSideProps` will be used to fetch data at request time, and the data is used to render the initial HTML of the page.
  * `props` passed to the page component can be viewed on the client as part of the initial HTML. This is to allow the page to be [hydrated](https://react.dev/reference/react-dom/hydrate) correctly. Make sure that you don't pass any sensitive information that shouldn't be available on the client in `props`.
  * When a user visits the page through [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) or [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router), Next.js sends an API request to the server, which runs `getServerSideProps`.
  * You do not have to call a Next.js [API Route](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) to fetch data when using `getServerSideProps` since the function runs on the server. Instead, you can call a CMS, database, or other third-party APIs directly from inside `getServerSideProps`.



> **Good to know:**
> 
>   * See [`getServerSideProps` API reference](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props) for parameters and props that can be used with `getServerSideProps`.
>   * You can use the [next-code-elimination tool](https://next-code-elimination.vercel.app/) to verify what Next.js eliminates from the client-side bundle.
> 


## Error Handling[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#error-handling)

If an error is thrown inside `getServerSideProps`, it will show the `pages/500.js` file. Check out the documentation for [500 page](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#500-page) to learn more on how to create it. During development, this file will not be used and the development error overlay will be shown instead.

## Edge Cases[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#edge-cases)

### Caching with Server-Side Rendering (SSR)[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#caching-with-server-side-rendering-ssr)

You can use caching headers (`Cache-Control`) inside `getServerSideProps` to cache dynamic responses. For example, using [`stale-while-revalidate`](https://web.dev/stale-while-revalidate/).
[code] 
    // This value is considered fresh for ten seconds (s-maxage=10).
    // If a request is repeated within the next 10 seconds, the previously
    // cached value will still be fresh. If the request is repeated before 59 seconds,
    // the cached value will be stale but still render (stale-while-revalidate=59).
    //
    // In the background, a revalidation request will be made to populate the cache
    // with a fresh value. If you refresh the page, you will see the new value.
    export async function getServerSideProps({ req, res }) {
      res.setHeader(
        'Cache-Control',
        'public, s-maxage=10, stale-while-revalidate=59'
      )
     
      return {
        props: {},
      }
    }
[/code]

However, before reaching for `cache-control`, we recommend seeing if [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) with [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration) is a better fit for your use case.

Was this helpful?

supported.

Send
