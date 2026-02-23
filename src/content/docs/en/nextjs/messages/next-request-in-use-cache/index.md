---
title: 'Cannot access cookies() or headers() in "use cache"'
description: 'A function is trying to read from the current incoming request inside the scope of a function annotated with . This is not supported because it would...'
---

# Cannot access `cookies()` or `headers()` in `"use cache"` | Next.js

Source URL: https://nextjs.org/docs/messages/next-request-in-use-cache

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Cannot access `cookies()` or `headers()` in `"use cache"`

# Cannot access `cookies()` or `headers()` in `"use cache"`

## Why This Error Occurred[](https://nextjs.org/docs/messages/next-request-in-use-cache#why-this-error-occurred)

A function is trying to read from the current incoming request inside the scope of a function annotated with `"use cache"`. This is not supported because it would make the cache invalidated by every request which is probably not what you intended.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/next-request-in-use-cache#possible-ways-to-fix-it)

Instead of calling this inside the `"use cache"` function, move it outside the function and pass the value in as an argument. The specific value will now be part of the cache key through its arguments.

Before:

app/page.js
[code]
    import { cookies } from 'next/headers'
     
    async function getExampleData() {
      "use cache"
      const isLoggedIn = (await cookies()).has('token')
      ...
    }
     
    export default async function Page() {
      const data = await getExampleData()
      return ...
    }
[/code]

After:

app/page.js
[code]
    import { cookies } from 'next/headers'
     
    async function getExampleData(isLoggedIn) {
      "use cache"
      ...
    }
     
    export default async function Page() {
      const isLoggedIn = (await cookies()).has('token')
      const data = await getExampleData(isLoggedIn)
      return ...
    }
[/code]

## Useful Links[](https://nextjs.org/docs/messages/next-request-in-use-cache#useful-links)

  * [`headers()` function](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`cookies()` function](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`draftMode()` function](https://nextjs.org/docs/app/api-reference/functions/draft-mode)



Was this helpful?

supported.

Send
