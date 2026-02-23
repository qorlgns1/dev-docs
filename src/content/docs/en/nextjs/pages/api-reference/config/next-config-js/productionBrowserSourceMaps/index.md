---
title: 'next.config.js Options: productionBrowserSourceMaps'
description: 'Last updated February 20, 2026'
---

# next.config.js Options: productionBrowserSourceMaps | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)productionBrowserSourceMaps

Copy page

# productionBrowserSourceMaps

Last updated February 20, 2026

Source Maps are enabled by default during development. During production builds, they are disabled to prevent you leaking your source on the client, unless you specifically opt-in with the configuration flag.

Next.js provides a configuration flag you can use to enable browser source map generation during the production build:

next.config.js
[code]
    module.exports = {
      productionBrowserSourceMaps: true,
    }
[/code]

When the `productionBrowserSourceMaps` option is enabled, the source maps will be output in the same directory as the JavaScript files. Next.js will automatically serve these files when requested.

  * Adding source maps can increase `next build` time
  * Increases memory usage during `next build`



Was this helpful?

supported.

Send
