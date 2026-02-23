---
title: 'next.config.js: viewTransition'
description: "This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub."
---

# next.config.js: viewTransition | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)viewTransition

Copy page

# viewTransition

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

`viewTransition` is an experimental flag that enables the new [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) in React. This API allows you to leverage the native View Transitions browser API to create seamless transitions between UI states.

To enable this feature, you need to set the `viewTransition` property to `true` in your `next.config.js` file.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        viewTransition: true,
      },
    }
     
    module.exports = nextConfig
[/code]

> Important Notice: The `<ViewTransition>` Component is already available in React's Canary release channel. `experimental.viewTransition` is only required to enable deeper integration with Next.js features e.g. automatically [adding Transition types](https://react.dev/reference/react/addTransitionType) for navigations. Next.js specific transition types are not implemented yet.

## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition#usage)

You can import the [`<ViewTransition>` Component](https://react.dev/reference/react/ViewTransition) from React in your application:
[code] 
    import { ViewTransition } from 'react'
[/code]

### Live Demo[](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition#live-demo)

Check out our [Next.js View Transition Demo](https://view-transition-example.vercel.app) to see this feature in action.

As this API evolves, we will update our documentation and share more examples. However, for now, we strongly advise against using this feature in production.

Was this helpful?

supported.

Send
