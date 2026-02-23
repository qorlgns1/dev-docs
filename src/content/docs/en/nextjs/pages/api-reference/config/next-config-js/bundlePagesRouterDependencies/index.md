---
title: 'next.config.js Options: bundlePagesRouterDependencies'
description: 'Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.'
---

# next.config.js Options: bundlePagesRouterDependencies | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)bundlePagesRouterDependencies

Copy page

# bundlePagesRouterDependencies

Last updated February 20, 2026

Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      bundlePagesRouterDependencies: true,
    }
     
    module.exports = nextConfig
[/code]

Explicitly opt-out certain packages from being bundled using the [`serverExternalPackages`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages) option.

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies#version-history)

Version| Changes  
---|---  
`v15.0.0`| Moved from experimental to stable. Renamed from `bundlePagesExternals` to `bundlePagesRouterDependencies`  
  
Was this helpful?

supported.

Send
