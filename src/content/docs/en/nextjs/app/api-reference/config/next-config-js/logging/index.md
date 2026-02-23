---
title: 'next.config.js: logging'
description: 'Last updated February 20, 2026'
---

# next.config.js: logging | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/logging

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)logging

Copy page

# logging

Last updated February 20, 2026

## Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#options)

### Fetching[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#fetching)

You can configure the logging level and whether the full URL is logged to the console when running Next.js in development mode.

Currently, `logging` only applies to data fetching using the `fetch` API. It does not yet apply to other logs inside of Next.js.

next.config.js
[code]
    module.exports = {
      logging: {
        fetches: {
          fullUrl: true,
        },
      },
    }
[/code]

Any `fetch` requests that are restored from the [Server Components HMR cache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache) are not logged by default. However, this can be enabled by setting `logging.fetches.hmrRefreshes` to `true`.

next.config.js
[code]
    module.exports = {
      logging: {
        fetches: {
          hmrRefreshes: true,
        },
      },
    }
[/code]

### Incoming Requests[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#incoming-requests)

By default all the incoming requests will be logged in the console during development. You can use the `incomingRequests` option to decide which requests to ignore. Since this is only logged in development, this option doesn't affect production builds.

next.config.js
[code]
    module.exports = {
      logging: {
        incomingRequests: {
          ignore: [/\api\/v1\/health/],
        },
      },
    }
[/code]

Or you can disable incoming request logging by setting `incomingRequests` to `false`.

next.config.js
[code]
    module.exports = {
      logging: {
        incomingRequests: false,
      },
    }
[/code]

### Disabling Logging[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#disabling-logging)

In addition, you can disable the development logging by setting `logging` to `false`.

next.config.js
[code]
    module.exports = {
      logging: false,
    }
[/code]

Was this helpful?

supported.

Send
