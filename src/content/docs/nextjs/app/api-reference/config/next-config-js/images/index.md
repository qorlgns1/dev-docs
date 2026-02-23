---
title: 'next.config.js: 이미지'
description: 'Next.js 내장 Image Optimization API 대신 클라우드 공급자를 사용해 이미지를 최적화하려면 를 다음과 같이 구성할 수 있습니다.'
---

# next.config.js: 이미지 | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/images

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)images

페이지 복사

# 이미지

마지막 업데이트 2026년 2월 20일

Next.js 내장 Image Optimization API 대신 클라우드 공급자를 사용해 이미지를 최적화하려면 `next.config.js`를 다음과 같이 구성할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        loader: 'custom',
        loaderFile: './my/image/loader.js',
      },
    }
[/code]

이 `loaderFile`은 Next.js 애플리케이션 루트를 기준으로 하는 파일을 가리켜야 합니다. 해당 파일은 문자열을 반환하는 기본 함수를 내보내야 하며, 예시는 다음과 같습니다.

my/image/loader.js
[code]
    'use client'
     
    export default function myImageLoader({ src, width, quality }) {
      return `https://example.com/${src}?w=${width}&q=${quality || 75}`
    }
[/code]

또는 [`loader` prop](https://nextjs.org/docs/app/api-reference/components/image#loader)을 사용해 함수를 각 `next/image` 인스턴스에 전달할 수도 있습니다.

> **알아두면 좋은 점** : 함수를 받는 이미지 로더 파일을 커스터마이즈하려면 제공한 함수를 직렬화하기 위해 [Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)를 사용해야 합니다.

내장 [Image Optimization API](https://nextjs.org/docs/app/api-reference/components/image)와 [Image Component](https://nextjs.org/docs/app/api-reference/components/image)의 동작을 구성하는 방법을 더 알아보려면 사용 가능한 옵션이 정리된 [Image Configuration Options](https://nextjs.org/docs/app/api-reference/components/image#configuration-options)를 참조하세요.

## 로더 구성 예시[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#example-loader-configuration)

  * [Akamai](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#akamai)
  * [AWS CloudFront](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#aws-cloudfront)
  * [Cloudinary](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#cloudinary)
  * [Cloudflare](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#cloudflare)
  * [Contentful](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#contentful)
  * [Fastly](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#fastly)
  * [Gumlet](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#gumlet)
  * [ImageEngine](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#imageengine)
  * [Imgix](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#imgix)
  * [PixelBin](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#pixelbin)
  * [Sanity](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#sanity)
  * [Sirv](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#sirv)
  * [Supabase](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#supabase)
  * [Thumbor](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#thumbor)
  * [Imagekit](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#imagekitio)
  * [Nitrogen AIO](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#nitrogen-aio)



### Akamai[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#akamai)
[code] 
    // Docs: https://techdocs.akamai.com/ivm/reference/test-images-on-demand
    export default function akamaiLoader({ src, width, quality }) {
      return `https://example.com/${src}?imwidth=${width}`
    }
[/code]

### AWS CloudFront[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#aws-cloudfront)
[code] 
    // Docs: https://aws.amazon.com/developer/application-security-performance/articles/image-optimization
    export default function cloudfrontLoader({ src, width, quality }) {
      const url = new URL(`https://example.com${src}`)
      url.searchParams.set('format', 'auto')
      url.searchParams.set('width', width.toString())
      url.searchParams.set('quality', (quality || 75).toString())
      return url.href
    }
[/code]

### Cloudinary[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#cloudinary)
[code] 
    // Demo: https://res.cloudinary.com/demo/image/upload/w_300,c_limit,q_auto/turtles.jpg
    export default function cloudinaryLoader({ src, width, quality }) {
      const params = ['f_auto', 'c_limit', `w_${width}`, `q_${quality || 'auto'}`]
      return `https://example.com/${params.join(',')}${src}`
    }
[/code]

### Cloudflare[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#cloudflare)
[code] 
    // Docs: https://developers.cloudflare.com/images/transform-images
    export default function cloudflareLoader({ src, width, quality }) {
      const params = [`width=${width}`, `quality=${quality || 75}`, 'format=auto']
      return `https://example.com/cdn-cgi/image/${params.join(',')}/${src}`
    }
[/code]

### Contentful[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#contentful)
[code] 
    // Docs: https://www.contentful.com/developers/docs/references/images-api/
    export default function contentfulLoader({ src, width, quality }) {
      const url = new URL(`https://example.com${src}`)
      url.searchParams.set('fm', 'webp')
      url.searchParams.set('w', width.toString())
      url.searchParams.set('q', (quality || 75).toString())
      return url.href
    }
[/code]

### Fastly[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#fastly)
[code] 
    // Docs: https://developer.fastly.com/reference/io/
    export default function fastlyLoader({ src, width, quality }) {
      const url = new URL(`https://example.com${src}`)
      url.searchParams.set('auto', 'webp')
      url.searchParams.set('width', width.toString())
      url.searchParams.set('quality', (quality || 75).toString())
      return url.href
    }
[/code]

### Gumlet[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#gumlet)
[code] 
    // Docs: https://docs.gumlet.com/reference/image-transform-size
    export default function gumletLoader({ src, width, quality }) {
      const url = new URL(`https://example.com${src}`)
      url.searchParams.set('format', 'auto')
      url.searchParams.set('w', width.toString())
      url.searchParams.set('q', (quality || 75).toString())
      return url.href
    }
[/code]

### ImageEngine[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#imageengine)
[code] 
    // Docs: https://support.imageengine.io/hc/en-us/articles/360058880672-Directives
    export default function imageengineLoader({ src, width, quality }) {
      const compression = 100 - (quality || 50)
      const params = [`w_${width}`, `cmpr_${compression}`)]
      return `https://example.com${src}?imgeng=/${params.join('/')`
    }
[/code]

### Imgix[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#imgix)
[code] 
    // Demo: https://static.imgix.net/daisy.png?format=auto&fit=max&w=300
    export default function imgixLoader({ src, width, quality }) {
      const url = new URL(`https://example.com${src}`)
      const params = url.searchParams
      params.set('auto', params.getAll('auto').join(',') || 'format')
      params.set('fit', params.get('fit') || 'max')
      params.set('w', params.get('w') || width.toString())
      params.set('q', (quality || 50).toString())
      return url.href
    }
[/code]

### PixelBin[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#pixelbin)
[code] 
    // Doc (Resize): https://www.pixelbin.io/docs/transformations/basic/resize/#width-w
    // Doc (Optimise): https://www.pixelbin.io/docs/optimizations/quality/#image-quality-when-delivering
    // Doc (Auto Format Delivery): https://www.pixelbin.io/docs/optimizations/format/#automatic-format-selection-with-f_auto-url-parameter
    export default function pixelBinLoader({ src, width, quality }) {
      const name = '<your-cloud-name>'
      const opt = `t.resize(w:${width})~t.compress(q:${quality || 75})`
      return `https://cdn.pixelbin.io/v2/${name}/${opt}/${src}?f_auto=true`
    }
[/code]

### Sanity[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#sanity)
[code] 
    // Docs: https://www.sanity.io/docs/image-urls
    export default function sanityLoader({ src, width, quality }) {
      const prj = 'zp7mbokg'
      const dataset = 'production'
      const url = new URL(`https://cdn.sanity.io/images/${prj}/${dataset}${src}`)
      url.searchParams.set('auto', 'format')
      url.searchParams.set('fit', 'max')
      url.searchParams.set('w', width.toString())
      if (quality) {
        url.searchParams.set('q', quality.toString())
      }
      return url.href
    }
[/code]

### Sirv[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#sirv)
[code] 
    // Docs: https://sirv.com/help/articles/dynamic-imaging/
    export default function sirvLoader({ src, width, quality }) {
      const url = new URL(`https://example.com${src}`)
      const params = url.searchParams
      params.set('format', params.getAll('format').join(',') || 'optimal')
      params.set('w', params.get('w') || width.toString())
      params.set('q', (quality || 85).toString())
      return url.href
    }
[/code]

### Supabase[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#supabase)
[code] 
    // Docs: https://supabase.com/docs/guides/storage/image-transformations#nextjs-loader
    export default function supabaseLoader({ src, width, quality }) {
      const url = new URL(`https://example.com${src}`)
      url.searchParams.set('width', width.toString())
      url.searchParams.set('quality', (quality || 75).toString())
      return url.href
    }
[/code]

### Thumbor[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#thumbor)
[code] 
    // Docs: https://thumbor.readthedocs.io/en/latest/
    export default function thumborLoader({ src, width, quality }) {
      const params = [`${width}x0`, `filters:quality(${quality || 75})`]
      return `https://example.com${params.join('/')}${src}`
    }
[/code]

### ImageKit.io[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#imagekitio)
[code] 
    // Docs: https://imagekit.io/docs/image-transformation
    export default function imageKitLoader({ src, width, quality }) {
      const params = [`w-${width}`, `q-${quality || 80}`]
      return `https://ik.imagekit.io/your_imagekit_id/${src}?tr=${params.join(',')}`
    }
[/code]

### Nitrogen AIO[](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#nitrogen-aio)
[code] 
    // Docs: https://docs.n7.io/aio/intergrations/
    export default function aioLoader({ src, width, quality }) {
      const url = new URL(src, window.location.href)
      const params = url.searchParams
      const aioParams = params.getAll('aio')
      aioParams.push(`w-${width}`)
      if (quality) {
        aioParams.push(`q-${quality.toString()}`)
      }
      params.set('aio', aioParams.join(';'))
      return url.href
    }
[/code]

도움이 되었나요?

지원됨.

전송
