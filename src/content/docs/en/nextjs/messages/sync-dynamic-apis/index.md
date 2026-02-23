---
title: 'Dynamic APIs are Asynchronous'
description: 'Learn more about why accessing certain APIs synchronously now warns.'
---

# Dynamic APIs are Asynchronous | Next.js

Source URL: https://nextjs.org/docs/messages/sync-dynamic-apis

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Dynamic APIs are Asynchronous

# Dynamic APIs are Asynchronous

Learn more about why accessing certain APIs synchronously now warns.

## Why This Warning Occurred[](https://nextjs.org/docs/messages/sync-dynamic-apis#why-this-warning-occurred)

Somewhere in your code you used an API that opts into [dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering).

Dynamic APIs are:

  * The `params` and `searchParams` props that get provided to pages, layouts, metadata APIs, and route handlers.
  * `cookies()`, `draftMode()`, and `headers()` from `next/headers`



In Next 15, these APIs have been made asynchronous. You can read more about this in the Next.js 15 [Upgrade Guide](https://nextjs.org/docs/app/guides/upgrading/version-15).

For example, the following code will issue a warning:

app/[id]/page.js
[code]
    function Page({ params }) {
      // direct access of `params.id`.
      return <p>ID: {params.id}</p>
    }
[/code]

This also includes enumerating (e.g. `{...params}`, or `Object.keys(params)`) or iterating over the return value of these APIs (e.g. `[...headers()]` or `for (const cookie of cookies())`, or explicitly with `cookies()[Symbol.iterator]()`).

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/sync-dynamic-apis#possible-ways-to-fix-it)

The [`next-async-request-api` codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#next-async-request-api) can fix many of these cases automatically:

Terminal
[code]
    npx @next/codemod@canary next-async-request-api .
[/code]

The codemod cannot cover all cases, so you may need to manually adjust some code.

If the warning occurred on the Server (e.g. a route handler, or a Server Component), you must `await` the dynamic API to access its properties:

app/[id]/page.js
[code]
    async function Page({ params }) {
      // asynchronous access of `params.id`.
      const { id } = await params
      return <p>ID: {id}</p>
    }
[/code]

If the warning occurred in a synchronous component (e.g. a Client component), you must use `React.use()` to unwrap the Promise first:

app/[id]/page.js
[code]
    'use client'
    import * as React from 'react'
     
    function Page({ params }) {
      // asynchronous access of `params.id`.
      const { id } = React.use(params)
      return <p>ID: {id}</p>
    }
[/code]

### Unmigratable Cases[](https://nextjs.org/docs/messages/sync-dynamic-apis#unmigratable-cases)

If Next.js codemod found anything that is not able to be migrated by the codemod, it will leave a comment with `@next-codemod-error` prefix and the suggested action, for example: In this case, you need to manually await the call to `cookies()`, and change the function to async. Then refactor the usages of the function to be properly awaited:
[code] 
    export function MyCookiesComponent() {
      const c =
        /* @next-codemod-error Manually await this call and refactor the function to be async */
        cookies()
      return c.get('name')
    }
[/code]

### Enforced Migration with Linter[](https://nextjs.org/docs/messages/sync-dynamic-apis#enforced-migration-with-linter)

If you didn't address the comments that starting with `@next-codemod-error` left by the codemod, Next.js will error in both dev and build to enforce you to address the issues. You can review the changes and follow the suggestion in the comments. You can either make the necessary changes and remove the comment, or replace the comment prefix `@next-codemod-error` with `@next-codemod-ignore` If there's no action to be taken, the comment prefix `@next-codemod-ignore` will bypass the build error.
[code] 
    - /* @next-codemod-error <suggested message> */
    + /* @next-codemod-ignore */
[/code]

> **Good to know** :
> 
> You can delay unwrapping the Promise (either with `await` or `React.use`) until you actually need to consume the value. This will allow Next.js to statically render more of your page.

Was this helpful?

supported.

Send
