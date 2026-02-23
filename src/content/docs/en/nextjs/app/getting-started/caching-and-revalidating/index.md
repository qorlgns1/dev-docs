---
title: 'Getting Started: Caching and Revalidating'
description: 'Caching is a technique for storing the result of data fetching and other computations so that future requests for the same data can be served faster,...'
---

# Getting Started: Caching and Revalidating | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/caching-and-revalidating

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Caching and Revalidating

Copy page

# Caching and Revalidating

Last updated February 20, 2026

Caching is a technique for storing the result of data fetching and other computations so that future requests for the same data can be served faster, without doing the work again. While revalidation allows you to update cache entries without having to rebuild your entire application.

Next.js provides a few APIs to handle caching and revalidation. This guide will walk you through when and how to use them.

  * [`fetch`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch)
  * [`cacheTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag)
  * [`revalidateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag)
  * [`updateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag)
  * [`revalidatePath`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatepath)
  * [`unstable_cache`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#unstable_cache) (Legacy)



## `fetch`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch)

By default, [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch) requests are not cached. You can cache individual requests by setting the `cache` option to `'force-cache'`.

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const data = await fetch('https://...', { cache: 'force-cache' })
    }
[/code]

> **Good to know** : Although `fetch` requests are not cached by default, Next.js will [pre-render](https://nextjs.org/docs/app/guides/caching#static-rendering) routes that have `fetch` requests and cache the HTML. If you want to guarantee a route is [dynamic](https://nextjs.org/docs/app/guides/caching#dynamic-rendering), use the [`connection` API](https://nextjs.org/docs/app/api-reference/functions/connection).

To revalidate the data returned by a `fetch` request, you can use the `next.revalidate` option.

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const data = await fetch('https://...', { next: { revalidate: 3600 } })
    }
[/code]

This will revalidate the data after a specified amount of seconds.

You can also tag `fetch` requests to enable on-demand cache invalidation:

app/lib/data.ts

JavaScriptTypeScript
[code]
    export async function getUserById(id: string) {
      const data = await fetch(`https://...`, {
        next: {
          tags: ['user'],
        },
      })
    }
[/code]

