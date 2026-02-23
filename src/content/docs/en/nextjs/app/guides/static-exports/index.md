---
title: 'Guides: Static Exports'
description: 'Last updated February 20, 2026'
---

# Guides: Static Exports | Next.js

Source URL: https://nextjs.org/docs/app/guides/static-exports

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)Static Exports

Copy page

# How to create a static export of your Next.js application

Last updated February 20, 2026

Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.

When running `next build`, Next.js generates an HTML file per route. By breaking a strict SPA into individual HTML files, Next.js can avoid loading unnecessary JavaScript code on the client-side, reducing the bundle size and enabling faster page loads.

Since Next.js supports this static export, it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets.

## Configuration[](https://nextjs.org/docs/app/guides/static-exports#configuration)

To enable a static export, change the output mode inside `next.config.js`:

next.config.js
[code]
    /**
     * @type {import('next').NextConfig}
     */
    const nextConfig = {
      output: 'export',
     
      // Optional: Change links `/me` -> `/me/` and emit `/me.html` -> `/me/index.html`
      // trailingSlash: true,
     
      // Optional: Prevent automatic `/me` -> `/me/`, instead preserve `href`
      // skipTrailingSlashRedirect: true,
     
      // Optional: Change the output directory `out` -> `dist`
      // distDir: 'dist',
    }
     
    module.exports = nextConfig
[/code]

After running `next build`, Next.js will create an `out` folder with the HTML/CSS/JS assets for your application.

## Supported Features[](https://nextjs.org/docs/app/guides/static-exports#supported-features)

The core of Next.js has been designed to support static exports.

### Server Components[](https://nextjs.org/docs/app/guides/static-exports#server-components)

When you run `next build` to generate a static export, Server Components consumed inside the `app` directory will run during the build, similar to traditional static-site generation.

The resulting component will be rendered into static HTML for the initial page load and a static payload for client navigation between routes. No changes are required for your Server Components when using the static export, unless they consume [dynamic server functions](https://nextjs.org/docs/app/guides/static-exports#unsupported-features).

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      // This fetch will run on the server during `next build`
      const res = await fetch('https://api.example.com/...')
      const data = await res.json()
     
      return <main>...</main>
    }
[/code]

### Client Components[](https://nextjs.org/docs/app/guides/static-exports#client-components)

If you want to perform data fetching on the client, you can use a Client Component with [SWR](https://github.com/vercel/swr) to memoize requests.

app/other/page.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import useSWR from 'swr'
     
    const fetcher = (url: string) => fetch(url).then((r) => r.json())
     
    export default function Page() {
      const { data, error } = useSWR(
        `https://jsonplaceholder.typicode.com/posts/1`,
        fetcher
      )
      if (error) return 'Failed to load'
      if (!data) return 'Loading...'
     
      return data.title
    }
[/code]

Since route transitions happen client-side, this behaves like a traditional SPA. For example, the following index route allows you to navigate to different posts on the client:

app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <>
          <h1>Index Page</h1>
          <hr />
          <ul>
            <li>
              <Link href="/post/1">Post 1</Link>
            </li>
            <li>
              <Link href="/post/2">Post 2</Link>
            </li>
          </ul>
        </>
      )
    }
[/code]

### Image Optimization[](https://nextjs.org/docs/app/guides/static-exports#image-optimization)

[Image Optimization](https://nextjs.org/docs/app/api-reference/components/image) through `next/image` can be used with a static export by defining a custom image loader in `next.config.js`. For example, you can optimize images with a service like Cloudinary:

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      output: 'export',
      images: {
        loader: 'custom',
        loaderFile: './my-loader.ts',
      },
    }
     
    module.exports = nextConfig
[/code]

This custom loader will define how to fetch images from a remote source. For example, the following loader will construct the URL for Cloudinary:

my-loader.ts

