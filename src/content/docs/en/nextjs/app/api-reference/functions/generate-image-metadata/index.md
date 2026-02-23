---
title: 'Functions: generateImageMetadata'
description: 'Last updated February 20, 2026'
---

# Functions: generateImageMetadata | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)generateImageMetadata

Copy page

# generateImageMetadata

Last updated February 20, 2026

You can use `generateImageMetadata` to generate different versions of one image or return multiple images for one route segment. This is useful for when you want to avoid hard-coding metadata values, such as for icons.

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#parameters)

`generateImageMetadata` function accepts the following parameters:

#### `params` (optional)[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#params-optional)

An object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) object from the root segment down to the segment `generateImageMetadata` is called from.

icon.tsx

JavaScriptTypeScript
[code]
    export function generateImageMetadata({
      params,
    }: {
      params: { slug: string }
    }) {
      // ...
    }
[/code]

Route| URL| `params`  
---|---|---  
`app/shop/icon.js`| `/shop`| `undefined`  
`app/shop/[slug]/icon.js`| `/shop/1`| `{ slug: '1' }`  
`app/shop/[tag]/[item]/icon.js`| `/shop/1/2`| `{ tag: '1', item: '2' }`  
  
## Returns[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#returns)

The `generateImageMetadata` function should return an `array` of objects containing the image's metadata such as `alt` and `size`. In addition, each item **must** include an `id` value which will be passed as a promise to the props of the image generating function.

Image Metadata Object| Type  
---|---  
`id`| `string` (required)  
`alt`| `string`  
`size`| `{ width: number; height: number }`  
`contentType`| `string`  
  
icon.tsx

JavaScriptTypeScript
[code]
    import { ImageResponse } from 'next/og'
     
    export function generateImageMetadata() {
      return [
        {
          contentType: 'image/png',
          size: { width: 48, height: 48 },
          id: 'small',
        },
        {
          contentType: 'image/png',
          size: { width: 72, height: 72 },
          id: 'medium',
        },
      ]
    }
     
    export default async function Icon({ id }: { id: Promise<string | number> }) {
      const iconId = await id
      return new ImageResponse(
        (
          <div
            style={{
              width: '100%',
              height: '100%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: 88,
              background: '#000',
              color: '#fafafa',
            }}
          >
            Icon {iconId}
          </div>
        )
      )
    }
[/code]

## Image generation function props[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#image-generation-function-props)

When using `generateImageMetadata`, the default export image generation function receives the following props:

#### `id`[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#id)

A promise that resolves to the `id` value from one of the items returned by `generateImageMetadata`. The `id` will be a `string` or `number` depending on what was returned from `generateImageMetadata`.

icon.tsx

JavaScriptTypeScript
[code]
    export default async function Icon({ id }: { id: Promise<string | number> }) {
      const iconId = await id
      // Use iconId to generate the image
    }
[/code]

#### `params` (optional)[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#params-optional-1)

A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) from the root segment down to the segment the image is colocated in.

icon.tsx

JavaScriptTypeScript
[code]
    export default async function Icon({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      // Use slug to generate the image
    }
[/code]

### Examples[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#examples)

#### Using external data[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#using-external-data)

This example uses the `params` object and external data to generate multiple [Open Graph images](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image) for a route segment.

app/products/[id]/opengraph-image.tsx

JavaScriptTypeScript
[code]
    import { ImageResponse } from 'next/og'
    import { getCaptionForImage, getOGImages } from '@/app/utils/images'
     
    export async function generateImageMetadata({
      params,
    }: {
      params: { id: string }
    }) {
      const images = await getOGImages(params.id)
     
      return images.map((image, idx) => ({
        id: idx,
        size: { width: 1200, height: 600 },
        alt: image.text,
        contentType: 'image/png',
      }))
    }
     
    export default async function Image({
      params,
      id,
    }: {
      params: Promise<{ id: string }>
      id: Promise<number>
    }) {
      const productId = (await params).id
      const imageId = await id
      const text = await getCaptionForImage(productId, imageId)
     
      return new ImageResponse(
        (
          <div
            style={
              {
                // ...
              }
            }
          >
            {text}
          </div>
        )
      )
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#version-history)

Version| Changes  
---|---  
`v16.0.0`| `id` passed to the Image generation function is now a promise that resolves to `string` or `number`  
`v16.0.0`| `params` passed to the Image generation function is now a promise that resolves to an object  
`v13.3.0`| `generateImageMetadata` introduced.  
  
## Next Steps

View all the Metadata API options.

### [Metadata FilesAPI documentation for the metadata file conventions.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)

Was this helpful?

supported.

Send
