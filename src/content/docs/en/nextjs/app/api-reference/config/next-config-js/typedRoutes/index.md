---
title: 'next.config.js: typedRoutes'
description: 'Last updated February 20, 2026'
---

# next.config.js: typedRoutes | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)typedRoutes

Copy page

# typedRoutes

Last updated February 20, 2026

> **Note** : This option has been marked as stable, so you should use `typedRoutes` instead of `experimental.typedRoutes`.

Support for [statically typed links](https://nextjs.org/docs/app/api-reference/config/typescript#statically-typed-links). This feature requires using TypeScript in your project.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      typedRoutes: true,
    }
     
    module.exports = nextConfig
[/code]

Was this helpful?

supported.

Send
