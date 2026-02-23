---
title: 'next.config.js: cacheHandler'
description: 'Last updated February 20, 2026'
---

# next.config.js: cacheHandler | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)cacheHandler

Copy page

# Custom Next.js Cache Handler

Last updated February 20, 2026

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.

> **Good to know** : The `cacheHandler` (singular) configuration is specifically used by Next.js for server cache operations such as storing and revalidating ISR and route handler responses. It is **not** used by `'use cache'` directives. For `'use cache'` directives, use [`cacheHandlers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers) (plural) instead.

next.config.js
[code]
    module.exports = {
      cacheHandler: require.resolve('./cache-handler.js'),
      cacheMaxMemorySize: 0, // disable default in-memory caching
    }
[/code]

View an example of a [custom cache handler](https://nextjs.org/docs/app/guides/self-hosting#configuring-caching) and learn more about the implementation.

## API Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#api-reference)

The cache handler can implement the following methods: `get`, `set`, `revalidateTag`, and `resetRequestCache`.

### `get()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#get)

Parameter| Type| Description  
---|---|---  
`key`| `string`| The key to the cached value.  
  
Returns the cached value or `null` if not found.

### `set()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#set)

Parameter| Type| Description  
---|---|---  
`key`| `string`| The key to store the data under.  
`data`| Data or `null`| The data to be cached.  
`ctx`| `{ tags: [] }`| The cache tags provided.  
  
Returns `Promise<void>`.

### `revalidateTag()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#revalidatetag)

Parameter| Type| Description  
---|---|---  
`tag`| `string` or `string[]`| The cache tags to revalidate.  
  
Returns `Promise<void>`. Learn more about [revalidating data](https://nextjs.org/docs/app/guides/incremental-static-regeneration) or the [`revalidateTag()`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) function.

### `resetRequestCache()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#resetrequestcache)

This method resets the temporary in-memory cache for a single request before the next request.

Returns `void`.

**Good to know:**

  * `revalidatePath` is a convenience layer on top of cache tags. Calling `revalidatePath` will call your `revalidateTag` function, which you can then choose if you want to tag cache keys based on the path.



## Platform Support[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#platform-support)

Deployment Option| Supported  
---|---  
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| Yes  
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| Yes  
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| No  
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| Platform-specific  
  
Learn how to [configure ISR](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr) when self-hosting Next.js.

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#version-history)

Version| Changes  
---|---  
`v14.1.0`| Renamed to `cacheHandler` and became stable.  
`v13.4.0`| `incrementalCacheHandlerPath` support for `revalidateTag`.  
`v13.4.0`| `incrementalCacheHandlerPath` support for standalone output.  
`v12.2.0`| Experimental `incrementalCacheHandlerPath` added.  
  
Was this helpful?

supported.

Send
