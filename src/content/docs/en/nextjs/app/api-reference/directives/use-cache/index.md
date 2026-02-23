---
title: 'Directives: use cache'
description: 'The  directive allows you to mark a route, React component, or a function as cacheable. It can be used at the top of a file to indicate that all expor...'
---

# Directives: use cache | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/directives/use-cache

[API Reference](https://nextjs.org/docs/app/api-reference)[Directives](https://nextjs.org/docs/app/api-reference/directives)use cache

Copy page

# use cache

Last updated February 20, 2026

The `use cache` directive allows you to mark a route, React component, or a function as cacheable. It can be used at the top of a file to indicate that all exports in the file should be cached, or inline at the top of function or component to cache the return value.

> **Good to know:**
> 
>   * To use cookies or headers, read them outside cached scopes and pass values as arguments. This is the preferred pattern.
>   * If the in-memory cache isn't sufficient for runtime data, [`'use cache: remote'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote) allows platforms to provide a dedicated cache handler, though it requires a network roundtrip to check the cache and typically incurs platform fees.
>   * For compliance requirements or when you can't refactor to pass runtime data as arguments to a `use cache` scope, see [`'use cache: private'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private).
> 


## Usage[](https://nextjs.org/docs/app/api-reference/directives/use-cache#usage)

`use cache` is a Cache Components feature. To enable it, add the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) option to your `next.config.ts` file:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      cacheComponents: true,
    }
     
    export default nextConfig
[/code]

Then, add `use cache` at the file, component, or function level:
[code] 
    // File level
    'use cache'
     
    export default async function Page() {
      // ...
    }
     
    // Component level
    export async function MyComponent() {
      'use cache'
      return <></>
    }
     
    // Function level
    export async function getData() {
      'use cache'
      const data = await fetch('/api/data')
      return data
    }
[/code]

> **Good to know** : When used at file level, all function exports must be async functions.

## How `use cache` works[](https://nextjs.org/docs/app/api-reference/directives/use-cache#how-use-cache-works)

### Cache keys[](https://nextjs.org/docs/app/api-reference/directives/use-cache#cache-keys)

A cache entry's key is generated using a serialized version of its inputs, which includes:

  1. **Build ID** \- Unique per build, changing this invalidates all cache entries
  2. **Function ID** \- A secure hash of the function's location and signature in the codebase
  3. **Serializable arguments** \- Props (for components) or function arguments
  4. **HMR refresh hash** (development only) - Invalidates cache on hot module replacement



When a cached function references variables from outer scopes, those variables are automatically captured and bound as arguments, making them part of the cache key.

lib/data.ts
[code]
    async function Component({ userId }: { userId: string }) {
      const getData = async (filter: string) => {
        'use cache'
        // Cache key includes both userId (from closure) and filter (argument)
        return fetch(`/api/users/${userId}/data?filter=${filter}`)
      }
     
      return getData('active')
    }
[/code]

In the snippet above, `userId` is captured from the outer scope and `filter` is passed as an argument, so both become part of the `getData` function's cache key. This means different user and filter combinations will have separate cache entries.

## Serialization[](https://nextjs.org/docs/app/api-reference/directives/use-cache#serialization)

Arguments to cached functions and their return values must be serializable.

