---
title: '안내서: Static Exports'
description: 'Next.js는 정적 사이트 또는 단일 페이지 애플리케이션(SPA)으로 시작한 뒤, 서버가 필요한 기능을 나중에 선택적으로 도입할 수 있게 해줍니다.'
---

# 안내서: Static Exports | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/static-exports

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Static Exports

페이지 복사

# Next.js 애플리케이션의 정적 내보내기를 생성하는 방법

마지막 업데이트 2026년 2월 20일

Next.js는 정적 사이트 또는 단일 페이지 애플리케이션(SPA)으로 시작한 뒤, 서버가 필요한 기능을 나중에 선택적으로 도입할 수 있게 해줍니다.

`next build`를 실행하면 Next.js는 라우트마다 HTML 파일을 생성합니다. 순수 SPA를 개별 HTML 파일로 분할하면, Next.js는 클라이언트 측에서 불필요한 JavaScript 코드를 불러오지 않아 번들 크기를 줄이고 더 빠른 페이지 로드를 가능하게 합니다.

Next.js는 이러한 정적 내보내기를 지원하므로 HTML/CSS/JS 정적 에셋을 제공할 수 있는 모든 웹 서버에 배포하고 호스팅할 수 있습니다.

## 구성[](https://nextjs.org/docs/pages/guides/static-exports#configuration)

정적 내보내기를 활성화하려면 `next.config.js` 내부의 출력 모드를 변경합니다:

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

`next build`를 실행하면 Next.js가 애플리케이션용 HTML/CSS/JS 에셋이 포함된 `out` 폴더를 생성합니다.

[`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) 및 [`getStaticPaths`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)를 활용하면 `pages` 디렉터리의 각 페이지(또는 [동적 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)의 경우 더 많은 페이지)에 대한 HTML 파일을 생성할 수 있습니다.

## 지원되는 기능[](https://nextjs.org/docs/pages/guides/static-exports#supported-features-1)

정적 사이트 구축에 필요한 대부분의 핵심 Next.js 기능을 지원합니다. 예를 들면 다음과 같습니다.

  * [`getStaticPaths`를 사용하는 동적 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)
  * `next/link` 사전 로드
  * JavaScript 프리로딩
  * [Dynamic Imports](https://nextjs.org/docs/pages/guides/lazy-loading)
  * 모든 스타일링 옵션(예: CSS Modules, styled-jsx)
  * [클라이언트 측 데이터 패칭](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)
  * [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
  * [`getStaticPaths`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)



### 이미지 최적화[](https://nextjs.org/docs/pages/guides/static-exports#image-optimization)

`next/image`를 통한 [이미지 최적화](https://nextjs.org/docs/app/api-reference/components/image)는 `next.config.js`에서 커스텀 이미지 로더를 정의하면 정적 내보내기와 함께 사용할 수 있습니다. 예를 들어 Cloudinary 같은 서비스를 사용해 이미지를 최적화할 수 있습니다:

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

이 커스텀 로더는 원격 소스에서 이미지를 가져오는 방법을 정의합니다. 예를 들어 다음 로더는 Cloudinary용 URL을 구성합니다:

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

그런 다음 애플리케이션에서 `next/image`를 사용하면서 Cloudinary에 있는 이미지의 상대 경로를 정의할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return <Image alt="turtles" src="/turtles.jpg" width={300} height={300} />
    }
[/code]

## 지원되지 않는 기능[](https://nextjs.org/docs/pages/guides/static-exports#unsupported-features)

Node.js 서버가 필요하거나 빌드 과정에서 계산할 수 없는 동적 로직이 필요한 기능은 **지원되지 않습니다**.

  * [국제화 라우팅](https://nextjs.org/docs/pages/guides/internationalization)
  * [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
  * [Rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites)
  * [Redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)
  * [Headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)
  * [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)
  * [Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)
  * 기본 `loader`를 사용하는 [Image Optimization](https://nextjs.org/docs/pages/api-reference/components/image)
  * [Draft Mode](https://nextjs.org/docs/pages/guides/draft-mode)
  * [`fallback: true`가 있는 `getStaticPaths`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)
  * [`fallback: 'blocking'`이 있는 `getStaticPaths`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-blocking)
  * [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)



## 배포[](https://nextjs.org/docs/pages/guides/static-exports#deploying)

정적 내보내기를 사용하면 HTML/CSS/JS 정적 에셋을 제공할 수 있는 모든 웹 서버에 Next.js를 배포하고 호스팅할 수 있습니다.

`next build`를 실행하면 Next.js는 정적 내보내기를 `out` 폴더에 생성합니다. 예를 들어 다음과 같은 라우트가 있다고 가정해 봅시다.

  * `/`
  * `/blog/[id]`



`next build` 실행 후 Next.js는 다음 파일을 생성합니다.

  * `/out/index.html`
  * `/out/404.html`
  * `/out/blog/post-1.html`
  * `/out/blog/post-2.html`



Nginx와 같은 정적 호스트를 사용하는 경우, 들어오는 요청을 올바른 파일로 리라이트하도록 구성할 수 있습니다.

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

## 버전 기록[](https://nextjs.org/docs/pages/guides/static-exports#version-history)

버전| 변경 사항  
---|---  
`v14.0.0`| `next export`가 `"output": "export"`로 대체되며 제거되었습니다.  
`v13.4.0`| App Router(안정 버전)가 React Server Components와 Route Handlers 사용을 포함해 강화된 정적 내보내기 지원을 추가했습니다.  
`v13.3.0`| `next export`가 더 이상 권장되지 않으며 `"output": "export"`로 대체되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
