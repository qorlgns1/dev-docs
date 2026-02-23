---
title: 'next.config.js Options: poweredByHeader'
description: 'Last updated February 20, 2026'
---

# next.config.js Options: poweredByHeader | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)poweredByHeader

Copy page

# poweredByHeader

Last updated February 20, 2026

By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:

next.config.js
[code]
    module.exports = {
      poweredByHeader: false,
    }
[/code]

Was this helpful?

supported.

Send
