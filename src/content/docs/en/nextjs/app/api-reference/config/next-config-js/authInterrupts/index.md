---
title: 'authInterrupts'
description: '> This feature is currently available in the canary channel and subject to change.'
---

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts

# authInterrupts

> This feature is currently available in the canary channel and subject to change.

The `authInterrupts` configuration option allows you to use [`forbidden`](https://nextjs.org/docs/app/api-reference/functions/forbidden) and [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized) APIs in your application. While these functions are experimental, you must enable the `authInterrupts` option in your `next.config.js` file to use them:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
module.exports = {
  experimental: {
    authInterrupts: true,
  },
}
```
- [forbidden](https://nextjs.org/docs/app/api-reference/functions/forbidden)
  - API Reference for the forbidden function.
- [unauthorized](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
  - API Reference for the unauthorized function.
- [forbidden.js](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
  - API reference for the forbidden.js special file.
- [unauthorized.js](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
  - API reference for the unauthorized.js special file.

---

