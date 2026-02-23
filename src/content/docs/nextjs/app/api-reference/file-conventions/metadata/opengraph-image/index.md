---
title: '메타데이터 파일: opengraph-image 및 twitter-image'
description: '및  파일 규칙은 라우트 세그먼트에 대해 Open Graph 및 Twitter 이미지를 설정할 수 있게 해줍니다.'
---

# 메타데이터 파일: opengraph-image 및 twitter-image | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image

[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)[메타데이터 파일](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)opengraph-image 및 twitter-image

# opengraph-image 및 twitter-image

마지막 업데이트 2026년 2월 20일

`opengraph-image` 및 `twitter-image` 파일 규칙은 라우트 세그먼트에 대해 Open Graph 및 Twitter 이미지를 설정할 수 있게 해줍니다.

이 규칙은 사용자가 사이트 링크를 소셜 네트워크나 메신저 앱에서 공유할 때 표시되는 이미지를 지정하는 데 유용합니다.

Open Graph와 Twitter 이미지를 설정하는 방법은 두 가지입니다.

  * [이미지 파일 사용(.jpg, .png, .gif)](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif)
  * [코드를 사용해 이미지 생성(.js, .ts, .tsx)](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)

## 이미지 파일(.jpg, .png, .gif)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif)

세그먼트에 `opengraph-image` 또는 `twitter-image` 이미지 파일을 배치해 해당 라우트 세그먼트의 공유 이미지를 설정합니다.

Next.js는 파일을 평가하고 앱의 `<head>` 요소에 적절한 태그를 자동으로 추가합니다.

파일 규칙| 지원 파일 형식
---|---
[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)| `.jpg`, `.jpeg`, `.png`, `.gif`
[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)| `.jpg`, `.jpeg`, `.png`, `.gif`
[`opengraph-image.alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-imagealttxt)| `.txt`
[`twitter-image.alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-imagealttxt)| `.txt`

