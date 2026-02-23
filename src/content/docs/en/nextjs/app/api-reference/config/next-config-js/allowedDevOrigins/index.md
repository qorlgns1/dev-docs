---
title: 'next.config.js: allowedDevOrigins'
description: 'Next.js does not automatically block cross-origin requests during development, but will block by default in a future major version of Next.js to preve...'
---

# next.config.js: allowedDevOrigins | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)allowedDevOrigins

Copy page

# allowedDevOrigins

Last updated February 20, 2026

Next.js does not automatically block cross-origin requests during development, but will block by default in a future major version of Next.js to prevent unauthorized requesting of internal assets/endpoints that are available in development mode.

To configure a Next.js application to allow requests from origins other than the hostname the server was initialized with (`localhost` by default) you can use the `allowedDevOrigins` config option.

`allowedDevOrigins` allows you to set additional origins that can be used in development mode. For example, to use `local-origin.dev` instead of only `localhost`, open `next.config.js` and add the `allowedDevOrigins` config:

next.config.js
[code]
    module.exports = {
      allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
    }
[/code]

Was this helpful?

supported.

Send
