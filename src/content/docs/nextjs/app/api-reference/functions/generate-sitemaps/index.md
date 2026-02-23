---
title: '함수: generateSitemaps'
description: '애플리케이션에 대해 여러 사이트맵을 생성하려면  함수를 사용할 수 있습니다.'
---

# 함수: generateSitemaps | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps

# generateSitemaps

최종 업데이트 2026년 2월 20일

애플리케이션에 대해 여러 사이트맵을 생성하려면 `generateSitemaps` 함수를 사용할 수 있습니다.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps#returns)

`generateSitemaps` 는 `id` 속성을 포함한 객체 배열을 반환합니다.

## URLs[](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps#urls)

생성된 사이트맵은 `/.../sitemap/[id].xml` 에서 확인할 수 있습니다. 예: `/product/sitemap/1.xml`.

## Example[](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps#example)

예를 들어 `generateSitemaps` 로 사이트맵을 분할하려면 사이트맵 `id` 가 포함된 객체 배열을 반환하십시오. 그런 다음 해당 `id` 로 고유한 사이트맵을 생성합니다.

app/product/sitemap.ts

JavaScriptTypeScript
```javascript
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
```

## Version History[](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps#version-history)

Version| Changes
---|---
`v16.0.0`| `generateSitemaps` 에서 반환된 `id` 값이 이제 사이트맵 함수에 `string` 으로 해석되는 프로미스로 전달됩니다.
`v15.0.0`| `generateSitemaps` 가 이제 개발 환경과 프로덕션 환경에서 일관된 URL을 생성합니다.
`v13.3.2`| `generateSitemaps` 가 도입되었습니다. 개발 환경에서는 `/.../sitemap.xml/[id]` 에서 생성된 사이트맵을 확인할 수 있습니다. 예: `/product/sitemap.xml/1`.

## 다음 단계

Next.js 애플리케이션용 사이트맵을 만드는 방법을 알아보세요.

- [sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
  - 파일에 대한 API 레퍼런스.

보내기