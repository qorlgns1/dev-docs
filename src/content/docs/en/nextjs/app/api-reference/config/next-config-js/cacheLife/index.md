---
title: 'next.config.js: cacheLife'
description: 'Last updated February 20, 2026'
---

# next.config.js: cacheLife | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)cacheLife

Copy page

# cacheLife

Last updated February 20, 2026

The `cacheLife` option allows you to define **custom cache profiles** when using the [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) function inside components or functions, and within the scope of the [`use cache` directive](https://nextjs.org/docs/app/api-reference/directives/use-cache).

## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife#usage)

To define a profile, enable the [`cacheComponents` flag](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) and add the cache profile in the `cacheLife` object in the `next.config.js` file. For example, a `blog` profile:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      cacheComponents: true,
      cacheLife: {
        blog: {
          stale: 3600, // 1 hour
          revalidate: 900, // 15 minutes
          expire: 86400, // 1 day
        },
      },
    }
     
    export default nextConfig
[/code]

You can now use this custom `blog` configuration in your component or function as follows:

app/actions.ts

JavaScriptTypeScript
[code]
    import { cacheLife } from 'next/cache'
     
    export async function getCachedData() {
      'use cache'
      cacheLife('blog')
      const data = await fetch('/api/data')
      return data
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife#reference)

The configuration object has key values with the following format:

**Property**| **Value**| **Description**| **Requirement**  
---|---|---|---  
`stale`| `number`| Duration the client should cache a value without checking the server.| Optional  
`revalidate`| `number`| Frequency at which the cache should refresh on the server; stale values may be served while revalidating.| Optional  
`expire`| `number`| Maximum duration for which a value can remain stale before switching to dynamic.| Optional - Must be longer than `revalidate`  
  
## Related

View related API references.

### [use cacheLearn how to use the "use cache" directive to cache data in your Next.js application.](https://nextjs.org/docs/app/api-reference/directives/use-cache)### [cacheHandlersConfigure custom cache handlers for use cache directives in Next.js.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)### [cacheLifeLearn how to use the cacheLife function to set the cache expiration time for a cached function or component.](https://nextjs.org/docs/app/api-reference/functions/cacheLife)

Was this helpful?

supported.

Send
