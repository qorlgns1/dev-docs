---
title: 'Guides: ISR'
description: 'Incremental Static Regeneration (ISR) enables you to:'
---

# Guides: ISR | Next.js

Source URL: https://nextjs.org/docs/pages/guides/incremental-static-regeneration

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)ISR

Copy page

# How to implement Incremental Static Regeneration (ISR)

Last updated February 20, 2026

Examples

  * [Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce)
  * [On-Demand ISR](https://on-demand-isr.vercel.app)
  * [Next.js Forms](https://github.com/vercel/next.js/tree/canary/examples/next-forms)



Incremental Static Regeneration (ISR) enables you to:

  * Update static content without rebuilding the entire site
  * Reduce server load by serving prerendered, static pages for most requests
  * Ensure proper `cache-control` headers are automatically added to pages
  * Handle large amounts of content pages without long `next build` times



Here's a minimal example:

pages/blog/[id].tsx

JavaScriptTypeScript
[code]
    import type { GetStaticPaths, GetStaticProps } from 'next'
     
    interface Post {
      id: string
      title: string
      content: string
    }
     
    interface Props {
      post: Post
    }
     
    export const getStaticPaths: GetStaticPaths = async () => {
      const posts = await fetch('https://api.vercel.app/blog').then((res) =>
        res.json()
      )
      const paths = posts.map((post: Post) => ({
        params: { id: String(post.id) },
      }))
     
      return { paths, fallback: 'blocking' }
    }
     
    export const getStaticProps: GetStaticProps<Props> = async ({
      params,
    }: {
      params: { id: string }
    }) => {
      const post = await fetch(`https://api.vercel.app/blog/${params.id}`).then(
        (res) => res.json()
      )
     
      return {
        props: { post },
        // Next.js will invalidate the cache when a
        // request comes in, at most once every 60 seconds.
        revalidate: 60,
      }
    }
     
    export default function Page({ post }: Props) {
      return (
        <main>
          <h1>{post.title}</h1>
          <p>{post.content}</p>
        </main>
      )
    }
[/code]

Here's how this example works:

  1. During `next build`, all known blog posts are generated
  2. All requests made to these pages (e.g. `/blog/1`) are cached and instantaneous
  3. After 60 seconds has passed, the next request will still return the cached (now stale) page
  4. The cache is invalidated and a new version of the page begins generating in the background
  5. Once generated successfully, the next request will return the updated page and cache it for subsequent requests
  6. If `/blog/26` is requested, and it exists, the page will be generated on-demand. This behavior can be changed by using a different [fallback](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-false) value. However, if the post does not exist, then 404 is returned.



## Reference[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#reference)

### Functions[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#functions-1)

  * [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
  * [`res.revalidate`](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#response-helpers)



## Examples[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#examples)

### On-demand validation with `res.revalidate()`[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-validation-with-resrevalidate)

For a more precise method of revalidation, use `res.revalidate` to generate a new page on-demand from an API Router.

For example, this API Route can be called at `/api/revalidate?secret=<token>` to revalidate a given blog post. Create a secret token only known by your Next.js app. This secret will be used to prevent unauthorized access to the revalidation API Route.

pages/api/revalidate.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'
     
    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      // Check for secret to confirm this is a valid request
      if (req.query.secret !== process.env.MY_SECRET_TOKEN) {
        return res.status(401).json({ message: 'Invalid token' })
      }
     
      try {
        // This should be the actual path not a rewritten path
        // e.g. for "/posts/[id]" this should be "/posts/1"
        await res.revalidate('/posts/1')
        return res.json({ revalidated: true })
      } catch (err) {
        // If there was an error, Next.js will continue
        // to show the last successfully generated page
        return res.status(500).send('Error revalidating')
      }
    }
[/code]

If you are using on-demand revalidation, you do not need to specify a `revalidate` time inside of `getStaticProps`. Next.js will use the default value of `false` (no revalidation) and only revalidate the page on-demand when `res.revalidate()` is called.

### Handling uncaught exceptions[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#handling-uncaught-exceptions)

If there is an error inside `getStaticProps` when handling background regeneration, or you manually throw an error, the last successfully generated page will continue to show. On the next subsequent request, Next.js will retry calling `getStaticProps`.

pages/blog/[id].tsx

JavaScriptTypeScript
[code]
    import type { GetStaticProps } from 'next'
     
    interface Post {
      id: string
      title: string
      content: string
    }
     
    interface Props {
      post: Post
    }
     
    export const getStaticProps: GetStaticProps<Props> = async ({
      params,
    }: {
      params: { id: string }
    }) => {
      // If this request throws an uncaught error, Next.js will
      // not invalidate the currently shown page and
      // retry getStaticProps on the next request.
      const res = await fetch(`https://api.vercel.app/blog/${params.id}`)
      const post: Post = await res.json()
     
      if (!res.ok) {
        // If there is a server error, you might want to
        // throw an error instead of returning so that the cache is not updated
        // until the next successful request.
        throw new Error(`Failed to fetch posts, received status ${res.status}`)
      }
     
      return {
        props: { post },
        // Next.js will invalidate the cache when a
        // request comes in, at most once every 60 seconds.
        revalidate: 60,
      }
    }
[/code]

### Customizing the cache location[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#customizing-the-cache-location)

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application. [Learn more](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr).

## Troubleshooting[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#troubleshooting)

### Debugging cached data in local development[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#debugging-cached-data-in-local-development)

If you are using the `fetch` API, you can add additional logging to understand which requests are cached or uncached. [Learn more about the `logging` option](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging).

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

### Verifying correct production behavior[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#verifying-correct-production-behavior)

To verify your pages are cached and revalidated correctly in production, you can test locally by running `next build` and then `next start` to run the production Next.js server.

This will allow you to test ISR behavior as it would work in a production environment. For further debugging, add the following environment variable to your `.env` file:

.env
[code]
    NEXT_PRIVATE_DEBUG_CACHE=1
[/code]

This will make the Next.js server console log ISR cache hits and misses. You can inspect the output to see which pages are generated during `next build`, as well as how pages are updated as paths are accessed on-demand.

## Caveats[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#caveats)

  * ISR is only supported when using the Node.js runtime (default).
  * ISR is not supported when creating a [Static Export](https://nextjs.org/docs/app/guides/static-exports).
  * Proxy won't be executed for on-demand ISR requests, meaning any path rewrites or logic in Proxy will not be applied. Ensure you are revalidating the exact path. For example, `/post/1` instead of a rewritten `/post-1`.



## Platform Support[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#platform-support)

Deployment Option| Supported  
---|---  
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| Yes  
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| Yes  
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| No  
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| Platform-specific  
  
Learn how to [configure ISR](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr) when self-hosting Next.js.

## Version history[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#version-history)

Version| Changes  
---|---  
`v14.1.0`| Custom `cacheHandler` is stable.  
`v13.0.0`| App Router is introduced.  
`v12.2.0`| Pages Router: On-Demand ISR is stable  
`v12.0.0`| Pages Router: [Bot-aware ISR fallback](https://nextjs.org/blog/next-12#bot-aware-isr-fallback) added.  
`v9.5.0`| Pages Router: [Stable ISR introduced](https://nextjs.org/blog/next-9-5).  
  
Was this helpful?

supported.

Send
