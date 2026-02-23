---
title: '메타데이터 파일: favicon, icon, and apple-icon'
description: ', , 또는  파일 규칙을 사용하면 애플리케이션 아이콘을 설정할 수 있습니다.'
---

# 메타데이터 파일: favicon, icon, and apple-icon | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons

[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)[메타데이터 파일](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)favicon, icon, and apple-icon

페이지 복사

# favicon, icon, and apple-icon

마지막 업데이트 2026년 2월 20일

`favicon`, `icon`, 또는 `apple-icon` 파일 규칙을 사용하면 애플리케이션 아이콘을 설정할 수 있습니다.

웹 브라우저 탭, 휴대폰 홈 화면, 검색 엔진 결과 등 다양한 위치에 나타나는 앱 아이콘을 추가할 때 유용합니다.

앱 아이콘을 설정하는 방법은 두 가지입니다.

  * [이미지 파일 사용 (.ico, .jpg, .png)](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png)
  * [코드로 아이콘 생성 (.js, .ts, .tsx)](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)



## 이미지 파일 (.ico, .jpg, .png)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png)

`/app` 디렉터리 안에 `favicon`, `icon`, 또는 `apple-icon` 이미지 파일을 두어 앱 아이콘으로 사용할 수 있습니다. `favicon` 이미지는 `app/`의 최상위에만 둘 수 있습니다.

Next.js는 해당 파일을 평가한 뒤, 앱의 `<head>` 요소에 필요한 태그를 자동으로 추가합니다.

File convention| Supported file types| Valid locations  
---|---|---  
[`favicon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)| `.ico`| `app/`  
[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)| `.ico`, `.jpg`, `.jpeg`, `.png`, `.svg`| `app/**/*`  
[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)| `.jpg`, `.jpeg`, `.png`| `app/**/*`  
  
### `favicon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)

루트 `/app` 라우트 세그먼트에 `favicon.ico` 이미지 파일을 추가하세요.

<head> 출력
```
    <link rel="icon" href="/favicon.ico" sizes="any" />
```

### `icon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)

`icon.(ico|jpg|jpeg|png|svg)` 이미지 파일을 추가하세요.

<head> 출력
```
    <link
      rel="icon"
      href="/icon?<generated>"
      type="image/<generated>"
      sizes="<generated>"
    />
```

### `apple-icon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)

`apple-icon.(jpg|jpeg|png)` 이미지 파일을 추가하세요.

<head> 출력
```
    <link
      rel="apple-touch-icon"
      href="/apple-icon?<generated>"
      type="image/<generated>"
      sizes="<generated>"
    />
```

> **알아두면 좋아요** :
> 
>   * 파일 이름에 숫자 접미사를 추가해 여러 개의 아이콘을 설정할 수 있습니다. 예: `icon1.png`, `icon2.png` 등. 번호가 붙은 파일은 사전순으로 정렬됩니다.
>   * Favicon은 루트 `/app` 세그먼트에서만 설정할 수 있습니다. 더 세밀한 제어가 필요하면 [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)을 사용하세요.
>   * `<link>` 태그와 `rel`, `href`, `type`, `sizes` 같은 속성은 아이콘 유형과 평가된 파일의 메타데이터에 따라 결정됩니다.
>   * 예를 들어 32×32px `.png` 파일은 `type="image/png"` 및 `sizes="32x32"` 속성을 가집니다.
>   * `.svg` 확장자이거나 이미지 크기를 알 수 없는 경우 `sizes="any"`가 추가됩니다. 자세한 내용은 이 [favicon 핸드북](https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs)을 참고하세요.
> 


## 코드로 아이콘 생성 (.js, .ts, .tsx)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)

[실제 이미지 파일](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png)을 사용하는 것 외에도, 코드를 통해 아이콘을 **프로그램matically 생성**할 수 있습니다.

`icon` 또는 `apple-icon` 라우트를 만들고 기본(default)으로 함수를 export하여 앱 아이콘을 생성하세요.

