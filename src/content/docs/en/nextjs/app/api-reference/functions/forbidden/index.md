---
title: 'Functions: forbidden'
description: "This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub."
---

# Functions: forbidden | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/forbidden

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)forbidden

Copy page

# forbidden

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

The `forbidden` function throws an error that renders a Next.js 403 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`forbidden.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden).

To start using `forbidden`, enable the experimental [`authInterrupts`](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts) configuration option in your `next.config.js` file:

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

`forbidden` can be invoked in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data), and [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route).

app/auth/page.tsx

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
    import { forbidden } from 'next/navigation'
     
    export default async function AdminPage() {
      const session = await verifySession()
     
      // Check if the user has the 'admin' role
      if (session.role !== 'admin') {
        forbidden()
      }
     
      // Render the admin page for authorized users
      return <></>
    }
[/code]

## Good to know[](https://nextjs.org/docs/app/api-reference/functions/forbidden#good-to-know)

  * The `forbidden` function cannot be called in the [root layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout).



## Examples[](https://nextjs.org/docs/app/api-reference/functions/forbidden#examples)

### Role-based route protection[](https://nextjs.org/docs/app/api-reference/functions/forbidden#role-based-route-protection)

You can use `forbidden` to restrict access to certain routes based on user roles. This ensures that users who are authenticated but lack the required permissions cannot access the route.

app/admin/page.tsx

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
    import { forbidden } from 'next/navigation'
     
    export default async function AdminPage() {
      const session = await verifySession()
     
      // Check if the user has the 'admin' role
      if (session.role !== 'admin') {
        forbidden()
      }
     
      // Render the admin page for authorized users
      return (
        <main>
          <h1>Admin Dashboard</h1>
          <p>Welcome, {session.user.name}!</p>
        </main>
      )
    }
[/code]

### Mutations with Server Actions[](https://nextjs.org/docs/app/api-reference/functions/forbidden#mutations-with-server-actions)

When implementing mutations in Server Actions, you can use `forbidden` to only allow users with a specific role to update sensitive data.

app/actions/update-role.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { verifySession } from '@/app/lib/dal'
    import { forbidden } from 'next/navigation'
    import db from '@/app/lib/db'
     
    export async function updateRole(formData: FormData) {
      const session = await verifySession()
     
      // Ensure only admins can update roles
      if (session.role !== 'admin') {
        forbidden()
      }
     
      // Perform the role update for authorized users
      // ...
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/forbidden#version-history)

Version| Changes  
---|---  
`v15.1.0`| `forbidden` introduced.  
  
## 

### [forbidden.jsAPI reference for the forbidden.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)

Was this helpful?

supported.

Send
