---
title: 'next.config.js: pageExtensions'
description: 'Last updated February 20, 2026'
---

# next.config.js: pageExtensions | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)pageExtensions

Copy page

# pageExtensions

Last updated February 20, 2026

By default, Next.js accepts files with the following extensions: `.tsx`, `.ts`, `.jsx`, `.js`. This can be modified to allow other extensions like markdown (`.md`, `.mdx`).

next.config.js
[code]
    const withMDX = require('@next/mdx')()
     
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
    }
     
    module.exports = withMDX(nextConfig)
[/code]

Was this helpful?

supported.

Send
