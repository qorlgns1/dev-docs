---
title: 'Functions: refresh'
description: 'allows you to refresh the client router from within a Server Action.'
---

# Functions: refresh | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/refresh

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)refresh

Copy page

# refresh

Last updated February 20, 2026

`refresh` allows you to refresh the client router from within a [Server Action](https://nextjs.org/docs/app/getting-started/updating-data).

## Usage[](https://nextjs.org/docs/app/api-reference/functions/refresh#usage)

`refresh` can **only** be called from within Server Actions. It cannot be used in Route Handlers, Client Components, or any other context.

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/refresh#parameters)
[code] 
    refresh(): void;
[/code]

## Returns[](https://nextjs.org/docs/app/api-reference/functions/refresh#returns)

`refresh` does not return a value.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/refresh#examples)

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { refresh } from 'next/cache'
     
    export async function createPost(formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')
     
      // Create the post in your database
      const post = await db.post.create({
        data: { title, content },
      })
     
      refresh()
    }
[/code]

### Error when used outside Server Actions[](https://nextjs.org/docs/app/api-reference/functions/refresh#error-when-used-outside-server-actions)

app/api/posts/route.ts

JavaScriptTypeScript
[code]
    import { refresh } from 'next/cache'
     
    export async function POST() {
      // This will throw an error
      refresh()
    }
[/code]

Was this helpful?

supported.

Send
