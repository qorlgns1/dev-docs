---
title: 'App Router: Glossary'
description: 'Last updated February 20, 2026'
---

# App Router: Glossary | Next.js

Source URL: https://nextjs.org/docs/app/glossary

[Next.js Docs](https://nextjs.org/docs)[App Router](https://nextjs.org/docs/app)Glossary

Copy page

# Next.js Glossary

Last updated February 20, 2026

# A[](https://nextjs.org/docs/app/glossary#a)

## App Router[](https://nextjs.org/docs/app/glossary#app-router)

The Next.js router introduced in version 13, built on top of React Server Components. It uses file-system based routing and supports layouts, nested routing, loading states, error handling, and more. Learn more in the [App Router documentation](https://nextjs.org/docs/app).

# B[](https://nextjs.org/docs/app/glossary#b)

## Build time[](https://nextjs.org/docs/app/glossary#build-time)

The stage when your application is being compiled. During build time, Next.js transforms your code into optimized files for production, generates static pages, and prepares assets for deployment. See the [`next build` CLI reference](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options).

# C[](https://nextjs.org/docs/app/glossary#c)

## Cache Components[](https://nextjs.org/docs/app/glossary#cache-components)

A feature that enables component and function-level caching using the [`"use cache"` directive](https://nextjs.org/docs/app/api-reference/directives/use-cache). Cache Components allows you to mix static, cached, and dynamic content within a single route by prerendering a static HTML shell that's served immediately, while dynamic content streams in when ready. Configure cache duration with [`cacheLife()`](https://nextjs.org/docs/app/api-reference/functions/cacheLife), tag cached data with [`cacheTag()`](https://nextjs.org/docs/app/api-reference/functions/cacheTag), and invalidate on-demand with [`updateTag()`](https://nextjs.org/docs/app/api-reference/functions/updateTag). Learn more in the [Cache Components guide](https://nextjs.org/docs/app/getting-started/cache-components).

## Catch-all Segments[](https://nextjs.org/docs/app/glossary#catch-all-segments)

Dynamic route segments that can match multiple URL parts using the `[...folder]/page.js` syntax. These segments capture all remaining URL segments and are useful for implementing features like documentation sites or file browsers. Learn more in [Dynamic Route Segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments).

## Client Bundles[](https://nextjs.org/docs/app/glossary#client-bundles)

JavaScript bundles sent to the browser. Next.js splits these automatically based on the [module graph](https://nextjs.org/docs/app/glossary#module-graph) to reduce initial payload size and load only the necessary code for each page.

## Client Component[](https://nextjs.org/docs/app/glossary#client-component)

A React component that runs in the browser. In Next.js, Client Components can also be rendered on the server during initial page generation. They can use state, effects, event handlers, and browser APIs, and are marked with the [`"use client"` directive](https://nextjs.org/docs/app/glossary#use-client-directive) at the top of a file. Learn more in [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components).

## Client-side navigation[](https://nextjs.org/docs/app/glossary#client-side-navigation)

A navigation technique where the page content updates dynamically without a full page reload. Next.js uses client-side navigation with the [`<Link>` component](https://nextjs.org/docs/app/api-reference/components/link), keeping shared layouts interactive and preserving browser state. Learn more in [Linking and Navigating](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions).

## Code Splitting[](https://nextjs.org/docs/app/glossary#code-splitting)

The process of dividing your application into smaller JavaScript chunks based on routes. Instead of loading all code upfront, only the code needed for the current route is loaded, reducing initial load time. Next.js automatically performs code splitting based on routes. Learn more in the [Package Bundling guide](https://nextjs.org/docs/app/guides/package-bundling).

# D[](https://nextjs.org/docs/app/glossary#d)

## Dynamic rendering[](https://nextjs.org/docs/app/glossary#dynamic-rendering)

See [Request-time rendering](https://nextjs.org/docs/app/glossary#request-time-rendering).

## Dynamic route segments[](https://nextjs.org/docs/app/glossary#dynamic-route-segments)

[Route segments](https://nextjs.org/docs/app/glossary#route-segment) that are generated from data at request time. Created by wrapping a folder name in square brackets (e.g., `[slug]`), they allow you to create routes from dynamic data like blog posts or product pages. Learn more in [Dynamic Route Segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes).

# E[](https://nextjs.org/docs/app/glossary#e)

## Environment Variables[](https://nextjs.org/docs/app/glossary#environment-variables)

Configuration values accessible at build time or request time. In Next.js, variables prefixed with `NEXT_PUBLIC_` are exposed to the browser, while others are only available server-side. Learn more in [Environment Variables](https://nextjs.org/docs/app/guides/environment-variables).

## Error Boundary[](https://nextjs.org/docs/app/glossary#error-boundary)

A React component that catches JavaScript errors in its child component tree and displays a fallback UI. In Next.js, create an [`error.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/error) to automatically wrap a route segment in an error boundary. Learn more in [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling).

# F[](https://nextjs.org/docs/app/glossary#f)

## Font Optimization[](https://nextjs.org/docs/app/glossary#font-optimization)

Automatic font optimization using [`next/font`](https://nextjs.org/docs/app/api-reference/components/font). Next.js self-hosts fonts, eliminates layout shift, and applies best practices for performance. Works with Google Fonts and local font files. Learn more in [Fonts](https://nextjs.org/docs/app/getting-started/fonts).

## File-system caching[](https://nextjs.org/docs/app/glossary#file-system-caching)

A Turbopack feature that stores compiler artifacts on disk between runs, reducing work across `next dev` or `next build` commands for significantly faster compile times. Learn more in [Turbopack FileSystem Caching](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache).

# H[](https://nextjs.org/docs/app/glossary#h)

## Hydration[](https://nextjs.org/docs/app/glossary#hydration)

React's process of attaching event handlers to the DOM to make server-rendered static HTML interactive. During hydration, React reconciles the server-rendered markup with the client-side JavaScript. Learn more in [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs).

# I[](https://nextjs.org/docs/app/glossary#i)

## Import Aliases[](https://nextjs.org/docs/app/glossary#import-aliases)

Custom path mappings that provide shorthand references for frequently used directories. Import aliases reduce the complexity of relative imports and make code more readable and maintainable. Learn more in [Absolute Imports and Module Path Aliases](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases).

## Incremental Static Regeneration (ISR)[](https://nextjs.org/docs/app/glossary#incremental-static-regeneration-isr)

A technique that allows you to update static content without rebuilding the entire site. ISR enables you to use static generation on a per-page basis while revalidating pages in the background as traffic comes in. Learn more in the [ISR guide](https://nextjs.org/docs/app/guides/incremental-static-regeneration).

> **Good to know** : In Next.js, ISR is also known as [Revalidation](https://nextjs.org/docs/app/glossary#revalidation).

## Intercepting Routes[](https://nextjs.org/docs/app/glossary#intercepting-routes)

A routing pattern that allows loading a route from another part of your application within the current layout. Useful for displaying content (like modals) without the user switching context, while keeping the URL shareable. Learn more in [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes).

## Image Optimization[](https://nextjs.org/docs/app/glossary#image-optimization)

Automatic image optimization using the [`<Image>` component](https://nextjs.org/docs/app/api-reference/components/image). Next.js optimizes images on-demand, serves them in modern formats like WebP, and automatically handles lazy loading and responsive sizing. Learn more in [Images](https://nextjs.org/docs/app/getting-started/images).

# L[](https://nextjs.org/docs/app/glossary#l)

## Layout[](https://nextjs.org/docs/app/glossary#layout)

UI that is shared between multiple pages. Layouts preserve state, remain interactive, and do not re-render on navigation. Defined by exporting a React component from a [`layout.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/layout). Learn more in [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages).

## Loading UI[](https://nextjs.org/docs/app/glossary#loading-ui)

Fallback UI shown while a [route segment](https://nextjs.org/docs/app/glossary#route-segment) is loading. Created by adding a [`loading.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/loading) to a folder, which automatically wraps the page in a [Suspense boundary](https://nextjs.org/docs/app/glossary#suspense-boundary). Learn more in [Loading UI](https://nextjs.org/docs/app/api-reference/file-conventions/loading).

# M[](https://nextjs.org/docs/app/glossary#m)

## Module Graph[](https://nextjs.org/docs/app/glossary#module-graph)

A graph of file dependencies in your app. Each file (module) is a node, and import/export relationships form the edges. Next.js analyzes this graph to determine optimal bundling and code-splitting strategies. Learn more in [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#reducing-js-bundle-size).

## Metadata[](https://nextjs.org/docs/app/glossary#metadata)

Information about a page used by browsers and search engines, such as title, description, and Open Graph images. In Next.js, define metadata using the [`metadata` export](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) or [`generateMetadata` function](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) in layout or page files. Learn more in [Metadata and OG Images](https://nextjs.org/docs/app/getting-started/metadata-and-og-images).

## Memoization[](https://nextjs.org/docs/app/glossary#memoization)

Caching the return value of a function so that calling the same function multiple times during a render pass (request) only executes it once. In Next.js, fetch requests with the same URL and options are automatically memoized. Learn more about [React Cache](https://react.dev/reference/react/cache).

## Middleware[](https://nextjs.org/docs/app/glossary#middleware)

See [Proxy](https://nextjs.org/docs/app/glossary#proxy).

# N[](https://nextjs.org/docs/app/glossary#n)

## Not Found[](https://nextjs.org/docs/app/glossary#not-found)

A special component shown when a route doesn't exist or when the [`notFound()` function](https://nextjs.org/docs/app/api-reference/functions/not-found) is called. Created by adding a [`not-found.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) to your app directory. Learn more in [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling#not-found).

# P[](https://nextjs.org/docs/app/glossary#p)

## Private Folders[](https://nextjs.org/docs/app/glossary#private-folders)

Folders prefixed with an underscore (e.g., `_components`) that are excluded from the routing system. These folders are used for code organization and shared utilities without creating accessible routes. Learn more in [Private Folders](https://nextjs.org/docs/app/getting-started/project-structure#private-folders).

## Page[](https://nextjs.org/docs/app/glossary#page)

UI that is unique to a route. Defined by exporting a React component from a [`page.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/page) within the `app` directory. Learn more in [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages).

## Parallel Routes[](https://nextjs.org/docs/app/glossary#parallel-routes)

A pattern that allows simultaneously or conditionally rendering multiple pages within the same layout. Created using named slots with the `@folder` convention, useful for dashboards, modals, and complex layouts. Learn more in [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes).

## Partial Prerendering (PPR)[](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr)

A rendering optimization that combines static and dynamic rendering in a single route. The static shell is served immediately while dynamic content streams in when ready, providing the best of both rendering strategies. Learn more in [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components).

## Prefetching[](https://nextjs.org/docs/app/glossary#prefetching)

Loading a route in the background before the user navigates to it. Next.js automatically prefetches routes linked with the [`<Link>` component](https://nextjs.org/docs/app/api-reference/components/link) when they enter the viewport, making navigation feel instant. Learn more in the [Prefetching guide](https://nextjs.org/docs/app/guides/prefetching).

## Prerendering[](https://nextjs.org/docs/app/glossary#prerendering)

When a component is rendered at [build time](https://nextjs.org/docs/app/glossary#build-time) or in the background during [revalidation](https://nextjs.org/docs/app/glossary#revalidation). The result is HTML and [RSC Payload](https://nextjs.org/docs/app/glossary#rsc-payload), which can be cached and served from a CDN. Prerendering is the default for components that don't use [Request-time APIs](https://nextjs.org/docs/app/glossary#request-time-apis).

## Proxy[](https://nextjs.org/docs/app/glossary#proxy)

A file ([`proxy.js`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)) that runs code on the server before request is completed. Used to implement server-side logic like logging, redirects, and rewrites. Formerly known as Middleware. Learn more in the [Proxy guide](https://nextjs.org/docs/app/getting-started/proxy).

# R[](https://nextjs.org/docs/app/glossary#r)

## Redirect[](https://nextjs.org/docs/app/glossary#redirect)

Sending users from one URL to another. In Next.js, redirects can be configured in [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects), returned from [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy), or triggered programmatically with the [`redirect()` function](https://nextjs.org/docs/app/api-reference/functions/redirect). Learn more in [Redirecting](https://nextjs.org/docs/app/guides/redirecting).

## Request time[](https://nextjs.org/docs/app/glossary#request-time)

The time when a user makes a request to your application. At request time, dynamic routes are rendered, cookies and headers are accessible, and request-specific data can be used.

## Request-time APIs[](https://nextjs.org/docs/app/glossary#request-time-apis)

Functions that access request-specific data, causing a component to opt into [request-time rendering](https://nextjs.org/docs/app/glossary#request-time-rendering). These include:

  * [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies) \- Access request cookies
  * [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers) \- Access request headers
  * [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) \- Access URL query parameters
  * [`draftMode()`](https://nextjs.org/docs/app/api-reference/functions/draft-mode) \- Enable or check draft mode



## Request-time rendering[](https://nextjs.org/docs/app/glossary#request-time-rendering)

When a component is rendered at [request time](https://nextjs.org/docs/app/glossary#request-time) rather than [build time](https://nextjs.org/docs/app/glossary#build-time). A component becomes dynamic when it uses [Request-time APIs](https://nextjs.org/docs/app/glossary#request-time-apis).

## Revalidation[](https://nextjs.org/docs/app/glossary#revalidation)

The process of updating cached data. Can be time-based (using [`cacheLife()`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) to set cache duration) or on-demand (using [`cacheTag()`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) to tag data, then [`updateTag()`](https://nextjs.org/docs/app/api-reference/functions/updateTag) to invalidate). Learn more in [Caching and Revalidating](https://nextjs.org/docs/app/getting-started/caching-and-revalidating).

## Rewrite[](https://nextjs.org/docs/app/glossary#rewrite)

Mapping an incoming request path to a different destination path without changing the URL in the browser. Configured in [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) or returned from [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy). Useful for proxying to external services or legacy URLs.

## Route Groups[](https://nextjs.org/docs/app/glossary#route-groups)

A way to organize routes without affecting the URL structure. Created by wrapping a folder name in parentheses (e.g., `(marketing)`), route groups help organize related routes and enable per-group [layouts](https://nextjs.org/docs/app/glossary#layout). Learn more in [Route Groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups).

## Route Handler[](https://nextjs.org/docs/app/glossary#route-handler)

A function that handles HTTP requests for a specific route, defined in a [`route.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/route). Route Handlers use the Web Request and Response APIs and can handle `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS` methods. Learn more in [Route Handlers](https://nextjs.org/docs/app/getting-started/route-handlers).

## Route Segment[](https://nextjs.org/docs/app/glossary#route-segment)

A part of the URL path (between two slashes) defined by a folder in the `app` directory. Each folder represents a segment in the URL structure. Learn more in [Project Structure](https://nextjs.org/docs/app/getting-started/project-structure).

## RSC Payload[](https://nextjs.org/docs/app/glossary#rsc-payload)

The React Server Component Payload—a compact binary representation of the rendered React Server Components tree. Contains the rendered result of Server Components, placeholders for Client Components, and props passed between them. Learn more in [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs).

# S[](https://nextjs.org/docs/app/glossary#s)

## Server Component[](https://nextjs.org/docs/app/glossary#server-component)

The default component type in the App Router. Server Components render on the server, can fetch data directly, and don't add to the client JavaScript bundle. They cannot use state or browser APIs. Learn more in [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components).

## Server Action[](https://nextjs.org/docs/app/glossary#server-action)

A [Server Function](https://nextjs.org/docs/app/glossary#server-function) that is passed to a Client Component as a prop or bound to a form action. Server Actions are commonly used for form submissions and data mutations. Learn more in [Server Actions and Mutations](https://nextjs.org/docs/app/getting-started/updating-data).

## Server Function[](https://nextjs.org/docs/app/glossary#server-function)

An asynchronous function that runs on the server, marked with the [`"use server"` directive](https://nextjs.org/docs/app/api-reference/directives/use-server). Server Functions can be invoked from Client Components. When passed as a prop to a Client Component or bound to a form action, they are called [Server Actions](https://nextjs.org/docs/app/glossary#server-action). Learn more in [React Server Functions](https://react.dev/reference/rsc/server-functions).

## Static Export[](https://nextjs.org/docs/app/glossary#static-export)

A deployment mode that generates a fully static site with HTML, CSS, and JavaScript files. Enabled by setting `output: 'export'` in `next.config.js`. Static exports can be hosted on any static file server without a Node.js server. Learn more in [Static Exports](https://nextjs.org/docs/app/guides/static-exports).

## Static rendering[](https://nextjs.org/docs/app/glossary#static-rendering)

See [Prerendering](https://nextjs.org/docs/app/glossary#prerendering).

## Static Assets[](https://nextjs.org/docs/app/glossary#static-assets)

Files such as images, fonts, videos, and other media that are served directly without processing. Static assets are typically stored in the `public` directory and referenced by their relative paths. Learn more in [Static Assets](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder).

## Static Shell[](https://nextjs.org/docs/app/glossary#static-shell)

The prerendered HTML structure of a page that's served immediately to the browser. With [Partial Prerendering](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr), the static shell includes all statically renderable content plus [Suspense boundary](https://nextjs.org/docs/app/glossary#suspense-boundary) fallbacks for dynamic content that streams in later.

## Streaming[](https://nextjs.org/docs/app/glossary#streaming)

A technique that allows the server to send parts of a page to the client as they become ready, rather than waiting for the entire page to render. Enabled automatically with [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) or manual `<Suspense>` boundaries. Learn more in [Linking and Navigating - Streaming](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming).

## Suspense boundary[](https://nextjs.org/docs/app/glossary#suspense-boundary)

A React [`<Suspense>`](https://react.dev/reference/react/Suspense) component that wraps async content and displays fallback UI while it loads. In Next.js, Suspense boundaries define where the [static shell](https://nextjs.org/docs/app/glossary#static-shell) ends and [streaming](https://nextjs.org/docs/app/glossary#streaming) begins, enabling [Partial Prerendering](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr).

# T[](https://nextjs.org/docs/app/glossary#t)

## Turbopack[](https://nextjs.org/docs/app/glossary#turbopack)

A fast, Rust-based bundler built for Next.js. Turbopack is the default bundler for `next dev` and available for `next build`. It provides significantly faster compilation times compared to Webpack. Learn more in [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack).

## Tree Shaking[](https://nextjs.org/docs/app/glossary#tree-shaking)

The process of removing unused code from your JavaScript bundles during the build process. Next.js automatically tree-shakes your code to reduce bundle sizes. Learn more in the [Package Bundling guide](https://nextjs.org/docs/app/guides/package-bundling).

# U[](https://nextjs.org/docs/app/glossary#u)

## `"use cache"` Directive[](https://nextjs.org/docs/app/glossary#use-cache-directive)

A directive that marks a component or function as cacheable. It can be placed at the top of a file to indicate that all exports in the file are cacheable, or inline at the top of a function or component to mark that specific scope as cacheable. Learn more in the [`"use cache"` reference](https://nextjs.org/docs/app/api-reference/directives/use-cache).

## `"use client"` Directive[](https://nextjs.org/docs/app/glossary#use-client-directive)

A special React directive that marks the boundary between server and client code. It must be placed at the top of a file, before any imports or other code. It indicates that React Components, helper functions, variable declarations, and all imported dependencies should be included in the [client bundle](https://nextjs.org/docs/app/glossary#client-bundles). Learn more in the [`"use client"` reference](https://nextjs.org/docs/app/api-reference/directives/use-client).

## `"use server"` Directive[](https://nextjs.org/docs/app/glossary#use-server-directive)

A directive that marks a function as a [Server Function](https://nextjs.org/docs/app/glossary#server-function) that can be called from client-side code. It can be placed at the top of a file to indicate that all exports in the file are Server Functions, or inline at the top of a function to mark that specific function. Learn more in the [`"use server"` reference](https://nextjs.org/docs/app/api-reference/directives/use-server).

# V[](https://nextjs.org/docs/app/glossary#v)

## Version skew[](https://nextjs.org/docs/app/glossary#version-skew)

After a new version of your application is deployed, clients that are still active may reference JavaScript, CSS, or data from an older build. This mismatch between client and server versions is called version skew, and it can cause missing assets, Server Action errors, and navigation failures. Next.js uses [`deploymentId`](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId) to detect and handle version skew. Learn more in [Self-Hosting - Version Skew](https://nextjs.org/docs/app/guides/self-hosting#version-skew).

Was this helpful?

supported.

Send