For a complete reference, see:

  * [Serializable arguments](https://react.dev/reference/rsc/use-server#serializable-parameters-and-return-values) \- Uses **React Server Components** serialization
  * [Serializable return types](https://react.dev/reference/rsc/use-client#serializable-types) \- Uses **React Client Components** serialization



> **Good to know:** Arguments and return values use different serialization systems. Server Component serialization (for arguments) is more restrictive than Client Component serialization (for return values). This means you can return JSX elements but cannot accept them as arguments unless using pass-through patterns.

### Supported types[](https://nextjs.org/docs/app/api-reference/directives/use-cache#supported-types)

**Arguments:**

  * Primitives: `string`, `number`, `boolean`, `null`, `undefined`
  * Plain objects: `{ key: value }`
  * Arrays: `[1, 2, 3]`
  * Dates, Maps, Sets, TypedArrays, ArrayBuffers
  * React elements (as pass-through only)



**Return values:**

  * Same as arguments, plus JSX elements



### Unsupported types[](https://nextjs.org/docs/app/api-reference/directives/use-cache#unsupported-types)

  * Class instances
  * Functions (except as pass-through)
  * Symbols, WeakMaps, WeakSets
  * URL instances



app/components/user-card.tsx
[code]
    // Valid - primitives and plain objects
    async function UserCard({
      id,
      config,
    }: {
      id: string
      config: { theme: string }
    }) {
      'use cache'
      return <div>{id}</div>
    }
     
    // Invalid - class instance
    async function UserProfile({ user }: { user: UserClass }) {
      'use cache'
      // Error: Cannot serialize class instance
      return <div>{user.name}</div>
    }
[/code]

### Pass-through (non-serializable arguments)[](https://nextjs.org/docs/app/api-reference/directives/use-cache#pass-through-non-serializable-arguments)

You can accept non-serializable values **as long as you don't introspect them**. This enables composition patterns with `children` and Server Actions:

app/components/cached-wrapper.tsx
[code]
    async function CachedWrapper({ children }: { children: ReactNode }) {
      'use cache'
      // Don't read or modify children - just pass it through
      return (
        <div className="wrapper">
          <header>Cached Header</header>
          {children}
        </div>
      )
    }
     
    // Usage: children can be dynamic
    export default function Page() {
      return (
        <CachedWrapper>
          <DynamicComponent /> {/* Not cached, passed through */}
        </CachedWrapper>
      )
    }
[/code]

You can also pass Server Actions through cached components:

app/components/cached-form.tsx
[code]
    async function CachedForm({ action }: { action: () => Promise<void> }) {
      'use cache'
      // Don't call action here - just pass it through
      return <form action={action}>{/* ... */}</form>
    }
[/code]

## Constraints[](https://nextjs.org/docs/app/api-reference/directives/use-cache#constraints)

Cached functions execute in an isolated environment. The following constraints ensure cache behavior remains predictable and secure.

### Runtime APIs[](https://nextjs.org/docs/app/api-reference/directives/use-cache#runtime-apis)

Cached functions and components **cannot** directly access runtime APIs like `cookies()`, `headers()`, or `searchParams`. Instead, read these values outside the cached scope and pass them as arguments.

### Runtime caching considerations[](https://nextjs.org/docs/app/api-reference/directives/use-cache#runtime-caching-considerations)

While `use cache` is designed primarily to include dynamic data in the static shell, it can also cache data at runtime using in-memory LRU (Least Recently Used) storage.

Runtime cache behavior depends on your hosting environment:

Environment| Runtime Caching Behavior  
---|---  
**Serverless**|  Cache entries typically don't persist across requests (each request can be a different instance). Build-time caching works normally.  
**Self-hosted**|  Cache entries persist across requests. Control cache size with [`cacheMaxMemorySize`](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath).  
  
If the default in-memory cache isn't enough, consider **[`use cache: remote`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote)** which allows platforms to provide a dedicated cache handler (like Redis or KV database). This helps reduce hits against data sources not scaled to your total traffic, though it comes with costs (storage, network latency, platform fees).

Very rarely, for compliance requirements or when you can't refactor your code to pass runtime data as arguments to a `use cache` scope, you might need [`use cache: private`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private).

### React.cache isolation[](https://nextjs.org/docs/app/api-reference/directives/use-cache#reactcache-isolation)

[`React.cache`](https://react.dev/reference/react/cache) operates in an isolated scope inside `use cache` boundaries. Values stored via `React.cache` outside a `use cache` function are not visible inside it.

This means you cannot use `React.cache` to pass data into a `use cache` scope:
[code] 
    import { cache } from 'react'
     
    const store = cache(() => ({ current: null as string | null }))
     
    function Parent() {
      const shared = store()
      shared.current = 'value from parent'
      return <Child />
    }
     
    async function Child() {
      'use cache'
      const shared = store()
      // shared.current is null, not 'value from parent'
      // use cache has its own isolated React.cache scope
      return <div>{shared.current}</div>
    }
[/code]

This isolation ensures cached functions have predictable, self-contained behavior. To pass data into a `use cache` scope, use function arguments instead.

## `use cache` at runtime[](https://nextjs.org/docs/app/api-reference/directives/use-cache#use-cache-at-runtime)

On the **server** , cache entries are stored in-memory and respect the `revalidate` and `expire` times from your `cacheLife` configuration. You can customize the cache storage by configuring [`cacheHandlers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers) in your `next.config.js` file.

On the **client** , content from the server cache is stored in the browser's memory for the duration defined by the `stale` time. The client router enforces a **minimum 30-second stale time** , regardless of configuration.

The `x-nextjs-stale-time` response header communicates cache lifetime from server to client, ensuring coordinated behavior.

## Revalidation[](https://nextjs.org/docs/app/api-reference/directives/use-cache#revalidation)

By default, `use cache` uses the `default` profile with these settings:

  * **stale** : 5 minutes (client-side)
  * **revalidate** : 15 minutes (server-side)
  * **expire** : Never expires by time



lib/data.ts
[code]
    async function getData() {
      'use cache'
      // Implicitly uses default profile
      return fetch('/api/data')
    }
[/code]

### Customizing cache lifetime[](https://nextjs.org/docs/app/api-reference/directives/use-cache#customizing-cache-lifetime)

Use the [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) function to customize cache duration:

lib/data.ts
[code]
    import { cacheLife } from 'next/cache'
     
    async function getData() {
      'use cache'
      cacheLife('hours') // Use built-in 'hours' profile
      return fetch('/api/data')
    }
[/code]

### On-demand revalidation[](https://nextjs.org/docs/app/api-reference/directives/use-cache#on-demand-revalidation)

Use [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag), [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag), or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) for on-demand cache invalidation:

lib/data.ts
[code]
    import { cacheTag } from 'next/cache'
     
    async function getProducts() {
      'use cache'
      cacheTag('products')
      return fetch('/api/products')
    }
[/code]

app/actions.ts
[code]
    'use server'
     
    import { updateTag } from 'next/cache'
     
    export async function updateProduct() {
      await db.products.update(...)
      updateTag('products') // Invalidates all 'products' caches
    }
[/code]

Both `cacheLife` and `cacheTag` integrate across client and server caching layers, meaning you configure your caching semantics in one place and they apply everywhere.

## Examples[](https://nextjs.org/docs/app/api-reference/directives/use-cache#examples)

### Caching an entire route with `use cache`[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-an-entire-route-with-use-cache)

To pre-render an entire route, add `use cache` to the top of **both** the `layout` and `page` files. Each of these segments are treated as separate entry points in your application, and will be cached independently.

app/layout.tsx

JavaScriptTypeScript
[code]
    'use cache'
     
    export default async function Layout({ children }: { children: ReactNode }) {
      return <div>{children}</div>
    }
[/code]

Any components imported and nested in `page` file are part of the cache output associated with the `page`.

app/page.tsx

JavaScriptTypeScript
[code]
    'use cache'
     
    async function Users() {
      const users = await fetch('/api/users')
      // loop through users
    }
     
    export default async function Page() {
      return (
        <main>
          <Users />
        </main>
      )
    }
[/code]

> **Good to know** :
> 
>   * If `use cache` is added only to the `layout` or the `page`, only that route segment and any components imported into it will be cached.
> 


### Caching a component's output with `use cache`[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-a-components-output-with-use-cache)

You can use `use cache` at the component level to cache any fetches or computations performed within that component. The cache entry will be reused as long as the serialized props produce the same value in each instance.

app/components/bookings.tsx

JavaScriptTypeScript
[code]
    export async function Bookings({ type = 'haircut' }: BookingsProps) {
      'use cache'
      async function getBookingsData() {
        const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
        return data
      }
      return //...
    }
     
    interface BookingsProps {
      type: string
    }
[/code]

### Caching function output with `use cache`[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-function-output-with-use-cache)

Since you can add `use cache` to any asynchronous function, you aren't limited to caching components or routes only. You might want to cache a network request, a database query, or a slow computation.

app/actions.ts

JavaScriptTypeScript
[code]
    export async function getData() {
      'use cache'
     
      const data = await fetch('/api/data')
      return data
    }
[/code]

### Interleaving[](https://nextjs.org/docs/app/api-reference/directives/use-cache#interleaving)

In React, composition with `children` or slots is a well-known pattern for building flexible components. When using `use cache`, you can continue to compose your UI in this way. Anything included as `children`, or other compositional slots, in the returned JSX will be passed through the cached component without affecting its cache entry.

As long as you don't directly reference any of the JSX slots inside the body of the cacheable function itself, their presence in the returned output won't affect the cache entry.

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const uncachedData = await getData()
      return (
        // Pass compositional slots as props, e.g. header and children
        <CacheComponent header={<h1>Home</h1>}>
          {/* DynamicComponent is provided as the children slot */}
          <DynamicComponent data={uncachedData} />
        </CacheComponent>
      )
    }
     
    async function CacheComponent({
      header, // header: a compositional slot, injected as a prop
      children, // children: another slot for nested composition
    }: {
      header: ReactNode
      children: ReactNode
    }) {
      'use cache'
      const cachedData = await fetch('/api/cached-data')
      return (
        <div>
          {header}
          <PrerenderedComponent data={cachedData} />
          {children}
        </div>
      )
    }
[/code]

You can also pass Server Actions through cached components to Client Components without invoking them inside the cacheable function.

app/page.tsx

JavaScriptTypeScript
[code]
    import ClientComponent from './ClientComponent'
     
    export default async function Page() {
      const performUpdate = async () => {
        'use server'
        // Perform some server-side update
        await db.update(...)
      }
     
      return <CachedComponent performUpdate={performUpdate} />
    }
     
    async function CachedComponent({
      performUpdate,
    }: {
      performUpdate: () => Promise<void>
    }) {
      'use cache'
      // Do not call performUpdate here
      return <ClientComponent action={performUpdate} />
    }
[/code]

app/ClientComponent.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function ClientComponent({
      action,
    }: {
      action: () => Promise<void>
    }) {
      return <button onClick={action}>Update</button>
    }
[/code]

## Troubleshooting[](https://nextjs.org/docs/app/api-reference/directives/use-cache#troubleshooting)

### Debugging cache behavior[](https://nextjs.org/docs/app/api-reference/directives/use-cache#debugging-cache-behavior)

#### Verbose logging[](https://nextjs.org/docs/app/api-reference/directives/use-cache#verbose-logging)

Set `NEXT_PRIVATE_DEBUG_CACHE=1` for verbose cache logging:
[code] 
    NEXT_PRIVATE_DEBUG_CACHE=1 npm run dev
    # or for production
    NEXT_PRIVATE_DEBUG_CACHE=1 npm run start
[/code]

> **Good to know:** This environment variable also logs ISR and other caching mechanisms. See [Verifying correct production behavior](https://nextjs.org/docs/app/guides/incremental-static-regeneration#verifying-correct-production-behavior) for more details.

#### Console log replays[](https://nextjs.org/docs/app/api-reference/directives/use-cache#console-log-replays)

In development, console logs from cached functions appear with a `Cache` prefix.

### Build Hangs (Cache Timeout)[](https://nextjs.org/docs/app/api-reference/directives/use-cache#build-hangs-cache-timeout)

If your build hangs, you're accessing Promises that resolve to dynamic or runtime data, created outside a `use cache` boundary. The cached function waits for data that can't resolve during the build, causing a timeout after 50 seconds.

When the build timeouts you'll see this error message:

> Error: Filling a cache during prerender timed out, likely because request-specific arguments such as params, searchParams, cookies() or dynamic data were used inside "use cache".

Common ways this happens: passing such Promises as props, accessing them via closure, or retrieving them from shared storage (Maps).

> **Good to know:** Directly calling `cookies()` or `headers()` inside `use cache` fails immediately with a [different error](https://nextjs.org/docs/messages/next-request-in-use-cache), not a timeout.

**Passing runtime data Promises as props:**

app/page.tsx
[code]
    import { cookies } from 'next/headers'
    import { Suspense } from 'react'
     
    export default function Page() {
      return (
        <Suspense fallback={<div>Loading...</div>}>
          <Dynamic />
        </Suspense>
      )
    }
     
    async function Dynamic() {
      const cookieStore = cookies()
      return <Cached promise={cookieStore} /> // Build hangs
    }
     
    async function Cached({ promise }: { promise: Promise<unknown> }) {
      'use cache'
      const data = await promise // Waits for runtime data during build
      return <p>..</p>
    }
[/code]

Await the `cookies` store in the `Dynamic` component, and pass a cookie value to the `Cached` component.

**Shared deduplication storage:**

app/page.tsx
[code]
    // Problem: Map stores dynamic Promises, accessed by cached code
    import { Suspense } from 'react'
     
    const cache = new Map<string, Promise<string>>()
     
    export default function Page() {
      return (
        <>
          <Suspense fallback={<div>Loading...</div>}>
            <Dynamic id="data" />
          </Suspense>
          <Cached id="data" />
        </>
      )
    }
     
    async function Dynamic({ id }: { id: string }) {
      // Stores dynamic Promise in shared Map
      cache.set(
        id,
        fetch(`https://api.example.com/${id}`).then((r) => r.text())
      )
      return <p>Dynamic</p>
    }
     
    async function Cached({ id }: { id: string }) {
      'use cache'
      return <p>{await cache.get(id)}</p> // Build hangs - retrieves dynamic Promise
    }
[/code]

Use Next.js's built-in `fetch()` deduplication or use separate Maps for cached and uncached contexts.

## Platform Support[](https://nextjs.org/docs/app/api-reference/directives/use-cache#platform-support)

Deployment Option| Supported  
---|---  
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| Yes  
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| Yes  
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| No  
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| Platform-specific  
  
Learn how to [configure caching](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr) when self-hosting Next.js.

## Version History[](https://nextjs.org/docs/app/api-reference/directives/use-cache#version-history)

Version| Changes  
---|---  
`v16.0.0`| `"use cache"` is enabled with the Cache Components feature.  
`v15.0.0`| `"use cache"` is introduced as an experimental feature.  
  
## Related

View related API references.

### [use cache: privateLearn how to use the "use cache: private" directive to cache functions that access runtime request APIs.](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)### [cacheComponentsLearn how to enable the cacheComponents flag in Next.js.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)### [cacheLifeLearn how to set up cacheLife configurations in Next.js.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)### [cacheHandlersConfigure custom cache handlers for use cache directives in Next.js.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)### [cacheTagLearn how to use the cacheTag function to manage cache invalidation in your Next.js application.](https://nextjs.org/docs/app/api-reference/functions/cacheTag)### [cacheLifeLearn how to use the cacheLife function to set the cache expiration time for a cached function or component.](https://nextjs.org/docs/app/api-reference/functions/cacheLife)### [revalidateTagAPI Reference for the revalidateTag function.](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)

Was this helpful?

supported.

Send
