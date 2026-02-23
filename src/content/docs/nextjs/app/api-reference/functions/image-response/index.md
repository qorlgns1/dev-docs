---
title: '함수: ImageResponse'
description: '생성자는 JSX와 CSS를 사용해 동적 이미지를 생성할 수 있게 합니다. 이는 Open Graph 이미지, Twitter 카드 등 소셜 미디어 이미지를 만들 때 유용합니다.'
---

# 함수: ImageResponse | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/image-response

# ImageResponse

마지막 업데이트 2026년 2월 20일

`ImageResponse` 생성자는 JSX와 CSS를 사용해 동적 이미지를 생성할 수 있게 합니다. 이는 Open Graph 이미지, Twitter 카드 등 소셜 미디어 이미지를 만들 때 유용합니다.

## 참고[](https://nextjs.org/docs/app/api-reference/functions/image-response#reference)

### 매개변수[](https://nextjs.org/docs/app/api-reference/functions/image-response#parameters)

다음 매개변수를 `ImageResponse`에서 사용할 수 있습니다:
[code]
    import { ImageResponse } from 'next/og'

    new ImageResponse(
      element: ReactElement,
      options: {
        width?: number = 1200
        height?: number = 630
        emoji?: 'twemoji' | 'blobmoji' | 'noto' | 'openmoji' = 'twemoji',
        fonts?: {
          name: string,
          data: ArrayBuffer,
          weight: number,
          style: 'normal' | 'italic'
        }[]
        debug?: boolean = false

        // Options that will be passed to the HTTP response
        status?: number = 200
        statusText?: string
        headers?: Record<string, string>
      },
    )
[/code]

> 예시는 [Vercel OG Playground](https://og-playground.vercel.app/)에서 확인할 수 있습니다.

### 지원되는 HTML 및 CSS 기능[](https://nextjs.org/docs/app/api-reference/functions/image-response#supported-html-and-css-features)

`ImageResponse`는 플렉스박스와 절대 배치, 사용자 지정 폰트, 텍스트 줄바꿈, 정렬, 중첩 이미지 등 일반적인 CSS 속성을 지원합니다.

지원되는 HTML 및 CSS 기능 목록은 [Satori 문서](https://github.com/vercel/satori#css)를 참고하세요.

## 동작[](https://nextjs.org/docs/app/api-reference/functions/image-response#behavior)

  * `ImageResponse`는 [@vercel/og](https://vercel.com/docs/concepts/functions/edge-functions/og-image-generation), [Satori](https://github.com/vercel/satori), Resvg를 사용해 HTML과 CSS를 PNG로 변환합니다.
  * 플렉스박스와 일부 CSS 속성만 지원됩니다. `display: grid`와 같은 고급 레이아웃은 동작하지 않습니다.
  * 번들 최대 크기는 `500KB`입니다. 번들 크기에는 JSX, CSS, 폰트, 이미지 및 기타 자산이 모두 포함됩니다. 제한을 초과하면 자산 크기를 줄이거나 런타임에서 가져오는 방법을 고려하세요.
  * `ttf`, `otf`, `woff` 폰트 형식만 지원됩니다. 폰트 파싱 속도를 높이려면 `ttf` 또는 `otf` 사용을 권장합니다.

## 예제[](https://nextjs.org/docs/app/api-reference/functions/image-response#examples)

### 라우트 핸들러[](https://nextjs.org/docs/app/api-reference/functions/image-response#route-handlers)

`ImageResponse`는 라우트 핸들러에서 요청 시점에 이미지를 동적으로 생성하는 데 사용할 수 있습니다.

app/api/route.js
[code]
    import { ImageResponse } from 'next/og'

    export async function GET() {
      try {
        return new ImageResponse(
          (
            <div
              style={{
                height: '100%',
                width: '100%',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                backgroundColor: 'white',
                padding: '40px',
              }}
            >
              <div
                style={{
                  fontSize: 60,
                  fontWeight: 'bold',
                  color: 'black',
                  textAlign: 'center',
                }}
              >
                Welcome to My Site
              </div>
              <div
                style={{
                  fontSize: 30,
                  color: '#666',
                  marginTop: '20px',
                }}
              >
                Generated with Next.js ImageResponse
              </div>
            </div>
          ),
          {
            width: 1200,
            height: 630,
          }
        )
      } catch (e) {
        console.log(`${e.message}`)
        return new Response(`Failed to generate the image`, {
          status: 500,
        })
      }
    }
[/code]

### 파일 기반 메타데이터[](https://nextjs.org/docs/app/api-reference/functions/image-response#file-based-metadata)

[`opengraph-image.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image) 파일에서 `ImageResponse`를 사용해 Open Graph 이미지를 빌드 타임 또는 요청 시점에 동적으로 생성할 수 있습니다.

app/opengraph-image.tsx
[code]
    import { ImageResponse } from 'next/og'

    // Image metadata
    export const alt = 'My site'
    export const size = {
      width: 1200,
      height: 630,
    }

    export const contentType = 'image/png'

    // Image generation
    export default async function Image() {
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
            My site
          </div>
        ),
        // ImageResponse options
        {
          // For convenience, we can re-use the exported opengraph-image
          // size config to also set the ImageResponse's width and height.
          ...size,
        }
      )
    }
[/code]

### 사용자 지정 폰트[](https://nextjs.org/docs/app/api-reference/functions/image-response#custom-fonts)

옵션에 `fonts` 배열을 제공하면 `ImageResponse`에서 사용자 지정 폰트를 사용할 수 있습니다.

app/opengraph-image.tsx
[code]
    import { ImageResponse } from 'next/og'
    import { readFile } from 'node:fs/promises'
    import { join } from 'node:path'

    // Image metadata
    export const alt = 'My site'
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
          // ...
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
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/image-response#version-history)

버전| 변경 사항
---|---
`v14.0.0`| `ImageResponse`가 `next/server`에서 `next/og`로 이동했습니다.
`v13.3.0`| `ImageResponse`를 `next/server`에서 가져올 수 있습니다.
`v13.0.0`| `ImageResponse`가 `@vercel/og` 패키지를 통해 도입되었습니다.

보내기
