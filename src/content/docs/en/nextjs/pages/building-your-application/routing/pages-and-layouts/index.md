---
title: 'Routing: Pages and Layouts'
description: 'Last updated February 20, 2026'
---

# Routing: Pages and Layouts | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts

[Building Your Application](https://nextjs.org/docs/pages/building-your-application)[Routing](https://nextjs.org/docs/pages/building-your-application/routing)Pages and Layouts

Copy page

# Pages and Layouts

Last updated February 20, 2026

The Pages Router has a file-system based router built on the concept of pages.

When a file is added to the `pages` directory, it's automatically available as a route.

In Next.js, a **page** is a [React Component](https://react.dev/learn/your-first-component) exported from a `.js`, `.jsx`, `.ts`, or `.tsx` file in the `pages` directory. Each page is associated with a route based on its file name.

**Example** : If you create `pages/about.js` that exports a React component like below, it will be accessible at `/about`.
[code] 
    export default function About() {
      return <div>About</div>
    }
[/code]

## Index routes[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)

The router will automatically route files named `index` to the root of the directory.

  * `pages/index.js` → `/`
  * `pages/blog/index.js` → `/blog`



## Nested routes[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#nested-routes)

The router supports nested files. If you create a nested folder structure, files will automatically be routed in the same way still.

  * `pages/blog/first-post.js` → `/blog/first-post`
  * `pages/dashboard/settings/username.js` → `/dashboard/settings/username`



## Pages with Dynamic Routes[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#pages-with-dynamic-routes)

Next.js supports pages with dynamic routes. For example, if you create a file called `pages/posts/[id].js`, then it will be accessible at `posts/1`, `posts/2`, etc.

> To learn more about dynamic routing, check the [Dynamic Routing documentation](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes).

## Layout Pattern[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)

The React model allows us to deconstruct a [page](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts) into a series of components. Many of these components are often reused between pages. For example, you might have the same navigation bar and footer on every page.

components/layout.js
[code]
    import Navbar from './navbar'
    import Footer from './footer'
     
    export default function Layout({ children }) {
      return (
        <>
          <Navbar />
          <main>{children}</main>
          <Footer />
        </>
      )
    }
[/code]

## Examples[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#examples)

### Single Shared Layout with Custom App[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#single-shared-layout-with-custom-app)

If you only have one layout for your entire application, you can create a [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) and wrap your application with the layout. Since the `<Layout />` component is re-used when changing pages, its component state will be preserved (e.g. input values).

pages/_app.js
[code]
    import Layout from '../components/layout'
     
    export default function MyApp({ Component, pageProps }) {
      return (
        <Layout>
          <Component {...pageProps} />
        </Layout>
      )
    }
[/code]

### Per-Page Layouts[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#per-page-layouts)

If you need multiple layouts, you can add a property `getLayout` to your page, allowing you to return a React component for the layout. This allows you to define the layout on a _per-page basis_. Since we're returning a function, we can have complex nested layouts if desired.

pages/index.js
[code]
     
    import Layout from '../components/layout'
    import NestedLayout from '../components/nested-layout'
     
    export default function Page() {
      return (
        /** Your content */
      )
    }
     
    Page.getLayout = function getLayout(page) {
      return (
        <Layout>
          <NestedLayout>{page}</NestedLayout>
        </Layout>
      )
    }
[/code]

pages/_app.js
[code]
    export default function MyApp({ Component, pageProps }) {
      // Use the layout defined at the page level, if available
      const getLayout = Component.getLayout ?? ((page) => page)
     
      return getLayout(<Component {...pageProps} />)
    }
[/code]

When navigating between pages, we want to _persist_ page state (input values, scroll position, etc.) for a Single-Page Application (SPA) experience.

This layout pattern enables state persistence because the React component tree is maintained between page transitions. With the component tree, React can understand which elements have changed to preserve state.

> **Good to know** : This process is called [reconciliation](https://react.dev/learn/preserving-and-resetting-state), which is how React understands which elements have changed.

### With TypeScript[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#with-typescript)

When using TypeScript, you must first create a new type for your pages which includes a `getLayout` function. Then, you must create a new type for your `AppProps` which overrides the `Component` property to use the previously created type.

pages/index.tsx

JavaScriptTypeScript
[code]
    import type { ReactElement } from 'react'
    import Layout from '../components/layout'
    import NestedLayout from '../components/nested-layout'
    import type { NextPageWithLayout } from './_app'
     
    const Page: NextPageWithLayout = () => {
      return <p>hello world</p>
    }
     
    Page.getLayout = function getLayout(page: ReactElement) {
      return (
        <Layout>
          <NestedLayout>{page}</NestedLayout>
        </Layout>
      )
    }
     
    export default Page
[/code]

pages/_app.tsx

JavaScriptTypeScript
[code]
    import type { ReactElement, ReactNode } from 'react'
    import type { NextPage } from 'next'
    import type { AppProps } from 'next/app'
     
    export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
      getLayout?: (page: ReactElement) => ReactNode
    }
     
    type AppPropsWithLayout = AppProps & {
      Component: NextPageWithLayout
    }
     
    export default function MyApp({ Component, pageProps }: AppPropsWithLayout) {
      // Use the layout defined at the page level, if available
      const getLayout = Component.getLayout ?? ((page) => page)
     
      return getLayout(<Component {...pageProps} />)
    }
[/code]

### Data Fetching[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#data-fetching)

Inside your layout, you can fetch data on the client-side using `useEffect` or a library like [SWR](https://swr.vercel.app/). Because this file is not a [Page](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts), you cannot use `getStaticProps` or `getServerSideProps` currently.

components/layout.js
[code]
    import useSWR from 'swr'
    import Navbar from './navbar'
    import Footer from './footer'
     
    export default function Layout({ children }) {
      const { data, error } = useSWR('/api/navigation', fetcher)
     
      if (error) return <div>Failed to load</div>
      if (!data) return <div>Loading...</div>
     
      return (
        <>
          <Navbar links={data.links} />
          <main>{children}</main>
          <Footer />
        </>
      )
    }
[/code]

Was this helpful?

supported.

Send
