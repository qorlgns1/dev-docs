---
title: 'Getting Started: Image Optimization'
description: 'The Next.js  component extends the HTML  element to provide:'
---

# Getting Started: Image Optimization | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/images

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Image Optimization

Copy page

# Image Optimization

Last updated February 20, 2026

The Next.js [`<Image>`](https://nextjs.org/docs/app/api-reference/components/image) component extends the HTML `<img>` element to provide:

  * **Size optimization:** Automatically serving correctly sized images for each device, using modern image formats like WebP.
  * **Visual stability:** Preventing [layout shift](https://web.dev/articles/cls) automatically when images are loading.
  * **Faster page loads:** Only loading images when they enter the viewport using native browser lazy loading, with optional blur-up placeholders.
  * **Asset flexibility:** Resizing images on-demand, even images stored on remote servers.



To start using `<Image>`, import it from `next/image` and render it within your component.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return <Image src="" alt="" />
    }
[/code]

The `src` property can be a [local](https://nextjs.org/docs/app/getting-started/images#local-images) or [remote](https://nextjs.org/docs/app/getting-started/images#remote-images) image.

> **🎥 Watch:** Learn more about how to use `next/image` → [YouTube (9 minutes)](https://youtu.be/IU_qq_c_lKA).

## Local images[](https://nextjs.org/docs/app/getting-started/images#local-images)

You can store static files, like images and fonts, under a folder called [`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return (
        <Image
          src="/profile.png"
          alt="Picture of the author"
          width={500}
          height={500}
        />
      )
    }
[/code]

If the image is statically imported, Next.js will automatically determine the intrinsic [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height) and [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height). These values are used to determine the image ratio and prevent [Cumulative Layout Shift](https://web.dev/articles/cls) while your image is loading.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
    import ProfileImage from './profile.png'
     
    export default function Page() {
      return (
        <Image
          src={ProfileImage}
          alt="Picture of the author"
          // width={500} automatically provided
          // height={500} automatically provided
          // blurDataURL="data:..." automatically provided
          // placeholder="blur" // Optional blur-up while loading
        />
      )
    }
[/code]

## Remote images[](https://nextjs.org/docs/app/getting-started/images#remote-images)

To use a remote image, you can provide a URL string for the `src` property.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return (
        <Image
          src="https://s3.amazonaws.com/my-bucket/profile.png"
          alt="Picture of the author"
          width={500}
          height={500}
        />
      )
    }
[/code]

Since Next.js does not have access to remote files during the build process, you'll need to provide the [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height) and optional [`blurDataURL`](https://nextjs.org/docs/app/api-reference/components/image#blurdataurl) props manually. The `width` and `height` are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in. Alternatively, you can use the [`fill` property](https://nextjs.org/docs/app/api-reference/components/image#fill) to make the image fill the size of the parent element.

To safely allow images from remote servers, you need to define a list of supported URL patterns in [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js). Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      images: {
        remotePatterns: [
          {
            protocol: 'https',
            hostname: 's3.amazonaws.com',
            port: '',
            pathname: '/my-bucket/**',
            search: '',
          },
        ],
      },
    }
     
    export default config
[/code]

## API Reference

See the API Reference for the full feature set of Next.js Image.

### [Image ComponentOptimize Images in your Next.js Application using the built-in `next/image` Component.](https://nextjs.org/docs/app/api-reference/components/image)

Was this helpful?

supported.

Send
