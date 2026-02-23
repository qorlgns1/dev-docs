---
title: 'next.config.js Options: isolatedDevBuild'
description: 'The experimental  option separates development and production build outputs into different directories. When enabled, the development server () writes...'
---

# next.config.js Options: isolatedDevBuild | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)isolatedDevBuild

Copy page

# isolatedDevBuild

Last updated February 20, 2026

The experimental `isolatedDevBuild` option separates development and production build outputs into different directories. When enabled, the development server (`next dev`) writes its output to `.next/dev` instead of `.next`, preventing conflicts when running `next dev` and `next build` concurrently.

This is especially helpful when automated tools (for example, AI agents) run `next build` to validate changes while your development server is running, ensuring the dev server is not affected by changes made by the build process.

This feature is **enabled by default** to keep development and production outputs separate and prevent conflicts.

## Configuration[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild#configuration)

To opt out of this feature, set `isolatedDevBuild` to `false` in your configuration:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        isolatedDevBuild: false, // defaults to true
      },
    }
     
    export default nextConfig
[/code]

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild#version-history)

Version| Changes  
---|---  
`v16.0.0`| `experimental.isolatedDevBuild` is introduced.  
  
Was this helpful?

supported.

Send
