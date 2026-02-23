---
title: 'Functions: revalidateTag'
description: 'Last updated February 20, 2026'
---

# Functions: revalidateTag | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/revalidateTag

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)revalidateTag

Copy page

# revalidateTag

Last updated February 20, 2026

`revalidateTag` allows you to invalidate [cached data](https://nextjs.org/docs/app/guides/caching) on-demand for a specific cache tag.

This function is ideal for content where a slight delay in updates is acceptable, such as blog posts, product catalogs, or documentation. Users receive stale content while fresh data loads in the background.

## Usage[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#usage)

`revalidateTag` can be called in Server Functions and Route Handlers.

`revalidateTag` cannot be called in Client Components or Proxy, as it only works in server environments.

### Revalidation Behavior[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#revalidation-behavior)

The revalidation behavior depends on whether you provide the second argument:

  * **With`profile="max"` (recommended)**: The tag entry is marked as stale, and the next time a resource with that tag is visited, it will use stale-while-revalidate semantics. This means the stale content is served while fresh content is fetched in the background.
  * **With a custom cache life profile** : For advanced usage, you can specify any cache life profile that your application has defined, allowing for custom revalidation behaviors tailored to your specific caching requirements.
  * **Without the second argument (deprecated)** : The tag entry is expired immediately, and the next request to that resource will be a blocking revalidate/cache miss. This behavior is now deprecated, and you should either use `profile="max"` or migrate to [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag).



> **Good to know** : When using `profile="max"`, `revalidateTag` marks tagged data as stale, but fresh data is only fetched when pages using that tag are next visited. This means calling `revalidateTag` will not immediately trigger many revalidations at once. The invalidation only happens when any page using that tag is next visited.

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#parameters)
[code] 
    revalidateTag(tag: string, profile: string | { expire?: number }): void;
[/code]

  * `tag`: A string representing the cache tag associated with the data you want to revalidate. Must not exceed 256 characters. This value is case-sensitive.
  * `profile`: A string that specifies the revalidation behavior. The recommended value is `"max"` which provides stale-while-revalidate semantics, or any of the other default or custom profiles defined in [`cacheLife`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife). Alternatively, you can pass an object with an `expire` property for custom expiration behavior.



Tags must first be assigned to cached data. You can do this in two ways:

  * Using the [`next.tags`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag) option with `fetch` for caching external API requests:


[code] 
    fetch(url, { next: { tags: ['posts'] } })
[/code]

  * Using [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) inside cached functions or components with the `'use cache'` directive:


[code] 
    import { cacheTag } from 'next/cache'
     
    async function getData() {
      'use cache'
      cacheTag('posts')
      // ...
    }
[/code]

> **Good to know** : The single-argument form `revalidateTag(tag)` is deprecated. It currently works if TypeScript errors are suppressed, but this behavior may be removed in a future version. Update to the two-argument signature.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#returns)

`revalidateTag` does not return a value.

## Relationship with `revalidatePath`[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#relationship-with-revalidatepath)

`revalidateTag` invalidates data with specific tags across all pages that use those tags, while [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) invalidates specific page or layout paths.

> **Good to know** : These functions serve different purposes and may need to be used together for comprehensive data consistency. For detailed examples and considerations, see [relationship with revalidateTag and updateTag](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#relationship-with-revalidatetag-and-updatetag) for more information.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#examples)

The following examples demonstrate how to use `revalidateTag` in different contexts. In both cases, we're using `profile="max"` to mark data as stale and use stale-while-revalidate semantics, which is the recommended approach for most use cases.

### Server Action[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#server-action)

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { revalidateTag } from 'next/cache'
     
    export default async function submit() {
      await addPost()
      revalidateTag('posts', 'max')
    }
[/code]

### Route Handler[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#route-handler)

app/api/revalidate/route.ts

JavaScriptTypeScript
[code]
    import type { NextRequest } from 'next/server'
    import { revalidateTag } from 'next/cache'
     
    export async function GET(request: NextRequest) {
      const tag = request.nextUrl.searchParams.get('tag')
     
      if (tag) {
        revalidateTag(tag, 'max')
        return Response.json({ revalidated: true, now: Date.now() })
      }
     
      return Response.json({
        revalidated: false,
        now: Date.now(),
        message: 'Missing tag to revalidate',
      })
    }
[/code]

> **Good to know** : For webhooks or third-party services that need immediate expiration, you can pass `{ expire: 0 }` as the second argument: `revalidateTag(tag, { expire: 0 })`. This pattern is necessary when external systems call your Route Handlers and require data to expire immediately. For all other cases, it's recommended to use [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) in Server Actions for immediate updates instead.

Was this helpful?

supported.

Send