File convention| Supported file types  
---|---  
`icon`| `.js`, `.ts`, `.tsx`  
`apple-icon`| `.js`, `.ts`, `.tsx`  
  
가장 쉬운 아이콘 생성 방법은 `next/og`의 [`ImageResponse`](https://nextjs.org/docs/app/api-reference/functions/image-response) API를 사용하는 것입니다.

app/icon.tsx

JavaScriptTypeScript
```
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
```

<head> 출력
```
    <link rel="icon" href="/icon?<generated>" type="image/png" sizes="32x32" />
```

> **알아두면 좋아요** :
> 
>   * 기본적으로 생성된 아이콘은 [**정적 최적화**](https://nextjs.org/docs/app/guides/caching#static-rendering)되어(빌드 시 생성 및 캐시) 있으며, [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)나 캐시되지 않은 데이터를 사용하지 않는 한 그렇습니다.
>   * [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)를 사용해 한 파일에서 여러 아이콘을 생성할 수 있습니다.
>   * `favicon` 아이콘은 생성할 수 없습니다. 대신 [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon) 또는 [favicon.ico](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon) 파일을 사용하세요.
>   * 앱 아이콘은 특수한 Route Handler로, [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis)나 [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) 옵션을 사용하지 않는 한 기본적으로 캐시됩니다.
> 


### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#props)

기본 export 함수는 다음 props를 받습니다.

#### `params` (선택)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#params-optional)

루트 세그먼트부터 `icon` 또는 `apple-icon`이 위치한 세그먼트까지의 [동적 라우트 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) 객체를 포함하는 객체로 resolve되는 Promise입니다.

> **알아두면 좋아요** : [`generateImageMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)를 사용하면, 해당 함수는 `generateImageMetadata`가 반환한 항목 중 하나의 `id` 값을 resolve하는 Promise인 `id` prop도 받습니다.

app/shop/[slug]/icon.tsx

JavaScriptTypeScript
```
    export default async function Icon({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      // ...
    }
```

Route| URL| `params`  
---|---|---  
`app/shop/icon.js`| `/shop`| `undefined`  
`app/shop/[slug]/icon.js`| `/shop/1`| `Promise<{ slug: '1' }>`  
`app/shop/[tag]/[item]/icon.js`| `/shop/1/2`| `Promise<{ tag: '1', item: '2' }>`  
  
### Returns[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#returns)

기본 export 함수는 `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response` 중 하나를 반환해야 합니다.

> **알아두면 좋아요** : `ImageResponse`는 이 반환 타입을 만족합니다.

### Config exports[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#config-exports)

`icon` 또는 `apple-icon` 라우트에서 `size`와 `contentType` 변수를 export하여 아이콘 메타데이터를 선택적으로 구성할 수 있습니다.

Option| Type  
---|---  
[`size`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#size)| `{ width: number; height: number }`  
[`contentType`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#contenttype)| `string` \- [이미지 MIME 타입](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types#image_types)  
  
#### `size`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#size)

icon.tsx | apple-icon.tsx

JavaScriptTypeScript
```
    export const size = { width: 32, height: 32 }
     
    export default function Icon() {}
```

<head> 출력
```
    <link rel="icon" sizes="32x32" />
```

#### `contentType`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#contenttype)

icon.tsx | apple-icon.tsx

JavaScriptTypeScript
```
    export const contentType = 'image/png'
     
    export default function Icon() {}
```

<head> 출력
```
    <link rel="icon" type="image/png" />
```

#### 라우트 세그먼트 설정[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#route-segment-config)

`icon`과 `apple-icon`은 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)의 특수 형태로, 페이지와 레이아웃과 동일한 [route segment configuration](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) 옵션을 사용할 수 있습니다.

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#version-history)

Version| Changes  
---|---  
`v16.0.0`| `params`가 객체로 resolve되는 Promise가 되었습니다  
`v13.3.0`| `favicon`, `icon`, `apple-icon`이 도입되었습니다  
  
도움이 되었나요?

지원됨.

전송
