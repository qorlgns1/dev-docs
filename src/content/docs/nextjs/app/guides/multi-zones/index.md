---
title: '가이드: 멀티 존'
description: '마지막 업데이트: 2026년 2월 20일'
---

# 가이드: 멀티 존 | Next.js

Source URL: https://nextjs.org/docs/app/guides/multi-zones

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)멀티 존

Copy page

# Multi-zones와 Next.js로 마이크로 프론트엔드를 구축하는 방법

마지막 업데이트: 2026년 2월 20일

Examples

  * [With Zones](https://github.com/vercel/next.js/tree/canary/examples/with-zones)



멀티 존은 하나의 도메인에 있는 대형 애플리케이션을 경로 집합별로 서비스하는 더 작은 Next.js 애플리케이션으로 분리하는 마이크로 프론트엔드 접근 방식입니다. 애플리케이션의 다른 페이지들과 연관성이 낮은 페이지 묶음이 있을 때 유용합니다. 해당 페이지를 별도의 존(즉, 별도 애플리케이션)으로 이동하면 각 애플리케이션 크기를 줄여 빌드 시간을 개선하고 특정 존에만 필요한 코드를 제거할 수 있습니다. 애플리케이션이 분리되어 있으므로, 멀티 존은 같은 도메인에 있는 다른 애플리케이션이 원하는 프레임워크를 사용하도록 허용하기도 합니다.

예를 들어 다음과 같은 페이지 모음을 분리하고 싶다고 가정해 봅시다.

  * `/blog/*` – 모든 블로그 게시물
  * `/dashboard/*` – 사용자가 대시보드에 로그인했을 때의 모든 페이지
  * `/*` – 다른 존에서 다루지 않는 나머지 웹사이트



멀티 존을 지원하면 동일한 도메인에서 사용자에게 동일하게 보이도록 세 개의 애플리케이션을 서비스하되, 각 애플리케이션을 독립적으로 개발 및 배포할 수 있습니다.

같은 존 내 페이지 간 이동은 페이지를 다시 로드하지 않는 소프트 내비게이션으로 수행됩니다. 예를 들어 아래 다이어그램에서 `/`에서 `/products`로 이동하는 경우 소프트 내비게이션이 일어납니다.

`/`에서 `/dashboard`처럼 한 존의 페이지에서 다른 존의 페이지로 이동하면 현재 페이지 리소스를 언로드하고 새 페이지 리소스를 로드하는 하드 내비게이션이 수행됩니다. 자주 함께 방문하는 페이지는 하드 내비게이션을 피하기 위해 같은 존에 두는 것이 좋습니다.

## 존 정의 방법[](https://nextjs.org/docs/app/guides/multi-zones#how-to-define-a-zone)

존은 다른 존의 페이지와 정적 파일과의 충돌을 피하기 위해 [assetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)를 추가로 설정한 일반적인 Next.js 애플리케이션입니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      assetPrefix: '/blog-static',
    }
[/code]

JavaScript 및 CSS 같은 Next.js 에셋은 `assetPrefix`가 앞에 붙어 다른 존의 에셋과 충돌하지 않도록 합니다. 각 존에서 이러한 에셋은 `/assetPrefix/_next/...` 경로 아래에서 제공됩니다.

다른 더 구체적인 존으로 라우팅되지 않은 모든 경로를 처리하는 기본 애플리케이션에는 `assetPrefix`가 필요하지 않습니다.

Next.js 15 이전 버전에서는 정적 에셋을 처리하기 위한 추가 rewrite가 필요할 수 있습니다. Next.js 15에서는 더 이상 필요하지 않습니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      assetPrefix: '/blog-static',
      async rewrites() {
        return {
          beforeFiles: [
            {
              source: '/blog-static/_next/:path+',
              destination: '/_next/:path+',
            },
          ],
        }
      },
    }
[/code]

## 올바른 존으로 요청을 라우팅하는 방법[](https://nextjs.org/docs/app/guides/multi-zones#how-to-route-requests-to-the-right-zone)

멀티 존 구성을 사용하면 서로 다른 애플리케이션에서 서비스하기 때문에 경로를 올바른 존으로 라우팅해야 합니다. 이를 위해서는 어떤 HTTP 프록시도 사용할 수 있으며, Next.js 애플리케이션 하나를 전체 도메인 요청 라우팅에 활용할 수도 있습니다.

