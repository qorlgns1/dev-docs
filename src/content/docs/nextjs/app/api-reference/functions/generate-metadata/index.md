---
title: '함수: generateMetadata'
description: '객체나  함수를 사용하여 메타데이터를 정의할 수 있습니다.'
---

# 함수: generateMetadata | Next.js
출처 URL: https://nextjs.org/docs/app/api-reference/functions/generate-metadata

[API 레퍼런스](https://nextjs.org/docs/app/api-reference) [함수](https://nextjs.org/docs/app/api-reference/functions) generateMetadata

페이지 복사

# generateMetadata

마지막 업데이트 2026년 2월 20일

`metadata` 객체나 `generateMetadata` 함수를 사용하여 메타데이터를 정의할 수 있습니다.

## `metadata` 객체[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#the-metadata-object)

정적 메타데이터를 정의하려면 `layout.js` 또는 `page.js` 파일에서 [`Metadata` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields)를 export 하세요.

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: '...',
      description: '...',
    }
     
    export default function Page() {}
[/code]

> 전체 지원 옵션 목록은 [Metadata Fields](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields)를 참고하세요.

## `generateMetadata` 함수[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#generatemetadata-function)

현재 경로 매개변수, 외부 데이터, 상위 세그먼트의 `metadata` 등 **동적 정보** 에 따라 달라지는 동적 메타데이터는 [`Metadata` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields)를 반환하는 `generateMetadata` 함수를 export 하여 설정할 수 있습니다.

`generateMetadata` 해석은 페이지 렌더링 과정의 일부입니다. 페이지를 사전 렌더링할 수 있고 `generateMetadata` 가 동적 동작을 도입하지 않으면 결과 메타데이터가 페이지 초기 HTML에 포함됩니다.

그렇지 않으면 `generateMetadata` 에서 해석된 메타데이터는 초기 UI 전송 후 [스트리밍](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata)할 수 있습니다.

app/products/[id]/page.tsx

JavaScriptTypeScript
[code]
    import type { Metadata, ResolvingMetadata } from 'next'
     
    type Props = {
      params: Promise<{ id: string }>
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }
     
    export async function generateMetadata(
      { params, searchParams }: Props,
      parent: ResolvingMetadata
    ): Promise<Metadata> {
      // read route params
      const { id } = await params
     
      // fetch data
      const product = await fetch(`https://.../${id}`).then((res) => res.json())
     
      // optionally access and extend (rather than replace) parent metadata
      const previousImages = (await parent).openGraph?.images || []
     
      return {
        title: product.title,
        openGraph: {
          images: ['/some-specific-page-image.jpg', ...previousImages],
        },
      }
    }
     
    export default function Page({ params, searchParams }: Props) {}
[/code]

`params` 와 `searchParams` 의 타입 완성을 위해, 페이지와 레이아웃에 각각 [`PageProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper) 또는 [`LayoutProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)를 사용할 수 있습니다.

