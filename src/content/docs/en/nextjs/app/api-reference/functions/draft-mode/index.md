---
title: 'Functions: draftMode'
description: 'is an async function allows you to enable and disable Draft Mode, as well as check if Draft Mode is enabled in a Server Component.'
---

# Functions: draftMode | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/draft-mode

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)draftMode

Copy page

# draftMode

Last updated February 20, 2026

`draftMode` is an **async** function allows you to enable and disable [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode), as well as check if Draft Mode is enabled in a [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components).

app/page.ts

JavaScriptTypeScript
[code]
    import { draftMode } from 'next/headers'
     
    export default async function Page() {
      const { isEnabled } = await draftMode()
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#reference)

The following methods and properties are available:

Method| Description  
---|---  
`isEnabled`| A boolean value that indicates if Draft Mode is enabled.  
`enable()`| Enables Draft Mode in a Route Handler by setting a cookie (`__prerender_bypass`).  
`disable()`| Disables Draft Mode in a Route Handler by deleting a cookie.  
  
## Good to know[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#good-to-know)

  * `draftMode` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function.
    * In version 14 and earlier, `draftMode` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * A new bypass cookie value will be generated each time you run `next build`. This ensures that the bypass cookie can’t be guessed.
  * To test Draft Mode locally over HTTP, your browser will need to allow third-party cookies and local storage access.



## Examples[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#examples)

### Enabling Draft Mode[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#enabling-draft-mode)

To enable Draft Mode, create a new [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) and call the `enable()` method:

app/draft/route.ts

JavaScriptTypeScript
[code]
    import { draftMode } from 'next/headers'
     
    export async function GET(request: Request) {
      const draft = await draftMode()
      draft.enable()
      return new Response('Draft mode is enabled')
    }
[/code]

### Disabling Draft Mode[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#disabling-draft-mode)

By default, the Draft Mode session ends when the browser is closed.

To disable Draft Mode manually, call the `disable()` method in your [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route):

app/draft/route.ts

JavaScriptTypeScript
[code]
    import { draftMode } from 'next/headers'
     
    export async function GET(request: Request) {
      const draft = await draftMode()
      draft.disable()
      return new Response('Draft mode is disabled')
    }
[/code]

Then, send a request to invoke the Route Handler. If calling the route using the [`<Link>` component](https://nextjs.org/docs/app/api-reference/components/link), you must pass `prefetch={false}` to prevent accidentally deleting the cookie on prefetch.

### Checking if Draft Mode is enabled[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#checking-if-draft-mode-is-enabled)

You can check if Draft Mode is enabled in a Server Component with the `isEnabled` property:

app/page.ts

JavaScriptTypeScript
[code]
    import { draftMode } from 'next/headers'
     
    export default async function Page() {
      const { isEnabled } = await draftMode()
      return (
        <main>
          <h1>My Blog Post</h1>
          <p>Draft Mode is currently {isEnabled ? 'Enabled' : 'Disabled'}</p>
        </main>
      )
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#version-history)

Version| Changes  
---|---  
`v15.0.0-RC`| `draftMode` is now an async function. A [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150) is available.  
`v13.4.0`| `draftMode` introduced.  
  
## Next Steps

Learn how to use Draft Mode with this step-by-step guide.

### [Draft ModeNext.js has draft mode to toggle between static and dynamic pages. You can learn how it works with App Router here.](https://nextjs.org/docs/app/guides/draft-mode)

Was this helpful?

supported.

Send
