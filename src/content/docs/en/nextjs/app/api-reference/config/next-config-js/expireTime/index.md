---
title: 'next.config.js: expireTime'
description: 'Last updated February 20, 2026'
---

# next.config.js: expireTime | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)expireTime

Copy page

# expireTime

Last updated February 20, 2026

You can specify a custom `stale-while-revalidate` expire time for CDNs to consume in the `Cache-Control` header for ISR enabled pages.

Open `next.config.js` and add the `expireTime` config:

next.config.js
[code]
    module.exports = {
      // one hour in seconds
      expireTime: 3600,
    }
[/code]

Now when sending the `Cache-Control` header the expire time will be calculated depending on the specific revalidate period.

For example, if you have a revalidate of 15 minutes on a path and the expire time is one hour the generated `Cache-Control` header will be `s-maxage=900, stale-while-revalidate=2700` so that it can stay stale for 15 minutes less than the configured expire time.

Was this helpful?

supported.

Send