Next.js 애플리케이션으로 올바른 존에 라우팅하려면 [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)를 사용할 수 있습니다. 다른 존이 서비스하는 각 경로마다 해당 경로를 그 존의 도메인으로 보내는 rewrite 규칙을 추가하고, 정적 에셋 요청도 rewrite해야 합니다. 예를 들어:

next.config.js
[code]
    async rewrites() {
        return [
            {
                source: '/blog',
                destination: `${process.env.BLOG_DOMAIN}/blog`,
            },
            {
                source: '/blog/:path+',
                destination: `${process.env.BLOG_DOMAIN}/blog/:path+`,
            },
            {
                source: '/blog-static/:path+',
                destination: `${process.env.BLOG_DOMAIN}/blog-static/:path+`,
            }
        ];
    }
[/code]

`destination`은 존이 서비스하는 URL이어야 하며, 스킴과 도메인을 포함해야 합니다. 이는 존의 프로덕션 도메인을 가리키는 것이 일반적이지만, 로컬 개발 중 `localhost`로 요청을 라우팅하는 데에도 사용할 수 있습니다.

> **참고** : URL 경로는 존마다 고유해야 합니다. 예를 들어 두 존이 모두 `/blog`를 서비스하려고 하면 라우팅 충돌이 발생합니다.

### 프록시를 사용한 요청 라우팅[](https://nextjs.org/docs/app/guides/multi-zones#routing-requests-using-proxy)

요청을 [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)로 라우팅하는 것이 지연 시간을 최소화하기 때문에 권장되지만, 라우팅 시 동적 결정을 내려야 하는 경우에는 프록시도 사용할 수 있습니다. 예를 들어 마이그레이션 중 특정 경로를 어디로 라우팅할지 기능 플래그로 결정해야 한다면 프록시를 활용할 수 있습니다.

proxy.js
[code]
    export async function proxy(request) {
      const { pathname, search } = request.nextUrl
      if (pathname === '/your-path' && myFeatureFlag.isEnabled()) {
        return NextResponse.rewrite(`${rewriteDomain}${pathname}${search}`)
      }
    }
[/code]

## 존 간 링크 연결[](https://nextjs.org/docs/app/guides/multi-zones#linking-between-zones)

다른 존의 경로로 연결되는 링크는 Next.js [`<Link>`](https://nextjs.org/docs/pages/api-reference/components/link) 컴포넌트 대신 `a` 태그를 사용해야 합니다. Next.js는 `<Link>` 컴포넌트에 있는 모든 상대 경로를 사전 패치하고 소프트 내비게이션하려고 시도하는데, 이는 존을 넘나드는 경우 작동하지 않기 때문입니다.

## 코드 공유[](https://nextjs.org/docs/app/guides/multi-zones#sharing-code)

여러 존으로 구성된 Next.js 애플리케이션은 어느 저장소에든 위치할 수 있습니다. 다만 코드를 더 쉽게 공유하기 위해 [모노레포](https://en.wikipedia.org/wiki/Monorepo)에 두는 것이 편리할 때가 많습니다. 서로 다른 저장소에 있는 존 간에는 공개 혹은 비공개 NPM 패키지를 통해 코드를 공유할 수도 있습니다.

각 존의 페이지는 서로 다른 시점에 배포될 수 있으므로, 기능 플래그를 활용해 여러 존에서 기능을 동시에 활성화하거나 비활성화하면 도움이 됩니다.

## Server Actions[](https://nextjs.org/docs/app/guides/multi-zones#server-actions)

멀티 존과 함께 [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data)을 사용할 때는 사용자에게 노출되는 도메인이 여러 애플리케이션을 서비스할 수 있으므로, 사용자 도메인 오리진을 명시적으로 허용해야 합니다. `next.config.js` 파일에 다음 내용을 추가하세요:

next.config.js
[code]
    const nextConfig = {
      experimental: {
        serverActions: {
          allowedOrigins: ['your-production-domain.com'],
        },
      },
    }
[/code]

자세한 내용은 [`serverActions.allowedOrigins`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions#allowedorigins)를 참고하세요.

Was this helpful?

supported.

Send
