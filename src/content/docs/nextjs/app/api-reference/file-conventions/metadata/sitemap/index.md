---
title: '메타데이터 파일: sitemap.xml'
description: '는 Sitemaps XML 포맷과 일치하는 특별한 파일로, 검색 엔진 크롤러가 사이트를 더 효율적으로 색인화하도록 돕습니다.'
---

# 메타데이터 파일: sitemap.xml | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap

[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)[Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)sitemap.xml

Copy page

# sitemap.xml

마지막 업데이트 2026년 2월 20일

`sitemap.(xml|js|ts)`는 [Sitemaps XML 포맷](https://www.sitemaps.org/protocol.html)과 일치하는 특별한 파일로, 검색 엔진 크롤러가 사이트를 더 효율적으로 색인화하도록 돕습니다.

### Sitemap files (.xml)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#sitemap-files-xml)

규모가 작은 애플리케이션에서는 `sitemap.xml` 파일을 생성해 `app` 디렉터리 루트에 두면 됩니다.

app/sitemap.xml
[code]
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url>
        <loc>https://acme.com</loc>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
        <changefreq>yearly</changefreq>
        <priority>1</priority>
      </url>
      <url>
        <loc>https://acme.com/about</loc>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
      </url>
      <url>
        <loc>https://acme.com/blog</loc>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.5</priority>
      </url>
    </urlset>
[/code]

### Generating a sitemap using code (.js, .ts)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts)

`sitemap.(js|ts)` 파일 컨벤션을 사용해 URL 배열을 반환하는 기본 함수를 내보내면 사이트맵을 프로그래밍 방식으로 **생성**할 수 있습니다. TypeScript를 사용할 경우 [`Sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#returns) 타입을 사용할 수 있습니다.

> **참고**: `sitemap.js`는 특별한 Route Handler로, [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis)나 [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) 옵션을 사용하지 않는 한 기본적으로 캐시됩니다.

app/sitemap.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
     
    export default function sitemap(): MetadataRoute.Sitemap {
      return [
        {
          url: 'https://acme.com',
          lastModified: new Date(),
          changeFrequency: 'yearly',
          priority: 1,
        },
        {
          url: 'https://acme.com/about',
          lastModified: new Date(),
          changeFrequency: 'monthly',
          priority: 0.8,
        },
        {
          url: 'https://acme.com/blog',
          lastModified: new Date(),
          changeFrequency: 'weekly',
          priority: 0.5,
        },
      ]
    }
[/code]

Output:

acme.com/sitemap.xml
[code]
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url>
        <loc>https://acme.com</loc>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
        <changefreq>yearly</changefreq>
        <priority>1</priority>
      </url>
      <url>
        <loc>https://acme.com/about</loc>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
      </url>
      <url>
        <loc>https://acme.com/blog</loc>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.5</priority>
      </url>
    </urlset>
[/code]

### Image Sitemaps[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#image-sitemaps)

`images` 속성을 사용해 이미지 사이트맵을 만들 수 있습니다. 자세한 내용은 [Google Developer Docs](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps)를 참고하세요.

app/sitemap.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
     
    export default function sitemap(): MetadataRoute.Sitemap {
      return [
        {
          url: 'https://example.com',
          lastModified: '2021-01-01',
          changeFrequency: 'weekly',
          priority: 0.5,
          images: ['https://example.com/image.jpg'],
        },
      ]
    }
[/code]

Output:

acme.com/sitemap.xml
[code]
    <?xml version="1.0" encoding="UTF-8"?>
    <urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
    >
      <url>
        <loc>https://example.com</loc>
        <image:image>
          <image:loc>https://example.com/image.jpg</image:loc>
        </image:image>
        <lastmod>2021-01-01</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.5</priority>
      </url>
    </urlset>
[/code]

### Video Sitemaps[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#video-sitemaps)

`videos` 속성을 사용해 비디오 사이트맵을 만들 수 있습니다. 자세한 내용은 [Google Developer Docs](https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps)를 참고하세요.

app/sitemap.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
     
    export default function sitemap(): MetadataRoute.Sitemap {
      return [
        {
          url: 'https://example.com',
          lastModified: '2021-01-01',
          changeFrequency: 'weekly',
          priority: 0.5,
          videos: [
            {
              title: 'example',
              thumbnail_loc: 'https://example.com/image.jpg',
              description: 'this is the description',
            },
          ],
        },
      ]
    }
[/code]

Output:

acme.com/sitemap.xml
[code]
    <?xml version="1.0" encoding="UTF-8"?>
    <urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"
    >
      <url>
        <loc>https://example.com</loc>
        <video:video>
          <video:title>example</video:title>
          <video:thumbnail_loc>https://example.com/image.jpg</video:thumbnail_loc>
          <video:description>this is the description</video:description>
        </video:video>
        <lastmod>2021-01-01</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.5</priority>
      </url>
    </urlset>
[/code]

### Generate a localized Sitemap[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generate-a-localized-sitemap)

app/sitemap.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
     
    export default function sitemap(): MetadataRoute.Sitemap {
      return [
        {
          url: 'https://acme.com',
          lastModified: new Date(),
          alternates: {
            languages: {
              es: 'https://acme.com/es',
              de: 'https://acme.com/de',
            },
          },
        },
        {
          url: 'https://acme.com/about',
          lastModified: new Date(),
          alternates: {
            languages: {
              es: 'https://acme.com/es/about',
              de: 'https://acme.com/de/about',
            },
          },
        },
        {
          url: 'https://acme.com/blog',
          lastModified: new Date(),
          alternates: {
            languages: {
              es: 'https://acme.com/es/blog',
              de: 'https://acme.com/de/blog',
            },
          },
        },
      ]
    }
[/code]

Output:

acme.com/sitemap.xml
[code]
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
      <url>
        <loc>https://acme.com</loc>
        <xhtml:link
          rel="alternate"
          hreflang="es"
          href="https://acme.com/es"/>
        <xhtml:link
          rel="alternate"
          hreflang="de"
          href="https://acme.com/de"/>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
      </url>
      <url>
        <loc>https://acme.com/about</loc>
        <xhtml:link
          rel="alternate"
          hreflang="es"
          href="https://acme.com/es/about"/>
        <xhtml:link
          rel="alternate"
          hreflang="de"
          href="https://acme.com/de/about"/>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
      </url>
      <url>
        <loc>https://acme.com/blog</loc>
        <xhtml:link
          rel="alternate"
          hreflang="es"
          href="https://acme.com/es/blog"/>
        <xhtml:link
          rel="alternate"
          hreflang="de"
          href="https://acme.com/de/blog"/>
        <lastmod>2023-04-06T15:02:24.021Z</lastmod>
      </url>
    </urlset>
[/code]

### Generating multiple sitemaps[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generating-multiple-sitemaps)

대부분의 애플리케이션에서는 단일 사이트맵이면 충분하지만, 대규모 웹 애플리케이션에서는 여러 파일로 나눠야 할 수도 있습니다.

여러 사이트맵을 만드는 방법은 두 가지입니다.

  * `sitemap.(xml|js|ts)`를 여러 라우트 세그먼트에 중첩하는 방법. 예: `app/sitemap.xml`, `app/products/sitemap.xml`.
  * [`generateSitemaps`](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps) 함수를 사용하는 방법.



예를 들어 `generateSitemaps`를 사용해 사이트맵을 분할하려면 사이트맵 `id`가 포함된 객체 배열을 반환합니다. 그런 다음 `id`를 사용해 고유한 사이트맵을 생성합니다.

app/product/sitemap.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
    import { BASE_URL } from '@/app/lib/constants'
     
    export async function generateSitemaps() {
      // Fetch the total number of products and calculate the number of sitemaps needed
      return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
    }
     
    export default async function sitemap(props: {
      id: Promise<string>
    }): Promise<MetadataRoute.Sitemap> {
      const id = await props.id
      // Google's limit is 50,000 URLs per sitemap
      const start = id * 50000
      const end = start + 50000
      const products = await getProducts(
        `SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
      )
      return products.map((product) => ({
        url: `${BASE_URL}/product/${product.id}`,
        lastModified: product.date,
      }))
    }
