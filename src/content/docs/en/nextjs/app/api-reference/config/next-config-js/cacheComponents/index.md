---
title: 'next.config.js: cacheComponents'
description: 'Last updated February 20, 2026'
---

# next.config.js: cacheComponents | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)cacheComponents

Copy page

# cacheComponents

Last updated February 20, 2026

The `cacheComponents` flag is a feature in Next.js that causes data fetching operations in the App Router to be excluded from pre-renders unless they are explicitly cached. This can be useful for optimizing the performance of dynamic data fetching in Server Components.

It is useful if your application requires fresh data fetching during runtime rather than serving from a pre-rendered cache.

It is expected to be used in conjunction with [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) so that your data fetching happens at runtime by default unless you define specific parts of your application to be cached with `use cache` at the page, function, or component level.

## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents#usage)

To enable the `cacheComponents` flag, set it to `true` in your `next.config.ts` file:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      cacheComponents: true,
    }
     
    export default nextConfig
[/code]

When `cacheComponents` is enabled, you can use the following cache functions and configurations:

  * The [`use cache` directive](https://nextjs.org/docs/app/api-reference/directives/use-cache)
  * The [`cacheLife` function](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife) with `use cache`
  * The [`cacheTag` function](https://nextjs.org/docs/app/api-reference/functions/cacheTag)



## Notes[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents#notes)

  * While `cacheComponents` can optimize performance by ensuring fresh data fetching during runtime, it may also introduce additional latency compared to serving pre-rendered content.



## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents#version-history)

Version| Change  
---|---  
16.0.0| `cacheComponents` introduced. This flag controls the `ppr`, `useCache`, and `dynamicIO` flags as a single, unified configuration.  
  
Was this helpful?

supported.

Send
