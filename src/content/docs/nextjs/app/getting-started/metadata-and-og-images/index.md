---
title: '시작하기: 메타데이터와 OG 이미지'
description: '메타데이터 API는 애플리케이션 메타데이터를 정의해 SEO와 웹 공유성을 향상할 수 있으며 다음을 포함합니다.'
---

# 시작하기: 메타데이터와 OG 이미지 | Next.js

소스 URL: https://nextjs.org/docs/app/getting-started/metadata-and-og-images

[App Router](https://nextjs.org/docs/app/getting-started)[Getting Started](https://nextjs.org/docs/app/getting-started)Metadata and OG images

# 메타데이터와 OG 이미지

마지막 업데이트 2026년 2월 20일

메타데이터 API는 애플리케이션 메타데이터를 정의해 SEO와 웹 공유성을 향상할 수 있으며 다음을 포함합니다.

  1. [정적 `metadata` 객체](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-metadata)
  2. [동적 `generateMetadata` 함수](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-metadata)
  3. 정적 또는 동적으로 생성한 [파비콘](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#favicons)과 [OG 이미지](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-open-graph-images)를 추가하는 데 사용할 수 있는 특별한 [파일 규칙](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)

위 옵션을 사용하면 Next.js가 페이지에 필요한 `<head>` 태그를 자동으로 생성하고, 브라우저 개발자 도구에서 확인할 수 있습니다.

`metadata` 객체와 `generateMetadata` 함수 export는 서버 컴포넌트에서만 지원됩니다.

## 기본 필드[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#default-fields)

라우트가 메타데이터를 정의하지 않아도 항상 추가되는 기본 `meta` 태그 두 가지가 있습니다.

  * [meta charset 태그](https://developer.mozilla.org/docs/Web/HTML/Element/meta#attr-charset)는 웹사이트의 문자 인코딩을 설정합니다.
  * [meta viewport 태그](https://developer.mozilla.org/docs/Web/HTML/Viewport_meta_tag)는 다양한 기기에 맞춰 웹사이트의 뷰포트 너비와 배율을 설정합니다.

[code]
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
[/code]

다른 메타데이터 필드는 [`Metadata` 객체](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-metadata)([정적 메타데이터](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-metadata)용) 또는 `generateMetadata` 함수([생성된 메타데이터](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-metadata)용)로 정의할 수 있습니다.

## 정적 메타데이터[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-metadata)

정적 메타데이터를 정의하려면 정적 [`layout.js`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) 또는 [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page) 파일에서 [`Metadata` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-object)를 export하세요. 예를 들어 blog 라우트에 제목과 설명을 추가하려면 다음과 같습니다.

app/blog/layout.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'

    export const metadata: Metadata = {
      title: 'My Blog',
      description: '...',
    }

    export default function Layout() {}
[/code]

사용 가능한 전체 옵션 목록은 [`generateMetadata` 문서](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields)에서 확인하세요.

## 생성된 메타데이터[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-metadata)

[`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) 함수를 사용해 데이터에 따라 달라지는 메타데이터를 `fetch`할 수 있습니다. 예를 들어 특정 블로그 게시물의 제목과 설명을 가져오려면 다음과 같습니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    import type { Metadata, ResolvingMetadata } from 'next'

    type Props = {
      params: Promise<{ slug: string }>
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }

    export async function generateMetadata(
      { params, searchParams }: Props,
      parent: ResolvingMetadata
    ): Promise<Metadata> {
      const slug = (await params).slug

      // fetch post information
      const post = await fetch(`https://api.vercel.app/blog/${slug}`).then((res) =>
        res.json()
      )

      return {
        title: post.title,
        description: post.description,
      }
    }

    export default function Page({ params, searchParams }: Props) {}
[/code]

### 스트리밍 메타데이터[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#streaming-metadata)

동적으로 렌더링되는 페이지의 경우 Next.js는 메타데이터를 별도로 스트리밍하여 `generateMetadata`가 완료되면 HTML에 주입하고, UI 렌더링을 차단하지 않습니다.

스트리밍 메타데이터는 시각적 콘텐츠를 먼저 스트리밍해 체감 성능을 향상합니다.

메타데이터가 `<head>` 태그에 있기를 기대하는 **봇과 크롤러(Twitterbot, Slackbot, Bingbot 등)** 에게는 스트리밍 메타데이터가 비활성화됩니다. 이는 들어오는 요청의 User-Agent 헤더를 사용해 감지합니다.

Next.js 구성 파일의 [`htmlLimitedBots`](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#disabling) 옵션으로 스트리밍 메타데이터를 사용자 지정하거나 **완전히 비활성화**할 수 있습니다.

정적으로 렌더링되는 페이지는 메타데이터가 빌드 타임에 해결되므로 스트리밍을 사용하지 않습니다.

[스트리밍 메타데이터](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata)에 대해 더 알아보세요.

### 데이터 요청 메모이제이션[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#memoizing-data-requests)

메타데이터와 페이지 자체에서 **동일한** 데이터를 가져와야 하는 경우가 있을 수 있습니다. 중복 요청을 피하려면 React의 [`cache` 함수](https://react.dev/reference/react/cache)를 사용해 반환 값을 메모이제이션하고 한 번만 데이터를 가져오세요. 예를 들어 메타데이터와 페이지 모두에서 블로그 게시물 정보를 가져오려면 다음과 같습니다.

app/lib/data.ts

JavaScriptTypeScript
[code]
    import { cache } from 'react'
    import { db } from '@/app/lib/db'

    // getPost will be used twice, but execute only once
    export const getPost = cache(async (slug: string) => {
      const res = await db.query.posts.findFirst({ where: eq(posts.slug, slug) })
      return res
    })
[/code]

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    import { getPost } from '@/app/lib/data'

    export async function generateMetadata({
      params,
    }: {
      params: { slug: string }
    }) {
      const post = await getPost(params.slug)
      return {
        title: post.title,
        description: post.description,
      }
    }

    export default async function Page({ params }: { params: { slug: string } }) {
      const post = await getPost(params.slug)
      return <div>{post.title}</div>
    }
[/code]

## 파일 기반 메타데이터[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#file-based-metadata)

다음과 같은 메타데이터 전용 파일을 사용할 수 있습니다.

  * [favicon.ico, apple-icon.jpg, icon.jpg](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
  * [opengraph-image.jpg, twitter-image.jpg](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
  * [robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)
  * [sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)

이 파일들을 정적 메타데이터로 사용하거나 코드로 프로그래밍 방식으로 생성할 수 있습니다.

## 파비콘[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#favicons)

파비콘은 북마크와 검색 결과에 사이트를 표시하는 작은 아이콘입니다. 애플리케이션에 파비콘을 추가하려면 `favicon.ico`를 만들고 앱 폴더 루트에 추가하세요.

> 코드로 파비콘을 프로그래밍 방식으로 생성할 수도 있습니다. 자세한 내용은 [파비콘 문서](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)를 참고하세요.

## 정적 오픈 그래프 이미지[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-open-graph-images)

오픈 그래프(OG) 이미지는 소셜 미디어에서 사이트를 표현하는 이미지입니다. 애플리케이션에 정적 OG 이미지를 추가하려면 앱 폴더 루트에 `opengraph-image.jpg` 파일을 생성하세요.

폴더 구조에서 더 깊숙한 위치에 `opengraph-image.jpg`를 만들어 특정 라우트용 OG 이미지를 추가할 수도 있습니다. 예를 들어 `/blog` 라우트 전용 OG 이미지를 만들려면 `blog` 폴더 안에 `opengraph-image.jpg` 파일을 추가하세요.

더 구체적인 이미지가 상위 폴더의 OG 이미지보다 우선합니다.

> `jpeg`, `png`, `gif` 같은 다른 이미지 포맷도 지원됩니다. 자세한 내용은 [오픈 그래프 이미지 문서](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)를 참고하세요.

## 생성된 오픈 그래프 이미지[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-open-graph-images)

[`ImageResponse` 생성자](https://nextjs.org/docs/app/api-reference/functions/image-response)를 사용하면 JSX와 CSS로 동적 이미지를 생성할 수 있습니다. 이는 데이터에 따라 달라지는 OG 이미지에 유용합니다.

예를 들어 각 블로그 게시물마다 고유한 OG 이미지를 생성하려면 `blog` 폴더 안에 `opengraph-image.tsx` 파일을 추가하고 `next/og`에서 `ImageResponse` 생성자를 import하세요.

app/blog/[slug]/opengraph-image.tsx

JavaScriptTypeScript
[code]
    import { ImageResponse } from 'next/og'
    import { getPost } from '@/app/lib/data'

    // Image metadata
    export const size = {
      width: 1200,
      height: 630,
    }

    export const contentType = 'image/png'

    // Image generation
    export default async function Image({ params }: { params: { slug: string } }) {
      const post = await getPost(params.slug)

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
            {post.title}
          </div>
        )
      )
    }
[/code]

`ImageResponse`는 플렉스박스와 절대 위치를 포함한 일반적인 CSS 속성, 사용자 지정 폰트, 줄 바꿈, 중앙 정렬, 중첩 이미지를 지원합니다. [지원되는 CSS 속성 전체 목록](https://nextjs.org/docs/app/api-reference/functions/image-response)을 확인하세요.

> **알아두면 좋아요** :
>
>   * [Vercel OG Playground](https://og-playground.vercel.app/)에서 예제를 볼 수 있습니다.
>   * `ImageResponse`는 HTML과 CSS를 PNG로 변환하기 위해 [`@vercel/og`](https://vercel.com/docs/og-image-generation), [`satori`](https://github.com/vercel/satori), `resvg`를 사용합니다.
>   * 플렉스박스와 일부 CSS 속성만 지원합니다. `display: grid` 같은 고급 레이아웃은 작동하지 않습니다.
>

## API Reference

이 페이지에서 언급한 메타데이터 API에 대해 더 알아보세요.

- [generateMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)
  - Next.js 애플리케이션에 메타데이터를 추가해 검색 엔진 최적화(SEO)와 웹 공유성을 향상시키는 방법을 알아보세요.
- [generateViewport](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)
  - generateViewport 함수에 대한 API 레퍼런스를 확인하세요.
- [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response)
  - ImageResponse 생성자에 대한 API 레퍼런스를 확인하세요.
- [개요](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)
  - Metadata Files메타데이터 파일 규칙에 대한 API 문서를 확인하세요.
- [favicon, icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
  - Favicon, Icon, Apple Icon 파일 규칙에 대한 API 레퍼런스를 확인하세요.
- [opengraph-image and twitter-image](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
  - Open Graph 이미지와 Twitter 이미지 파일 규칙에 대한 API 레퍼런스를 확인하세요.
- [robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)
  - robots.txrobots.txt 파일에 대한 API 레퍼런스를 확인하세요.
- [sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
  - sitemap.xml 파일에 대한 API 레퍼런스를 확인하세요.
- [htmlLimitedBots](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots)
  - 차단 메타데이터를 받아야 하는 사용자 에이전트 목록을 지정하세요.

보내기
