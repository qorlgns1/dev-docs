---
title: 'typedRoutes'
description: '> Note: This option has been marked as stable, so you should use  instead of .'
---

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes

# typedRoutes

> **Note**: This option has been marked as stable, so you should use `typedRoutes` instead of `experimental.typedRoutes`.

Support for [statically typed links](https://nextjs.org/docs/app/api-reference/config/typescript#statically-typed-links). This feature requires using TypeScript in your project.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  typedRoutes: true,
}

module.exports = nextConfig
```
---

