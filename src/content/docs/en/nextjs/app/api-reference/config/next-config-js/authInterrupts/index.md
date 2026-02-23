---
title: 'next.config.js: authInterrupts'
description: 'This feature is currently available in the canary channel and subject to change. Try it out by upgrading Next.js, and share your feedback on GitHub.'
---

# next.config.js: authInterrupts | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)authInterrupts

Copy page

# authInterrupts

This feature is currently available in the canary channel and subject to change. Try it out by [upgrading Next.js](https://nextjs.org/docs/app/getting-started/upgrading#canary-version), and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

The `authInterrupts` configuration option allows you to use [`forbidden`](https://nextjs.org/docs/app/api-reference/functions/forbidden) and [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized) APIs in your application. While these functions are experimental, you must enable the `authInterrupts` option in your `next.config.js` file to use them:

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

## 

### [forbiddenAPI Reference for the forbidden function.](https://nextjs.org/docs/app/api-reference/functions/forbidden)### [unauthorizedAPI Reference for the unauthorized function.](https://nextjs.org/docs/app/api-reference/functions/unauthorized)### [forbidden.jsAPI reference for the forbidden.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)### [unauthorized.jsAPI reference for the unauthorized.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)

Was this helpful?

supported.

Send
