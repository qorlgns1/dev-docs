---
title: 'File-system conventions: unauthorized.js'
description: "This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub."
---

# File-system conventions: unauthorized.js | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)unauthorized.js

Copy page

# unauthorized.js

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

The **unauthorized** file is used to render UI when the [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `401` status code.

app/unauthorized.tsx

JavaScriptTypeScript
[code]
    import Login from '@/app/components/Login'
     
    export default function Unauthorized() {
      return (
        <main>
          <h1>401 - Unauthorized</h1>
          <p>Please log in to access this page.</p>
          <Login />
        </main>
      )
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#reference)

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#props)

`unauthorized.js` components do not accept any props.

## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#examples)

### Displaying login UI to unauthenticated users[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#displaying-login-ui-to-unauthenticated-users)

You can use [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized) function to render the `unauthorized.js` file with a login UI.

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
    import { unauthorized } from 'next/navigation'
     
    export default async function DashboardPage() {
      const session = await verifySession()
     
      if (!session) {
        unauthorized()
      }
     
      return <div>Dashboard</div>
    }
[/code]

app/unauthorized.tsx

JavaScriptTypeScript
[code]
    import Login from '@/app/components/Login'
     
    export default function UnauthorizedPage() {
      return (
        <main>
          <h1>401 - Unauthorized</h1>
          <p>Please log in to access this page.</p>
          <Login />
        </main>
      )
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#version-history)

Version| Changes  
---|---  
`v15.1.0`| `unauthorized.js` introduced.  
  
## 

### [unauthorizedAPI Reference for the unauthorized function.](https://nextjs.org/docs/app/api-reference/functions/unauthorized)

Was this helpful?

supported.

Send
