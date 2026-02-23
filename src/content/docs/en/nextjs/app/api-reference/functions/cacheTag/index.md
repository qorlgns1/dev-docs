---
title: 'Functions: cacheTag'
description: 'The  function allows you to tag cached data for on-demand invalidation. By associating tags with cache entries, you can selectively purge or revalidat...'
---

# Functions: cacheTag | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/cacheTag

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)cacheTag

Copy page

# cacheTag

Last updated February 20, 2026

The `cacheTag` function allows you to tag cached data for on-demand invalidation. By associating tags with cache entries, you can selectively purge or revalidate specific cache entries without affecting other cached data.

## Usage[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#usage)

To use `cacheTag`, enable the [`cacheComponents` flag](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) in your `next.config.js` file:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      cacheComponents: true,
    }
     
    export default nextConfig
[/code]

The `cacheTag` function takes one or more string values.

app/data.ts

JavaScriptTypeScript
[code]
    import { cacheTag } from 'next/cache'
     
    export async function getData() {
      'use cache'
      cacheTag('my-data')
      const data = await fetch('/api/data')
      return data
    }
[/code]

You can then purge the cache on-demand using [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) API in another function, for example, a [route handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) or [Server Action](https://nextjs.org/docs/app/getting-started/updating-data):

app/action.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { revalidateTag } from 'next/cache'
     
    export default async function submit() {
      await addPost()
      revalidateTag('my-data')
    }
[/code]

## Good to know[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#good-to-know)

  * **Idempotent Tags** : Applying the same tag multiple times has no additional effect.
  * **Multiple Tags** : You can assign multiple tags to a single cache entry by passing multiple string values to `cacheTag`.


[code] 
    cacheTag('tag-one', 'tag-two')
[/code]

  * **Limits** : The max length for a custom tag is 256 characters and the max tag items is 128.



## Examples[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#examples)

### Tagging components or functions[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#tagging-components-or-functions)

Tag your cached data by calling `cacheTag` within a cached function or component:

app/components/bookings.tsx

JavaScriptTypeScript
[code]
    import { cacheTag } from 'next/cache'
     
    interface BookingsProps {
      type: string
    }
     
    export async function Bookings({ type = 'haircut' }: BookingsProps) {
      'use cache'
      cacheTag('bookings-data')
     
      async function getBookingsData() {
        const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
        return data
      }
     
      return //...
    }
[/code]

### Creating tags from external data[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#creating-tags-from-external-data)

You can use the data returned from an async function to tag the cache entry.

app/components/bookings.tsx

JavaScriptTypeScript
[code]
    import { cacheTag } from 'next/cache'
     
    interface BookingsProps {
      type: string
    }
     
    export async function Bookings({ type = 'haircut' }: BookingsProps) {
      async function getBookingsData() {
        'use cache'
        const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
        cacheTag('bookings-data', data.id)
        return data
      }
      return //...
    }
[/code]

### Invalidating tagged cache[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#invalidating-tagged-cache)

Using [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag), you can invalidate the cache for a specific tag when needed:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { revalidateTag } from 'next/cache'
     
    export async function updateBookings() {
      await updateBookingData()
      revalidateTag('bookings-data')
    }
[/code]

## Related

View related API references.

### [cacheComponentsLearn how to enable the cacheComponents flag in Next.js.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)### [use cacheLearn how to use the "use cache" directive to cache data in your Next.js application.](https://nextjs.org/docs/app/api-reference/directives/use-cache)### [revalidateTagAPI Reference for the revalidateTag function.](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)### [cacheLifeLearn how to use the cacheLife function to set the cache expiration time for a cached function or component.](https://nextjs.org/docs/app/api-reference/functions/cacheLife)

Was this helpful?

supported.

Send
