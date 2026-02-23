---
title: '가이드: 정적 내보내기'
description: 'Next.js는 정적 사이트 또는 Single-Page Application(SPA)으로 시작한 뒤, 나중에 서버가 필요한 기능으로 선택적으로 업그레이드할 수 있게 해 줍니다.'
---

# 가이드: 정적 내보내기 | Next.js

출처 URL: https://nextjs.org/docs/app/guides/static-exports

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)정적 내보내기

페이지 복사

# Next.js 애플리케이션에서 정적 내보내기를 만드는 방법

최종 업데이트 2026년 2월 20일

Next.js는 정적 사이트 또는 Single-Page Application(SPA)으로 시작한 뒤, 나중에 서버가 필요한 기능으로 선택적으로 업그레이드할 수 있게 해 줍니다.

`next build`를 실행하면 Next.js는 라우트마다 HTML 파일을 생성합니다. 순수 SPA를 개별 HTML 파일로 분할함으로써 클라이언트 측에서 불필요한 JavaScript 코드를 불러오지 않아 번들 크기를 줄이고 페이지 로딩 속도를 높일 수 있습니다.

Next.js는 이러한 정적 내보내기를 지원하므로 HTML/CSS/JS 정적 자산을 제공할 수 있는 어떤 웹 서버에도 배포하고 호스팅할 수 있습니다.

## 구성[](https://nextjs.org/docs/app/guides/static-exports#configuration)

정적 내보내기를 활성화하려면 `next.config.js`에서 출력 모드를 변경하세요:

next.config.js
[code]
    /**
     * @type {import('next').NextConfig}
     */
    const nextConfig = {
      output: 'export',
     
      // Optional: Change links `/me` -> `/me/` and emit `/me.html` -> `/me/index.html`
      // trailingSlash: true,
     
      // Optional: Prevent automatic `/me` -> `/me/`, instead preserve `href`
      // skipTrailingSlashRedirect: true,
     
      // Optional: Change the output directory `out` -> `dist`
      // distDir: 'dist',
    }
     
    module.exports = nextConfig
[/code]

`next build`를 실행하면 Next.js가 애플리케이션용 HTML/CSS/JS 자산이 들어 있는 `out` 폴더를 생성합니다.

## 지원되는 기능[](https://nextjs.org/docs/app/guides/static-exports#supported-features)

Next.js의 코어는 정적 내보내기를 지원하도록 설계되어 있습니다.

### 서버 컴포넌트[](https://nextjs.org/docs/app/guides/static-exports#server-components)

정적 내보내기를 생성하기 위해 `next build`를 실행하면 `app` 디렉터리에서 사용하는 서버 컴포넌트가 빌드 시 실행되며, 이는 전통적인 정적 사이트 생성과 유사합니다.

결과 컴포넌트는 초기 페이지 로드를 위한 정적 HTML과 라우트 간 클라이언트 내비게이션을 위한 정적 페이로드로 렌더링됩니다. [동적 서버 함수](https://nextjs.org/docs/app/guides/static-exports#unsupported-features)를 사용하지 않는 한, 정적 내보내기를 사용할 때 서버 컴포넌트를 변경할 필요가 없습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      // This fetch will run on the server during `next build`
      const res = await fetch('https://api.example.com/...')
      const data = await res.json()
     
      return <main>...</main>
    }
[/code]

### 클라이언트 컴포넌트[](https://nextjs.org/docs/app/guides/static-exports#client-components)

클라이언트에서 데이터 패칭을 수행하려면 [SWR](https://github.com/vercel/swr)과 함께 클라이언트 컴포넌트를 사용해 요청을 메모이제이션할 수 있습니다.

app/other/page.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import useSWR from 'swr'
     
    const fetcher = (url: string) => fetch(url).then((r) => r.json())
     
    export default function Page() {
      const { data, error } = useSWR(
        `https://jsonplaceholder.typicode.com/posts/1`,
        fetcher
      )
      if (error) return 'Failed to load'
      if (!data) return 'Loading...'
     
      return data.title
    }
[/code]

라우트 전환이 클라이언트에서 일어나므로 이는 기존 SPA처럼 동작합니다. 예를 들어, 다음 인덱스 라우트는 클라이언트에서 다른 게시물로 이동할 수 있게 해 줍니다:

app/page.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <>
          <h1>Index Page</h1>
          <hr />
          <ul>
            <li>
              <Link href="/post/1">Post 1</Link>
            </li>
            <li>
              <Link href="/post/2">Post 2</Link>
            </li>
          </ul>
        </>
      )
    }
[/code]

### 이미지 최적화[](https://nextjs.org/docs/app/guides/static-exports#image-optimization)

`next/image`를 통한 [이미지 최적화](https://nextjs.org/docs/app/api-reference/components/image)는 `next.config.js`에 사용자 정의 이미지 로더를 정의해 정적 내보내기에서도 사용할 수 있습니다. 예를 들어 Cloudinary 같은 서비스를 통해 이미지를 최적화할 수 있습니다:

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      output: 'export',
      images: {
        loader: 'custom',
        loaderFile: './my-loader.ts',
      },
    }
     
    module.exports = nextConfig
[/code]

이 사용자 정의 로더는 원격 소스에서 이미지를 가져오는 방법을 정의합니다. 예를 들어, 아래 로더는 Cloudinary용 URL을 구성합니다:

