---
title: 'Functions: unauthorized'
description: "This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub."
---

# Functions: unauthorized | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/unauthorized

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)unauthorized

Copy page

# unauthorized

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

The `unauthorized` function throws an error that renders a Next.js 401 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`unauthorized.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized).

To start using `unauthorized`, enable the experimental [`authInterrupts`](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts) configuration option in your `next.config.js` file:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        authInterrupts: true,
      },
    }
     
    export default nextConfig
[/code]

`unauthorized` can be invoked in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data), and [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route).

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
     
      // Render the dashboard for authenticated users
      return (
        <main>
          <h1>Welcome to the Dashboard</h1>
          <p>Hi, {session.user.name}.</p>
        </main>
      )
    }
[/code]

## Good to know[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#good-to-know)

  * The `unauthorized` function cannot be called in the [root layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout).



## Examples[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#examples)

### Displaying login UI to unauthenticated users[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#displaying-login-ui-to-unauthenticated-users)

You can use `unauthorized` function to display the `unauthorized.js` file with a login UI.

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

### Mutations with Server Actions[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#mutations-with-server-actions)

You can invoke `unauthorized` in Server Actions to ensure only authenticated users can perform specific mutations.

app/actions/update-profile.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { verifySession } from '@/app/lib/dal'
    import { unauthorized } from 'next/navigation'
    import db from '@/app/lib/db'
     
    export async function updateProfile(data: FormData) {
      const session = await verifySession()
     
      // If the user is not authenticated, return a 401
      if (!session) {
        unauthorized()
      }
     
      // Proceed with mutation
      // ...
    }
[/code]

### Fetching data with Route Handlers[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#fetching-data-with-route-handlers)

You can use `unauthorized` in Route Handlers to ensure only authenticated users can access the endpoint.

app/api/profile/route.ts

JavaScriptTypeScript
[code]
    import { NextRequest, NextResponse } from 'next/server'
    import { verifySession } from '@/app/lib/dal'
    import { unauthorized } from 'next/navigation'
     
    export async function GET(req: NextRequest): Promise<NextResponse> {
      // Verify the user's session
      const session = await verifySession()
     
      // If no session exists, return a 401 and render unauthorized.tsx
      if (!session) {
        unauthorized()
      }
     
      // Fetch data
      // ...
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#version-history)

Version| Changes  
---|---  
`v15.1.0`| `unauthorized` introduced.  
  
## 

### [unauthorized.jsAPI reference for the unauthorized.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)

Was this helpful?

supported.

Send