JavaScriptTypeScript
[code]
    export default function cloudinaryLoader({
      src,
      width,
      quality,
    }: {
      src: string
      width: number
      quality?: number
    }) {
      const params = ['f_auto', 'c_limit', `w_${width}`, `q_${quality || 'auto'}`]
      return `https://res.cloudinary.com/demo/image/upload/${params.join(
        ','
      )}${src}`
    }
[/code]

You can then use `next/image` in your application, defining relative paths to the image in Cloudinary:

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return <Image alt="turtles" src="/turtles.jpg" width={300} height={300} />
    }
[/code]

### Route Handlers[](https://nextjs.org/docs/app/guides/static-exports#route-handlers)

Route Handlers will render a static response when running `next build`. Only the `GET` HTTP verb is supported. This can be used to generate static HTML, JSON, TXT, or other files from cached or uncached data. For example:

app/data.json/route.ts

JavaScriptTypeScript
[code]
    export async function GET() {
      return Response.json({ name: 'Lee' })
    }
[/code]

The above file `app/data.json/route.ts` will render to a static file during `next build`, producing `data.json` containing `{ name: 'Lee' }`.

If you need to read dynamic values from the incoming request, you cannot use a static export.

### Browser APIs[](https://nextjs.org/docs/app/guides/static-exports#browser-apis)

Client Components are pre-rendered to HTML during `next build`. Because [Web APIs](https://developer.mozilla.org/docs/Web/API) like `window`, `localStorage`, and `navigator` are not available on the server, you need to safely access these APIs only when running in the browser. For example:
[code]
    'use client';
     
    import { useEffect } from 'react';
     
    export default function ClientComponent() {
      useEffect(() => {
        // You now have access to `window`
        console.log(window.innerHeight);
      }, [])
     
      return ...;
    }
[/code]

## Unsupported Features[](https://nextjs.org/docs/app/guides/static-exports#unsupported-features)

Features that require a Node.js server, or dynamic logic that cannot be computed during the build process, are **not** supported:

  * [Dynamic Routes](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) with `dynamicParams: true`
  * [Dynamic Routes](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) without `generateStaticParams()`
  * [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) that rely on Request
  * [Cookies](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [Rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)
  * [Redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
  * [Headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)
  * [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  * [Incremental Static Regeneration](https://nextjs.org/docs/app/guides/incremental-static-regeneration)
  * [Image Optimization](https://nextjs.org/docs/app/api-reference/components/image) with the default `loader`
  * [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode)
  * [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data)
  * [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes)



Attempting to use any of these features with `next dev` will result in an error, similar to setting the [`dynamic`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) option to `error` in the root layout.
[code]
    export const dynamic = 'error'
[/code]

## Deploying[](https://nextjs.org/docs/app/guides/static-exports#deploying)

With a static export, Next.js can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets.

When running `next build`, Next.js generates the static export into the `out` folder. For example, let's say you have the following routes:

  * `/`
  * `/blog/[id]`



After running `next build`, Next.js will generate the following files:

  * `/out/index.html`
  * `/out/404.html`
  * `/out/blog/post-1.html`
  * `/out/blog/post-2.html`



If you are using a static host like Nginx, you can configure rewrites from incoming requests to the correct files:

nginx.conf
[code]
    server {
      listen 80;
      server_name acme.com;
     
      root /var/www/out;
     
      location / {
          try_files $uri $uri.html $uri/ =404;
      }
     
      # This is necessary when `trailingSlash: false`.
      # You can omit this when `trailingSlash: true`.
      location /blog/ {
          rewrite ^/blog/(.*)$ /blog/$1.html break;
      }
     
      error_page 404 /404.html;
      location = /404.html {
          internal;
      }
    }
[/code]

## Version History[](https://nextjs.org/docs/app/guides/static-exports#version-history)

Version| Changes  
---|---  
`v14.0.0`| `next export` has been removed in favor of `"output": "export"`  
`v13.4.0`| App Router (Stable) adds enhanced static export support, including using React Server Components and Route Handlers.  
`v13.3.0`| `next export` is deprecated and replaced with `"output": "export"`  
  
Was this helpful?

supported.

Send
