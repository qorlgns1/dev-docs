---
title: 'Functions: headers'
description: 'is an async function that allows you to read the HTTP incoming request headers from a Server Component.'
---

# Functions: headers | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/headers

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)headers

Copy page

# headers

Last updated February 20, 2026

`headers` is an **async** function that allows you to **read** the HTTP incoming request headers from a [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components).

app/page.tsx

JavaScriptTypeScript
[code]
    import { headers } from 'next/headers'
     
    export default async function Page() {
      const headersList = await headers()
      const userAgent = headersList.get('user-agent')
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/functions/headers#reference)

### Parameters[](https://nextjs.org/docs/app/api-reference/functions/headers#parameters)

`headers` does not take any parameters.

### Returns[](https://nextjs.org/docs/app/api-reference/functions/headers#returns)

`headers` returns a **read-only** [Web Headers](https://developer.mozilla.org/docs/Web/API/Headers) object.

  * [`Headers.entries()`](https://developer.mozilla.org/docs/Web/API/Headers/entries): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing to go through all key/value pairs contained in this object.
  * [`Headers.forEach()`](https://developer.mozilla.org/docs/Web/API/Headers/forEach): Executes a provided function once for each key/value pair in this `Headers` object.
  * [`Headers.get()`](https://developer.mozilla.org/docs/Web/API/Headers/get): Returns a [`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) sequence of all the values of a header within a `Headers` object with a given name.
  * [`Headers.has()`](https://developer.mozilla.org/docs/Web/API/Headers/has): Returns a boolean stating whether a `Headers` object contains a certain header.
  * [`Headers.keys()`](https://developer.mozilla.org/docs/Web/API/Headers/keys): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all keys of the key/value pairs contained in this object.
  * [`Headers.values()`](https://developer.mozilla.org/docs/Web/API/Headers/values): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all values of the key/value pairs contained in this object.



## Good to know[](https://nextjs.org/docs/app/api-reference/functions/headers#good-to-know)

  * `headers` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function.
    * In version 14 and earlier, `headers` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * Since `headers` is read-only, you cannot `set` or `delete` the outgoing request headers.
  * `headers` is a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) whose returned values cannot be known ahead of time. Using it in will opt a route into **[dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)**.



## Examples[](https://nextjs.org/docs/app/api-reference/functions/headers#examples)

### Using the Authorization header[](https://nextjs.org/docs/app/api-reference/functions/headers#using-the-authorization-header)

app/page.js
[code]
    import { headers } from 'next/headers'
     
    export default async function Page() {
      const authorization = (await headers()).get('authorization')
      const res = await fetch('...', {
        headers: { authorization }, // Forward the authorization header
      })
      const user = await res.json()
     
      return <h1>{user.name}</h1>
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/headers#version-history)

Version| Changes  
---|---  
`v15.0.0-RC`| `headers` is now an async function. A [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150) is available.  
`v13.0.0`| `headers` introduced.  
  
Was this helpful?

supported.

Send
