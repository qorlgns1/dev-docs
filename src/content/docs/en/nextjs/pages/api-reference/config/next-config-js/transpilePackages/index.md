---
title: 'next.config.js Options: transpilePackages'
description: 'Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (). This replaces the...'
---

# next.config.js Options: transpilePackages | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)transpilePackages

Copy page

# transpilePackages

Last updated February 20, 2026

Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`). This replaces the `next-transpile-modules` package.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      transpilePackages: ['package-name'],
    }
     
    module.exports = nextConfig
[/code]

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages#version-history)

Version| Changes  
---|---  
`v13.0.0`| `transpilePackages` added.  
  
Was this helpful?

supported.

Send
