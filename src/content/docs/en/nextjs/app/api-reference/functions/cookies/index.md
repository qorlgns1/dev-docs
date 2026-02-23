---
title: 'Functions: cookies'
description: 'Last updated February 20, 2026'
---

# Functions: cookies | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/cookies

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)cookies

Copy page

# cookies

Last updated February 20, 2026

`cookies` is an **async** function that allows you to read the HTTP incoming request cookies in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), and read/write outgoing request cookies in [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route).

app/page.tsx

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'
     
    export default async function Page() {
      const cookieStore = await cookies()
      const theme = cookieStore.get('theme')
      return '...'
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/functions/cookies#reference)

### Methods[](https://nextjs.org/docs/app/api-reference/functions/cookies#methods)

The following methods are available:

Method| Return Type| Description  
---|---|---  
`get('name')`| Object| Accepts a cookie name and returns an object with the name and value.  
`getAll()`| Array of objects| Returns a list of all the cookies with a matching name.  
`has('name')`| Boolean| Accepts a cookie name and returns a boolean based on if the cookie exists.  
`set(name, value, options)`| -| Accepts a cookie name, value, and options and sets the outgoing request cookie.  
`delete(name)`| -| Accepts a cookie name and deletes the cookie.  
`toString()`| String| Returns a string representation of the cookies.  
  
### Options[](https://nextjs.org/docs/app/api-reference/functions/cookies#options)

When setting a cookie, the following properties from the `options` object are supported:

Option| Type| Description  
---|---|---  
`name`| String| Specifies the name of the cookie.  
`value`| String| Specifies the value to be stored in the cookie.  
`expires`| Date| Defines the exact date when the cookie will expire.  
`maxAge`| Number| Sets the cookie’s lifespan in seconds.  
`domain`| String| Specifies the domain where the cookie is available.  
`path`| String, default: `'/'`| Limits the cookie's scope to a specific path within the domain.  
`secure`| Boolean| Ensures the cookie is sent only over HTTPS connections for added security.  
`httpOnly`| Boolean| Restricts the cookie to HTTP requests, preventing client-side access.  
`sameSite`| Boolean, `'lax'`, `'strict'`, `'none'`| Controls the cookie's cross-site request behavior.  
`priority`| String (`"low"`, `"medium"`, `"high"`)| Specifies the cookie's priority  
`partitioned`| Boolean| Indicates whether the cookie is [partitioned](https://github.com/privacycg/CHIPS).  
  
The only option with a default value is `path`.

To learn more about these options, see the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).

## Good to know[](https://nextjs.org/docs/app/api-reference/functions/cookies#good-to-know)

  * `cookies` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access cookies.
    * In version 14 and earlier, `cookies` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * `cookies` is a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) whose returned values cannot be known ahead of time. Using it in a layout or page will opt a route into [dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering).
  * The `.delete` method can only be called:
    * In a [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route).
    * If it belongs to the same domain from which `.set` is called. For wildcard domains, the specific subdomain must be an exact match. Additionally, the code must be executed on the same protocol (HTTP or HTTPS) as the cookie you want to delete.
  * HTTP does not allow setting cookies after streaming starts, so you must use `.set` in a [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route).



## Understanding Cookie Behavior in Server Components[](https://nextjs.org/docs/app/api-reference/functions/cookies#understanding-cookie-behavior-in-server-components)

When working with cookies in Server Components, it's important to understand that cookies are fundamentally a client-side storage mechanism:

  * **Reading cookies** works in Server Components because you're accessing the cookie data that the client's browser sends to the server in the HTTP request headers.
  * **Setting cookies** is not supported during Server Component rendering. To modify cookies, invoke a Server Function from the client or use a Route Handler.



The server can only send instructions (via `Set-Cookie` headers) to tell the browser to store cookies - the actual storage happens on the client side. This is why cookie operations that modify state (`.set`, `.delete`) must be performed in a Server Function or Route Handler where the response headers can be properly set.

## Understanding Cookie Behavior in Server Functions[](https://nextjs.org/docs/app/api-reference/functions/cookies#understanding-cookie-behavior-in-server-functions)

After you set or delete a cookie in a Server Function, Next.js can return both the updated UI and new data in a single server roundtrip when the function is used as a [Server Action](https://nextjs.org/docs/app/getting-started/updating-data#what-are-server-functions) (e.g., passed to a form's `action` prop). See the [Caching guide](https://nextjs.org/docs/app/guides/caching#cookies).

The UI is not unmounted, but effects that depend on data coming from the server will re-run.

To refresh cached data too, call [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) inside the function.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/cookies#examples)

### Getting a cookie[](https://nextjs.org/docs/app/api-reference/functions/cookies#getting-a-cookie)

You can use the `(await cookies()).get('name')` method to get a single cookie:

app/page.tsx

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'
     
    export default async function Page() {
      const cookieStore = await cookies()
      const theme = cookieStore.get('theme')
      return '...'
    }
[/code]

### Getting all cookies[](https://nextjs.org/docs/app/api-reference/functions/cookies#getting-all-cookies)

You can use the `(await cookies()).getAll()` method to get all cookies with a matching name. If `name` is unspecified, it returns all the available cookies.

app/page.tsx

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'
     
    export default async function Page() {
      const cookieStore = await cookies()
      return cookieStore.getAll().map((cookie) => (
        <div key={cookie.name}>
          <p>Name: {cookie.name}</p>
          <p>Value: {cookie.value}</p>
        </div>
      ))
    }
[/code]

### Setting a cookie[](https://nextjs.org/docs/app/api-reference/functions/cookies#setting-a-cookie)

You can use the `(await cookies()).set(name, value, options)` method in a [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) to set a cookie. The [`options` object](https://nextjs.org/docs/app/api-reference/functions/cookies#options) is optional.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { cookies } from 'next/headers'
     
    export async function create(data) {
      const cookieStore = await cookies()
     
      cookieStore.set('name', 'lee')
      // or
      cookieStore.set('name', 'lee', { secure: true })
      // or
      cookieStore.set({
        name: 'name',
        value: 'lee',
        httpOnly: true,
        path: '/',
      })
    }
[/code]

### Checking if a cookie exists[](https://nextjs.org/docs/app/api-reference/functions/cookies#checking-if-a-cookie-exists)

You can use the `(await cookies()).has(name)` method to check if a cookie exists:

app/page.ts

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'
     
    export default async function Page() {
      const cookieStore = await cookies()
      const hasCookie = cookieStore.has('theme')
      return '...'
    }
[/code]

### Deleting cookies[](https://nextjs.org/docs/app/api-reference/functions/cookies#deleting-cookies)

There are three ways you can delete a cookie.

Using the `delete()` method:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { cookies } from 'next/headers'
     
    export async function deleteCookie(data) {
      const cookieStore = await cookies()
      cookieStore.delete('name')
    }
[/code]

Setting a new cookie with the same name and an empty value:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { cookies } from 'next/headers'
     
    export async function deleteCookie(data) {
      const cookieStore = await cookies()
      cookieStore.set('name', '')
    }
[/code]

Setting the `maxAge` to 0 will immediately expire a cookie. `maxAge` accepts a value in seconds.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { cookies } from 'next/headers'
     
    export async function deleteCookie(data) {
      const cookieStore = await cookies()
      cookieStore.set('name', 'value', { maxAge: 0 })
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/cookies#version-history)

Version| Changes  
---|---  
`v15.0.0-RC`| `cookies` is now an async function. A [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150) is available.  
`v13.0.0`| `cookies` introduced.  
  
Was this helpful?

supported.

Send
