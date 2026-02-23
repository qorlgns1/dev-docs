---
title: 'Getting Started: Server and Client Components'
description: 'By default, layouts and pages are Server Components, which lets you fetch data and render parts of your UI on the server, optionally cache the result,...'
---

# Getting Started: Server and Client Components | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/server-and-client-components

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Server and Client Components

Copy page

# Server and Client Components

Last updated February 20, 2026

By default, layouts and pages are [Server Components](https://react.dev/reference/rsc/server-components), which lets you fetch data and render parts of your UI on the server, optionally cache the result, and stream it to the client. When you need interactivity or browser APIs, you can use [Client Components](https://react.dev/reference/rsc/use-client) to layer in functionality.

This page explains how Server and Client Components work in Next.js and when to use them, with examples of how to compose them together in your application.

## When to use Server and Client Components?[](https://nextjs.org/docs/app/getting-started/server-and-client-components#when-to-use-server-and-client-components)

The client and server environments have different capabilities. Server and Client components allow you to run logic in each environment depending on your use case.

Use **Client Components** when you need:

  * [State](https://react.dev/learn/managing-state) and [event handlers](https://react.dev/learn/responding-to-events). E.g. `onClick`, `onChange`.
  * [Lifecycle logic](https://react.dev/learn/lifecycle-of-reactive-effects). E.g. `useEffect`.
  * Browser-only APIs. E.g. `localStorage`, `window`, `Navigator.geolocation`, etc.
  * [Custom hooks](https://react.dev/learn/reusing-logic-with-custom-hooks).



Use **Server Components** when you need:

  * Fetch data from databases or APIs close to the source.
  * Use API keys, tokens, and other secrets without exposing them to the client.
  * Reduce the amount of JavaScript sent to the browser.
  * Improve the [First Contentful Paint (FCP)](https://web.dev/fcp/), and stream content progressively to the client.



For example, the `<Page>` component is a Server Component that fetches data about a post, and passes it as props to the `<LikeButton>` which handles client-side interactivity.

app/[id]/page.tsx

JavaScriptTypeScript
[code]
    import LikeButton from '@/app/ui/like-button'
    import { getPost } from '@/lib/data'
     
    export default async function Page({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      const post = await getPost(id)
     
      return (
        <div>
          <main>
            <h1>{post.title}</h1>
            {/* ... */}
            <LikeButton likes={post.likes} />
          </main>
        </div>
      )
    }
[/code]

app/ui/like-button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useState } from 'react'
     
    export default function LikeButton({ likes }: { likes: number }) {
      // ...
    }
[/code]

## How do Server and Client Components work in Next.js?[](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs)

### On the server[](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-server)

On the server, Next.js uses React's APIs to orchestrate rendering. The rendering work is split into chunks, by individual route segments ([layouts and pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)):

  * **Server Components** are rendered into a special data format called the React Server Component Payload (RSC Payload).
  * **Client Components** and the RSC Payload are used to [pre-render](https://nextjs.org/docs/app/guides/caching#rendering-strategies) HTML.



> **What is the React Server Component Payload (RSC)?**
> 
> The RSC Payload is a compact binary representation of the rendered React Server Components tree. It's used by React on the client to update the browser's DOM. The RSC Payload contains:
> 
>   * The rendered result of Server Components
>   * Placeholders for where Client Components should be rendered and references to their JavaScript files
>   * Any props passed from a Server Component to a Client Component
> 


### On the client (first load)[](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-client-first-load)

Then, on the client:

  1. **HTML** is used to immediately show a fast non-interactive preview of the route to the user.
  2. **RSC Payload** is used to reconcile the Client and Server Component trees.
  3. **JavaScript** is used to hydrate Client Components and make the application interactive.



> **What is hydration?**
> 
> Hydration is React's process for attaching [event handlers](https://react.dev/learn/responding-to-events) to the DOM, to make the static HTML interactive.

### Subsequent Navigations[](https://nextjs.org/docs/app/getting-started/server-and-client-components#subsequent-navigations)

On subsequent navigations:

  * The **RSC Payload** is prefetched and cached for instant navigation.
  * **Client Components** are rendered entirely on the client, without the server-rendered HTML.



## Examples[](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples)

### Using Client Components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#using-client-components)

You can create a Client Component by adding the [`"use client"`](https://react.dev/reference/react/use-client) directive at the top of the file, above your imports.

app/ui/counter.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useState } from 'react'
     
    export default function Counter() {
      const [count, setCount] = useState(0)
     
      return (
        <div>
          <p>{count} likes</p>
          <button onClick={() => setCount(count + 1)}>Click me</button>
        </div>
      )
    }
[/code]

`"use client"` is used to declare a **boundary** between the Server and Client module graphs (trees).

Once a file is marked with `"use client"`, **all its imports and child components are considered part of the client bundle**. This means you don't need to add the directive to every component that is intended for the client.

### Reducing JS bundle size[](https://nextjs.org/docs/app/getting-started/server-and-client-components#reducing-js-bundle-size)

To reduce the size of your client JavaScript bundles, add `'use client'` to specific interactive components instead of marking large parts of your UI as Client Components.

For example, the `<Layout>` component contains mostly static elements like a logo and navigation links, but includes an interactive search bar. `<Search />` is interactive and needs to be a Client Component, however, the rest of the layout can remain a Server Component.

app/layout.tsx

JavaScriptTypeScript
[code]
    // Client Component
    import Search from './search'
    // Server Component
    import Logo from './logo'
     
    // Layout is a Server Component by default
    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <>
          <nav>
            <Logo />
            <Search />
          </nav>
          <main>{children}</main>
        </>
      )
    }
[/code]

app/ui/search.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function Search() {
      // ...
    }
[/code]

### Passing data from Server to Client Components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#passing-data-from-server-to-client-components)

You can pass data from Server Components to Client Components using props.

app/[id]/page.tsx

JavaScriptTypeScript
[code]
    import LikeButton from '@/app/ui/like-button'
    import { getPost } from '@/lib/data'
     
    export default async function Page({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      const post = await getPost(id)
     
      return <LikeButton likes={post.likes} />
    }
[/code]

app/ui/like-button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function LikeButton({ likes }: { likes: number }) {
      // ...
    }
[/code]

Alternatively, you can stream data from a Server Component to a Client Component with the [`use` API](https://react.dev/reference/react/use). See an [example](https://nextjs.org/docs/app/getting-started/fetching-data#streaming-data-with-the-use-api).

> **Good to know** : Props passed to Client Components need to be [serializable](https://react.dev/reference/react/use-server#serializable-parameters-and-return-values) by React.

### Interleaving Server and Client Components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#interleaving-server-and-client-components)

You can pass Server Components as a prop to a Client Component. This allows you to visually nest server-rendered UI within Client components.

A common pattern is to use `children` to create a _slot_ in a `<ClientComponent>`. For example, a `<Cart>` component that fetches data on the server, inside a `<Modal>` component that uses client state to toggle visibility.

app/ui/modal.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function Modal({ children }: { children: React.ReactNode }) {
      return <div>{children}</div>
    }
[/code]

Then, in a parent Server Component (e.g.`<Page>`), you can pass a `<Cart>` as the child of the `<Modal>`:

app/page.tsx

JavaScriptTypeScript
[code]
    import Modal from './ui/modal'
    import Cart from './ui/cart'
     
    export default function Page() {
      return (
        <Modal>
          <Cart />
        </Modal>
      )
    }
[/code]

In this pattern, all Server Components will be rendered on the server ahead of time, including those as props. The resulting RSC payload will contain references of where Client Components should be rendered within the component tree.

### Context providers[](https://nextjs.org/docs/app/getting-started/server-and-client-components#context-providers)

[React context](https://react.dev/learn/passing-data-deeply-with-context) is commonly used to share global state like the current theme. However, React context is not supported in Server Components.

To use context, create a Client Component that accepts `children`:

app/theme-provider.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { createContext } from 'react'
     
    export const ThemeContext = createContext({})
     
    export default function ThemeProvider({
      children,
    }: {
      children: React.ReactNode
    }) {
      return <ThemeContext.Provider value="dark">{children}</ThemeContext.Provider>
    }
[/code]

Then, import it into a Server Component (e.g. `layout`):

app/layout.tsx

JavaScriptTypeScript
[code]
    import ThemeProvider from './theme-provider'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html>
          <body>
            <ThemeProvider>{children}</ThemeProvider>
          </body>
        </html>
      )
    }
[/code]

Your Server Component will now be able to directly render your provider, and all other Client Components throughout your app will be able to consume this context.

> **Good to know** : You should render providers as deep as possible in the tree – notice how `ThemeProvider` only wraps `{children}` instead of the entire `<html>` document. This makes it easier for Next.js to optimize the static parts of your Server Components.

### Sharing data with context and React.cache[](https://nextjs.org/docs/app/getting-started/server-and-client-components#sharing-data-with-context-and-reactcache)

You can share fetched data across both Server and Client Components by combining [`React.cache`](https://react.dev/reference/react/cache) with context providers.

Create a cached function that fetches data:

app/lib/user.ts

JavaScriptTypeScript
[code]
    import { cache } from 'react'
     
    export const getUser = cache(async () => {
      const res = await fetch('https://api.example.com/user')
      return res.json()
    })
[/code]

Create a context provider that stores the promise:

app/user-provider.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { createContext } from 'react'
     
    type User = {
      id: string
      name: string
    }
     
    export const UserContext = createContext<Promise<User> | null>(null)
     
    export default function UserProvider({
      children,
      userPromise,
    }: {
      children: React.ReactNode
      userPromise: Promise<User>
    }) {
      return <UserContext value={userPromise}>{children}</UserContext>
    }
[/code]

In a layout, pass the promise to the provider without awaiting:

app/layout.tsx

JavaScriptTypeScript
[code]
    import UserProvider from './user-provider'
    import { getUser } from './lib/user'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      const userPromise = getUser() // Don't await
     
      return (
        <html>
          <body>
            <UserProvider userPromise={userPromise}>{children}</UserProvider>
          </body>
        </html>
      )
    }
[/code]

Client Components use [`use()`](https://react.dev/reference/react/use) to resolve the promise from context, wrapped in `<Suspense>` for fallback UI:

app/ui/profile.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { use, useContext } from 'react'
    import { UserContext } from '../user-provider'
     
    export function Profile() {
      const userPromise = useContext(UserContext)
      if (!userPromise) {
        throw new Error('useContext must be used within a UserProvider')
      }
      const user = use(userPromise)
      return <p>Welcome, {user.name}</p>
    }
[/code]

app/page.tsx

JavaScriptTypeScript
[code]
    import { Suspense } from 'react'
    import { Profile } from './ui/profile'
     
    export default function Page() {
      return (
        <Suspense fallback={<div>Loading profile...</div>}>
          <Profile />
        </Suspense>
      )
    }
[/code]

Server Components can also call `getUser()` directly:

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { getUser } from '../lib/user'
     
    export default async function DashboardPage() {
      const user = await getUser() // Cached - same request, no duplicate fetch
      return <h1>Dashboard for {user.name}</h1>
    }
[/code]

Since `getUser` is wrapped with `React.cache`, multiple calls within the same request return the same memoized result, whether called directly in Server Components or resolved via context in Client Components.

> **Good to know** : `React.cache` is scoped to the current request only. Each request gets its own memoization scope with no sharing between requests.

### Third-party components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#third-party-components)

When using a third-party component that relies on client-only features, you can wrap it in a Client Component to ensure it works as expected.

For example, the `<Carousel />` can be imported from the `acme-carousel` package. This component uses `useState`, but it doesn't yet have the `"use client"` directive.

If you use `<Carousel />` within a Client Component, it will work as expected:

app/gallery.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useState } from 'react'
    import { Carousel } from 'acme-carousel'
     
    export default function Gallery() {
      const [isOpen, setIsOpen] = useState(false)
     
      return (
        <div>
          <button onClick={() => setIsOpen(true)}>View pictures</button>
          {/* Works, since Carousel is used within a Client Component */}
          {isOpen && <Carousel />}
        </div>
      )
    }
[/code]

However, if you try to use it directly within a Server Component, you'll see an error. This is because Next.js doesn't know `<Carousel />` is using client-only features.

To fix this, you can wrap third-party components that rely on client-only features in your own Client Components:

app/carousel.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { Carousel } from 'acme-carousel'
     
    export default Carousel
[/code]

Now, you can use `<Carousel />` directly within a Server Component:

app/page.tsx

JavaScriptTypeScript
[code]
    import Carousel from './carousel'
     
    export default function Page() {
      return (
        <div>
          <p>View pictures</p>
          {/*  Works, since Carousel is a Client Component */}
          <Carousel />
        </div>
      )
    }
[/code]

> **Advice for Library Authors**
> 
> If you’re building a component library, add the `"use client"` directive to entry points that rely on client-only features. This lets your users import components into Server Components without needing to create wrappers.
> 
> It's worth noting some bundlers might strip out `"use client"` directives. You can find an example of how to configure esbuild to include the `"use client"` directive in the [React Wrap Balancer](https://github.com/shuding/react-wrap-balancer/blob/main/tsup.config.ts#L10-L13) and [Vercel Analytics](https://github.com/vercel/analytics/blob/main/packages/web/tsup.config.js#L26-L30) repositories.

### Preventing environment poisoning[](https://nextjs.org/docs/app/getting-started/server-and-client-components#preventing-environment-poisoning)

JavaScript modules can be shared between both Server and Client Components modules. This means it's possible to accidentally import server-only code into the client. For example, consider the following function:

lib/data.ts

JavaScriptTypeScript
[code]
    export async function getData() {
      const res = await fetch('https://external-service.com/data', {
        headers: {
          authorization: process.env.API_KEY,
        },
      })
     
      return res.json()
    }
[/code]

This function contains an `API_KEY` that should never be exposed to the client.

In Next.js, only environment variables prefixed with `NEXT_PUBLIC_` are included in the client bundle. If variables are not prefixed, Next.js replaces them with an empty string.

As a result, even though `getData()` can be imported and executed on the client, it won't work as expected.

To prevent accidental usage in Client Components, you can use the [`server-only` package](https://www.npmjs.com/package/server-only).

Then, import the package into a file that contains server-only code:

lib/data.js
[code]
    import 'server-only'
     
    export async function getData() {
      const res = await fetch('https://external-service.com/data', {
        headers: {
          authorization: process.env.API_KEY,
        },
      })
     
      return res.json()
    }
[/code]

Now, if you try to import the module into a Client Component, there will be a build-time error.

The corresponding [`client-only` package](https://www.npmjs.com/package/client-only) can be used to mark modules that contain client-only logic like code that accesses the `window` object.

In Next.js, installing `server-only` or `client-only` is **optional**. However, if your linting rules flag extraneous dependencies, you may install them to avoid issues.

pnpmnpmyarnbun

Terminal
[code]
    pnpm add server-only
[/code]

Next.js handles `server-only` and `client-only` imports internally to provide clearer error messages when a module is used in the wrong environment. The contents of these packages from NPM are not used by Next.js.

Next.js also provides its own type declarations for `server-only` and `client-only`, for TypeScript configurations where [`noUncheckedSideEffectImports`](https://www.typescriptlang.org/tsconfig/#noUncheckedSideEffectImports) is active.

## Next Steps

Learn more about the APIs mentioned in this page.

### [use clientLearn how to use the use client directive to render a component on the client.](https://nextjs.org/docs/app/api-reference/directives/use-client)

Was this helpful?

supported.

Send
