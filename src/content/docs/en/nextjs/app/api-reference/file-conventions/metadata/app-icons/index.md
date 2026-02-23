---
title: 'Metadata Files: favicon, icon, and apple-icon'
description: 'Last updated February 20, 2026'
---

# Metadata Files: favicon, icon, and apple-icon | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons

[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)[Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)favicon, icon, and apple-icon

Copy page

# favicon, icon, and apple-icon

Last updated February 20, 2026

The `favicon`, `icon`, or `apple-icon` file conventions allow you to set icons for your application.

They are useful for adding app icons that appear in places like web browser tabs, phone home screens, and search engine results.

There are two ways to set app icons:

  * [Using image files (.ico, .jpg, .png)](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png)
  * [Using code to generate an icon (.js, .ts, .tsx)](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)



## Image files (.ico, .jpg, .png)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png)

Use an image file to set an app icon by placing a `favicon`, `icon`, or `apple-icon` image file within your `/app` directory. The `favicon` image can only be located in the top level of `app/`.

Next.js will evaluate the file and automatically add the appropriate tags to your app's `<head>` element.

File convention| Supported file types| Valid locations  
---|---|---  
[`favicon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)| `.ico`| `app/`  
[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)| `.ico`, `.jpg`, `.jpeg`, `.png`, `.svg`| `app/**/*`  
[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)| `.jpg`, `.jpeg`, `.png`| `app/**/*`  
  
### `favicon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)

Add a `favicon.ico` image file to the root `/app` route segment.

<head> output
[code]
    <link rel="icon" href="/favicon.ico" sizes="any" />
[/code]

### `icon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)

Add an `icon.(ico|jpg|jpeg|png|svg)` image file.

<head> output
[code]
    <link
      rel="icon"
      href="/icon?<generated>"
      type="image/<generated>"
      sizes="<generated>"
    />
[/code]

### `apple-icon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)

Add an `apple-icon.(jpg|jpeg|png)` image file.

<head> output
[code]
    <link
      rel="apple-touch-icon"
      href="/apple-icon?<generated>"
      type="image/<generated>"
      sizes="<generated>"
    />
[/code]

> **Good to know** :
> 
>   * You can set multiple icons by adding a number suffix to the file name. For example, `icon1.png`, `icon2.png`, etc. Numbered files will sort lexically.
>   * Favicons can only be set in the root `/app` segment. If you need more granularity, you can use [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon).
>   * The appropriate `<link>` tags and attributes such as `rel`, `href`, `type`, and `sizes` are determined by the icon type and metadata of the evaluated file.
>   * For example, a 32 by 32px `.png` file will have `type="image/png"` and `sizes="32x32"` attributes.
>   * `sizes="any"` is added to icons when the extension is `.svg` or the image size of the file is not determined. More details in this [favicon handbook](https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs).
> 


## Generate icons using code (.js, .ts, .tsx)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)

In addition to using [literal image files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png), you can programmatically **generate** icons using code.

Generate an app icon by creating an `icon` or `apple-icon` route that default exports a function.

File convention| Supported file types  
---|---  
`icon`| `.js`, `.ts`, `.tsx`  
`apple-icon`| `.js`, `.ts`, `.tsx`  
  
The easiest way to generate an icon is to use the [`ImageResponse`](https://nextjs.org/docs/app/api-reference/functions/image-response) API from `next/og`.

app/icon.tsx

JavaScriptTypeScript
[code]
    import { ImageResponse } from 'next/og'
     
    // Image metadata
    export const size = {
      width: 32,
      height: 32,
    }
    export const contentType = 'image/png'
     
    // Image generation
    export default function Icon() {
      return new ImageResponse(
        (
          // ImageResponse JSX element
          <div
            style={{
              fontSize: 24,
              background: 'black',
              width: '100%',
              height: '100%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: 'white',
            }}
          >
            A
          </div>
        ),
        // ImageResponse options
        {
          // For convenience, we can re-use the exported icons size metadata
          // config to also set the ImageResponse's width and height.
          ...size,
        }
      )
    }
[/code]

<head> output
[code]
    <link rel="icon" href="/icon?<generated>" type="image/png" sizes="32x32" />
[/code]

> **Good to know** :
> 
>   * By default, generated icons are [**statically optimized**](https://nextjs.org/docs/app/guides/caching#static-rendering) (generated at build time and cached) unless they use [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) or uncached data.
>   * You can generate multiple icons in the same file using [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata).
>   * You cannot generate a `favicon` icon. Use [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon) or a [favicon.ico](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon) file instead.
>   * App icons are special Route Handlers that are cached by default unless they use a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis) or [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) option.
> 


### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#props)

The default export function receives the following props:

#### `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#params-optional)

A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) object from the root segment down to the segment `icon` or `apple-icon` is colocated in.

> **Good to know** : If you use [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata), the function will also receive an `id` prop that is a promise resolving to the `id` value from one of the items returned by `generateImageMetadata`.

app/shop/[slug]/icon.tsx

JavaScriptTypeScript
[code]
    export default async function Icon({
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
`app/shop/icon.js`| `/shop`| `undefined`  
`app/shop/[slug]/icon.js`| `/shop/1`| `Promise<{ slug: '1' }>`  
`app/shop/[tag]/[item]/icon.js`| `/shop/1/2`| `Promise<{ tag: '1', item: '2' }>`  
  
### Returns[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#returns)

The default export function should return a `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response`.

> **Good to know** : `ImageResponse` satisfies this return type.

### Config exports[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#config-exports)

You can optionally configure the icon's metadata by exporting `size` and `contentType` variables from the `icon` or `apple-icon` route.

Option| Type  
---|---  
[`size`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#size)| `{ width: number; height: number }`  
[`contentType`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#contenttype)| `string` \- [image MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types#image_types)  
  
#### `size`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#size)

icon.tsx | apple-icon.tsx

JavaScriptTypeScript
[code]
    export const size = { width: 32, height: 32 }
     
    export default function Icon() {}
[/code]

<head> output
[code]
    <link rel="icon" sizes="32x32" />
[/code]

#### `contentType`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#contenttype)

icon.tsx | apple-icon.tsx

JavaScriptTypeScript
[code]
    export const contentType = 'image/png'
     
    export default function Icon() {}
[/code]

<head> output
[code]
    <link rel="icon" type="image/png" />
[/code]

#### Route Segment Config[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#route-segment-config)

`icon` and `apple-icon` are specialized [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) that can use the same [route segment configuration](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) options as Pages and Layouts.

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#version-history)

Version| Changes  
---|---  
`v16.0.0`| `params` is now a promise that resolves to an object  
`v13.3.0`| `favicon` `icon` and `apple-icon` introduced  
  
Was this helpful?

supported.

Send
