---
title: 'Routing: Custom App'
description: 'Next.js uses the  component to initialize pages. You can override it and control the page initialization and:'
---

# Routing: Custom App | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/routing/custom-app

[Building Your Application](https://nextjs.org/docs/pages/building-your-application)[Routing](https://nextjs.org/docs/pages/building-your-application/routing)Custom App

Copy page

# Custom App

Last updated February 20, 2026

Next.js uses the `App` component to initialize pages. You can override it and control the page initialization and:

  * Create a shared layout between page changes
  * Inject additional data into pages
  * [Add global CSS](https://nextjs.org/docs/app/getting-started/css)



## Usage[](https://nextjs.org/docs/pages/building-your-application/routing/custom-app#usage)

To override the default `App`, create the file `pages/_app` as shown below:

pages/_app.tsx

JavaScriptTypeScript
[code]
    import type { AppProps } from 'next/app'
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return <Component {...pageProps} />
    }
[/code]

The `Component` prop is the active `page`, so whenever you navigate between routes, `Component` will change to the new `page`. Therefore, any props you send to `Component` will be received by the `page`.

`pageProps` is an object with the initial props that were preloaded for your page by one of our [data fetching methods](https://nextjs.org/docs/pages/building-your-application/data-fetching), otherwise it's an empty object.

> **Good to know** :
> 
>   * If your app is running and you added a custom `App`, you'll need to restart the development server. Only required if `pages/_app.js` didn't exist before.
>   * `App` does not support Next.js [Data Fetching methods](https://nextjs.org/docs/pages/building-your-application/data-fetching) like [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) or [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props).
> 


## `getInitialProps` with `App`[](https://nextjs.org/docs/pages/building-your-application/routing/custom-app#getinitialprops-with-app)

Using [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props) in `App` will disable [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) for pages without [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props).

**We do not recommend using this pattern.** Instead, consider [incrementally adopting](https://nextjs.org/docs/app/guides/migrating/app-router-migration) the App Router, which allows you to more easily fetch data for pages and layouts.

pages/_app.tsx

JavaScriptTypeScript
[code]
    import App, { AppContext, AppInitialProps, AppProps } from 'next/app'
     
    type AppOwnProps = { example: string }
     
    export default function MyApp({
      Component,
      pageProps,
      example,
    }: AppProps & AppOwnProps) {
      return (
        <>
          <p>Data: {example}</p>
          <Component {...pageProps} />
        </>
      )
    }
     
    MyApp.getInitialProps = async (
      context: AppContext
    ): Promise<AppOwnProps & AppInitialProps> => {
      const ctx = await App.getInitialProps(context)
     
      return { ...ctx, example: 'data' }
    }
[/code]

Was this helpful?

supported.

Send
