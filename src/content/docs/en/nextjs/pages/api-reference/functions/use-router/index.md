---
title: 'Functions: useRouter'
description: 'If you want to access the  object inside any function component in your app, you can use the  hook, take a look at the following example:'
---

# Functions: useRouter | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/functions/use-router

[API Reference](https://nextjs.org/docs/pages/api-reference)[Functions](https://nextjs.org/docs/pages/api-reference/functions)useRouter

Copy page

# useRouter

Last updated February 20, 2026

If you want to access the [`router` object](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) inside any function component in your app, you can use the `useRouter` hook, take a look at the following example:
[code] 
    import { useRouter } from 'next/router'
     
    function ActiveLink({ children, href }) {
      const router = useRouter()
      const style = {
        marginRight: 10,
        color: router.asPath === href ? 'red' : 'black',
      }
     
      const handleClick = (e) => {
        e.preventDefault()
        router.push(href)
      }
     
      return (
        <a href={href} onClick={handleClick} style={style}>
          {children}
        </a>
      )
    }
     
    export default ActiveLink
[/code]

> `useRouter` is a [React Hook](https://react.dev/learn#using-hooks), meaning it cannot be used with classes. You can either use [withRouter](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter) or wrap your class in a function component.

## `router` object[](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)

The following is the definition of the `router` object returned by both [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#top) and [`withRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter):

  * `pathname`: `String` \- The path for current route file that comes after `/pages`. Therefore, `basePath`, `locale` and trailing slash (`trailingSlash: true`) are not included.
  * `query`: `Object` \- The query string parsed to an object, including [dynamic route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes) parameters. It will be an empty object during prerendering if the page doesn't use [Server-side Rendering](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props). Defaults to `{}`
  * `asPath`: `String` \- The path as shown in the browser including the search params and respecting the `trailingSlash` configuration. `basePath` and `locale` are not included.
  * `isFallback`: `boolean` \- Whether the current page is in [fallback mode](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true).
  * `basePath`: `String` \- The active [basePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath) (if enabled).
  * `locale`: `String` \- The active locale (if enabled).
  * `locales`: `String[]` \- All supported locales (if enabled).
  * `defaultLocale`: `String` \- The current default locale (if enabled).
  * `domainLocales`: `Array<{domain, defaultLocale, locales}>` \- Any configured domain locales.
  * `isReady`: `boolean` \- Whether the router fields are updated client-side and ready for use. Should only be used inside of `useEffect` methods and not for conditionally rendering on the server. See related docs for use case with [automatically statically optimized pages](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)
  * `isPreview`: `boolean` \- Whether the application is currently in [preview mode](https://nextjs.org/docs/pages/guides/preview-mode).



> Using the `asPath` field may lead to a mismatch between client and server if the page is rendered using server-side rendering or [automatic static optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization). Avoid using `asPath` until the `isReady` field is `true`.

The following methods are included inside `router`:

### router.push[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerpush)

Handles client-side transitions, this method is useful for cases where [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) is not enough.
[code] 
    router.push(url, as, options)
[/code]

  * `url`: `UrlObject | String` \- The URL to navigate to (see [Node.JS URL module documentation](https://nodejs.org/api/url.html#legacy-urlobject) for `UrlObject` properties).
  * `as`: `UrlObject | String` \- Optional decorator for the path that will be shown in the browser URL bar. Before Next.js 9.5.3 this was used for dynamic routes.
  * `options` \- Optional object with the following configuration options:
    * `scroll` \- Optional boolean, controls scrolling to the top of the page after navigation. Defaults to `true`
    * [`shallow`](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#shallow-routing): Update the path of the current page without rerunning [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props), [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) or [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props). Defaults to `false`
    * `locale` \- Optional string, indicates locale of the new page



> You don't need to use `router.push` for external URLs. [window.location](https://developer.mozilla.org/docs/Web/API/Window/location) is better suited for those cases.

Navigating to `pages/about.js`, which is a predefined route:
[code] 
    import { useRouter } from 'next/router'
     
    export default function Page() {
      const router = useRouter()
     
      return (
        <button type="button" onClick={() => router.push('/about')}>
          Click me
        </button>
      )
    }
[/code]

Navigating `pages/post/[pid].js`, which is a dynamic route:
[code] 
    import { useRouter } from 'next/router'
     
    export default function Page() {
      const router = useRouter()
     
      return (
        <button type="button" onClick={() => router.push('/post/abc')}>
          Click me
        </button>
      )
    }
[/code]

Redirecting the user to `pages/login.js`, useful for pages behind [authentication](https://nextjs.org/docs/pages/guides/authentication):
[code] 
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'
     
    // Here you would fetch and return the user
    const useUser = () => ({ user: null, loading: false })
     
    export default function Page() {
      const { user, loading } = useUser()
      const router = useRouter()
     
      useEffect(() => {
        if (!(user || loading)) {
          router.push('/login')
        }
      }, [user, loading])
     
      return <p>Redirecting...</p>
    }
[/code]

#### Resetting state after navigation[](https://nextjs.org/docs/pages/api-reference/functions/use-router#resetting-state-after-navigation)

When navigating to the same page in Next.js, the page's state **will not** be reset by default as React does not unmount unless the parent component has changed.

pages/[slug].js
[code]
    import Link from 'next/link'
    import { useState } from 'react'
    import { useRouter } from 'next/router'
     
    export default function Page(props) {
      const router = useRouter()
      const [count, setCount] = useState(0)
      return (
        <div>
          <h1>Page: {router.query.slug}</h1>
          <p>Count: {count}</p>
          <button onClick={() => setCount(count + 1)}>Increase count</button>
          <Link href="/one">one</Link> <Link href="/two">two</Link>
        </div>
      )
    }
[/code]

In the above example, navigating between `/one` and `/two` **will not** reset the count . The `useState` is maintained between renders because the top-level React component, `Page`, is the same.

If you do not want this behavior, you have a couple of options:

  * Manually ensure each state is updated using `useEffect`. In the above example, that could look like:
[code] useEffect(() => {
          setCount(0)
        }, [router.query.slug])
[/code]

  * Use a React `key` to [tell React to remount the component](https://react.dev/learn/rendering-lists#keeping-list-items-in-order-with-key). To do this for all pages, you can use a custom app:

pages/_app.js
[code]import { useRouter } from 'next/router'
         
        export default function MyApp({ Component, pageProps }) {
          const router = useRouter()
          return <Component key={router.asPath} {...pageProps} />
        }
[/code]




#### With URL object[](https://nextjs.org/docs/pages/api-reference/functions/use-router#with-url-object)

You can use a URL object in the same way you can use it for [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link#passing-a-url-object). Works for both the `url` and `as` parameters:
[code] 
    import { useRouter } from 'next/router'
     
    export default function ReadMore({ post }) {
      const router = useRouter()
     
      return (
        <button
          type="button"
          onClick={() => {
            router.push({
              pathname: '/post/[pid]',
              query: { pid: post.id },
            })
          }}
        >
          Click here to read more
        </button>
      )
    }
[/code]

### router.replace[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerreplace)

Similar to the `replace` prop in [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link), `router.replace` will prevent adding a new URL entry into the `history` stack.
[code] 
    router.replace(url, as, options)
[/code]

  * The API for `router.replace` is exactly the same as the API for [`router.push`](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerpush).



Take a look at the following example:
[code] 
    import { useRouter } from 'next/router'
     
    export default function Page() {
      const router = useRouter()
     
      return (
        <button type="button" onClick={() => router.replace('/home')}>
          Click me
        </button>
      )
    }
[/code]

### router.prefetch[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerprefetch)

Prefetch pages for faster client-side transitions. This method is only useful for navigations without [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link), as `next/link` takes care of prefetching pages automatically.

> This is a production only feature. Next.js doesn't prefetch pages in development.
[code] 
    router.prefetch(url, as, options)
[/code]

  * `url` \- The URL to prefetch, including explicit routes (e.g. `/dashboard`) and dynamic routes (e.g. `/product/[id]`)
  * `as` \- Optional decorator for `url`. Before Next.js 9.5.3 this was used to prefetch dynamic routes.
  * `options` \- Optional object with the following allowed fields:
    * `locale` \- allows providing a different locale from the active one. If `false`, `url` has to include the locale as the active locale won't be used.



Let's say you have a login page, and after a login, you redirect the user to the dashboard. For that case, we can prefetch the dashboard to make a faster transition, like in the following example:
[code] 
    import { useCallback, useEffect } from 'react'
    import { useRouter } from 'next/router'
     
    export default function Login() {
      const router = useRouter()
      const handleSubmit = useCallback((e) => {
        e.preventDefault()
     
        fetch('/api/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            /* Form data */
          }),
        }).then((res) => {
          // Do a fast client-side transition to the already prefetched dashboard page
          if (res.ok) router.push('/dashboard')
        })
      }, [])
     
      useEffect(() => {
        // Prefetch the dashboard page
        router.prefetch('/dashboard')
      }, [router])
     
      return (
        <form onSubmit={handleSubmit}>
          {/* Form fields */}
          <button type="submit">Login</button>
        </form>
      )
    }
[/code]

### router.beforePopState[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerbeforepopstate)

In some cases (for example, if using a [Custom Server](https://nextjs.org/docs/pages/guides/custom-server)), you may wish to listen to [popstate](https://developer.mozilla.org/docs/Web/API/Window/popstate_event) and do something before the router acts on it.
[code] 
    router.beforePopState(cb)
[/code]

  * `cb` \- The function to run on incoming `popstate` events. The function receives the state of the event as an object with the following props:
    * `url`: `String` \- the route for the new state. This is usually the name of a `page`
    * `as`: `String` \- the url that will be shown in the browser
    * `options`: `Object` \- Additional options sent by [router.push](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerpush)



If `cb` returns `false`, the Next.js router will not handle `popstate`, and you'll be responsible for handling it in that case. See [Disabling file-system routing](https://nextjs.org/docs/pages/guides/custom-server#disabling-file-system-routing).

You could use `beforePopState` to manipulate the request, or force a SSR refresh, as in the following example:
[code] 
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'
     
    export default function Page() {
      const router = useRouter()
     
      useEffect(() => {
        router.beforePopState(({ url, as, options }) => {
          // I only want to allow these two routes!
          if (as !== '/' && as !== '/other') {
            // Have SSR render bad routes as a 404.
            window.location.href = as
            return false
          }
     
          return true
        })
      }, [router])
     
      return <p>Welcome to the page</p>
    }
[/code]

### router.back[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerback)

Navigate back in history. Equivalent to clicking the browser’s back button. It executes `window.history.back()`.
[code] 
    import { useRouter } from 'next/router'
     
    export default function Page() {
      const router = useRouter()
     
      return (
        <button type="button" onClick={() => router.back()}>
          Click here to go back
        </button>
      )
    }
[/code]

### router.reload[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerreload)

Reload the current URL. Equivalent to clicking the browser’s refresh button. It executes `window.location.reload()`.
[code] 
    import { useRouter } from 'next/router'
     
    export default function Page() {
      const router = useRouter()
     
      return (
        <button type="button" onClick={() => router.reload()}>
          Click here to reload
        </button>
      )
    }
[/code]

### router.events[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerevents)

You can listen to different events happening inside the Next.js Router. Here's a list of supported events:

  * `routeChangeStart(url, { shallow })` \- Fires when a route starts to change
  * `routeChangeComplete(url, { shallow })` \- Fires when a route changed completely
  * `routeChangeError(err, url, { shallow })` \- Fires when there's an error when changing routes, or a route load is cancelled
    * `err.cancelled` \- Indicates if the navigation was cancelled
  * `beforeHistoryChange(url, { shallow })` \- Fires before changing the browser's history
  * `hashChangeStart(url, { shallow })` \- Fires when the hash will change but not the page
  * `hashChangeComplete(url, { shallow })` \- Fires when the hash has changed but not the page



> **Good to know** : Here `url` is the URL shown in the browser, including the [`basePath`](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath).

For example, to listen to the router event `routeChangeStart`, open or create `pages/_app.js` and subscribe to the event, like so:
[code] 
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'
     
    export default function MyApp({ Component, pageProps }) {
      const router = useRouter()
     
      useEffect(() => {
        const handleRouteChange = (url, { shallow }) => {
          console.log(
            `App is changing to ${url} ${
              shallow ? 'with' : 'without'
            } shallow routing`
          )
        }
     
        router.events.on('routeChangeStart', handleRouteChange)
     
        // If the component is unmounted, unsubscribe
        // from the event with the `off` method:
        return () => {
          router.events.off('routeChangeStart', handleRouteChange)
        }
      }, [router])
     
      return <Component {...pageProps} />
    }
[/code]

> We use a [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) (`pages/_app.js`) for this example to subscribe to the event because it's not unmounted on page navigations, but you can subscribe to router events on any component in your application.

Router events should be registered when a component mounts ([useEffect](https://react.dev/reference/react/useEffect) or [componentDidMount](https://react.dev/reference/react/Component#componentdidmount) / [componentWillUnmount](https://react.dev/reference/react/Component#componentwillunmount)) or imperatively when an event happens.

If a route load is cancelled (for example, by clicking two links rapidly in succession), `routeChangeError` will fire. And the passed `err` will contain a `cancelled` property set to `true`, as in the following example:
[code] 
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'
     
    export default function MyApp({ Component, pageProps }) {
      const router = useRouter()
     
      useEffect(() => {
        const handleRouteChangeError = (err, url) => {
          if (err.cancelled) {
            console.log(`Route to ${url} was cancelled!`)
          }
        }
     
        router.events.on('routeChangeError', handleRouteChangeError)
     
        // If the component is unmounted, unsubscribe
        // from the event with the `off` method:
        return () => {
          router.events.off('routeChangeError', handleRouteChangeError)
        }
      }, [router])
     
      return <Component {...pageProps} />
    }
[/code]

## The `next/compat/router` export[](https://nextjs.org/docs/pages/api-reference/functions/use-router#the-nextcompatrouter-export)

This is the same `useRouter` hook, but can be used in both `app` and `pages` directories.

It differs from `next/router` in that it does not throw an error when the pages router is not mounted, and instead has a return type of `NextRouter | null`. This allows developers to convert components to support running in both `app` and `pages` as they transition to the `app` router.

A component that previously looked like this:
[code] 
    import { useRouter } from 'next/router'
    const MyComponent = () => {
      const { isReady, query } = useRouter()
      // ...
    }
[/code]

Will error when converted over to `next/compat/router`, as `null` cannot be destructured. Instead, developers will be able to take advantage of new hooks:
[code] 
    import { useEffect } from 'react'
    import { useRouter } from 'next/compat/router'
    import { useSearchParams } from 'next/navigation'
    const MyComponent = () => {
      const router = useRouter() // may be null or a NextRouter instance
      const searchParams = useSearchParams()
      useEffect(() => {
        if (router && !router.isReady) {
          return
        }
        // In `app/`, searchParams will be ready immediately with the values, in
        // `pages/` it will be available after the router is ready.
        const search = searchParams.get('search')
        // ...
      }, [router, searchParams])
      // ...
    }
[/code]

This component will now work in both `pages` and `app` directories. When the component is no longer used in `pages`, you can remove the references to the compat router:
[code] 
    import { useSearchParams } from 'next/navigation'
    const MyComponent = () => {
      const searchParams = useSearchParams()
      // As this component is only used in `app/`, the compat router can be removed.
      const search = searchParams.get('search')
      // ...
    }
[/code]

### Using `useRouter` outside of Next.js context in pages[](https://nextjs.org/docs/pages/api-reference/functions/use-router#using-userouter-outside-of-nextjs-context-in-pages)

Another specific use case is when rendering components outside of a Next.js application context, such as inside `getServerSideProps` on the `pages` directory. In this case, the compat router can be used to avoid errors:
[code] 
    import { renderToString } from 'react-dom/server'
    import { useRouter } from 'next/compat/router'
    const MyComponent = () => {
      const router = useRouter() // may be null or a NextRouter instance
      // ...
    }
    export async function getServerSideProps() {
      const renderedComponent = renderToString(<MyComponent />)
      return {
        props: {
          renderedComponent,
        },
      }
    }
[/code]

## Potential ESLint errors[](https://nextjs.org/docs/pages/api-reference/functions/use-router#potential-eslint-errors)

Certain methods accessible on the `router` object return a Promise. If you have the ESLint rule, [no-floating-promises](https://typescript-eslint.io/rules/no-floating-promises) enabled, consider disabling it either globally, or for the affected line.

If your application needs this rule, you should either `void` the promise – or use an `async` function, `await` the Promise, then void the function call. **This is not applicable when the method is called from inside an`onClick` handler**.

The affected methods are:

  * `router.push`
  * `router.replace`
  * `router.prefetch`



### Potential solutions[](https://nextjs.org/docs/pages/api-reference/functions/use-router#potential-solutions)
[code] 
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'
     
    // Here you would fetch and return the user
    const useUser = () => ({ user: null, loading: false })
     
    export default function Page() {
      const { user, loading } = useUser()
      const router = useRouter()
     
      useEffect(() => {
        // disable the linting on the next line - This is the cleanest solution
        // eslint-disable-next-line no-floating-promises
        router.push('/login')
     
        // void the Promise returned by router.push
        if (!(user || loading)) {
          void router.push('/login')
        }
        // or use an async function, await the Promise, then void the function call
        async function handleRouteChange() {
          if (!(user || loading)) {
            await router.push('/login')
          }
        }
        void handleRouteChange()
      }, [user, loading])
     
      return <p>Redirecting...</p>
    }
[/code]

## withRouter[](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter)

If [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) is not the best fit for you, `withRouter` can also add the same [`router` object](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) to any component.

### Usage[](https://nextjs.org/docs/pages/api-reference/functions/use-router#usage)
[code] 
    import { withRouter } from 'next/router'
     
    function Page({ router }) {
      return <p>{router.pathname}</p>
    }
     
    export default withRouter(Page)
[/code]

### TypeScript[](https://nextjs.org/docs/pages/api-reference/functions/use-router#typescript)

To use class components with `withRouter`, the component needs to accept a router prop:
[code] 
    import React from 'react'
    import { withRouter, NextRouter } from 'next/router'
     
    interface WithRouterProps {
      router: NextRouter
    }
     
    interface MyComponentProps extends WithRouterProps {}
     
    class MyComponent extends React.Component<MyComponentProps> {
      render() {
        return <p>{this.props.router.pathname}</p>
      }
    }
     
    export default withRouter(MyComponent)
[/code]

Was this helpful?

supported.

Send
