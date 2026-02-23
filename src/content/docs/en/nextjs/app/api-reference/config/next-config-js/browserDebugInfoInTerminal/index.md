---
title: 'next.config.js: browserDebugInfoInTerminal'
description: "This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub."
---

# next.config.js: browserDebugInfoInTerminal | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)browserDebugInfoInTerminal

Copy page

# browserDebugInfoInTerminal

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

The `experimental.browserDebugInfoInTerminal` option forwards console output and runtime errors originating in the browser to the dev server terminal.

This option is disabled by default. When enabled it only works in development mode.

## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#usage)

Enable forwarding:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        browserDebugInfoInTerminal: true,
      },
    }
     
    export default nextConfig
[/code]

### Serialization limits[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#serialization-limits)

Deeply nested objects/arrays are truncated using **sensible defaults**. You can tweak these limits:

  * **depthLimit** : (optional) Limit stringification depth for nested objects/arrays. Default: 5
  * **edgeLimit** : (optional) Max number of properties or elements to include per object or array. Default: 100



next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        browserDebugInfoInTerminal: {
          depthLimit: 5,
          edgeLimit: 100,
        },
      },
    }
     
    export default nextConfig
[/code]

### Source location[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#source-location)

Source locations are included by default when this feature is enabled.

app/page.tsx
[code]
    'use client'
     
    export default function Home() {
      return (
        <button
          type="button"
          onClick={() => {
            console.log('Hello World')
          }}
        >
          Click me
        </button>
      )
    }
[/code]

Clicking the button prints this message to the terminal.

Terminal
[code]
    [browser] Hello World (app/page.tsx:8:17)
[/code]

To suppress them, set `showSourceLocation: false`.

  * **showSourceLocation** : Include source location info when available.



next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        browserDebugInfoInTerminal: {
          showSourceLocation: false,
        },
      },
    }
     
    export default nextConfig
[/code]

Version| Changes  
---|---  
`v15.4.0`| experimental `browserDebugInfoInTerminal` introduced  
  
Was this helpful?

supported.

Send