my-loader.ts

JavaScriptTypeScript
[code]
    export default function cloudinaryLoader({
      src,
      width,
      quality,
    }: {
      src: string
      width: number
      quality?: number
    }) {
      const params = ['f_auto', 'c_limit', `w_${width}`, `q_${quality || 'auto'}`]
      return `https://res.cloudinary.com/demo/image/upload/${params.join(
        ','
      )}${src}`
    }
[/code]

그런 다음 애플리케이션에서 `next/image`를 사용할 때 Cloudinary의 이미지로 가는 상대 경로를 지정할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return <Image alt="turtles" src="/turtles.jpg" width={300} height={300} />
    }
[/code]

### 라우트 핸들러[](https://nextjs.org/docs/app/guides/static-exports#route-handlers)

`next build`를 실행하면 라우트 핸들러가 정적 응답을 렌더링합니다. 지원되는 HTTP 메서드는 `GET`뿐입니다. 이를 사용하면 캐시된 또는 캐시되지 않은 데이터를 기반으로 정적 HTML, JSON, TXT, 기타 파일을 생성할 수 있습니다. 예:

app/data.json/route.ts

JavaScriptTypeScript
[code]
    export async function GET() {
      return Response.json({ name: 'Lee' })
    }
[/code]

위 `app/data.json/route.ts` 파일은 `next build` 중 정적 파일로 렌더링되어 `{ name: 'Lee' }`가 포함된 `data.json`을 생성합니다.

수신 요청에서 동적 값을 읽어야 한다면 정적 내보내기를 사용할 수 없습니다.

### 브라우저 API[](https://nextjs.org/docs/app/guides/static-exports#browser-apis)

클라이언트 컴포넌트는 `next build` 중 HTML로 미리 렌더링됩니다. `window`, `localStorage`, `navigator` 같은 [웹 API](https://developer.mozilla.org/docs/Web/API)는 서버에서 사용할 수 없으므로, 브라우저에서 실행될 때만 안전하게 접근해야 합니다. 예:
[code]
    'use client';
     
    import { useEffect } from 'react';
     
    export default function ClientComponent() {
      useEffect(() => {
        // You now have access to `window`
        console.log(window.innerHeight);
      }, [])
     
      return ...;
    }
[/code]

## 지원되지 않는 기능[](https://nextjs.org/docs/app/guides/static-exports#unsupported-features)

Node.js 서버가 필요하거나 빌드 과정에서 계산할 수 없는 동적 로직이 필요한 기능은 **지원되지 않습니다**:

  * `dynamicParams: true`인 [동적 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)
  * `generateStaticParams()`가 없는 [동적 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)
  * Request에 의존하는 [라우트 핸들러](https://nextjs.org/docs/app/api-reference/file-conventions/route)
  * [Cookies](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [Rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)
  * [Redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
  * [Headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)
  * [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  * [Incremental Static Regeneration](https://nextjs.org/docs/app/guides/incremental-static-regeneration)
  * 기본 `loader`를 사용하는 [이미지 최적화](https://nextjs.org/docs/app/api-reference/components/image)
  * [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode)
  * [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data)
  * [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes)

이러한 기능을 `next dev`와 함께 사용하려 하면, 루트 레이아웃에서 [`dynamic`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) 옵션을 `error`로 설정했을 때와 유사한 오류가 발생합니다.
[code]
    export const dynamic = 'error'
[/code]

## 배포[](https://nextjs.org/docs/app/guides/static-exports#deploying)

정적 내보내기가 있으면 Next.js를 HTML/CSS/JS 정적 자산을 제공할 수 있는 어떤 웹 서버에도 배포하고 호스팅할 수 있습니다.

`next build`를 실행하면 Next.js는 정적 내보내기를 `out` 폴더에 생성합니다. 예를 들어 다음과 같은 라우트가 있다고 해 봅시다:

  * `/`
  * `/blog/[id]`

`next build` 실행 후 Next.js는 다음 파일을 생성합니다:

  * `/out/index.html`
  * `/out/404.html`
  * `/out/blog/post-1.html`
  * `/out/blog/post-2.html`

Nginx 같은 정적 호스트를 사용한다면, 들어오는 요청을 올바른 파일로 리라이트하도록 구성할 수 있습니다:

nginx.conf
[code]
    server {
      listen 80;
      server_name acme.com;
     
      root /var/www/out;
     
      location / {
          try_files $uri $uri.html $uri/ =404;
      }
     
      # This is necessary when `trailingSlash: false`.
      # You can omit this when `trailingSlash: true`.
      location /blog/ {
          rewrite ^/blog/(.*)$ /blog/$1.html break;
      }
     
      error_page 404 /404.html;
      location = /404.html {
          internal;
      }
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/guides/static-exports#version-history)

Version| Changes  
---|---  
`v14.0.0`| `next export`가 `"output": "export"`로 대체되며 제거되었습니다.  
`v13.4.0`| 앱 라우터(안정판)가 React 서버 컴포넌트와 라우트 핸들러 사용을 포함해 정적 내보내기 지원을 강화했습니다.  
`v13.3.0`| `next export`가 더 이상 사용되지 않으며 `"output": "export"`로 대체되었습니다.  
  
도움이 되었나요?

지원됨.

전송
