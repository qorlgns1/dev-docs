---
title: 'next.config.js: compress'
description: 'Last updated February 20, 2026'
---

# next.config.js: compress | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/compress

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)compress

Copy page

# compress

Last updated February 20, 2026

By default, Next.js uses `gzip` to compress rendered content and static files when using `next start` or a custom server. This is an optimization for applications that do not have compression configured. If compression is _already_ configured in your application via a custom server, Next.js will not add compression.

You can check if compression is enabled and which algorithm is used by looking at the [`Accept-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding) (browser accepted options) and [`Content-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) (currently used) headers in the response.

## Disabling compression[](https://nextjs.org/docs/app/api-reference/config/next-config-js/compress#disabling-compression)

To disable **compression** , set the `compress` config option to `false`:

next.config.js
[code]
    module.exports = {
      compress: false,
    }
[/code]

We **do not recommend disabling compression** unless you have compression configured on your server, as compression reduces bandwidth usage and improves the performance of your application. For example, you're using [nginx](https://nginx.org/) and want to switch to `brotli`, set the `compress` option to `false` to allow nginx to handle compression.

Was this helpful?

supported.

Send
