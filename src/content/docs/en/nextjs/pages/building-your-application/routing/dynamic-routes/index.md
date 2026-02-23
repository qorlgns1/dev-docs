---
title: 'Routing: Dynamic Routes'
description: "When you don't know the exact segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in..."
---

# Routing: Dynamic Routes | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes

[Building Your Application](https://nextjs.org/docs/pages/building-your-application)[Routing](https://nextjs.org/docs/pages/building-your-application/routing)Dynamic Routes

Copy page

# Dynamic Routes

Last updated February 20, 2026

When you don't know the exact segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or [prerendered](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths) at build time.

## Convention[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention)

A Dynamic Segment can be created by wrapping a file or folder name in square brackets: `[segmentName]`. For example, `[id]` or `[slug]`.

Dynamic Segments can be accessed from [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router).

## Example[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#example)

For example, a blog could include the following route `pages/blog/[slug].js` where `[slug]` is the Dynamic Segment for blog posts.
[code] 
    import { useRouter } from 'next/router'
     
    export default function Page() {
      const router = useRouter()
      return <p>Post: {router.query.slug}</p>
    }
[/code]

Route| Example URL| `params`  
---|---|---  
`pages/blog/[slug].js`| `/blog/a`| `{ slug: 'a' }`  
`pages/blog/[slug].js`| `/blog/b`| `{ slug: 'b' }`  
`pages/blog/[slug].js`| `/blog/c`| `{ slug: 'c' }`  
  
## Catch-all Segments[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#catch-all-segments)

Dynamic Segments can be extended to **catch-all** subsequent segments by adding an ellipsis inside the brackets `[...segmentName]`.

For example, `pages/shop/[...slug].js` will match `/shop/clothes`, but also `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`, and so on.

Route| Example URL| `params`  
---|---|---  
`pages/shop/[...slug].js`| `/shop/a`| `{ slug: ['a'] }`  
`pages/shop/[...slug].js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`  
`pages/shop/[...slug].js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`  
  
## Optional Catch-all Segments[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments)

Catch-all Segments can be made **optional** by including the parameter in double square brackets: `[[...segmentName]]`.

For example, `pages/shop/[[...slug]].js` will **also** match `/shop`, in addition to `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`.

The difference between **catch-all** and **optional catch-all** segments is that with optional, the route without the parameter is also matched (`/shop` in the example above).

Route| Example URL| `params`  
---|---|---  
`pages/shop/[[...slug]].js`| `/shop`| `{ slug: undefined }`  
`pages/shop/[[...slug]].js`| `/shop/a`| `{ slug: ['a'] }`  
`pages/shop/[[...slug]].js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`  
`pages/shop/[[...slug]].js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`  
  
## Next Steps

For more information on what to do next, we recommend the following sections

### [Linking and NavigatingLearn how navigation works in Next.js, and how to use the Link Component and `useRouter` hook.](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating)### [useRouterLearn more about the API of the Next.js Router, and access the router instance in your page with the useRouter hook.](https://nextjs.org/docs/pages/api-reference/functions/use-router)

Was this helpful?

supported.

Send
