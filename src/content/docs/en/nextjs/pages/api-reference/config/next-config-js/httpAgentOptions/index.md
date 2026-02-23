---
title: 'httpAgentOptions'
description: 'In Node.js versions prior to 18, Next.js automatically polyfills  with undici and enables HTTP Keep-Alive by default.'
---

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions

# httpAgentOptions

In Node.js versions prior to 18, Next.js automatically polyfills `fetch()` with [undici](https://nextjs.org/docs/architecture/supported-browsers#polyfills) and enables [HTTP Keep-Alive](https://developer.mozilla.org/docs/Web/HTTP/Headers/Keep-Alive) by default.

To disable HTTP Keep-Alive for all `fetch()` calls on the server-side, open `next.config.js` and add the `httpAgentOptions` config:

```js filename="next.config.js"
module.exports = {
  httpAgentOptions: {
    keepAlive: false,
  },
}
```
---

