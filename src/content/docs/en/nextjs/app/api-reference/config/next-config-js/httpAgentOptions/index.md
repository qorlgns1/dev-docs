---
title: 'next.config.js: httpAgentOptions'
description: 'In Node.js versions prior to 18, Next.js automatically polyfills  with undici and enables HTTP Keep-Alive by default.'
---

# next.config.js: httpAgentOptions | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)httpAgentOptions

Copy page

# httpAgentOptions

Last updated February 20, 2026

In Node.js versions prior to 18, Next.js automatically polyfills `fetch()` with [undici](https://nextjs.org/docs/architecture/supported-browsers#polyfills) and enables [HTTP Keep-Alive](https://developer.mozilla.org/docs/Web/HTTP/Headers/Keep-Alive) by default.

To disable HTTP Keep-Alive for all `fetch()` calls on the server-side, open `next.config.js` and add the `httpAgentOptions` config:

next.config.js
[code]
    module.exports = {
      httpAgentOptions: {
        keepAlive: false,
      },
    }
[/code]

Was this helpful?

supported.

Send