[/code]

생성된 사이트맵은 `/.../sitemap/[id]`에서 사용할 수 있습니다. 예: `/product/sitemap/1.xml`.

자세한 내용은 [`generateSitemaps` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps)를 참고하세요.

## Returns[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#returns)

`sitemap.(xml|ts|js)`에서 내보내는 기본 함수는 다음 속성을 가진 객체 배열을 반환해야 합니다:
[code] 
    type Sitemap = Array<{
      url: string
      lastModified?: string | Date
      changeFrequency?:
        | 'always'
        | 'hourly'
        | 'daily'
        | 'weekly'
        | 'monthly'
        | 'yearly'
        | 'never'
      priority?: number
      alternates?: {
        languages?: Languages<string>
      }
    }>
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#version-history)

Version| Changes  
---|---  
`v16.0.0`| `id`가 이제 `string`으로 resolve되는 promise입니다.  
`v14.2.0`| 현지화(localizations) 지원을 추가했습니다.  
`v13.4.14`| 사이트맵에 `changeFrequency`, `priority` 속성을 추가했습니다.  
`v13.3.0`| `sitemap`이 도입되었습니다.  
  
## Next Steps

generateSitemaps 함수를 사용하는 방법을 알아보세요.

### [generateSitemaps애플리케이션에 여러 사이트맵을 만들기 위해 generateSiteMaps 함수를 사용하는 방법을 배워보세요.](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps)

Was this helpful?

supported.

Send
