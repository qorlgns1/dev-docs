---
title: 'Directives: use client'
description: 'The  directive declares an entry point for the components to be rendered on the client side and should be used when creating interactive user interfac...'
---

# Directives: use client | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/directives/use-client

[API Reference](https://nextjs.org/docs/app/api-reference)[Directives](https://nextjs.org/docs/app/api-reference/directives)use client

Copy page

# use client

Last updated February 20, 2026

The `'use client'` directive declares an entry point for the components to be rendered on the **client side** and should be used when creating interactive user interfaces (UI) that require client-side JavaScript capabilities, such as state management, event handling, and access to browser APIs. This is a React feature.

> **Good to know:**
> 
> You do not need to add the `'use client'` directive to every file that contains Client Components. You only need to add it to the files whose components you want to render directly within Server Components. The `'use client'` directive defines the client-server [boundary](https://nextjs.org/docs/app/building-your-application/rendering#network-boundary), and the components exported from such a file serve as entry points to the client.

## Usage[](https://nextjs.org/docs/app/api-reference/directives/use-client#usage)

To declare an entry point for the Client Components, add the `'use client'` directive **at the top of the file** , before any imports:

app/components/counter.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useState } from 'react'
     
    export default function Counter() {
      const [count, setCount] = useState(0)
     
      return (
        <div>
          <p>Count: {count}</p>
          <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
      )
    }
[/code]

When using the `'use client'` directive, the props of the Client Components must be [serializable](https://react.dev/reference/rsc/use-client#serializable-types). This means the props need to be in a format that React can serialize when sending data from the server to the client.

app/components/counter.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function Counter({
      onClick /* ❌ Function is not serializable */,
    }) {
      return (
        <div>
          <button onClick={onClick}>Increment</button>
        </div>
      )
    }
[/code]

## Nesting Client Components within Server Components[](https://nextjs.org/docs/app/api-reference/directives/use-client#nesting-client-components-within-server-components)

Combining Server and Client Components allows you to build applications that are both performant and interactive:

  1. **Server Components** : Use for static content, data fetching, and SEO-friendly elements.
  2. **Client Components** : Use for interactive elements that require state, effects, or browser APIs.
  3. **Component composition** : Nest Client Components within Server Components as needed for a clear separation of server and client logic.



In the following example:

  * `Header` is a Server Component handling static content.
  * `Counter` is a Client Component enabling interactivity within the page.



app/page.tsx

JavaScriptTypeScript
[code]
    import Header from './header'
    import Counter from './counter' // This is a Client Component
     
    export default function Page() {
      return (
        <div>
          <Header />
          <Counter />
        </div>
      )
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/directives/use-client#reference)

See the [React documentation](https://react.dev/reference/rsc/use-client) for more information on `'use client'`.

Was this helpful?

supported.

Send
