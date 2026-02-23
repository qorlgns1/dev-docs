---
title: 'Functions: generateViewport'
description: 'You can customize the initial viewport of the page with the static  object or the dynamic  function.'
---

# Functions: generateViewport | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/generate-viewport

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)generateViewport

Copy page

# generateViewport

Last updated February 20, 2026

You can customize the initial viewport of the page with the static `viewport` object or the dynamic `generateViewport` function.

> **Good to know** :
> 
>   * The `viewport` object and `generateViewport` function exports are **only supported in Server Components**.
>   * You cannot export both the `viewport` object and `generateViewport` function from the same route segment.
>   * If you're coming from migrating `metadata` exports, you can use [metadata-to-viewport-export codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#metadata-to-viewport-export) to update your changes.
> 


## The `viewport` object[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#the-viewport-object)

To define the viewport options, export a `viewport` object from a `layout.jsx` or `page.jsx` file.

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      themeColor: 'black',
    }
     
    export default function Page() {}
[/code]

## `generateViewport` function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#generateviewport-function)

`generateViewport` should return a [`Viewport` object](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-fields) containing one or more viewport fields.

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    export function generateViewport({ params }) {
      return {
        themeColor: '...',
      }
    }
[/code]

In TypeScript, the `params` argument can be typed via [`PageProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper) or [`LayoutProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper) depending on where `generateViewport` is defined.

> **Good to know** :
> 
>   * If the viewport doesn't depend on runtime information, it should be defined using the static [`viewport` object](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#the-viewport-object) rather than `generateViewport`.
> 


## Viewport Fields[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-fields)

### `themeColor`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#themecolor)

Learn more about [`theme-color`](https://developer.mozilla.org/docs/Web/HTML/Element/meta/name/theme-color).

**Simple theme color**

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      themeColor: 'black',
    }
[/code]

<head> output
[code]
    <meta name="theme-color" content="black" />
[/code]

**With media attribute**

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      themeColor: [
        { media: '(prefers-color-scheme: light)', color: 'cyan' },
        { media: '(prefers-color-scheme: dark)', color: 'black' },
      ],
    }
[/code]

<head> output
[code]
    <meta name="theme-color" media="(prefers-color-scheme: light)" content="cyan" />
    <meta name="theme-color" media="(prefers-color-scheme: dark)" content="black" />
[/code]

### `width`, `initialScale`, `maximumScale` and `userScalable`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#width-initialscale-maximumscale-and-userscalable)

> **Good to know** : The `viewport` meta tag is automatically set, and manual configuration is usually unnecessary as the default is sufficient. However, the information is provided for completeness.

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      width: 'device-width',
      initialScale: 1,
      maximumScale: 1,
      userScalable: false,
      // Also supported but less commonly used
      // interactiveWidget: 'resizes-visual',
    }
[/code]

<head> output
[code]
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
    />
[/code]

### `colorScheme`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#colorscheme)

Learn more about [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta/name#:~:text=color%2Dscheme%3A%20specifies,of%20the%20following%3A).

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      colorScheme: 'dark',
    }
[/code]

<head> output
[code]
    <meta name="color-scheme" content="dark" />
[/code]

## With Cache Components[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#with-cache-components)

When [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) is enabled, `generateViewport` follows the same rules as other components. If viewport accesses runtime data (`cookies()`, `headers()`, `params`, `searchParams`) or performs uncached data fetching, it defers to request time.

Unlike metadata, viewport cannot be streamed because it affects initial page load UI. If `generateViewport` defers to request time, the page would need to block until resolved.

If viewport depends on external data but not runtime data, use `use cache`:

app/layout.tsx
[code]
    export async function generateViewport() {
      'use cache'
      const { width, initialScale } = await db.query('viewport-size')
      return { width, initialScale }
    }
[/code]

If viewport genuinely requires runtime data, wrap the document `<body>` in a Suspense boundary to signal that the entire route should be dynamic:

app/layout.tsx
[code]
    import { Suspense } from 'react'
    import { cookies } from 'next/headers'
     
    export async function generateViewport() {
      const cookieJar = await cookies()
      return {
        themeColor: cookieJar.get('theme-color')?.value,
      }
    }
     
    export default function RootLayout({ children }) {
      return (
        <Suspense>
          <html>
            <body>{children}</body>
          </html>
        </Suspense>
      )
    }
[/code]

Caching is preferred because it allows static shell generation. Wrapping the document `body` in Suspense means there is no static shell or content to immediately send when a request arrives, making the entire route block until ready on every request.

> **Good to know** : Use [multiple root layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout) to isolate fully dynamic viewport to specific routes, while still letting other routes in your application generate a static shell.

## Types[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#types)

You can add type safety to your viewport object by using the `Viewport` type. If you are using the [built-in TypeScript plugin](https://nextjs.org/docs/app/api-reference/config/typescript) in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.

### `viewport` object[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-object)
[code] 
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      themeColor: 'black',
    }
[/code]

### `generateViewport` function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#generateviewport-function-1)

#### Regular function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#regular-function)
[code] 
    import type { Viewport } from 'next'
     
    export function generateViewport(): Viewport {
      return {
        themeColor: 'black',
      }
    }
[/code]

#### With segment props[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#with-segment-props)
[code] 
    import type { Viewport } from 'next'
     
    type Props = {
      params: Promise<{ id: string }>
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }
     
    export function generateViewport({ params, searchParams }: Props): Viewport {
      return {
        themeColor: 'black',
      }
    }
     
    export default function Page({ params, searchParams }: Props) {}
[/code]

#### JavaScript Projects[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#javascript-projects)

For JavaScript projects, you can use JSDoc to add type safety.
[code] 
    /** @type {import("next").Viewport} */
    export const viewport = {
      themeColor: 'black',
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#version-history)

Version| Changes  
---|---  
`v14.0.0`| `viewport` and `generateViewport` introduced.  
  
## Next Steps

View all the Metadata API options.

### [Metadata FilesAPI documentation for the metadata file conventions.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)### [Cache ComponentsLearn how to use Cache Components and combine the benefits of static and dynamic rendering.](https://nextjs.org/docs/app/getting-started/cache-components)### [cacheComponentsLearn how to enable the cacheComponents flag in Next.js.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)

Was this helpful?

supported.

Send
