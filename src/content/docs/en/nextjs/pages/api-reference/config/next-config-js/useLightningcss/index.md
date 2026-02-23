---
title: 'next.config.js Options: useLightningcss'
description: "This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub."
---

# next.config.js Options: useLightningcss | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)useLightningcss

Copy page

# useLightningcss

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

Experimental support for using [Lightning CSS](https://lightningcss.dev) with webpack. Lightning CSS is a fast CSS transformer and minifier, written in Rust.

If this option is not set, Next.js on webpack uses [PostCSS](https://postcss.org/) with [`postcss-preset-env`](https://www.npmjs.com/package/postcss-preset-env) by default.

Turbopack uses Lightning CSS by default since Next 14.2. This configuration option has no effect on Turbopack. Turbopack always uses Lightning CSS.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        useLightningcss: false, // default, ignored on Turbopack
      },
    }
     
    export default nextConfig
[/code]

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss#version-history)

Version| Changes  
---|---  
`15.1.0`| Support for `useSwcCss` was removed from Turbopack.  
`14.2.0`| Turbopack's default CSS processor was changed from `@swc/css` to Lightning CSS. `useLightningcss` became ignored on Turbopack, and a legacy `experimental.turbo.useSwcCss` option was added.  
  
Was this helpful?

supported.

Send
