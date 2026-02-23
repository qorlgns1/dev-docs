---
title: 'Functions: getInitialProps'
description: 'Last updated February 20, 2026'
---

# Functions: getInitialProps | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/functions/get-initial-props

[API Reference](https://nextjs.org/docs/pages/api-reference)[Functions](https://nextjs.org/docs/pages/api-reference/functions)getInitialProps

Copy page

# getInitialProps

Last updated February 20, 2026

> **Good to know** : `getInitialProps` is a legacy API. We recommend using [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) or [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) instead.

`getInitialProps` is an `async` function that can be added to the default exported React component for the page. It will run on both the server-side and again on the client-side during page transitions. The result of the function will be forwarded to the React component as `props`.

pages/index.tsx

JavaScriptTypeScript
[code]
    import { NextPageContext } from 'next'
     
    Page.getInitialProps = async (ctx: NextPageContext) => {
      const res = await fetch('https://api.github.com/repos/vercel/next.js')
      const json = await res.json()
      return { stars: json.stargazers_count }
    }
     
    export default function Page({ stars }: { stars: number }) {
      return stars
    }
[/code]

> **Good to know** :
> 
>   * Data returned from `getInitialProps` is serialized when server rendering. Ensure the returned object from `getInitialProps` is a plain `Object`, and not using `Date`, `Map` or `Set`.
>   * For the initial page load, `getInitialProps` will run on the server only. `getInitialProps` will then also run on the client when navigating to a different route with the [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) component or by using [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router).
>   * If `getInitialProps` is used in a custom `_app.js`, and the page being navigated to is using `getServerSideProps`, then `getInitialProps` will **only** run on the server.
> 


## Context Object[](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props#context-object)

`getInitialProps` receives a single argument called `context`, which is an object with the following properties:

Name| Description  
---|---  
`pathname`| Current route, the path of the page in `/pages`  
`query`| Query string of the URL, parsed as an object  
`asPath`| `String` of the actual path (including the query) shown in the browser  
`req`| [HTTP request object](https://nodejs.org/api/http.html#http_class_http_incomingmessage) (server only)  
`res`| [HTTP response object](https://nodejs.org/api/http.html#http_class_http_serverresponse) (server only)  
`err`| Error object if any error is encountered during the rendering  
  
## Caveats[](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props#caveats)

  * `getInitialProps` can only be used in `pages/` top level files, and not in nested components. To have nested data fetching at the component level, consider exploring the [App Router](https://nextjs.org/docs/app/getting-started/fetching-data).
  * Regardless of whether your route is static or dynamic, any data returned from `getInitialProps` as `props` will be able to be examined on the client-side in the initial HTML. This is to allow the page to be [hydrated](https://react.dev/reference/react-dom/hydrate) correctly. Make sure that you don't pass any sensitive information that shouldn't be available on the client in `props`.



Was this helpful?

supported.

Send
