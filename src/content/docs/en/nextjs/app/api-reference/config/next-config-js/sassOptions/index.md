---
title: 'next.config.js: sassOptions'
description: 'Last updated February 20, 2026'
---

# next.config.js: sassOptions | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)sassOptions

Copy page

# sassOptions

Last updated February 20, 2026

`sassOptions` allow you to configure the Sass compiler.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const sassOptions = {
      additionalData: `
        $var: red;
      `,
    }
     
    const nextConfig: NextConfig = {
      sassOptions: {
        ...sassOptions,
        implementation: 'sass-embedded',
      },
    }
     
    export default nextConfig
[/code]

> **Good to know:**
> 
>   * `sassOptions` are not typed outside of `implementation` because Next.js does not maintain the other possible properties.
>   * The `functions` property for defining custom Sass functions is only supported with webpack. When using Turbopack, custom Sass functions are not available because Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through this option.
> 


Was this helpful?

supported.

Send
