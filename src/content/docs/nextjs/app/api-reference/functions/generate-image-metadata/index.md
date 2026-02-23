---
title: '함수: generateImageMetadata'
description: '를 사용하면 하나의 이미지에 대한 다양한 버전을 생성하거나 하나의 라우트 세그먼트에 여러 이미지를 반환할 수 있습니다. 이는 아이콘처럼 메타데이터 값을 하드코딩하지 않고자 할 때 유용합니다.'
---

# 함수: generateImageMetadata | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata

# generateImageMetadata

마지막 업데이트 2026년 2월 20일

`generateImageMetadata`를 사용하면 하나의 이미지에 대한 다양한 버전을 생성하거나 하나의 라우트 세그먼트에 여러 이미지를 반환할 수 있습니다. 이는 아이콘처럼 메타데이터 값을 하드코딩하지 않고자 할 때 유용합니다.

## 매개변수[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#parameters)

`generateImageMetadata` 함수는 다음 매개변수를 받습니다.

#### `params` (옵션)[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#params-optional)

루트 세그먼트부터 `generateImageMetadata`가 호출되는 세그먼트까지의 [동적 라우트 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) 객체를 포함하는 객체입니다.

icon.tsx

JavaScriptTypeScript
```
    export function generateImageMetadata({
      params,
    }: {
      params: { slug: string }
    }) {
      // ...
    }
```

Route| URL| `params`
---|---|---
`app/shop/icon.js`| `/shop`| `undefined`
`app/shop/[slug]/icon.js`| `/shop/1`| `{ slug: '1' }`
`app/shop/[tag]/[item]/icon.js`| `/shop/1/2`| `{ tag: '1', item: '2' }`

## 반환값[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#returns)

`generateImageMetadata` 함수는 `alt`와 `size` 같은 이미지 메타데이터를 포함하는 객체의 `array`를 반환해야 합니다. 추가로 각 항목에는 이미지 생성 함수의 props로 promise 형태로 전달될 `id` 값이 반드시 포함되어야 합니다.

이미지 메타데이터 객체| 타입
---|---
`id`| `string` (필수)
`alt`| `string`
`size`| `{ width: number; height: number }`
`contentType`| `string`

icon.tsx

JavaScriptTypeScript
```
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
```

## 이미지 생성 함수 props[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#image-generation-function-props)

`generateImageMetadata`를 사용할 때 기본 내보내기 이미지 생성 함수는 다음 props를 받습니다.

#### `id`[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#id)

`generateImageMetadata`가 반환한 항목 중 하나의 `id` 값으로 해결되는 promise입니다. `id`는 `generateImageMetadata`에서 반환한 값에 따라 `string` 또는 `number`가 됩니다.

icon.tsx

JavaScriptTypeScript
```
    export default async function Icon({ id }: { id: Promise<string | number> }) {
      const iconId = await id
      // Use iconId to generate the image
    }
```

#### `params` (옵션)[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#params-optional-1)

루트 세그먼트부터 이미지가 공존하는 세그먼트까지의 [동적 라우트 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 포함하는 객체로 해결되는 promise입니다.

icon.tsx

JavaScriptTypeScript
```
    export default async function Icon({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      // Use slug to generate the image
    }
```

### 예시[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#examples)

#### 외부 데이터 사용[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#using-external-data)

이 예시는 `params` 객체와 외부 데이터를 사용해 라우트 세그먼트에 대한 여러 [Open Graph 이미지](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)를 생성합니다.

app/products/[id]/opengraph-image.tsx

JavaScriptTypeScript
```
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
```

## 버전 히스토리[](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata#version-history)

버전| 변경 사항
---|---
`v16.0.0`| 이미지 생성 함수에 전달되는 `id`가 이제 `string` 또는 `number`로 해결되는 promise입니다.
`v16.0.0`| 이미지 생성 함수에 전달되는 `params`가 이제 객체로 해결되는 promise입니다.
`v13.3.0`| `generateImageMetadata` 도입.

## 다음 단계

모든 Metadata API 옵션을 확인하세요.

- [개요](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)
  - Metadata 파일Metadata 파일 컨벤션에 대한 API 문서입니다.

보내기