> **알아두면 좋아요** :
>
> `twitter-image` 파일 크기는 [5MB](https://developer.x.com/en/docs/x-for-websites/cards/overview/summary)를, `opengraph-image` 파일 크기는 [8MB](https://developers.facebook.com/docs/sharing/webmasters/images)를 초과하면 안 됩니다. 이미지 파일 크기가 이 한도를 넘으면 빌드가 실패합니다.

### `opengraph-image`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)

원하는 라우트 세그먼트에 `opengraph-image.(jpg|jpeg|png|gif)` 이미지 파일을 추가합니다.

<head> 출력
```
    <meta property="og:image" content="<generated>" />
    <meta property="og:image:type" content="<generated>" />
    <meta property="og:image:width" content="<generated>" />
    <meta property="og:image:height" content="<generated>" />
```

### `twitter-image`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)

원하는 라우트 세그먼트에 `twitter-image.(jpg|jpeg|png|gif)` 이미지 파일을 추가합니다.

<head> 출력
```
    <meta name="twitter:image" content="<generated>" />
    <meta name="twitter:image:type" content="<generated>" />
    <meta name="twitter:image:width" content="<generated>" />
    <meta name="twitter:image:height" content="<generated>" />
```

### `opengraph-image.alt.txt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-imagealttxt)

`opengraph-image.(jpg|jpeg|png|gif)` 이미지와 같은 라우트 세그먼트에 해당 alt 텍스트인 `opengraph-image.alt.txt` 파일을 추가합니다.

opengraph-image.alt.txt
```
    About Acme
```

<head> 출력
```
    <meta property="og:image:alt" content="About Acme" />
```

### `twitter-image.alt.txt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-imagealttxt)

`twitter-image.(jpg|jpeg|png|gif)` 이미지와 같은 라우트 세그먼트에 해당 alt 텍스트인 `twitter-image.alt.txt` 파일을 추가합니다.

twitter-image.alt.txt
```
    About Acme
```

<head> 출력
```
    <meta property="twitter:image:alt" content="About Acme" />
```

## 코드로 이미지 생성(.js, .ts, .tsx)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)

[실제 이미지 파일](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif)을 사용하는 것 외에도 코드로 이미지를 프로그래밍 방식으로 **생성**할 수 있습니다.

`opengraph-image` 또는 `twitter-image` 라우트를 만들고 기본 내보내기 함수에서 라우트 세그먼트의 공유 이미지를 생성하세요.

파일 규칙| 지원 파일 형식
---|---
`opengraph-image`| `.js`, `.ts`, `.tsx`
`twitter-image`| `.js`, `.ts`, `.tsx`

> **알아두면 좋아요** :
>
>   * 기본적으로 생성된 이미지는 [**정적 최적화**](https://nextjs.org/docs/app/guides/caching#static-rendering)(빌드 시 생성 후 캐시)에 속하며, [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)나 캐시되지 않은 데이터를 사용하지 않는 한 그렇습니다.
>   * [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)를 사용하면 하나의 파일에서 여러 이미지를 생성할 수 있습니다.
>   * `opengraph-image.js`와 `twitter-image.js`는 특별한 Route Handler이며 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis)나 [동적 구성](https://nextjs.org/docs/app/guides/caching#segment-config-options) 옵션을 사용하지 않는 한 기본적으로 캐시됩니다.
>

가장 쉬운 이미지 생성 방법은 `next/og`의 [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response) API를 사용하는 것입니다.

app/about/opengraph-image.tsx

JavaScriptTypeScript
```
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
```

<head> 출력
```
    <meta property="og:image" content="<generated>" />
    <meta property="og:image:alt" content="About Acme" />
    <meta property="og:image:type" content="image/png" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
```

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#props)

기본 내보내기 함수는 다음 props를 받습니다.

#### `params`(선택 사항)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#params-optional)

루트 세그먼트부터 `opengraph-image` 또는 `twitter-image`가 배치된 세그먼트까지의 [동적 라우트 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) 객체를 담은 객체로 해결되는 Promise입니다.

> **알아두면 좋아요** : [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)를 사용하면, 함수는 `generateImageMetadata`에서 반환된 항목 중 하나의 `id` 값을 resolve하는 `id` prop도 받습니다.

app/shop/[slug]/opengraph-image.tsx

JavaScriptTypeScript
```
    export default async function Image({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      // ...
    }
```

라우트| URL| `params`
---|---|---
`app/shop/opengraph-image.js`| `/shop`| `undefined`
`app/shop/[slug]/opengraph-image.js`| `/shop/1`| `Promise<{ slug: '1' }>`
`app/shop/[tag]/[item]/opengraph-image.js`| `/shop/1/2`| `Promise<{ tag: '1', item: '2' }>`

### 반환값[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#returns)

기본 내보내기 함수는 `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response` 중 하나를 반환해야 합니다.

> **알아두면 좋아요** : `ImageResponse`는 이 반환 타입을 충족합니다.

### 구성 내보내기[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#config-exports)

`opengraph-image` 또는 `twitter-image` 라우트에서 `alt`, `size`, `contentType` 변수를 내보내 이미지 메타데이터를 선택적으로 구성할 수 있습니다.

옵션| 타입
---|---
[`alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#alt)| `string`
[`size`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#size)| `{ width: number; height: number }`
[`contentType`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#contenttype)| `string` \- [이미지 MIME 타입](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types#image_types)

#### `alt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#alt)

opengraph-image.tsx | twitter-image.tsx

JavaScriptTypeScript
```
    export const alt = 'My images alt text'

    export default function Image() {}
```

<head> 출력
```
    <meta property="og:image:alt" content="My images alt text" />
```

#### `size`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#size)

opengraph-image.tsx | twitter-image.tsx

JavaScriptTypeScript
```
    export const size = { width: 1200, height: 630 }

    export default function Image() {}
```

<head> 출력
```
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
```

#### `contentType`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#contenttype)

opengraph-image.tsx | twitter-image.tsx

JavaScriptTypeScript
```
    export const contentType = 'image/png'

    export default function Image() {}
```

<head> 출력
```
    <meta property="og:image:type" content="image/png" />
```

#### 라우트 세그먼트 구성[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#route-segment-config)

`opengraph-image` 및 `twitter-image`는 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)의 특수 형태이며, 페이지와 레이아웃과 동일한 [라우트 세그먼트 구성](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) 옵션을 사용할 수 있습니다.

### 예시[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#examples)

#### 외부 데이터 사용[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#using-external-data)

이 예시는 `params` 객체와 외부 데이터를 사용해 이미지를 생성합니다.

> **알아두면 좋아요** : 기본적으로 이 생성된 이미지는 [정적으로 최적화](https://nextjs.org/docs/app/guides/caching#static-rendering)됩니다. 이 동작을 변경하려면 개별 `fetch` [`options`](https://nextjs.org/docs/app/api-reference/functions/fetch) 또는 라우트 세그먼트 [options](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate)을 구성할 수 있습니다.

app/posts/[slug]/opengraph-image.tsx

JavaScriptTypeScript
```
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
```

#### 로컬 에셋과 함께 Node.js 런타임 사용[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#using-nodejs-runtime-with-local-assets)

다음 예시는 Node.js 런타임을 사용해 파일 시스템에서 로컬 이미지를 가져온 뒤 `<img>`의 `src` 속성에 base64 문자열 또는 `ArrayBuffer`로 전달합니다. 로컬 에셋은 예제 소스 파일이 아니라 프로젝트 루트 기준으로 배치하세요.

app/opengraph-image.tsx

JavaScriptTypeScript
```
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
```

`<img>` 요소의 `src` 속성에 `ArrayBuffer`를 전달하는 것은 HTML 명세에 포함되지 않습니다. `next/og`에서 사용하는 렌더링 엔진은 이를 지원하지만, TypeScript 정의는 명세를 따르므로 이 [기능](https://github.com/vercel/satori/issues/606#issuecomment-2144000453)을 사용하려면 `@ts-expect-error` 지시문이나 유사한 처리가 필요합니다.

app/opengraph-image.tsx

JavaScriptTypeScript
```
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
```

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#version-history)

Version| Changes
---|---
`v16.0.0`| `params`가 이제 객체로 해석되는 프로미스입니다.
`v13.3.0`| `opengraph-image`와 `twitter-image`가 도입되었습니다.