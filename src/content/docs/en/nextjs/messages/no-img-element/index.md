---
title: 'No img element'
description: '> Prevent usage of  element due to slower LCP and higher bandwidth.'
---

# No img element | Next.js

Source URL: https://nextjs.org/docs/messages/no-img-element

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No img element

# No img element

> Prevent usage of `<img>` element due to slower LCP and higher bandwidth.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-img-element#why-this-error-occurred)

An `<img>` element was used to display an image instead of `<Image />` from `next/image`.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-img-element#possible-ways-to-fix-it)

  1. Use [`next/image`](https://nextjs.org/docs/pages/api-reference/components/image) to improve performance with automatic [Image Optimization](https://nextjs.org/docs/pages/api-reference/components/image).



> **Note** : If deploying to a [managed hosting provider](https://nextjs.org/docs/pages/getting-started/deploying), remember to check provider pricing since optimized images might be charged differently than the original images.
> 
> Common image optimization platform pricing:
> 
>   * [Vercel pricing](https://vercel.com/pricing)
>   * [Cloudinary pricing](https://cloudinary.com/pricing)
>   * [imgix pricing](https://imgix.com/pricing)
> 


> **Note** : If self-hosting, remember to install [`sharp`](https://www.npmjs.com/package/sharp) and check if your server has enough storage to cache the optimized images.

pages/index.js
[code]
    import Image from 'next/image'
     
    function Home() {
      return (
        <Image
          src="https://example.com/hero.jpg"
          alt="Landscape picture"
          width={800}
          height={500}
        />
      )
    }
     
    export default Home
[/code]

  2. If you would like to use `next/image` features such as blur-up placeholders but disable Image Optimization, you can do so using [unoptimized](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized):



pages/index.js
[code]
    import Image from 'next/image'
     
    const UnoptimizedImage = (props) => {
      return <Image {...props} unoptimized />
    }
[/code]

  3. You can also use the `<picture>` element with the nested `<img>` element:



pages/index.js
[code]
    function Home() {
      return (
        <picture>
          <source srcSet="https://example.com/hero.avif" type="image/avif" />
          <source srcSet="https://example.com/hero.webp" type="image/webp" />
          <img
            src="https://example.com/hero.jpg"
            alt="Landscape picture"
            width={800}
            height={500}
          />
        </picture>
      )
    }
[/code]

  4. You can use a [custom image loader](https://nextjs.org/docs/pages/api-reference/components/image#loader) to optimize images. Set [loaderFile](https://nextjs.org/docs/pages/api-reference/components/image#loaderfile) to the path of your custom loader.



next.config.js
[code]
    module.exports = {
      images: {
        loader: 'custom',
        loaderFile: './my/image/loader.js',
      },
    }
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-img-element#useful-links)

  * [Image Component and Image Optimization](https://nextjs.org/docs/pages/api-reference/components/image)
  * [next/image API Reference](https://nextjs.org/docs/pages/api-reference/components/image)
  * [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp)
  * [Next.js config loaderFile option](https://nextjs.org/docs/pages/api-reference/components/image#loaderfile)



Was this helpful?

supported.

Send
