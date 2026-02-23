---
title: 'Metadata Files: opengraph-image and twitter-image'
description: 'Last updated February 20, 2026'
---

# Metadata Files: opengraph-image and twitter-image | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image

[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)[Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)opengraph-image and twitter-image

Copy page

# opengraph-image and twitter-image

Last updated February 20, 2026

The `opengraph-image` and `twitter-image` file conventions allow you to set Open Graph and Twitter images for a route segment.

They are useful for setting the images that appear on social networks and messaging apps when a user shares a link to your site.

There are two ways to set Open Graph and Twitter images:

  * [Using image files (.jpg, .png, .gif)](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif)
  * [Using code to generate images (.js, .ts, .tsx)](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)



## Image files (.jpg, .png, .gif)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif)

Use an image file to set a route segment's shared image by placing an `opengraph-image` or `twitter-image` image file in the segment.

Next.js will evaluate the file and automatically add the appropriate tags to your app's `<head>` element.

File convention| Supported file types  
---|---  
[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)| `.jpg`, `.jpeg`, `.png`, `.gif`  
[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)| `.jpg`, `.jpeg`, `.png`, `.gif`  
[`opengraph-image.alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-imagealttxt)| `.txt`  
[`twitter-image.alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-imagealttxt)| `.txt`  
  
