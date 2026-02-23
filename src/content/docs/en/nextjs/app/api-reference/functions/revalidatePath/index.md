---
title: 'Functions: revalidatePath'
description: 'allows you to invalidate cached data on-demand for a specific path.'
---

# Functions: revalidatePath | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/revalidatePath

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)revalidatePath

Copy page

# revalidatePath

Last updated February 20, 2026

`revalidatePath` allows you to invalidate [cached data](https://nextjs.org/docs/app/guides/caching) on-demand for a specific path.

## Usage[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#usage)

`revalidatePath` can be called in Server Functions and Route Handlers.

`revalidatePath` cannot be called in Client Components or Proxy, as it only works in server environments.

> **Good to know** :
> 
>   * **Server Functions** : Updates the UI immediately (if viewing the affected path). Currently, it also causes all previously visited pages to refresh when navigated to again. This behavior is temporary and will be updated in the future to apply only to the specific path.
>   * **Route Handlers** : Marks the path for revalidation. The revalidation is done on the next visit to the specified path. This means calling `revalidatePath` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.
> 


## Parameters[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#parameters)
[code] 
    revalidatePath(path: string, type?: 'page' | 'layout'): void;
[/code]

  * `path`: Either a route pattern corresponding to the data you want to revalidate, for example `/product/[slug]`, or a specific URL, `/product/123`. Do not append `/page` or `/layout`, use the `type` parameter instead. Must not exceed 1024 characters. This value is case-sensitive.
  * `type`: (optional) `'page'` or `'layout'` string to change the type of path to revalidate. If `path` contains a dynamic segment, for example `/product/[slug]`, this parameter is required. If `path` is a specific URL, `/product/1`, omit `type`.



Use a specific URL when you want to refresh a [single page](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-specific-url). Use a route pattern plus `type` to refresh [multiple URLs](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-page-path).

## Returns[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#returns)

`revalidatePath` does not return a value.

## What can be invalidated[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#what-can-be-invalidated)

The path parameter can point to pages, layouts, or route handlers:

  * **Pages** : Invalidates the specific page
  * **Layouts** : Invalidates the layout (the `layout.tsx` at that segment), all nested layouts beneath it, and all pages beneath them
  * **Route Handlers** : Invalidates Data Cache entries accessed within route handlers. For example `revalidatePath("/api/data")` invalidates this GET handler:



app/api/data/route.ts
[code]
    export async function GET() {
      const data = await fetch('https://api.vercel.app/blog', {
        cache: 'force-cache',
      })
     
      return Response.json(await data.json())
    }
[/code]

## Relationship with `revalidateTag` and `updateTag`[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#relationship-with-revalidatetag-and-updatetag)

`revalidatePath`, [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) and [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) serve different purposes:

  * **`revalidatePath`** : Invalidates a specific page or layout path
  * **`revalidateTag`** : Marks data with specific tags as **stale**. Applies across all pages that use those tags
  * **`updateTag`** : Expires data with specific tags. Applies across all pages that use those tags



When you call `revalidatePath`, only the specified path gets fresh data on the next visit. Other pages that use the same data tags will continue to serve cached data until those specific tags are also revalidated:
[code] 
    // Page A: /blog
    const posts = await fetch('https://api.vercel.app/blog', {
      next: { tags: ['posts'] },
    })
     
    // Page B: /dashboard
    const recentPosts = await fetch('https://api.vercel.app/blog?limit=5', {
      next: { tags: ['posts'] },
    })
[/code]

After calling `revalidatePath('/blog')`:

  * **Page A (/blog)** : Shows fresh data (page re-rendered)
  * **Page B (/dashboard)** : Still shows stale data (cache tag 'posts' not invalidated)



Learn about the difference between [`revalidateTag` and `updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag#differences-from-revalidatetag).

### Building revalidation utilities[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#building-revalidation-utilities)

`revalidatePath` and `updateTag` are complementary primitives that are often used together in utility functions to ensure comprehensive data consistency across your application:
[code] 
    'use server'
     
    import { revalidatePath, updateTag } from 'next/cache'
     
    export async function updatePost() {
      await updatePostInDatabase()
     
      revalidatePath('/blog') // Refresh the blog page
      updateTag('posts') // Refresh all pages using 'posts' tag
    }
[/code]

This pattern ensures that both the specific page and any other pages using the same data remain consistent.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#examples)

### Revalidating a specific URL[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-specific-url)
[code] 
    import { revalidatePath } from 'next/cache'
    revalidatePath('/blog/post-1')
[/code]

This will invalidate one specific URL for revalidation on the next page visit.

### Revalidating a Page path[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-page-path)
[code] 
    import { revalidatePath } from 'next/cache'
    revalidatePath('/blog/[slug]', 'page')
    // or with route groups
    revalidatePath('/(main)/blog/[slug]', 'page')
[/code]

This will invalidate any URL that matches the provided `page` file for revalidation on the next page visit. This will _not_ invalidate pages beneath the specific page. For example, `/blog/[slug]` won't invalidate `/blog/[slug]/[author]`.

### Revalidating a Layout path[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-layout-path)
[code] 
    import { revalidatePath } from 'next/cache'
    revalidatePath('/blog/[slug]', 'layout')
    // or with route groups
    revalidatePath('/(main)/post/[slug]', 'layout')
[/code]

This will invalidate any URL that matches the provided `layout` file for revalidation on the next page visit. This will cause pages beneath with the same layout to be invalidated and revalidated on the next visit. For example, in the above case, `/blog/[slug]/[another]` would also be invalidated and revalidated on the next visit.

### Revalidating all data[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-all-data)
[code] 
    import { revalidatePath } from 'next/cache'
     
    revalidatePath('/', 'layout')
[/code]

This will purge the Client-side Router Cache, and invalidate the Data Cache for revalidation on the next page visit.

### Server Function[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#server-function)

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { revalidatePath } from 'next/cache'
     
    export default async function submit() {
      await submitForm()
      revalidatePath('/')
    }
[/code]

### Route Handler[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#route-handler)

app/api/revalidate/route.ts

JavaScriptTypeScript
[code]
    import { revalidatePath } from 'next/cache'
    import type { NextRequest } from 'next/server'
     
    export async function GET(request: NextRequest) {
      const path = request.nextUrl.searchParams.get('path')
     
      if (path) {
        revalidatePath(path)
        return Response.json({ revalidated: true, now: Date.now() })
      }
     
      return Response.json({
        revalidated: false,
        now: Date.now(),
        message: 'Missing path to revalidate',
      })
    }
[/code]

Was this helpful?

supported.

Send
