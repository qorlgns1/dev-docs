---
title: 'next.config.js: mdxRs'
description: "This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub."
---

# next.config.js: mdxRs | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)mdxRs

Copy page

# mdxRs

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

For experimental use with `@next/mdx`. Compiles MDX files using the new Rust compiler.

next.config.js
[code]
    const withMDX = require('@next/mdx')()
     
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      pageExtensions: ['ts', 'tsx', 'mdx'],
      experimental: {
        mdxRs: true,
      },
    }
     
    module.exports = withMDX(nextConfig)
[/code]

Was this helpful?

supported.

Send