> **Good to know** :
> 
> The `twitter-image` file size must not exceed [5MB](https://developer.x.com/en/docs/x-for-websites/cards/overview/summary), and the `opengraph-image` file size must not exceed [8MB](https://developers.facebook.com/docs/sharing/webmasters/images). If the image file size exceeds these limits, the build will fail.

### `opengraph-image`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)

Add an `opengraph-image.(jpg|jpeg|png|gif)` image file to any route segment.

<head> output
[code]
    <meta property="og:image" content="<generated>" />
    <meta property="og:image:type" content="<generated>" />
    <meta property="og:image:width" content="<generated>" />
    <meta property="og:image:height" content="<generated>" />
[/code]

### `twitter-image`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)

Add a `twitter-image.(jpg|jpeg|png|gif)` image file to any route segment.

<head> output
[code]
    <meta name="twitter:image" content="<generated>" />
    <meta name="twitter:image:type" content="<generated>" />
    <meta name="twitter:image:width" content="<generated>" />
    <meta name="twitter:image:height" content="<generated>" />
[/code]

### `opengraph-image.alt.txt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-imagealttxt)

Add an accompanying `opengraph-image.alt.txt` file in the same route segment as the `opengraph-image.(jpg|jpeg|png|gif)` image it's alt text.

opengraph-image.alt.txt
[code]
    About Acme
[/code]

<head> output
[code]
    <meta property="og:image:alt" content="About Acme" />
[/code]

### `twitter-image.alt.txt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-imagealttxt)

Add an accompanying `twitter-image.alt.txt` file in the same route segment as the `twitter-image.(jpg|jpeg|png|gif)` image it's alt text.

twitter-image.alt.txt
[code]
    About Acme
[/code]

<head> output
[code]
    <meta property="twitter:image:alt" content="About Acme" />
[/code]

## Generate images using code (.js, .ts, .tsx)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)

In addition to using [literal image files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif), you can programmatically **generate** images using code.

Generate a route segment's shared image by creating an `opengraph-image` or `twitter-image` route that default exports a function.

File convention| Supported file types  
---|---  
`opengraph-image`| `.js`, `.ts`, `.tsx`  
`twitter-image`| `.js`, `.ts`, `.tsx`  
  
> **Good to know** :
> 
>   * By default, generated images are [**statically optimized**](https://nextjs.org/docs/app/guides/caching#static-rendering) (generated at build time and cached) unless they use [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) or uncached data.
>   * You can generate multiple Images in the same file using [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata).
>   * `opengraph-image.js` and `twitter-image.js` are special Route Handlers that is cached by default unless it uses a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis) or [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) option.
> 


The easiest way to generate an image is to use the [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response) API from `next/og`.

app/about/opengraph-image.tsx

JavaScriptTypeScript
[code]
    import { ImageResponse } from 'next/og'
    import { readFile } from 'node:fs/promises'
    import { join } from 'node:path'
     
    // Image metadata
    export const alt = 'About Acme'
    export const size = {
      width: 1200,
      height: 630,
    }
     
    export const contentType = 'image/png'
     
    // Image generation
    export default async function Image() {
      // Font loading, process.cwd() is Next.js project directory
      const interSemiBold = await readFile(
        join(process.cwd(), 'assets/Inter-SemiBold.ttf')
      )
     
      return new ImageResponse(
        (
          // ImageResponse JSX element
          <div
            style={{
              fontSize: 128,
              background: 'white',
              width: '100%',
              height: '100%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            About Acme
          </div>
        ),
        // ImageResponse options
        {
          // For convenience, we can re-use the exported opengraph-image
          // size config to also set the ImageResponse's width and height.
          ...size,
          fonts: [
            {
              name: 'Inter',
              data: interSemiBold,
              style: 'normal',
              weight: 400,
            },
          ],
        }
      )
    }
[/code]

<head> output
[code]
    <meta property="og:image" content="<generated>" />
    <meta property="og:image:alt" content="About Acme" />
    <meta property="og:image:type" content="image/png" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
[/code]

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#props)

The default export function receives the following props:

#### `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#params-optional)

A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) object from the root segment down to the segment `opengraph-image` or `twitter-image` is colocated in.

> **Good to know** : If you use [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata), the function will also receive an `id` prop that is a promise resolving to the `id` value from one of the items returned by `generateImageMetadata`.

app/shop/[slug]/opengraph-image.tsx

JavaScriptTypeScript
[code]
    export default async function Image({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      // ...
    }
[/code]

Route| URL| `params`  
---|---|---  
`app/shop/opengraph-image.js`| `/shop`| `undefined`  
`app/shop/[slug]/opengraph-image.js`| `/shop/1`| `Promise<{ slug: '1' }>`  
`app/shop/[tag]/[item]/opengraph-image.js`| `/shop/1/2`| `Promise<{ tag: '1', item: '2' }>`  
  
### Returns[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#returns)

The default export function should return a `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response`.

> **Good to know** : `ImageResponse` satisfies this return type.

### Config exports[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#config-exports)

You can optionally configure the image's metadata by exporting `alt`, `size`, and `contentType` variables from `opengraph-image` or `twitter-image` route.

Option| Type  
---|---  
[`alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#alt)| `string`  
[`size`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#size)| `{ width: number; height: number }`  
[`contentType`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#contenttype)| `string` \- [image MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types#image_types)  
  
#### `alt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#alt)

opengraph-image.tsx | twitter-image.tsx

JavaScriptTypeScript
[code]
    export const alt = 'My images alt text'
     
    export default function Image() {}
[/code]

<head> output
[code]
    <meta property="og:image:alt" content="My images alt text" />
[/code]

#### `size`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#size)

opengraph-image.tsx | twitter-image.tsx

JavaScriptTypeScript
[code]
    export const size = { width: 1200, height: 630 }
     
    export default function Image() {}
[/code]

<head> output
[code]
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
[/code]

#### `contentType`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#contenttype)

opengraph-image.tsx | twitter-image.tsx

JavaScriptTypeScript
[code]
    export const contentType = 'image/png'
     
    export default function Image() {}
[/code]

<head> output
[code]
    <meta property="og:image:type" content="image/png" />
[/code]

#### Route Segment Config[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#route-segment-config)

`opengraph-image` and `twitter-image` are specialized [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) that can use the same [route segment configuration](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) options as Pages and Layouts.

### Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#examples)

#### Using external data[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#using-external-data)

This example uses the `params` object and external data to generate the image.

> **Good to know** : By default, this generated image will be [statically optimized](https://nextjs.org/docs/app/guides/caching#static-rendering). You can configure the individual `fetch` [`options`](https://nextjs.org/docs/app/api-reference/functions/fetch) or route segments [options](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate) to change this behavior.

app/posts/[slug]/opengraph-image.tsx

JavaScriptTypeScript
[code]
    import { ImageResponse } from 'next/og'
     
    export const alt = 'About Acme'
    export const size = {
      width: 1200,
      height: 630,
    }
    export const contentType = 'image/png'
     
    export default async function Image({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      const post = await fetch(`https://.../posts/${slug}`).then((res) =>
        res.json()
      )
     
      return new ImageResponse(
        (
          <div
            style={{
              fontSize: 48,
              background: 'white',
              width: '100%',
              height: '100%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {post.title}
          </div>
        ),
        {
          ...size,
        }
      )
    }
[/code]

#### Using Node.js runtime with local assets[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#using-nodejs-runtime-with-local-assets)

These examples use the Node.js runtime to fetch a local image from the file system and pass it to the `<img>` `src` attribute, either as a base64 string or an `ArrayBuffer`. Place the local asset relative to the project root, not the example source file.

app/opengraph-image.tsx

JavaScriptTypeScript
[code]
    import { ImageResponse } from 'next/og'
    import { join } from 'node:path'
    import { readFile } from 'node:fs/promises'
     
    export default async function Image() {
      const logoData = await readFile(join(process.cwd(), 'logo.png'), 'base64')
      const logoSrc = `data:image/png;base64,${logoData}`
     
      return new ImageResponse(
        (
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <img src={logoSrc} height="100" />
          </div>
        )
      )
    }
[/code]

Passing an `ArrayBuffer` to the `src` attribute of an `<img>` element is not part of the HTML spec. The rendering engine used by `next/og` supports it, but because TypeScript definitions follow the spec, you need a `@ts-expect-error` directive or similar to use this [feature](https://github.com/vercel/satori/issues/606#issuecomment-2144000453).

app/opengraph-image.tsx

JavaScriptTypeScript
[code]
    import { ImageResponse } from 'next/og'
    import { join } from 'node:path'
    import { readFile } from 'node:fs/promises'
     
    export default async function Image() {
      const logoData = await readFile(join(process.cwd(), 'logo.png'))
      const logoSrc = Uint8Array.from(logoData).buffer
     
      return new ImageResponse(
        (
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {/* @ts-expect-error Satori accepts ArrayBuffer/typed arrays for <img src> at runtime */}
            <img src={logoSrc} height="100" />
          </div>
        )
      )
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#version-history)

Version| Changes  
---|---  
`v16.0.0`| `params` is now a promise that resolves to an object  
`v13.3.0`| `opengraph-image` and `twitter-image` introduced.  
  
Was this helpful?

supported.

Send
