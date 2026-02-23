---
title: 'next.config.js Options: generateEtags'
description: 'Last updated February 20, 2026'
---

# next.config.js Options: generateEtags | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)generateEtags

Copy page

# generateEtags

Last updated February 20, 2026

Next.js will generate [etags](https://en.wikipedia.org/wiki/HTTP_ETag) for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.

Open `next.config.js` and disable the `generateEtags` option:

next.config.js
[code]
    module.exports = {
      generateEtags: false,
    }
[/code]

Was this helpful?

supported.

Send