See the [`fetch` API reference](https://nextjs.org/docs/app/api-reference/functions/fetch) to learn more.

## `cacheTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag)

[`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) allows you to tag cached data in [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) so it can be revalidated on-demand. Previously, cache tagging was limited to `fetch` requests, and caching other work required the experimental `unstable_cache` API.

With Cache Components, you can use the [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) directive to cache any computation, and `cacheTag` to tag it. This works with database queries, file system operations, and other server-side work.

app/lib/data.ts

JavaScriptTypeScript
[code]
    import { cacheTag } from 'next/cache'
     
    export async function getProducts() {
      'use cache'
      cacheTag('products')
     
      const products = await db.query('SELECT * FROM products')
      return products
    }
[/code]

Once tagged, you can use [`revalidateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag) or [`updateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag) to invalidate the cache entry for products.

> **Good to know** : `cacheTag` is used with [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) and the [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) directive. It expands the caching and revalidation story beyond `fetch`.

See the [`cacheTag` API reference](https://nextjs.org/docs/app/api-reference/functions/cacheTag) to learn more.

## `revalidateTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag)

`revalidateTag` is used to revalidate cache entries based on a tag and following an event. The function now supports two behaviors:

  * **With`profile="max"`**: Uses stale-while-revalidate semantics, serving stale content while fetching fresh content in the background
  * **Without the second argument** : Legacy behavior that immediately expires the cache (deprecated)



After tagging your cached data, using [`fetch`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch) with `next.tags`, or the [`cacheTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag) function, you may call `revalidateTag` in a [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) or Server Action:

app/lib/actions.ts

JavaScriptTypeScript
[code]
    import { revalidateTag } from 'next/cache'
     
    export async function updateUser(id: string) {
      // Mutate data
      revalidateTag('user', 'max') // Recommended: Uses stale-while-revalidate
    }
[/code]

You can reuse the same tag in multiple functions to revalidate them all at once.

See the [`revalidateTag` API reference](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) to learn more.

## `updateTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag)

`updateTag` is specifically designed for Server Actions to immediately expire cached data for read-your-own-writes scenarios. Unlike `revalidateTag`, it can only be used within Server Actions and immediately expires the cache entry.

app/lib/actions.ts

JavaScriptTypeScript
[code]
    import { updateTag } from 'next/cache'
    import { redirect } from 'next/navigation'
     
    export async function createPost(formData: FormData) {
      // Create post in database
      const post = await db.post.create({
        data: {
          title: formData.get('title'),
          content: formData.get('content'),
        },
      })
     
      // Immediately expire cache so the new post is visible
      updateTag('posts')
      updateTag(`post-${post.id}`)
     
      redirect(`/posts/${post.id}`)
    }
[/code]

The key differences between `revalidateTag` and `updateTag`:

  * **`updateTag`** : Only in Server Actions, immediately expires cache, for read-your-own-writes
  * **`revalidateTag`** : In Server Actions and Route Handlers, supports stale-while-revalidate with `profile="max"`



See the [`updateTag` API reference](https://nextjs.org/docs/app/api-reference/functions/updateTag) to learn more.

## `revalidatePath`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatepath)

`revalidatePath` is used to revalidate a route and following an event. To use it, call it in a [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) or Server Action:

app/lib/actions.ts

JavaScriptTypeScript
[code]
    import { revalidatePath } from 'next/cache'
     
    export async function updateUser(id: string) {
      // Mutate data
      revalidatePath('/profile')
[/code]

See the [`revalidatePath` API reference](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) to learn more.

## `unstable_cache`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#unstable_cache)

> **Good to know** : `unstable_cache` is an experimental API. We recommend opting into [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) and replacing `unstable_cache` with the [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) directive. See the [Cache Components documentation](https://nextjs.org/docs/app/getting-started/cache-components) for more details.

`unstable_cache` allows you to cache the result of database queries and other async functions. To use it, wrap `unstable_cache` around the function. For example:

app/lib/data.ts

JavaScriptTypeScript
[code]
    import { db } from '@/lib/db'
    export async function getUserById(id: string) {
      return db
        .select()
        .from(users)
        .where(eq(users.id, id))
        .then((res) => res[0])
    }
[/code]

app/page.tsx

JavaScriptTypeScript
[code]
    import { unstable_cache } from 'next/cache'
    import { getUserById } from '@/app/lib/data'
     
    export default async function Page({
      params,
    }: {
      params: Promise<{ userId: string }>
    }) {
      const { userId } = await params
     
      const getCachedUser = unstable_cache(
        async () => {
          return getUserById(userId)
        },
        [userId] // add the user ID to the cache key
      )
    }
[/code]

The function accepts a third optional object to define how the cache should be revalidated. It accepts:

  * `tags`: an array of tags used by Next.js to revalidate the cache.
  * `revalidate`: the number of seconds after cache should be revalidated.



app/page.tsx

JavaScriptTypeScript
[code]
    const getCachedUser = unstable_cache(
      async () => {
        return getUserById(userId)
      },
      [userId],
      {
        tags: ['user'],
        revalidate: 3600,
      }
    )
[/code]

See the [`unstable_cache` API reference](https://nextjs.org/docs/app/api-reference/functions/unstable_cache) to learn more.

## API Reference

Learn more about the features mentioned in this page by reading the API Reference.

### [fetchAPI reference for the extended fetch function.](https://nextjs.org/docs/app/api-reference/functions/fetch)### [cacheTagLearn how to use the cacheTag function to manage cache invalidation in your Next.js application.](https://nextjs.org/docs/app/api-reference/functions/cacheTag)### [revalidateTagAPI Reference for the revalidateTag function.](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)### [updateTagAPI Reference for the updateTag function.](https://nextjs.org/docs/app/api-reference/functions/updateTag)### [revalidatePathAPI Reference for the revalidatePath function.](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)### [unstable_cacheAPI Reference for the unstable_cache function.](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)

Was this helpful?

supported.

Send