> **알아두면 좋은 사항**
> 
>   * 메타데이터는 `layout.js` 및 `page.js` 파일에 추가할 수 있습니다.
>   * Next.js는 메타데이터를 자동으로 해석하여 페이지에 필요한 `<head>` 태그를 생성합니다.
>   * `metadata` 객체와 `generateMetadata` 함수 export 는 **Server Component 에서만 지원** 됩니다.
>   * 동일한 경로 세그먼트에서 `metadata` 객체와 `generateMetadata` 함수를 동시에 export 할 수 없습니다.
>   * `generateMetadata` 내부의 `fetch` 요청은 `generateMetadata`, `generateStaticParams`, 레이아웃, 페이지, Server Component 전반에서 동일한 데이터를 위해 자동으로 [메모이즈](https://nextjs.org/docs/app/guides/caching#request-memoization)됩니다.
>   * `fetch` 를 사용할 수 없다면 React [`cache`](https://nextjs.org/docs/app/guides/caching#react-cache-function)를 사용할 수 있습니다.
>   * [파일 기반 메타데이터](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)가 더 높은 우선순위를 가지며 `metadata` 객체와 `generateMetadata` 함수를 무시합니다.
> 


## Reference[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#reference)

### Parameters[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#parameters)

`generateMetadata` 함수는 다음 매개변수를 받습니다.

  * `props` \- 현재 경로의 매개변수를 포함하는 객체:
    * `params` \- 루트 세그먼트부터 `generateMetadata` 가 호출되는 세그먼트까지의 [동적 경로 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 담는 객체입니다. 예:

Route| URL| `params`  
---|---|---  
`app/shop/[slug]/page.js`| `/shop/1`| `{ slug: '1' }`  
`app/shop/[tag]/[item]/page.js`| `/shop/1/2`| `{ tag: '1', item: '2' }`  
`app/shop/[...slug]/page.js`| `/shop/1/2`| `{ slug: ['1', '2'] }`  
  
    * `searchParams` \- 현재 URL의 [검색 매개변수](https://developer.mozilla.org/docs/Learn/Common_questions/What_is_a_URL#parameters)를 담는 객체입니다. 예:

URL| `searchParams`  
---|---  
`/shop?a=1`| `{ a: '1' }`  
`/shop?a=1&b=2`| `{ a: '1', b: '2' }`  
`/shop?a=1&a=2`| `{ a: ['1', '2'] }`  
  
  * `parent` \- 상위 경로 세그먼트에서 해석된 메타데이터에 대한 프로미스입니다.




### Returns[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#returns)

`generateMetadata` 는 하나 이상의 메타데이터 필드를 포함하는 [`Metadata` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields)를 반환해야 합니다.

> **알아두면 좋은 사항**
> 
>   * 메타데이터가 런타임 정보에 의존하지 않는다면 `generateMetadata` 대신 정적 [`metadata` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#the-metadata-object)로 정의해야 합니다.
>   * `fetch` 요청은 `generateMetadata`, `generateStaticParams`, 레이아웃, 페이지, Server Component 전반에서 동일한 데이터를 위해 자동으로 [메모이즈](https://nextjs.org/docs/app/guides/caching#request-memoization)됩니다. `fetch` 를 사용할 수 없다면 React [`cache`](https://nextjs.org/docs/app/guides/caching#react-cache-function)를 사용할 수 있습니다.
>   * `searchParams` 는 `page.js` 세그먼트에서만 사용할 수 있습니다.
>   * Next.js의 [`redirect()`](https://nextjs.org/docs/app/api-reference/functions/redirect) 및 [`notFound()`](https://nextjs.org/docs/app/api-reference/functions/not-found) 메서드도 `generateMetadata` 안에서 사용할 수 있습니다.
> 


### Metadata Fields[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-fields)

다음 필드를 지원합니다.

#### `title`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#title)

`title` 속성은 문서 제목을 설정하는 데 사용됩니다. 단순 [문자열](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#string) 또는 선택적 [템플릿 객체](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#template)로 정의할 수 있습니다.

##### String[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#string)

layout.js | page.js
[code]
    export const metadata = {
      title: 'Next.js',
    }
[/code]

<head> output
[code]
    <title>Next.js</title>
[/code]

##### `default`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#default)

`title.default` 는 `title` 을 정의하지 않은 하위 경로 세그먼트에 **대체 제목** 을 제공하는 데 사용할 수 있습니다.

app/layout.tsx
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: {
        default: 'Acme',
      },
    }
[/code]

app/about/page.tsx
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {}
     
    // Output: <title>Acme</title>
[/code]

##### `template`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#template)

`title.template` 은 **하위** 경로 세그먼트에서 정의된 `title` 에 접두사나 접미사를 추가하는 데 사용할 수 있습니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: {
        template: '%s | Acme',
        default: 'Acme', // a default is required when creating a template
      },
    }
[/code]

app/about/page.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: 'About',
    }
     
    // Output: <title>About | Acme</title>
[/code]

> **알아두면 좋은 사항**
> 
>   * `title.template` 는 **하위** 경로 세그먼트에 적용되며 정의된 세그먼트에는 적용되지 않습니다. 따라서:
>     * `title.template` 를 추가할 때 `title.default` 가 **필수** 입니다.
>     * `layout.js` 에 정의된 `title.template` 는 동일한 경로 세그먼트의 `page.js` 에 정의된 `title` 에 적용되지 않습니다.
>     * `page.js` 에 정의된 `title.template` 는 페이지가 항상 말단 세그먼트이므로 효과가 없습니다.
>   * 경로에서 `title` 이나 `title.default` 를 정의하지 않으면 `title.template` 는 **효과가 없습니다**.
> 


##### `absolute`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#absolute)

`title.absolute` 는 상위 세그먼트에 설정된 `title.template` 를 **무시하는** 제목을 제공하는 데 사용할 수 있습니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: {
        template: '%s | Acme',
      },
    }
[/code]

app/about/page.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: {
        absolute: 'About',
      },
    }
     
    // Output: <title>About</title>
[/code]

> **알아두면 좋은 사항**
> 
>   * `layout.js`
>     * `title` (문자열)과 `title.default` 는 자체 `title` 을 정의하지 않은 하위 세그먼트의 기본 제목을 정의합니다. 존재한다면 가장 가까운 상위 세그먼트의 `title.template` 를 보완합니다.
>     * `title.absolute` 는 하위 세그먼트의 기본 제목을 정의합니다. 상위 세그먼트의 `title.template` 를 무시합니다.
>     * `title.template` 는 하위 세그먼트를 위한 새로운 제목 템플릿을 정의합니다.
>   * `page.js`
>     * 페이지가 자체 제목을 정의하지 않으면 가장 가까운 상위의 해석된 제목을 사용합니다.
>     * `title` (문자열)은 경로의 제목을 정의하며, 존재한다면 가장 가까운 상위 세그먼트의 `title.template` 를 보완합니다.
>     * `title.absolute` 는 경로의 제목을 정의하며 상위 세그먼트의 `title.template` 를 무시합니다.
>     * 페이지는 항상 경로의 말단 세그먼트이므로 `page.js` 의 `title.template` 는 효과가 없습니다.
> 


### `description`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#description)

layout.js | page.js
[code]
    export const metadata = {
      description: 'The React Framework for the Web',
    }
[/code]

<head> output
[code]
    <meta name="description" content="The React Framework for the Web" />
[/code]

### 기타 필드[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#other-fields)

layout.js | page.js
[code]
    export const metadata = {
      generator: 'Next.js',
      applicationName: 'Next.js',
      referrer: 'origin-when-cross-origin',
      keywords: ['Next.js', 'React', 'JavaScript'],
      authors: [{ name: 'Seb' }, { name: 'Josh', url: 'https://nextjs.org' }],
      creator: 'Jiachi Liu',
      publisher: 'Sebastian Markbåge',
      formatDetection: {
        email: false,
        address: false,
        telephone: false,
      },
    }
[/code]

<head> output
[code]
    <meta name="application-name" content="Next.js" />
    <meta name="author" content="Seb" />
    <link rel="author" href="https://nextjs.org" />
[/code]

<meta name="author" content="Josh" />
    <meta name="generator" content="Next.js" />
    <meta name="keywords" content="Next.js,React,JavaScript" />
    <meta name="referrer" content="origin-when-cross-origin" />
    <meta name="color-scheme" content="dark" />
    <meta name="creator" content="Jiachi Liu" />
    <meta name="publisher" content="Sebastian Markbåge" />
    <meta name="format-detection" content="telephone=no, address=no, email=no" />
[/code]

#### `metadataBase`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadatabase)

`metadataBase`는 완전한 URL이 필요한 `metadata` 필드에 사용할 기본 URL 접두사를 설정하기 위한 편의 옵션입니다.

  * `metadataBase`를 사용하면 **현재 라우트 세그먼트 및 그 하위**에서 정의된 URL 기반 `metadata` 필드가 원래 필요했던 절대 URL 대신 **상대 경로**를 사용할 수 있습니다.
  * 필드가 제공한 상대 경로는 `metadataBase`와 합쳐져 완전한 URL이 됩니다.



layout.js | page.js
[code]
    export const metadata = {
      metadataBase: new URL('https://acme.com'),
      alternates: {
        canonical: '/',
        languages: {
          'en-US': '/en-US',
          'de-DE': '/de-DE',
        },
      },
      openGraph: {
        images: '/og-image.png',
      },
    }
[/code]

<head> output
[code]
    <link rel="canonical" href="https://acme.com" />
    <link rel="alternate" hreflang="en-US" href="https://acme.com/en-US" />
    <link rel="alternate" hreflang="de-DE" href="https://acme.com/de-DE" />
    <meta property="og:image" content="https://acme.com/og-image.png" />
[/code]

> **알아두면 좋아요** :
> 
>   * `metadataBase`는 일반적으로 루트 `app/layout.js`에서 설정해 모든 라우트의 URL 기반 `metadata` 필드에 적용합니다.
>   * 절대 URL이 필요한 모든 URL 기반 `metadata` 필드는 `metadataBase` 옵션으로 구성할 수 있습니다.
>   * `metadataBase`는 `https://app.acme.com`과 같은 서브도메인이나 `https://acme.com/start/from/here`와 같은 기본 경로를 포함할 수 있습니다.
>   * `metadata` 필드가 절대 URL을 제공하면 `metadataBase`는 무시됩니다.
>   * `metadataBase` 없이 URL 기반 `metadata` 필드에서 상대 경로를 사용하면 빌드 오류가 발생합니다.
>   * Next.js는 `metadataBase`(예: `https://acme.com/`)와 상대 필드(예: `/path`) 사이의 중복 슬래시를 단일 슬래시(예: `https://acme.com/path`)로 정규화합니다.
> 


#### URL Composition[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#url-composition)

URL 구성은 기본 디렉터리 탐색 규칙보다 개발자의 의도를 우선시합니다.

  * `metadataBase`와 `metadata` 필드 사이의 끝 슬래시는 정규화됩니다.
  * 일반적으로 전체 URL 경로를 대체할 수 있는 `metadata` 필드의 “절대” 경로도 “상대” 경로(즉, `metadataBase` 끝에서 시작)로 처리됩니다.



다음과 같은 `metadataBase`가 있다고 가정해봅시다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      metadataBase: new URL('https://acme.com'),
    }
[/code]

위 `metadataBase`를 상속하고 자체 값을 설정하는 모든 `metadata` 필드는 다음과 같이 해석됩니다:

`metadata` field| Resolved URL  
---|---  
`/`| `https://acme.com`  
`./`| `https://acme.com`  
`payments`| `https://acme.com/payments`  
`/payments`| `https://acme.com/payments`  
`./payments`| `https://acme.com/payments`  
`../payments`| `https://acme.com/payments`  
`https://beta.acme.com/payments`| `https://beta.acme.com/payments`  
  
### `openGraph`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#opengraph)

layout.js | page.js
[code]
    export const metadata = {
      openGraph: {
        title: 'Next.js',
        description: 'The React Framework for the Web',
        url: 'https://nextjs.org',
        siteName: 'Next.js',
        images: [
          {
            url: 'https://nextjs.org/og.png', // Must be an absolute URL
            width: 800,
            height: 600,
          },
          {
            url: 'https://nextjs.org/og-alt.png', // Must be an absolute URL
            width: 1800,
            height: 1600,
            alt: 'My custom alt',
          },
        ],
        videos: [
          {
            url: 'https://nextjs.org/video.mp4', // Must be an absolute URL
            width: 800,
            height: 600,
          },
        ],
        audio: [
          {
            url: 'https://nextjs.org/audio.mp3', // Must be an absolute URL
          },
        ],
        locale: 'en_US',
        type: 'website',
      },
    }
[/code]

<head> output
[code]
    <meta property="og:title" content="Next.js" />
    <meta property="og:description" content="The React Framework for the Web" />
    <meta property="og:url" content="https://nextjs.org/" />
    <meta property="og:site_name" content="Next.js" />
    <meta property="og:locale" content="en_US" />
    <meta property="og:image" content="https://nextjs.org/og.png" />
    <meta property="og:image:width" content="800" />
    <meta property="og:image:height" content="600" />
    <meta property="og:image" content="https://nextjs.org/og-alt.png" />
    <meta property="og:image:width" content="1800" />
    <meta property="og:image:height" content="1600" />
    <meta property="og:image:alt" content="My custom alt" />
    <meta property="og:video" content="https://nextjs.org/video.mp4" />
    <meta property="og:video:width" content="800" />
    <meta property="og:video:height" content="600" />
    <meta property="og:audio" content="https://nextjs.org/audio.mp3" />
    <meta property="og:type" content="website" />
[/code]

layout.js | page.js
[code]
    export const metadata = {
      openGraph: {
        title: 'Next.js',
        description: 'The React Framework for the Web',
        type: 'article',
        publishedTime: '2023-01-01T00:00:00.000Z',
        authors: ['Seb', 'Josh'],
      },
    }
[/code]

<head> output
[code]
    <meta property="og:title" content="Next.js" />
    <meta property="og:description" content="The React Framework for the Web" />
    <meta property="og:type" content="article" />
    <meta property="article:published_time" content="2023-01-01T00:00:00.000Z" />
    <meta property="article:author" content="Seb" />
    <meta property="article:author" content="Josh" />
[/code]

> **알아두면 좋아요** :
> 
>   * Open Graph 이미지를 위해 [파일 기반 Metadata API](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif)를 사용하면 더 편리할 수 있습니다. 설정 내보내기와 실제 파일을 동기화하는 대신 파일 기반 API가 올바른 메타데이터를 자동으로 생성합니다.
> 


### `robots`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#robots)

layout.tsx | page.tsx
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      robots: {
        index: true,
        follow: true,
        nocache: false,
        googleBot: {
          index: true,
          follow: true,
          noimageindex: false,
          'max-video-preview': -1,
          'max-image-preview': 'large',
          'max-snippet': -1,
        },
      },
    }
[/code]

<head> output
[code]
    <meta name="robots" content="index, follow" />
    <meta
      name="googlebot"
      content="index, follow, max-video-preview:-1, max-image-preview:large, max-snippet:-1"
    />
[/code]

### `icons`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#icons)

> **알아두면 좋아요** : 가능하다면 아이콘에도 [파일 기반 Metadata API](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png)를 사용하는 것을 권장합니다. 설정 내보내기와 실제 파일을 동기화하지 않아도 파일 기반 API가 올바른 메타데이터를 자동으로 생성합니다.

layout.js | page.js
[code]
    export const metadata = {
      icons: {
        icon: '/icon.png',
        shortcut: '/shortcut-icon.png',
        apple: '/apple-icon.png',
        other: {
          rel: 'apple-touch-icon-precomposed',
          url: '/apple-touch-icon-precomposed.png',
        },
      },
    }
[/code]

<head> output
[code]
    <link rel="shortcut icon" href="/shortcut-icon.png" />
    <link rel="icon" href="/icon.png" />
    <link rel="apple-touch-icon" href="/apple-icon.png" />
    <link
      rel="apple-touch-icon-precomposed"
      href="/apple-touch-icon-precomposed.png"
    />
[/code]

layout.js | page.js
[code]
    export const metadata = {
      icons: {
        icon: [
          { url: '/icon.png' },
          new URL('/icon.png', 'https://example.com'),
          { url: '/icon-dark.png', media: '(prefers-color-scheme: dark)' },
        ],
        shortcut: ['/shortcut-icon.png'],
        apple: [
          { url: '/apple-icon.png' },
          { url: '/apple-icon-x3.png', sizes: '180x180', type: 'image/png' },
        ],
        other: [
          {
            rel: 'apple-touch-icon-precomposed',
            url: '/apple-touch-icon-precomposed.png',
          },
        ],
      },
    }
[/code]

<head> output
[code]
    <link rel="shortcut icon" href="/shortcut-icon.png" />
    <link rel="icon" href="/icon.png" />
    <link rel="icon" href="https://example.com/icon.png" />
    <link rel="icon" href="/icon-dark.png" media="(prefers-color-scheme: dark)" />
    <link rel="apple-touch-icon" href="/apple-icon.png" />
    <link
      rel="apple-touch-icon-precomposed"
      href="/apple-touch-icon-precomposed.png"
    />
    <link
      rel="apple-touch-icon"
      href="/apple-icon-x3.png"
      sizes="180x180"
      type="image/png"
    />
[/code]

> **알아두면 좋아요** : `msapplication-*` 메타 태그는 Chromium 기반 Microsoft Edge에서 더 이상 지원되지 않으므로 사용할 필요가 없습니다.

### `themeColor`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#themecolor)

> **사용 중단됨** : Next.js 14부터 `metadata`의 `themeColor` 옵션은 사용 중단되었습니다. 대신 [`viewport` 구성](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)을 사용하세요.

### `colorScheme`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#colorscheme)

> **사용 중단됨** : Next.js 14부터 `metadata`의 `colorScheme` 옵션은 사용 중단되었습니다. 대신 [`viewport` 구성](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)을 사용하세요.

### `manifest`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#manifest)

[Web Application Manifest 명세](https://developer.mozilla.org/docs/Web/Manifest)에 정의된 웹 애플리케이션 매니페스트입니다.

layout.js | page.js
[code]
    export const metadata = {
      manifest: 'https://nextjs.org/manifest.json',
    }
[/code]

<head> output
[code]
    <link rel="manifest" href="https://nextjs.org/manifest.json" />
[/code]

### `twitter`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#twitter)

Twitter 명세는 (놀랍게도) X(구 Twitter) 외의 곳에서도 사용됩니다.

[Twitter Card markup reference](https://developer.x.com/en/docs/twitter-for-websites/cards/overview/markup)에 대해 더 알아보세요.

layout.js | page.js
[code]
    export const metadata = {
      twitter: {
        card: 'summary_large_image',
        title: 'Next.js',
        description: 'The React Framework for the Web',
        siteId: '1467726470533754880',
        creator: '@nextjs',
        creatorId: '1467726470533754880',
        images: ['https://nextjs.org/og.png'], // Must be an absolute URL
      },
    }
[/code]

<head> output
[code]
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site:id" content="1467726470533754880" />
    <meta name="twitter:creator" content="@nextjs" />
    <meta name="twitter:creator:id" content="1467726470533754880" />
    <meta name="twitter:title" content="Next.js" />

<meta name="twitter:description" content="The React Framework for the Web" />
    <meta name="twitter:image" content="https://nextjs.org/og.png" />
[/code]

layout.js | page.js
[code]
    export const metadata = {
      twitter: {
        card: 'app',
        title: 'Next.js',
        description: 'The React Framework for the Web',
        siteId: '1467726470533754880',
        creator: '@nextjs',
        creatorId: '1467726470533754880',
        images: {
          url: 'https://nextjs.org/og.png',
          alt: 'Next.js Logo',
        },
        app: {
          name: 'twitter_app',
          id: {
            iphone: 'twitter_app://iphone',
            ipad: 'twitter_app://ipad',
            googleplay: 'twitter_app://googleplay',
          },
          url: {
            iphone: 'https://iphone_url',
            ipad: 'https://ipad_url',
          },
        },
      },
    }
[/code]

<head> 출력
[code]
    <meta name="twitter:site:id" content="1467726470533754880" />
    <meta name="twitter:creator" content="@nextjs" />
    <meta name="twitter:creator:id" content="1467726470533754880" />
    <meta name="twitter:title" content="Next.js" />
    <meta name="twitter:description" content="The React Framework for the Web" />
    <meta name="twitter:card" content="app" />
    <meta name="twitter:image" content="https://nextjs.org/og.png" />
    <meta name="twitter:image:alt" content="Next.js Logo" />
    <meta name="twitter:app:name:iphone" content="twitter_app" />
    <meta name="twitter:app:id:iphone" content="twitter_app://iphone" />
    <meta name="twitter:app:id:ipad" content="twitter_app://ipad" />
    <meta name="twitter:app:id:googleplay" content="twitter_app://googleplay" />
    <meta name="twitter:app:url:iphone" content="https://iphone_url" />
    <meta name="twitter:app:url:ipad" content="https://ipad_url" />
    <meta name="twitter:app:name:ipad" content="twitter_app" />
    <meta name="twitter:app:name:googleplay" content="twitter_app" />
[/code]

### `viewport`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#viewport)

> **사용 중단 안내** : Next.js 14부터 `metadata`의 `viewport` 옵션은 사용 중단되었습니다. 대신 [`viewport` 구성](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)을 사용하세요.

### `verification`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#verification)

layout.js | page.js
[code]
    export const metadata = {
      verification: {
        google: 'google',
        yandex: 'yandex',
        yahoo: 'yahoo',
        other: {
          me: ['my-email', 'my-link'],
        },
      },
    }
[/code]

<head> 출력
[code]
    <meta name="google-site-verification" content="google" />
    <meta name="y_key" content="yahoo" />
    <meta name="yandex-verification" content="yandex" />
    <meta name="me" content="my-email" />
    <meta name="me" content="my-link" />
[/code]

### `appleWebApp`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#applewebapp)

layout.js | page.js
[code]
    export const metadata = {
      itunes: {
        appId: 'myAppStoreID',
        appArgument: 'myAppArgument',
      },
      appleWebApp: {
        title: 'Apple Web App',
        statusBarStyle: 'black-translucent',
        startupImage: [
          '/assets/startup/apple-touch-startup-image-768x1004.png',
          {
            url: '/assets/startup/apple-touch-startup-image-1536x2008.png',
            media: '(device-width: 768px) and (device-height: 1024px)',
          },
        ],
      },
    }
[/code]

<head> 출력
[code]
    <meta
      name="apple-itunes-app"
      content="app-id=myAppStoreID, app-argument=myAppArgument"
    />
    <meta name="mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-title" content="Apple Web App" />
    <link
      href="/assets/startup/apple-touch-startup-image-768x1004.png"
      rel="apple-touch-startup-image"
    />
    <link
      href="/assets/startup/apple-touch-startup-image-1536x2008.png"
      media="(device-width: 768px) and (device-height: 1024px)"
      rel="apple-touch-startup-image"
    />
    <meta
      name="apple-mobile-web-app-status-bar-style"
      content="black-translucent"
    />
[/code]

### `alternates`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#alternates)

layout.js | page.js
[code]
    export const metadata = {
      alternates: {
        canonical: 'https://nextjs.org',
        languages: {
          'en-US': 'https://nextjs.org/en-US',
          'de-DE': 'https://nextjs.org/de-DE',
        },
        media: {
          'only screen and (max-width: 600px)': 'https://nextjs.org/mobile',
        },
        types: {
          'application/rss+xml': 'https://nextjs.org/rss',
        },
      },
    }
[/code]

<head> 출력
[code]
    <link rel="canonical" href="https://nextjs.org" />
    <link rel="alternate" hreflang="en-US" href="https://nextjs.org/en-US" />
    <link rel="alternate" hreflang="de-DE" href="https://nextjs.org/de-DE" />
    <link
      rel="alternate"
      media="only screen and (max-width: 600px)"
      href="https://nextjs.org/mobile"
    />
    <link
      rel="alternate"
      type="application/rss+xml"
      href="https://nextjs.org/rss"
    />
[/code]

### `appLinks`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#applinks)

layout.js | page.js
[code]
    export const metadata = {
      appLinks: {
        ios: {
          url: 'https://nextjs.org/ios',
          app_store_id: 'app_store_id',
        },
        android: {
          package: 'com.example.android/package',
          app_name: 'app_name_android',
        },
        web: {
          url: 'https://nextjs.org/web',
          should_fallback: true,
        },
      },
    }
[/code]

<head> 출력
[code]
    <meta property="al:ios:url" content="https://nextjs.org/ios" />
    <meta property="al:ios:app_store_id" content="app_store_id" />
    <meta property="al:android:package" content="com.example.android/package" />
    <meta property="al:android:app_name" content="app_name_android" />
    <meta property="al:web:url" content="https://nextjs.org/web" />
    <meta property="al:web:should_fallback" content="true" />
[/code]

### `archives`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#archives)

역사적으로 중요한 기록, 문서 또는 기타 자료 모음을 설명합니다([출처](https://www.w3.org/TR/2011/WD-html5-20110113/links.html#rel-archives)).

layout.js | page.js
[code]
    export const metadata = {
      archives: ['https://nextjs.org/13'],
    }
[/code]

<head> 출력
[code]
    <link rel="archives" href="https://nextjs.org/13" />
[/code]

### `assets`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#assets)

layout.js | page.js
[code]
    export const metadata = {
      assets: ['https://nextjs.org/assets'],
    }
[/code]

<head> 출력
[code]
    <link rel="assets" href="https://nextjs.org/assets" />
[/code]

### `bookmarks`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#bookmarks)

layout.js | page.js
[code]
    export const metadata = {
      bookmarks: ['https://nextjs.org/13'],
    }
[/code]

<head> 출력
[code]
    <link rel="bookmarks" href="https://nextjs.org/13" />
[/code]

### `category`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#category)

layout.js | page.js
[code]
    export const metadata = {
      category: 'technology',
    }
[/code]

<head> 출력
[code]
    <meta name="category" content="technology" />
[/code]

### `facebook`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#facebook)

특정 Facebook 소셜 플러그인을 위해 웹페이지에 Facebook 앱 또는 Facebook 계정을 연결할 수 있습니다. [Facebook 문서](https://developers.facebook.com/docs/plugins/comments/#moderation-setup-instructions)

> **알아두면 좋아요** : appId와 admins 중 하나만 지정할 수 있습니다.

layout.js | page.js
[code]
    export const metadata = {
      facebook: {
        appId: '12345678',
      },
    }
[/code]

<head> 출력
[code]
    <meta property="fb:app_id" content="12345678" />
[/code]

layout.js | page.js
[code]
    export const metadata = {
      facebook: {
        admins: '12345678',
      },
    }
[/code]

<head> 출력
[code]
    <meta property="fb:admins" content="12345678" />
[/code]

여러 개의 fb:admins 메타 태그를 생성하려면 배열 값을 사용할 수 있습니다.

layout.js | page.js
[code]
    export const metadata = {
      facebook: {
        admins: ['12345678', '87654321'],
      },
    }
[/code]

<head> 출력
[code]
    <meta property="fb:admins" content="12345678" />
    <meta property="fb:admins" content="87654321" />
[/code]

### `pinterest`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#pinterest)

웹페이지에서 [Pinterest 리치 핀](https://developers.pinterest.com/docs/web-features/rich-pins-overview/)을 활성화하거나 비활성화할 수 있습니다.

layout.js | page.js
[code]
    export const metadata = {
      pinterest: {
        richPin: true,
      },
    }
[/code]

<head> 출력
[code]
    <meta name="pinterest-rich-pin" content="true" />
[/code]

### `other`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#other)

모든 메타데이터 옵션은 기본 제공 기능으로 처리해야 합니다. 그러나 사이트 특화 메타데이터 태그나 새로 출시된 메타데이터 태그가 있을 수 있습니다. `other` 옵션을 사용하면 맞춤형 메타데이터 태그를 렌더링할 수 있습니다.

layout.js | page.js
[code]
    export const metadata = {
      other: {
        custom: 'meta',
      },
    }
[/code]

<head> 출력
[code]
    <meta name="custom" content="meta" />
[/code]

같은 키의 메타 태그를 여러 개 생성하려면 배열 값을 사용할 수 있습니다.

layout.js | page.js
[code]
    export const metadata = {
      other: {
        custom: ['meta1', 'meta2'],
      },
    }
[/code]

<head> 출력
[code]
    <meta name="custom" content="meta1" /> <meta name="custom" content="meta2" />
[/code]

### Types[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#types)

`Metadata` 타입을 사용하여 메타데이터에 타입 안전성을 추가할 수 있습니다. IDE에서 [기본 제공 TypeScript 플러그인](https://nextjs.org/docs/app/api-reference/config/typescript)을 사용 중이라면 타입을 수동으로 추가할 필요는 없지만, 원한다면 명시적으로 추가할 수 있습니다.

#### `metadata` object[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-object)

layout.tsx | page.tsx
[code]
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: 'Next.js',
    }
[/code]

#### `generateMetadata` function[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#generatemetadata-function-1)

##### Regular function[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#regular-function)

layout.tsx | page.tsx
[code]
    import type { Metadata } from 'next'
     
    export function generateMetadata(): Metadata {
      return {
        title: 'Next.js',
      }
    }
[/code]

##### Async function[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#async-function)

layout.tsx | page.tsx
[code]
    import type { Metadata } from 'next'
     
    export async function generateMetadata(): Promise<Metadata> {
      return {
        title: 'Next.js',
      }
    }
[/code]

##### With segment props[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#with-segment-props)

layout.tsx | page.tsx
[code]
    import type { Metadata } from 'next'
     
    type Props = {
      params: Promise<{ id: string }>
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }
     
    export function generateMetadata({ params, searchParams }: Props): Metadata {
      return {
        title: 'Next.js',
      }
    }
[/code]

export default function Page({ params, searchParams }: Props) {}
[/code]

##### 상위 Metadata와 함께[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#with-parent-metadata)

layout.tsx | page.tsx
[code]
    import type { Metadata, ResolvingMetadata } from 'next'
     
    export async function generateMetadata(
      { params, searchParams }: Props,
      parent: ResolvingMetadata
    ): Promise<Metadata> {
      return {
        title: 'Next.js',
      }
    }
[/code]

##### JavaScript 프로젝트[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#javascript-projects)

JavaScript 프로젝트에서는 JSDoc을 사용해 타입 안정성을 추가할 수 있습니다.

layout.js | page.js
[code]
    /** @type {import("next").Metadata} */
    export const metadata = {
      title: 'Next.js',
    }
[/code]

### 지원되지 않는 Metadata[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#unsupported-metadata)

다음 Metadata 타입은 현재 기본 지원이 없습니다. 하지만 레이아웃이나 페이지 자체에서 직접 렌더링할 수 있습니다.

Metadata| 권장 사항  
---|---  
`<meta http-equiv="...">`| [`redirect()`](https://nextjs.org/docs/app/api-reference/functions/redirect), [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#nextresponse), [Security Headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)를 통해 적절한 HTTP 헤더를 사용하세요.  
`<base>`| 레이아웃이나 페이지에서 직접 태그를 렌더링하세요.  
`<noscript>`| 레이아웃이나 페이지에서 직접 태그를 렌더링하세요.  
`<style>`| [Next.js 스타일링](https://nextjs.org/docs/app/getting-started/css)에 대해 자세히 알아보세요.  
`<script>`| [스크립트 사용법](https://nextjs.org/docs/app/guides/scripts)에 대해 자세히 알아보세요.  
`<link rel="stylesheet" />`| 레이아웃이나 페이지에서 스타일시트를 직접 `import` 하세요.  
`<link rel="preload />`| [ReactDOM preload 메서드](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#link-relpreload)를 사용하세요.  
`<link rel="preconnect" />`| [ReactDOM preconnect 메서드](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#link-relpreconnect)를 사용하세요.  
`<link rel="dns-prefetch" />`| [ReactDOM prefetchDNS 메서드](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#link-reldns-prefetch)를 사용하세요.  
  
### 리소스 힌트[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#resource-hints)

`<link>` 요소에는 브라우저가 외부 리소스가 필요할 가능성을 알려줄 수 있는 여러 `rel` 키워드가 있습니다. 브라우저는 키워드에 따라 사전 로드 최적화를 적용합니다.

Metadata API가 이러한 힌트를 직접 지원하지는 않지만, 새로운 [`ReactDOM` 메서드](https://github.com/facebook/react/pull/26237)를 사용하면 문서 `<head>`에 안전하게 삽입할 수 있습니다.

app/preload-resources.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import ReactDOM from 'react-dom'
     
    export function PreloadResources() {
      ReactDOM.preload('...', { as: '...' })
      ReactDOM.preconnect('...', { crossOrigin: '...' })
      ReactDOM.prefetchDNS('...')
     
      return '...'
    }
[/code]

#### `<link rel="preload">`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#link-relpreload)

페이지 렌더링(브라우저) 라이프사이클 초기에 리소스를 미리 로드합니다. [MDN 문서](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/preload).
[code] 
    ReactDOM.preload(href: string, options: { as: string })
[/code]

<head> 출력
[code]
    <link rel="preload" href="..." as="..." />
[/code]

##### `<link rel="preconnect">`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#link-relpreconnect)

오리진에 대한 연결을 선제적으로 초기화합니다. [MDN 문서](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/preconnect).
[code] 
    ReactDOM.preconnect(href: string, options?: { crossOrigin?: string })
[/code]

<head> 출력
[code]
    <link rel="preconnect" href="..." crossorigin />
[/code]

#### `<link rel="dns-prefetch">`[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#link-reldns-prefetch)

리소스 요청 전에 도메인 이름을 미리 확인하려 시도합니다. [MDN 문서](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/dns-prefetch).
[code] 
    ReactDOM.prefetchDNS(href: string)
[/code]

<head> 출력
[code]
    <link rel="dns-prefetch" href="..." />
[/code]

> **알아두면 좋아요** :
> 
>   * 이러한 메서드는 현재 클라이언트 컴포넌트에서만 지원되며, 초기 페이지 로드 시에도 서버 사이드 렌더링됩니다.
>   * `next/font`, `next/image`, `next/script`와 같은 Next.js 내장 기능은 관련 리소스 힌트를 자동으로 처리합니다.
> 


## 동작[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#behavior)

### 기본 필드[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#default-fields)

다음 두 개의 기본 `meta` 태그는 라우트가 Metadata를 정의하지 않아도 항상 추가됩니다.

  * [meta charset 태그](https://developer.mozilla.org/docs/Web/HTML/Element/meta#attr-charset)는 웹사이트의 문자 인코딩을 설정합니다.
  * [meta viewport 태그](https://developer.mozilla.org/docs/Web/HTML/Viewport_meta_tag)는 디바이스별로 조정할 수 있도록 뷰포트 너비와 스케일을 설정합니다.


[code] 
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
[/code]

> **알아두면 좋아요** : 기본 [`viewport`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#viewport) meta 태그를 덮어쓸 수 있습니다.

### 스트리밍 Metadata[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata)

스트리밍 Metadata를 사용하면 Next.js가 `generateMetadata`가 완료되기 전에 초기 UI를 브라우저로 렌더링하고 전송할 수 있습니다.

`generateMetadata`가 resolve되면 결과 Metadata 태그가 `<body>` 태그에 추가됩니다. JavaScript를 실행하고 전체 DOM을 검사하는 봇(`Googlebot` 등)에서 Metadata가 올바르게 해석됨을 확인했습니다.

JavaScript를 실행할 수 없는 **HTML 제한 봇**(`facebookexternalhit` 등)의 경우 Metadata는 계속해서 페이지 렌더링을 차단합니다. 이때 Metadata는 `<head>` 태그에서 사용할 수 있습니다.

Next.js는 User Agent 헤더를 확인하여 **HTML 제한 봇**을 자동으로 감지합니다. Next.js 설정 파일에서 [`htmlLimitedBots`](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots) 옵션을 사용하여 기본 [User Agent 목록](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts)을 재정의할 수 있습니다.

스트리밍 Metadata를 완전히 비활성화하려면:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      htmlLimitedBots: /.*/,
    }
     
    export default config
[/code]

스트리밍 Metadata는 [TTFB](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte)를 줄여 체감 성능을 개선하고 [LCP](https://developer.mozilla.org/docs/Glossary/Largest_contentful_paint)을 줄이는 데 도움을 줄 수 있습니다.

`htmlLimitedBots`를 재정의하면 응답 시간이 길어질 수 있습니다. 스트리밍 Metadata는 고급 기능이며 대부분의 경우 기본 설정이면 충분합니다.

### Cache 컴포넌트와 함께 사용할 때[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#with-cache-components)

[Cache 컴포넌트](https://nextjs.org/docs/app/getting-started/cache-components)를 활성화하면 `generateMetadata`는 다른 컴포넌트와 동일한 규칙을 따릅니다. Metadata가 런타임 데이터(`cookies()`, `headers()`, `params`, `searchParams`)에 접근하거나 캐시되지 않은 데이터 패칭을 수행하면 요청 시점으로 위임됩니다.

Next.js의 처리 방식은 페이지의 나머지 부분에 따라 달라집니다.

  * **다른 부분도 요청 시점으로 위임하는 경우** : 프리렌더링이 정적 셸을 생성하고 Metadata가 다른 지연 콘텐츠와 함께 스트리밍됩니다.
  * **페이지나 레이아웃이 완전히 프리렌더링 가능한 경우** : 데이터를 캐시할 수 있으면 캐시하거나, 지연 렌더링이 의도적임을 명시적으로 표시해야 합니다.



페이지의 나머지 부분이 완전히 프리렌더링 가능한 상태에서 런타임에 Metadata를 스트리밍하는 경우는 드뭅니다. 이 동작이 의도적임을 보장하기 위해 어떤 페이지나 레이아웃을 처리해야 하는지 알려주는 오류가 발생합니다.

이를 해결하려면 두 가지 옵션이 있습니다. Metadata가 런타임 데이터가 아닌 외부 데이터에 의존한다면 `use cache`를 사용하세요.

app/page.tsx
[code]
    export async function generateMetadata() {
      'use cache'
      const { title, description } = await db.query('site-metadata')
      return { title, description }
    }
[/code]

Metadata가 실제로 런타임 데이터를 필요로 한다면 페이지에 동적 마커 컴포넌트를 추가하세요.

app/page.tsx
[code]
    import { Suspense } from 'react'
    import { cookies } from 'next/headers'
    import { connection } from 'next/server'
     
    export async function generateMetadata() {
      const token = (await cookies()).get('token')?.value
      // ... use token to fetch personalized metadata
      return { title: 'Personalized Title' }
    }
     
    const Connection = async () => {
      await connection()
      return null
    }
     
    async function DynamicMarker() {
      return (
        <Suspense>
          <Connection />
        </Suspense>
      )
    }
     
    export default function Page() {
      // DO NOT place await connection() here
      // doing so prevents the article tag content from
      // being included in the static shell
      return (
        <>
          <article>Static content</article>
          <DynamicMarker />
        </>
      )
    }
[/code]

`DynamicMarker` 컴포넌트는 아무 것도 렌더링하지 않지만 페이지에 의도적인 동적 콘텐츠가 있음을 Next.js에 전달합니다. 이를 Suspense로 감싸면 정적 콘텐츠는 정상적으로 프리렌더링됩니다.

### 순서[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#ordering)

Metadata는 루트 세그먼트에서 최종 `page.js`에 가장 가까운 세그먼트까지 순서대로 평가됩니다. 예:

  1. `app/layout.tsx` (루트 레이아웃)
  2. `app/blog/layout.tsx` (중첩 블로그 레이아웃)
  3. `app/blog/[slug]/page.tsx` (블로그 페이지)



### 병합[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#merging)

[평가 순서](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#ordering)를 따르며, 동일한 라우트의 여러 세그먼트에서 내보낸 Metadata 객체는 **얕게** 병합되어 라우트의 최종 Metadata 출력이 됩니다. 중복 키는 순서에 따라 **교체**됩니다.

이는 [`openGraph`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#opengraph)와 [`robots`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#robots)처럼 중첩 필드를 가지는 Metadata가 이전 세그먼트에서 정의되더라도, 이후 세그먼트에서 동일한 필드를 정의하면 **덮어쓰여** 마지막 세그먼트의 값이 된다는 의미입니다.

#### 필드 덮어쓰기[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#overwriting-fields)

app/layout.js
[code]
    export const metadata = {
      title: 'Acme',
      openGraph: {
        title: 'Acme',
        description: 'Acme is a...',
      },
    }
[/code]

app/blog/page.js
[code]
    export const metadata = {
      title: 'Blog',
      openGraph: {
        title: 'Blog',
      },
    }
     
    // Output:
    // <title>Blog</title>
    // <meta property="og:title" content="Blog" />
[/code]

위 예시에서:

  * `app/layout.js`의 `title`은 `app/blog/page.js`의 `title`로 **교체**됩니다.
  * `app/blog/page.js`가 `openGraph` Metadata를 설정하므로 `app/layout.js`의 모든 `openGraph` 필드가 `app/blog/page.js`에서 **교체**됩니다. `openGraph.description`이 없는 것을 확인하세요.



세그먼트 간에 일부 중첩 필드를 공유하면서 다른 필드만 덮어쓰고 싶다면, 별도의 변수로 분리할 수 있습니다.

app/shared-metadata.js
[code]

export const openGraphImage = { images: ['http://...'] }
[/code]

app/page.js
[code]
    import { openGraphImage } from './shared-metadata'
     
    export const metadata = {
      openGraph: {
        ...openGraphImage,
        title: 'Home',
      },
    }
[/code]

app/about/page.js
[code]
    import { openGraphImage } from '../shared-metadata'
     
    export const metadata = {
      openGraph: {
        ...openGraphImage,
        title: 'About',
      },
    }
[/code]

위 예제에서는 OG 이미지가 `app/layout.js`와 `app/about/page.js` 사이에서 공유되지만 제목은 서로 다릅니다.

#### 필드 상속[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#inheriting-fields)

app/layout.js
[code]
    export const metadata = {
      title: 'Acme',
      openGraph: {
        title: 'Acme',
        description: 'Acme is a...',
      },
    }
[/code]

app/about/page.js
[code]
    export const metadata = {
      title: 'About',
    }
     
    // Output:
    // <title>About</title>
    // <meta property="og:title" content="Acme" />
    // <meta property="og:description" content="Acme is a..." />
[/code]

**참고**

  * `app/layout.js`의 `title`은 `app/about/page.js`의 `title`로 **대체**됩니다.
  * `app/about/page.js`가 `openGraph` 메타데이터를 설정하지 않으므로 `app/layout.js`의 모든 `openGraph` 필드는 `app/about/page.js`에서 **상속**됩니다.



## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#version-history)

Version| Changes  
---|---  
`v15.2.0`| `generateMetadata`에 스트리밍 지원이 도입되었습니다.  
`v13.2.0`| [`viewport` 설정](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)을 사용하도록 `viewport`, `themeColor`, `colorScheme`이 사용 중단되었습니다.  
`v13.2.0`| `metadata`와 `generateMetadata`가 도입되었습니다.  
  
## 다음 단계

메타데이터 API 옵션 전체를 확인하세요.

### [Metadata Files메타데이터 파일 규칙에 대한 API 문서입니다.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)### [generateViewportgenerateViewport 함수에 대한 API 참조입니다.](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)### [Cache Components정적 렌더링과 동적 렌더링의 장점을 결합하는 방법을 알아보세요.](https://nextjs.org/docs/app/getting-started/cache-components)### [cacheComponentsNext.js에서 `cacheComponents` 플래그를 활성화하는 방법을 알아보세요.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)

도움이 되었나요?

지원됨.

전송
