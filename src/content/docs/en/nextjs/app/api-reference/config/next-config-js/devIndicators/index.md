---
title: 'next.config.js: devIndicators'
description: "allows you to configure the on-screen indicator that gives context about the current route you're viewing during development."
---

# next.config.js: devIndicators | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)devIndicators

Copy page

# devIndicators

Last updated February 20, 2026

`devIndicators` allows you to configure the on-screen indicator that gives context about the current route you're viewing during development.

Types
[code]
      devIndicators: false | {
        position?: 'bottom-right'
        | 'bottom-left'
        | 'top-right'
        | 'top-left', // defaults to 'bottom-left',
      },
[/code]

Setting `devIndicators` to `false` will hide the indicator, however Next.js will continue to surface any build or runtime errors that were encountered.

## Troubleshooting[](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators#troubleshooting)

### Indicator not marking a route as static[](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators#indicator-not-marking-a-route-as-static)

If you expect a route to be static and the indicator has marked it as dynamic, it's likely the route has opted out of static rendering.

You can confirm if a route is [static](https://nextjs.org/docs/app/guides/caching#static-rendering) or [dynamic](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) by building your application using `next build --debug`, and checking the output in your terminal. Static (or prerendered) routes will display a `○` symbol, whereas dynamic routes will display a `ƒ` symbol. For example:

Build Output
[code]
    Route (app)
    ┌ ○ /_not-found
    └ ƒ /products/[id]
     
    ○  (Static)   prerendered as static content
    ƒ  (Dynamic)  server-rendered on demand
[/code]

There are two reasons a route might opt out of static rendering:

  * The presence of [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) which rely on runtime information.
  * An [uncached data request](https://nextjs.org/docs/app/getting-started/fetching-data), like a call to an ORM or database driver.



Check your route for any of these conditions, and if you are not able to statically render the route, then consider using [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) or [`<Suspense />`](https://react.dev/reference/react/Suspense) to leverage [streaming](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming).

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators#version-history)

Version| Changes  
---|---  
`v16.0.0`| `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been removed.  
`v15.2.0`| Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated.  
`v15.0.0`| Static on-screen indicator added with `appIsrStatus` option.  
  
Was this helpful?

supported.

Send
