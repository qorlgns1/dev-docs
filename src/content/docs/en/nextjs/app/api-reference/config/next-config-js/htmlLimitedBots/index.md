---
title: 'next.config.js: htmlLimitedBots'
description: 'The  config allows you to specify a list of user agents that should receive blocking metadata instead of streaming metadata.'
---

# next.config.js: htmlLimitedBots | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)htmlLimitedBots

Copy page

# htmlLimitedBots

Last updated February 20, 2026

The `htmlLimitedBots` config allows you to specify a list of user agents that should receive blocking metadata instead of [streaming metadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata).

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
    }
     
    export default config
[/code]

## Default list[](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#default-list)

Next.js includes a default list of HTML limited bots, including:

  * Google crawlers (e.g. Mediapartners-Google, AdsBot-Google, Google-PageRenderer)
  * Bingbot
  * Twitterbot
  * Slackbot



See the full list [here](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts).

Specifying a `htmlLimitedBots` config will override the Next.js' default list. However, this is advanced behavior, and the default should be sufficient for most cases.

next.config.ts

JavaScriptTypeScript
[code]
    const config: NextConfig = {
      htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
    }
     
    export default config
[/code]

## Disabling[](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#disabling)

To fully disable streaming metadata:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      htmlLimitedBots: /.*/,
    }
     
    export default config
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#version-history)

Version| Changes  
---|---  
15.2.0| `htmlLimitedBots` option introduced.  
  
Was this helpful?

supported.

Send
